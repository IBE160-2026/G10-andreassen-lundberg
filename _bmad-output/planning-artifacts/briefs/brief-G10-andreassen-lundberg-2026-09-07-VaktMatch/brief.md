---
title: VaktMatch
status: complete
created: 2026-09-07
updated: 2026-09-07
---

# Product Brief: VaktMatch

> **Kandidatstatus:** Én av tre prosjektkandidater. Endelig prosjektvalg, MVP-omfang og arbeidsdeling er ikke felles besluttet. Dokumentstatusen gjelder utarbeidingen av briefen, ikke godkjenning av prosjektvalget.

_[ANTAKELSE] Arbeidstittel — ikke endelig bekreftet av gruppen. Alternativer under vurdering: Bemanningsassistent, VaktValg, ShiftPilot._

## Executive Summary

VaktMatch er en moderne, responsiv webapp — tilgjengelig fra nettleser på telefon, nettbrett eller PC, ingen installasjon nødvendig. Samtidig er den en KI-støttet beslutningsassistent for mellomledere som plutselig står med et udekket skift, typisk fordi en ansatt melder seg syk. I stedet for at lederen selv må huske alle regler og ringe rundt, viser systemet et lite sett med konkrete handlingsalternativer (intern omfordeling, ekstravakt/overtid, eller ekstern vikar), hver med tydelig forklaring på hva alternativet dekker, hva det koster i hviletid/overtid/rettferdighet, og hva som eventuelt mangler. Lederen velger selv — systemet anbefaler og forklarer, det bestemmer ikke.

Kjernen er en bevisst arbeidsdeling: deterministisk kode håndhever de reglene som ikke kan brytes (hviletid, kompetansekrav, tidskollisjoner), mens språkmodellen tolker lederens fritekstbehov og formulerer forklaringer et menneske faktisk forstår. Ingen av delene overtar den andres jobb.

Produktet bygges som et studieprosjekt (IBE160, Høgskolen i Molde), men er bevisst formet slik at MVP-avgrensningen ikke er en blindvei: samme datamodell og regelmotor kan i prinsippet utvides til større datamengder og sterkere infrastruktur uten en produktredesign.

## The Problem

Når en ansatt melder seg syk kort tid før en vakt, må en mellomleder på kort tid finne ut hvem som faktisk kan dekke skiftet — uten å bryte arbeidsmiljølovens hviletidsregler, uten å overse kompetansekrav, og helst uten å alltid velge de samme personene til ekstravakter. I dag skjer dette som regel manuelt: telefonrunder, hukommelse og magefølelse, med lav sporbarhet for hvorfor et valg ble tatt eller hvorfor et alternativ ble avvist.

Konsekvensen er dobbel: beslutningen tar unødig lang tid under tidspress, og den er vanskelig å etterprøve eller forklare i ettertid — både overfor den ansatte som ikke ble valgt, og overfor krav til dokumentasjon.

## The Solution

VaktMatch består av to deler som deler samme regelmotor: et lite **generert ukesgrunnlag** (en gyldig starturnus for den fiktive arbeidsplassen, satt sammen av deterministisk kode ut fra ansatte og bemanningsbehov, uten å bryte harde regler) og selve **avviks-flyten**, som er hovedproduktet og det som demonstreres mest. Å generere grunnlaget selv, i stedet for å anta det som statisk input, gjør at samme regelmotor kan gjenbrukes to steder og at demonstrasjonen ikke hviler på et "fasit"-datasett laget for hånd.

VaktMatch tar imot et udekket skift (sted, tidspunkt, rolle/kompetansekrav) og viser lederen et lite antall relevante alternativer, rangert og forklart:

