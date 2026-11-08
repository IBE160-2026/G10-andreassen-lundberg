import type { Absence, Alternative, Basis, Dataset } from './api'

export interface Selection {
  key: string; basis: Basis; target: string; alternative: Alternative
  sent: boolean; responses: Record<string, 'venter' | 'akseptert' | 'avslått'>
}
export function basisKey(basis: Basis, target: string): string {
  return JSON.stringify([basis.dataset_id, basis.version,
    [...new Set(basis.absences.map(a => JSON.stringify([a.employee_id, a.shift_id])))].sort(), target])
}
export function selectionKey(basis: Basis, target: string, alternative: Alternative, loadId = 0): string {
  return JSON.stringify([loadId, basisKey(basis, target), alternative.id])
}
export function preserveAbsences(absences: Absence[], data: Pick<Dataset, 'assignments' | 'shifts' | 'assessment_time' | 'week_start' | 'week_end'>): Absence[] {
  return absences.filter(a => {
    const assignment = data.assignments.find(t => t.employee_id === a.employee_id && t.shift_id === a.shift_id)
    const shift = data.shifts.find(s => s.id === a.shift_id)
    return !!assignment && !!shift && +new Date(shift.start) >= +new Date(data.week_start) &&
      +new Date(shift.start) < +new Date(data.week_end) &&
      (assignment.absent || +new Date(shift.start) > +new Date(data.assessment_time))
  })
}
export function offerStatus(selection: Selection): string {
  if (!selection.sent) return 'Aksept ikke simulert'
  const responses = selection.alternative.affected_employee_ids.map(id => selection.responses[id])
  if (responses.includes('avslått')) return 'Avslått – ikke full simulert aksept'
  if (responses.every(value => value === 'akseptert')) return 'Full simulert aksept'
  return 'Venter på svar – ikke full simulert aksept'
}
