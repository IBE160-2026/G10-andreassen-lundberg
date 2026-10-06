# Demoscenario: ett fravær på en generell arbeidsplass

*(Skrevet: Codex · 06.10.26; oppdatert: 07.10.26 etter Odins innspill)*

**Status:** Forslag til konkretisering av [produktbriefen](../productbrief.md).
Odin har valgt en generell arbeidsplass uten bransje og ønsker at lederen skal
kunne styre hvilke hensyn som prioriteres ved sortering. Regeltallene, de konkrete
sorteringsvalgene og datasettet nedenfor er Codex sine forslag til gjennomgang,
ikke vedtatte krav.
Alle ansatte og hendelser er konstruerte eksempler. Reglene beskriver et avgrenset
scenarioregelsett, ikke en full kontroll av lovverk eller avtaler.

**Arbeidsretning, presisert 07.10.26:** Førsteversjonen bruker en ferdig syntetisk
vaktplan som datagrunnlag og skal også kunne generere et enkelt planforslag.
Odin presiserte at generering beholdes; forslaget innføres ikke i den faktiske
vaktlisten. Dette dokumentet eksemplifiserer fraværsdelen, ikke hele genereringen.
VaktMatch viser forslag og konsekvenser, men gjennomfører ikke vaktendringer.
Eksemplet er tilpasset dette; tidligere alternativer for
bekreftelse er bevart som historikk nedenfor. Lederstyrt søkeomfang er ønsket,
men konkrete søkemåter og grenser gjenstår. Tabellen her viser direkte erstatning.

## Situasjonen og avgrensningen

En leder har en godkjent bemanningsplan. Ansatt A01 får registrert fravær fra
vakten onsdag 14.10.2026 kl. 08.00–16.00. Vakten trenger én person med kompetanse
K1. Lederen velger «Finn alternativer» og sammenligner direkte erstattere.

Eksemplet har åtte interne ansatte (A01–A08), én forhåndsgodkjent ekstern vikar
(V01) og kompetansekodene K1 og K2. Alle klokkeslett er lokale i Europe/Oslo.
Målperioden for timetelling er mandag 12.10 kl. 00.00 til mandag 19.10 kl. 00.00.
Én vakt teller åtte timer; pausefradrag er ikke modellert i eksemplet.

Vi undersøker bare om én person kan legges inn på den ledige vakten uten å flytte
andre vakter. Dette avgjør ikke om intern omfordeling av flere vakter skal inngå
i det endelige MVP-et. «Ingen løsning» gjelder det undersøkte kandidatsettet og
direkte erstatning. Det sier ikke at enhver mulig omplanlegging er umulig.

## Fem foreslåtte scenarioregler

| Regel | Konkret kontroll | Hvorfor den er med |
|---|---|---|
| R1 Kompetanse | Kandidaten må ha K1. | En ledig person må også kunne utføre oppgaven. |
| R2 Tilgjengelighet | Kandidaten må være registrert tilgjengelig hele 08.00–16.00. Fravær betyr utilgjengelig. | Ledig plass i kalenderen alene bekrefter ikke tilgjengelighet. |
| R3 Kollisjon | Ingen eksisterende vakt kan overlappe 08.00–16.00. Slutt lik start regnes ikke som overlapp. | Personen kan ikke være tildelt to samtidige vakter. |
| R4 Hvile | Minst 11 timer fra forrige vakt slutter til målskiftet starter, og fra målskiftet slutter til neste vakt starter. Nøyaktig 11 timer består. | En ny vakt må kontrolleres både bakover og fremover i planen. |
| R5 Timetall | Samlet planlagt arbeidstid etter tildeling må være høyst 40 timer i den definerte uken. Nøyaktig 40 timer består. | Gir en enkel grense som kan etterprøves for hånd. |

