import { render, screen } from '@testing-library/react'
import { afterEach, expect, test, vi } from 'vitest'
import App from './App'

afterEach(() => {
  vi.unstubAllGlobals()
})

test('viser backendstatus når API-et svarer', async () => {
  vi.stubGlobal(
    'fetch',
    vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ status: 'ok', version: '0.1.0', explainer: 'regelbasert' })),
    ),
  )

  render(<App />)

  expect(await screen.findByText(/Backend 0\.1\.0 kjører/)).toBeInTheDocument()
})

test('viser feilmelding når backend ikke svarer', async () => {
  vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response('', { status: 503 })))

  render(<App />)

  expect(await screen.findByText(/Får ikke kontakt med backend/)).toBeInTheDocument()
})
