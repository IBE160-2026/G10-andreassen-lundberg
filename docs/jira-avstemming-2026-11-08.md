# Jira-avstemming etter lokal demoflyt

Codex · 08.11.2026 · utført på Odins oppdrag «avstem jira».
Dette avstemmer dokumentert arbeid mot eksisterende akseptansekriterier.
Det er ingen ny felles produktbeslutning eller godkjenning av hele MVP-en.

## Grunnlag og metode

Alle 60 saker ble lest, med gjeldende beskrivelser, statuser, ansvar og
kommentarer for de åpne sakene som berøres. Akseptansekriteriene er beholdt.
Implementering fra [14b187d](https://github.com/IBE160-2026/G10-andreassen-lundberg/commit/14b187d3c0ca375e72825d5c1b252e5380b53d22)
og UX fra [953729e](https://github.com/IBE160-2026/G10-andreassen-lundberg/commit/953729e)
er publisert på `scrum-19-demoflyt` gjennom `82b6254`.
Tildeling beholdes som ansvar for oppfølging; den betegner ikke hvem som
skrev implementeringen. Gjennomføringen er Codex sitt arbeid på Odins mandat.

[Kontrollrapporten](demoflyt-kontrollrapport-2026-11-08.md),
[HTTP-kontrakten](api-demoflyt.md), kode og automatiserte tester ble lest mot
sakskriteriene. Eksisterende bevis er 64 backendtester, 20 frontendtester og
50 kontroller av faktisk app, samt 95 separate UX-prototypekontroller.
Testene er ikke kjørt om igjen i denne dokument-/Jira-økten. Ingen ny PR-/main-CI
eller kjøring i en annen nettlesermotor påstås.

En implementering som er ferdig mot den avgrensede Build-spesifikasjonen,
kan fortsatt ha åpne kriterier i en bredere Jira-sak. `Done` brukes der sakens
aktuelle kriterier har konkret bevis. `In Review` markerer levert arbeid med
navngitt etterkontroll eller restpunkt; det betyr ikke at hele saken er godkjent.
Uimplementert/avventende arbeid beholder `To Do`. Ingen kildeplan, produktbrief,
PRD, ansvar, prioritet eller sprintplassering endres av avstemmingen.

## Sak for sak

Førstatus er hentet før endringene. Hver berørt sak får egen kort kommentar med
commit, konkret bevis, eventuelt restpunkt og lenker til allerede publisert grunnlag,
før statusen settes. Kommentarenes ID-er og lest-tilbake-status føres nedenfor.

| Sak | Før | Målstatus | Kontrollgrunnlag / restpunkt |
|---|---|---|---|
| [SCRUM-19](https://stiodi.atlassian.net/browse/SCRUM-19) — Definer datamodell for ansatte, vakter, kompetanse og behov | To Do | Done | Datamodellen representerer interne/eksterne ansatte, kompetanse, tilgjengelighet, nabovakter, avtalte timer, fravær, låser, versjon/vurderingstidspunkt og intervallbaserte satser/tillegg. Kode/bevis: [backend/src/vaktmatch/data/schema.py](../backend/src/vaktmatch/data/schema.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-20](https://stiodi.atlassian.net/browse/SCRUM-20) — Lag syntetisk demodatasett med fasit | To Do | In Review | Fasitvarianter i tester må kartlegges mot alle Må-tilfeller og versjonerte scenarioer. Kode/bevis: [backend/data/generate_demo.py](../backend/data/generate_demo.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-21](https://stiodi.atlassian.net/browse/SCRUM-21) — Vis datagrunnlaget (ansatte, vakter og bemanningsbehov for uken) | To Do | Done | Ukesoversikten viser vakttider, behov/kompetanse, tildelte ansatte, fravær, låser og antall udekkede plasser. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json). |
| [SCRUM-22](https://stiodi.atlassian.net/browse/SCRUM-22) — Tilfør sykefravær i demodataene | To Do | Done | Ansatt/vakt velges eksplisitt; simulering bevarer tidligere fravær, fjerner fraværende fra aktiv bemanning og gjør målskiftets udekkede plass synlig uten å endre kildefilen. Kode/bevis: [backend/src/vaktmatch/api/routes.py](../backend/src/vaktmatch/api/routes.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-23](https://stiodi.atlassian.net/browse/SCRUM-23) — Last inn oppdatert datasett og vurder situasjonen på nytt | To Do | Done | Faste versjonerte datasett med stabile ID-er forhåndsvises før innlasting. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [frontend/src/App.test.tsx](../frontend/src/App.test.tsx). |
| [SCRUM-24](https://stiodi.atlassian.net/browse/SCRUM-24) — Implementer navngitt scenarioregelsett med synlig regelgrunnlag | To Do | In Review | Navngitt regelsett og eksplisitt kategori per regel mangler i kontrakt/visning. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [frontend/src/App.tsx](../frontend/src/App.tsx). |
| [SCRUM-25](https://stiodi.atlassian.net/browse/SCRUM-25) — Kontroller kompetanse, tilgjengelighet og tidskollisjoner | To Do | Done | R1 kompetanse, R2 tilgjengelighet og R3 kollisjon kontrolleres med bestått/regelavvik/uavklart, konkrete verdier og begrunnelser. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-26](https://stiodi.atlassian.net/browse/SCRUM-26) — Beregn hviletid før/etter vakt og arbeidstid | To Do | Done | Timer før/etter beregnes fra faktisk UTC-overlapp i arbeidsuken; hvile før/etter bruker konkrete nabovakter og bekreftet dataperiode. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-27](https://stiodi.atlassian.net/browse/SCRUM-27) — Beregn konsekvenser for andre vakter | To Do | Done | Hvert alternativ er en egen hypotetisk sluttplan med før/etter-timer, hvile og R1–R5 for alle berørte, bemanning på X/Y og synlig udekket behov. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-28](https://stiodi.atlassian.net/browse/SCRUM-28) — Testsuite: regelmotor mot fasit i testscenarioene | To Do | In Review | Lokalt grønt; full Må-matrise og grønn CI for ny demokode må bekreftes. Kode/bevis: [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py), [.github/workflows/ci.yml](../.github/workflows/ci.yml). |
| [SCRUM-29](https://stiodi.atlassian.net/browse/SCRUM-29) — «Finn alternativer» åpner sammenligningsside for fraværet | To Do | In Review | Direkte inngang fra allerede fraværsmerket ukekort til riktig sammenligning må bekreftes/ferdigstilles. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [frontend/src/App.test.tsx](../frontend/src/App.test.tsx). |
| [SCRUM-30](https://stiodi.atlassian.net/browse/SCRUM-30) — Vis alternativer i fast svarformat | To Do | Done | Kort og detaljer viser fast sammenligning med regler, verdier, før/etter-timer/hvile, alle berørte, konsekvenser, mangler og kostnadsreferanse/differanse/dataversjon. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json). |
| [SCRUM-31](https://stiodi.atlassian.net/browse/SCRUM-31) — Vis udekket behov når ingen kandidat oppfyller reglene | To Do | Done | Faktisk udekket plass og forslagets dekning vises separat, sammen med valgt omfang og nødvendig manglende grunnlag. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [frontend/src/App.tsx](../frontend/src/App.tsx). |
| [SCRUM-32](https://stiodi.atlassian.net/browse/SCRUM-32) — Innstilling for søkeomfang | To Do | Done | Søkegrense 0/1 er valgbart, med 1 som standard/maksimum. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [frontend/src/App.test.tsx](../frontend/src/App.test.tsx). |
| [SCRUM-33](https://stiodi.atlassian.net/browse/SCRUM-33) — Undersøk enhver kandidat, også lavt rangerte og med avvik | To Do | Done | Alle viste forslag, også lavt rangerte, uavklarte, regelavvik og delvis dekning, kan åpnes med beregnede konsekvenser. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json). |
| [SCRUM-34](https://stiodi.atlassian.net/browse/SCRUM-34) — Vis manglende opplysninger og hva som gjør vurderingen sikrere | To Do | Done | Mangler er knyttet til berørt person/kontroll eller kostnads-/sorteringsgrunnlag og vises sammen med virkningen uavklart/ukjent total/manglende rang. Kode/bevis: [backend/src/vaktmatch/explain/demoflow.py](../backend/src/vaktmatch/explain/demoflow.py), [backend/tests/test_explain.py](../backend/tests/test_explain.py). |
| [SCRUM-35](https://stiodi.atlassian.net/browse/SCRUM-35) — Velg og prioriter sorteringskriterier | To Do | Done | P1/P2 kan aktiveres og ordnes, med bare P1 som standard og minst ett kriterium. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-36](https://stiodi.atlassian.net/browse/SCRUM-36) — Vis valgte kriterier, lik rangering og manglende sorteringsdata | To Do | Done | Valgte kriterier og kriterieverdier vises ved rangeringen. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-37](https://stiodi.atlassian.net/browse/SCRUM-37) — Generer forslag ved frafall i uke 5 med låste og endrbare tildelinger | To Do | In Review | Må-søk og datasettlåser virker; Bør-delen med lederlåser i UI er ikke bygget. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-38](https://stiodi.atlassian.net/browse/SCRUM-38) — Vis forslag separat fra gjeldende plan med resultatstatus, regelkontroll og udekket behov | To Do | Done | Forslag og gjeldende plan er visuelt og tekstlig separate. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [backend/src/vaktmatch/api/models.py](../backend/src/vaktmatch/api/models.py). |
| [SCRUM-39](https://stiodi.atlassian.net/browse/SCRUM-39) — KI-tjeneste med fast svarformat basert på kontrollresultater | To Do | To Do | Bare standardforklaring og ærlig reserve er implementert. Ingen ekte modell eller forhåndsdefinert modell-testmodus er koblet inn. Neste handling er leverandør/modell/kostnadsgrense i SCRUM-59, deretter adapter/testmodus for «Forklar forskjellen» i fast norsk format. Beregnede statuser/rangeringer/kostnader skal fortsatt være autoritative. Kode/bevis: [backend/src/vaktmatch/api/routes.py](../backend/src/vaktmatch/api/routes.py), [docs/demoflyt-kontrollrapport-2026-11-08.md](../docs/demoflyt-kontrollrapport-2026-11-08.md). |
| [SCRUM-40](https://stiodi.atlassian.net/browse/SCRUM-40) — Regelbaserte standardforklaringer uten KI-nøkkel eller ved modellfeil | To Do | In Review | Standard/reserve uten nøkkel virker; simulert modellfeil/-timeout gjennom modellgrensen gjenstår. Kode/bevis: [backend/src/vaktmatch/explain/demoflow.py](../backend/src/vaktmatch/explain/demoflow.py), [backend/tests/test_explain.py](../backend/tests/test_explain.py). |
| [SCRUM-41](https://stiodi.atlassian.net/browse/SCRUM-41) — Verifiser sporbarhet: KI endrer ikke status, rangering eller valg | To Do | To Do | Regel-/forklaringslag er atskilt og standardforklaringen er testet, men sammenligning med/uten modell, kontroll av modellfakta og deterministiske timeout-/feilreserver er ikke levert. Avhenger av testbar modellintegrasjon i SCRUM-39 etter SCRUM-59. Beholdes To Do til dette grunnlaget finnes; ingen påstand om full KI-sporbarhet. Kode/bevis: [backend/src/vaktmatch/api/routes.py](../backend/src/vaktmatch/api/routes.py), [backend/tests/test_explain.py](../backend/tests/test_explain.py). |
| [SCRUM-42](https://stiodi.atlassian.net/browse/SCRUM-42) — Responsiv layout for mobil og PC | To Do | In Review | PC/mobil/axe/tastatur er kontrollert i Chromium; annen nettlesermotor gjenstår. Kode/bevis: [frontend/src/index.css](../frontend/src/index.css), [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json). |
| [SCRUM-43](https://stiodi.atlassian.net/browse/SCRUM-43) — Ende-til-ende-test av demoscenarioene mot suksesskriteriene | To Do | In Review | Faktisk E2E virker lokalt; full Må-sporbarhet, integrert UJ-1 i PR-CI og modellfeilkontroll gjenstår. Kode/bevis: [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/verify-browser.py](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/verify-browser.py), [.github/workflows/ci.yml](../.github/workflows/ci.yml). |
| [SCRUM-44](https://stiodi.atlassian.net/browse/SCRUM-44) — Dokumenter BMAD-bruk, egne valg og kvalitetssikring av KI-generert kode | To Do | In Review | Prosesspor finnes; samlet per-sak-kart er laget her, men komplett kravspor og publisering gjenstår. Kode/bevis: [README.md](../README.md), [_bmad-output/implementation-artifacts/spec-scrum-19-demoflyt.md](../_bmad-output/implementation-artifacts/spec-scrum-19-demoflyt.md). |
| [SCRUM-47](https://stiodi.atlassian.net/browse/SCRUM-47) — Lag UX-spesifikasjon og skisser for hovedflyten | In Progress | Done | DESIGN.md/EXPERIENCE.md, fire skjermreferanser, mobil/PC og klikkbar prototype er ferdigstilt og lenket fra README. Kode/bevis: [_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/validation-report.md](../_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/validation-report.md), [_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/.working/delegated-decisions-2026-11-08.md](../_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/.working/delegated-decisions-2026-11-08.md). |
| [SCRUM-48](https://stiodi.atlassian.net/browse/SCRUM-48) — Verifiser sensor-klar lokal levering | To Do | To Do | Kjørbar app, README, avhengighetslåser, syntetiske data og nøkkelfri reserve finnes. Full leveringskontroll er ikke utført: ren klone/separat miljø og en ny brukers dokumenterte UJ-1 på under 20 minutter gjenstår. Modell-testmodus og kostnadsgrense avhenger av SCRUM-59/39. Tidligere grønn skjelett-CI eller lokal utviklerkjøring oppfyller ikke dette alene. Kode/bevis: [README.md](../README.md), [docs/demoflyt-kontrollrapport-2026-11-08.md](../docs/demoflyt-kontrollrapport-2026-11-08.md). |
| [SCRUM-49](https://stiodi.atlassian.net/browse/SCRUM-49) — Avklar formelle leverings- og dokumentasjonskrav for IBE160 | To Do | To Do | Formelle krav er dokumentert i repoet; muntlig kilde peker på omtrent 15. desember for samtidig levering av app og refleksjon, men er ikke skriftlig fristbekreftelse. Skriftlig sluttfrist, omtalen av delvurdering 3 og eventuell formell godkjenningsstatus må fortsatt avklares mot faglærer/Canvas. Ingen ny ekstern kontakt er utført i avstemmingen. Kode/bevis: [docs/ibe160-leveringskrav.md](../docs/ibe160-leveringskrav.md), [docs/ibe160-leveringskrav.md](../docs/ibe160-leveringskrav.md). |
| [SCRUM-52](https://stiodi.atlassian.net/browse/SCRUM-52) — Simuler tilbud og svar for lederens valgte alternativ | To Do | Done | Valg, sendt/venter, akseptert/avslått og ikke simulert vises atskilt. Kode/bevis: [frontend/src/session.ts](../frontend/src/session.ts), [frontend/src/App.test.tsx](../frontend/src/App.test.tsx). |
| [SCRUM-53](https://stiodi.atlassian.net/browse/SCRUM-53) — Behold valg og simulerte svar i aktiv demoøkt | To Do | Done | Valg og alle berørtes svar beholdes i aktiv fane med grunnlag/forslag, og historiske registreringer beholdes ved datasettbytte. Kode/bevis: [frontend/src/session.ts](../frontend/src/session.ts), [frontend/src/session.test.ts](../frontend/src/session.test.ts). |
| [SCRUM-54](https://stiodi.atlassian.net/browse/SCRUM-54) — Valgfri varig beslutningslogg (avslått som standard, frivillig begrunnelse) | To Do | To Do | Ingen varig beslutningslogg er implementert. Valg/svar lever bare i fanens minne gjennom SCRUM-53. Bør-omfanget fra E35 beholdes; funksjonen skal ikke regnes som levert fordi øktminnet virker. Ingen aktivering eller valg av lagringsteknikk er gjort i denne avstemmingen. Kode/bevis: [docs/arkitektur.md](../docs/arkitektur.md), [docs/demoflyt-kontrollrapport-2026-11-08.md](../docs/demoflyt-kontrollrapport-2026-11-08.md). |
| [SCRUM-55](https://stiodi.atlassian.net/browse/SCRUM-55) — Vis historikk for uke 1–4 som synlig beslutningsgrunnlag | To Do | In Review | Historikk/kilde/periode/mangler virker; eksplisitt forbehold om ny tildelings gjennomførbarhet mangler. Kode/bevis: [frontend/src/App.tsx](../frontend/src/App.tsx), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-56](https://stiodi.atlassian.net/browse/SCRUM-56) — Ta med nabovakter fra uke 4 og uke 6 i hvile- og arbeidstidskontrollen | To Do | Done | Hvilegrunnlaget bruker nabovakter på begge sider av arbeidsuken; arbeidstid bruker faktisk periodeoverlapp. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |
| [SCRUM-57](https://stiodi.atlassian.net/browse/SCRUM-57) — Endringsoversikt og ny vurdering ved datasettbytte | To Do | In Review | Forskjeller og helt uendret grunnlag vises; uendrede vakter ved delvis endring trenger oversikt. Kode/bevis: [backend/src/vaktmatch/api/presentation.py](../backend/src/vaktmatch/api/presentation.py), [frontend/src/App.tsx](../frontend/src/App.tsx). |
| [SCRUM-58](https://stiodi.atlassian.net/browse/SCRUM-58) — Mål responstid for søket på representative data | To Do | In Review | Hovedscenario målt ved 0/1; flere representative demodatasett gjenstår. Kode/bevis: [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark.py](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark.py), [_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark-results.json](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark-results.json). |
| [SCRUM-59](https://stiodi.atlassian.net/browse/SCRUM-59) — Velg språkmodell og leverandør for KI-forklaringen | To Do | To Do | Leverandør, modell og kostnadsgrense er fortsatt ikke valgt. Den pushede appen virker uten nøkkel med standardforklaring, men dette avslutter ikke modellvalget. Neste handling: begrunnet valg og dokumentert test-/mockmodus/kostnadsgrense, deretter implementering i SCRUM-39 og kontroll i SCRUM-41. Kode/bevis: [docs/arkitektur.md](../docs/arkitektur.md), [docs/demoflyt-kontrollrapport-2026-11-08.md](../docs/demoflyt-kontrollrapport-2026-11-08.md). |
| [SCRUM-60](https://stiodi.atlassian.net/browse/SCRUM-60) — Vis anslått kostnad per bemanningsalternativ med syntetiske satser og tillegg | To Do | Done | O1–O5 er kontrollert: alle berørte tildelinger, referanse/differanse, timer/satser/intervalltillegg, ny dataversjon og halv-opp-avrunding per tildeling. Kode/bevis: [backend/src/vaktmatch/rules/engine.py](../backend/src/vaktmatch/rules/engine.py), [backend/tests/test_demoflow.py](../backend/tests/test_demoflow.py). |

## Epics, sprint og uendret arbeid

E1/E2/E3/E4/E6/E7/E8 (SCRUM-5/6/7/8/10/11/12) har dokumentert utført arbeid
og åpne undersaker og skal stå `In Progress`. E5/SCRUM-9 kan avsluttes når
SCRUM-35/36 er verifisert `Done`; ingen andre undersaker er registrert på epicen.
Tidligere ferdige SCRUM-13–18/46/51 beholdes. Valgfrie bruker-/hypotesetester
SCRUM-45/50 og eksempeloppgavene SCRUM-1–4 endres ikke.

Sprint 0 er fortsatt aktiv med planlagt sluttdato 04.11.2026; Sprint 1 er fremtidig.
Ingen sprint avsluttes eller omlegges, og ingen eksempeloppgaver slettes.
Slik administrasjon krever samordning etter AGENTS.md og tas opp i SCRUM-5.
Modellvalg/integrasjon/sporbarhet følges i SCRUM-59/39/41, leveringskontroll i
SCRUM-48 og skriftlige kursavklaringer i SCRUM-49. Varig logg forblir Bør i SCRUM-54.

## Faktisk resultat

20 oppgaver er satt `Done`, 12 oppgaver er satt `In Review`, og seks avventende
oppgaver beholder `To Do` med presisert neste handling. Sju epics er satt
`In Progress`; sorteringsepicen SCRUM-9 er satt `Done` etter SCRUM-35/36.
Dette er 40 statusendringer. Totalt på prosjektet etter avstemmingen:
29 `Done`, 12 `In Review`, sju `In Progress` og 12 `To Do` (60 saker).

38 saksavstemminger og åtte epicavstemminger har egne kommentarer med commit
og kontrollgrunnlag. SCRUM-20 har i tillegg en presisering om at testfiksturer
kan inngå i bevisene; ingen ny regel om én JSON-fil per testvariant er innført.
Kun nåstatus/publiseringsmetadata er endret i beskrivelsene til SCRUM-47/60;
alle opprinnelige akseptansekriterier er bevart.

Alle 60 saker er lest tilbake uten avvik i forventet status, beskrivelse,
tittel, ansvar, prioritet eller forelder. Kommentarene ble bekreftet av
skriveverktøyet med ID og gjengitt innhold før tilhørende statusendring.
Sprint/board/arbeidsflyt/tillatelser er ikke endret. Ingen Jira-saker er
slettet, omfordelt eller tatt inn i en sprint. Kontrollgrunnlaget i kommentarene
peker til allerede publiserte commits; dette nye repodokumentet er lokalt
frem til en senere konkret godkjent push.

### Spor til Jira-kontrollen

| Sak | Bekreftet status | Kontrollkommentar |
|---|---|---|
| SCRUM-5 | In Progress | [10110](https://stiodi.atlassian.net/browse/SCRUM-5?focusedCommentId=10110) |
| SCRUM-6 | In Progress | [10111](https://stiodi.atlassian.net/browse/SCRUM-6?focusedCommentId=10111) |
| SCRUM-7 | In Progress | [10112](https://stiodi.atlassian.net/browse/SCRUM-7?focusedCommentId=10112) |
| SCRUM-8 | In Progress | [10113](https://stiodi.atlassian.net/browse/SCRUM-8?focusedCommentId=10113) |
| SCRUM-9 | Done | [10114](https://stiodi.atlassian.net/browse/SCRUM-9?focusedCommentId=10114) |
| SCRUM-10 | In Progress | [10115](https://stiodi.atlassian.net/browse/SCRUM-10?focusedCommentId=10115) |
| SCRUM-11 | In Progress | [10116](https://stiodi.atlassian.net/browse/SCRUM-11?focusedCommentId=10116) |
| SCRUM-12 | In Progress | [10117](https://stiodi.atlassian.net/browse/SCRUM-12?focusedCommentId=10117) |
| SCRUM-19 | Done | [10072](https://stiodi.atlassian.net/browse/SCRUM-19?focusedCommentId=10072) |
| SCRUM-20 | In Review | [10073](https://stiodi.atlassian.net/browse/SCRUM-20?focusedCommentId=10073) |
| SCRUM-21 | Done | [10074](https://stiodi.atlassian.net/browse/SCRUM-21?focusedCommentId=10074) |
| SCRUM-22 | Done | [10075](https://stiodi.atlassian.net/browse/SCRUM-22?focusedCommentId=10075) |
| SCRUM-23 | Done | [10076](https://stiodi.atlassian.net/browse/SCRUM-23?focusedCommentId=10076) |
| SCRUM-24 | In Review | [10077](https://stiodi.atlassian.net/browse/SCRUM-24?focusedCommentId=10077) |
| SCRUM-25 | Done | [10078](https://stiodi.atlassian.net/browse/SCRUM-25?focusedCommentId=10078) |
| SCRUM-26 | Done | [10079](https://stiodi.atlassian.net/browse/SCRUM-26?focusedCommentId=10079) |
| SCRUM-27 | Done | [10080](https://stiodi.atlassian.net/browse/SCRUM-27?focusedCommentId=10080) |
| SCRUM-28 | In Review | [10081](https://stiodi.atlassian.net/browse/SCRUM-28?focusedCommentId=10081) |
| SCRUM-29 | In Review | [10082](https://stiodi.atlassian.net/browse/SCRUM-29?focusedCommentId=10082) |
| SCRUM-30 | Done | [10083](https://stiodi.atlassian.net/browse/SCRUM-30?focusedCommentId=10083) |
| SCRUM-31 | Done | [10084](https://stiodi.atlassian.net/browse/SCRUM-31?focusedCommentId=10084) |
| SCRUM-32 | Done | [10085](https://stiodi.atlassian.net/browse/SCRUM-32?focusedCommentId=10085) |
| SCRUM-33 | Done | [10086](https://stiodi.atlassian.net/browse/SCRUM-33?focusedCommentId=10086) |
| SCRUM-34 | Done | [10087](https://stiodi.atlassian.net/browse/SCRUM-34?focusedCommentId=10087) |
| SCRUM-35 | Done | [10088](https://stiodi.atlassian.net/browse/SCRUM-35?focusedCommentId=10088) |
| SCRUM-36 | Done | [10089](https://stiodi.atlassian.net/browse/SCRUM-36?focusedCommentId=10089) |
| SCRUM-37 | In Review | [10090](https://stiodi.atlassian.net/browse/SCRUM-37?focusedCommentId=10090) |
| SCRUM-38 | Done | [10091](https://stiodi.atlassian.net/browse/SCRUM-38?focusedCommentId=10091) |
| SCRUM-39 | To Do | [10092](https://stiodi.atlassian.net/browse/SCRUM-39?focusedCommentId=10092) |
| SCRUM-40 | In Review | [10093](https://stiodi.atlassian.net/browse/SCRUM-40?focusedCommentId=10093) |
| SCRUM-41 | To Do | [10094](https://stiodi.atlassian.net/browse/SCRUM-41?focusedCommentId=10094) |
| SCRUM-42 | In Review | [10095](https://stiodi.atlassian.net/browse/SCRUM-42?focusedCommentId=10095) |
| SCRUM-43 | In Review | [10096](https://stiodi.atlassian.net/browse/SCRUM-43?focusedCommentId=10096) |
| SCRUM-44 | In Review | [10097](https://stiodi.atlassian.net/browse/SCRUM-44?focusedCommentId=10097) |
| SCRUM-47 | Done | [10098](https://stiodi.atlassian.net/browse/SCRUM-47?focusedCommentId=10098) |
| SCRUM-48 | To Do | [10099](https://stiodi.atlassian.net/browse/SCRUM-48?focusedCommentId=10099) |
| SCRUM-49 | To Do | [10100](https://stiodi.atlassian.net/browse/SCRUM-49?focusedCommentId=10100) |
| SCRUM-52 | Done | [10101](https://stiodi.atlassian.net/browse/SCRUM-52?focusedCommentId=10101) |
| SCRUM-53 | Done | [10102](https://stiodi.atlassian.net/browse/SCRUM-53?focusedCommentId=10102) |
| SCRUM-54 | To Do | [10103](https://stiodi.atlassian.net/browse/SCRUM-54?focusedCommentId=10103) |
| SCRUM-55 | In Review | [10104](https://stiodi.atlassian.net/browse/SCRUM-55?focusedCommentId=10104) |
| SCRUM-56 | Done | [10105](https://stiodi.atlassian.net/browse/SCRUM-56?focusedCommentId=10105) |
| SCRUM-57 | In Review | [10106](https://stiodi.atlassian.net/browse/SCRUM-57?focusedCommentId=10106) |
| SCRUM-58 | In Review | [10107](https://stiodi.atlassian.net/browse/SCRUM-58?focusedCommentId=10107) |
| SCRUM-59 | To Do | [10108](https://stiodi.atlassian.net/browse/SCRUM-59?focusedCommentId=10108) |
| SCRUM-60 | Done | [10109](https://stiodi.atlassian.net/browse/SCRUM-60?focusedCommentId=10109) |

SCRUM-20s presisering: [10118](https://stiodi.atlassian.net/browse/SCRUM-20?focusedCommentId=10118).
