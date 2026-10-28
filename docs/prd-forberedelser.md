# Forberedelser til PRD – torsdag 29. oktober 2026

Skrevet av Codex 26.10.2026. Dette er en oversikt over eksisterende grunnlag og
researchplanen som Odin godkjente for gjennomføring 26.10.2026. Dette er ikke en ferdig PRD eller nye produktkrav.

## Kursbeskjeden

Kunngjøringen fra Istvan Hadhazi, publisert 26.10.2026 kl. 20.27 i IBE160,
ber studentene forberede relevant research før torsdag. Temaene er prosjektets
problem og målgruppe, uklare spørsmål, brukerbehov, ideer/funksjoner og lignende
løsninger. Research topics og brainstorming-temaer bør noteres underveis.
PRD-en trenger ikke være ferdig før samlingen.

Kilde: kunngjøringens tekst gjengitt i prosjektsamtalen 26.10.2026. En direkte
kunngjøringslenke er ikke oppgitt, og teksten er ikke kontrollert på nytt i Canvas.
Torsdag er 29.10.2026; dette er en forberedelse til undervisningen, ikke en ny
sluttfrist for prosjektleveransen. Se [kravoversikten](ibe160-leveringskrav.md).

## Grunnlag som allerede finnes

| Prosjektgrunnlag | Hva det bidrar med | Hva det ikke dokumenterer |
|---|---|---|
| [Gjeldende produktbrief](../productbrief.md) | Problemhypotese, målgruppe, kjerneflyt, suksesskriterier og MVP-grenser. | Problemets hyppighet og tidsbesparelse er uttrykkelig ikke validert med målgruppen. |
| [Demoscenario](demoscenario-fravaer.md) og [søkemetode](forslag-ved-frafall.md) | R1–R5, P1/P2, søkegrense 0–1, historikk, statuser og kontrolltilfeller. | Komplett datasett, kode, responstidsmålinger og faktisk brukerforståelse. |
| [Teknologi og arbeidsdeling](teknologivalg.md) | React/Python/FastAPI, lokal oppstart, justerbar arbeidsdeling og utsatt modellvalg. | Valgt KI-modell, ferdig integrasjon eller beslutning om hosting/Supabase. |
| [Konkurransesjekken fra 7. september](../_bmad-output/planning-artifacts/research/competitive-simployer-quinyx-4human-akutt-bemannings-2026-09-07/research.md) | Tidligere spørsmål, kilder og åpne hull om Simployer, Quinyx og 4human. | Ny verifikasjon av funksjoner. At noe ikke ble funnet offentlig, dokumenterer ikke at leverandøren mangler det. |
| [Faglærers tilbakemelding](../tilbakemelding-product-brief.md) | Råd om avgrensning, konkrete regler, scenarier og kjøring uten KI-nøkkel. | Tilbakemeldingen vurderer briefen slik den var 6. oktober, ikke dagens løsning. |

Dette er fakta om prosjektets dokumentasjon, ikke uavhengig forskning som
bekrefter behovet for produktet.

## Godkjent researchplan