1. **Intern omfordeling** — flytte en allerede ansatt som fyller kravene.
2. **Ekstravakt/overtid** — tilby en ekstra vakt til noen som er tilgjengelig.
3. **Ekstern vikar** — hente inn noen som allerede er formelt ansatt hos et bemanningsbyrå med kontrakt og stillingsprosent, og som er forhåndsgodkjent i nettverket. [ANTAKELSE-oppdatert] Dette er ikke en åpen "gig"-markedsplass — norsk regelverk krever at bemanningsforetak gir reell ansettelseskontrakt med stillingsprosent, ikke løs tilknytning uten kontrakt.
4. **Ingen gyldig løsning** — systemet sier tydelig fra om et absolutt krav gjør situasjonen uløselig med dagens grunnlag, i stedet for å late som et alternativ finnes.

Hvert alternativ vises med: om kompetansekravet er dekket, hviletid før/etter vakten, beregnet arbeidstid/overtid, konsekvens for andre vakter, rettferdighetsbelastning (har denne personen fått uforholdsmessig mange ekstravakter), og eventuelle manglende opplysninger. Språkmodellen oppsummerer forskjellene i klart språk og kan svare på avgrensede "hva om"-spørsmål — men beregner ikke selv reglene, og foreslår ikke noe den strukturerte kontrollen ikke kan bekrefte.

Lederen godkjenner, avviser eller justerer. VaktMatch tildeler aldri en vakt på egen hånd.

## What Makes This Different

VaktMatch konkurrerer ikke med etablerte WFM/HR-systemer som Simployer, Quinyx og 4Human — de eier allerede fraværsregistrering, vaktplaner og compliance-oppfølging hos mange bedrifter, og å late som det problemet er uløst ville vært uærlig. En rask konkurrentsjekk (2026-09-07, se [research.md](../../research/competitive-simployer-quinyx-4human-akutt-bemannings-2026-09-07/research.md)) bekrefter derimot at ingen av de tre i dag dokumenterer det konkrete VaktMatch gjør: et lite sett **rangerte, forklarte** alternativer ved et akutt dekningsgap, hver annotert med kompetansematch, hviletidsoverholdelse, beregnet overtid og konsekvens for andre vakter. Alle tre er dokumentert på nivået «registrer fravær → varsle leder → la leder manuelt finne/tildele erstatning» — ikke en forklarende, regelsjekket sammenligning på beslutningsøyeblikket. [ANTAKELSE-nedgradert til medium sikkerhet, ikke høy] Dette er et raskt søk i offentlig dokumentasjon; Simployers «Finn vikar»-funksjon kunne ikke inspiseres i detalj, og salgs-gatede AI-funksjoner hos alle tre er ikke undersøkt.

Utover denne markedsposisjonen er styrken at det strukturerte regelverket (hviletid, kompetanse, kollisjoner) håndheves av kode som kan testes og etterprøves, mens språkmodellen kun brukes der den faktisk har verdi: å tolke et ustrukturert behov og forklare et resultat i naturlig språk. Rent KI-generert turnusforslag uten en deterministisk kjerne ble vurdert og forkastet tidlig — en språkmodell kan ikke pålitelig garantere at harde regler aldri brytes.

Den tydeligste differensieringen mot en generell turnusgenerator handler fortsatt om omfang: VaktMatch løser ett akutt avvik om gangen med forklaring (pluss et generert ukesgrunnlag som utgangspunkt), ikke en hel periodeplan med myke preferanser. Dette er et bevisst MVP-valg, ikke en påstand om at fullstendig turnusgenerering er teknisk umulig.

## Who This Serves

**Primær bruker:** en mellomleder med personalansvar (f.eks. lagerleder/skiftleder) som må håndtere et akutt bemanningsavvik raskt, og som ønsker et forslag den kan stå inne for — ikke en svart boks.

**Sekundær "bruker" (for demonstrasjon):** et lite, syntetisk sett ansatte og forhåndsgodkjente vikarer i en fiktiv lager-/logistikkbedrift. [ANTAKELSE] Lager/logistikk er valgt som domene fremfor helse eller barnehage nettopp fordi det har færre lovpålagte særkrav, og gjør det lettere å holde studieprototypen avgrenset uten å miste poenget med matchingen.

## Success Criteria

