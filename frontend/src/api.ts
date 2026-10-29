// Alle kall til backend går herfra. Frontend beregner aldri regelstatus selv.

export interface Health {
  status: string
  version: string
  explainer: string
}

export async function fetchHealth(): Promise<Health> {
  const response = await fetch('/api/health')
  if (!response.ok) {
    throw new Error(`Backend svarte ${response.status}`)
  }
  return response.json()
}
