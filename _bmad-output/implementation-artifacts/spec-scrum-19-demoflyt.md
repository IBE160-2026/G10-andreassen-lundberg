---
title: 'SCRUM-19: kjørbar demoflyt fra fravær til kontrollert alternativ'
type: feature
created: 2026-11-08
status: done
route: dispatch
review_loop_iteration: 0
baseline_commit: 3277c041f56d08e66232b2408bfd077747c43795
context:
  - '{project-root}/AGENTS.md'
  - '{project-root}/docs/demoscenario-fravaer.md'
  - '{project-root}/docs/forslag-ved-frafall.md'
  - '{project-root}/docs/kostnadsanslag.md'
  - '{project-root}/docs/arkitektur.md'
  - '{project-root}/docs/api-demoflyt.md'
  - '{project-root}/_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/DESIGN.md'
  - '{project-root}/_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/EXPERIENCE.md'
---

<frozen-after-approval reason="Eksisterende produktgrunnlag og Odins gjennomføringsmandat; ikke særskilt punktgodkjent spesifikasjon">

## Intent

Appen viser bare backendstatus. Gjør den til en lokal, etterprøvbar demoflyt:
registrer ett fravær, finn og sammenlign beregnede alternativer, undersøk og
velg, simuler svar og vurder igjen på nye data. Gjeldende UX brukes som kontrakt.

## Boundaries & Constraints

**Always:** R1–R5, P1/P2, dekning, søk og kostnad beregnes i rene backendfunksjoner.
Timer utledes fra konkrete tidssonebevisste vakter, med faktisk periodeoverlapp.
Kjent brudd har forrang for mangel. Historikk, påbegynte og andre låste tildelinger
flyttes aldri; låst målskift kan ha fravær. Bare komplett/bestått kan velges.
Vis alle berørte og kilder/mangler. Valg og svar nøkles til grunnlag og forslag.
Alle personer/satser er syntetiske; opphav er Codex på Odins mandat.

**Never:** Endre kildeplan eller datasettfiler gjennom API, beregn regelstatus
i frontend, arve aksept ved nytt grunnlag, innføre kostnadsrangering, skjule
mangler, velge skyleverandør eller kreve konto/nøkkel. Ingen varig logg,
leverandørintegrasjon, vaktdeling eller flyttegrense over 1.

## I/O & Edge-Case Matrix

| Tilfelle | Inndata | Resultat / feilbehandling |
|---|---|---|
| Hovedscenario | A01 fravær på X; grense 0 for S1, grense 1 for utvidet søk | S1: A02 24→32 t, hvile16/16; A03 32→40, hvile12/16. P1 A02 først, P2 A03 først. A04–08 avvik, V01 uavklart. Grense 1 undersøker også alle tillatte omfordelinger og kan gi annen rangering. |
| Mangler/grenser | Ukjent tilgjengelighet/arbeid, 11 t/40 t, kollisjon, ukegrense | Ukjent nødvendig grunnlag gir Uavklart; kjent brudd består. Lik grense består. Ingen overlapp ved slutt=start. |
| Én flytting | B på Y overlapper X; C kan bare Y | Grense0 gir ingen komplett; grense1 gir B→X/C→Y. Uten C vises Y udekket. Alle kontrolleres i sluttplan. |
| Kostnad | O1–O5 | Eksakte desimaler, intervalltillegg og avrunding per tildeling. Manglende sats gir ukjent total/differanse. |
| Ugyldig/utdatert | Feil ID/uke, startet målskift, manglende ansatt, gammel versjon | Norske felt-/API-feil, 404/409/422/503 etter kontrakt. Ingen krasj eller falske resultater. |
| Nye data/flere fravær | Tidligere valg/aksept og deretter oppdatering/nytt fravær | Bevar aktive fravær, vis endringer og historiske valg; ny kontroll uten arvet aksept. Forslag innføres aldri ved valg. |

</frozen-after-approval>

## Code Map

- `backend/src/vaktmatch/data/schema.py`, `repository.py`: eksisterende metadata beholdes; utvid med full validert modell/innlasting.
- `backend/src/vaktmatch/rules/`: eksisterende ControlStatus gjenbrukes; legg til rene kontroller, søk, kostnad og resultatmodeller.
- `backend/src/vaktmatch/api/routes.py`, `main.py`: dependency-oppsett finnes; HTTP setter sammen lagene og oversetter feil.
- `backend/src/vaktmatch/explain/`: eksisterende standardforklaring beholdes; nye forklaringer bygger på beregnede fakta.
- `frontend/src/api.ts`, `App.tsx`, `index.css`: alle fetch-kall i api.ts, React-komponenter presenterer API-resultater med UX-tokens.
- `backend/tests/`, `frontend/src/*.test.*`: eksisterende små tester utvides med fasit og meningsfulle regresjonstilfeller.

