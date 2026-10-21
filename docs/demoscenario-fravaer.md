# Demoscenario: ett fravær på en generell arbeidsplass

*(Skrevet: Codex · 06.10.26; oppdatert: 22.10.26 etter Odins beslutning)*

**Status:** Konkretisering av [produktbriefen](../productbrief.md).
Odin har valgt en generell arbeidsplass uten bransje og ønsker at lederen skal
kunne styre hvilke hensyn som prioriteres ved sortering. Odin besluttet R1–R5,
P1 som standard og P2 som valgfritt kriterium 21.10.26 innenfor felles delegert
beslutningsmyndighet, slik han har gjengitt avtalen fra møtet med Stian samme dag.
Dette tilskriver ikke Stian de konkrete regelvalgene. Datasettet nedenfor er et
konstruert eksempel skrevet av Codex.
Alle ansatte og hendelser er konstruerte eksempler. Reglene beskriver et avgrenset
scenarioregelsett, ikke en full kontroll av lovverk eller avtaler.

**Arbeidsretning, avklart i SCRUM-16:** Førsteversjonen bruker demodata med fire
uker historikk og ferdig planlagt uke 5. Verktøyet foreslår håndtering av frafall
i uke 5 med synlig kontekst fra tidligere planer. Dette erstatter separat
generering av en ny ukeplan i MVP. Historikken endres ikke. VaktMatch viser
forslag og konsekvenser, men gjennomfører ikke vaktendringer.
Eksemplet er tilpasset dette; tidligere alternativer for
bekreftelse er bevart som historikk nedenfor. Søkegrense og tilbudssimulering er
avklart i SCRUM-15, som beskrevet nedenfor. Tabellen her viser direkte erstatning.

## Situasjonen og avgrensningen

En leder har en godkjent bemanningsplan. Ansatt A01 får registrert fravær fra
vakten onsdag 14.10.2026 kl. 08.00–16.00. Vakten trenger én person med kompetanse
K1. Lederen velger «Finn alternativer» og sammenligner direkte erstattere.

Eksemplet har åtte interne ansatte (A01–A08), én forhåndsgodkjent ekstern vikar
(V01) og kompetansekodene K1 og K2. Alle klokkeslett er lokale i Europe/Oslo.
Målperioden for timetelling er mandag 12.10 kl. 00.00 til mandag 19.10 kl. 00.00.
Én vakt teller åtte timer; pausefradrag er ikke modellert i eksemplet.
Uke 5 er her 12.–18.10.2026. Uke 1–4 er de fire foregående ukene, fra
14.09 kl. 00.00 til 12.10 kl. 00.00. Dette er relative ukenumre i demoen,
ikke kalenderens ukenumre. Historikken skal vise tilgjengelig dokumentasjon av
tidligere arbeidstid og vakter; den er ikke ferdig laget i hovedtabellen nedenfor.
Nødvendige nabovakter inn i uke 6 følger med for hvilekontroll ved ukegrensen.
P1, P2 og R5 bruker den samme faste sjudagersperioden i dette scenarioet. For en
vakt som krysser periodegrensen, teller bare den delen av vakten som ligger i
perioden. Dette er en scenariodefinisjon, ikke en generell regel for arbeidstid.

Hovedeksemplet bruker søkegrense 0 og undersøker direkte erstattere. Appens
standardgrense er 1, som også undersøker én intern flytting. «Ingen løsning»
gjelder alltid det undersøkte kandidatsettet og den viste søkegrensen.

## Historikk som synlig beslutningsgrunnlag – SCRUM-16

Odin har avklart fire ukers historikk som synlig beslutningsgrunnlag for
lederens valg ved frafall i en eksisterende uke 5. Arbeidstid, vakttyper og
sammenlignbare vakter kan gi kontekst når grunnlaget finnes. En tidligere
planlagt vakt dokumenterer ikke alene faktisk utført arbeid eller hvem som
dekket et fravær. Opplysningenes kilde, periode og eventuelle mangler skal vises.

