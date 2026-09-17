---
title: VaktMatch
status: draft
created: 2026-09-17
updated: 2026-09-17
---

# Product Brief: VaktMatch

**Gruppe:** Odin A Andreassen og Stian Lundberg · IBE160, høsten 2026  
**Metode:** BMAD (`bmad-product-brief`) · **Innlevering:** søndag 20. september 2026

VaktMatch er valgt som gruppens prosjekt. Dette er et oppdatert utkast til innlevering; detaljert MVP-omfang og arbeidsdeling gjenstår å bekrefte sammen.

## Executive Summary

VaktMatch er en planlagt responsiv webapp som hjelper en skiftleder når en vakt plutselig mangler bemanning. Lederen får sammenligne intern omfordeling, ekstravakt og ekstern vikar, med forklaring på hvem som oppfyller kravene og hvilke konsekvenser hvert alternativ har. Målet er å gjøre beslutningen raskere og enklere å etterprøve.

Studieprototypen skal generere et enkelt ukesgrunnlag og deretter håndtere ett sykefravær i planen. Faste regler i kode kontrollerer kompetanse, hviletid og tidskollisjoner. KI tolker behov skrevet i fritekst og forklarer kontrollerte resultater. Lederen tar den endelige beslutningen. Prosjektet utvikles med BMAD og syntetiske data, slik at gruppen kan demonstrere og teste hele forløpet.

## The Problem

Utgangspunktet er en skiftleder som får beskjed om fravær kort før vaktstart. Lederen må finne en tilgjengelig erstatter, kontrollere kompetanse og nabovakter, og vurdere om flyttingen skaper et nytt bemanningsproblem. Når dette må sammenstilles manuelt fra planer, lister og telefonhenvendelser, kan det være vanskelig å få oversikt og forklare valget i ettertid.

**[ANTAKELSE]** Denne arbeidsflyten er en problemhypotese fra prosjektarbeidet. Gruppen har foreløpig ikke validert problemets hyppighet eller mulig tidsbesparelse med målgruppen.

## The Solution

Lederen starter med ansatte og bemanningsbehov for én uke. Systemet lager et ukesgrunnlag og viser eventuelle udekkede vakter. Når fravær registreres, viser en sammenligningsside aktuelle alternativer og hvorfor andre kandidater er utelukket.

For hvert alternativ skal lederen kunne se kompetanse, tilgjengelighet, hviletid før og etter vakten, beregnet arbeidstid og konsekvenser for andre vakter. Rangeringen skal bygge på synlige kriterier som gruppen avklarer før implementering. Manglende opplysninger merkes som uavklart. Dersom ingen kandidat oppfyller scenarioreglene, sier systemet det tydelig.

KI hjelper med å tolke behovet og forklare forskjellene med utgangspunkt i kontrollerte data. Regelkontrollen skjer i kode, og lederen må bekrefte valget før planen endres. Appen skal beskrive resultater som kontrollert mot et navngitt scenarioregelsett; den gir ingen generell garanti om lovlighet.

## What Makes This Different

VaktMatch samler sammenligning, regelkontroll og forklaring i det øyeblikket lederen må håndtere et avvik. En viktig egenskap er at brukeren både får se aktuelle kandidater og forstå hvorfor et alternativ faller bort eller flytter problemet til en annen vakt.

Prosjektets ambisjon er å demonstrere denne avgrensede arbeidsflyten. Det er ikke dokumentert at funksjonen er unik i markedet. En tidligere, begrenset konkurrentsjekk er beholdt som bakgrunnsmateriale, med usikkerhetene beskrevet i [VaktMatch-vedlegget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/addendum.md).

## Who This Serves

**Primærbruker:** En skiftleder med bemanningsansvar som trenger et forståelig beslutningsgrunnlag under tidspress. Et vellykket resultat er at lederen kan velge en kandidat og forklare hvorfor vedkommende passer, eller forstå hvorfor vakten fortsatt står udekket.

**[ANTAKELSE]** Demonstrasjonen legges til en fiktiv lager- eller logistikkbedrift. Ansatte og forhåndsgodkjente vikarer inngår som syntetiske data; egne brukerflater for dem er ikke del av førsteversjonen.

## Success Criteria

Følgende er foreslåtte kriterier som skal testes, ikke oppnådde resultater:

- Ingen forslag som vises som godkjent, bryter det valgte regelsettet i testscenarioene. Manglende data gir uavklart status.
- Både ukegeneratoren og avvikshåndteringen viser udekket behov når det ikke finnes en løsning innenfor reglene.
- En testbruker kan finne en aktuell kandidat og forklare hvorfor minst ett annet alternativ er utelukket.
- Opplysninger i KI-forklaringen kan spores til scenarioets data og regelkontroll.
- Tidsbruk og forståelse sammenlignes for samme bemanningsoppgave med manuell oversikt og med prototypen. Måltall fastsettes etter en første prøve.

For studiearbeidet skal gruppen også dokumentere BMAD-bruken, egne valg og hvordan KI-generert kode er kvalitetssikret.

## Scope

**Foreslått førsteversjon:** Én fiktiv arbeidsplass, 8–10 ansatte og noen forhåndsgodkjente eksterne vikarer tilknyttet et bemanningsforetak. Et enkelt generert ukesgrunnlag bygger på minimumsnivået i Stians turnusgenerator-idé. Ett sykefravær utløser sammenligning av alternativer på én side. Samme regelmotor bruker 3–5 eksplisitte regler ved generering og avvikshåndtering, med nødvendige nabovakter som kontrollgrunnlag. Grensesnittet skal fungere i nettleser på mobil og PC.

**Utenfor førsteversjonen:** Full periodeplanlegging med preferanser og helgefordeling, åpen vikarmarkedsplass, reelle persondata, integrasjoner med HR- og turnussystemer, automatisk vakttildeling og produksjonsdrift.

**Gjenstår å avklare:** Endelig demonstrasjonsdomene, de konkrete reglene og rangeringskriteriene, eventuell simulering av tilbud og aksept, teknologistakk og arbeidsdeling.

## Vision

Hvis prototypen viser verdi, kan neste steg være å teste den med skiftledere og mer realistiske scenarioer. Senere kan løsningen utvides med flere avdelinger, planlegging over lengre perioder og integrasjoner med eksisterende bemanningssystemer. Reell bruk krever eget arbeid med tilgangsstyring, personvern, regelgrunnlag og drift. Prinsippet videreføres: etterprøvbar regelkontroll, forståelige forklaringer og menneskelig beslutning.