## Tasks & Acceptance

**Execution:**
- [x] `docs/api-demoflyt.md` — frys delt modell-/HTTP-kontrakt før implementering.
- [x] `backend/src/vaktmatch/data/`, `backend/data/datasets/` — validerte modeller, versjonerte fulle scenarioer og fasitgrunnlag.
- [x] `backend/src/vaktmatch/rules/`, `explain/` — kontroller, avgrenset søk, P1/P2, historikk og kostnad uten I/O.
- [x] `backend/src/vaktmatch/api/`, `main.py` — eksplisitt fravær, vurdering, datasettendringer og ærlig forklaringsreserve.
- [x] `frontend/src/` — komplett responsiv demoflyt med øktminne og foreldede forespørsler avvist.
- [x] `backend/tests/`, `frontend/src/` — fasit-, grense-, feil- og øktkontroller; kjør faktisk PC-/mobilflyt.
- [x] `README.md`, `docs/arkitektur.md`, kontrollrapport og memlog — oppstart, nye kontrakter, faktisk dekning og gjenstående grenser.

**Acceptance Criteria:**
- Given fullstendige demodata, when UJ-1/2 gjennomføres i appen, then resultatene følger kildefasiten og kildeplanen er uendret.
- Given manglende nødvendig grunnlag, when en kandidat undersøkes, then mangelen vises uten beståttstatus eller oppdiktet tall.
- Given valgt forslag og simulerte svar, when A→B→A eller nye data prøves, then svar bevares bare for riktig grunnlag og alle berørte må akseptere.
- Given ingen modellnøkkel eller stoppet backend, when relevante handlinger prøves, then norsk reserve/feil vises med vei videre.
- Given 360 px, tastatur og 200 % tekst, when hovedflyten brukes, then nødvendig informasjon og handlinger er tilgjengelige uten vannrett rulling.

### Review Findings – 2026-11-09

Ny vurdering på Odins oppdrag, med fire separate KI-lag og hovedagentens
etterkontroll. [Samlet rapport](review-status-2026-11-09.md) viser nye tester,
produktstatus og alle 14 individuelle dommer før gruppering. Ingen høye funn;
ni middels og to lave tiltak. Dette er vurdering, ikke utførte rettelser.

- [x] [Review][Patch] K1: Fungerende gjenforsøk ved feilet fraværsforhåndsvisning [frontend/src/App.tsx:141,154,177] — medium; oppfølging SCRUM-22/43. Rettet 09.11: dd046ad.
- [x] [Review][Patch] K2: Vis faktisk R4-brudd med vakt og hvileintervall [backend/src/vaktmatch/rules/engine.py:234,243] — medium; oppfølging SCRUM-26/30. Rettet 09.11: d37f92a.
- [x] [Review][Patch] K3: Identifiser konkret plan i valg og historikk [frontend/src/App.tsx:389,396] — medium; oppfølging SCRUM-52/53. Rettet 09.11: dd046ad.
- [x] [Review][Patch] K4: Bevar åpne øvrige funn og tilbakefokus [frontend/src/App.tsx:217,366] — medium; oppfølging SCRUM-33/42. Rettet 09.11: dd046ad.
- [x] [Review][Patch] K5: Behandle manglende scenariofamilie som ubekreftet [backend/src/vaktmatch/data/schema.py:16; backend/src/vaktmatch/api/routes.py:295] — medium; oppfølging SCRUM-19/23. Rettet 09.11: d37f92a.
- [x] [Review][Patch] K6: Verifiser lesbare differansefelt i API og frontend [backend/tests/test_demoflow.py:286; frontend/src/App.test.tsx:26] — medium; oppfølging SCRUM-28/43/57. Rettet 09.11: d37f92a, dd046ad.
- [x] [Review][Patch] K7: Test rekkefølgen på kombinerte P-kriterier [backend/src/vaktmatch/rules/engine.py:463; backend/tests/test_demoflow.py:51,95] — medium; oppfølging SCRUM-28/35/43. Rettet 09.11: d37f92a.
- [x] [Review][Patch] K8: Test sekundærkriteriet ved lik primærverdi [backend/tests/test_demoflow.py:95; backend/src/vaktmatch/rules/engine.py:463] — medium; oppfølging SCRUM-28/36/43. Rettet 09.11: d37f92a.
- [x] [Review][Patch] K9: Bevar riktig dato og separate benchmarkkjøringer [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark.py:32,39] — medium; oppfølging SCRUM-58. Rettet 09.11: c7679d8.
- [x] [Review][Patch] K10: Nullstill neste datasett ved innlasting [frontend/src/App.tsx:256,400] — low; oppfølging SCRUM-23/57. Rettet 09.11: dd046ad.
- [x] [Review][Patch] K11: Registrer kjøringens proveniens i nettleserrapport [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/verify-browser.py:242] — low; oppfølging SCRUM-43/44. Rettet 09.11: c7679d8, a706007, 1bbfdec.