Historikken gir ikke en ny poengsum eller automatisk endret rangering. P1/P2
beregnes fortsatt for arbeidsuken, og R1–R5 kontrolleres i det nye forslaget.
Gjenbruk av et historisk mønster betyr ikke at ny tildeling er bestått; kompetanse,
tilgjengelighet, kollisjon, hvile og timer må vurderes på det aktuelle grunnlaget.
Konkrete historikkfelt og presentasjon må spesifiseres i videre data-/designarbeid.
At historikken ligger fast betyr at søket og forslagene ikke omskriver den.
En korrigert datakilde kan lastes inn som ny dataversjon gjennom den avklarte
oppdateringshandlingen. Endrede historikkopplysninger vises i endringsoversikten
og utløser ny vurdering når de berører kontrollgrunnlaget, for eksempel hvilen
fra uke 4. Tidligere valg og svar forblir knyttet til gammel dataversjon.

| Kontrolltilfelle | Oppsett | Forventet resultat |
|---|---|---|
| H1 Uendret sortering | A02/A03 som i hovedtabellen; endre bare historikk som ikke påvirker R1–R5 eller P1/P2, for eksempel eldre vakttyper uten betydning for nabovakter. | Historikken vises med periode og kilde. P1 gir fortsatt A02 først, P2 A03 først. Historikk som påvirker nødvendig kontrollgrunnlag krever derimot ny regelkontroll. Lederen velger. |
| H2 Ufullstendig historikk | Historiske timer eller vakttyper mangler. | Vis mangelen uten å fylle den med antakelser. Dersom nødvendig grunnlag for R1–R5 mangler, blir den berørte kontrollen uavklart. |
| H3 Gammelt mønster med nytt avvik | En person hadde lignende vakter tidligere, men er utilgjengelig i uke 5. | Historikken gjør ikke personen tilgjengelig; R2 viser avvik på det aktuelle grunnlaget. |
| H4 Ukegrense | Forslaget berører siste vakt i uke 5. | Hvile mot første relevante vakt i uke 6 kontrolleres; manglende nødvendig nabovaktgrunnlag gir uavklart kontroll. |
| H5 Start på arbeidsuken | Første vakt i uke 5 starter mandag 12.10 kl. 08. Samme kandidat har siste relevante vaktslutt i uke 4 søndag kl. 21, eller kl. 22, eller ukjent. Øvrige nødvendige opplysninger er komplette og gir ingen brudd. | Kl. 21 gir 11 timer og består denne siden av R4; kl. 22 gir 10 timer og regelavvik. Ukjent nødvendig grunnlag gir uavklart kontroll. |

## Søkeomfang og simulert tilbud – SCRUM-15

**Beslutning:** Odin avklarte søkeomfang og tilbudssimulering i samtalen om
SCRUM-15 innenfor den dokumenterte felles delegeringen. Grense 0 betyr bare
direkte erstattere. Grense 1 inkluderer også omfordeling med opptil én flytting
av en eksisterende vakttildeling og er både standard og maksimum i førsteversjonen.
En ny tildeling til en ledig erstatter teller ikke som en flytting. Alle berørte
vakter må fortsatt være dekket og R1–R5 kontrollert mot den foreslåtte sluttplanen.
Et forslag som flytter bemanningsmangelen til en annen vakt er ikke komplett.
Hver ny tildeling kontrolleres mot den aktuelle vaktens kompetansekrav og tidsrom;
K1 og 08–16 i hovedtabellen gjelder fraværsvakten X. Før kontroll fjernes
flyttede tildelinger fra den hypotetiske planen, og de nye legges inn. Kollisjon,
hvile og timer beregnes deretter for alle berørte ansatte i sluttplanen.

To flyttinger er en mulig neste utvidelse etter vurdering av kompleksitet og
målt responstid på representative demodata. En høyere grense er et senere
vurderingspunkt, ikke vedtatt funksjonalitet. Ingen konkret ytelse er lovet.

Demodata skal gi flere fungerende alternativer med ulike avveininger. A02 og A03
viser allerede to direkte alternativer: P1 favoriserer A02, P2 favoriserer A03.
Lederen kan beholde P1 og sende et simulert tilbud til A03. Antall gode kandidater
er uavhengig av antall flyttinger som tillates.
P1 og P2 bruker verdiene etter hele omfordelingen for personen som skal dekke
fraværsvakten. Øvrige berørtes timer, hvile og svarstatus vises som konsekvenser,
ikke som en ny samlet poengsum. Hvis direkte erstatter A har 32 timer etter
tildeling, mens B har 24 timer etter en omfordeling, står B først med P1 når
begge forslag består kontrollene. Lederen ser samtidig at Bs alternativ krever
en flytting og en erstatter C, og kan velge A for å unngå den omfordelingen.

