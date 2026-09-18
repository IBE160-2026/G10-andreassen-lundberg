# Addendum: VaktMatch – Turnusgenerator (alternativt forslag)

Dette dokumentet bevarer utdypende teknisk grunnlag for turnusgenerator-briefen, hentet fra Stians opprinnelige forslag og en påfølgende teknisk vurdering i samtalen. Det er bakgrunnsmateriale for videre BMAD-arbeid (arkitektur, PRD) — ikke del av selve briefen, og ikke en beslutning tatt av gruppen.

## Vurderte tekniske strategier

**1. Regelbasert/optimaliseringsbasert kjerne + KI på toppen (anbefalt, lagt til grunn i briefen)**

Et constraint-solver-bibliotek løser selve turnusproblemet, som er NP-hardt. Språkmodellen tolker fritekst-input og genererer forklaringer/forslag ved konflikter. Gir en robust, korrekt kjerne og en tydelig historie om hvor og hvorfor KI brukes.

**2. Ren KI-basert generering (vurdert og lagt bort)**

La en språkmodell generere hele planen direkte fra reglene. Enklere å bygge, men risikerer brudd på harde regler siden språkmodeller ikke er pålitelige på eksakt kombinatorisk optimalisering. Kan fungere for et svært lite scope, men er risikabelt hvis gruppen vil vise at løsningen faktisk er korrekt — særlig i en rapport som skal vurderes.

## Bibliotek- og algoritmevalg

**Anbefaling: Google OR-Tools CP-SAT (Python)**

- Har et ferdig referanseeksempel for skiftplanlegging (`shift_scheduling_sat.py`) som ligner problemet direkte.
- Harde regler (hviletid, maks vakter på rad, kompetansekrav) uttrykkes som constraints — solveren garanterer at en funnet løsning overholder dem.
- Myke regler (rettferdighet, ferieønsker) legges inn som vektede straffeledd i objektivfunksjonen.
- Ved 8–10 ansatte og to ukers horisont løses problemet på under et sekund; ingen egen heuristikk nødvendig.
- Gir en sterk historie for rapporten: en anerkjent solver er brukt, ikke en hjemmesnekret heuristikk som selv må bevises riktig.

**Alternativ vurdert: håndskrevet constraint-checker + backtracking**

Fungerer på dette lille omfanget, men gruppen må selv bevise at heuristikken finner en gyldig løsning når en finnes — svakere garanti for mer arbeid. Eneste fordel er å unngå et andre språk i stacken.

**Arkitekturkonsekvens av stack-valget (frontend JavaScript, backend Python):** OR-Tools har offisielle bindings for Python, C++, Java og .NET — ikke Node.js. Dette løses naturlig av den valgte stacken: Python-backenden eier hele regelmotoren og eksponerer et REST-endepunkt som JavaScript-frontenden kaller.

## Datamodell (forslag)

- **Ansatt:** navn, stillingsprosent, kompetanser, tilgjengelighet, ferieønsker, historikk (for rettferdighet over tid)
- **Skift:** dato, starttid/sluttid, krav til kompetanse, antall personer
- **Regelsett:** hviletid, maks vakter/uke, helgekvote, kompetansekrav per skift
- **Turnusplan:** liste av tildelinger (ansatt ↔ skift), status (utkast/godkjent), avvikslogg

## Utfordringer å reflektere rundt i rapporten

- **Uløselig behov:** Hva skjer når for få ansatte dekker behovet? Systemet må si tydelig fra, ikke feile stille eller levere en ugyldig plan uten varsel.
- **Rettferdighet er subjektivt:** Gruppen må selv definere og vekte hva som teller som «rettferdig» fordeling (f.eks. hvordan helg/natt/uønskede vakter veies mot hverandre), og dokumentere valget i rapporten.
- **Skalering:** En liten arbeidsplass (5 ansatte) er beregningsmessig enkel. En stor organisasjon (100 ansatte, mange kompetansekrav) er langt tyngre. Dette prosjektet skalerer ikke dit uten videre arbeid, og det bør sies eksplisitt i rapporten fremfor å love mer enn scope dekker.
- **Etikk/personvern:** Turnusdata kan avsløre sensitiv informasjon (sykdom, permisjoner). Bør diskuteres i rapporten selv med syntetiske data, siden det er en egenskap ved domenet, ikke bare ved datasettet.

## Foreslått avgrensning hvis tiden er knapp

Én liten, fiktiv arbeidsplass, 8–10 ansatte, 2 kompetansetyper, 2 ukers planhorisont. Viser hele konseptet (optimalisering + KI-forklaringer + avvikshåndtering) uten at kompleksitet i seg selv blir hovedutfordringen.
