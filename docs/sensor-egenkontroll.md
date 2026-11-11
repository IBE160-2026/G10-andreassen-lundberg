# Egenkontroll mot sensorveiledningen for del 1

*Skrevet: Claude Code (Opus 5.5) · 09.11.2026, på Stians oppdrag. Dette er en
KI-vurdering av repoet mot sensorveiledningen. Det er ikke en karakterprognose
eller en gruppebeslutning.*

Grunnlag: *Sensorveiledning IBE160 – Del 1, applikasjon og prosess (70 %)*,
høst 2026. En lokal kopi ble lest 09.11.2026 og samsvarer med veiledningen
som er gjengitt i [leveringskravene](ibe160-leveringskrav.md#vurdering-og-dokumentasjon-av-ki-bruk).
PDF-en er ikke lagt i repoet. Kontrollert grunnlag er grenen `scrum-19-demoflyt`
etter etterkontrollen samme dag. `main` mangler fortsatt denne grenen.

## Kriterier og vekt

| Nr. | Kriterium | Vekt | Hva sensor gjør konkret |
|---|---|---|---|
| 1 | Prosess og KI-styring | 30 % | Følger spor fra BMAD-plan til kode: commits, prompter, iterasjoner, beslutninger, PR-er og issues |
| 2 | Funksjonalitet og omfang | 20 % | Kjører kjerneflytene fra product brief og README, også feil input og gjentatte handlinger |
| 3 | Kvalitetssikring og testing | 15 % | Kjører testene etter README og ser etter spor av gjennomgang og rettede KI-feil |
| 4 | Design og brukeropplevelse | 10 % | Ser på konsistens, tilbakemeldinger, tilgjengelighet, skjermstørrelser og designspor |
| 5 | Kodekvalitet og arkitektur | 10 % | Stikkprøver koden mot beskrevet arkitektur; ser etter duplisering og død kode |
| 6 | README og kjørbarhet | 10 % | Installerer på en ren maskin, kun etter README, i inntil 15–20 minutter |
| 7 | Ryddighet i repoet | 5 % | Ser etter `.gitignore`, hemmeligheter, byggartefakter og løse filer |

Delkarakteren er et vektet snitt (A = 5 … F = 0). Grensene er A ≥ 4,5,
B ≥ 3,5, C ≥ 2,5, D ≥ 1,5 og E ≥ 0,5. Sensor kloner repoet i `IBE160-2026`
og bruker siste commit før fristen. Det som ikke er merget eller pushet da,
teller ikke.

## Status per kriterium

### 1. Prosess og KI-styring (30 %)

**Sterkt:** BMAD-sporet er brukt og oppdatert over tid: product brief med
[endringslogg](productbrief-endringslogg.md), PRD, UX, arkitektur og spesifikasjoner
per sak i `_bmad-output/`. I tillegg finnes [`.memlog.md`](../.memlog.md),
sesjonslogger i `.logs/` og Jira-nøkler i commit-meldingene. Det finnes
konkrete eksempler på at KI-forslag er kritisert og rettet. Gjennomgangen
09.11 fant elleve feil, og alle er rettet med tester som er kontrollert ved
mutasjon (se [etterkontrollen](../_bmad-output/implementation-artifacts/review-status-2026-11-09.md#etterkontroll-09112026)).

**Risiko:**
- Commit `14b187d` (08.11) legger inn 15 757 linjer i 49 filer på én gang.
  Sensorveiledningen nevner store enkeltcommits som varseltegn. Historikken
  omskrives ikke. Spesifikasjonen og kontrollrapporten forklarer hva commiten
  inneholder, og senere arbeid bør komme i små commits.
- Commitene er ujevnt fordelt over tid: 25 commits 31.10, og ingen mellom
  01.11 og 05.11. Veiledningen sier at ujevn fordeling alene ikke gir trekk.
- 27 commits ligger på `scrum-19-demoflyt` uten PR. PR-er med CI og
  gjennomgang er nettopp det sensor ser etter under arbeidsflyt.
- Stian har få commits i eget navn (9 av 78) og ingen egen `.logs/`-mappe før
  09.11. Veiledningen sier at commit-statistikk alene ikke gir trekk. Del 2
  har en personlig refleksjon for hvert medlem.

### 2. Funksjonalitet og omfang (20 %)

**Sterkt:** Den regelbaserte kjerneflyten kan kjøres fra start til slutt:
fravær, direkte erstatning eller én flytting, R1–R5, P1/P2, kostnad, valg og
simulerte svar, og nye data. Den fungerer på elleve datasett, også med feil
input og gjentatte handlinger.

**Største gap:** Product brief og PRD lover KI-forklaringer. Appen gir i dag
bare regelbaserte standardforklaringer
([SCRUM-59](https://stiodi.atlassian.net/browse/SCRUM-59) →
[SCRUM-39](https://stiodi.atlassian.net/browse/SCRUM-39) →
[SCRUM-41](https://stiodi.atlassian.net/browse/SCRUM-41)). Kriteriet ser også
etter om utelatt omfang er begrunnet. Hvis KI-sporet ikke rekker fristen, må
README og PRD si det tydelig og forklare hvorfor.

### 3. Kvalitetssikring og testing (15 %)

**Sterkt:** 70 backendtester og 24 frontendtester tester fasit og
grensetilfeller, ikke trivialiteter. Nettleserkontroll mot den faktiske appen
er gjort i tre motorer. Mutasjonskontroll viser at testene fanger kjente feil,
og CI kjører på hver PR.

**Gap:** Nettleserkontrollen ligger i `_bmad-output/` og kjøres ikke i CI.
Grenen har heller ikke kjørt PR-CI ennå.

### 4. Design og brukeropplevelse (10 %)

**Sterkt:** UX-spesifikasjon og klikkbar prototype (SCRUM-47). Appen har
konsistent visuelt uttrykk, norske feilmeldinger med gjenforsøk, tastatur og
fokusstyring, axe-pass og fungerer på 360 px.

**Gap:** Ingen manuell skjermlesertest og ingen brukertest
([SCRUM-45](https://stiodi.atlassian.net/browse/SCRUM-45) er valgfri).

### 5. Kodekvalitet og arkitektur (10 %)

**Sterkt:** Ansvarsgrensene er tydelige (`rules/` er ren beregning, `api/`
håndterer HTTP og `frontend/src/api.ts` samler HTTP-kallene) og samsvarer med
[arkitekturen](arkitektur.md). Linter og formatterer kjører i CI.

**Risiko:** `frontend/src/App.tsx` samler hele grensesnittet i én komponent
på rundt 420 linjer med svært lange JSX-linjer. Det er lesbart, men tett.
`engine.py` har noen lange funksjoner (`control_person`, `evaluate`). Det bør
vurderes å dele ut visninger (uke, fravær, alternativer, detalj, valg, data)
i egne komponenter når KI-sporet uansett endrer detaljvisningen.

### 6. README og kjørbarhet (10 %)

**Sterkt:** README har prosjektspesifikk beskrivelse, forutsetninger med
versjoner, kopierbare kommandoer, testkommandoer, `.env.example`, en
demoflyt-gjennomgang med datasettabell, mappeoversikt og lenker.

**Gap:**
- Node 24 og en ny brukers installasjon på under 20 minutter er ikke
  verifisert ([SCRUM-48](https://stiodi.atlassian.net/browse/SCRUM-48)).
- README mangler skjermbilde. Det er lagt til i samme omgang som denne
  kontrollen.
- Kommandoene i README er skrevet for PowerShell, med `Push-Location`. Sensor
  på macOS eller Linux må oversette dem selv. Bash-varianter bør vurderes.

### 7. Ryddighet i repoet (5 %)

**Sterkt:** `.gitignore` holder `node_modules`, `.venv`, `dist` og `.env` ute.
Ingen hemmeligheter ble funnet i et søk etter vanlige nøkkelmønstre 09.11.
Ingen byggartefakter er sporet.

**Mindre punkter:**
- `product-brief-template.md` i roten er en mal, ikke prosjektinnhold.
- `.gitignore` starter med overskriften «Next.js», som ikke brukes.
- `_bmad-output/…/ux-designs/…/.working/` har arbeids-PNG-er fra prototypen.

Disse punktene er ikke ryddet her. Sletting skal koordineres etter
[AGENTS.md](../AGENTS.md#robust-bruk-av-jira).

## Prioritert før fristen (forslag)

1. Merge `scrum-19-demoflyt` til `main` gjennom en PR med grønn CI og
   gjennomgang. Ellers ser sensor ikke appen (kriterium 1, 2, 3 og 6).
2. Fullfør eller begrunn KI-sporet: SCRUM-59, SCRUM-39 og SCRUM-41
   (kriterium 2).
3. Gjennomfør en dokumentert førstegangsinstallasjon med Node 24 etter README,
   og lukk SCRUM-48 (kriterium 6).
4. Fortsett med små, beskrivende commits og PR-er per sak (kriterium 1).
5. Avklar skriftlig fristen, «delvurdering 3» og godkjenningsstatusen
   (SCRUM-49).
6. Vurder småryddingen under kriterium 7 og oppdeling av `App.tsx`
   (kriterium 5 og 7).
