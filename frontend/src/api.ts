// HTTP er samlet her. Alle kontroll-, deknings-, sorterings- og kostnadstall kommer fra backend.
export type DecimalValue = string | number
export type ControlStatus = 'bestatt' | 'regelavvik' | 'uavklart'
export type Criterion = 'P1' | 'P2'
export interface Health { status: string; version: string; explainer: string }
export interface DatasetInfo {
  id: string; version: string; title: string; description: string; family_id: string
}
export interface Interval { start: string; end: string }
export interface Employee {
  id: string; name: string; kind: 'internal' | 'external'; skills: string[] | null
  availability: Interval[] | null; contract_hours: DecimalValue | null; hourly_rate: DecimalValue | null
  work_context_complete: boolean; history_complete: boolean; history_source: string
}
export interface Shift extends Interval { id: string; required_skill: string; required_count: number }
export interface Assignment { id: string; employee_id: string; shift_id: string; locked: boolean; absent: boolean }
export interface Absence { employee_id: string; shift_id: string }
export interface Coverage { shift_id: string; required: number; assigned: string[]; uncovered: number }
export interface Rule {
  rule: string; status: ControlStatus | 'ikke_vurdert'; value: string; explanation: string
  source: string; limitation: string
}
export interface Rest {
  shift_id: string; before_hours: DecimalValue | null; after_hours: DecimalValue | null
  previous_shift_id: string | null; next_shift_id: string | null
  before_known: boolean; after_known: boolean; collision: boolean
}
export interface Consequence {
  employee_id: string; hours_before: DecimalValue; hours_after: DecimalValue; hours_complete: boolean
  rest_before: Rest[]; rest_after: Rest[]; rules: Rule[]; missing: string[]
  control_status: ControlStatus; period_start: string; period_end: string
}
export interface Dataset {
  dataset: DatasetInfo; assessment_time: string; week_start: string; week_end: string
  coverage_start: string; coverage_end: string; employees: Employee[]; shifts: Shift[]
  assignments: Assignment[]; coverage: Coverage[]; current_controls: Consequence[]
}
export interface CostAssignment {
  employee_id: string; shift_id: string; amount: DecimalValue | null; missing: string[]
  segments: (Interval & { hours: DecimalValue; rate: DecimalValue | null; supplement: DecimalValue | null; amount: DecimalValue | null })[]
}
export interface Cost {
  currency: string; complete: boolean; total: DecimalValue | null; reference: DecimalValue | null
  difference: DecimalValue | null; known_subtotal: DecimalValue; missing: string[]; omitted: string[]
  assignments: CostAssignment[]; reference_assignments: CostAssignment[]
}
export interface Explanation { short_answer: string; tradeoff: string; consequences: string; uncertainty: string }
export interface Alternative {
  id: string; candidate_id: string; kind: 'direkte' | 'flytting' | 'delvis'; moves: number
  control_status: ControlStatus; coverage_status: 'full' | 'delvis'; complete: boolean; selectable: boolean
  affected_employee_ids: string[]; affected_shift_ids: string[]
  plan: { shift_id: string; before: string[]; after: string[] }[]; uncovered: Coverage[]
  consequences: Consequence[]; cost: Cost; p1: DecimalValue | null; p2: DecimalValue | null
  rank: number | null; sorting_missing: string[]; explanation: Explanation
  coverage_reason: string; replacement_findings: { employee_id: string; control_status: ControlStatus; findings: string[] }[]
  history: { employee_id: string; weeks: (Interval & { week: number; known_hours: DecimalValue; shift_ids: string[]; source: string; complete: boolean; limitation: string })[] }[]
}
export interface Basis { dataset_id: string; version: string; absences: Absence[] }
export interface EvaluationInput extends Basis { target_shift_id: string; search_limit: 0 | 1; criteria: Criterion[] }
export interface Evaluation extends EvaluationInput {
  assessment_time: string; search_status: 'fullfort' | 'avbrutt' | 'utenfor_omfang'; message: string
  coverage: Coverage[]; alternatives: Alternative[]; combinations_examined: number; duration_ms: number
}
export interface DatasetComparison {
  previous: DatasetInfo; next: DatasetInfo; same_family: boolean; unchanged: boolean
  changes: { category: string; id: string; field: string; before: unknown; after: unknown; label: string; before_label: string; after_label: string }[]
}

export const REQUEST_TIMEOUT_MS = 15_000
class ApiError extends Error {}

async function request<T>(path: string, body?: unknown, signal?: AbortSignal): Promise<T> {
  const controller = new AbortController()
  let timedOut = false
  const cancelled = new Promise<never>((_, reject) => {
    controller.signal.addEventListener('abort', () => reject(new Error(timedOut ?
      'Backend svarte ikke innen tidsfristen. Prøv igjen.' : 'Forespørselen ble avbrutt. Prøv igjen.')), { once: true })
  })
  const cancel = () => controller.abort()
  signal?.addEventListener('abort', cancel, { once: true })
  if (signal?.aborted) cancel()
  const timer = setTimeout(() => { timedOut = true; controller.abort() }, REQUEST_TIMEOUT_MS)
  const operation = async () => {
    let response: Response
    try {
      response = await fetch(`/api${path}`, body === undefined ? { signal: controller.signal } : {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body), signal: controller.signal,
      })
    } catch {
      throw new ApiError('Backend er utilgjengelig. Kontroller at serveren kjører og prøv igjen.')
    }
    if (!response.ok) {
      const error = await response.json().catch(() => ({}))
      throw new ApiError(error.message || 'Backend kan ikke fullføre handlingen. Prøv igjen.')
    }
    try { return await response.json() as T }
    catch { throw new ApiError('Backend ga et uleselig svar. Prøv igjen.') }
  }
  try {
    return await Promise.race([cancelled, operation()])
  } finally {
    clearTimeout(timer)
    signal?.removeEventListener('abort', cancel)
  }
}

export const fetchHealth = () => request<Health>('/health')
export const fetchDatasets = (signal?: AbortSignal) => request<DatasetInfo[]>('/datasets', undefined, signal)
export const fetchDataset = (id: string, signal?: AbortSignal) => request<Dataset>(`/datasets/${encodeURIComponent(id)}/state`, undefined, signal)
export const refreshState = (basis: Basis) => request<Dataset>('/state', basis)
export const simulateAbsence = (basis: Basis, absence: Absence) => request<Basis & { coverage: Coverage[]; message: string }>('/absences/simulate', { ...basis, absence })
export const previewAbsence = (basis: Basis, employee_id: string, start_shift_id: string, calendar_days: number, signal?: AbortSignal) => request<Interval & { affected: { shift: Shift; eligible: boolean; limitation: string }[] }>('/absences/preview', { ...basis, employee_id, start_shift_id, calendar_days }, signal)
export const evaluate = (body: EvaluationInput) => request<Evaluation>('/evaluate', body)
export const compareDatasets = (previous_id: string, next_id: string) => request<DatasetComparison>('/datasets/compare', { previous_id, next_id })
export const explain = (body: EvaluationInput, alternative_id: string) => request<{ mode: string; message: string; explanation: Explanation; reference_id: string | null }>('/explain', { ...body, alternative_id })