Etterkontroll 09.11.2026 (Claude Code på Stians oppdrag): alle elleve tiltak
er rettet med regresjonstester. Hver ny test er kontrollert mot mutasjonen fra
gjennomgangen og feiler når rettingen fjernes. Backend 70 tester, frontend 24
tester, lint, format og build bestått; nettleserkontrollen 39/39 uten axe. Se
[etterkontrollen i rapporten](review-status-2026-11-09.md#etterkontroll-09112026).
Statusen er derfor satt tilbake til `done`; Må-restpunktene og KI-sporet følges
fortsatt i Jira og er ikke en del av denne spesifikasjonen.

#### Rejected

Ingen. 0 decision-needed, 11 patch, 0 defer. Alle lag fullførte.
Appkoden og tidligere kontrollhistorikk er uendret; nye åpne funn gir status
in-progress. Jira/sprint er bare lest og er ikke synkronisert av vurderingen.


## Implementation Notes

Planlagt på Odins autonome mandat 08.11.2026. Ingen irreversible handlinger.
Eksakte JSON-felter, nødvendige datagrenser og API-former er implementeringsvalg
i den delte kontrakten; ingen ny produktprioritering eller ansvarsendring.

Implementert gjennom én sekvensiell Build-overlevering. Felles kontrakt,
Pydantic-responsmodeller og ren regel-/forklaringsseparasjon beholdes.
Hovedagentens uavhengige sluttkjøring bestod 64 backendtester, 20 frontendtester,
ruff, oxlint og produksjonsbygg. Faktisk nettleserkontroll bestod 50
kontroller, inkludert elleve axe-pass på PC/mobil. Nye tester dekker hver
matriserad; se [kontrollrapporten](../../docs/demoflyt-kontrollrapport-2026-11-08.md).

## Spec Change Log

- 2026-11-08, Codex: Kildekontrollen rettet KI-matrisens uklare «grense 0/1»
  ved S1. Demoscenarioets hovedtabell gjelder uttrykkelig grense 0; grense 1
  inkluderer legitime omfordelinger som kan endre rangeringen. Dette er en
  rettelse av KI-spesifikasjonen etter den opprinnelige kilden, ikke endring
  av produktvalg eller tilpasning av tester til et feil resultat. Behold
  hovedtabellens eksakte direkte fasit og hele avgrensede søket ved grense 1.

## Review Triage Log

Alle tre lag er mottatt før triage: Blind Hunter (BH), Edge Case Hunter (EH)
og Verification Gap (VG). Samme modellkapasitet, separate kontekstfrie
KI-gjennomganger; dette er ikke en uavhengig menneskelig gjennomgang.

| Funn | Dom | Kontrollgrunnlag og konsekvens | Rute |
|---|---|---|---|
| BH1: samlet status tilskrevet hovedperson | medium | Kjørt B/F04-variant: B består, F04 har avvik, men teksten sier at B har avvik. Forveksler person og forslag. | patch |
| BH2: `P2 None` og manglende sorteringsforbehold | medium | Kjørt `mangler-p2`: sammenligning skriver None og rå andel; usikkerhetsfelt utelater manglende avtalte timer. | patch |
| BH3: gammel kollisjon gir dagens avvik | high | En ekstra overlapp i uke 1 endret A02s X-forslag til Regelavvik/R4 Ikke vurdert med uendret 16/16 t hvile. Strider mot H1. | patch |
| BH4: gammel aksept ved retur til data | high | Faktisk nettleserrepro: akseptert A02, hovedscenario→komplettert→hovedscenario, ny vurdering/valg; gammel full aksept gjenoppstår. | patch |
| BH5: gjenforsøk uten ny handling | medium | Hovedknappens handler kaller bare `setError('')` ved simulerings-, data- og forklaringsfeil. Ingen annen effekt avhenger av denne endringen. | patch |
| BH6: sent søk overtar navigasjonen | medium | `go` lar visning endres under busy uten å endre forespørsels-ID; søkets fullføring kaller alltid `go('alternatives')`. | patch |
| BH7: gamle kort merkes med nye kriterier | medium | Kortleseren bruker dagens `criteria`; etter grense-/kriterieendring er resultatets gamle rangering fortsatt synlig. | patch |
| BH8: nullhistorikk feilmerket komplett | medium | Validert datasett med kontrollstart lik ukestart og fullstendighetsflagg ga fire eldre uker med 0 timer/komplett. | patch |
| BH9: overført fravær blir tidsmessig ugyldig | medium | Hjelperen sjekker bare tildelingsparet; `/state` avviser gammelt simulert fravær når nytt vurderingstidspunkt passerer vakten. Gyldig oppdatering kan ikke lastes. | patch |
| BH10: ubegrenset nettventing | medium | Fetch har verken signal, avbrytelse eller tidsgrense. Et uavsluttet svar kan holde busy og handlingene låst. | patch |
| EH1: komplett flytting uten ny erstatter utelates | medium | Kjørt validert variant med B og F04 på Y: B→X/F04 igjen på Y er komplett, men bare B→X/C→Y/F04 beholdes når C kan svare. | patch |
| EH2: tidsmessig ugyldig overføring | medium | Samme konkrete kallkjede som BH9; oppgitt ny vurdering gjør den bevarte hendelsen ugyldig i API-et. | patch |
| EH3: historikk ved sommertidsskifte | medium | Validert novembervariant ga første historikkgrense 05.10 kl. 01 i Oslo, i stedet for lokal midnatt. Feil ukeavgrensning. | patch |
| EH4: manglende timeout/avbrytelse | medium | Samme hengende fetch og busy-kjede som BH10; ingen annen vakt eller gjenforsøk kan avslutte forespørselen. | patch |
| VG1: historikk kan forsvinne uten testfeil | medium | Forhåndsverifisert testgap: alle 56 tester bestod med 0 timer og tomme vakt-ID-er for hver historikkuke. | patch |
| VG2: nåværende kontroller kan forsvinne | medium | Forhåndsverifisert testgap: alle 56 tester bestod med tom `current_controls` fra begge state-innganger. | patch |

Etter individuell dom grupperes BH9/EH2 og BH10/EH4 etter samme rotårsak.
Øvrige funn har separate årsaker, også der de berører samme historikkfunksjon.
Alle rettelser gjelder demonstrerte tilstander innen eksisterende kontrakt,
uten nye endepunkter eller produktvalg. To høye og fjorten middels funn
gir fjorten avgrensede rettelsesoppgaver; ingen funn er avvist eller utsatt.

2026-11-08, Codex, etterkontroll: Alle fjorten rettelser er implementert.
Blind Hunter bekrefter BH1–BH10 løst; Edge Case Hunter bekrefter EH1–EH4 løst.
Verification Gap bekrefter VG1/VG2 med nye verdi-/medlemskapskontroller;
de tidligere prosesslokale mutasjonene gir nå henholdsvis tre og én testfeil.
Normal sluttkjøring er 64 backendtester, 20 frontendtester og 50 faktiske
nettleserkontroller uten feil, samt grønn lint/formatering og produksjonsbygg.
Alle elleve genererte datasett er kontrollert mot separate reproduksjoner.
Nettleserbevis og lokal tidsmåling er lenket fra kontrollrapporten.
Ingen nye funn eller utsatte rettelser; dette avslutter samme patch-rute.

## Verification

Backend: `uv run pytest`, `uv run ruff check .`, `uv run ruff format --check .`.
Frontend: `npm test`, `npm run lint`, `npm run build`.
Deretter faktisk backend+frontend med Playwright/axe på PC og 360 px, inkludert
fravær, P1/P2, én flytting, nye data, feil og tilbud. Dokumenter faktiske
resultater, ikke bare planlagt dekning. Ingen apppåstand bygger på den gamle mocken.
