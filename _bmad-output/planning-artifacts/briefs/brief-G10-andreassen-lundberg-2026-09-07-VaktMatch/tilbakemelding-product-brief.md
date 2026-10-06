# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G10 – G10-andreassen-lundberg |
| **Product brief** | `_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/brief.md` (commit `587bc45`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

Vurderingen gjelder `brief.md` i denne mappen slik den står på main, sammen med `addendum.md` i samme mappe. Fila har status `superseded` og inneholder bare en henvisning til `productbrief.md` i roten. Den opprinnelige kandidatbriefen fra 7. september (commit `54bcdc7`) finnes bare i Git-historikken. Jeg har lest den for kontekst, men det er dagens fil som vurderes.

## Samlet vurdering

- **Bør revideres før dere går videre.** Rett punktene markert «Endre» før dere lager PRD og arkitektur.

Denne briefen ser ut til å være forlatt som arbeidsdokument. Den er eldre enn `productbrief.md` og er formelt erstattet av den 17. september. Den har derfor ikke noe eget innhold som PRD og arkitektur kan bygge på. Vurderingen «Bør revideres» betyr her ikke at dere skal skrive den på nytt. Den betyr at dere bør rydde: bestem én gjeldende brief, og merk eller flytt resten tydelig. Vedlegget i samme mappe er fortsatt i bruk, fordi både README og `productbrief.md` lenker til det.

**Det som er bra:**

1. Henvisningen er ærlig og sporbar. Den sier hvilken fil som gjelder, når og hvorfor den ble erstattet, og at den opprinnelige teksten finnes i Git-historikken. Det er god praksis for kriterium 1 (prosess og KI-styring).
2. Vedlegget er nyttig grunnlag for PRD og arkitektur. Det har de tre nivåene for turnusgeneratoren (minimum, middels og avansert), et forslag til datamodell (`Ansatt`, `Skift`, `Regelsett`, `Turnusplan` med avvikslogg) og et tydelig valg om at KI ikke skal generere planen. Det har også nøkterne forbehold om konkurrentsjekken mot Simployer, Quinyx og 4Human.

**De viktigste endringene:**

1. Repoet har nå tre briefer: denne henvisningen, `productbrief.md` i roten og turnusgenerator-forslaget fra 18. september. Bestem hvilken som gjelder, og merk eller flytt de andre, slik at sensor ikke må lete. Det er viktig for ryddighet i repoet (kriterium 7) og for sporbarheten fra brief til PRD (kriterium 1).
2. Flytt vedlegget slik at det ligger sammen med den gjeldende briefen, eller la `productbrief.md` lenke tydelig til det. I dag ligger det aktive vedlegget i en mappe som ellers er arkiv.
3. Ta med de åpne valgene fra vedlegget, «Åpne valg» og «Konkrete harde regler, rangeringskriterier …», i den gjeldende briefen. Avklar dem der, og ikke i denne mappa.

## Vanskelighetsgrad og gjennomførbarhet

Briefen beskriver ingenting selv. Vurderingen under bygger derfor på det vedlegget og den henviste `productbrief.md` sier om førsteversjonen. Den samsvarer med vurderingen av `productbrief.md`.

### Vurdert vanskelighetsgrad

- **Vanskelig**

**Sammenlignbart med:** 4) KI-støttet MRP II, særlig modul 4.6 Operations Planning (scheduling) (vanskelig). Vedlegget beskriver et generert ukesgrunnlag og avvikshåndtering ved ett sykefravær, med samme regelmotor. Kjernen er altså planlegging med regler som må stemme. Holdes førsteversjonen til én arbeidsplass, 8–10 ansatte og 3–5 regler, ligger prosjektet i nedre del av «vanskelig».

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Høy | Hviletid, kompetanse, tidskollisjoner og konsekvenser for nabovakter, både ved generering av ukesgrunnlaget og ved avvik. Vedlegget sier selv at reglene og rangeringskriteriene ikke er bestemt. |
| Datamodell – antall entiteter og relasjoner mellom dem | Middels | `Ansatt`, `Skift`, `Regelsett` og `Turnusplan` med planstatus og avvikslogg, i tillegg til vikarer fra et bemanningsforetak. Felt som arbeidsgiver, stillingsprosent og kontraktstype er nevnt, men ikke avklart. |
| Brukere, roller og innlogging | Lav | Én rolle, skiftlederen. Ansatte og vikarer finnes bare som syntetiske data. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Middels | KI skal tolke behov og forklare, ikke generere planen. Dette er et godt valg, men det står ikke hvilken modell som skal brukes, eller hva som skjer uten nøkkel. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Lav–middels | Språkmodell-API. Integrasjoner mot HR-systemer er riktig lagt utenfor. Supabase og GitHub Actions er nevnt som kursbakgrunn, ikke som et valg. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Én leder og syntetiske data. Simulering av tilbud og aksept står som åpent valg. Hold det utenfor v1. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Lav | Eksport er lagt til senere nivåer. |
| Sikkerhet og personvern | Lav | Ingen reelle persondata i prototypen. Forbeholdet om at reell bruk krever eget arbeid med personvern og tilgangsstyring, er bra. |

**Hva vanskelighetsgraden betyr for dere:**