11 timer er hentet som utgangspunkt fra [turnusforslaget](../_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/brief.md).
40 timer er en foreslått demoverdi fra Codex. Tallene er ikke valgt som en
påstand om hvilke regler som gjelder for en faktisk arbeidsplass.

Alle fem regler må være bekreftet oppfylt før en kandidat kan vises som
**oppfyller scenarioreglene**. Et kjent brudd gir **regelavvik**. Ingen kjente
brudd, men manglende nødvendige data, gir **uavklart**. Kandidater med bestått
kontroll rangeres som en egen gruppe; de øvrige skal også kunne undersøkes med
tydelig status. Å undersøke et alternativ gjennomfører ingen vaktendring.
Ved kollisjon vises
R3-bruddet; hvilekontrollen kan da markeres som ikke vurdert fordi vakten allerede
overlapper. En kjent kollisjon er ikke datamangel.

## Data som trengs

For hver kandidat trengs ID, intern/ekstern tilknytning, kompetanser, registrert
tilgjengelighet, eksisterende vakter med start og slutt, samlet arbeidstid i
uken og en tydelig markering av om kontrollgrunnlaget er komplett. Nabovakter
utenfor den viste planperioden må også være med når de påvirker hvilen.
For eksterne vikarer må opplysningene dekke øvrig relevant arbeid.

Tabellen er et håndregnet kontrollgrunnlag for fravær, ikke en komplett syntetisk
vaktplan. Ukestimene er oppgitte syntetiske verdier. Før
implementering må de erstattes av konkrete vakter som summeres av systemet.
For alle unntatt V01 er tilgjengeligheten bekreftet hele målskiftet. V01 mangler
kun bekreftet tilgjengelighet; øvrige opplysninger i tabellen er komplette.

| Ansatt | Kompetanse | Forrige vakts slutt | Neste vakts start | Overlappende vakt | Timer før → etter | Kontrollutfall |
|---|---|---|---|---|---|---|
| A02 | K1 | ti. 13.10 kl. 16 | to. 15.10 kl. 08 | Ingen | 24 → 32 | Består alle regler; 16 t hvile på hver side. |
| A03 | K1 | ti. 13.10 kl. 20 | to. 15.10 kl. 08 | Ingen | 32 → 40 | Består alle regler; 12 t før og 16 t etter. |
| A04 | K2 | ti. 13.10 kl. 16 | to. 15.10 kl. 08 | Ingen | 24 → 32 | Regelavvik: mangler K1 (R1). |
| A05 | K1 | on. 14.10 kl. 00 | to. 15.10 kl. 08 | Ingen | 24 → 32 | Regelavvik: 8 t hvile før vakten (R4). |
| A06 | K1 | ti. 13.10 kl. 16 | on. 14.10 kl. 20 | Ingen | 24 → 32 | Regelavvik: 4 t hvile etter vakten (R4). |
| A07 | K1 | ti. 13.10 kl. 16 | to. 15.10 kl. 08 | on. 14.10 kl. 12–20 | 24 → 32 | Regelavvik: 4 t overlapp (R3). Hvile ikke vurdert. |
| A08 | K1 | ti. 13.10 kl. 16 | to. 15.10 kl. 08 | Ingen | 40 → 48 | Regelavvik: overstiger 40 t (R5). |
| V01 | K1 | ti. 13.10 kl. 16 | to. 15.10 kl. 08 | Ingen | 16 → 24 | Uavklart: tilgjengelighet mangler (R2). |

A01 er den fraværende ansatte og oppfyller ikke tilgjengelighetsregelen R2. For A07 viser
kolonnene også nærmeste ikke-overlappende nabovakter; den overlappende vakten
står separat og må inngå i kontrollgrunnlaget. «Timer etter» er en hypotetisk
beregning, også for kandidater med regelavvik; ingen tildeling er gjennomført.

## Lederstyrt prioritering – forslag til to sorteringsvalg

