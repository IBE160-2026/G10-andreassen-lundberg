import { expect, test } from 'vitest'
import { alternative, dataset } from './test/demo-fixture'
import { basisKey, offerStatus, preserveAbsences, selectionKey, type Selection } from './session'

test('alle berørte må akseptere; avslag og ventende er separate tilstander', () => {
  const proposal = alternative('B','8'); proposal.affected_employee_ids = ['B','C']
  const selection: Selection = { key: 'test', basis: { dataset_id: 'demo', version: '1', absences: [] }, target: 'X', alternative: proposal, sent: false, responses: {} }
  expect(offerStatus(selection)).toBe('Aksept ikke simulert')
  selection.sent = true; selection.responses = { B: 'akseptert', C: 'venter' }
  expect(offerStatus(selection)).toContain('Venter på svar')
  selection.responses.C = 'avslått'
  expect(offerStatus(selection)).toContain('Avslått')
  selection.responses.C = 'akseptert'
  expect(offerStatus(selection)).toBe('Full simulert aksept')
})

test('kanoniske fravær og konkrete forslag/versjoner avgrenser svar', () => {
  const basis = { dataset_id: 'demo', version: '1', absences: [{ employee_id: 'A', shift_id: 'B:C' }] }
  expect(basisKey(basis,'X')).not.toBe(basisKey({ ...basis, absences: [{ employee_id: 'A:B', shift_id: 'C' }] },'X'))
  expect(basisKey(basis,'X')).toBe(basisKey({ ...basis, absences: [...basis.absences, ...basis.absences] },'X'))
  expect(selectionKey(basis,'X',alternative('A02','32'))).not.toBe(selectionKey({ ...basis, version: '2' },'X',alternative('A02','32')))
})

test('fravær bevares bare på framtidig eller kildeført gyldig tildeling', () => {
  const absences = [{ employee_id: 'A01', shift_id: 'X' }]
  const advanced = { ...dataset, assessment_time: '2026-10-14T09:00:00+02:00' }
  expect(preserveAbsences(absences, dataset)).toEqual(absences)
  expect(preserveAbsences(absences, advanced)).toEqual([])
  expect(preserveAbsences(absences, { ...advanced, assignments: dataset.assignments.map(a => ({ ...a, absent: true })) })).toEqual(absences)
  expect(preserveAbsences(absences, { ...advanced, assignments: [] })).toEqual([])
  expect(selectionKey({ dataset_id: 'demo', version: '1', absences }, 'X', alternative('A02','32'), 1)).not.toBe(
    selectionKey({ dataset_id: 'demo', version: '1', absences }, 'X', alternative('A02','32'), 2))
})