Siden dette er et studieprosjekt (IBE160), er "suksess" todelt:

- **Akademisk:** proposal godkjent av faglærer, og en fungerende MVP som tydelig demonstrerer KI-bruk pluss kvalitetssikring av KI-generert kode (jf. kursets 70/30-vekting mellom prosjektkode og refleksjonsrapport).
- **Produkt:** en leder som får et konkret bemanningsavvik presentert, kan i praksis se relevante alternativer, forstå hvorfor et alternativ er utelukket, og ta en beslutning raskere og mer sporbart enn ved manuell håndtering — demonstrert gjennom scenarioet i MVP-en, ikke i produksjon.

## Scope

**Inn i MVP:**
- Én fiktiv arbeidsplass, 8–10 interne ansatte, noen forhåndsgodkjente eksterne vikarer (ansatt hos bemanningsbyrå med kontrakt/stillingsprosent).
- Et **generert** ukesgrunnlag — deterministisk kode setter sammen en gyldig starturnus fra ansatte og bemanningsbehov, uten å bryte harde regler (Stians "Minimum"-nivå), vist som tabell/kalender.
- Ett sykefraværsscenario som trigger et udekket skift i dette grunnlaget.
- 3–5 harde regler (hviletid, kompetanse, tidskollisjon) håndhevet deterministisk — samme regelsett brukes både til generering og til avviks-matching.
- Én side som viser og sammenligner handlingsalternativene ved avviket, med forklaring fra språkmodellen. Dette er hovedflyten som demonstreres mest.

**Bevisst utenfor MVP** (dokumentert som veivalg, ikke som teknisk umulig):
- Middels/avansert turnusgenerering (helg/natt-fordeling, myke preferanser som "ikke fredager", eksport, "hva om"-scenarioer på hele perioden) — grunnlaget genereres, men periodeplanlegging utover det er visjon.
- En åpen/offentlig vikarmarkedsplass — nettverket er lukket og forhåndsgodkjent i MVP-en.
- Skalering til reelle datamengder, produksjonssikkerhet og drift utover det som er gratis/kontrollerbart innenfor et studieprosjekt — se [addendum.md](addendum.md) for hva dette ville krevd.
- Enhver påstand om at et forslag "er lovlig" — kun kontrollert mot et navngitt, versjonert scenarioregelsett.

## Vision

MVP-en genererer allerede grunnlaget med samme regelmotor som styrer avviks-matchingen — neste naturlige steg er å bygge ut denne generatoren til Stians middels/avanserte nivå: fordeling av helg/natt/uønskede vakter, myke preferanser, eksport og "hva om"-scenarioer over en hel periode, ikke bare ett grunnlag. Det udekkede skiftet som i dag løses mot et lite forhåndsgodkjent vikarnettverk kan på sikt sendes videre til et større nettverk av bemanningsbyråer. Det samme produktet kan også løftes fra studieprototype til noe nærmere reell drift ved å koble til betalte backend-tjenester, mer KI-kapasitet og ordentlig tilgangsstyring — uten at kjernemodellen (regelmotor + KI-forklaring + menneske bestemmer) må endres.

[ANTAKELSE — langsiktig, ikke MVP] På lengre sikt kan VaktMatch bli et leverandøragnostisk forklaringslag over flere eksisterende WFM/HR-systemer (Simployer, Quinyx, 4Human m.fl.) i stedet for å stå alene — samme mønster som Akva og Pisada bruker i oppdrettsnæringen, der ett lag kobler seg over flere ulike flåtestyringssystemer som i praksis gjør det samme med forskjellig grensesnitt. Konkurrentsjekken (over) støtter at hullet finnes; ekte integrasjon mot navngitte leverandører krever derimot partner-API-tilgang og forretningsavtaler gruppen ikke har som studentprosjekt, og teamet mangler i dag førstehåndskunnskap om hvordan disse systemene faktisk oppleves av en mellomleder. Dette er derfor bevisst holdt som visjon, ikke MVP.
