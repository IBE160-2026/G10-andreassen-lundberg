---
title: Forplanner
status: draft
created: 2026-09-07
updated: 2026-09-07
---

# Product Brief: Forplanner

> **Kandidatstatus:** Én av tre prosjektkandidater. Endelig prosjektvalg, MVP-omfang og arbeidsdeling er ikke felles besluttet. Dokumentstatusen gjelder utarbeidingen av briefen, ikke godkjenning av prosjektvalget.

_[Oppdatert 2026-09-07] Bygges 100 % fra bunnen — ikke videreutvikling av Odins eksisterende private AquaTools-kode. Det private verktøyet brukes kun som inspirasjon/referanse for domenemodell og problemforståelse, ikke som kodegrunnlag. Dette fjerner to av de opprinnelig fire blokkerne (se under). Les "Uavklarte blokkere" før resten av dokumentet._

## Uavklarte blokkere og avklaringer før prosjektvalg

1. **Felles prosjektvalg og arbeidsdeling er ikke avklart.** Forplanner er én av tre kandidater. Før et eventuelt valg må gruppen avklare ønsket domene, en konkret MVP og hvordan begge skal bidra. Kandidatbeskrivelsen er ikke en felles godkjenning av prosjektet.
2. ~~Uavklart om eksisterende, privat kode kan brukes som utgangspunkt~~ — **løst 2026-09-07:** ingen privat kode brukes, alt bygges fra bunnen som et nytt IBE160-prosjekt.
3. ~~Uavklart om nok nytt arbeid gjenstår~~ — **løst 2026-09-07:** en 100 % fra bunnen-app har samme type nytt-arbeid-profil som VaktMatch og PantBuddy.
4. ~~Uavklart om produktet trenger en KI-funksjon~~ — **langt på vei løst 2026-09-07:** Odin og Codex har utviklet et konkret forslag («Beskriv status» — fritekst til strukturert utkast), se Solution. Gjenstår kun å bekrefte omfanget (kun tolkning, eller også forklaring/scenarioer) i gruppen.

Felles prosjektvalg, endelig MVP-omfang og arbeidsdeling gjenstår. Punkt 2–4 dokumenterer tidligere avklaringer; KI-funksjonens endelige omfang er fortsatt åpent.

## Executive Summary

Forplanner er en ny fôrlogistikk-app, bygget fra bunnen som IBE160-prosjekt — **inspirert av**, men ikke kodet på toppen av, et eksisterende privat verktøy i Odins AquaTools. Den planlegger fôrbestillinger til et (syntetisk, oppdiktet) oppdrettsanlegg ved å holde silobeholdning, daglig forbruk per merd, leveringer og fôrtype opp mot hverandre, og foreslår bestillinger med mengdetrinn og silofordeling.

Dette gir faglig dybde gjennom datamodellering, dato-/mengdeberegning, validering og algoritmevalg. Eksisterende domeneerfaring gir et utgangspunkt for referansescenarioer; felles forståelse av oppgaven og arbeidsdelingen må avklares før prosjektvalg.

**En fordel ingen av de andre to kandidatene har:** Odin har allerede bygget en fungerende versjon av dette problemet privat, uten BMAD. En fra-bunnen rebuild med BMAD gir dermed et konkret, direkte sammenligningsgrunnlag — samme problem, løst én gang uten strukturert KI-metodikk og én gang med — til refleksjonsrapporten, som eksplisitt skal inneholde en kritisk vurdering av hvordan KI påvirket sluttresultatet (30 % av karakteren). [ANTAKELSE] For at sammenligningen skal være noe mer enn en påstand, bør gruppen kort dokumentere *hvordan* den private versjonen faktisk ble bygget (hvilke verktøy, hvor mye iterasjon, om KI ble brukt i det hele tatt) før den brukes som referansepunkt.

## The Problem

Den som planlegger fôrbestillinger ved et oppdrettsanlegg må sørge for at beholdning og leveranser dekker forbruket over tid, samtidig som fôret havner i riktig silo (kapasitet, reserve, fôrtype). En plan kan se dekket ut i sum, men likevel gi mangel i én enkelt silo; en levering kan dekke behovet, men samtidig overskride kapasiteten. [ANTAKELSE] Akkurat hvilket konkret problem dagens Forplanner *ikke* løser godt nok — og dermed hva som faktisk er verdt å bygge — er ikke bekreftet mot brukere eller kode ennå.

## The Solution — bygget fra bunnen, inspirert av eksisterende funksjonalitet

Den private Forplanner-appen brukes som **inspirasjonsgrunnlag for domenemodellen**, ikke som kode: siloer (beholdning, kapasitet, fôrtype, reserve), merder (dagsforbruk, tidspunkt for stans i fôring), leveringer, og forslag til bestillinger med avrunding og silofordeling, med et skille mellom et forslag og en bestilling registrert som avtalt. Dette er observert i grensesnittet 2026-09-07, ikke hentet fra kildekoden.

[ANTAKELSE] **Mulig kjernefunksjon utover det den private versjonen allerede gjør** (ikke besluttet, velges i gruppen):
- Sammenligne en grunnplan med et scenario der en levering blir forsinket eller forbruket endres, og vise hvilke siloer og dager som får problemer.
- En avgrenset importflyt med eksplisitt feltkobling, feilrapport og sporbarhet til datagrunnlaget.
- Bedre forklaring av *hvorfor* en plan er umulig å gjennomføre, og hvilke endringer som ville gjort den gjennomførbar.