- _Vanskelig:_ Et vanskelig prosjekt gir større mulighet for toppkarakter, men også større risiko. Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn etterpå. Trappen med minimum, middels og avansert i vedlegget er et godt verktøy for dette, men trinnene må stå i den gjeldende briefen, ikke i et vedlegg til en erstattet fil.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | Risiko | Omfanget i vedlegget er overkommelig, men det er nå oktober uten PRD, og med tre briefer i repoet. Tiden går med til å velge retning. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | Stor risiko | Denne fila kan ikke brukes som grunnlag for PRD, fordi den bare er en henvisning. Kjører dere `bmad-prd` mot denne mappa, får KI-en et halvt bilde. Pek PRD-arbeidet mot én gjeldende brief. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | En responsiv webapp med regelbasert kode er godt egnet. Teknologistakken er ikke valgt ennå. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | Risiko | Med 3–5 eksplisitte regler og 8–10 ansatte kan dere kontrollere svarene for hånd. Det forutsetter at reglene blir skrevet ned med konkrete verdier, og det har ikke skjedd ennå. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | Risiko | Vedlegget har gode presiseringer: umulig bemanning skal gi synlig udekket behov, og manglende nabovakter skal gi uavklart status. Men uten konkrete regler og demoscenarioer finnes det ennå ingen fasit å teste mot. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Syntetiske data er bra. KI-forklaringene krever nøkkel, og det finnes ingen plan for hvordan appen skal kjøre uten. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Vedlegget nevner kostnader bare for fremtidig drift. Lag en plan for testmodus eller faste standardforklaringer i v1. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart med justert omfang.** Se forslagene under. Konklusjonen gjelder idéen slik vedlegget og `productbrief.md` beskriver den, ikke denne fila som planleggingsgrunnlag.

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Hold v1 til det vedlegget kaller minimumsnivået: et enkelt ukesgrunnlag og ett fravær. Legg middels og avansert nivå (helg- og nattfordeling, preferanser, eksport, «hva om», tilgang for ansatte) tydelig utenfor i den gjeldende briefen.
2. Ta de åpne valgene fra vedlegget inn i den gjeldende briefen, og avklar dem der. Det gjelder konkrete regler med verdier, rangering og demodomene.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | Endre | Mangler i fila. Innholdet finnes i `productbrief.md`. Ikke skriv det inn her. Merk heller fila som arkiv. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | Endre | Mangler i fila. Den opprinnelige versjonen (`54bcdc7`) beskrev fravær kort før vakt og telefonrunder godt. Dette er videreført i `productbrief.md`. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | Endre | Mangler i fila. Vedlegget beskriver arbeidsdelingen mellom regelkode og KI, men ikke hva lederen ser og gjør. |
| What Makes This Different – er vurderingen ærlig og realistisk? | Juster | Mangler i fila, men vedlegget har en ærlig vurdering. Konkurrentsjekken dokumenterer ikke et markedshull, og flere funksjoner kunne ikke undersøkes. Det er en god justering fra den opprinnelige teksten, som påsto mer. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Endre | Mangler i fila. Lager/logistikk står bare som forslag i vedlegget. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Endre | Mangler i fila. Presiseringene i vedlegget (udekket behov, uavklart status, konsekvenser for vakten personen flyttes fra) er gode kandidater til testtilfeller i den gjeldende briefen. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | Endre | Mangler i fila. Vedlegget sier at minimumsnivået er med og resten er fremtidige muligheter, men at dette ikke er felles godkjent. Avklar det i den gjeldende briefen. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | Juster | Mangler i fila. Vedlegget holder et forklaringslag over eksisterende systemer og reelle integrasjoner utenfor MVP. Det er riktig. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | Juster | Henvisningen, memloggen og vedlegget viser godt hvordan idéen har utviklet seg. Det er et pluss. Men med tre briefer blir det uklart hvilken PRD-en skal spores tilbake til. Dokumenter beslutningen og pek PRD-en mot én brief. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | Endre | Fila beskriver ingen funksjonalitet. Omfanget må stå i den gjeldende briefen. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Endre | Fila har ingen suksesskriterier. Flytt presiseringene fra vedlegget inn i den gjeldende briefen som testbare kriterier. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Endre | Fila har ingen brukere eller flyt. Responsiv webapp for mobil og PC står i memloggen og i `productbrief.md`. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | Juster | Vedlegget sier riktig at verktøylisten (Node, Python, Docker, Supabase osv.) ikke er en vedtatt teknologistakk. Velg og begrunn stakken i arkitekturen. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Syntetiske data er et godt valg. Planlegg at appen kjører lokalt uten KI-nøkkel. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Endre | Det aktive vedlegget ligger i en mappe med en erstattet brief, og et alternativt forslag ligger i nabomappa. Samle gjeldende planleggingsdokumenter på ett sted. Merk denne mappa som arkiv, eller fjern `brief.md` og flytt vedlegget. |

## 3. Neste steg for gruppen

1. Bestem én gjeldende brief, enten `productbrief.md` eller en ny felles brief som tar inn turnusforslaget. Skriv beslutningen kort i memloggen eller i README.
2. Rydd i `_bmad-output/planning-artifacts/briefs/`: flytt `addendum.md` dit den gjeldende briefen ligger, eller oppdater lenkene, og merk eller fjern denne `brief.md` slik at det bare finnes én brief som ser gjeldende ut.
3. Ta de åpne valgene fra vedlegget inn i den gjeldende briefen. Det gjelder regler med konkrete verdier, rangering, demodomene og hva KI gjør uten nøkkel. Gå deretter videre til PRD.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