Lederen velger hvilket hensyn som er viktigst blant kandidatene som består alle
reglene. Scenarioreglene gjelder ved begge valg. Endret sortering endrer verken
regelstatus eller tildelingen i planen. Valget vises ved resultatet og brukes i
KI-forklaringen. Antall kriterier, eventuell prioritert rekkefølge og standardvalg
gjenstår å avklare; eksemplet viser ett valgt kriterium om gangen.

| Valg | Foreslått beregning | Hva det viser |
|---|---|---|
| P1 Færrest planlagte uketimer | Lavest samlet timetall etter tildeling først. | Hvem som vil ha færrest timer i den aktuelle uken. |
| P2 Lavest andel av avtalt timetall | Planlagte timer etter tildeling delt på avtalte timer for samme uke, stigende. | Hvor stor del av det avtalte timegrunnlaget den planlagte tiden utgjør. |

For å vise forskjellen legger vi til to konstruerte avtaleverdier:

| Ansatt | Planlagte timer etter tildeling | Avtalte timer for uken | Andel etter tildeling |
|---|---|---|---|
| A02 | 32 | 24 | 32 / 24 = 133,3 % |
| A03 | 40 | 40 | 40 / 40 = 100 % |

Med P1 kommer A02 først. Med P2 kommer A03 først. Begge oppfyller fortsatt
R1–R5. Avtalte timer er her et grunnlag for sortering, mens 40-timersgrensen i R5
er en egen scenarioregel. Eksemplet modellerer ikke avtalevilkår eller regler for
merarbeid og overtid. Et forholdstall alene dokumenterer heller ikke rettferdighet.

P2 krever et kjent, positivt avtalt timetall for den samme perioden. Bare en
stillingsprosent er ikke nok uten et definert timegrunnlag. Mangler sorteringsdata,
vises det tydelig og en fullstendig rangering etter P2 kan ikke bekreftes.
Regelstatusen beholdes: en kandidat som består R1–R5 blir ikke utelukket fordi
avtalte timer mangler. Systemet må heller ikke stille bytte til P1 uten å vise det.

Ved lik verdi foreslås kandidatene vist som likeverdige; ID brukes bare for
stabil visningsrekkefølge. KI-en skal ikke finne på et skille mellom dem.
Eksemplet har ingen vedtatt prioritering av intern foran ekstern eller noen
kostnadsberegning. P1 og P2 er forslag til gjennomgang, ikke et fastsatt kriterieutvalg.

## Tre scenarioer med forventede svar

| Scenario | Endring fra dataene over | Forventet svar |
|---|---|---|
| S1 To bekreftede alternativer | Lederen velger P1 eller P2; ansattdataene er de samme. | P1 gir A02 foran A03; P2 gir A03 foran A02. Lederen kan undersøke begge og se konsekvensene. A04–A08 har fortsatt regelavvik. V01 er fortsatt uavklart og inngår ikke i rangeringen. Vakten vises som udekket i gjeldende datasett til oppdaterte data viser ny bemanning. |
| S2 Ingen direkte erstatter innenfor reglene | A02, A03 og V01 er uttrykkelig registrert utilgjengelige for hele vakten. | Ingen kandidat består. Vis «Ingen direkte erstatter innenfor scenarioreglene» og la lederen undersøke avvikene. Behovet er fortsatt udekket i datasettet. Resultatet gjelder direkte erstatning; omfordeling er ikke undersøkt i dette eksemplet. |
| S3 Mulig kandidat, men manglende data | A02 og A03 er registrert utilgjengelige. V01 har fortsatt ukjent tilgjengelighet. | Ingen bekreftet erstatter. Vis «Tilgjengelighet for V01 må avklares». Behovet er udekket og vurderingen uavklart; systemet kan ikke konkludere med at ingen kan ta vakten. |

Eksempel på KI-forklaring i S1 med P1:

