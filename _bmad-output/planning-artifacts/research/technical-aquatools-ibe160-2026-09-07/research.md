---
title: AquaTools som prosjekt i IBE160
type: technical
topic: aquatools-ibe160
decision: Vurdere Forplanner og alternative prosjektkandidater
source: Direkte UI-observasjoner og eksplisitt merket prosjektkontekst
status: complete
verified_claims: 0
unverified_claims: 7
preset: quick
validation: normal
created: 2026-09-07
updated: 2026-09-07
---

# AquaTools som prosjekt i IBE160

**Anbefaling: behold fôrplanleggeren som første kandidat. Den har etter min vurdering tilstrekkelig programmeringsfaglig dybde. Det uavklarte er om det gjenstår nok nytt arbeid for gruppen, og hvordan eksisterende kode kan brukes i emnet.**

Grensesnittet viser lager, tidsavhengig forbruk, leveringer, silokapasitet og bestillingsforslag. Det gir et konkret grunnlag for datamodellering, regler, validering og tester. Flere av disse funksjonene finnes allerede; de kan derfor ikke uten videre presenteres som gruppens nye leveranse. [1]

Vurderingen bygger på besøk i alle sju verktøy, men uten kildekodegjennomgang eller beregningstester. Stingray-funksjonene bak innlogging er ikke undersøkt. Dette er en anbefaling om kandidat, ikke bekreftelse på at emnets formelle krav er oppfylt.

## Emneramme og gruppesamarbeid

Gruppens [tidligere addendum](../../briefs/brief-G10-andreassen-lundberg-2026-09-07/addendum.md) oppgir 70 prosent kode/funksjonalitet, 30 prosent refleksjon, BMAD som metode og avklaring med faglærer. Dette er tidligere registrert prosjektkontekst. Den aktuelle oppgaveteksten fra Canvas/Teams er ikke kontrollert i denne vurderingen; nettsøket ga ingen anvendelig aktuell primærkilde.

Et tidligere Stingray/AquaTools-spor ble lagt bort. Et eventuelt valg av Forplanner krever en ny, felles avklaring av omfang og arbeidsdeling. Fôrplanlegging kan forklares som lager og etterspørsel over tid. En mulig arbeidsdeling er regler og referanseberegninger på den ene siden, og import, brukerflyt og lagring på den andre, med felles gjennomgang av tester og kode. Dette er et forslag, ikke en avtalt arbeidsdeling.

## Hva som gir Forplanner faglig dybde

| Område | Synlig grunnlag | Mulig dokumentasjon av læring |
| --- | --- | --- |
| Datamodell | Siloer, merder, leveringer og forbindelser mellom dem | Forklare relasjoner og konsistensregler |
| Beregninger | Forbruk per dag og dato for stans i fôring | Håndregnede fasiter og grensetester for datoer |
| Begrensninger | Kapasitet, reserve og fôrtype | Teste planer som har nok totalfôr, men feil fordeling |
| Forslag | Mengdetrinn og justerbare/låste bestillinger | Begrunne algoritmevalg og teste umulige planer |
| Brukerflyt | Inndata, oversikt og forhåndsvisning | Brukertester og sporbarhet fra behov til endring |

Grunnlaget i tabellen er observert i grensesnittet; læringsaktivitetene er mine forslag. Ingen korrekthet i beregningsmotoren er bekreftet. [1]

Et enkelt referansescenario er 10 000 kg på lager, 2 000 kg daglig forbruk og en levering på 5 000 kg. Testen må gjøre eksplisitt om levering skjer før eller etter dagens fôring. Deretter kan samme scenario utvides med to siloer, ulik kapasitet og forskjellig fôrtype. Dette er konstruerte testdata, ikke observerte driftsdata.

## Sammenligning med de andre verktøyene

Dette er en kvalitativ faglig vurdering, ikke en objektiv rangering. Ingen kandidat er vurdert mot bekreftede regler for gjenbruk av tidligere kode.

| Kandidat | Observert grunnlag | Min vurdering som prosjekt |
| --- | --- | --- |
| Forplanner [1] | Sammenhengende plan med lager, forbruk og leveringer | Første kandidat: tydelig problem og mange testbare regler. Nytt arbeid må avgrenses. |
| Lokalitetspanel [2] | Kart, ukedata, sortering og rapporteringsdekning | Sterkt alternativ hvis begge foretrekker data og visualisering. Datakilder og feiltilstander må undersøkes. |
| Døgngrader [3] | Flere temperaturkilder, filimport og kalender | Mer substans enn en enkel kalkulator. Egnet hvis prosjektet handler om datakvalitet og sporbare beregninger. |
| Fôrkalkulatoren [4] | Forbruksgrunnlag, import og avrundet bestilling | Mulig mindre prosjekt eller avgrenset datainngang til Forplanner. Betydelig funksjonalitet finnes allerede. |
| Dødelighetsforløp [5] | Observasjoner, tidsfordeling og tydelig estimatmerking | Interessant metodeprosjekt, men det blir vanskeligere å validere en rekonstruksjon når faktisk forløp er ukjent. |
| Slangetrykk [6] | Hurtigberegning og organisering av fôringslinjer | Ser smalest ut som selvstendig prosjekt ut fra besøkt hovedflate. Flere funksjoner kan finnes bak valg som ikke ble åpnet. |
| Stingray Status [7] | Innloggingskrav og inngang til eksportfilanalyse | Uavklart teknisk omfang. Ikke anbefalt foran Forplanner uten innsyn, tilgjengelige testdata og avklart interesse hos begge. |

