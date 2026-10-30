---
title: VaktMatch
status: draft
document_role: current_product_brief
created: 2026-09-17
updated: 2026-10-30
---

# Product Brief: VaktMatch

**Gruppe:** Odin A Andreassen og Stian Lundberg · IBE160, høsten 2026  
**Metode:** BMAD (`bmad-product-brief`) · **Innlevering:** søndag 20. september 2026

**Status:** VaktMatch er valgt som gruppens prosjekt, og dette er eneste gjeldende produktbrief. Odin opplyste 21.10.26 at han og Stian samme dag avtalte at begge kan ta prosjektbeslutninger alene for å få arbeidet i gang. Scenarioreglene, sorteringen, søkeomfanget og tilbuds-/akseptsimuleringen nedenfor er besluttet av Odin innenfor denne felles delegeringen; dette betyr ikke at Stian personlig valgte detaljene. React og Python/FastAPI er utgangspunktet for lokal oppstart, og hovedfordelingen av arbeid er akseptert som justerbar: Stians forslag i SCRUM-13, med Odins tilslutning 26.10.26. Språkmodell og tekniske detaljer avklares videre; se [teknologi og arbeidsdeling](docs/teknologivalg.md).

[Endringsloggen](docs/productbrief-endringslogg.md) forklarer endringene og opphavet. [Dokumentoversikten](README.md#dokumentoversikt) viser vedlegg og historikk; [faglærerens tilbakemelding](tilbakemelding-product-brief.md) er grunnlag for videre avklaring.

## Executive Summary

Målet er å gjøre morgenens bemanningsavklaringer raske og enkle når flere ansatte melder fravær. Førsteversjonen håndterer fraværene ett etter ett; samlet løsning for flere samtidige fravær vurderes senere. Lederen skal kunne vurdere fordeling av arbeid, resultater fra regelkontrollen og anslått kostnad per alternativ. Kostnadsanslaget bygger på syntetiske satser og tillegg. Dette er Odins presisering av ønsket merverdi 30.10.26, ikke dokumentert tidsbesparelse, rettferdighet eller økonomisk gevinst.

VaktMatch er en planlagt responsiv webapp som gir en skiftleder informasjon og kontekst når en vakt plutselig mangler bemanning. Lederen får undersøke bemanningsalternativer og se relevante konflikter, arbeidstidsgrenser, hviletid og interne føringer. «Helhetsoversikt» betyr her å gjøre den tilgjengelige, relevante informasjonen forståelig, med synlige begrensninger i grunnlaget. Lederen beholder beslutningsmyndigheten og velger hvilke hensyn som er viktige og hvilken kandidat som skal brukes. KI forklarer mulighetene og konsekvensene uten å gjennomføre valget.

Studieprototypen bruker demodata med fire uker historikk og en ferdig planlagt uke 5. Ved frafall, for eksempel sykdom, sammenligner lederen forslag til hvordan eksisterende bemanning kan tilpasses. Tidligere planer vises som relevant beslutningsgrunnlag. Forslagene innføres ikke direkte i den faktiske vaktlisten. Lederen bruker skjemaer og faste handlinger for å finne alternativer. Faste regler i kode kontrollerer kompetanse, hviletid og tidskollisjoner; KI bruker relevante ansattdata og kontrollresultater til å forklare avveininger, konsekvenser og usikkerhet i et fast svarformat. Lederen kan undersøke et annet alternativ enn det som kommer øverst i sorteringen. Reell leverandørtilkobling er ikke en forutsetning for studieprototypen.

## The Problem

Utgangspunktet er en skiftleder som får beskjed om fravær kort før vaktstart. Lederen må finne en tilgjengelig erstatter, kontrollere kompetanse og nabovakter, og vurdere om flyttingen skaper et nytt bemanningsproblem. Når dette må sammenstilles manuelt fra planer, lister og telefonhenvendelser, kan det være vanskelig å få oversikt og forklare valget i ettertid.

**[ANTAKELSE]** Denne arbeidsflyten er en problemhypotese fra prosjektarbeidet. Gruppen har foreløpig ikke validert problemets hyppighet eller mulig tidsbesparelse med målgruppen.

## The Solution

Lederen starter med ansatte, vakter og bemanningsbehov for en ferdig planlagt uke 5, med uke 1–4 som historikk. Demohandlingen «Simuler fravær» markerer en valgt ansatt som utilgjengelig på en valgt vakt i uke 5 og viser bemanningsmangelen. «Finn alternativer» åpner sammenligningen. «Last inn oppdaterte vaktdata» bytter til et forhåndslaget datasett, viser hva som er endret og beregner vurderingen på nytt. Gjeldende dataversjon skal være synlig.

Ved flere morgenfravær velges ett målskift om gangen. Tidligere fravær beholdes i grunnlaget. Et undersøkt eller akseptert forslag reserverer ingen ansatte og endrer ingen vakter. Før en løsning regnes som innført ved neste fravær, må en separat demooppdatering vise den faktiske nye bemanningen; neste vurdering bruker dette oppdaterte grunnlaget. Dette er Codex sin konkretisering av sekvensiell håndtering og av at VaktMatch ikke gjennomfører vaktendringer.

Forslagene tar utgangspunkt i den eksisterende planen og viser måter å håndtere frafall på, med regelkontroll, udekket behov og konsekvenser for berørte ansatte og vakter. Historikken ligger fast. Den kan gi synlig kontekst om tidligere arbeidstid, vakttyper og sammenlignbare vakter. Historiske mønstre er ikke bevis på at en ny tildeling er gjennomførbar; nødvendige opplysninger og R1–R5 kontrolleres i det aktuelle forslaget. Historikken gir ingen skjult poengsum og endrer ikke sorteringen etter P1/P2. Nabovakter på begge sider av arbeidsuken, også inn i uke 6, må følge med når de påvirker hvilekontrollen. Separat generering av en ny ukeplan inngår ikke i MVP etter denne avklaringen.

Lederen skal kunne styre søkeomfanget i innstillinger. Grense 0 undersøker direkte erstattere; grense 1 undersøker også intern omfordeling med opptil én flytting av en eksisterende vakttildeling. Standard og maksimal grense i førsteversjonen er 1. Direkte erstattere inngår også ved grense 1. En flytting betyr at en allerede tildelt person flyttes til en annen vakt, mens en erstatter dekker vakten personen forlater; ny tildeling til en ledig person teller ikke som flytting. Alle berørte vakter må være dekket og R1–R5 kontrollert i den foreslåtte planen. Innstillingen endrer ikke regelgrunnlaget, og resultatet viser søkegrensen og konsekvensene for alle berørte. To flyttinger er neste mulige utvidelse etter vurdering av kompleksitet og målt responstid. Flere flyttinger vurderes senere dersom nytten forsvarer kostnad og tidsbruk.

Førsteversjonen skal kunne simulere tilbud og aksept: tilbud sendt, venter på svar, akseptert eller avslått. Lederen velger kandidaten som får det simulerte tilbudet og kan undersøke et annet alternativ ved avslag. For en omfordeling vises svar fra alle berørte; forslaget har full simulert aksept først når alle har akseptert. Manglende svar er fortsatt ventende. Det enkle demoscenarioet kan kjøres uten tilbudssteget, og viser da at aksept ikke er simulert. Simuleringen endrer ikke vaktlisten eller regelstatus. Demodata skal vise flere fungerende alternativer med synlige avveininger, slik at lederen kan velge også en lavere rangert kandidat.

Svaret har en fast struktur: sammenlignbare alternativer, begrunnelser, regelkontroll, konsekvenser og manglende opplysninger. Innholdet tilpasses den aktuelle vakten og ansattdataene. For hvert alternativ skal lederen kunne se kompetanse, tilgjengelighet, hviletid før og etter vakten, beregnet arbeidstid og konsekvenser for andre vakter. Lederen kan velge og prioritere blant definerte sorteringskriterier for kandidatene som oppfyller scenarioreglene. Valgte kriterier vises sammen med rangeringen; bytte av prioritering oppdaterer rekkefølge og begrunnelse uten å endre planen. Kandidater med regelavvik eller manglende kontrollopplysninger skal også kunne undersøkes, med avvik og usikkerhet synlig. Dersom ingen kandidat er bekreftet å oppfylle scenarioreglene, skal dette fremgå uten å fremstille uavklarte kandidater som ferdig vurdert.

Det vedtatte regelsettet er R1 kompetanse, R2 tilgjengelighet og R3 ingen tidskollisjon som interne scenarioregler, samt R4 minst 11 timers sammenhengende arbeidsfri og R5 høyst 40 planlagte timer i sju dager som forenklede scenarioregler med lovutgangspunkt. R4 og R5 er ikke en full juridisk kontroll: arbeidsmiljøloven åpner for unntak, og blant annet skift-, turnus-, overtids- og gjennomsnittsberegningsregler er ikke modellert. [Demoscenarioet](docs/demoscenario-fravaer.md#fem-vedtatte-scenarioregler) angir terskler, kilder og begrensninger.

P1, færrest planlagte timer etter tildeling, er standard sorteringskriterium. P2, lavest andel av avtalt timetall for samme periode, kan velges. Lederen kan prioritere kriteriene i rekkefølge; neste kriterium brukes bare når kandidater er like på det foregående. Kandidater som er like på alle valgte kriterier, vises som likeverdige. Stabil kandidat-ID kan styre visningsrekkefølgen, men skal ikke fremstilles som et faglig skille. Manglende sorteringsdata endrer ikke regelstatus, men hindrer en komplett rangering etter det berørte kriteriet.

P1/P2 og synlig historikk skal hjelpe lederen å vurdere en fair fordeling, men er ikke en full rettferdighetsmodell. Anslått kostnad vises separat fra regelstatus og rangering; et billigere alternativ blir ikke automatisk foretrukket. Kostnadene bruker bare syntetiske satser og tillegg, med synlig beregningsgrunnlag og mangler. [Kostnadsanslaget](docs/kostnadsanslag.md) beskriver Codex sin konkretisering av Odins valg, inkludert hvordan alle berørte vakter inngår ved omfordeling. Første KI-handling er «Forklar forskjellen»; flere faste forklaringshandlinger kan vurderes senere gjennom samme grensesnitt. Merverdien av KI-tekst sammenlignet med standardtekst er fortsatt uavklart.

Ved intern omfordeling beregnes P1 og P2 for kandidaten som dekker fraværsvakten, etter hele den foreslåtte omfordelingen. Konsekvensene for øvrige berørte vises separat. Simulerte tilbud og svar gjelder det konkrete forslaget og datagrunnlaget; endringer krever ny vurdering og gir ikke automatisk videreført aksept. Disse detaljene er konkretisert av Codex i [demoscenarioet](docs/demoscenario-fravaer.md#søkeomfang-og-simulert-tilbud--scrum-15).

Regelmotoren finner og kontrollerer kandidater og beregner konsekvenser. KI forklarer hva prioriteringene betyr, hvorfor alternativene skiller seg og hva et undersøkt alternativ innebærer, for eksempel redusert hvile eller økt arbeidstid. Regelgrunnlaget skal være synlig, slik at lov- og avtaleregler, interne føringer og rene demoregler ikke blandes sammen. Studieprototypen kontrollerer et navngitt scenarioregelsett; den gir ingen generell garanti om lovlighet. Hvilke faktiske regler som gjelder på en arbeidsplass, må avklares før eventuell reell bruk.

Manglende opplysninger og hvilke vurderinger de hindrer skal vises. Demoen kan laste inn et forhåndslaget, komplettert datasett og vurdere situasjonen på nytt. Ansvar for å skaffe eller rette data på en virkelig arbeidsplass avklares før reell bruk; det legges ikke automatisk til mellomlederen. Veiledningen bygger på kontrollresultatene og lederens valgte prioriteringer; den endrer ikke regelutfall eller lederens valg. Førsteversjonen gir hjelpen gjennom faste handlinger og svar, uten chat. Uten KI-nøkkel eller ved modellfeil skal samme sammenligning fungere med regelbaserte standardforklaringer.

Lederen kan undersøke konsekvensene av enhver vist kandidat, også når denne kommer lenger ned i sorteringen. VaktMatch gir forslag; undersøkelse eller valg av et forslag endrer ikke selve vaktene. I en mulig fremtidig løsning gjøres endringen i systemet som forvalter vaktplanen. I demoen representerer datasettbytte en oppdatering fra denne datakilden. Endringsoversikten viser også om ingen vakter er endret eller om bemanningen avviker fra alternativet lederen undersøkte. En observert endring er ikke i seg selv bevis på hvem som tok beslutningen eller hvorfor.

Valgt alternativ og simulerte tilbud/svar beholdes i den aktive demoøkten, knyttet til forslaget og dataversjonen de gjelder. Odin valgte 30.10.26 en liten, komplett demo med enkel tilbudssimulering og bytte mellom et begrenset sett forhåndslagde datasett. Varig beslutningslogg utsettes til Bør, etter at denne flyten fungerer og er testet. Den er dermed ikke påkrevd i førsteversjonen. Hvis funksjonen bygges senere, er den valgfri, avslått som standard og uten krav om begrunnelse. Loggen vil beskrive registrerte valg og simuleringer, ikke gjennomførte vaktendringer. Den tidligere bekreftelsesmodellen er bevart som [historikk](docs/demoscenario-fravaer.md#åpent-valg--bekreftelse-ved-regelavvik).

Demoøkten avsluttes når fanen lukkes. Etter datasettbytte beholdes tidligere valg som historikk på gammel dataversjon; de fremstår ikke som gjeldende før ny kontroll. De tidligere konkretiserte av/på-reglene for varig logging beholdes som grunnlag for en eventuell senere utvidelse i [demoscenarioet](docs/demoscenario-fravaer.md#beslutningslogg-i-demoen--scrum-17).

At historikken ligger fast gjelder søket og forslagene. En korrigert datakilde kan lastes inn som ny dataversjon; endrede historikkopplysninger vises, og berørte kontroller kjøres på nytt. Dette kan endre regelstatus når for eksempel en nabovakt i uke 4 korrigeres, selv om historikken ikke gir et eget rangeringskriterium.

Førsteversjonen bruker avgrenset regelbasert søk etter direkte erstatning og opptil én flytting. Historikk, gjennomførte/påbegynte vakter og lederlåste tildelinger beskyttes; framtidige ulåste tildelinger i uke 5 kan inngå i forslag. Søket bruker et synlig vurderingstidspunkt fra demoen. Det endrer ikke vakttider eller deler vakter. Låser bekrefter ikke regelstatus og skal ikke skjule fravær eller udekket behov.

Full og delvis dekning, regelstatus og fullført/avbrutt søk vises hver for seg. Et avbrutt søk kan vise kontrollerte funn, men ikke hevde fullstendig rangering eller at ingen løsning finnes. Ingen konkret responstid er lovet; søket og total ventetid skal måles separat. Solver og to flyttinger er mulige senere utvidelser. [Metodebeskrivelsen](docs/forslag-ved-frafall.md) konkretiserer søk, låser, statuser og målemetode fra anbefalingene Odin sluttet seg til i SCRUM-16.

## What Makes This Different

VaktMatch samler sammenligning, regelkontroll og forklaring i det øyeblikket lederen må håndtere et avvik. En viktig egenskap er at brukeren får undersøke alternativene, styre hvilke hensyn som prioriteres og forstå konsekvensene av sitt eget valg, også når det avviker fra sorteringsrekkefølgen.

Prosjektets ambisjon er å demonstrere denne avgrensede arbeidsflyten. Det er ikke dokumentert at funksjonen er unik i markedet. En tidligere, begrenset konkurrentsjekk er beholdt som bakgrunnsmateriale, med usikkerhetene beskrevet i [VaktMatch-vedlegget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/addendum.md).

## Who This Serves

**Primærbruker:** En skiftleder med bemanningsansvar som trenger et forståelig beslutningsgrunnlag under tidspress. Et vellykket resultat er at lederen kan velge en kandidat og forklare hvorfor vedkommende passer, eller forstå hvorfor vakten fortsatt står udekket.

Demonstrasjonen legges til en generell, fiktiv arbeidsplass uten bransjetilknytning, etter Odins avklaring 06.10.26. Egne brukerflater for ansatte og forhåndsgodkjente vikarer er ikke del av førsteversjonen.

## Success Criteria

Følgende er foreslåtte kriterier som skal testes, ikke oppnådde resultater:

- Ingen kandidat som vises som «oppfyller scenarioreglene», bryter det valgte regelsettet i testscenarioene. Manglende kontrolldata gir uavklart status. Lederens preferanse for et alternativ endrer ikke kontrollresultatet.
- Sammenligningen viser udekket behov når ingen undersøkte alternativer oppfyller scenarioreglene. Valgt søkeomfang og manglende grunnlag er synlig; resultatet påstår ikke at alle mulige omplanlegginger er undersøkt.
- Forslag ved frafall i uke 5 vises separat fra gjeldende plan, med synlig kontekst fra uke 1–4. Historikken og vaktlisten endres ikke ved undersøkelse av forslag. Udekket behov og manglende kontrollgrunnlag er synlig.
- Opplysninger i KI-forklaringen kan spores til scenarioets data, regelkontroll og definerte prioriteringer. Forklaringen endrer ikke kandidatstatus eller rangering.
- Lederen kan endre prioriteringen i samme scenario og se en rangering med begrunnelse som følger valget. Regelstatusene beholdes; sortering alene endrer ikke planen. Manglende data til et valgt sorteringskriterium synliggjøres, og systemet skal ikke hevde en fullstendig rangering uten nødvendig grunnlag.
- Sammenligningen viser alternativer eller udekket behov, regelkontroll, konsekvenser og manglende opplysninger i et fast format. Ingen kandidat presenteres som ferdig kontrollert når nødvendige kontrollopplysninger mangler.
- Lederen kan undersøke en lavere rangert kandidat og se beregnede konsekvenser. KI-veiledningen forklarer avveiningen uten å bytte kandidaten eller prioriteringen på lederens vegne. Forslag og undersøkelse av alternativer endrer ikke vaktene i datagrunnlaget.
- Søkegrense 0 viser direkte erstattere, mens standardgrensen 1 også tillater én intern flytting. Forslag som etterlater en annen vakt udekket, vises ikke som komplette løsninger. Flere fungerende alternativer og konsekvensene for berørte ansatte skal kunne sammenlignes.
- Tilbud og svar kan simuleres for lederens valgte alternativ. Ventende svar, avslag og full aksept skilles tydelig; når tilbudssteget hoppes over i det enkle eksemplet, vises det som ikke simulert. Ingen av disse statusene gjennomfører en vaktendring.
- Når et oppdatert datasett lastes inn, bygger en ny vurdering på dette grunnlaget. Et forslag skal ikke vises som gjennomført bare fordi det er undersøkt eller foretrukket i appen.
- Fravær kan simuleres på valgt ansatt og vakt. Datasettbytte viser dataversjon, endrede eller uendrede vakter og manglende opplysninger; tidligere simulert aksept videreføres ikke automatisk.
- Valg og simulerte svar er tilgjengelige i aktiv demoøkt. Varig beslutningslogg er Bør og utsettes; logging er ikke nødvendig for å gjennomføre førsteversjonens flyt.
- Flere fravær kan håndteres ett etter ett på gjeldende grunnlag, uten at tidligere fravær nullstilles eller et simulert svar regnes som gjennomført bemanning.
- Anslått kostnad for alle berørte vakter og forskjellen fra gjeldende grunnlag kan etterprøves med syntetiske satser og tillegg. Manglende kostnadsdata vises; kostnad endrer ikke P1/P2 eller regelstatus.
- Sammenligning, visning av historisk kontekst og vurdering av oppdaterte data kan gjennomføres uten KI-nøkkel og ved modellfeil, med regelbaserte standardforklaringer.

**Valgfri brukertest (forslag fra Codex):** La en testbruker forklare en avveining, en konsekvens og eventuell manglende informasjon i et scenario. Tidsbruk mot manuell oversikt kan også sammenlignes senere. Dette er et testforslag, ikke et leveransekrav eller krav om begrunnelse i appen, i tråd med [faglærerens råd](tilbakemelding-product-brief.md).

For studiearbeidet skal gruppen også dokumentere BMAD-bruken, egne valg og hvordan KI-generert kode er kvalitetssikret.

## Scope

**Foreslått førsteversjon:** Én fiktiv arbeidsplass, 8–10 ansatte og noen forhåndsgodkjente eksterne vikarer tilknyttet et bemanningsforetak. Demoen bruker fiktive (syntetiske) data med fire uker historikk, ferdig planlagt uke 5, kompetanse, tilgjengelighet og nødvendige nabovakter. Ett simulert sykefravær i uke 5 utløser sammenligning av alternativer på én side gjennom en fast handling. Flyten kan gjentas for neste fravær på gjeldende grunnlag; samlet løsning for flere samtidige fravær vurderes senere. KI forklarer kontrollerte data og historisk kontekst i et fast svarformat. Forslag kontrolleres mot R1–R5; P1 og P2 beregnes for uke 5. Søkegrense 0–1 er lederstyrt med 1 som standard. Forhåndslagde datasett viser oppdateringer gjennom en demohandling med endringsoversikt og ny kontroll. Anslått kostnad med syntetiske satser og tillegg vises per alternativ. Valg og simulerte svar beholdes i økten; varig beslutningslogg utsettes til Bør. Grensesnittet skal fungere i nettleser på mobil og PC.

**Avgrensning av planforslag:** MVP støtter forslag ved frafall i en eksisterende ukeplan, med fire ukers historikk som synlig beslutningsgrunnlag. Dette erstatter den tidligere separate funksjonen for enkel plangenerering. Stians turnusgenerator-idé og tidligere begrunnelser er bevart som kreditert bakgrunn i [VaktMatch-vedlegget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/addendum.md). Endringen bygger på Odins valg i samtalen om SCRUM-16 innenfor tidligere dokumentert felles delegering; Stian tilskrives ikke de konkrete detaljvalgene.

**Utenfor førsteversjonen:** AI-chat, friteksttolkning av behov og ønsker, full periodeplanlegging med preferanser og helgefordeling, åpen vikarmarkedsplass, reelle persondata, reelle integrasjoner med HR- og turnussystemer, innføring av planforslag og gjennomføring av foreslåtte vaktendringer i den faktiske vaktlisten, samt produksjonsdrift. En eventuell demofunksjon for å bytte datasett representerer en oppdatering fra datakilden, ikke en utført lederbeslutning i VaktMatch.

**Valg 30.10.26:** Odin beholder enkel tilbudssimulering og begrenset datasettbytte som Må i sluttresultatet, utsetter varig logg til Bør og velger én KI-handling først. Fravær håndteres ett etter ett. Anslått kostnad med syntetiske satser og tillegg inngår i førsteversjonen. Lederlåser i grensesnittet beholder Bør-statusen fra PRD-en. Dette er Odins valg innenfor den delegerte myndigheten; det fremstilles ikke som begge deltakernes valg av detaljene. Se [PRD](_bmad-output/planning-artifacts/prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md) og endringsloggen E35.

**Gjenstår å avklare:**

- **Implementering og ytelse:** Den avklarte søkemetoden, låser og resultatstatuser må implementeres og testes. Responstid må måles på representative data før eventuelle tidsmål eller større søkeomfang velges.
- **Demodata og implementering:** Fullstendige datasett med fire uker historikk, planlagt uke 5, nødvendige nabovakter, fasit for fravær/oppdateringer og syntetiske kostnadsdata gjenstår. Varig beslutningslogg og lagringsteknikk vurderes etter at demoflyten er testet. Ansvar for datakvalitet ved reell bruk avklares senere.
- **Gjennomføring:** React og Python/FastAPI brukes som utgangspunkt for lokal oppstart. Odin følger opp UX, grensesnitt, sammenligning, prioritering og forklaringer; Stian følger opp datagrunnlag, regelmotor, søk og teknisk oppsett. Fordelingen kan justeres. KI-modell velges når oppgavene, input og svarformat er mer konkrete (SCRUM-59); standardforklaringer lages først. Hosting og Supabase/RLS vurderes senere, uten et leverandørvalg nå. Opphav, avgrensning og gjenstående tekniske detaljer står i [teknologivalgene](docs/teknologivalg.md).

**Arbeidsgrunnlag for konkretisering:** [Fraværsscenarioet](docs/demoscenario-fravaer.md) viser ansattdata, de fem vedtatte scenarioreglene, P1 og P2 og forventede svar ved gyldige alternativer, ingen direkte erstatter og manglende data. Regelsettet og sorteringen ble besluttet av Odin 21.10.26 innenfor den felles delegeringen han har gjengitt. Eksemplet er ikke en ferdig implementasjon eller et komplett datasett med alle vakter.

**Tilrettelegging for senere chat:** Datatilgang, regelberegning, KI-forklaring og visning skal ha tydelige ansvarsgrenser. En eventuell samtaleassistent skal kunne bruke de samme funksjonene og kontrollene. Førsteversjonen trenger ikke chatgrensesnitt, samtalehistorikk eller en generell agentplattform.

## Vision

Hvis prototypen viser verdi, kan neste steg være å teste den med skiftledere og mer realistiske scenarioer. Odin ser for seg et beslutningsstøttelag koblet til et løpende oppdatert bemanningssystem, for eksempel Quinyx, der vaktendringer gjøres i kildesystemet og VaktMatch gir nye vurderinger når data endres. Dette er en produktidé; leverandørtilgang, integrasjonsmuligheter og oppdateringsfrekvens er ikke undersøkt eller lovet. En samtaleassistent kan legges til hvis bruk eller testing viser behov for friere oppfølging. Flere avdelinger og planlegging over lengre perioder er også mulige senere utvidelser. Reell bruk krever eget arbeid med tilgangsstyring, personvern, regelgrunnlag og drift. Prinsippet videreføres: etterprøvbar regelkontroll, forståelige forklaringer og menneskelig beslutning.
