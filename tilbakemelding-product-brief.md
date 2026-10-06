# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G10 – G10-andreassen-lundberg |
| **Product brief** | `productbrief.md` (commit `587bc45`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

Repoet har flere briefer, og hver av dem har fått egen tilbakemelding: `_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/tilbakemelding-product-brief.md` og `_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/tilbakemelding-product-brief.md`.

Vurderingen gjelder `productbrief.md` i roten, som README og den eldre VaktMatch-briefen peker på som gjeldende. Jeg har også lest det alternative forslaget i `_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/` (brief, forslag og svar til felles retning), fordi det påvirker omfanget.

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

**Det som er bra:**

1. Arbeidsdelingen mellom regelkontroll i kode og KI som bare tolker og forklarer, er svært godt gjennomtenkt. Det gjør appen etterprøvbar og gir dere noe konkret å teste: ingen forslag som vises som godkjent, skal bryte regelsettet.
2. Briefen er ærlig om usikkerhet: problemet er merket som antakelse, appen lover ikke «lovlighet», bare kontroll mot et navngitt scenarioregelsett, og konkurrentsjekken er presentert med sine begrensninger.
3. Suksesskriteriene er uvanlig gode: udekket behov skal vises når det ikke finnes løsning, manglende data gir «uavklart» status, og KI-forklaringen skal kunne spores til data og regelkontroll. Dette er rett fram å gjøre om til testtilfeller.

**De viktigste endringene:**

1. Dere har nå to retninger (avvikshåndtering ved ett sykefravær og turnusgenerering med constraint-solver) og et forslag om å slå dem sammen, men ingen felles beslutning. Bestem retning og samle den i én oppdatert brief før dere lager PRD.
2. «Gjenstår å avklare» inneholder det som bærer hele appen: de konkrete 3–5 reglene, rangeringskriteriene og teknologistakken. Skriv reglene ned med tall (f.eks. minst 11 timers hvile) og et regneeksempel.
3. Avklar KI-delen i v1: hvilken språkmodell, hva som skjer uten nøkkel, og om friteksttolkning faktisk er med (svaret til felles retning foreslår å utsette den).

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 4) KI-støttet MRP II, særlig modul 4.6 Operations Planning (scheduling) (vanskelig). VaktMatch er avgrenset til én arbeidsplass og få regler, men kjernen er planlegging med regler som må stemme, og det er der vanskelighetsgraden ligger. Holdes v1 strengt til ett ukesgrunnlag og ett fravær, ligger prosjektet i nedre del av «vanskelig».

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Høy | Kompetanse, hviletid før og etter vakt, tidskollisjoner, arbeidstid og konsekvenser for nabovakter. Generering av ukesgrunnlag i tillegg til avvikshåndtering dobler logikken. Med CP-SAT og objektivfunksjon (turnusforslaget) blir det enda mer krevende. |
| Datamodell – antall entiteter og relasjoner mellom dem | Middels | Ansatt, vikar, skift, kompetanse, regelsett, turnusplan og avvikslogg. Overkommelig, men relasjonene mellom skift og ansatte over tid må modelleres nøye. |
| Brukere, roller og innlogging | Lav | Én rolle (skiftleder). Ansatt- og vikarflater er riktig holdt utenfor v1. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Middels | KI tolker fritekst og forklarer kontrollerte resultater. Avgrenset og godt plassert, men forklaringene må ikke kunne si noe annet enn regelmotoren. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Lav–middels | Språkmodell-API, og eventuelt en solver-bibliotek (OR-Tools) som kjører lokalt. HR-integrasjoner er utenfor. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Én leder, syntetiske data. Simulering av tilbud og aksept er nevnt som uavklart; hold det utenfor. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Lav | Ikke i v1. Eksport står bare i turnusforslagets middels nivå. |
| Sikkerhet og personvern | Lav | Syntetiske data og ingen reelle persondata i v1. Godt valg. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn etterpå. Demonstrasjonsforløpet i «forslag til felles retning» (legg inn ansatte → generer → godkjenn → registrer fravær → sammenlign → godkjenn endring → vis oppdatert plan) er et godt utgangspunkt for en slik minimal versjon, så lenge hvert steg holdes enkelt.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Risiko | Briefen ble levert 20. september, og per i dag finnes ingen PRD eller arkitektur, og retningen er ikke avklart. To personer med både generering og avvikshåndtering er mye. Det går hvis dere låser omfanget nå. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Problem, bruker og prinsipper er tydelige, men reglene, rangeringen og demodomenet er uavklart. Uten dem vil PRD-en enten gjette eller utsette det viktigste. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | En webapp med Python-backend og eventuelt OR-Tools er godt dokumentert. Regelbasert kode i ren Python er også et alternativ som er lettere å forstå. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Risiko | Med 3–5 eksplisitte regler og 8–10 ansatte kan dere kontrollere svarene for hånd. Med en solver og objektivfunksjon blir det vanskeligere å vite om «beste» plan faktisk er best. Lag håndregnede scenarioer med fasit. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | OK | Svært godt utgangspunkt. Reglene er deterministiske, og suksesskriteriene beskriver forventet oppførsel (godkjent, utelukket, uavklart, udekket). Forslaget om ett løsbart og ett uløsbart fraværsscenario er verdt å følge. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Regelmotoren kan kjøre lokalt, men KI-forklaringene krever nøkkel. Sørg for at kjerneflyten virker uten KI (f.eks. med regelbaserte standardforklaringer), og at syntetiske data lastes automatisk. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Språkmodell er ikke valgt, og det finnes ingen plan for kostnad eller testmodus. Supabase og andre tjenester er nevnt som bakgrunn; unngå eksterne tjenester som sensor må sette opp. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Velg én kjerneflyt for v1. Mitt råd er å beholde avvikshåndteringen som hovedfunksjon (gjeldende brief) med et enkelt, regelbasert ukesgrunnlag, og legge full periodeplanlegging med solver, rettferdighet og helgefordeling i et senere trinn. Velger dere sammenslåingen, hold den til én uke, to kompetansetyper og ett fravær.
2. Lås regelsettet i briefen: list de 3–5 reglene med konkrete verdier, og skriv rangeringen som en enkel, synlig prioritering (f.eks. dekning først, deretter færrest endringer).
3. Gjør KI-forklaringen til et lag på toppen av en ferdig regelbasert flyt, og flytt friteksttolkning av behov til etter v1. Da kan sensor kjøre og teste kjernen uten nøkkel.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Tydelig: en webapp som hjelper skiftlederen å sammenligne intern omfordeling, ekstravakt og ekstern vikar når en vakt plutselig mangler bemanning. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | OK | Konkret situasjon (fravær kort før vaktstart) og ærlig merket som en uvalidert hypotese. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | Juster | Godt beskrevet med sammenligningsside, utelukkede kandidater og bekreftelse før endring. Men «KI tolker behov i fritekst» må samkjøres med beslutningen om hva KI gjør i v1. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Ærlig: ingen påstand om markedsunikhet, verdien ligger i den avgrensede arbeidsflyten. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | OK | Én tydelig primærbruker (skiftleder under tidspress) med et konkret mål. Bestem demodomenet (lager/logistikk) endelig. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Juster | De fire første er gode og testbare. Det siste (tidsbruk og forståelse sammenlignet med manuell oversikt) er vanskelig å måle i emnet. Behold det gjerne som brukertest, men ikke som hovedkriterium. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Endre | Rammen (8–10 ansatte, 3–5 regler, ett fravær) er god, men reglene, rangeringen, teknologistakken og forholdet til turnusforslaget er uavklart. Dette må på plass før PRD. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Nøktern og tydelig adskilt fra v1. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Dere har gode spor av prosessen: memlog, forslag og svar mellom gruppemedlemmene, og en tydelig historikk over valg. Det er bra for kriterium 1. Avslutt diskusjonen med en dokumentert beslutning og gå videre til PRD. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Juster | Kjerneflyten er tydelig og har nok innhold. Risikoen er at både generering og avvikshåndtering blir halvferdige. Prioriter. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | OK | Regler og forventede statuser gir et svært godt grunnlag for automatiske tester. Lag faste demoscenarioer med fasit. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Sammenligningssiden og kravet om mobil og PC gir et godt designfokus. Skisser ukesvisningen og sammenligningssiden, og hvordan «utelukket» og «uavklart» vises. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | Juster | Teknologistakken er åpen. Begrunn valget i arkitekturen; vurder om en solver trengs i v1 eller om enkel regelbasert kode holder. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Syntetiske data er et godt valg. Planlegg at appen kjører lokalt med ferdige demodata og uten KI-nøkkel. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Briefen ligger i roten mens tilhørende vedlegg og forslag ligger i `_bmad-output/`, og den gamle briefen er en henvisning. Samle gjeldende planleggingsdokumenter på ett sted, og legg demodata og `.env.example` inn i planen. |

## 3. Neste steg for gruppen

1. Ta en felles beslutning om retning (avvikshåndtering, turnusgenerering eller den sammenslåtte flyten), og oppdater `productbrief.md` slik at den er den eneste gjeldende briefen.
2. Skriv inn regelsettet med konkrete verdier, rangeringskriteriene og to–tre demoscenarioer med forventet resultat, inkludert ett fravær uten gyldig erstatter.
3. Bestem hva KI gjør i v1 og hvordan appen virker uten nøkkel, og gå deretter videre til PRD og arkitektur.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
