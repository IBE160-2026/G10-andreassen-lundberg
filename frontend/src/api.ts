// Alle kall til backend går herfra. Frontend beregner aldri regelstatus selv.

export interface Health {
  status: string
  version: string
  explainer: string
}

export async function fetchHealth(): Promise<Health> {
  let response: Response
  try {
    response = await fetch('/api/health')
  } catch {
    throw new Error('Backend er utilgjengelig. Kontroller at serveren kjører.')
  }
  if (!response.ok) {
    throw new Error(`Backend svarte ${response.status}`)
  }
  return response.json()
}
