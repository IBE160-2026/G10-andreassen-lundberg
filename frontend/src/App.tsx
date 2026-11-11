import { useEffect, useRef, useState } from 'react'
import * as api from './api'
import { basisKey, offerStatus, preserveAbsences, selectionKey, type Selection } from './session'

const labels: Record<string, string> = {
  bestatt: 'Oppfyller scenarioreglene', regelavvik: 'Regelavvik', uavklart: 'Uavklart',
  ikke_vurdert: 'Ikke vurdert', direkte: 'Direkte erstatter', flytting: 'Én flytting', delvis: 'Delvis dekning',
  fullfort: 'Fullført', avbrutt: 'Avbrutt – ufullstendige resultater', utenfor_omfang: 'Ikke kjørt – utenfor omfang',
}
const date = (value: string) => new Intl.DateTimeFormat('nb-NO', {
  timeZone: 'Europe/Oslo', day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit',
}).format(new Date(value))
const number = (value: api.DecimalValue | null) => value === null ? 'Uavklart' : new Intl.NumberFormat('nb-NO', { maximumFractionDigits: 2 }).format(Number(value))
const money = (value: api.DecimalValue | null) => value === null ? 'Uavklart anslag' : `${number(value)} kr`
const rate = (value: api.DecimalValue | null) => value === null ? 'Uavklart' : `${String(value).replace('.', ',')} kr`
const period = (shift: api.Interval) => `${date(shift.start)} – ${date(shift.end)}`
const planSummary = (alternative: api.Alternative) => alternative.plan
  .map(item => `${item.shift_id}: ${item.before.join(', ') || 'Udekket'} → ${item.after.join(', ') || 'Udekket'}`).join('; ')
const errorMessage = (error: unknown) => error instanceof Error ? error.message : 'Handlingen feilet. Prøv igjen.'
type View = 'week' | 'absence' | 'alternatives' | 'detail' | 'choice' | 'data'
type FailedAction = 'startup' | 'simulate' | 'search' | 'previewDataset' | 'loadDataset' | 'explainDifference' | null

function Badge({ status, prefix = 'Kontrollstatus' }: { status: string; prefix?: string }) {
  return <span className={`badge ${status}`}>{prefix}: {labels[status] || status}</span>
}
function Explanation({ value }: { value: api.Explanation }) {
  return <dl className="facts">{([
    ['Kort svar', value.short_answer], ['Avveining', value.tradeoff],
    ['Konsekvenser', value.consequences], ['Usikkerhet', value.uncertainty],
  ]).map(([name, text]) => <div key={name}><dt>{name}</dt><dd>{text}</dd></div>)}</dl>
}
function Consequences({ items }: { items: api.Consequence[] }) {
  return <>{items.map(person => <section className="inset" key={person.employee_id}>
    <h3>{person.employee_id} · konsekvenser</h3>
    <Badge status={person.control_status} />
    <p>Registrerte timer før → etter: <strong>{number(person.hours_before)} → {number(person.hours_after)} t</strong>
      {!person.hours_complete && ' · ufullstendig arbeidsgrunnlag, ingen bekreftet total'}</p>
    <p className="meta">Arbeidsperiode: {date(person.period_start)} – {date(person.period_end)}. Kilde: vakter i dataversjonen.</p>
    <h4>Hvile før og etter forslaget</h4>
    {(['rest_before', 'rest_after'] as const).map(key => <div key={key}>
      <strong>{key === 'rest_before' ? 'Før' : 'Etter'}</strong>
      {person[key].map(rest => <p key={rest.shift_id}>{rest.shift_id}: før {rest.before_hours === null ?
        (rest.before_known ? 'ingen nabovakt i komplett grunnlag' : 'uavklart nabogrunnlag') : `${number(rest.before_hours)} t fra ${rest.previous_shift_id}`};
        {' '}etter {rest.after_hours === null ? (rest.after_known ? 'ingen nabovakt i komplett grunnlag' : 'uavklart nabogrunnlag') : `${number(rest.after_hours)} t til ${rest.next_shift_id}`}.
        {rest.collision && ' Kjent kollisjon; hvile er ikke bekreftet.'}
        {(!rest.before_known || !rest.after_known) && ' Nødvendig øvrig arbeidsgrunnlag er ufullstendig.'}</p>)}
    </div>)}
    <h4>R1–R5</h4>
    <div className="rule-list">{person.rules.map(rule => <div key={rule.rule}>
      <strong>{rule.rule} · {labels[rule.status]}</strong><p>{rule.value}</p><p>{rule.explanation}</p>
      <details><summary>Kilde og begrensning for {rule.rule}</summary><p>{rule.source}</p><p>{rule.limitation}</p></details>
    </div>)}</div>
  </section>)}</>
}
function CostDetail({ value }: { value: api.Cost }) {
  const assignments = (items: api.CostAssignment[]) => items.map((item, index) => <div className="inset" key={`${item.employee_id}-${item.shift_id}-${index}`}>
    <strong>{item.employee_id} på {item.shift_id}: {money(item.amount)}</strong>
    {item.segments.map((segment, i) => <p key={i}>{period(segment)}: {number(segment.hours)} t ×
      {' '}({rate(segment.rate)} + {rate(segment.supplement)} per time) = {money(segment.amount)}</p>)}
    {item.missing.map(m => <p key={m}>{m}</p>)}
  </div>)
  return <section><h3>Kostnadsanslag · {value.currency}</h3>
    <dl className="facts"><div><dt>Forslag</dt><dd>{money(value.total)}</dd></div>
      <div><dt>Tilsvarende referanse</dt><dd>{money(value.reference)}</dd></div>
      <div><dt>Differanse</dt><dd>{value.difference !== null && Number(value.difference) > 0 ? '+' : ''}{money(value.difference)}</dd></div></dl>
    {!value.complete && <p className="notice">Ufullstendig kjent delsum: {money(value.known_subtotal)}. {value.missing.join(' ')}</p>}
    <details><summary>Timer, satser og tillegg</summary><h4>Forslagets tildelinger</h4>{assignments(value.assignments)}
      <h4>Referansens aktive tildelinger</h4>{value.reference_assignments.length ? assignments(value.reference_assignments) : <p>Ingen aktive berørte tildelinger. Fraværskostnad er utelatt.</p>}</details>
    {value.omitted.map(text => <p className="meta" key={text}>{text}</p>)}
  </section>
}

