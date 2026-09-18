---
title: VaktMatch – Turnusgenerator (alternativt forslag)
status: draft
created: 2026-09-18
updated: 2026-09-18
---

# Product Brief: VaktMatch – Turnusgenerator (alternativt forslag)

**Gruppe:** Odin A Andreassen og Stian Lundberg · IBE160, høsten 2026
**Status:** Forslag fra Stian til en alternativ/utvidet retning for VaktMatch, lagt frem til vurdering sammen med Odin. Dette er **ikke** en beslutning, og det endrer eller erstatter ikke den gjeldende [productbrief.md](../../../../../productbrief.md), som beholder sitt scope (ukesgrunnlag + sammenligning ved ett sykefravær) inntil gruppen eventuelt beslutter noe annet.

## Executive Summary

VaktMatch kan angripes fra en annen vinkel enn dagens avvikshåndtering: i stedet for å sammenligne alternativer når én vakt mangler bemanning, kan systemet generere en hel, gyldig og rettferdig turnusplan for en periode (f.eks. to uker) direkte fra bemanningsbehov, ansattes tilgjengelighet/kompetanse og et definert regelsett. Kombinatorikken bak en slik plan er et klassisk NP-hardt optimaliseringsproblem — for mange ansatte, skift og regler til å løse for hånd eller ved gjetning.

Forslaget er å la en regelbasert optimaliseringsmotor (en constraint-solver) løse selve planleggingsproblemet, mens en språkmodell brukes på toppen: til å tolke bemanningsbehov og ansattes ønsker skrevet i fritekst, og til å forklare resultatet i naturlig språk — inkludert hvorfor planen ser ut som den gjør, og hvilke avveininger som er gjort. Dette gir en tydelig og etterprøvbar arbeidsdeling mellom KI og eksakt beregning, i stedet for å be en språkmodell løse et matteproblem den ikke er pålitelig på.

Dette representerer en større kjernefunksjon (generering av en hel periodeplan) enn dagens productbrief.md, som er avgrenset til å generere ett ukesgrunnlag og deretter sammenligne alternativer ved ett enkelt sykefravær.

## The Problem

En som setter opp turnusplaner for en gruppe ansatte med skiftarbeid, må balansere flere krav samtidig: dekke bemanningsbehovet for hvert skift, overholde lovpålagte regler (f.eks. minimum hviletid mellom vakter, maks antall vakter på rad), ta hensyn til hver ansatts kompetanse og tilgjengelighet, og fordele belastende vakter (helg, natt, uønskede vakter) noenlunde rettferdig over tid. Manuelt er dette tidkrevende og feilutsatt allerede ved et lite antall ansatte, og antall mulige kombinasjoner vokser eksplosivt med antall ansatte og skift.

**[ANTAKELSE]** Dette er en problemhypotese overtatt fra prosjektarbeidet omkring VaktMatch. Gruppen har ikke validert hvor mye tid dagens manuelle planlegging faktisk tar, eller hvor ofte planer må endres i etterkant, hos en reell målgruppe.

## The Solution

Planleggeren registrerer ansatte med kompetanse, stillingsprosent og tilgjengelighet, og definerer bemanningsbehovet per skift og dag for en periode. Systemet genererer en turnusplan som dekker behovet uten å bryte harde regler (hviletid, maks vakter på rad, kompetansekrav), og viser planen i en kalender/tabellvisning.

Utover minimumsnivået kan planen også vektlegge rettferdighet (jevn fordeling av helg/natt/uønskede vakter over tid) og ta hensyn til ferieønsker og fridag-forespørsler som «myke» preferanser. Der planen ikke kan dekke behovet fullt ut, eller må bryte en mykere preferanse for å overholde en hardere regel, skal systemet vise dette tydelig med en forklaring — ikke bare levere en plan uten kontekst.

Teknisk deles arbeidet i to lag: en regelbasert optimaliseringskjerne (constraint-solver) løser selve tildelingsproblemet og garanterer at harde regler overholdes, mens en språkmodell tolker fritekst-input (f.eks. «jeg vil helst ikke jobbe fredager») og forklarer resultatet og eventuelle avveininger i naturlig språk. Ved akutt fravær (f.eks. sykdom) kan samme motor foreslå hvem som kan ta vakten, basert på kompetanse, hviletid og rettferdighet.

## What Makes This Different

Den sentrale, bevisste avgrensningen er hvor KI *ikke* brukes: til å løse selve kombinatorikkproblemet. Alternativet — å la en språkmodell generere hele planen direkte — er vurdert og lagt bort, fordi språkmodeller ikke er pålitelige på eksakt kombinatorisk optimalisering og risikerer regelbrudd (full vurdering av begge strategiene og av bibliotekvalg står i addendum). Ved å holde solveren og språkmodellen adskilt får hver gjøre det den er god på, med en etterprøvbar garanti for at harde regler overholdes.

