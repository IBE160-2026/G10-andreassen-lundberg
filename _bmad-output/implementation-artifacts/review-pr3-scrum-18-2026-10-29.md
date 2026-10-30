# Kodegjennomgang av PR #3 (SCRUM-18: kodeskjelett, CI og arkitektur)

*(Skrevet: Claude · 29.10.26, med `bmad-code-review`. Gjennomgangen er utført av
KI-lag med samme modell som skrev koden, og er ikke en uavhengig menneskelig
gjennomgang. Funnene er kontrollert mot koden på grenen
`scrum-18-kodeskjelett` (commit `1958161`).)*

**Omfang:** PR #3 mot `origin/main` (f967a96), 44 filer og 746 linjer uten
låsfilene `backend/uv.lock` og `frontend/package-lock.json`. Spesifikasjon:
[PRD-en](../planning-artifacts/prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md).
Lag: Blind Hunter, Edge Case Hunter, Verification Gap og Acceptance Auditor.

**Resultat:** 2 avgjørelser, 7 rettelser, 4 utsatt, 14 avvist. Ingen rettelser er
utført. Skjelettet bryter ingen krav i PRD-en som det skulle ha dekket; mye av
«ikke dekket ennå» (R1–R5, søk, UX, E2E-test) er forventet og regnes ikke som feil.

## Avgjørelser

- **D1. Arkitekturvalg uten godkjenning.** `docs/arkitektur.md` presenterer
  uv, ruff, Vitest, oxlint og modulgrensene som fastsatt, mens memlog sier at de
  er forslag. **Avgjort av Odin 29.10.26: godkjent som de står.** Stian er ikke
  konsultert. Dokumentet får en statuslinje med dette når PR-en oppdateres.
- **D2. Ingen felles feilhåndtering etter NFR-3** (norske meldinger og feilkode
  for valideringsfeil og uventede feil). **Avgjort av Odin 29.10.26: utsettes til
  første endepunkt med input (FR-3, SCRUM-22).**

## Rettelser (ikke utført)

| # | Funn | Sted |
|---|---|---|
| P1 | `DatasetRepository` kaster rå `JSONDecodeError`/`KeyError`/`ValidationError` ved én ødelagt fil og gir 500 for alle datasettendepunkter. Duplikat-id og manglende `data_dir` oppdages ikke. Mangler tester. (FR-1, NFR-3.) HTTP-delen av meldingene følger D2. | `backend/src/vaktmatch/data/repository.py` |
| P2 | Ingen test for miljøkontrakten (`VAKTMATCH_`-prefiks, `.env`, tomme verdier i `.env.example`). | `backend/tests` |
| P3 | README-testblokken kan ikke kopieres som den står (`cd frontend` kjøres fra `backend/`) og mangler `ruff format --check`. (NFR-1.) | `README.md` |
| P4 | `.env.example` mangler `VAKTMATCH_CORS_ORIGINS` (JSON-liste), og relativ `VAKTMATCH_DATA_DIR` følger arbeidsmappen. | `backend/.env.example` |
| P5 | CI mangler `permissions: contents: read` og tidsavbrudd. | `.github/workflows/ci.yml` |
| P6 | `App.test.tsx` mangler `cleanup()`, og Vitest uten `globals` rydder ikke automatisk. | `frontend/src/App.test.tsx` |
| P7 | Nettverksfeil viser nettleserens engelske «Failed to fetch» i norsk grensesnitt. (NFR-9.) | `frontend/src/api.ts`, `App.tsx` |

## Utsatt

- **W1.** `Explainer.explain(status)` er for smal for FR-12, FR-17 og FR-18; inputtypen må endres. SCRUM-40/39.
- **W2.** Fallback til regelbasert forklaring varsles ikke til brukeren (FR-19), og provider uten nøkkel går stille. Doc-kommentaren lover fallback ved feil. SCRUM-41/59.
- **W3.** `ControlStatus` har ASCII-verdier («bestatt») synlige i API-et; visningsetikett trengs før UI. SCRUM-30/34.
- **W4.** To memlog-innslag i PR-en er ført etter et nyere innslag og datert bakover, og det ene sier at en tidligere versjon var redigert for hånd. Rettes med et `override`-innslag, ikke ved omskriving.
- **D2-oppfølging.** Felles feilhåndtering (se over).

## Avvist

- **false:** «Låsfiler mangler» og «avhengigheter ikke pinnet». Filene finnes i PR-en; de var utelatt fra diffen som ble gitt til gjennomgangen.
- **Lav, ikke verdt kompleksiteten:** abort/timeout i `useEffect`, ikke-JSON-svar, bred CORS og manglende CORS-test (CORS brukes ikke med Vite-proxy), import-tids `create_app()` (feiler tydelig), pakking av `data/` i wheel, rester fra Vite-malen, flytende versjonstagger i Actions, at hvert kall leser alle datasettfilene, `explain` importerer `config`, ingen håndheving av modulgrenser, og at endringsloggen ikke er oppdatert (PR-en endrer ikke produktbriefen).
