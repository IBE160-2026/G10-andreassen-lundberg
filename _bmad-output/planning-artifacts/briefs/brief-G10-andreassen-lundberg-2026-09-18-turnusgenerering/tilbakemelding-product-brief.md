# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G10 – G10-andreassen-lundberg |
| **Product brief** | `_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/brief.md` (commit `3e71b59`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

Vurderingen gjelder `brief.md` i denne mappen, sammen med `addendum.md`. For kontekst har jeg også lest `forslag-til-felles-retning.md` (18. september) og `svar-til-felles-retning.md` (27. september) i samme mappe.

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

Briefen er en alternativ og utvidet retning i forhold til `productbrief.md`, som allerede har fått tilbakemelding. Den er en dag nyere, men sier selv at den ikke erstatter `productbrief.md`. Den flytter hovedvekten fra avvikshåndtering ved ett sykefravær til generering av en hel periodeplan med en constraint-solver. Avvikshåndteringen er lagt på «avansert» nivå. Forslaget og svaret om felles retning viser at dere er godt i gang med å slå retningene sammen, men beslutningen er ikke tatt. **Dere må avklare én felles retning mellom denne briefen og `productbrief.md` før dere lager PRD.** Samle den i én gjeldende brief, og merk eller flytt de andre.

**Det som er bra:**

1. Valget om at KI ikke skal løse selve kombinatorikken, er godt begrunnet. Solveren håndhever de harde reglene, og språkmodellen tolker og forklarer. Vedlegget forklarer også hvorfor ren KI-generering og hjemmelaget backtracking ble lagt bort. Dette er presis KI-styring, og det gir en god historie for både del 1 og refleksjonsrapporten.
2. Omfanget er trappet opp i tre nivåer (førsteversjon, middels og avansert), og førsteversjonen er konkret: 8–10 ansatte, to kompetansetyper, to uker og minst 11 timers hviletid. Teknologivalget (Python med OR-Tools CP-SAT og JavaScript i frontend) er tatt og begrunnet.
3. Suksesskriteriene er testbare. En plan som vises som gyldig, skal ikke bryte de harde reglene, og systemet skal si tydelig fra når behovet ikke kan dekkes. Utfordringene i vedlegget (uløselig behov, at rettferdighet er subjektivt, skalering og personvern) viser god faglig refleksjon.

**De viktigste endringene:**

1. Avklar forholdet til `productbrief.md` (se over). Stillingen i «Gjenstår å avklare» kan ikke stå åpen når PRD-en skal skrives. Demonstrasjonsforløpet i forslaget til felles retning og de seks endringene i svaret er et godt grunnlag for en felles brief.
2. KI er ikke med i førsteversjonen slik scope er skrevet. Executive Summary og Solution beskriver en språkmodell som tolker og forklarer, men «Foreslått førsteversjon» nevner bare solver og kalendervisning. KI-forklaringer ligger først på «avansert» nivå. Bestem hva KI gjør i v1, og få briefen til å si det samme overalt.
3. To suksesskriterier gjelder funksjoner som ikke er med i førsteversjonen. Erstatter ved akutt fravær og forklaring av prioriteringer ved konflikt ligger på «avansert» og «middels» nivå. Flytt funksjonene inn i v1, eller merk kriteriene med hvilket nivå de gjelder.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 4) KI-støttet MRP II, modul 4.6 Operations Planning (scheduling) (vanskelig). Briefen beskriver planlegging over en periode med harde regler, kompetansekrav og etter hvert en objektivfunksjon for rettferdighet. Det er samme type problem som detaljplanlegging av produksjon. Selv minimumsnivået ligger høyere enn i `productbrief.md`, fordi hele toukersplanen skal genereres av en solver, og ikke bare et enkelt ukesgrunnlag. Med fravær og omplanlegging («minimal endring») i tillegg ligger prosjektet i øvre del av «vanskelig».

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Høy | Hviletid, maks vakter på rad, kompetanse og dekning per skift skal uttrykkes som constraints i CP-SAT. Rettferdighet og ønsker blir vektede straffeledd. Svaret til felles retning peker riktig på at omplanlegging etter fravær krever et eget ledd for minimal endring. Verdien for «maks vakter på rad» er ikke oppgitt. |
| Datamodell – antall entiteter og relasjoner mellom dem | Middels | `Ansatt`, `Skift`, `Regelsett` og `Turnusplan` med tildelinger, status og avvikslogg. Historikk for rettferdighet over tid gjør modellen tyngre. Hold den utenfor v1. |
| Brukere, roller og innlogging | Lav | Én planlegger i v1. Rollebasert tilgang er riktig lagt på «avansert» nivå. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Middels | Tolkning av fritekst («jeg vil helst ikke jobbe fredager») og forklaring av avveininger. Fritekst som skal bli constraints for solveren, er krevende å gjøre pålitelig. Svaret foreslår å utsette det. Det er klokt. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Lav–middels | OR-Tools er gratis og kjører lokalt. Språkmodellen er ikke valgt. Ingen integrasjoner mot HR- eller lønnssystemer. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Én bruker og syntetiske data. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Lav | Eksport til PDF, Excel og kalender er lagt på middels nivå. Hold det der. |
| Sikkerhet og personvern | Lav | Syntetiske data. Vedlegget peker godt på at turnusdata kan avsløre sykdom og permisjoner. Det er nyttig i refleksjonsrapporten. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn etterpå. Trappen med førsteversjon, middels og avansert nivå er et godt verktøy for dette. Men den felles retningen dere diskuterer, trekker fravær og forklaring inn i v1, og da må noe annet ut. Bestem hva.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Risiko | Toukersgenerering med solver er overkommelig for to personer. Generering, fravær, omplanlegging, KI-forklaring og rettferdighet samtidig er mye. Det er oktober, og dere har ingen PRD ennå. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Risiko | Førsteversjonen er konkret, men det er uklart hvilken brief PRD-en skal bygge på. KI-delen og suksesskriteriene samsvarer heller ikke med scope. Ryddes dette opp, blir stories for minimumsnivået overkommelige. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | Python, OR-Tools og et REST-API er godt dokumentert, og det finnes et referanseeksempel for skiftplanlegging. To språk (Python og JavaScript) gir to oppsett i README. Vurder om en enkel frontend uten byggesteg holder. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Risiko | Solveren garanterer bare de reglene som faktisk er modellert riktig. Skriver Claude Code en constraint feil, får dere en «gyldig» plan som bryter regelen. Med straffeledd er det også vanskelig å vite om planen faktisk er den beste. Lag en egen, enkel regelsjekk i ren Python som kontrollerer hver plan uavhengig av solveren. Lag også små scenarioer med fasit som dere har regnet ut for hånd. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | OK | Harde regler er deterministiske og kan testes. Forslaget i svaret om ett løsbart og ett uløsbart fraværsscenario bør bli faste testdata. Rettferdighet må defineres med tall (f.eks. maks antall helgevakter per person i perioden) for å kunne testes. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | OR-Tools installeres med `pip` og kjører lokalt, og det er bra. KI-forklaringene krever nøkkel. Sørg for at generering og visning virker uten nøkkel, og at demodata lastes automatisk. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Briefen sier ikke hvilken språkmodell som skal brukes, eller hva den koster. Planlegg en testmodus med faste forklaringer laget ut fra solverresultatet. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Velg felles v1 etter demonstrasjonsforløpet i forslaget til felles retning, men hold det smalt: generer plan for to uker, registrer ett fravær, foreslå en direkte erstatter eller vis udekket behov, og la lederen godkjenne. Legg omplanlegging av flere vakter, myke preferanser fra fritekst, «what-if» og eksport utenfor v1.
2. Ta med ett mykt hensyn med tydelig definisjon, slik svaret foreslår, for eksempel jevn fordeling av helgevakter. Da har solveren noe å optimalisere, og KI-en noe å forklare. Ikke ta med flere før dette virker og er testet.
3. Gjør KI-forklaringen til et lag på toppen av solverresultatet (hvilke regler og hensyn som avgjorde), og la appen virke fullt ut uten språkmodell. Flytt fritekst-tolkning av ønsker til etter v1.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Tydelig: generere en gyldig og rettferdig turnusplan for en periode, med solver og et forklarende KI-lag. Forholdet til `productbrief.md` er ærlig beskrevet. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | OK | Konkret om kravene som må balanseres (dekning, hviletid, kompetanse, rettferdighet), og ærlig merket som en uvalidert hypotese. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | Juster | Første avsnitt beskriver hva planleggeren gjør. Tredje avsnitt handler mest om teknologi, og det hører hjemme i arkitekturen. Beskriv heller hva planleggeren ser når behovet ikke kan dekkes, og hvordan planen godkjennes. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Ærlig: kommersielle turnussystemer finnes, og differensieringen er demonstrasjonen av arbeidsdelingen mellom solver og språkmodell. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | Én primærbruker (planlegger eller leder) med et klart mål. Brukeren og demodomenet (generisk arbeidsplass) er ikke de samme som i `productbrief.md` (skiftleder, lager/logistikk). Samkjør dette i den felles briefen. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Juster | De to første er gode og testbare. Kriteriet om erstatter ved akutt fravær gjelder en funksjon på «avansert» nivå, og kriteriet om forklaring av prioritering forutsetter myke hensyn på middels nivå. Knytt hvert kriterium til nivået det gjelder for. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Endre | Nivåene er tydelige, men forholdet til `productbrief.md` står som «gjenstår å avklare», og KI er ikke med i førsteversjonen. Dette må avklares før PRD. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Visjonen om at periodegenerering og avvikshåndtering utfyller hverandre, er nøktern og peker mot den felles retningen. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Forslaget og svaret om felles retning er gode spor av prosess og KI-styring. KI-assistenten skiller mellom det som står i briefen, egen tolkning og nye forslag. Men med to konkurrerende briefer kan sensor ikke se hvilken PRD-en bygger på. Avslutt med en dokumentert beslutning. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Juster | Førsteversjonen har nok innhold til å vise reell funksjonalitet. Risikoen er at middels og avansert nivå trekkes inn i v1 gjennom sammenslåingen. Prioriter. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Juster | Harde regler gir et godt grunnlag for tester. Legg til en uavhengig regelsjekk av solverens planer, faste scenarioer med fasit og en tallfestet definisjon av rettferdighet. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | «Enkel kalender/tabellvisning» er lite å bygge et design på. Skisser planvisningen for to uker, hvordan udekket behov og konflikter markeres, og hvor forklaringen vises. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | OK | Valget av CP-SAT er godt begrunnet, og vedlegget forklarer hvorfor Python-backenden må eie regelmotoren. Begrunn valget av frontend-rammeverk når det tas. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Lokal solver og syntetiske data er bra. Planlegg README for både Python- og JavaScript-delen, og at appen kjører uten KI-nøkkel. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Endre | Repoet har tre briefer: `productbrief.md` i roten, en erstattet henvisning i VaktMatch-mappa og denne. Lenken til `productbrief.md` i statuslinjen øverst har én `../` for mye og peker ut av repoet. Bestem én gjeldende brief, merk eller flytt de andre, og planlegg hvor demodata og `.env.example` skal ligge. |

## 3. Neste steg for gruppen

1. Ta en felles beslutning om retning, med utgangspunkt i forslaget og svaret om felles retning. Skriv den inn i én gjeldende brief, og merk denne briefen og VaktMatch-henvisningen som historikk, eller flytt dem.
2. Skriv v1 slik at den henger sammen: hvilke harde regler med konkrete verdier (også maks vakter på rad), hvilket ene myke hensyn, hva KI gjør i v1 og uten nøkkel, og hvilke suksesskriterier som gjelder v1.
3. Lag to–tre demoscenarioer med fasit, inkludert ett fravær uten gyldig erstatter. Planlegg en enkel regelsjekk som kontrollerer solverens planer. Gå deretter videre til PRD og arkitektur.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