Lokalitetspanel er nærmeste alternativ hvis arbeidsdeling rundt fôrplanlegging ikke fungerer. Døgngrader er et mulig mer avgrenset alternativ. Å ta med flere verktøy vil øke bredden, men gir ikke automatisk mer nytt eller bedre dokumenterbart arbeid.

## Forslag til avgrensning

Mulig prosjektformulering: **Videreutvikle og kvalitetssikre en fôrlogistikkplanlegger som viser konsekvensene av endret forbruk og forsinkede leveringer.**

Start med en dokumentert kodeversjon og en oversikt over eksisterende funksjoner og tester. Velg deretter én sammenhengende forbedring med brukerbehov og akseptansekriterier. Mulige spor som må kontrolleres mot koden:

- Sammenligne en grunnplan med et scenario med forsinket levering eller endret forbruk, og forklare hvilke dager og siloer som rammes.
- Koble et avgrenset importformat til planleggingen, med eksplisitt feltkobling, feilrapport og sporbarhet til datagrunnlaget. Fôrkalkulatoren har allerede en importingang. [4]
- Forbedre forklaringen av hvorfor en plan er umulig, og vise hvilke endringer som gjør den gjennomførbar.

Suppler med relevante tester, brukertest og dokumentasjon av KI-feil, rettelser og egne faglige valg. BMAD-dokumentene bør beskrive arbeidet slik det faktisk skjer; allerede utviklede funksjoner må merkes som utgangspunkt.

Om appen må ha en KI-funksjon er ikke bekreftet. Et eventuelt krav kan møtes med forklaring av beregnede avvik, men selve mengde- og kapasitetskontrollen bør være etterprøvbar kode. Dette er et designforslag, ikke en dokumentert emneregel.

## Beslutning og åpne spørsmål

Den sterkeste innvendingen mot Forplanner er at løsningen allerede er omfattende. En nesten ferdig app med små endringer kan gi mindre nytt prosjektarbeid enn et enklere verktøy med en tydelig uløst brukeroppgave.

Før kandidaten blir et endelig prosjektvalg må gruppen avklare:

1. Hva tillater oppgaveteksten/faglærer av eksisterende kode og tidligere privat arbeid?
2. Hvilke konkrete forbedringer mangler i dagens kode og tester?
3. Er kjerneproblemet forståelig for begge, og er en vesentlig del av leveransen avtalt for hvert gruppemedlem?
4. Kreves KI i produktet, eller er dokumentert KI-bruk i utviklingsprosessen tilstrekkelig?

Anbefalt BMAD-overgang: bruk vurderingen i `bmad-product-brief` når punktene over er avklart. Briefen må angi eksisterende løsning, nytt arbeid, målgruppe og suksesskriterier. Ikke start et prosjekt for hele AquaTools uten en samlet brukeroppgave som begrunner omfanget.

## Kilder og begrensninger

Alle kildene er AquaTools' egne, direkte observerte sider. Publiseringsdato er ukjent; besøksdato er 2026-09-07. Tillit er middels for hva grensesnittet viser. Uavhengig verifikasjon av funksjonenes virkemåte foreligger ikke. Detaljer finnes i [observasjonsnotatet](digests/ui-r1-1.md).

| Ref | Støtter | Utgiver og kilde | Publisert | Besøkt | Tillit |
| --- | --- | --- | --- | --- | --- |
| [1] | Planleggingsfelter og forslag | [AquaTools – Forplanner](https://aquatools.vercel.app/forplanner) | Ukjent | 2026-09-07 | Middels |
| [2] | Kart, filtrering og dekning | [AquaTools – Lokalitetspanel](https://aquatools.vercel.app/lokalitetspanel) | Ukjent | 2026-09-07 | Middels |
| [3] | Temperaturkilder og kalender | [AquaTools – Døgngrader](https://aquatools.vercel.app/dogngrader) | Ukjent | 2026-09-07 | Middels |
| [4] | Forbruk, import og bestilling | [AquaTools – Fôrkalkulatoren](https://aquatools.vercel.app/kalkis2) | Ukjent | 2026-09-07 | Middels |
| [5] | Estimert tidsfordeling av observasjoner | [AquaTools – Dødelighetsforløp](https://aquatools.vercel.app/dodfiskfordeler) | Ukjent | 2026-09-07 | Middels |
| [6] | Hurtigberegning og organisering | [AquaTools – Slangetrykk](https://aquatools.vercel.app/slangetrykk) | Ukjent | 2026-09-07 | Middels |
| [7] | Tilgangsbegrensning og filanalyseinngang | [AquaTools – Stingray Status](https://aquatools.vercel.app/stingray-status) | Ukjent | 2026-09-07 | Middels |

## Når vurderingen må oppdateres

Publiseringsdatoene er ukjente, så datobasert foreldelse kan ikke beregnes pålitelig. Se `staleness.json`. Sjekk funksjonsomfanget mot konkret kodeversjon før prosjektvalg. Emnekravene må avklares nå. Oppdater vurderingen hvis ny oppgavetekst, nye funksjoner eller endrede gruppepreferanser kommer til.
