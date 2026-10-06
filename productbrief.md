---
title: VaktMatch
status: draft
document_role: current_product_brief
created: 2026-09-17
updated: 2026-10-07
---

# Product Brief: VaktMatch

**Gruppe:** Odin A Andreassen og Stian Lundberg · IBE160, høsten 2026  
**Metode:** BMAD (`bmad-product-brief`) · **Innlevering:** søndag 20. september 2026

VaktMatch er valgt som gruppens prosjekt. Arbeidsutkastet videreutvikles etter Odins innspill 06.–07.10.26: faste handlinger og konkrete KI-svar, med forslag basert på et syntetisk datasett. VaktMatch skal gi beslutningsstøtte og kunne vise endringer i datagrunnlaget; selve vaktendringen kan skje i et annet system. Chat er en mulig senere utvidelse. Endringene fra 06.–07.10.26 er ennå ikke avklart med Stian og publiseres som Odins innspill, bearbeidet med Codex, til felles vurdering. Detaljert MVP-omfang, teknologistakk og arbeidsdeling er fortsatt åpne; publiseringen innebærer ingen felles godkjenning av endringene.

**Dokumentrolle (oppdatert 07.10.26):** Dette er repoets eneste gjeldende produktbrief, fortsatt med status utkast. Alternativforslag, vedlegg og historikk er samlet i [dokumentoversikten](README.md#dokumentoversikt). KI-rollen og arbeidsflyten er oppdatert etter Odins avklaringer og [faglærerens tilbakemelding](tilbakemelding-product-brief.md); endelig regelsett og fullstendige demodata gjenstår. Oppdateringen er skrevet med Codex. [Endringsloggen](docs/productbrief-endringslogg.md) viser hva som er endret siden første versjon, hvorfor og hvilket grunnlag valgene har. Den løpende prosesshistorikken finnes i [.memlog.md](.memlog.md).

## Executive Summary

VaktMatch er en planlagt responsiv webapp som gir en skiftleder informasjon og kontekst når en vakt plutselig mangler bemanning. Lederen får undersøke bemanningsalternativer og se relevante konflikter, arbeidstidsgrenser, hviletid og interne føringer. «Helhetsoversikt» betyr her å gjøre den tilgjengelige, relevante informasjonen forståelig, med synlige begrensninger i grunnlaget. Lederen beholder beslutningsmyndigheten og velger hvilke hensyn som er viktige og hvilken kandidat som skal brukes. KI forklarer mulighetene og konsekvensene uten å gjennomføre valget.

Studieprototypen skal bruke en ferdig syntetisk vaktplan som datagrunnlag, kunne generere et enkelt planforslag og demonstrere alternativer ved ett sykefravær. Odin presiserte 07.10.26 at plangenerering skal beholdes, mens forslaget ikke innføres direkte i den faktiske vaktlisten. Lederen bruker skjemaer og faste handlinger for å finne alternativer. Faste regler i kode kontrollerer kompetanse, hviletid og tidskollisjoner; KI bruker relevante ansattdata og kontrollresultater til å forklare avveininger, konsekvenser og usikkerhet i et fast svarformat. Lederen kan undersøke et annet alternativ enn det som kommer øverst i sorteringen. Reell leverandørtilkobling er ikke en forutsetning for studieprototypen.

## The Problem

Utgangspunktet er en skiftleder som får beskjed om fravær kort før vaktstart. Lederen må finne en tilgjengelig erstatter, kontrollere kompetanse og nabovakter, og vurdere om flyttingen skaper et nytt bemanningsproblem. Når dette må sammenstilles manuelt fra planer, lister og telefonhenvendelser, kan det være vanskelig å få oversikt og forklare valget i ettertid.

**[ANTAKELSE]** Denne arbeidsflyten er en problemhypotese fra prosjektarbeidet. Gruppen har foreløpig ikke validert problemets hyppighet eller mulig tidsbesparelse med målgruppen.

## The Solution

Lederen starter med et datagrunnlag som viser ansatte, vakter og bemanningsbehov for en avgrenset periode; én uke er foreløpig utgangspunkt. Når grunnlaget viser et fravær, velger lederen «Finn alternativer» og får en sammenligningsside. Førsteversjonen bruker syntetiske data. Hvordan fravær og senere endringer tilføres demodataene, gjenstår å konkretisere.

Lederen skal også kunne generere et enkelt planforslag for den avgrensede perioden. Forslaget vises separat fra gjeldende vaktliste, med foreslått bemanning, regelkontroll, udekket behov og konsekvenser. Kodebasert generering og avvikshåndtering bruker samme scenarioregler; KI forklarer resultatet. Å generere eller undersøke forslaget erstatter ikke vaktlisten i datagrunnlaget. Detaljene for hvilke eksisterende tildelinger som kan foreslås endret, og hvilke som skal ligge fast, gjenstår å avklare.

Lederen skal kunne styre søkeomfanget i innstillinger. Mulige valg er direkte erstattere og intern omfordeling, men hvilke søkemåter førsteversjonen støtter, grensene for antall flyttinger og standardvalget er åpne. Innstillingen styrer hvilke alternativer som undersøkes; den endrer ikke kontrollresultatene eller regelgrunnlaget. Resultatet må vise hvilket søkeomfang vurderingen gjelder.

Svaret har en fast struktur: sammenlignbare alternativer, begrunnelser, regelkontroll, konsekvenser og manglende opplysninger. Innholdet tilpasses den aktuelle vakten og ansattdataene. For hvert alternativ skal lederen kunne se kompetanse, tilgjengelighet, hviletid før og etter vakten, beregnet arbeidstid og konsekvenser for andre vakter. Lederen kan velge og prioritere blant definerte sorteringskriterier for kandidatene som oppfyller scenarioreglene. Valgte kriterier vises sammen med rangeringen; bytte av prioritering oppdaterer rekkefølge og begrunnelse uten å endre planen. Kandidater med regelavvik eller manglende kontrollopplysninger skal også kunne undersøkes, med avvik og usikkerhet synlig. Dersom ingen kandidat er bekreftet å oppfylle scenarioreglene, skal dette fremgå uten å fremstille uavklarte kandidater som ferdig vurdert.

Regelmotoren finner og kontrollerer kandidater og beregner konsekvenser. KI forklarer hva prioriteringene betyr, hvorfor alternativene skiller seg og hva et undersøkt alternativ innebærer, for eksempel redusert hvile eller økt arbeidstid. Regelgrunnlaget skal være synlig, slik at lov- og avtaleregler, interne føringer og rene demoregler ikke blandes sammen. Studieprototypen kontrollerer et navngitt scenarioregelsett; den gir ingen generell garanti om lovlighet. Hvilke faktiske regler som gjelder på en arbeidsplass, må avklares før eventuell reell bruk.

Manglende opplysninger og virkningen på vurderingen skal vises. Der grunnlaget tillater det, kan appen foreslå hva som vil gjøre vurderingen sikrere. Det er ikke avklart hvem som skal skaffe eller rette opplysningene; dette legges ikke automatisk som en oppgave til mellomlederen. Veiledningen bygger på kontrollresultatene og lederens valgte prioriteringer; den endrer ikke regelutfall eller lederens valg. Førsteversjonen gir hjelpen gjennom faste handlinger og svar, uten chat. Uten KI-nøkkel eller ved modellfeil skal samme sammenligning fungere med regelbaserte standardforklaringer.

Lederen kan undersøke konsekvensene av enhver vist kandidat, også når denne kommer lenger ned i sorteringen. VaktMatch gir forslag; undersøkelse eller valg av et forslag endrer ikke selve vaktene. I en mulig fremtidig løsning gjøres endringen i systemet som forvalter vaktplanen. Når VaktMatch mottar et oppdatert datagrunnlag, kan appen vise endringene og vurdere situasjonen på nytt. Hvordan oppdateringer hentes eller simuleres, er åpent. En observert endring er ikke i seg selv bevis på hvem som tok beslutningen eller hvorfor.

Lagring av lederens valg og krav om skriftlig begrunnelse er separate, åpne produktvalg. Odin ønsker at funksjonaliteten skal kunne slås av når den bare følger interne retningslinjer og ikke er lovpålagt. Dette er ikke en avklaring av eventuelle lovkrav. Standardinnstillinger og MVP-omfang gjenstår. Tidligere alternativer for bekreftelse ved regelavvik er bevart som historikk i [demoscenarioet](docs/demoscenario-fravaer.md#åpent-valg--bekreftelse-ved-regelavvik); de er ikke valgt som en gjennomføringsflyt i VaktMatch.

## What Makes This Different

VaktMatch samler sammenligning, regelkontroll og forklaring i det øyeblikket lederen må håndtere et avvik. En viktig egenskap er at brukeren får undersøke alternativene, styre hvilke hensyn som prioriteres og forstå konsekvensene av sitt eget valg, også når det avviker fra sorteringsrekkefølgen.

Prosjektets ambisjon er å demonstrere denne avgrensede arbeidsflyten. Det er ikke dokumentert at funksjonen er unik i markedet. En tidligere, begrenset konkurrentsjekk er beholdt som bakgrunnsmateriale, med usikkerhetene beskrevet i [VaktMatch-vedlegget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/addendum.md).

## Who This Serves

**Primærbruker:** En skiftleder med bemanningsansvar som trenger et forståelig beslutningsgrunnlag under tidspress. Et vellykket resultat er at lederen kan velge en kandidat og forklare hvorfor vedkommende passer, eller forstå hvorfor vakten fortsatt står udekket.

Demonstrasjonen legges til en generell, fiktiv arbeidsplass uten bransjetilknytning, etter Odins avklaring 06.10.26. Ansatte og forhåndsgodkjente vikarer inngår som syntetiske data; egne brukerflater for dem er ikke del av førsteversjonen.

## Success Criteria

Følgende er foreslåtte kriterier som skal testes, ikke oppnådde resultater:

- Ingen kandidat som vises som «oppfyller scenarioreglene», bryter det valgte regelsettet i testscenarioene. Manglende kontrolldata gir uavklart status. Lederens preferanse for et alternativ endrer ikke kontrollresultatet.
- Sammenligningen viser udekket behov når ingen undersøkte alternativer oppfyller scenarioreglene. Valgt søkeomfang og manglende grunnlag er synlig; resultatet påstår ikke at alle mulige omplanlegginger er undersøkt.
- Et generert planforslag vises separat fra gjeldende vaktliste og kontrolleres mot samme scenarioregler som bemanningsalternativene. Udekket behov og manglende kontrollgrunnlag skal være synlig. Generering endrer ikke den faktiske vaktlisten.
- Opplysninger i KI-forklaringen kan spores til scenarioets data, regelkontroll og definerte prioriteringer. Forklaringen endrer ikke kandidatstatus eller rangering.
- Lederen kan endre prioriteringen i samme scenario og se en rangering med begrunnelse som følger valget. Regelstatusene beholdes; sortering alene endrer ikke planen. Manglende data til et valgt sorteringskriterium synliggjøres, og systemet skal ikke hevde en fullstendig rangering uten nødvendig grunnlag.
- Sammenligningen viser alternativer eller udekket behov, regelkontroll, konsekvenser og manglende opplysninger i et fast format. Ingen kandidat presenteres som ferdig kontrollert når nødvendige kontrollopplysninger mangler.
- Lederen kan undersøke en lavere rangert kandidat og se beregnede konsekvenser. KI-veiledningen forklarer avveiningen uten å bytte kandidaten eller prioriteringen på lederens vegne. Forslag og undersøkelse av alternativer endrer ikke vaktene i datagrunnlaget.
- Når et oppdatert datasett lastes inn, bygger en ny vurdering på dette grunnlaget. Et forslag skal ikke vises som gjennomført bare fordi det er undersøkt eller foretrukket i appen.
- Plangenerering, sammenligning og vurdering av oppdaterte data kan gjennomføres uten KI-nøkkel og ved modellfeil, med regelbaserte standardforklaringer.

**Valgfritt forslag til brukertest fra Codex:** La en testbruker undersøke et scenario og forklare en avveining, en konsekvens og eventuell manglende informasjon. Sammenligning av tidsbruk mot manuell oversikt kan vurderes senere. Dette er ikke et dokumentert emnekrav, et hovedkriterium eller et krav om at lederen skal begrunne valgene i appen. [Faglærerens tilbakemelding](tilbakemelding-product-brief.md) anbefaler at sammenligningen av tidsbruk og forståelse eventuelt beholdes som brukertest, ikke hovedkriterium.

For studiearbeidet skal gruppen også dokumentere BMAD-bruken, egne valg og hvordan KI-generert kode er kvalitetssikret.

## Scope

**Foreslått førsteversjon:** Én fiktiv arbeidsplass, 8–10 ansatte og noen forhåndsgodkjente eksterne vikarer tilknyttet et bemanningsforetak. Et syntetisk datasett med konkrete vakter, kompetanse, tilgjengelighet og nødvendige nabovakter danner grunnlaget. Appen kan generere et enkelt planforslag uten å endre gjeldende vaktliste. Ett sykefravær utløser sammenligning av alternativer på én side gjennom en fast handling. KI forklarer kontrollerte data i et fast svarformat. Generering og avvikshåndtering bruker samme 3–5 eksplisitte scenarioregler. Lederstyrt søkeomfang konkretiseres til et begrenset sett innstillinger. Oppdateringer i datagrunnlaget kan demonstreres med syntetiske data; mekanismen er ikke valgt. Grensesnittet skal fungere i nettleser på mobil og PC.

**Avgrensning av plangenerering:** Enkel plangenerering beholdes som forslag i MVP. Ferdig syntetisk datagrunnlag og generering av planforslag kan inngå sammen. Codex tolket først valget av ferdig datasett som at generering skulle fjernes; Odin korrigerte dette 07.10.26. Skillet gjelder å generere et forslag og å innføre det i den faktiske vaktlisten. Minimumsnivået i Stians turnusgenerator-idé er fortsatt bakgrunn for enkel generering; bidraget og tidligere begrunnelser er bevart i [VaktMatch-vedlegget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/addendum.md). Dette er Odins presiserte arbeidsretning, ikke en ny felles godkjenning av omfanget.

**Utenfor førsteversjonen:** AI-chat, friteksttolkning av behov og ønsker, full periodeplanlegging med preferanser og helgefordeling, åpen vikarmarkedsplass, reelle persondata, reelle integrasjoner med HR- og turnussystemer, innføring av planforslag og gjennomføring av foreslåtte vaktendringer i den faktiske vaktlisten, samt produksjonsdrift. En eventuell demofunksjon for å bytte datasett representerer en oppdatering fra datakilden, ikke en utført lederbeslutning i VaktMatch.

**Gjenstår å avklare:** Planhorisont (én uke er foreløpig utgangspunkt), hvilke tildelinger plangenereringen kan foreslå endret og hvilke som skal ligge fast, konkrete regler og deres grunnlag, sorteringskriterier med standardvalg og lik rangering, støttede søkemåter og grenser for intern omfordeling, fullstendige demodata med fasit for både generering og fravær, hvordan oppdateringer lastes inn og vises, ansvar for manglende opplysninger, eventuell beslutningslogg og begrunnelsesinnstilling, teknologistakk, modellvalg og arbeidsdeling. Simulering av tilbud og aksept er ikke valgt.

**Arbeidsgrunnlag for konkretisering:** [Forslaget til fraværsscenario](docs/demoscenario-fravaer.md) viser ansattdata, fem tallfestede scenarioregler, eksempler på lederstyrt sortering og forventede svar ved gyldige alternativer, ingen direkte erstatter og manglende data. Lederstyrt prioritering følger Odins innspill 06.10.26. Regeltall, konkrete sorteringsvalg og beregningsmåter er forslag fra Codex og gjenstår å avklare; eksemplet er ikke en ferdig implementasjon eller et komplett datasett med alle vakter.

**Tilrettelegging for senere chat:** Datatilgang, regelberegning, KI-forklaring og visning skal ha tydelige ansvarsgrenser. En eventuell samtaleassistent skal kunne bruke de samme funksjonene og kontrollene. Førsteversjonen trenger ikke chatgrensesnitt, samtalehistorikk eller en generell agentplattform.

## Vision

Hvis prototypen viser verdi, kan neste steg være å teste den med skiftledere og mer realistiske scenarioer. Odin ser for seg et beslutningsstøttelag koblet til et løpende oppdatert bemanningssystem, for eksempel Quinyx, der vaktendringer gjøres i kildesystemet og VaktMatch gir nye vurderinger når data endres. Dette er en produktidé; leverandørtilgang, integrasjonsmuligheter og oppdateringsfrekvens er ikke undersøkt eller lovet. En samtaleassistent kan legges til hvis bruk eller testing viser behov for friere oppfølging. Flere avdelinger og planlegging over lengre perioder er også mulige senere utvidelser. Reell bruk krever eget arbeid med tilgangsstyring, personvern, regelgrunnlag og drift. Prinsippet videreføres: etterprøvbar regelkontroll, forståelige forklaringer og menneskelig beslutning.
