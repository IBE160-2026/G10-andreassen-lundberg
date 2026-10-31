# Arkitektur – VaktMatch

*(Skrevet: Claude Code · 25.10.26, SCRUM-18. Bygger på [teknologivalg](teknologivalg.md).)*

Modulgrensene og verktøyvalgene uv, ruff, Vitest og oxlint ble godkjent av
Odin 29.10.26 innenfor delegert myndighet; dette er ikke en ny felles
detaljbeslutning. Se [gjennomgangen](../_bmad-output/implementation-artifacts/review-pr3-scrum-18-2026-10-29.md).
Felles HTTP-feilhåndtering leveres i SCRUM-22. Datalaget avviser ugyldige
metadata med fil-/mappekontekst; dette erstatter ikke den kommende API-kontrakten.

VaktMatch er en lokal webapp med en Python-backend (FastAPI) og en
React-frontend. All regelberegning skjer i backend. Frontend viser resultatene
og sender lederens valg. Forklaringslaget leser ferdige kontrollresultater og
kan aldri endre dem.

```
frontend (React)  ──HTTP /api──▶  api  ──▶  data      (leser datasett)
                                       ├─▶  rules     (R1–R5, søk, status)
                                       └─▶  explain   (regelbasert / språkmodell)
```

## Moduler og grenser

| Modul | Ansvar | Kan bruke | Skal ikke |
|---|---|---|---|
| `backend/src/vaktmatch/data` | Lese og validere demodatasett (JSON) og, senere, valgfri beslutningslogg. | Pydantic | Kjenne regler, HTTP eller KI. Endre datasettfilene. |
| `backend/src/vaktmatch/rules` | Kontroll mot R1–R5, søk ved frafall, dekning/kontroll/søkestatus, sortering P1/P2. | Datamodellene fra `data` | Gjøre I/O, kalle KI eller avhenge av FastAPI. |
| `backend/src/vaktmatch/explain` | Forklaring i fast svarformat. Regelbasert standard; språkmodell bak samme grensesnitt (`Explainer`). | Resultater fra `rules` | Endre status, rangering eller valg. Være nødvendig for at appen virker. |
| `backend/src/vaktmatch/api` | HTTP-endepunkter under `/api`; setter sammen lagene. | Alle lag over | Inneholde regellogikk. |
| `frontend/src` | Visning, innstillinger og lederens valg. `api.ts` er eneste sted med kall mot backend. | `/api` | Beregne regelstatus selv. |

Grensene gjør at en senere samtaleassistent kan bruke de samme funksjonene i
`data`, `rules` og `explain` uten å gå via grensesnittet (jf. «Tilrettelegging
for senere chat» i [produktbriefen](../productbrief.md#scope)).

## Konfigurasjon og hemmeligheter

Innstillinger leses fra miljøvariabler med prefikset `VAKTMATCH_`
(`backend/src/vaktmatch/config.py`), eventuelt fra en lokal `backend/.env`.
`.env` er ignorert av Git; [`backend/.env.example`](../backend/.env.example)
viser tilgjengelige variabler uten verdier. Uten språkmodellnøkkel brukes
regelbaserte forklaringer, så kjerneflyten krever ingen konto eller nøkkel.

## Data

Demodatasett ligger i `backend/data/datasets/` som versjonerte JSON-filer.
`skjelett.json` er en plassholder med bare metadata og erstattes i SCRUM-20.
Datamodellen for ansatte, vakter, kompetanse og behov defineres i SCRUM-19.
Lagring av den valgfrie beslutningsloggen (forslag: SQLite utenfor Git)
avgjøres i SCRUM-54.

## Kvalitetssikring

- Backend: pytest (`backend/tests`), ruff for lint og formatering.
- Frontend: Vitest med Testing Library, oxlint, TypeScript-bygg.
- CI (`.github/workflows/ci.yml`) kjører alt ved push til `main` og på pull requests.
- Regelmotoren testes mot fasit i demoscenarioene (SCRUM-28).

## Avvik og åpne punkter

- Språkmodell er ikke valgt (SCRUM-59); `get_explainer` faller alltid tilbake
  til regelbasert inntil en leverandør er implementert.
- Visuelt uttrykk er bare en midlertidig grunnstil (SCRUM-42, SCRUM-47).
