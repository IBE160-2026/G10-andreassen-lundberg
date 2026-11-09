import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, expect, test, vi } from 'vitest'
import App from './App'
import { alternative, dataset, evaluation, info, updatedInfo } from './test/demo-fixture'

beforeEach(() => { vi.stubGlobal('scrollTo', vi.fn()) })

afterEach(() => {
  cleanup()
  vi.unstubAllGlobals()
})

function setupApi(evaluationValue = evaluation) {
  const fetchMock = vi.fn(async (url: string, options?: RequestInit) => {
    const body = options?.body ? JSON.parse(String(options.body)) : undefined
    let value: unknown
    if (url === '/api/datasets') value = [info, updatedInfo]
    else if (url.includes('/state') && options?.method !== 'POST') value = { ...dataset, dataset: url.includes('komplettert') ? updatedInfo : info }
    else if (url === '/api/state') value = { ...dataset, dataset: body.dataset_id === updatedInfo.id ? updatedInfo : info, coverage: evaluation.coverage }
    else if (url === '/api/absences/preview') value = { start: dataset.week_start, end: dataset.week_end, affected: [{ shift: dataset.shifts[0], eligible: true, limitation: '' }] }
    else if (url === '/api/absences/simulate') value = { ...body, absences: [body.absence], coverage: evaluation.coverage, message: 'Fraværet er simulert for valgt vakt. Finn alternativer når du er klar.' }
    else if (url === '/api/evaluate') value = { ...evaluationValue, ...body, alternatives: evaluationValue.alternatives.filter(a => body.search_limit === 1 || a.moves === 0) }
    else if (url === '/api/datasets/compare') value = { previous: body.previous_id === info.id ? info : updatedInfo, next: body.next_id === info.id ? info : updatedInfo, same_family: true, unchanged: false, changes: [{ category: 'employees', id: 'V01', field: 'availability', before: null, after: [], label: 'Ansatte · V01 · Tilgjengelighet', before_label: 'Mangler opplysninger / ingen oppføring', after_label: 'Kjent utilgjengelig' }] }
    else if (url === '/api/explain') value = { mode: 'standard', message: 'Standardforklaringen vises fortsatt.', explanation: evaluation.alternatives[0].explanation, reference_id: 'A02' }
    else throw new Error(`Uventet testforespørsel: ${url}`)
    return new Response(JSON.stringify(value))
  })
  vi.stubGlobal('fetch', fetchMock)
  return fetchMock
}

function failOnce(fetchMock: ReturnType<typeof setupApi>, path: string) {
  const original = fetchMock.getMockImplementation()!
  let failed = false
  fetchMock.mockImplementation(async (url, options) => {
    if (url === path && !failed) { failed = true; return new Response(JSON.stringify({ message: 'Midlertidig feil. Prøv igjen.' }), { status: 503 }) }
    return original(url, options)
  })
}

async function startSearch() {
  render(<App />)
  fireEvent.click(await screen.findByRole('button', { name: 'Registrer fravær' }))
  await screen.findByRole('radio')
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  await waitFor(() => expect(screen.getByRole('button', { name: 'Finn alternativer' })).toBeEnabled())
  fireEvent.click(screen.getByRole('button', { name: 'Finn alternativer' }))
  await screen.findByRole('button', { name: /Undersøk A02/ })
}

test('simulering og søk er separate handlinger med API-beregnet dekning', async () => {
  const fetchMock = setupApi()
  render(<App />)
  fireEvent.click(await screen.findByRole('button', { name: 'Registrer fravær' }))
  await screen.findByRole('radio')
  expect(fetchMock.mock.calls.some(([url]) => url === '/api/evaluate')).toBe(false)
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  await screen.findByText('Faktisk udekket: 1 plass(er)')
  expect(fetchMock.mock.calls.some(([url]) => url === '/api/evaluate')).toBe(false)
  fireEvent.click(screen.getByRole('button', { name: 'Finn alternativer' }))
  await screen.findByRole('button', { name: /Undersøk A02/ })
  expect(fetchMock.mock.calls.some(([url]) => url === '/api/evaluate')).toBe(true)
})