**[ANTAKELSE]** Det er ikke dokumentert at selve konseptet (turnusgenerering med forklarende KI-lag) er unikt i markedet — kommersielle turnussystemer finnes allerede. Differensieringen her er prosjektets demonstrasjon av arbeidsdelingen mellom solver og språkmodell, ikke en påstått markedsunik funksjon.

## Who This Serves

**Primærbruker:** En planlegger/leder med bemanningsansvar for en gruppe ansatte i skiftarbeid, som trenger en gyldig og rettferdig plan for en kommende periode uten å måtte regne ut alle kombinasjoner manuelt. Et vellykket resultat er at planleggeren får en dekkende plan raskt, forstår hvorfor planen ser ut som den gjør, og kan stole på at harde regler er overholdt.

**[ANTAKELSE]** Demonstrasjonen bruker en generisk, fiktiv arbeidsplass med skiftarbeid (ikke bransjespesifikk), med to enkle kompetansetyper og en liten ansattgruppe. Egne brukerflater for ansatte (rollebasert tilgang) er en mulig utvidelse, ikke del av MVP.

## Success Criteria

Følgende er foreslåtte kriterier som skal testes, ikke oppnådde resultater:

- Enhver generert plan som vises som gyldig, bryter ikke de definerte harde reglene (hviletid, maks vakter på rad, kompetansekrav) i testscenarioene.
- Systemet sier tydelig fra — ikke feiler stille — når bemanningsbehovet ikke kan dekkes innenfor reglene, og viser hvor og hvorfor.
- En testbruker kan lese ut av forklaringen hvorfor planen prioriterte som den gjorde ved en konflikt (f.eks. en ansatt fikk flere helgevakter på rad enn ønskelig, men planen bryter ingen hard regel).
- Ved akutt fravær foreslår systemet minst én kvalifisert erstatter når en finnes, med begrunnelse.
- **[ANTAKELSE]** Måltall for tidsbesparelse/kvalitet sammenlignet med manuell planlegging fastsettes etter en første prøve, tilsvarende tilnærmingen i dagens productbrief.md.

For studiearbeidet skal gruppen også dokumentere BMAD-bruken, egne valg (inkl. solver- og bibliotekvalg) og hvordan KI-generert kode er kvalitetssikret.

## Scope

**Foreslått førsteversjon:** Én liten, fiktiv arbeidsplass med 8–10 ansatte og to enkle kompetansetyper, planhorisont på to uker. Generere en turnusplan som dekker bemanningsbehovet uten å bryte harde regler (min. 11 timers hviletid, maks vakter på rad, kompetansekrav). Enkel kalender/tabellvisning. Frontend i JavaScript, backend i Python med en constraint-solver (se addendum for anbefalt bibliotek).

**Middels nivå (om tid tillater):** Rettferdighetsprinsipper (jevn fordeling av helg/natt/uønskede vakter), ferieønsker/fridag-forespørsler som myke preferanser, konfliktvarsler med forklaring, eksport til PDF/Excel/kalenderformat.

**Avansert (for å strekke ambisjonen):** Håndtering av akutt fravær med forslag til erstatter, KI-generert naturlig-språk-forklaring av planbrudd/avveininger, «what-if»-simulering (ansette/miste ansatt), rollebasert tilgang (leder/ansatt).

**Utenfor scope:** Reelle persondata, integrasjon med HR-/lønnssystemer, produksjonsdrift, støtte for organisasjoner med mange kompetansekrav og hundretalls ansatte (skaleringsutfordringer diskuteres i addendum, løses ikke i denne versjonen).

**Gjenstår å avklare:** Forholdet til dagens avvikshåndteringsscope (se statuslinjen øverst), konkrete rettferdighetsregler og vekting, valg av frontend-rammeverk, og endelig demonstrasjonsdomene.

## Vision

Hvis prototypen viser at solver + forklarende KI-lag gir gyldige og forståelige planer, kan de to retningene (periodegenerering og avvikshåndtering i dagens brief) i praksis utfylle hverandre: samme regelmotor kan både generere en ny periodeplan og håndtere avvik underveis, med KI-laget som felles forklaringsgrensesnitt. Senere kan løsningen utvides til flere kompetansetyper, større ansattgrupper, reelle regelverk per bransje og integrasjon med eksisterende systemer. Prinsippet videreføres: en solver som garanterer korrekthet, og en språkmodell som gjør resultatet forståelig — mennesket tar beslutningen.