Tilbudssimuleringen viser «tilbud sendt», «venter på svar», «akseptert» eller
«avslått». Alle berørte i en omfordeling må ha akseptert før forslaget vises med
full simulert aksept. Ett avslag gjør at forslaget ikke har full aksept, og lederen
kan undersøke et annet alternativ. Ubesvart tilbud forblir ventende. Simuleringen
gjennomfører ingen vaktendring og endrer ikke regelstatus. Det enkle eksemplet
kan kjøres uten tilbudssteget og merkes da «aksept ikke simulert».
Simulerte tilbud og svar gjelder det konkrete forslaget og datagrunnlaget de ble
gitt for. Endret deltaker eller tildeling krever ny simulering. Ved ny dataversjon
kontrolleres forslaget på nytt; gamle svar gir ikke automatisk aksept på det nye
grunnlaget. Dette er avgrensning av demostatus, ikke et krav om varig beslutningslogg.

| Kontrolltilfelle | Oppsett | Forventet resultat |
|---|---|---|
| F1 Direkte alternativer | Grense 0; A02 og A03 som i hovedtabellen. | Begge sammenlignes. Lederen kan velge A03 selv med P1 aktivt. |
| F2 Én intern flytting | B flyttes fra vakt Y til fraværsvakt X; ledige C dekker Y. Prøv grense 0 og 1. | Alternativet utelates ved grense 0 og undersøkes ved grense 1. Én eksisterende tildeling flyttes. Bare en sluttplan med begge vakter dekket og bestått R1–R5 for alle berørte kan vises som komplett. |
| F3 Flyttet bemanningsmangel | Som F2, men ingen kan dekke Y innenfor reglene. | Forslaget er ikke komplett, selv om X er dekket. |
| F4 Utenfor søkegrensen | Forslaget krever at både B og C flyttes fra eksisterende tildelinger. | Utelatt ved grense 0 og 1. Det gir ikke grunnlag for å hevde at ingen løsning finnes ved større søkeomfang. |
| F5 Tilbud til valgt kandidat | Lederen velger A03; simuler sendt tilbud og ventende svar, deretter aksept eller avslag. | Ventende er ikke aksept. Aksept endrer ingen vakter; ved avslag kan lederen undersøke A02. |
| F6 Delvis svar på omfordeling | B har akseptert, C har ikke svart eller avslår. | Forslaget vises ikke med full simulert aksept. Regelkontroll og svarstatus vises hver for seg. |
| F7 Eksempel uten tilbudssteg | Kjør hovedeksemplet uten simulering. | Vis «aksept ikke simulert»; ingen antatt aksept. |

F2–F4 er kontrollbeskrivelser med konstruerte roller, ikke et ferdig vaktsett med
fasit. Komplette vakter, tilgjengelighet og nabovakter gjenstår i dataarbeidet.

## Fem vedtatte scenarioregler