function nextShift(data: api.Dataset, employee: string): string {
  const assigned = new Set(data.assignments.filter(a => a.employee_id === employee && !a.absent).map(a => a.shift_id))
  return data.shifts.filter(s => assigned.has(s.id) && new Date(s.start) >= new Date(data.week_start) &&
    new Date(s.start) > new Date(data.assessment_time) && new Date(s.start) < new Date(data.week_end))
    .sort((a, b) => +new Date(a.start) - +new Date(b.start))[0]?.id || ''
}

export default function App() {
  const [data, setData] = useState<api.Dataset | null>(null)
  const [datasets, setDatasets] = useState<api.DatasetInfo[]>([])
  const [view, setView] = useState<View>('week')
  const [busy, setBusy] = useState('Laster demodata …')
  const [error, setError] = useState('')
  const [message, setMessage] = useState('')
  const [retry, setRetry] = useState(0)
  const [failedAction, setFailedAction] = useState<FailedAction>(null)
  const [loadId, setLoadId] = useState(0)
  const [absences, setAbsences] = useState<api.Absence[]>([])
  const [employee, setEmployee] = useState('')
  const [startShift, setStartShift] = useState('')
  const [days, setDays] = useState('1')
  const [targetDraft, setTargetDraft] = useState('')
  const [activeTarget, setActiveTarget] = useState('')
  const [formErrors, setFormErrors] = useState<Record<string, string>>({})
  const [previewAttempt, setPreviewAttempt] = useState(0)
  const [previewState, setPreviewState] = useState<{ key: string; value: Awaited<ReturnType<typeof api.previewAbsence>> | null; error: string } | null>(null)
  const [limit, setLimit] = useState<0 | 1>(1)
  const [criteria, setCriteria] = useState<api.Criterion[]>(['P1'])
  const [result, setResult] = useState<api.Evaluation | null>(null)
  const [resultData, setResultData] = useState<api.Dataset | null>(null)
  const [resultBasis, setResultBasis] = useState('')
  const [detailId, setDetailId] = useState('')
  const [records, setRecords] = useState<Record<string, Selection>>({})
  const [selectedKey, setSelectedKey] = useState('')
  const [nextDataset, setNextDataset] = useState('')
  const [comparison, setComparison] = useState<api.DatasetComparison | null>(null)
  const [othersOpen, setOthersOpen] = useState(false)
  const [extraExplanation, setExtraExplanation] = useState<api.Explanation | null>(null)
  const requestId = useRef(0)
  const heading = useRef<HTMLHeadingElement>(null)
  const listPosition = useRef(0)

  useEffect(() => {
    let active = true
    const controller = new AbortController()
    const id = ++requestId.current
    api.fetchDatasets(controller.signal).then(async list => {
      const initial = list.find(d => d.id === 'hovedscenario') || list[0]
      if (!initial) throw new Error('Ingen demodatasett er tilgjengelige.')
      const loaded = await api.fetchDataset(initial.id, controller.signal)
      if (!active || id !== requestId.current) return
      setDatasets(list); setData(loaded)
      const person = loaded.employees[0]?.id || ''
      setEmployee(person); setStartShift(nextShift(loaded, person))
      setNextDataset(list.find(d => d.id !== initial.id)?.id || '')
    }).catch(e => { if (active && id === requestId.current) { setFailedAction('startup'); setError(`Får ikke kontakt med backend: ${errorMessage(e)}`) } })
      .finally(() => { if (active && id === requestId.current) setBusy('') })
    return () => { active = false; controller.abort() }
  }, [retry])

  const basis: api.Basis | null = data ? { dataset_id: data.dataset.id, version: data.dataset.version, absences } : null
  const currentBasis = basis ? basisKey(basis, activeTarget) : ''
  const loadedBasis = `${loadId}:${currentBasis}`
  const previewKey = JSON.stringify([basis, employee, startShift, days])
  const preview = previewState?.key === previewKey ? previewState.value : null
  const previewError = previewState?.key === previewKey ? previewState.error : ''
  const fresh = !!result && resultBasis === loadedBasis && result.search_limit === limit && result.criteria.join(',') === criteria.join(',')
  const detail = result?.alternatives.find(a => a.id === detailId)
  const selected = selectedKey && records[selectedKey] && fresh &&
    basisKey(records[selectedKey].basis, records[selectedKey].target) === currentBasis &&
    result?.alternatives.some(a => a.id === records[selectedKey].alternative.id && a.selectable) ? records[selectedKey] : null

  useEffect(() => {
    let active = true
    const controller = new AbortController()
    if (!data || !employee || !startShift || !Number.isInteger(Number(days)) || Number(days) < 1) return
    api.previewAbsence({ dataset_id: data.dataset.id, version: data.dataset.version, absences }, employee, startShift, Number(days), controller.signal)
      .then(value => { if (active) setPreviewState({ key: previewKey, value, error: '' }) })
      .catch(e => { if (active) setPreviewState({ key: previewKey, value: null, error: errorMessage(e) }) })
    return () => { active = false; controller.abort() }
  }, [data, employee, startShift, days, absences, previewKey, previewAttempt])

  useEffect(() => { heading.current?.focus() }, [view])

  function go(next: View, completed = false) { if (busy && !completed) return; setView(next); setExtraExplanation(null) }
  function retryFailed() {
    if (busy) return
    if (failedAction === 'startup') { setBusy('Laster demodata …'); setError(''); setFailedAction(null); setRetry(r => r + 1) }
    else if (failedAction === 'simulate' && !preview) retryPreview()
    else if (failedAction === 'simulate') void simulate()
    else if (failedAction === 'search') void search()
    else if (failedAction === 'previewDataset') void previewDataset()
    else if (failedAction === 'loadDataset') void loadDataset()
    else if (failedAction === 'explainDifference') void explainDifference()
  }
  function retryPreview() {
    setPreviewState(null); setError(''); setFormErrors({}); setFailedAction(null); setPreviewAttempt(n => n + 1)
  }
  function chooseEmployee(value: string) {
    setEmployee(value); setStartShift(data ? nextShift(data, value) : ''); setTargetDraft(''); setFormErrors({})
  }
  function beginShift(shift: api.Shift) {
    const person = data?.assignments.find(a => a.shift_id === shift.id && !a.absent)?.employee_id || ''
    setEmployee(person); setStartShift(shift.id); setTargetDraft(shift.id); setDays('1'); go('absence')
  }
  async function simulate() {
    if (!basis || !data || busy) return
    const target = targetDraft || preview?.affected.find(a => a.eligible)?.shift.id || ''
    const errors: Record<string, string> = {}
    if (!employee) errors.employee = 'Velg en ansatt.'
    if (!startShift) errors.startShift = 'Velg en startvakt.'
    if (!Number.isInteger(Number(days)) || Number(days) < 1) errors.days = 'Kalenderdager må være et heltall på minst 1.'
    if (!target || !preview?.affected.some(s => s.shift.id === target && s.eligible)) errors.target = 'Velg ett framtidig målskift i uke 5.'
    setFormErrors(errors)
    if (Object.keys(errors).length) { setFailedAction('simulate'); setError('Kontroller feltene i fraværsskjemaet.'); return }
    const id = ++requestId.current
    setBusy('Simulerer fravær …'); setError('')
    try {
      const value = await api.simulateAbsence(basis, { employee_id: employee, shift_id: target })
      const updated = await api.refreshState({ ...basis, absences: value.absences })
      if (id !== requestId.current) return
      const changed = basisKey(basis, activeTarget) !== basisKey({ ...basis, absences: value.absences }, target)
      setAbsences(value.absences); setData(updated); setActiveTarget(target); setTargetDraft(target)
      if (changed) { setSelectedKey(''); setDetailId('') }
      setMessage(value.message); setFailedAction(null); go('alternatives', true)
    } catch (e) { if (id === requestId.current) { setFailedAction('simulate'); setError(errorMessage(e)) } }
    finally { if (id === requestId.current) setBusy('') }
  }
  async function search(nextCriteria = criteria) {
    if (!basis || !activeTarget || busy) return
    const id = ++requestId.current
    setBusy(`Søker med grense ${limit} …`); setError('')
    try {
      const value = await api.evaluate({ ...basis, target_shift_id: activeTarget, search_limit: limit, criteria: nextCriteria })
      if (id !== requestId.current) return
      setResult(value); setResultData(data); setResultBasis(loadedBasis); setDetailId(''); setExtraExplanation(null)
      const previousSelection = records[selectedKey]
      const retained = !previousSelection || value.alternatives.some(a => a.id === previousSelection.alternative.id && a.selectable)
      if (!retained) setSelectedKey('')
      setMessage(value.message + (retained ? '' : ' Tidligere valg er utenfor den nye vurderingen og er bevart som historikk.')); setFailedAction(null); go('alternatives', true)
      queueMicrotask(() => document.getElementById('result-title')?.focus())
    } catch (e) { if (id === requestId.current) { setFailedAction('search'); setError(`Søket feilet. ${errorMessage(e)}`) } }
    finally { if (id === requestId.current) setBusy('') }
  }
  function changeCriteria(next: api.Criterion[]) {
    if (!next.length) { setMessage('Minst ett P-kriterium må være aktivt.'); return }
    setCriteria(next)
    if (fresh) void search(next)
  }
  function inspect(alternative: api.Alternative) {
    listPosition.current = window.scrollY; setDetailId(alternative.id); go('detail')
  }
  function backToList() {
    if (busy) return
    go('alternatives')
    setTimeout(() => { document.getElementById(`inspect-${detailId}`)?.focus({ preventScroll: true }); window.scrollTo(0, listPosition.current) }, 0)
  }
  function selectAlternative() {
    if (!basis || !detail?.selectable || !fresh) return
    const key = selectionKey(basis, activeTarget, detail, loadId)
    setRecords(previous => ({ ...previous, [key]: previous[key] || { key, basis, target: activeTarget, alternative: detail, sent: false, responses: {} } }))
    setSelectedKey(key); setMessage('Valgt i økten. Vaktlisten er uendret.'); go('choice')
  }
  function updateOffer(response?: { employee: string; value: 'akseptert' | 'avslått' }) {
    if (!selected || busy || !fresh) return
    setRecords(previous => {
      const item = previous[selected.key]
      if (response && !item.sent) return previous
      return { ...previous, [selected.key]: { ...item, sent: true, responses: response ?
        { ...item.responses, [response.employee]: response.value } : item.sent ? item.responses :
          Object.fromEntries(item.alternative.affected_employee_ids.map(p => [p, 'venter'])) } }
    })
    setMessage(response ? `Svar simulert for ${response.employee}: ${response.value}.` : 'Tilbud sendt i simuleringen. Venter på svar.')
  }
  async function previewDataset() {
    if (!data || !nextDataset || nextDataset === data.dataset.id || busy) return
    const id = ++requestId.current; setBusy('Sammenligner datagrunnlag …'); setError('')
    try { const value = await api.compareDatasets(data.dataset.id, nextDataset); if (id === requestId.current) { setComparison(value); setFailedAction(null) } }
    catch (e) { if (id === requestId.current) { setFailedAction('previewDataset'); setError(errorMessage(e)) } }
    finally { if (id === requestId.current) setBusy('') }
  }
  async function loadDataset() {
    if (!basis || !data || !comparison || comparison.next.id !== nextDataset || busy) return
    const id = ++requestId.current; setBusy('Laster og kontrollerer nye data …'); setError('')
    try {
      const loaded = await api.fetchDataset(nextDataset)
      const kept = comparison.same_family ? preserveAbsences(absences, loaded) : []
      const refreshed = await api.refreshState({ dataset_id: loaded.dataset.id, version: loaded.dataset.version, absences: kept })
      if (id !== requestId.current) return
      const removed = absences.filter(a => !kept.includes(a))
      const keptTarget = refreshed.shifts.some(s => s.id === activeTarget) ? activeTarget : ''
      setData(refreshed); setLoadId(value => value + 1); setAbsences(kept); setSelectedKey(''); setDetailId(''); setComparison(null)
      setNextDataset(datasets.find(d => d.id !== refreshed.dataset.id)?.id || '')
      setActiveTarget(comparison.same_family ? keptTarget : ''); setTargetDraft('')
      const person = refreshed.employees[0]?.id || ''
      setEmployee(person); setStartShift(nextShift(refreshed, person)); setDays('1')
      setMessage(`Nytt grunnlag er kontrollert. Tidligere valg og svar er historiske. ${comparison.same_family ?
        `${kept.length} tidligere fravær beholdt.` : 'Nytt scenario startet.'} ${removed.length ?
        `Fravær som ikke overføres: ${removed.map(a => `${a.employee_id}/${a.shift_id}`).join(', ')}.` : ''} Kjør ny vurdering.`)
      setFailedAction(null); go('week', true)
    } catch (e) { if (id === requestId.current) { setFailedAction('loadDataset'); setError(`Innlasting feilet. Siste gyldige dataversjon er beholdt. ${errorMessage(e)}`) } }
    finally { if (id === requestId.current) setBusy('') }
  }
  async function explainDifference() {
    if (!basis || !detail || !result || !fresh || busy) return
    const id = ++requestId.current; setBusy('Henter forklaring …'); setError('')
    try { const value = await api.explain({ ...basis, target_shift_id: activeTarget, search_limit: limit, criteria }, detail.id)
      if (id === requestId.current) { setExtraExplanation(value.explanation); setMessage(value.message); setFailedAction(null) }
    } catch (e) { if (id === requestId.current) { setFailedAction('explainDifference'); setError(`KI-forklaring er ikke tilgjengelig. Standardforklaringen vises fortsatt. ${errorMessage(e)}`) } }
    finally { if (id === requestId.current) setBusy('') }
  }

  const card = (alternative: api.Alternative) => {
    const main = alternative.consequences.find(c => c.employee_id === alternative.candidate_id)
    return <article className={`card ${selected?.alternative.id === alternative.id && fresh ? 'selected' : ''}`} key={alternative.id}>
      <div className="card-head"><h3>{alternative.candidate_id} · {labels[alternative.kind]}</h3>
        {alternative.rank !== null && <strong>Rang {alternative.rank}</strong>}</div>
      {selected?.alternative.id === alternative.id && fresh && <p><strong>Valgt i økten</strong></p>}
      <div className="badges"><Badge status={alternative.control_status} /><Badge prefix="Forslagets dekning" status={alternative.coverage_status === 'full' ? 'Full' : 'delvis'} /></div>
      <p>Berørte: {alternative.affected_employee_ids.join(', ')} · vakter {alternative.affected_shift_ids.join(', ')}</p>
      <p><strong>{number(main?.hours_before ?? null)} → {number(main?.hours_after ?? null)} t</strong> registrert i arbeidsuken.</p>
      {main?.rest_after.map(r => <p key={r.shift_id}>Hvile ved {r.shift_id}: {r.before_hours === null ? 'ingen kjent nabovakt' : `${number(r.before_hours)} t før`} / {r.after_hours === null ? 'ingen kjent nabovakt' : `${number(r.after_hours)} t etter`}{r.collision && ' · kollisjon'}.</p>)}
      <p>Sortering {(result?.criteria || criteria).join(' → ')} · P1: {number(alternative.p1)} t · P2: {alternative.p2 === null ? 'Uavklart' : `${number(Number(alternative.p2) * 100)} %`}</p>
      <p>Anslag: <strong>{money(alternative.cost.total)}</strong> · differanse {alternative.cost.difference !== null && Number(alternative.cost.difference) > 0 ? '+' : ''}{money(alternative.cost.difference)}</p>
      {alternative.sorting_missing.map(text => <p className="notice" key={text}>{text}</p>)}
      {alternative.consequences.flatMap(c => c.missing).map((text, i) => <p className="notice" key={i}>{text}</p>)}
      {alternative.uncovered.map(c => <p className="notice" key={c.shift_id}>{c.shift_id}: {c.uncovered} udekket plass.</p>)}
      {alternative.coverage_reason && <p>{alternative.coverage_reason}</p>}
      <button id={`inspect-${alternative.id}`} className="secondary" disabled={!!busy} onClick={() => inspect(alternative)} aria-label={`Undersøk ${alternative.candidate_id}, ${labels[alternative.kind]}, ${alternative.affected_shift_ids.join(', ')}, forslag ${alternative.id.slice(0, 6)}`}>Undersøk</button>
    </article>
  }
  const target = data?.shifts.find(s => s.id === activeTarget)
  const pageTitles: Record<View, string> = { week: 'Ukesoversikt', absence: 'Registrer fravær', alternatives: 'Sammenlign alternativer', detail: 'Undersøk alternativ', choice: 'Valg og tilbud', data: 'Datagrunnlag' }
  const historical = Object.values(records).filter(record => record.key !== selected?.key)
  return <>
    <a className="skip" href="#main">Hopp til innhold</a>
    <header className="app-header"><div><strong className="wordmark">VaktMatch</strong><span>Beslutningsstøtte ved frafall</span></div>
      {data && <p className="meta">Uke 5 · {data.dataset.title}<br />{data.dataset.id} / v{data.dataset.version} · vurdering {date(data.assessment_time)}</p>}
      <nav aria-label="Sideinnganger"><button className="secondary" disabled={!!busy} onClick={() => go('week')}>Ukesoversikt</button><button className="secondary" disabled={!!busy} onClick={() => go('data')}>Datagrunnlag</button></nav>
    </header>
    <p className="demo-banner">Syntetiske data. Ingen endringer i vaktlisten.</p>
    <nav className="steps" aria-label="Arbeidsflyt">{([['absence', '1 Fravær'], ['alternatives', '2 Alternativer'], ['choice', '3 Valg']] as const).map(([name, label]) =>
      <button key={name} className="step" disabled={!!busy} aria-current={view === name || (name === 'alternatives' && view === 'detail') ? 'step' : undefined} onClick={() => go(name)}>{label}</button>)}</nav>
    <main id="main"><h1 ref={heading} tabIndex={-1}>{pageTitles[view]}</h1>
      <div className="announcements" aria-live="polite" role="status">{busy || message}</div>
      {error && <div className="error" role="alert"><strong>Handlingen kunne ikke fullføres</strong><p>{error}</p>
        <button className="secondary" disabled={!!busy} onClick={retryFailed}>Prøv igjen</button></div>}
      {!data && !error && <p>Laster demodata …</p>}
      {data && <div className="workspace"><aside className="context panel"><h2>Gjeldende grunnlag</h2>
        <p>{data.dataset.title} · v{data.dataset.version}</p><p>{date(data.week_start)} – {date(data.week_end)}</p>
        <p>Registrerte fravær: {absences.length ? absences.map(a => `${a.employee_id} på ${a.shift_id}`).join('; ') : 'Ingen simulerte fravær'}</p>
        {data.coverage.some(c => c.uncovered && c.shift_id !== activeTarget) && <p>Andre udekkede vakter: {data.coverage.filter(c => c.uncovered && c.shift_id !== activeTarget).map(c => `${c.shift_id}: ${c.uncovered} plass(er)`).join('; ')}. Dette søket løser bare målskiftet.</p>}
        {target && <><h3>Målskift {target.id}</h3><p>{period(target)}</p><p>Behov: {target.required_count} × {target.required_skill}</p>
          <p><strong>Faktisk udekket: {data.coverage.find(c => c.shift_id === target.id)?.uncovered ?? 'Ukjent'} plass(er)</strong></p></>}
        <p className="meta">Valg og aksept gjennomfører ingen tildeling. Historikk, påbegynte vakter og låste tildelinger flyttes aldri.</p>
      </aside><div className="work">
        {view === 'week' && <section className="panel"><div className="section-heading"><h2>Planlagt uke 5</h2><button disabled={!!busy} onClick={() => go('absence')}>Registrer fravær</button></div>
          <p>Bemanning og regelkontroll er separate. Vaktens lås hindrer flytting, men hindrer ikke fravær.</p>
          {!data.coverage.length && <p>Ingen vakter i dette grunnlaget. Åpne Datagrunnlag.</p>}
          <div className="shift-list">{[...data.coverage].sort((a, b) => +new Date(data.shifts.find(s => s.id === a.shift_id)!.start) - +new Date(data.shifts.find(s => s.id === b.shift_id)!.start)).map(c => {
            const shift = data.shifts.find(s => s.id === c.shift_id)!
            const assignments = data.assignments.filter(a => a.shift_id === shift.id)
            const started = new Date(shift.start) <= new Date(data.assessment_time)
            return <article className={`shift ${c.uncovered ? 'gap' : ''}`} key={shift.id}><h3>{shift.id}</h3><p>{period(shift)}</p>
              <p>Behov: {c.required} × {shift.required_skill} · tildelt: {c.assigned.join(', ') || 'Ingen'} · <strong>{c.uncovered} udekket</strong></p>
              <p>{assignments.map(a => `${a.employee_id}${a.locked ? ': låst tildeling' : ': ulåst'}${a.absent || absences.some(x => x.employee_id === a.employee_id && x.shift_id === a.shift_id) ? ', fravær' : ''}`).join('; ')}</p>
              {started ? <p className="meta">Påbegynt vakt; kan ikke velges som nytt fravær eller flyttes.</p> : <button className="secondary" disabled={!!busy} onClick={() => beginShift(shift)}>Åpne fravær for {shift.id}</button>}
            </article>
          })}</div>
          <details><summary>Kontroll av nåværende bemanning</summary><Consequences items={data.current_controls} /></details>
          {activeTarget && <button className="secondary" onClick={() => go('alternatives')}>Vurder gjeldende målskift på nytt</button>}
        </section>}

        {view === 'absence' && <section className="panel"><h2>Ett målskift om gangen</h2><p id="absence-help">Velg én vakt å undersøke. Dagene viser en periode, ikke kjent fraværsvarighet.</p>
          {Object.keys(formErrors).length > 0 && <div className="error" role="alert"><p>Rett feltene:</p><ul>{Object.entries(formErrors).map(([field, text]) => <li key={field}><a href={`#${field}`}>{text}</a></li>)}</ul></div>}
          <form noValidate onSubmit={e => { e.preventDefault(); void simulate() }}>
            <label htmlFor="employee">Ansatt</label><select id="employee" value={employee} disabled={!!busy} aria-invalid={!!formErrors.employee} aria-describedby="employee-error absence-help" onChange={e => chooseEmployee(e.target.value)}><option value="">Velg ansatt</option>{data.employees.map(e => <option key={e.id} value={e.id}>{e.name}</option>)}</select><p id="employee-error" className="field-error">{formErrors.employee}</p>
            <label htmlFor="startShift">Startvakt</label><select id="startShift" value={startShift} disabled={!!busy} aria-invalid={!!formErrors.startShift} aria-describedby="startShift-error" onChange={e => { setStartShift(e.target.value); setTargetDraft('') }}><option value="">Velg startvakt</option>{data.shifts.filter(s => data.assignments.some(a => a.employee_id === employee && a.shift_id === s.id)).sort((a,b) => +new Date(a.start)-+new Date(b.start)).map(s => <option key={s.id} value={s.id}>{s.id} · {period(s)}</option>)}</select><p id="startShift-error" className="field-error">{formErrors.startShift}</p>
            <label htmlFor="days">Kalenderdager</label><input id="days" type="number" min="1" step="1" value={days} disabled={!!busy} aria-invalid={!!formErrors.days} aria-describedby="days-error" onChange={e => { setDays(e.target.value); setTargetDraft('') }} /><p id="days-error" className="field-error">{formErrors.days}</p>
            <fieldset id="target" aria-invalid={!!formErrors.target} aria-describedby="target-error"><legend>Berørte vakter · velg ett målskift</legend>
              {preview ? <><p>Periode: {period(preview)} · Europe/Oslo</p>{preview.affected.length ? preview.affected.map(item => <label className="radio-row" key={item.shift.id}>
                <input type="radio" name="target" value={item.shift.id} disabled={!item.eligible || !!busy} checked={(targetDraft || preview.affected.find(a => a.eligible)?.shift.id) === item.shift.id} onChange={() => setTargetDraft(item.shift.id)} />
                <span>{item.shift.id} · {period(item.shift)}{item.limitation && <span className="meta">{item.limitation}</span>}</span></label>) : <p>Ingen vakter overlapper perioden. Velg en annen startvakt.</p>}</> : <>{previewError ? <><p>{previewError}</p><button type="button" className="secondary" disabled={!!busy} onClick={retryPreview}>Hent berørte vakter på nytt</button></> : <p>Velg gyldige felt for å vise berørte vakter.</p>}</>}
            </fieldset><p id="target-error" className="field-error">{formErrors.target}</p>
            <button disabled={!!busy} type="submit">Simuler fravær</button>
          </form>
        </section>}

        {view === 'alternatives' && <section className="panel"><h2>Søkeomfang og prioritering</h2>
          {!activeTarget && <p>Simuler først fravær for ett målskift. <button className="secondary" onClick={() => go('absence')}>Gå til Fravær</button></p>}
          <label htmlFor="search-limit">Søkegrense</label><select id="search-limit" value={limit} disabled={!!busy} onChange={e => setLimit(Number(e.target.value) as 0 | 1)}><option value="0">0 · Direkte erstattere</option><option value="1">1 · Også én flytting</option></select>
          <fieldset><legend>Aktive sorteringskriterier</legend>{(['P1','P2'] as const).map(c => <label key={c} className="radio-row"><input type="checkbox" disabled={!!busy} checked={criteria.includes(c)} onChange={e => changeCriteria(e.target.checked ? [...criteria, c] : criteria.filter(x => x !== c))} /><span>{c === 'P1' ? 'P1 · Færrest planlagte uketimer' : 'P2 · Lavest andel av avtalte timer'}</span></label>)}</fieldset>
          {criteria.length === 2 && <><label htmlFor="criteria-order">Prioritert rekkefølge</label><select id="criteria-order" value={criteria.join(',')} disabled={!!busy} onChange={e => changeCriteria(e.target.value.split(',') as api.Criterion[])}><option value="P1,P2">P1 → P2</option><option value="P2,P1">P2 → P1</option></select></>}
          <p className="meta">Minst ett kriterium. Kostnad og historikk endrer ikke rangeringen. Grenseendring krever nytt søk.</p>
          <button disabled={!activeTarget || !!busy} onClick={() => void search()}>Finn alternativer</button>
          {result && <><h2 id="result-title" tabIndex={-1}>Resultater · {result.target_shift_id}</h2>
            {!fresh && <p className="notice">Tidligere vurdering på {result.dataset_id} / v{result.version}, grense {result.search_limit}. Kjør ny vurdering på gjeldende grunnlag.</p>}
            <Badge prefix="Søkestatus" status={result.search_status} /><p>{result.message}</p>
            <p className="meta">{result.combinations_examined} kombinasjoner undersøkt · {number(result.duration_ms)} ms beregning · {result.criteria.join(' → ')}. Samme rang betyr like kriterieverdier.</p>
            <h3>Rangerte komplette forslag</h3>{result.alternatives.filter(a => a.rank !== null).map(card)}
            {!result.alternatives.some(a => a.rank !== null) && <p>Ingen komplette rangerte forslag på dette grunnlaget.</p>}
            {result.alternatives.some(a => a.selectable && a.rank === null) && <><h3>Bestått med manglende sorteringsgrunnlag</h3>{result.alternatives.filter(a => a.selectable && a.rank === null).map(card)}</>}
            <details open={othersOpen} onToggle={e => setOthersOpen(e.currentTarget.open)}><summary>Øvrige undersøkbare funn ({result.alternatives.filter(a => !a.selectable).length})</summary>{result.alternatives.filter(a => !a.selectable).map(card)}</details>
          </>}
        </section>}

        {view === 'detail' && <section className="panel"><button className="secondary" onClick={backToList}>Tilbake til alternativer</button>
          {detail ? <><h2>{detail.candidate_id} · {labels[detail.kind]}</h2><p className="meta">Forslag {detail.id} · {result?.dataset_id} / v{result?.version}</p>
            <div className="badges"><Badge status={detail.control_status} /><Badge prefix="Forslagets dekning" status={detail.complete ? 'Full' : 'delvis'} /></div>
            {!fresh && <p className="notice">Tidligere vurdering. Kjør ny vurdering før valg og tilbud.</p>}
            <section className="proposal"><h3>Forslag til plan · vaktlisten er uendret</h3>{detail.plan.map(item => <div key={item.shift_id}><strong>{item.shift_id} · {period((resultData || data).shifts.find(s => s.id === item.shift_id) || { start: data.week_start, end: data.week_end })}</strong><p>Gjeldende: {item.before.join(', ') || 'Udekket'} → Forslag: {item.after.join(', ') || 'Udekket'}</p></div>)}{detail.uncovered.map(c => <p key={c.shift_id}>{c.shift_id}: {c.uncovered} udekket plass i forslaget.</p>)}</section>
            <Consequences items={detail.consequences} />
            {detail.coverage_reason && <section><h3>Hvorfor er dekningen ikke bekreftet?</h3><p>{detail.coverage_reason}</p>{detail.replacement_findings.map(person => <details key={person.employee_id}><summary>{person.employee_id} · {labels[person.control_status]}</summary>{person.findings.map((finding, i) => <p key={i}>{finding}</p>)}</details>)}</section>}
            <h3>Historikk · uke 1–4</h3>{detail.history.map(person => <details key={person.employee_id}><summary>{person.employee_id} · {person.weeks.every(w => w.complete) ? 'Komplett registrert historikk' : 'Historikk ufullstendig'}</summary>{person.weeks.map(w => <div className="inset" key={w.week}><strong>Uke {w.week}: {period(w)}</strong><p>{number(w.known_hours)} registrerte timer · vakter: {w.shift_ids.join(', ') || 'Ingen registrerte vakter'}. {w.complete ? 'Komplett' : 'Ufullstendig – tall er bare kjent delgrunnlag'}</p><p>{w.source}</p><p className="meta">{w.limitation}</p></div>)}</details>)}
            <CostDetail value={detail.cost} />
            <section className="inset"><h3>Standardforklaring</h3><Explanation value={detail.explanation} />
              <button className="secondary" disabled={!!busy || !fresh || !result?.alternatives.some(a => a.rank === 1)} onClick={() => void explainDifference()}>Forklar forskjellen</button>
              {!result?.alternatives.some(a => a.rank === 1) && <p>Ingen rangert referanse på dette grunnlaget.</p>}
              {extraExplanation && <><h4>Standard sammenligning · KI er ikke tilgjengelig</h4><Explanation value={extraExplanation} /></>}
            </section>
            <button disabled={!!busy || !fresh || !detail.selectable} onClick={selectAlternative}>Velg alternativ</button>
            {(!detail.selectable || !fresh) && <p>Valg krever komplett dekning og bestått kontroll på gjeldende grunnlag.</p>}
          </> : <p>Velg et alternativ fra listen for å undersøke det.</p>}
        </section>}

        {view === 'choice' && <section className="panel"><h2>Gjeldende øktvalg</h2>{selected ? <><h3>{selected.alternative.candidate_id} · {labels[selected.alternative.kind]}</h3><p>{selected.basis.dataset_id} / v{selected.basis.version} · målskift {selected.target}</p><p>Plan: {planSummary(selected.alternative)} · forslag {selected.alternative.id.slice(0, 6)}</p><p>Valgt i økten. Vaktlisten er uendret.</p><Badge status={selected.alternative.control_status} />
          <h3>Tilbudssimulering</h3><p>{selected.sent && 'Tilbud sendt i simuleringen. '}{offerStatus(selected)}</p>
          {!fresh && <p className="notice">Kjør ny vurdering før videre tilbudssimulering.</p>}
          <button disabled={!!busy || selected.sent || !fresh} onClick={() => updateOffer()}>Simuler tilbud</button>
          {selected.alternative.affected_employee_ids.map(person => <div className="inset" key={person}><h4>{person}</h4><p>Svar: {selected.sent ? selected.responses[person] || 'venter' : 'Aksept ikke simulert'}</p><div className="actions"><button className="secondary" disabled={!!busy || !selected.sent || !fresh} onClick={() => updateOffer({ employee: person, value: 'akseptert' })}>Simuler aksept for {person}</button><button className="secondary" disabled={!!busy || !selected.sent || !fresh} onClick={() => updateOffer({ employee: person, value: 'avslått' })}>Simuler avslag for {person}</button></div></div>)}
          <button className="secondary" onClick={() => go('alternatives')}>Undersøk et annet alternativ</button>
        </> : <p>Ingen gjeldende valg. Undersøk et komplett, bestått alternativ og velg det. <button className="secondary" onClick={() => go('alternatives')}>Til alternativer</button></p>}
          <details><summary>Tidligere valg ({historical.length})</summary>{historical.length ? historical.map(record => <article className="inset" key={record.key}><h3>{record.alternative.candidate_id} · {labels[record.alternative.kind]}</h3><p>{record.basis.dataset_id} / v{record.basis.version} · {record.target}</p><p>Plan: {planSummary(record.alternative)} · forslag {record.alternative.id.slice(0, 6)}</p><p>Fravær: {record.basis.absences.map(a => `${a.employee_id}/${a.shift_id}`).join(', ')}</p><p>{record.sent && 'Tilbud sendt i simuleringen. '}{offerStatus(record)}</p>{record.alternative.affected_employee_ids.map(p => <p key={p}>{p}: {record.responses[p] || 'Aksept ikke simulert'}</p>)}</article>) : <p>Ingen tidligere valg i denne økten.</p>}</details>
          <p className="meta">Valg og svar lever i aktiv fane. Lukking avslutter økten.</p>
        </section>}

        {view === 'data' && <section className="panel"><h2>Forhåndslagde datagrunnlag</h2><p>Forhåndsvis forskjellene før innlasting. Ingen filer endres.</p><label htmlFor="dataset">Nytt datasett</label><select id="dataset" value={nextDataset} disabled={!!busy} onChange={e => { setNextDataset(e.target.value); setComparison(null) }}><option value="">Velg datasett</option>{datasets.filter(d => d.id !== data.dataset.id).map(d => <option key={d.id} value={d.id}>{d.title} · v{d.version}</option>)}</select>
          <p>{datasets.find(d => d.id === nextDataset)?.description}</p><button className="secondary" disabled={!!busy || !nextDataset} onClick={() => void previewDataset()}>Forhåndsvis endringer</button>
          {comparison && <><h3>{comparison.previous.id} / v{comparison.previous.version} → {comparison.next.id} / v{comparison.next.version}</h3>
            <p>{comparison.same_family ? 'Samme scenario: gyldige aktive fravær beholdes.' : 'Et annet scenario startes. Aktive fravær overføres ikke; tidligere valg og svar beholdes som økthistorikk.'}</p>
            {comparison.unchanged ? <p>Innholdet er uendret. Nytt grunnlag krever likevel ny vurdering og arver ingen aksept.</p> : <div className="changes">{comparison.changes.map((change, index) => <div className="inset" key={index}><strong>{change.label}</strong><p>Før: {change.before_label}</p><p>Etter: {change.after_label}</p></div>)}</div>}
            <button disabled={!!busy} onClick={() => void loadDataset()}>Last inn oppdaterte vaktdata</button>
          </>}
          <p className="meta">Historikk og satser er syntetiske, skrevet av Codex på Odins mandat 08.11.2026. Scenarioene er ikke reelle arbeidsplaner.</p>
        </section>}
      </div></div>}
    </main>
  </>
}
