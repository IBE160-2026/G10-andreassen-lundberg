import { afterEach, expect, test, vi } from 'vitest'
import { fetchDataset, fetchDatasets, REQUEST_TIMEOUT_MS } from './api'

afterEach(() => { vi.useRealTimers(); vi.unstubAllGlobals() })

test('tidsfrist avbryter en fetch som aldri svarer og tillater ny forespørsel', async () => {
  vi.useFakeTimers()
  const fetchMock = vi.fn(() => new Promise<Response>(() => {}))
  vi.stubGlobal('fetch', fetchMock)
  const request = fetchDatasets()
  const rejection = expect(request).rejects.toThrow('Backend svarte ikke innen tidsfristen. Prøv igjen.')
  await vi.advanceTimersByTimeAsync(REQUEST_TIMEOUT_MS)
  await rejection
  expect((fetchMock.mock.calls[0] as unknown as [string, RequestInit])[1].signal?.aborted).toBe(true)
  fetchMock.mockImplementation(() => Promise.resolve(new Response('[]')))
  await expect(fetchDatasets()).resolves.toEqual([])
})

test('samme tidsfrist omfatter venting på responsens JSON-body', async () => {
  vi.useFakeTimers()
  vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: () => new Promise(() => {}) }))
  const rejection = expect(fetchDatasets()).rejects.toThrow('Backend svarte ikke innen tidsfristen')
  await vi.advanceTimersByTimeAsync(REQUEST_TIMEOUT_MS)
  await rejection
})

test('kalleren kan avbryte en uavsluttet forespørsel', async () => {
  vi.stubGlobal('fetch', vi.fn(() => new Promise(() => {})))
  const controller = new AbortController()
  const rejection = expect(fetchDataset('demo', controller.signal)).rejects.toThrow('Forespørselen ble avbrutt')
  controller.abort()
  await rejection
})