| Regel | Konkret kontroll | Kategori og kilde | Begrensning |
|---|---|---|---|
| R1 Kompetanse | Kandidaten må ha K1. | Intern scenarioregel, besluttet av Odin 21.10.26. | K1 er en kode i det konstruerte datasettet, ikke en offentlig kvalifikasjonsstandard. |
| R2 Tilgjengelighet | Kandidaten må være registrert tilgjengelig hele 08.00–16.00. Fravær betyr utilgjengelig. | Intern scenarioregel, besluttet av Odin 21.10.26. | Ledig plass i kalenderen alene bekrefter ikke tilgjengelighet. |
| R3 Kollisjon | Ingen eksisterende vakt kan overlappe 08.00–16.00. Slutt lik start regnes ikke som overlapp. | Intern scenarioregel, besluttet av Odin 21.10.26. | Kontrollen gjelder registrerte vakter i datagrunnlaget. |
| R4 Hvile | Minst 11 timer fra forrige vakt slutter til målskiftet starter, og fra målskiftet slutter til neste vakt starter. Nøyaktig 11 timer består. | Forenklet scenarioregel med lovutgangspunkt i [arbeidsmiljøloven § 10-8](https://lovdata.no/nav/lov/2005-06-17-62/kap10/%C2%A710-8). | Loven åpner for unntak. Scenarioet modellerer ikke tariffavtaler eller alle vilkår for unntak. |
| R5 Timetall | Samlet planlagt arbeidstid etter tildeling må være høyst 40 timer i den definerte sjudagersperioden. Nøyaktig 40 timer består. | Forenklet scenarioregel med lovutgangspunkt i [arbeidsmiljøloven § 10-4](https://lovdata.no/lov/2005-06-17-62/%C2%A710-4). | Kortere grenser kan gjelde blant annet ved skift- og turnusarbeid. Gjennomsnittsberegning, merarbeid og overtid er ikke modellert. |

R4 og R5 gjør tersklene håndkontrollerbare i demoen. De må ikke presenteres som
en generell garanti om at en faktisk arbeidsplan er lovlig. Ved reell bruk må
gjeldende lov, avtaler, arbeidstidsordning og komplett arbeidsgrunnlag avklares.

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
Når komplett historikk uttrykkelig viser at det ikke finnes en forrige eller neste
vakt, består den aktuelle siden av R4-kontrollen. Hvis fraværet av en nabovakt
skyldes ufullstendig historikk, er kontrollen uavklart.

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

## Lederstyrt prioritering – vedtatte sorteringsvalg

Lederen velger hvilket hensyn som er viktigst blant kandidatene som består alle
reglene. Scenarioreglene gjelder ved begge valg. Endret sortering endrer verken
regelstatus eller tildelingen i planen. Valget vises ved resultatet og brukes i
KI-forklaringen. Standardkonfigurasjonen er bare `[P1]`. Lederen kan aktivere P2,
deaktivere et aktivt kriterium så lenge minst ett gjenstår, og flytte P1 og P2 i
prioritert rekkefølge. Neste kriterium brukes bare når kandidater er like på det
foregående.

| Valg | Vedtatt beregning | Hva det viser |
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
Når en kandidat mangler data til et aktivt kriterium, vises kandidaten utenfor den
komplette rangeringen. Verdier fra tidligere kriterier kan fortsatt vises, men de
brukes ikke til å gi kandidaten en plass i den komplette rangeringen. Kandidater
med alle nødvendige sorteringsdata rangeres fortsatt innbyrdes.

Ved lik verdi på alle valgte kriterier vises kandidatene som likeverdige; ID
brukes bare for stabil visningsrekkefølge. KI-en skal ikke finne på et skille
mellom dem. Eksemplet har ingen vedtatt prioritering av intern foran ekstern
eller noen kostnadsberegning.

## Fem scenarioer med forventede svar

| Scenario | Endring fra dataene over | Forventet svar |
|---|---|---|
| S1 To bekreftede alternativer | Lederen velger P1 eller P2; ansattdataene er de samme. | P1 gir A02 foran A03; P2 gir A03 foran A02. Lederen kan undersøke begge og se konsekvensene. A04–A08 har fortsatt regelavvik. V01 er fortsatt uavklart og inngår ikke i rangeringen. Vakten vises som udekket i gjeldende datasett til oppdaterte data viser ny bemanning. |
| S2 Ingen direkte erstatter innenfor reglene | A02, A03 og V01 er uttrykkelig registrert utilgjengelige for hele vakten. | Ingen kandidat består. Vis «Ingen direkte erstatter innenfor scenarioreglene» og la lederen undersøke avvikene. Behovet er fortsatt udekket i datasettet. Resultatet gjelder direkte erstatning; omfordeling er ikke undersøkt i dette eksemplet. |
| S3 Mulig kandidat, men manglende data | A02 og A03 er registrert utilgjengelige. V01 har fortsatt ukjent tilgjengelighet. | Ingen bekreftet erstatter. Vis «Tilgjengelighet for V01 må avklares». Behovet er udekket og vurderingen uavklart; systemet kan ikke konkludere med at ingen kan ta vakten. |
| S4 Lik rangering | A02 og A03 består R1–R5 og har samme verdi på alle aktive kriterier; bruk `[P1, P2]`. | A02 og A03 vises som likeverdige. ID kan gi stabil visningsrekkefølge, men begrunnelsen skal ikke hevde at den ene er bedre. |
| S5 Manglende sorteringsdata | A02 og A03 består R1–R5; P2 er aktivt, men A03 mangler avtalt timetall. | A02 kan vises i den komplette rangeringen. A03 vises separat som ikke fullstendig rangerbar, med manglende avtalt timetall; A03 beholder bestått regelstatus, og systemet bytter ikke stille til P1. |

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
hviletid og interne føringer. R1–R5 er vedtatte regler for dette avgrensede
scenarioet. De skal ikke presenteres som en fullstendig eller verifisert
gjengivelse av lov- eller avtalekrav. Regelkilde og begrensninger må være synlige. Innstillinger for
søkeomfang endrer ikke reglenes betydning eller gjør et avvik til bestått kontroll.

I S3 vises at bekreftet tilgjengelighet for V01 mangler og hindrer ferdig kontroll.
Et forhåndslaget, komplettert datasett kan lastes inn og gi en ny vurdering.
Ansvar for datakvalitet på en virkelig arbeidsplass avklares før reell bruk;
demoen legger ikke dette ansvaret automatisk til mellomlederen.

## Forslag til demonstrasjon av oppdaterte data

**Avklart i SCRUM-17:** Odin godtok demohandlingene «Simuler fravær» og
«Last inn oppdaterte vaktdata», synlig endringsoversikt og ny vurdering. Den
eksisterende overskriften beholdes for historiske lenker. Det tidligere forslaget
er nå valgt som mekanisme, mens komplette datasett og kode fortsatt gjenstår.

«Simuler fravær» virker på gjeldende datagrunnlag og markerer valgt ansatt
utilgjengelig på valgt vakt; handlingen tilbakestiller ikke tidligere oppdateringer.
I eksemplet er startgrunnlaget D0. D1 er tilstanden etter simulert fravær;
handlingen viser hvilket fravær og hvilken bemanningsmangel som er lagt til.
Den registrerer ingen erstatning. Følgende viser oppdateringsdelen:

1. Datasett D1 viser S1: vakten er udekket og A03 har 32 planlagte timer. Lederen
   undersøker A03; dette endrer ikke D1.
2. En separat demohandling laster inn D2. D2 viser at A03 har overtatt vakten,
   har 40 planlagte timer og at A02 fortsatt har 24. Fraværet til A01 beholdes.
   Dette representerer en endring gjort i datakilden, ikke en tildelingshandling
   utført av VaktMatch.
3. Programmet sammenligner datasettene og kontrollerer den nye situasjonen.
   KI forklarer de observerte endringene ut fra disse resultatene. Ny bemanning
   og regelstatus vises hver for seg; bemannet betyr ikke automatisk bestått kontroll.

For å gjøre dette etterprøvbart brukes stabile vakt- og ansatt-ID-er og en
synlig dataversjon. D0, D1 og D2 er beskrivelser; komplette datasett er ikke laget.
Det må også kunne vises at en ny dataversjon
er uendret eller har en annen bemanning enn forslaget lederen undersøkte.
Ingen mottatt oppdatering betyr bare at nye data ikke er tilgjengelige, ikke
at ingenting har skjedd utenfor appen. KI skal ikke utlede hvem som gjorde
endringen, hvorfor den ble gjort eller om den skyldtes forslaget i VaktMatch.

Oppdatering skjer ved den eksplisitte demohandlingen og et forhåndslaget datasett.
Simulerte tilbud og svar beholdes med kobling til det gamle grunnlaget, men gir
ikke automatisk aksept på den nye dataversjonen. Ny kontroll må være synlig før
oppdaterte alternativer presenteres som ferdig vurdert.
Tidligere valgt alternativ beholdes som et historisk øktvalg på gammel dataversjon.
Det vises ikke som et gjeldende, ferdig vurdert valg før det er kontrollert på nytt.
Er kandidaten blitt utilgjengelig, vises avviket; er vakten allerede dekket,
vises ny bemanning og at det gamle alternativet ikke lenger er aktuelt.

## Beslutningslogg i demoen – SCRUM-17

Odin godtok at valgt alternativ og simulerte tilbud/svar beholdes i den aktive
demoøkten. Varig beslutningslogg inngår som valgfri funksjon, avslått som standard.
Begrunnelse er frivillig, også når logging er slått på. Logger gjelder registrerte
valg og simuleringer, knyttet til forslag og dataversjon; en aksept eller et valgt
alternativ registreres ikke som en gjennomført vaktendring.

Med logging av lagres ikke øktens valg og svar varig automatisk. Med logging på
kan registrerte valg leses etter avsluttet økt. Lagringsteknikk gjenstår i
implementeringen. Dette er produktets demologg; prosjektbeslutninger føres fortsatt
i repoets eksisterende dokumentasjon.
Som konkretisering av øktgrensen avsluttes demoøkten når fanen lukkes. Med logging
av er øktens valg og svar da ikke tilgjengelige ved ny åpning. Aktivering av
logging gjelder nye registreringer fra aktiveringstidspunktet og kopierer ikke
tidligere økthendelser automatisk. Deaktivering stanser nye varige registreringer;
allerede lagrede valg beholdes og kan leses senere. Disse overgangene endrer
ikke øktens synlige valg og svar så lenge økten er aktiv.

| Kontrolltilfelle | Oppsett | Forventet resultat |
|---|---|---|
| D1 Fravær | Velg A01 og målskiftet i D0; bruk «Simuler fravær». | A01 er utilgjengelig på målskiftet, bemanningsmangelen vises, og D1 kan vurderes. |
| D2 Oppdatert plan | Last inn D2 etter å ha undersøkt A03 i D1. | Vis endret bemanning og timer, dataversjon og ny kontroll. Gammelt tilbud/svar arves ikke som gjeldende aksept. |
| D3 Uendret eller annen oppdatering | Last inn en dataversjon med uendrede vakter eller en annen bemanning enn A03. | Vis de faktiske forskjellene, uten å hevde at lederens undersøkte alternativ er gjennomført. |
| D4 Komplettert grunnlag | Bruk S3: A02/A03 er utilgjengelige, V01 mangler tilgjengelighet. Last inn samme opplysninger, men med V01 bekreftet tilgjengelig. | A02/A03 forblir utilgjengelige. V01 består R1–R5 etter ny kontroll av det ellers komplette grunnlaget og kan rangeres med P1. Vis hvilken opplysning som ble komplettert. |
| D5 Standard uten varig logg | Velg et alternativ og simuler svar med logging av. | Valg/svar er synlige i aktiv økt, uten automatisk varig loggføring eller krav om begrunnelse. |
| D6 Valgfri varig logg | Slå på logging; registrer et valg uten begrunnelse og avslutt økten. | Det registrerte valget kan leses senere med korrekt forslag/dataversjon. Manglende begrunnelse blokkerer ikke. |
| D7 Logging av/på | Gjør valg A med logging av, slå på og registrer B, slå av og registrer C. Lukk og åpne fanen. | A/B/C er synlige i aktiv økt. Bare B lagres varig; A etterregistreres ikke, og B slettes ikke ved deaktivering. |
| D8 Tidligere valg etter oppdatering | Velg A03; last inn data der A03 er utilgjengelig eller vakten har fått annen bemanning. | Det gamle valget vises på gammel dataversjon. Ny kontroll og aktuell bemanning vises uten at gammelt valg fremstår som gjeldende. |

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
lovkrav er fortsatt ikke fastslått. Standardinnstillinger og MVP-omfang er senere
avklart i SCRUM-17 ovenfor: valgfri varig logg, avslått som standard, frivillig
begrunnelse og økttilstand. En endringsvisning er fortsatt ikke i seg selv en
logg over lederens beslutninger.

## Hva eksemplet avklarer videre

R1–R5, P1 som standard, P2 som valgfritt kriterium og håndtering av lik rangering
er avklart for scenarioet. Behandling av avtalte timer og stillingsprosenter må
fortsatt konkretiseres i datasettet for at P2 skal kunne beregnes. Søkegrense og
tilbudssimulering er avklart i SCRUM-15. Fire historikkuker og arbeidsuke 5 er
avklart i SCRUM-16; separat generering av en ny ukeplan er tatt ut av MVP.
Komplette historikkdata, planlagt uke 5, nødvendige nabovakter og fasit gjenstår.
Mekanismen for fravær og oppdaterte data er avklart i SCRUM-17. Søkemetode og
eventuelle låste tildelinger i uke 5 gjenstår i SCRUM-16.

Når en endring i dette forslaget fører til et valg i hovedbriefen, skal valget og
begrunnelsen føres i [endringsloggen](productbrief-endringslogg.md).
