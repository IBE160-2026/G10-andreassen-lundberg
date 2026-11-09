# Tilstandsvurdering og kodegjennomgang – 09.11.2026

Codex på Odins oppdrag om å bruke flere agenter, teste og vurdere prosjektstatus.
Vurdert grunnlag: `fc5c111416de839fe00fb965952970b790ac2330` på
`scrum-19-demoflyt`, mot `origin/main`. Fire separate KI-gjennomganger med samme
modellkapasitet; dette er teknisk kontroll, ikke menneskelig akseptansetest.

## Vurdering

Den regelbaserte lokale demoflyten er kjørbar og har et godt kontrollgrunnlag.
Fravær, direkte erstatning/én flytting, R1–R5, P1/P2, kostnad, valg/svar og
nye data kan demonstreres. Testene er grønne, men seks konkrete feil i
grensesnitt/datakontrakt og tre verifikasjonshull ble påvist. Det er derfor
grunnlag for videre bygging, med en avgrenset feilrettingsrunde først.

Full MVP er fortsatt ikke levert: faktisk KI-forklaring og faktakontroll/
feilreserve samt de tidligere navngitte Må-restpunktene gjenstår.
Sensor-klar levering er heller ikke dokumentert. Varig logg og lederlåser
i grensesnittet er Bør og blokkerer ikke MVP.

## Hva som faktisk er kjørt

| Kontroll | Resultat 09.11.2026 |
|---|---|
| Backend, eksisterende arbeidskopi | 64 tester bestått; ruff lint/formatering bestått. Én Starlette/httpx-advarsel, ingen testfeil. |
| Frontend, eksisterende arbeidskopi | 20 tester bestått; lint, TypeScript og produksjonsbygg bestått. |
| Chromium 145.0.7632.6 | 50 nettleserkontroller bestått, elleve axe-pass. |
| Firefox 146.0.1 | Samme 50 kontroller bestått, elleve axe-pass. |
| WebKit 26.0 på Windows | Samme 50 kontroller bestått, elleve axe-pass. Dette er ikke attest på Safari på macOS/iOS. |
| Separat lokal klone | Nytt uv-miljø og `uv sync --locked`, `npm ci`, 64 backendtester, 20 frontendtester og produksjonsbygg bestått. |
| Egen backend fra klonen | Sju HTTP-kontroller bestått: helse, datasett, fravær, A02-fasit, 1 800 NOK, standardreserve og uendret kildefil. |
| Målrettede feilreproduksjoner | Fire UI-utfall bekreftet i ekte nettleser og to kontrakt-/forklaringsutfall i backend. |
| Mutasjon av testgrunnlag | Tomme lesbare differanser og ignorert sekundærkriterium lot hver gang alle 64 backendtester bestå. Testagenten bekreftet også feil prioritert kriterierekkefølge med grønn pakke. |

Nettleserkjøringene bruker eksisterende Playwright-rutine mot faktisk app,
med bare nettlesermotoren byttet i midlertidige kopier. I alt 150 kontroller og
33 axe-pass; ingen rapporterte JavaScript-feil eller eksterne modellkall.
PC- og mobilbildene er også visuelt kontrollert. Testene bruker syntetiske data.

[Manifest](status-verifikasjon-2026-11-09/manifest.json),
[Chromium](status-verifikasjon-2026-11-09/chromium-results.json),
[Firefox](status-verifikasjon-2026-11-09/firefox-results.json),
[WebKit](status-verifikasjon-2026-11-09/webkit-results.json),
[ren klone](status-verifikasjon-2026-11-09/clean-clone-results.json),
[PC](status-verifikasjon-2026-11-09/app-desktop.png) og
[mobil](status-verifikasjon-2026-11-09/app-mobile.png) er lagret separat fra
8. novembers historiske kontrollbevis.

Kontrollmiljøet hadde Python 3.12.14, uv 0.12.6, Node 22.18.0 og npm 10.9.3.
README/CI angir Node 24; denne versjonen er ikke kontrollert her. Klonen var
ren for prosjektavhengigheter, men brukte maskinens eksisterende verktøy og
pakkecacher. Dette er ikke en ny brukers installasjon/UJ-1 på under 20 minutter.

## Agentroller og samlet triage

| Lag | Rolle | Innspill |
|---|---|---|
| Blind Hunter | Finne feil og mangler uten endringsfortellingen | Ti konkrete innspill; funngulvet var ti på en diff på 935 632 byte. |
| Edge Case Hunter | Prøve feiltilstander og overganger, deretter kontrollere påstandene | To bekreftede UI-feil. |
| Verification Gap | Undersøke om testene kan slippe gjennom feil | Ett forhåndsverifisert gap med mutasjon og test-/referansesøk. |
| Acceptance Auditor | Kontrollere Build-AC, PRD og produkt-/leveringsstatus | Ett AC-brudd og en vurdering av demo/MVP/levering. |

