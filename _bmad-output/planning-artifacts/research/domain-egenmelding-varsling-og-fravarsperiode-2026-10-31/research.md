---
title: Egenmelding, varsling og fraværsperiode – kort kildesjekk
type: domain
topic: egenmelding, varsling og fraværsperiode
decision: Grunnlag for UX-valg om fravær og berørte vakter i SCRUM-47
source: native
status: complete
preset: quick
validation: normal
invoked_by: bmad-ux
claims_verified: 2
claims_unverified: 2
sources_read: 4
created: 2026-10-31
updated: 2026-10-31
---

# Egenmelding, varsling og fraværsperiode

Undersøkelsen følger [godkjent plan](brief.md) og er utført av Codex med
ett kildeuttrekk og målrettet verifikasjon. Prosjektopplysninger er ikke
brukt som faktabevis. Fire ulike offentlige veiledningssider er lest 31.10.2026.

## Kort konklusjon

Egenmelding er et mulig scenario for UX-drøftingen, men bestemmer ikke
hvilke vakter som faktisk blir berørt. NAV beskriver melding til arbeidsgiver
fra første sykedag, og muntlig eller skriftlig egenmelding etter
arbeidsgiverens rutiner. [1][2] Et generelt krav om telefon til nærmeste
leder før vaktstart er **ikke verifisert i undersøkelsen**. En slik rutine
må knyttes til den aktuelle arbeidsplassen eller merkes som scenariovalg.

Maksimalt antall egenmeldingsdager er ikke en prognose for det konkrete
fraværet. [2][3][4] Vaktvalg må derfor drøftes ut fra opplysninger om
fraværet, ikke ved å anta tre dagers fravær automatisk.

## Funn og sikkerhet

| Funn | Kildegrunnlag og vurdering |
|---|---|
| Arbeidsgiver skal få beskjed om sykdom. NAV beskriver første sykedag; Altinn omtaler snarest mulig og meldingsdagens betydning. | [1][4]. Bekreftet i to offentlige veiledninger; høy tillit til gjengivelsen. NAV brukes for den presise formuleringen om første sykedag. |
| NAV opplyser at egenmelding kan gis muntlig eller skriftlig, og beskriver arbeidsgiverens egne rutiner/skjema. | [2]. Direkte kontrollert, men ikke uttrykkelig bekreftet av en annen utgiver i denne runden; middels tillit etter undersøkelsens verifikasjonskriterier. Dette avgjør ikke alle lokale kanalrutiner. |
| Minimumsordningen har en ramme på inntil tre kalenderdager om gangen; ordninger kan være utvidet. | [2][3][4]. Bekreftet i flere offentlige veiledninger. Slutningen om at rammen ikke angir faktisk forventet varighet er en avgrenset vurdering fra Codex. |
| Alle ansatte må ringe nærmeste leder før vakten. | Ikke verifisert. De leste sidene etablerer ikke dette som et universelt krav. Fravær av slik tekst beviser ikke at ingen lokal eller særskilt plikt finnes. |

Kontaktmåte, dokumentasjonsordning og faktisk fraværsperiode er ulike
opplysninger. Denne kombinasjonen er viktig for UX-en: et mottatt varsel
forteller ikke alene hvilke senere vakter som blir udekket.

## UX-vurderinger til videre avklaring

Følgende er **forslag fra Codex**, ikke vedtatte krav eller rettslige regler:

- Demoen kan starte med at lederen allerede har mottatt et sykdomsvarsel.
  Telefon kan inngå som konkret scenariorutine hvis Odin velger det.
- «Egenmelding» kan diskuteres som standard i demonstrasjonen, slik Odin
  foreslo. Det innebærer ikke at appen godkjenner egenmeldingsrett.
- Skill mellom hvilken vakt som håndteres nå og eventuell opplyst periode.
  En mulig visning for ukjent varighet må velges i UX-arbeidet; det er
  ikke en konklusjon om hvilke sluttdatoopplysninger loven krever.

Dette følges opp i SCRUM-47 og UX-memloggen. Brief, PRD og
fraværsmodell er ikke endret gjennom researchen. MVP-søket gjelder fortsatt
ett målskift etter det eksisterende prosjektgrunnlaget.

## Begrensninger og åpne spørsmål

Direkte Lovdata-oppslag for folketrygdloven kapittel 8 svarte HTTP 405.
Lovordlyden i §§ 8-18, 8-23 og 8-24 er derfor ikke direkte kontrollert.
Veiledningene er konsistente om de generelle rammene, men utgjør ikke
uavhengige rettslige grunnlag. Ingen bestemt arbeidsgiverrutine er undersøkt.
Se [kildeuttrekket](digests/varsling-r1-1.md) og
[verifikasjonen](digests/verification-r1.md).

Åpent: Om telefon skal være scenariorutine, og hvordan lederen skal angi
aktuell vakt når kjent eller ukjent fraværsperiode gjelder flere vakter.
Det første er et scenario-/UX-valg; et faktisk arbeidsgiverkrav trenger
arbeidsplassens dokumenterte rutine.

Runden stoppet på dekning av den avtalte UX-avklaringen. Direkte lovkontroll
står åpen; ytterligere undersøkelse krever et nytt, avgrenset oppdrag.

## Kilder

Alle opprinnelige publiseringsdatoer er ukjente. Datoene nedenfor er
kildenes oppgitte oppdatering eller faglige endring; alle ble lest 31.10.2026.

| Ref | Støtter | Utgiver og kilde | Oppdatert/faglig endring | Tilgang | Tillit |
|---|---|---|---|---|---|
| [1] | Første sykedag og varsling | NAV: [Sykmelding – arbeidsgiver](https://www.nav.no/arbeidsgiver/sykmelding) | 2026-08-21 | 2026-10-31 | Høy for veiledningen |
| [2] | Muntlig/skriftlig, lokale rutiner, dagramme | NAV: [Egenmelding](https://www.nav.no/egenmelding) | 2025-09-16 | 2026-10-31 | Middels for kanal-/rutinepåstanden, som har én uttrykkelig kilde |
| [3] | Definisjon og egenmeldingsramme | Helsedirektoratet: [Egenmelding ved sykdom](https://www.helsedirektoratet.no/veiledere/sykmelderveileder/alternativer-til-sykmelding-tilrettelegging-egenmelding-pleiepenger-mfl/egenmelding-ved-sykdom) | 2020-05-26 | 2026-10-31 | Støttekilde med eldre endringsdato |
| [4] | Varsling og egenmeldingsramme | Altinn / Digitaliseringsdirektoratet: [Sykefravær og sykepenger](https://info.altinn.no/starte-og-drive/arbeidsforhold/sykdom/sykefravar-og-sykepenger/) | 2026-08-19 | 2026-10-31 | Høy for veiledningen |

## Ferskhet

Regelopplysninger må kontrolleres mot gjeldende kilder ved hver ny bruk.
[Maskinkontrollen](staleness.json), beregnet fra [påstandene](claims.json)
med null måneders gyldighetsvindu for regelklassen, gir aldersvarsler fra
2020-05-01, 2025-09-01 og 2026-08-01; tidligste er 2020-05-01.
Dette er varsler fra kildenes oppdateringsmåneder, ikke nye rettslige frister
eller bevis for at innholdet er feil. Den aktuelle kontrollen ble gjort
31.10.2026. Kontroller på nytt før gjenbruk som regelgrunnlag; direkte
lovtekst og konkret arbeidsgiverrutine er de viktigste uavklarte sporene.
