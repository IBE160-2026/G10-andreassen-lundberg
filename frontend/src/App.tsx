import { useEffect, useState } from 'react'
import { fetchHealth, type Health } from './api'

type BackendState =
  | { kind: 'loading' }
  | { kind: 'ok'; health: Health }
  | { kind: 'error'; message: string }

function App() {
  const [backend, setBackend] = useState<BackendState>({ kind: 'loading' })

  useEffect(() => {
    fetchHealth()
      .then((health) => setBackend({ kind: 'ok', health }))
      .catch((error: Error) => setBackend({ kind: 'error', message: error.message }))
  }, [])

  return (
    <main>
      <h1>VaktMatch</h1>
      <p>Beslutningsstøtte når en vakt mangler bemanning.</p>
      <p role="status">
        {backend.kind === 'loading' && 'Kobler til backend …'}
        {backend.kind === 'ok' &&
          `Backend ${backend.health.version} kjører (forklaring: ${backend.health.explainer}).`}
        {backend.kind === 'error' && `Får ikke kontakt med backend: ${backend.message}`}
      </p>
    </main>
  )
}

export default App