Alle lag fullførte. Hvert av de 14 defekt-/gapinnspillene fikk egen dom før
duplikater ble gruppert: 11 tiltak, ni middels og to lave; ingen høye.
Tre ulike testhull er beholdt separat selv om de berører samme sorteringsfunksjon/
testpakke. Grønn mutert testpakke er bevis på et testhull, ikke bevis på at
dagens sortering er feil.

Ruting: **0 beslutningsbehov, 11 patch, 0 defer, 0 avvist**.
`Patch` betyr at rettingen kan gjennomføres innen eksisterende intensjon.
Denne bestillingen er en vurderingsrunde: funnene er lagret som åpne tiltak,
og appkoden er ikke rettet i økten. Den opprinnelige spesifikasjonens status
er derfor satt tilbake til `in-progress`; det endrer ingen produktbeslutning.

### Prioriterte tiltak

| Tiltak | Dom | Konkret problem og etterkontroll |
|---|---|---|
| K1 | medium | Feilet fraværsforhåndsvisning blir ikke hentet igjen av «Prøv igjen». Etter ett avbrutt preview var det fortsatt ett kall og null radiovalg; feltendring ga et nytt kall. Legg til reelt preview-gjenforsøk og regresjon. |
| K2 | medium | R4 kan vise avvik med bare 16/16 t på X, mens bruddet er ni timer mellom andre relevante vakter. Vis vakt/intervallet som begrunner avviket. |
| K3 | medium | To ulike A08/A06-forslag med W5-A08-4 respektive W5-A08-5 fikk identisk valghistorikk. Vis konkret vaktplan eller identitet i valg og historikk. |
| K4 | medium | Tilbake fra A05 lukker «Øvrige funn» og mister fokusmålet. Bevar åpningstilstand og gjenopprett synlig fokus. |
| K5 | medium | To gyldige datasett uten family_id gir same_family=true og kan overføre fravær uten bekreftet familietilhørighet. Tom familie må ikke bekrefte overføring. De medfølgende datasettene har familie. |
| K6 | medium | Testene tåler tomme label/before_label/after_label i endringsoversikten. Test norske, meningsbærende visningsfelt med komplett frontendfikstur. |
| K7 | medium | Testene tåler at [P2,P1] sorteres som [P1,P2]. Legg til kombinerte rekkefølger med motstridende P-verdier. |
| K8 | medium | Testene tåler at sekundærkriteriet helt utelates. Test lik primærverdi og forskjellig sekundærverdi for begge rekkefølger. |
| K9 | medium | Benchmark hardkoder 2026-11-08 og overskriver samme råfil ved gjentakelse. Bruk riktig kjøretid og bevar separate kjøringer. Originalbeviset ble ikke overskrevet her. |
| K10 | low | Etter datasettbytte vises tomt neste-valg, mens forhåndsvisning sammenligner datasettet med seg selv. Korriger neste-valg ved innlasting. |
| K11 | low | Nettleserskriptets rårapport mangler automatisk kilde-/kjøreidentifikasjon. Registrer proveniens slik at en gammel server ikke forveksles med testet kildegrunnlag. Denne økten har eget manifest. |

[UI-reproduksjoner](status-verifikasjon-2026-11-09/ui-reproductions.json) og
[backend-reproduksjoner](status-verifikasjon-2026-11-09/backend-reproductions.json)
viser de faktiske utfallene. [Full individuell triage](status-verifikasjon-2026-11-09/findings.json)
bevarer alle kilder, dommer, steder, bevis og gruppetilhørighet.

### Individuelle dommer før gruppering