Formål: få et kildebelagt grunnlag for brukerbehov, krav og avgrensninger i
[SCRUM-46](https://stiodi.atlassian.net/browse/SCRUM-46), og en kort liste med
spørsmål å ta med til undervisningen. Planen er foreslått av Codex og godkjent for gjennomføring av Odin 26.10.2026. Godkjenningen gjelder researcharbeidet, ikke produktkrav.

| Prioritet og spor | Spørsmål | Planlagt grunnlag | Bruk i PRD |
|---|---|---|---|
| 1. Brukerbehov og arbeidsflyt | Hvilke opplysninger og avveininger er viktige når en leder skal håndtere et konkret frafall? Hva skaper usikkerhet eller manuelt arbeid? | Originalstudier og førstehåndsbeskrivelser, med tydelig målgruppe og kontekst. Eventuelle egne målgruppeinnspill holdes atskilt fra nettkilder. | Problem, brukerbehov og hva sammenligningen må forklare. |
| 2. Lignende løsninger | Hva viser Simployer, Quinyx og 4human faktisk om erstatning ved fravær, regelkontroll, rangering og forklaring? Hva kan vi lære, og hva er fortsatt ukjent? | En avgrenset utdyping av eksisterende konkurransesjekk, med produktdokumentasjon og relevante versjonsnotater. Åpne hull prioriteres fremfor å starte samme undersøkelse på nytt. | Realistisk omtale av alternativer og konkrete mønstre å lære av. |
| 3. KI-forklaringer og forståelse | Hvilken nytte skal språkmodellen gi utover standardforklaringen? Hvordan kan vi kontrollere at den følger dataene og hjelper lederen å forstå en avveining? | Originalforskning og dokumenterte evalueringsmetoder. Funn om andre domener merkes som overføringsgrunnlag, ikke målgruppevalidering. | KI-oppgave, input/svarformat og testbare kvalitetskrav før modellvalg. |

Metode: brukerbehov er hovedsporet (user-voice), med avgrenset utdyping
av den eksisterende konkurransesjekken og et eget spor om KI-forklaringer.
Spørsmålene undersøkes uavhengig og sammenstilles etterpå (breadth-first).

Avtalt innsats: en kort første runde, anslagsvis 10–20 minutter, med inntil
to parallelle researchassistenter, høyst fem nye kilder per spor og én runde per
spor. Sporene er selvstendige; resultatene gjennomgås sammen før videre utdyping.
Dette tilsvarer quick-innstilling med normal verifikasjon: sentrale påstander
kontrolleres, og svakheter og motstridende funn tas med. Primærkilder prioriteres.
Nettlesøk og direkte lesing av kilder er tilgjengelig. Jira/repo brukes til å
avgrense spørsmål, ikke som eksternt bevis på brukerbehov eller konkurrentfunksjoner.

For konkurransedelen prioriteres nyere dokumentasjon; eldre kilder merkes som
eldre. Alle funn skal ha URL, utgiver, publiseringsdato hvis kjent, besøksdato
og usikkerhet. Leverandørpåstander skilles fra uavhengige brukerfunn. Konstruerte
scenarioer og personaer skal ikke presenteres som intervjuer eller observasjoner.
Kildeinnsamling og resultater ligger i [researchrapporten](../_bmad-output/planning-artifacts/research/user-voice-vaktmatch-brukerbehov-og-prd-grunnlag-2026-10-26/research.md).

## Brainstorming-temaer for gjennomgang

- Hva må lederen forstå for å velge mellom to gyldige alternativer?
- Hvordan skiller vi «ingen funn innenfor søkegrensen» fra manglende opplysninger?
- Hvilken historisk kontekst hjelper i beslutningen uten å gi en skjult rangering?
- Hvilken merverdi kan KI-forklaringen gi, og når er standardforklaringen nok?
- Hvilke opplysninger og konsekvenser bør være synlige med én gang på mobil?

Temaene er spørsmål, ikke vedtatte nye funksjoner. Besluttede scenarioregler,
søkegrenser, lokal oppstart og utsatt modellvalg er arbeidsgrunnlaget. En endring
av disse må begrunnes og avklares særskilt.

## Resultat av første researchrunde

Researchen er gjennomført 26.10.2026 og bygger på elleve kilder. Se
[rapporten med kilder og forbehold](../_bmad-output/planning-artifacts/research/user-voice-vaktmatch-brukerbehov-og-prd-grunnlag-2026-10-26/research.md)
eller [lesevisningen](../_bmad-output/planning-artifacts/research/user-voice-vaktmatch-brukerbehov-og-prd-grunnlag-2026-10-26/research-briefing.html).
Den gir grunnlag for å undersøke kompetanse og konsekvenser ved fraværsdekning,
viser overlapp med etablerte løsninger og foreslår å evaluere KI-tekst mot
standardtekst. Behovene i vår konkrete målgruppe og produktets merverdi er
fortsatt ikke validert. Forslagene er Codex sine vurderinger, ikke nye krav.

## Videre arbeid før undervisningen

Rapportens åpne spørsmål diskuteres før funn eventuelt tas inn i brief/PRD.
Direkte brukerundersøkelse i SCRUM-50 og brukertest i SCRUM-45
er fortsatt valgfrie etter eksisterende prosjektgrunnlag; kunngjøringen gjør
dem ikke til nye obligatoriske leveranser.

Researchplanen er gjennomgått og oppstart er godkjent. PRD-filen utarbeides
videre gjennom SCRUM-46; denne forberedelsen erstatter ikke PRD-arbeidet.