> A02 og A03 oppfyller scenarioreglene. A02 kommer først etter prioriteringen
> «lavest uketimetall etter tildeling»: 32 timer mot 40 timer for A03. Begge kan
> ta vakten uten at andre vakter flyttes. V01 kan ikke vurderes ferdig før
> tilgjengeligheten er bekreftet. Dette er forslag; vaktene i datagrunnlaget
> er ikke endret.

Eksempel på KI-forklaring i S1 med P2:

> Du har prioritert lavest andel av avtalt timetall. A03 kommer først fordi 40
> planlagte timer utgjør 100 % av de avtalte 40 timene. For A02 utgjør 32
> planlagte timer 133,3 % av de avtalte 24 timene. Begge oppfyller fortsatt
> scenarioreglene. Planen er ikke endret ved å bytte sortering.

Dette er konstruerte eksempler på forventede forklaringer, ikke testede modellresultater.
De samme kandidatstatusene, tallene og prioriteringene skal vises uten modelltilgang,
med standardtekst. KI-en kan variere ordlyden, men skal ikke endre grunnlaget.

## Lederen velger – verktøyet viser avveiningene

Regelkontroll, sortering og lederens beslutning vises hver for seg. Lederen kan
for eksempel beholde P1 og likevel velge A03, selv om A02 har færrest uketimer.
Verktøyet skal da vise at A03 oppfyller reglene, at de planlagte timene øker fra
32 til 40, og at ingen andre vakter flyttes. A02s planlagte timer forblir 24 hvis
A03 får vakten. Sorteringskriteriet byttes ikke automatisk for å rettferdiggjøre valget.

KI-veiledningen kan nås med faste handlinger som «Forklar forskjellen»,
«Vis konsekvensene av dette valget» og «Hva mangler?». Handlingsnavnene er
Codex sine UI-forslag. Svarene skal forklare dokumenterte konsekvenser og gjøre
usikkerhet synlig. KI-en skal ikke anta lederens begrunnelse eller ta beslutningen.

Eksempel når lederen undersøker A03 med P1 valgt:

> Du undersøker A03. Begge kandidatene oppfyller scenarioreglene. A03 vil få
> 40 planlagte timer denne uken, mens valg av A02 ville gitt A02 32 timer.
> A02 står derfor først etter sorteringen du har valgt. Forslaget med A03
> flytter ingen andre vakter. Dette viser konsekvensene dersom A03 får vakten;
> ingen vaktendring er gjennomført av VaktMatch.

## Manglende data og regelgrunnlag

Odin ønsker at lederen får informasjon om relevante konflikter, arbeidstidsgrenser,
hviletid og interne føringer. I prototypen er R1–R5 fortsatt foreslåtte demoregler.
De skal ikke presenteres som en fullstendig eller verifisert gjengivelse av lov-
eller avtalekrav. Regelkilde og begrensninger må være synlige. Innstillinger for
søkeomfang endrer ikke reglenes betydning eller gjør et avvik til bestått kontroll.

I S3 kan teksten for eksempel forklare at bekreftet tilgjengelighet for V01 vil
gjøre kontrollgrunnlaget mer komplett. Dette er Codex sitt tekstforslag. Det
pålegger ikke mellomlederen å hente inn eller rette data; ansvar og eventuell
arbeidsflyt er ikke valgt. Appen skal vise usikkerheten selv om den ikke kan
tilby en konkret vei til bedre grunnlag.

## Forslag til demonstrasjon av oppdaterte data

Odin ønsker at beslutningsstøtten kan se når vaktdata endres, med syntetiske data
i prosjektet. Codex foreslår følgende enkle demonstrasjon, uten leverandørtilkobling:

1. Datasett D1 viser S1: vakten er udekket og A03 har 32 planlagte timer. Lederen
   undersøker A03; dette endrer ikke D1.
2. En separat demohandling laster inn D2. D2 viser at A03 har overtatt vakten,
   har 40 planlagte timer og at A02 fortsatt har 24. Fraværet til A01 beholdes.
   Dette representerer en endring gjort i datakilden, ikke en tildelingshandling
   utført av VaktMatch.