| ID | Kilde | Dom | Gruppe | Kontrollgrunnlag |
|---|---|---|---|---|
| 1 | blind-hunter | low | K10 | Etter innlasting av en-flytting viser velgeren tom verdi, mens aktiv forhåndsvisning sender previous_id=next_id=en-flytting. Hovedagentens faktiske nettleserrepro bekrefter samme-datasett-sammenligning. |
| 2 | blind-hunter | medium | K4 | Ukontrollert details avmonteres ved detaljvisning. Etter A05 → Tilbake er øvrige funn lukket, opprinnelig undersøk-knapp usynlig og fokus ikke returnert; bekreftet av hovedagentens nettleserrepro. |
| 3 | blind-hunter | medium | K1 | Ett avbrutt preview etterfulgt av Simuler og Prøv igjen gir fortsatt ett preview-kall og null målskiftvalg. Feltendring gir straks nytt kall; dette er feil gjenoppretting, ikke varig backendfeil. |
| 4 | blind-hunter | medium | K3 | To forskjellige A08/A06-forslag gjelder W5-A08-4 respektive W5-A08-5. Hovedagenten registrerte begge og valgte A02; de to historikkpostene har identisk synlig tekst, selv om forslag-ID og berørt vakt er ulike. Gjeldende valg har samme identifikasjonsmangel. |
| 5 | blind-hunter | medium | K2 | Validert variant forlenger W5-A02-1 til 23:00 og gir ni timers hvile til tirsdag. A02s direkte X-forslag får korrekt R4-avvik, men regelverdi og rest_after viser bare X:16/16 t. Bekreftet prosesslokalt av hovedagenten; dette er en forklarings-/sporbarhetsfeil, ikke en feilaktig beståttstatus. |
| 6 | blind-hunter | medium | K5 | family_id er valgfri med tom standard. To fullstendig validerte datasett med ulike ID-er uten familie gir HTTP 200 og same_family=true. Frontend kan da overføre kompatible fraværsreferanser uten bekreftet scenariofamilie. Ikke utløst av de elleve medfølgende, navngitte familiene; feilen gjelder den aksepterte datakontrakten. |
| 7 | blind-hunter | medium | K9 | Skriptet hardkoder 2026-11-08 og skriver samme versjonerte resultatfil hver gang. Rerun-kommandoen i kontrollrapporten vil derfor merke senere målinger som 8. november og erstatte eldre råtall. Verifisert ved å følge skrivebanen; originalfilen ble ikke kjørt/overskrevet i denne økten. |
| 8 | blind-hunter | low | K11 | Rapportobjektet har nettleser, URL og axe-flagg, men ikke kjøretid, commit, datasettfingeravtrykk eller axe-versjon. En utvikler som kjører mot en gammel lokal backend kan ikke avgjøre server-/kildegrunnlaget fra rårapporten. Denne økten har derfor eget manifest; kildeskriptets fremtidige rapportering er fortsatt åpen. |
| 9 | blind-hunter | medium | K6 | Hovedagenten gjentok prosesslokal mutasjon av label/before_label/after_label til tomme strenger: alle 64 backendtester bestod. Frontendfiksturen mangler de samme visningsfeltene. Den faktiske differansevisningen virker nå; dette er et verifikasjonsgap. |
| 10 | blind-hunter | medium | K8 | Hovedagenten gjentok prosesslokal mutasjon fra criteria til criteria[:1] i sorteringsnøkkelen: alle 64 backendtester bestod. Tilfeller med likt primærkriterium og ulikt sekundærkriterium mangler. Dagens implementering bruker alle kriteriene korrekt. |
| 11 | edge-case-hunter | medium | K1 | Samme konkrete ett-kallsrepro som funn 3 er bekreftet av hovedagenten. Gjenforsøk validerer bare det manglende målskiftet; mangelen kan løses ved nytt preview-kall. |
| 12 | edge-case-hunter | low | K10 | Samme faktiske tomme velger/aktive selv-sammenligning som funn 1 er bekreftet av hovedagenten. Direkte tilstandskorreksjon ved innlasting er nok. |
| 13 | verification-gap | medium | K7 | Forhåndsverifisert av testagenten etter test-/referansesøk: prosesslokal sorted(criteria)-mutasjon ga feil A02 først for [P2,P1], mens alle 64 tester bestod. Originalen ga korrekt A03. Forelderen bruker dette innsendte beviset uten å gjenta mutasjonen, etter workflow-regelen. |
| 14 | acceptance-auditor | medium | K1 | Agentens isolerte Vitest-repro og hovedagentens nettleserrepro bekrefter samme feil som 3/11. Bryter Build-AC4 og PRD NFR-3; feilmeldingen og den synlige gjenforsøkshandlingen gir ikke fungerende vei videre. |

### Rejected

Ingen innspill ble avvist. Ingen lag feilet. Vurderingen er ikke en garanti
for fravær av flere feil, og den separate gjennomgangen er ikke en brukertest.

## Betydning for Jira og veien videre

Jira ble lest 09.11.2026: 60 saker, 29 Done, 12 In Review, sju In Progress og
12 To Do. Ingen Jira-status, beskrivelse eller kommentar er endret i denne økten.
Nye funn er knyttet til eksisterende oppfølgingssaker i råtriagen; dette er
forslag til oppfølging, ikke nye gruppebeslutninger.

- SCRUM-42s krav om annen nettlesermotor er nå teknisk kontrollert; gårsdagens restpunkt om bare Chromium er ikke lenger dekkende.
- SCRUM-48 har sterkere teknisk installasjonsbevis, men ny bruker, under-20-minuttersmåling og angitte programversjoner gjenstår.
- SCRUM-59/39/41 om modellvalg, faktisk KI, testmodus og faktakontroll/feilreserve er fortsatt åpne.
- Må-restpunktene 24/29/55/57 og komplett Må-sporbarhet/PR-CI med integrert UJ-1 i 20/28/43 gjenstår.
- Skriftlige formelle leveringsavklaringer i SCRUM-49 gjenstår. Varig logg og UI-låser forblir Bør.

Anbefalt rekkefølge er en kort feilrettingsrunde med regresjoner for K1–K5/K10,
deretter verifikasjonshullene K6–K8 og pålitelig bevisføring K9/K11. Ferdigstill
så KI-sporet og de navngitte Må-gapene, og kjør PR-CI på Node 24 samt en
dokumentert oppstart med ny bruker. Større søkeomfang og valgfrie tillegg
bør vurderes etter at denne kjernen er etterkontrollert.

Dette er Codex sin vurdering. Produktbrief, PRD, produktprioriteringer og
arbeidsdeling er uendret. Resultatene er lagret lokalt; ingen push eller merge.
