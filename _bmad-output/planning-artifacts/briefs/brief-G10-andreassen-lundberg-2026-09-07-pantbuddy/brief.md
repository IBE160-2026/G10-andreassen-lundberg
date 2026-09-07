---
title: PantBuddy
status: complete
created: 2026-09-07
updated: 2026-09-07
---

# Product Brief: PantBuddy

> **Kandidatstatus:** Én av tre prosjektkandidater. Endelig prosjektvalg, MVP-omfang og arbeidsdeling er ikke felles besluttet. Dokumentstatusen gjelder utarbeidingen av briefen, ikke godkjenning av prosjektvalget.

## Executive Summary

PantBuddy er en responsiv webapp (mobil, ingen app store) som kobler sammen tre typer lokale brukere rundt norsk pant: folk som har flasker/bokser de ikke gidder å pante selv, privatpersoner som gjerne henter og panter mot å beholde verdien, og lag/foreninger som samler pant til et formål. Giveren blir kvitt rot, mottakeren får verdien, og flere flasker/bokser blir faktisk gjenvunnet i stedet for å bli stående.

Konseptet er ikke nytt — et raskt landskapssøk (se addendum) fant flere norske og internasjonale forløpere som hver dekker deler av dette. Det ingen av dem samler, er alle tre rollene pluss profiler, avtalt henting og gjensidig tillitsvurdering i én app. PantBuddy sin plass er der: å pakke sammen et spredt landskap, ikke å oppfinne et nytt konsept.

## The Problem

Mange har flasker og bokser liggende de aldri panter — festglade unge i delt husholdning er ett tydelig eksempel: pant hoper seg opp etter helg på helg, men å bære sekker til en automat og stå og mate dem inn oppleves som lite verdt tiden. Pantelotteriet gjør det enkelt å gi bort verdien til Røde Kors direkte i automaten, men fjerner samtidig muligheten for at et annet menneske i nærmiljøet får den ekstra inntekten.

Samtidig finnes det folk som gjerne vil ha den ekstra inntekten, og lag/foreninger som årlig samler pant dør-til-dør som dugnad — en arbeidskrevende, lite målrettet metode. Disse gruppene har i dag ingen enkel, lokal måte å finne hverandre på som også bygger tillit over tid.

## The Solution

En giver oppretter en enkel annonse (omtrentlig mengde, omtrentlig lokasjon, ledig hentevindu — ikke eksakt adresse, av sikkerhetshensyn før avtale er bekreftet). Innsamlere (privatpersoner eller lag/foreninger) ser annonser i nærheten, filtrert på rolle, og tar kontakt for å avtale henting. Etter gjennomført henting gir begge parter hverandre en enkel, gjensidig vurdering (kudos), som bygger en synlig tillitshistorikk — samme mønster som Finn.no Torget og Buy Nothing-grupper allerede bruker, ikke noe PantBuddy må finne opp selv (se addendum).

**KI-funksjonen: «Oppsummer min innsats».** En knapp — inspirert av Strava sine AI-oppsummeringer — som gir en kort, personlig oppsummering av det brukeren har bidratt med, på tre nivåer:

- **Én panterunde:** hva som ble hentet, hvor mange avtaler som ble gjennomført, og registrert pantebeløp.
- **Samlet innsats over tid:** utvikling, totalt innsamlet beløp, bidrag til ulike formål.
- **Lagets dugnad:** hva laget/foreningen fikk til sammen, og fremdrift mot et sparemål.

Eksempel: «Denne måneden har du gjennomført fire hentinger og bidratt med anslagsvis 620 kroner til håndballaget. Det bringer lagets anslåtte total til 3 100 kroner — cirka 62 % av målet til sommerturneringen.»

Arbeidsdelingen følger samme mønster som VaktMatch: vanlig kode regner ut tallene, KI-en formulerer en kort, forståelig oppsummering av dem — en avgrenset oppgave (finne sammenhenger, formulere dem), ikke å dikte opp resultater. Datagrunnlaget i MVP er giverens **selvrapporterte anslag** ved annonseopprettelse — ikke fritekst, men et enkelt valg av standard beholder (f.eks. «butikkpose», «bigbag», «sekk»), som vanlig kode omregner til et grovt mengde-/verdianslag ut fra kjente gjennomsnittstall per beholdertype — enklere å bygge og mer konsistent enn fritekst, men fortsatt et anslag, ikke en bekreftet sum. [ANTAKELSE] Nøyaktigheten i denne omregningen er ikke MVP-ens største prioritet — å kreve at innsamleren registrerer nøyaktig resultat etter henting ble vurdert, men er i seg selv et friksjonspunkt, og er derfor ikke et MVP-krav.