3. Programmet sammenligner datasettene og kontrollerer den nye situasjonen.
   KI forklarer de observerte endringene ut fra disse resultatene. Ny bemanning
   og regelstatus vises hver for seg; bemannet betyr ikke automatisk bestått kontroll.

For å gjøre dette etterprøvbart foreslår Codex stabile vakt- og ansatt-ID-er og
en synlig dataversjon eller oppdateringstid. D1 og D2 er foreløpig beskrivelser;
komplette datasett er ikke laget. Det må også kunne vises at en ny dataversjon
er uendret eller har en annen bemanning enn forslaget lederen undersøkte.
Ingen mottatt oppdatering betyr bare at nye data ikke er tilgjengelige, ikke
at ingenting har skjedd utenfor appen. KI skal ikke utlede hvem som gjorde
endringen, hvorfor den ble gjort eller om den skyldtes forslaget i VaktMatch.

Dette er et forslag til demomekanisme og kontrolltilfeller. Valg av innlasting,
oppdateringsfrekvens og omfang gjenstår; det er ikke lovet kontinuerlig overvåking.

## Åpent valg – bekreftelse ved regelavvik

**Historikk, presisert 07.10.26:** Alternativene nedenfor ble beskrevet da
VaktMatch fortsatt var tenkt å gjennomføre planendringen. Den nye arbeidsretningen
gir forslag uten å endre vakter; tabellen er derfor ikke gjeldende krav til en
bekreftelsesfunksjon. Ingen av modellene ble valgt.

Odin ba 06.10.26 om at begge mulighetene beskrives før dette avgjøres:

| Mulighet | Hva lederen kan gjøre | Hva verktøyet må vise |
|---|---|---|
| A – sperre ved regelavvik | Undersøke alle kandidater, men bare bekrefte en tildeling som oppfyller scenarioreglene. | Konkrete avvik og hvorfor bekreftelse er sperret. Lederen kan fritt velge blant kandidatene som består, uansett sorteringsrekkefølge. |
| B – bekrefte med dokumentert avvik | Undersøke og eventuelt bekrefte et alternativ med regelavvik etter en tydelig advarsel og registrert begrunnelse. | Regelavviket beholdes synlig på valgt kandidat og planendring. Lederens bekreftelse gjør ikke kontrollresultatet til «oppfyller scenarioreglene». |

Odin presiserte senere 06.10.26 at innspillet om å kunne slå av en funksjon gjaldt
lagring av valg og krav om begrunnelse, ikke adgang til å overstyre reglene.
Beslutningslogg og begrunnelseskrav er egne produktvalg, med ønske om at de kan
slås av når de bare følger interne retningslinjer og ikke er lovpålagt. Eventuelle
lovkrav, standardinnstillinger og MVP-omfang er ikke fastslått. En visning av
endrede vaktdata er heller ikke i seg selv en logg over lederens beslutninger.

## Hva eksemplet avklarer videre

Før reglene tas inn som krav, må vi ta stilling til 11 timers hvile, 40-timersgrensen
og hvilke sorteringsvalg lederen skal få, med standardvalg og håndtering av lik
rangering. Behandling av avtalte timer og stillingsprosenter må konkretiseres hvis
P2 skal inngå. Planhorisont, konkrete søkemåter og grenser for eventuell omfordeling
av flere vakter er fortsatt åpne valg i hovedbriefen. Fullstendig syntetisk vaktplan,
fasit og en mekanisme for å vise oppdaterte data gjenstår. Plangenerering inngår
som forslag uten innføring i faktisk vaktliste; den trenger et eget scenario
med bemanningsbehov, avgrensning av hvilke tildelinger som kan endres, og fasit.

Når en endring i dette forslaget fører til et valg i hovedbriefen, skal valget og
begrunnelsen føres i [endringsloggen](productbrief-endringslogg.md).