test('A → B → A bevarer svar for riktig forslag uten å endre vaktlisten', async () => {
  setupApi(); await startSearch()
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A02/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  fireEvent.click(screen.getByRole('button', { name: 'Simuler tilbud' }))
  fireEvent.click(screen.getByRole('button', { name: 'Simuler avslag for A02' }))
  expect(screen.getByText(/Avslått – ikke full simulert aksept/)).toBeInTheDocument()
  fireEvent.click(screen.getByRole('button', { name: 'Undersøk et annet alternativ' }))
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A03/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  expect(screen.getByRole('button', { name: 'Simuler tilbud' })).toBeEnabled()
  fireEvent.click(screen.getByRole('button', { name: 'Undersøk et annet alternativ' }))
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A02/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  expect(screen.getByRole('button', { name: 'Simuler tilbud' })).toBeDisabled()
  expect(screen.getByText(/Avslått – ikke full simulert aksept/)).toBeInTheDocument()
  expect(screen.getByText('Faktisk udekket: 1 plass(er)')).toBeInTheDocument()
})

test('datasettbytte arkiverer valg og svar og bevarer gyldig fravær', async () => {
  const fetchMock = setupApi(); await startSearch()
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A02/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  fireEvent.click(screen.getByRole('button', { name: 'Simuler tilbud' }))
  fireEvent.click(screen.getByRole('button', { name: 'Simuler aksept for A02' }))
  fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
  fireEvent.click(screen.getByRole('button', { name: 'Forhåndsvis endringer' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Last inn oppdaterte vaktdata' }))
  await screen.findByRole('heading', { name: 'Planlagt uke 5' })
  fireEvent.click(screen.getByRole('button', { name: '3 Valg' }))
  expect(screen.getByText(/Ingen gjeldende valg/)).toBeInTheDocument()
  fireEvent.click(screen.getByText('Tidligere valg (1)'))
  expect(screen.getByText(/Full simulert aksept/)).toBeInTheDocument()
  const refresh = fetchMock.mock.calls.filter(([url]) => url === '/api/state').at(-1)!
  expect(JSON.parse(String(refresh[1]?.body)).absences).toEqual([{ employee_id: 'A01', shift_id: 'X' }])
})

test('ugyldig skjema viser feltlenker og sender ikke fravær', async () => {
  const fetchMock = setupApi(); render(<App />)
  fireEvent.click(await screen.findByRole('button', { name: 'Registrer fravær' }))
  fireEvent.change(screen.getByLabelText('Kalenderdager'), { target: { value: '0' } })
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  expect(screen.getByRole('link', { name: /Kalenderdager må være/ })).toHaveAttribute('href', '#days')
  expect(fetchMock.mock.calls.some(([url]) => url === '/api/absences/simulate')).toBe(false)
})

test('et flyttevalg utenfor ny søkegrense blir historisk og kan ikke få tilbud', async () => {
  const moved = alternative('B','8'); moved.kind = 'flytting'; moved.moves = 1
  setupApi({ ...evaluation, alternatives: [...evaluation.alternatives, moved] })
  await startSearch()
  fireEvent.click(screen.getByRole('button', { name: /Undersøk B,/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  fireEvent.click(screen.getByRole('button', { name: 'Undersøk et annet alternativ' }))
  fireEvent.change(screen.getByLabelText('Søkegrense'), { target: { value: '0' } })
  fireEvent.click(screen.getByRole('button', { name: 'Finn alternativer' }))
  await waitFor(() => expect(screen.getByRole('button', { name: 'Finn alternativer' })).toBeEnabled())
  fireEvent.click(screen.getByRole('button', { name: '3 Valg' }))
  expect(screen.getByText(/Ingen gjeldende valg/)).toBeInTheDocument()
  expect(screen.queryByRole('button', { name: 'Simuler tilbud' })).not.toBeInTheDocument()
  expect(screen.getByText('Tidligere valg (1)')).toBeInTheDocument()
})

test('datasett A → B → A krever ny aksept men beholder tidligere svar historisk', async () => {
  setupApi(); await startSearch()
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A02/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  fireEvent.click(screen.getByRole('button', { name: 'Simuler tilbud' }))
  fireEvent.click(screen.getByRole('button', { name: 'Simuler aksept for A02' }))
  for (const identifier of [updatedInfo.id, info.id]) {
    fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
    fireEvent.change(screen.getByLabelText('Nytt datasett'), { target: { value: identifier } })
    fireEvent.click(screen.getByRole('button', { name: 'Forhåndsvis endringer' }))
    fireEvent.click(await screen.findByRole('button', { name: 'Last inn oppdaterte vaktdata' }))
    await screen.findByRole('heading', { name: 'Planlagt uke 5' })
    await waitFor(() => expect(screen.getByRole('button', { name: 'Datagrunnlag' })).toBeEnabled())
  }
  fireEvent.click(screen.getByRole('button', { name: '2 Alternativer' }))
  expect(screen.getByRole('button', { name: /Undersøk A02/ })).toBeEnabled()
  fireEvent.click(screen.getByRole('button', { name: 'Finn alternativer' }))
  await waitFor(() => expect(screen.getByRole('button', { name: 'Finn alternativer' })).toBeEnabled())
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A02/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
  expect(screen.getByRole('button', { name: 'Simuler tilbud' })).toBeEnabled()
  expect(screen.getByRole('button', { name: 'Simuler aksept for A02' })).toBeDisabled()
  fireEvent.click(screen.getByText('Tidligere valg (1)'))
  expect(screen.getByText(/Full simulert aksept/)).toBeInTheDocument()
})

test('Prøv igjen gjentar feilet fraværssimulering med gyldige felt', async () => {
  const fetchMock = setupApi(); render(<App />)
  fireEvent.click(await screen.findByRole('button', { name: 'Registrer fravær' }))
  await screen.findByRole('radio')
  failOnce(fetchMock, '/api/absences/simulate')
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Prøv igjen' }))
  await screen.findByRole('button', { name: 'Finn alternativer' })
  expect(fetchMock.mock.calls.filter(([url]) => url === '/api/absences/simulate')).toHaveLength(2)
})

test('Prøv igjen gjentar både feilet datasammenligning og innlasting', async () => {
  const fetchMock = setupApi(); render(<App />)
  await screen.findByRole('button', { name: 'Registrer fravær' })
  fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
  failOnce(fetchMock, '/api/datasets/compare')
  fireEvent.click(screen.getByRole('button', { name: 'Forhåndsvis endringer' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Prøv igjen' }))
  await screen.findByRole('button', { name: 'Last inn oppdaterte vaktdata' })
  expect(fetchMock.mock.calls.filter(([url]) => url === '/api/datasets/compare')).toHaveLength(2)
  failOnce(fetchMock, '/api/datasets/komplettert/state')
  fireEvent.click(screen.getByRole('button', { name: 'Last inn oppdaterte vaktdata' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Prøv igjen' }))
  await screen.findByRole('heading', { name: 'Planlagt uke 5' })
  expect(fetchMock.mock.calls.filter(([url]) => url === '/api/datasets/komplettert/state')).toHaveLength(2)
})

test('Prøv igjen gjentar feilet forklaring uten å fjerne standarden', async () => {
  const fetchMock = setupApi(); await startSearch()
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A03/ }))
  failOnce(fetchMock, '/api/explain')
  fireEvent.click(screen.getByRole('button', { name: 'Forklar forskjellen' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Prøv igjen' }))
  await screen.findByRole('heading', { name: 'Standard sammenligning · KI er ikke tilgjengelig' })
  expect(fetchMock.mock.calls.filter(([url]) => url === '/api/explain')).toHaveLength(2)
  expect(screen.getByRole('heading', { name: 'Standardforklaring' })).toBeInTheDocument()
})

test('ventende søk låser navigasjon og annonserer handlingen til svaret er behandlet', async () => {
  const fetchMock = setupApi(); render(<App />)
  fireEvent.click(await screen.findByRole('button', { name: 'Registrer fravær' }))
  await screen.findByRole('radio')
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  await waitFor(() => expect(screen.getByRole('button', { name: 'Finn alternativer' })).toBeEnabled())
  const original = fetchMock.getMockImplementation()!
  let resolve!: (response: Response) => void
  fetchMock.mockImplementation((url, options) => url === '/api/evaluate' ? new Promise<Response>(done => { resolve = done }) : original(url, options))
  fireEvent.click(screen.getByRole('button', { name: 'Finn alternativer' }))
  expect(screen.getByRole('status')).toHaveTextContent('Søker med grense 1')
  expect(screen.getByRole('button', { name: 'Datagrunnlag' })).toBeDisabled()
  expect(screen.getByRole('button', { name: '1 Fravær' })).toBeDisabled()
  fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
  resolve(new Response(JSON.stringify(evaluation)))
  await screen.findByRole('button', { name: /Undersøk A02/ })
  expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Sammenlign alternativer')
  expect(screen.getByRole('button', { name: 'Datagrunnlag' })).toBeEnabled()
})

test('gamle kort viser opprinnelige kriterier etter ubehandlet scope- og kriterieendring', async () => {
  const fetchMock = setupApi(); await startSearch()
  const count = fetchMock.mock.calls.filter(([url]) => url === '/api/evaluate').length
  fireEvent.change(screen.getByLabelText('Søkegrense'), { target: { value: '0' } })
  fireEvent.click(screen.getByLabelText('P2 · Lavest andel av avtalte timer'))
  fireEvent.click(screen.getByLabelText('P1 · Færrest planlagte uketimer'))
  expect(fetchMock.mock.calls.filter(([url]) => url === '/api/evaluate')).toHaveLength(count)
  expect(screen.getAllByText(/Sortering P1 ·/)).toHaveLength(2)
  expect(screen.queryByText(/Sortering P2 ·/)).not.toBeInTheDocument()
})

test('ny vurderingstid fjerner utløpt simulert fravær og forklarer paret ved innlasting', async () => {
  const fetchMock = setupApi(); await startSearch()
  const original = fetchMock.getMockImplementation()!
  fetchMock.mockImplementation(async (url, options) => {
    const response = await original(url, options)
    if (url === '/api/datasets/komplettert/state') {
      const value = await response.json()
      return new Response(JSON.stringify({ ...value, assessment_time: '2026-10-14T09:00:00+02:00' }))
    }
    return response
  })
  fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
  fireEvent.click(screen.getByRole('button', { name: 'Forhåndsvis endringer' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Last inn oppdaterte vaktdata' }))
  await screen.findByRole('heading', { name: 'Planlagt uke 5' })
  expect(screen.getByRole('status')).toHaveTextContent('Fravær som ikke overføres: A01/X')
  const last = fetchMock.mock.calls.filter(([url]) => url === '/api/state').at(-1)!
  expect(JSON.parse(String(last[1]?.body)).absences).toEqual([])
})

test('viser feilmelding når backend ikke svarer', async () => {
  vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response('', { status: 503 })))

  render(<App />)

  expect(await screen.findByText(/Får ikke kontakt med backend/)).toBeInTheDocument()
})

test('oversetter nettverksfeil til norsk', async () => {
  vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new TypeError('Failed to fetch')))

  render(<App />)

  expect(await screen.findByText(/Backend er utilgjengelig/)).toBeInTheDocument()
  expect(screen.queryByText(/Failed to fetch/)).not.toBeInTheDocument()
})

test('K1: Prøv igjen henter en feilet fraværsforhåndsvisning på nytt', async () => {
  const fetchMock = setupApi()
  failOnce(fetchMock, '/api/absences/preview')
  render(<App />)
  fireEvent.click(await screen.findByRole('button', { name: 'Registrer fravær' }))
  await screen.findByText('Midlertidig feil. Prøv igjen.')
  expect(screen.queryByRole('radio')).not.toBeInTheDocument()
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  fireEvent.click(await screen.findByRole('button', { name: 'Prøv igjen' }))
  expect(await screen.findByRole('radio')).toBeChecked()
  expect(fetchMock.mock.calls.filter(([url]) => url === '/api/absences/preview')).toHaveLength(2)
  expect(screen.queryByRole('alert')).not.toBeInTheDocument()
  fireEvent.click(screen.getByRole('button', { name: 'Simuler fravær' }))
  await screen.findByRole('button', { name: 'Finn alternativer' })
})

test('K3: valg og historikk viser hvilken konkret plan som ble valgt', async () => {
  const moved = (id: string, shift: string) => {
    const value = alternative(id, '40'); value.candidate_id = 'A08'; value.kind = 'flytting'; value.moves = 1
    value.affected_employee_ids = ['A06', 'A08']; value.affected_shift_ids = [shift, 'X']
    value.plan = [{ shift_id: shift, before: ['A08'], after: ['A06'] }, { shift_id: 'X', before: [], after: ['A08'] }]
    return value
  }
  setupApi({ ...evaluation, alternatives: [...evaluation.alternatives, moved('aaaaaa1', 'W5-A08-4'), moved('bbbbbb2', 'W5-A08-5')] })
  await startSearch()
  for (const id of ['aaaaaa', 'bbbbbb']) {
    fireEvent.click(screen.getByRole('button', { name: new RegExp(`Undersøk A08,.*forslag ${id}`) }))
    fireEvent.click(screen.getByRole('button', { name: 'Velg alternativ' }))
    if (id === 'aaaaaa') fireEvent.click(screen.getByRole('button', { name: 'Undersøk et annet alternativ' }))
  }
  expect(screen.getByText('Plan: W5-A08-5: A08 → A06; X: Udekket → A08 · forslag bbbbbb')).toBeInTheDocument()
  expect(screen.getByText('Plan: W5-A08-4: A08 → A06; X: Udekket → A08 · forslag aaaaaa')).toBeInTheDocument()
})

test('K4: tilbake fra et øvrig funn holder listen åpen og gir fokus til kortet', async () => {
  const other = alternative('A05', '32'); other.selectable = false; other.control_status = 'regelavvik'; other.rank = null
  setupApi({ ...evaluation, alternatives: [...evaluation.alternatives, other] })
  await startSearch()
  const details = () => screen.getByText('Øvrige undersøkbare funn (1)').closest('details')!
  details().open = true; fireEvent(details(), new Event('toggle'))
  fireEvent.click(screen.getByRole('button', { name: /Undersøk A05/ }))
  fireEvent.click(screen.getByRole('button', { name: 'Tilbake til alternativer' }))
  await waitFor(() => expect(document.activeElement).toBe(screen.getByRole('button', { name: /Undersøk A05/ })))
  expect(details().open).toBe(true)
})

test('K6 og K10: endringer vises med lesbare felt og neste datasett er aldri det innlastede', async () => {
  const fetchMock = setupApi(); render(<App />)
  await screen.findByRole('button', { name: 'Registrer fravær' })
  fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
  fireEvent.click(screen.getByRole('button', { name: 'Forhåndsvis endringer' }))
  expect(await screen.findByText('Ansatte · V01 · Tilgjengelighet')).toBeInTheDocument()
  expect(screen.getByText('Før: Mangler opplysninger / ingen oppføring')).toBeInTheDocument()
  expect(screen.getByText('Etter: Kjent utilgjengelig')).toBeInTheDocument()
  fireEvent.click(screen.getByRole('button', { name: 'Last inn oppdaterte vaktdata' }))
  await screen.findByRole('heading', { name: 'Planlagt uke 5' })
  await waitFor(() => expect(screen.getByRole('button', { name: 'Datagrunnlag' })).toBeEnabled())
  fireEvent.click(screen.getByRole('button', { name: 'Datagrunnlag' }))
  expect(screen.getByLabelText('Nytt datasett')).toHaveValue(info.id)
  fireEvent.click(screen.getByRole('button', { name: 'Forhåndsvis endringer' }))
  await screen.findByRole('button', { name: 'Last inn oppdaterte vaktdata' })
  const last = fetchMock.mock.calls.filter(([url]) => url === '/api/datasets/compare').at(-1)!
  expect(JSON.parse(String(last[1]?.body))).toEqual({ previous_id: updatedInfo.id, next_id: info.id })
})