**Ærlighetsgrense (samme mønster som «aldri påstå lovlig» og «aldri dikte klimatall»):** siden tallene er anslag, ikke bekreftede beløp, skal KI-en og resten av grensesnittet konsekvent merke dem som anslått («anslagsvis», «cirka»), aldri fremstille dem som eksakte — spesielt viktig for lagets dugnad-total, siden den til syvende og sist handler om ekte penger og et reelt sparemål.

[ANTAKELSE] Klimaeffekt nevnes i den opprinnelige pitchen, men holdes bevisst utenfor MVP med mindre et dokumentert beregningsgrunnlag finnes — antall innleverte enheter og kroner er lettere å vise presist. Hvis et klimaestimat likevel tas med, skal det merkes tydelig som estimat med kildehenvisning; KI-en skal aldri dikte CO₂-tall eller anta at panten ellers ville havnet i naturen.

**Ingen verdi eller penger flyttes i appen selv.** Basert på hvordan norsk pant faktisk fungerer (se addendum): en pantelapp er butikk-/kjedebundet, så appen oppfordrer til å gi bort ugjenløste flasker/bokser, ikke ferdig-pantede kvitteringer — da panter mottakeren selv, og PantBuddy trenger aldri håndtere penger eller verdioverføring.

## What Makes This Different

Pantes.no dekker lag/forening-siden godt (kart, delbar pantelapp, bulk-innløsning), men har verken profiler, vurderinger eller avtalt henting. Pfandgeben i Tyskland dekker privat-til-privat-siden godt, men er ikke lokalisert til Norge og har ingen lag/forening-rolle. Pantelotteriet løser «gi bort til godt formål» på automat-nivå, ikke person-til-person. **Ingen av dem samler alle tre rollene i én lokal, tillitsbygget flate.** Det er PantBuddys reelle, men beskjedne, differensiering — en pakking av et spredt landskap, ikke et nytt konsept. Dette bør sies rett ut i en eventuell proposal, ikke pyntes bort.

«Oppsummer min innsats» styrker denne differensieringen ytterligere: ingen av forbildene (Pantes.no, Pfandgeben, Pant-appen — en iOS-app der giveren velger mottaker av panten) ble funnet å tilby en personlig eller lag-basert innsatsoppsummering — det er ikke bare en KI-pynt, men en funksjon ingen av de undersøkte konkurrentene har.

**Presisering etter funn hos systemeieren selv (2026-09-07):** Infinitum, som eier det norske pantesystemet, tilbyr allerede gratis henting av pantesekker for bedrifter, lag og foreninger via «Bestill pantehenting», pluss en håndteringsgodtgjørelse (5 øre per boks, 10 øre per flaske) i tillegg til selve panten. Dette kunne sett ut som direkte konkurranse mot PantBuddys lag/forening-side — men Infinitums egen tjenestebeskrivelse forutsetter at laget allerede har samlet tomgodset og fylt sekkene («Ta imot tomgodset fra kunden og betal ut panten. Saml tomgodset i pantesekker og forsegl», deretter «Bestill gratis henting»). Infinitum løser altså *innløsningssteget* — henting og utbetaling av allerede fylte sekker — ikke *oppdagelsessteget*: å finne spredte, individuelle givere i nærmiljøet og få dem til å levere fra seg pant i utgangspunktet. Det siste er fortsatt det PantBuddy gjør. De to er komplementære, ikke konkurrenter: et lag kan bruke PantBuddy til å finne givere og avtale hentinger, og deretter bruke Infinitums gratis hentetjeneste til selve innløsningen i stedet for å bære sekker til en butikk selv.

## Who This Serves

**Primær (ankerpersona):** en ung, sosial enslig person som har mye pant liggende, men ikke prioriterer tiden det tar å levere den selv. Et konstruert eksempel er en 24-åring som ofte arrangerer fest. Personaen beskriver en brukssituasjon, ikke et gruppemedlem.

**Sekundære:** privatpersoner som ønsker litt ekstra inntekt ved å hente og pante for andre; lag/foreninger (idrettslag, korps, speidergrupper) som i dag samler pant dør-til-dør som dugnad og ønsker en mer målrettet metode.

## Success Criteria

Todelt, som for VaktMatch, siden dette også er et IBE160-kandidatprosjekt:

