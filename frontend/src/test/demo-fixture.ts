// Små kontraktfiksturer for grensesnittets tilstandsoverganger.
// Regel- og kostnadsfasit verifiseres mot de komplette datasettene i backendtestene.
import type { Alternative, Dataset, DatasetInfo, Evaluation } from '../api'

export const info: DatasetInfo = { id: 'hovedscenario', version: '1.0', title: 'Demodata', family_id: 'hoved', description: 'Syntetiske testdata' }
export const updatedInfo: DatasetInfo = { ...info, id: 'komplettert', version: '2.0', title: 'Komplettert' }
const interval = { start: '2026-10-14T08:00:00+02:00', end: '2026-10-14T16:00:00+02:00' }
export const dataset: Dataset = {
  dataset: info, assessment_time: '2026-10-14T07:00:00+02:00', week_start: '2026-10-12T00:00:00+02:00', week_end: '2026-10-19T00:00:00+02:00',
  coverage_start: '2026-09-14T00:00:00+02:00', coverage_end: '2026-10-21T00:00:00+02:00',
  employees: ['A01','A02','A03'].map(id => ({ id, name: `${id} · eksempelperson`, kind: 'internal', skills: ['K1'], availability: [interval], contract_hours: '40', hourly_rate: '200', work_context_complete: true, history_complete: true, history_source: 'Testgrunnlag' })),
  shifts: [{ ...interval, id: 'X', required_skill: 'K1', required_count: 1 }],
  assignments: [{ id: 'T-X', employee_id: 'A01', shift_id: 'X', absent: false, locked: false }],
  coverage: [{ shift_id: 'X', assigned: ['A01'], required: 1, uncovered: 0 }], current_controls: [],
}
export function alternative(id: string, hours: string): Alternative {
  return { id, candidate_id: id, kind: 'direkte', moves: 0, control_status: 'bestatt', complete: true, coverage_status: 'full', selectable: true,
    affected_employee_ids: [id], affected_shift_ids: ['X'], plan: [{ shift_id: 'X', before: [], after: [id] }], uncovered: [],
    consequences: [{ employee_id: id, hours_before: '24', hours_after: hours, hours_complete: true, rest_before: [], rest_after: [], rules: [], missing: [], control_status: 'bestatt', period_start: dataset.week_start, period_end: dataset.week_end }],
    cost: { currency: 'NOK', complete: true, total: '1800', reference: '0', difference: '1800', known_subtotal: '1800', missing: [], omitted: ['Syntetiske satser'], assignments: [], reference_assignments: [] },
    p1: hours, p2: '1', rank: id === 'A02' ? 1 : 2, sorting_missing: [], history: [], coverage_reason: '', replacement_findings: [],
    explanation: { short_answer: 'Oppfyller scenarioreglene.', tradeoff: 'Ingen flytting.', consequences: 'Vaktlisten er uendret.', uncertainty: 'Syntetiske data.' },
  }
}
export const evaluation: Evaluation = {
  dataset_id: info.id, version: info.version, absences: [{ employee_id: 'A01', shift_id: 'X' }], target_shift_id: 'X', search_limit: 1, criteria: ['P1'],
  assessment_time: dataset.assessment_time, search_status: 'fullfort', message: 'Søket er fullført innenfor valgt søkeomfang.',
  alternatives: [alternative('A02','32'), alternative('A03','40')], coverage: [{ shift_id: 'X', required: 1, assigned: [], uncovered: 1 }], combinations_examined: 3, duration_ms: 1,
}
