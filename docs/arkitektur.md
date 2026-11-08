# Arkitektur – VaktMatch

*(Skrevet: Claude Code · 25.10.26, SCRUM-18. Bygger på [teknologivalg](teknologivalg.md).)*

Modulgrensene og verktøyvalgene uv, ruff, Vitest og oxlint ble godkjent av
Odin 29.10.26 innenfor delegert myndighet; dette er ikke en ny felles
detaljbeslutning. Se [gjennomgangen](../_bmad-output/implementation-artifacts/review-pr3-scrum-18-2026-10-29.md).
SCRUM-19 er implementert 08.11.2026 av Codex på Odins gjennomføringsmandat.
Den [delte data-/HTTP-kontrakten](api-demoflyt.md) konkretiserer den eksisterende
produktretningen. API-et oversetter feil til norsk 404/409/422/503 uten å lekke
filstier. Dette er implementeringsvalg, ikke en ny felles produktbeslutning.

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
| `backend/src/vaktmatch/rules` | Rene R1–R5-kontroller, søk 0/1, dekning, sortering P1/P2, historikk og syntetisk kostnad. | Datamodellene fra `data` | Gjøre I/O, kalle KI eller avhenge av FastAPI. |
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

Elleve fullstendige, versjonerte syntetiske scenarioer ligger i
`backend/data/datasets/`; metadataplassholderen er erstattet. `schema.py` validerer
tidssoner, intervaller, referanser, unike ID-er, satser og arbeidsperioden.
`backend/data/generate_demo.py` dokumenterer og kan manuelt gjenskape filene;
API-et kjører aldri generatoren og skriver aldri til datasettfilene.

Timer og overlapp beregnes i UTC, med lokal visning og kalenderavgrensning i
Europe/Oslo. `tzdata` følger backend også på Windows. Uketimer bruker bare faktisk
overlapp med arbeidsuken; hvile bruker også uke 4/6 og bekreftet kontrollperiode.
Kostnad bruker `Decimal`, deler på tilleggsgrenser og avrunder halv opp per
tildeling før summering. Desimaler over HTTP er strenger.

Ukjent (`null`) skilles fra kjent tom liste. Kjent brudd har forrang ved
ufullstendig grunnlag. Rene sluttplaner bygges uten å mutere input; låste,
påbegynte og historiske tildelinger flyttes aldri. Alle berørte kontrolleres i
sluttplanen. Andre eksisterende bemanningshull er fortsatt synlige.

API-et er tilstandsløst. React beholder aktive fravær, utkast, søkeinnstillinger,
valg og tilbud/svar i fanens minne. Nøklene inkluderer innlastingsnummer,
datasett-ID/versjon, kanoniske fravær, målskift og stabil forslag-ID. Et gjeldende
valg må finnes som komplett/bestått i ferskt resultat. Bytte mellom forslag
A → B → A kan gjenbruke svar innen samme innlasting; nye datainnlastinger
krever nye svar, også ved retur til et tidligere datasett.
Datasettbytte bevarer gyldige fravær i samme scenariofamilie og arkiverer valg/svar.
Sene svar ignoreres, navigasjon sperres under handlinger og klientforespørsler
avsluttes etter 15 sekunder. Ingen `localStorage`, varig beslutningslogg eller ekte tilbud
er implementert; varig logg er fortsatt utsatt.

## Kvalitetssikring

- Backend: pytest (`backend/tests`), ruff for lint og formatering.
- Frontend: Vitest med Testing Library, oxlint, TypeScript-bygg.
- CI (`.github/workflows/ci.yml`) kjører alt ved push til `main` og på pull requests.
- Regelmotoren testes mot fasit, kostnad, grenser og datamangler i demoscenarioene.
- Frontendtestene verifiserer tilstandsoverganger og brukergrensesnittets API-kontrakt;
  de erstatter ikke backendfasit eller faktisk nettleserflyt.
- [Kontrollrapporten](demoflyt-kontrollrapport-2026-11-08.md) viser kjørte kontroller og nettlesergrunnlag.

## Avvik og åpne punkter

- Språkmodell er ikke valgt (SCRUM-59); `get_explainer` faller alltid tilbake
  til regelbasert inntil en leverandør er implementert.
- Den responsive appen bruker DESIGN.md/EXPERIENCE.md fra SCRUM-47, med native
  kontroller, synlig fokus og eksplisitte demohandlinger.
- Søket er avgrenset til ett målskift/en manglende plass og høyst én flytting.
  Ingen solver, vaktdeling, full lovkontroll eller samlet løsning for flere fravær.