- **Akademisk:** proposal godkjent, MVP som tydelig demonstrerer KI-bruk og kvalitetssikret KI-generert kode.
- **Produkt:** en giver kan opprette en annonse og få den hentet av en relevant mottaker innenfor demoscenarioet; en mottaker kan finne og avtale henting av relevant pant i nærheten; begge kan gi og se en tillitsvurdering etterpå.

## Scope

**Inn i MVP:**
- Ekte, fullt fungerende webapp — ikke bare en syntetisk demo — med tre profiltyper (giver, privat innsamler, lag/forening). Se «Kjent risiko» under for hvorfor dette likevel ikke løser kaldstart-problemet.
- Opprette og bla i annonser (mengde, omtrentlig lokasjon, hentevindu).
- Avtale henting mellom to parter.
- Gjensidig, enkel kudos-vurdering etter henting.
- Giveren oppgir et selvrapportert anslag (mengde) ved annonseopprettelse — datagrunnlaget «Oppsummer min innsats» bygger på i MVP.
- **KI-funksjon:** «Oppsummer min innsats» — kort KI-generert oppsummering (panterunde / samlet innsats / lagdugnad) bygget på anslåtte tall beregnet av vanlig kode, konsekvent merket som anslag, se over.
- En generert/seedet demo-versjon med mange syntetiske brukere, for å vise hvordan appen oppfører seg med reell trafikk og aktivitet — se «Kjent risiko».

**Bevisst utenfor MVP:**
- Enhver betaling eller verdioverføring i appen — bevisst valg basert på hvordan pantelapper faktisk fungerer, ikke bare tidsmangel.
- Ekte appstore-app.
- Hard identitetsverifisering eller forsikring ved henting — kjent åpent spørsmål også hos forbildene (Finn, Buy Nothing), ikke unikt for PantBuddy.
- Klimaeffekt-tall, med mindre et dokumentert beregningsgrunnlag finnes før PRD — se KI-funksjonen over.
- En reell, levende brukerbase i produksjon — se «Kjent risiko».

## Kjent risiko: kaldstart

Verdien i PantBuddy avhenger av at nok givere og mottakere faktisk er aktive i samme nærområde samtidig — det klassiske tosidede markedsplassproblemet. VaktMatch unngår dette ved å operere innenfor én fiktiv bedrift; PantBuddy kan ikke unngå det på samme måte, fordi hele poenget er et ekte lokalt nettverk.

[ANTAKELSE — bekreftet retning, detaljer ikke låst] Kurset stiller ikke krav om en reell, levende brukerbase, så MVP-en bygges som en ekte, fullt fungerende app, supplert med en generert/seedet demo-versjon med mange syntetiske brukere for å vise hvordan den oppfører seg i bruk. Dette beviser mekanikken og lar dere demonstrere realistisk skala — det løser derimot ikke den reelle kaldstart-risikoen en faktisk lansering ville hatt. Det bør stå eksplisitt i brief/PRD/refleksjonsrapport at dette er en bevisst avgrensning av hva kurset krever, ikke en påstand om at kaldstart-problemet er løst.

## Vision

To naturlige neste steg kan lukke gapet mellom anslag og bekreftet resultat: la giveren laste opp et bilde av panten ved annonseopprettelse, som kan analyseres for et mer treffsikkert automatisk anslag; og/eller la innsamleren valgfritt registrere eller fotografere det faktiske resultatet etter henting. Begge er bevisst utelatt fra MVP fordi de introduserer egne friksjonspunkter, men de er den naturlige veien til å kunne love «bekreftet», ikke bare «anslått».

[ANTAKELSE] Et konkret, lavthengende neste steg: la lag/foreninger som bruker PantBuddy få en direkte lenke/påminnelse om å bestille Infinitums gratis hentetjeneste når sekkene deres er fulle, i stedet for å finne på en egen innløsningsløsning — PantBuddy fokuserer på oppdagelse/matching, Infinitum tar innløsningen.

Utover det kunne PantBuddy på sikt vokse til flere lokalområder, få en enkel «miljøregnskap»-visning (hvor mange flasker/bokser som er gjenvunnet via appen, med kildemerket beregningsgrunnlag), og samarbeide med lag/foreninger eller kommuner om organiserte innsamlingsdager. Prinsippet «ingen verdioverføring i appen» kan holdes fast selv i en større versjon, siden det er det som holder produktet enkelt og unngår betalings-/regulatorisk kompleksitet.