**KI-funksjonen (utviklet av Odin med Codex, 2026-09-07): «Beskriv status».** Brukeren beskriver situasjonen i vanlig språk — f.eks. «Vi har tre siloer med 15 043, 25 000 og 19 200 kg. Merdene bruker 5 435, 4 659 og 5 643 kg per dag. Alle bruker fôrtype 2500. Neste fôrbåt kommer 9. september og deretter ukentlig» — og KI-en gjør det om til et strukturert, redigerbart utkast (silo, beholdning, dagsforbruk, fôrtype, leveringsdato). Mangler noe (f.eks. hvilken dato beholdningen gjelder, eller om dagens fôring er gjennomført), spør KI-en om det i stedet for å gjette.

Samme grense som i VaktMatch og PantBuddy: **KI-en bestemmer ikke selve fôrplanen.** Behov, buffer, leveringsmengder, silokapasitet og risiko for tom/overfylt silo beregnes med faste regler — stabilt, testbart, forklarlig. Forplanner kontrollerer alt KI-en foreslår (avviser ugyldige datoer, negative mengder, beholdning over kapasitet, ukjente siloer), og brukeren godkjenner et redigerbart utkast før noe lagres.

[ANTAKELSE] **Første byggetrinn (bekreftet av Odin som naturlig start):** kun tolkning av fritekst til utkast, med kontroll og godkjenningsvisning. To videre KI-oppgaver — forklare et resultat (f.eks. hvorfor silo 2 blir tom før neste levering) og tolke «hva skjer hvis»-scenarioer — er del av den fulle KI-visjonen, men ikke bekreftet som MVP-scope ennå. Full arkitektur (dataformat, byttbar AI-tilkobling, kontrollregler) i addendum.

## What Makes This Different (fra VaktMatch og PantBuddy, ikke fra et marked)

Forplanner konkurrerer ikke i et marked — den skal ikke sammenlignes mot andre produkter, men mot de to andre kandidatene i denne gruppens beslutning:

- **Fordel:** ekte domenedybde og et problem Odin forstår førstehånds, uten å måtte konstruere en syntetisk fiktiv bedrift fra bunnen (domenet finnes allerede i hodet, selv om koden ikke gjør det). Pluss den unike med/uten-BMAD-sammenligningen nevnt over.
- **Åpent før prosjektvalg:** gruppen må avklare omfang og arbeidsdeling. Oppdrett er et spesialisert domene, så kjerneproblemet bør forklares med et enkelt lager- og forbruksscenario for lesere uten oppdrettsbakgrunn.

## Who This Serves

**Primær:** en fôrplanlegger/driftsansvarlig ved et oppdrettsanlegg. [ANTAKELSE] Faktisk forbedringsbehov hos en reell bruker er ikke bekreftet — dette bygger på Odins egen domeneerfaring, ikke brukerintervjuer.

## Success Criteria

- **Akademisk:** proposal godkjent av faglærer etter at gruppen har valgt prosjekt og avklart MVP og arbeidsdeling.
- **Produkt:** en fra-bunnen bygget fôrplanleggingsapp med tester, brukertest og dokumentert KI-bruk og kvalitetssikring.
- **Refleksjon:** en kort, konkret dokumentasjon av hvordan den private originalversjonen ble bygget (verktøy, iterasjon, KI-bruk eller fravær av det), som gjør med/uten-BMAD-sammenligningen i refleksjonsrapporten til noe mer enn en påstand.

## Scope

**Før scope låses:** gruppen velger én av kjernefunksjonene over og avtaler arbeidsdeling. Begge skal kunne forklare kjerneproblemet og egne bidrag. Funksjonsparitet med den private appen er ikke et mål.

**Sannsynlig inn i MVP:**
- Én fiktiv, syntetisk oppdrettslokalitet (samme prinsipp som VaktMatch og PantBuddy) — ikke ekte driftsdata fra AquaTools.
- Grunnleggende datamodell (siloer, merder, leveranser, bestillingsforslag), bygget fra bunnen.
- **KI-funksjon:** «Beskriv status» — fritekst til strukturert, kontrollert og godkjennbart utkast (se Solution). Dette er det bekreftede første byggetrinnet.
- Én av de opprinnelig skisserte kjernefunksjonene (scenario-sammenligning, avgrenset import, eller bedre infeasibility-forklaring) — ikke alle tre, og ikke nødvendigvis samme som KI-forklaring/scenario-tolkning (som er egne, uavklarte KI-oppgaver, se Uavklarte blokkere).
- Relevante automatiserte tester (håndregnet fasit, grensetilfeller, samt at KI-tolkningen korrekt gjenkjenner/avviser eksemplene i addendum) og minst én brukertest.
- Kort dokumentasjon av hvordan den private originalversjonen ble bygget, som grunnlag for med/uten-BMAD-sammenligningen i refleksjonsrapporten.

**Bevisst utenfor MVP:**
- Å kopiere hele den private appens funksjonsbredde — målet er ett solid, testbart kjerneproblem, ikke funksjonsparitet.
- Ekte driftsdata eller tilgang til AquaTools-produksjonssystemet.
- Alt relatert til Stingray Status eller andre AquaTools-verktøy — helt urelatert til denne kandidaten.

## Vision

Hvis dette velges og blokker 1 løses: den nye Forplanner-appen kunne på sikt bygges videre med flere av de samme funksjonsområdene som den private originalen dekker — men det er langt fram, og ingen grunn til å love det nå. Den mest interessante videreføringen er trolig ikke flere funksjoner, men en ferdigskrevet med/uten-BMAD-sammenligning som konkret case i refleksjonsrapporten.
