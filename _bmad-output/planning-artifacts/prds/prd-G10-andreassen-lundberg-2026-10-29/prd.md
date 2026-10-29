---
title: VaktMatch – PRD
status: final
created: 2026-10-29
updated: 2026-10-29
---

# PRD: VaktMatch

*(Skrevet: Claude Code · 29.10.26, etter Stians valg av kjerne og prioriteringer.
Gjennomgått mot BMAD-rubrikken i [review-rubric.md](review-rubric.md). Odin har
ikke gått gjennom PRD-en ennå; se åpent spørsmål 2. PRD-en er et levende
dokument og oppdateres når krav endres.)*

## 0. Formål og grunnlag

PRD-en gjør [produktbriefen](../../../../productbrief.md) om til nummererte,
testbare krav som Jira-saker, commits og tester kan vise til. Den er skrevet for
gruppen, for videre BMAD-arbeid (UX, arkitektur, stories) og for sensor, som
vurderer appen mot det briefen lovet.

PRD-en gjentar ikke detaljene som allerede er besluttet. Den viser til:

- [Demoscenarioet](../../../../docs/demoscenario-fravaer.md) for R1–R5, P1/P2,
  kontrolltilfeller og forventede svar (S1–S5, H1–H5, F1–F7, D1–D8).
- [Forslag ved frafall](../../../../docs/forslag-ved-frafall.md) for søkemetode,
  låser, vurderingstidspunkt og resultatstatuser.
- [Teknologi og arbeidsdeling](../../../../docs/teknologivalg.md) og
  arkitekturen fra SCRUM-18 for tekniske valg.
- [Researchrapporten fra 26.10.26](../../research/user-voice-vaktmatch-brukerbehov-og-prd-grunnlag-2026-10-26/research.md)
  for brukerbehov, lignende løsninger og KI-forklaringer.
- [Leveringskravene](../../../../docs/ibe160-leveringskrav.md) og
  sensorveiledningen for del 1.

Kravene er delt i **Må** (kjerneflyten som skal fungere fra start til slutt) og
**Bør** (utvidelser som bygger på kjernen). Avvik fra briefen står i §7.2.

## 1. Visjon

VaktMatch hjelper en skiftleder som får beskjed om fravær kort før vaktstart.
Lederen ser hvem som kan ta vakten, hva det betyr for resten av planen og hva
som er usikkert. Faste regler i kode kontrollerer kompetanse, tilgjengelighet,
kollisjoner, hviletid og timetall. Forklaringen gjør resultatet forståelig.
Lederen bestemmer selv, og VaktMatch endrer aldri vaktene.

Det viktigste løftet er at appen **aldri viser et regelbrudd som gyldig**. En
kandidat er bare «oppfyller scenarioreglene» når alle kontroller er bekreftet.
Kjente brudd vises som regelavvik, og manglende data vises som uavklart.

Prosjektet er en studieprototype med syntetiske data for én fiktiv
arbeidsplass. Det skal demonstrere en avgrenset, etterprøvbar arbeidsflyt, ikke
et ferdig bemanningssystem. Det er ikke dokumentert at kombinasjonen er unik i
markedet (se researchrapporten).

**Kjernesetning:** VaktMatch er vellykket hvis en leder på under fem minutter
kan se hvem som kan ta vakten, hva det betyr for resten av planen og hva som er
usikkert, uten at appen noen gang viser et regelbrudd som gyldig.

## 2. Målbruker

### 2.1 Oppgaver brukeren skal få løst

- Finne en erstatter som faktisk oppfyller reglene, raskt og under tidspress.
- Se konsekvensene for andre ansatte og vakter før valget tas.
- Forstå hvorfor en kandidat står øverst, og velge en annen med åpne øyne.
- Se hva som mangler av opplysninger, og hvilken vurdering det hindrer.
- Kunne forklare valget i ettertid.

Problemets hyppighet og mulig tidsbesparelse er ikke validert med målgruppen
(se briefen og researchrapporten).

### 2.2 Ikke målbrukere i førsteversjonen

Ansatte og vikarer som skal motta eller svare på tilbud, HR og lønn, og planleggere
som lager hele turnuser over lengre perioder.

### 2.3 Brukerreiser

Kari er en konstruert eksempelperson, ikke en intervjuet bruker.

- **UJ-1. Kari finner en erstatter før vakten starter.**
  Kari er skiftleder på en fiktiv arbeidsplass. Onsdag kl. 07.00 melder A01 seg
  syk fra vakten 08.00–16.00. Kari åpner VaktMatch på mobilen, velger A01 og
  vakten, og trykker «Simuler fravær». Vakten vises som udekket. Hun trykker
  «Finn alternativer». Sammenligningen viser at A02 og A03 oppfyller
  scenarioreglene, mens A04–A08 har regelavvik og V01 er uavklart. Med P1 står
  A02 først (32 timer mot 40). Kari bytter til P2 og ser at A03 kommer først.
  Hun undersøker A03, leser forklaringen og ser at ingen andre vakter flyttes.
  Hun markerer A03 som valgt. Vaktlisten er uendret; Kari ringer A03 selv.
  **Kanttilfelle:** Kari undersøker A05 og ser at hvilen før vakten bare er
  8 timer (R4). A05 kan ikke velges som bestått alternativ.

- **UJ-2. Ingen direkte erstatter, men én flytting løser det.**
  Som UJ-1, men ingen ledig person oppfyller reglene. Med søkegrense 0 viser
  VaktMatch «Ingen direkte erstatter innenfor scenarioreglene». Kari beholder
  standardgrensen 1 og søker på nytt. Nå vises et forslag der B flyttes fra en
  annen vakt og C dekker vakten B forlater. Begge vakter er dekket og alle
  berørte består R1–R5. Konsekvensene for B og C vises separat.
  **Kanttilfelle:** Ingen kan dekke vakten B forlater. Forslaget vises som
  delvis dekning med den nye udekkede vakten synlig, og rangeres ikke som en
  komplett løsning.

- **UJ-3. En mulig kandidat mangler opplysninger.**
  A02 og A03 er utilgjengelige. V01 har riktig kompetanse, men tilgjengeligheten
  er ikke registrert. VaktMatch viser V01 som uavklart med teksten
  «Tilgjengelighet for V01 må avklares», og sier ikke at ingen kan ta vakten.

- **UJ-4. Sensor kjører appen.**
  Sensor kloner repoet, følger README og starter backend og frontend uten konto
  eller nøkkel. Sensor kjører UJ-1 og UJ-2 med demodataene, prøver feil input
  (for eksempel ingen valgt vakt) og kjører testene slik README beskriver.

## 3. Begreper

Begrepene brukes slik i hele PRD-en.

- **Arbeidsuke** – uke 5 i demoen (12.–18.10.2026), ferdig planlagt.
- **Historikk** – uke 1–4. Vises som kontekst og endres aldri av søket.
- **Nabovakt** – vakt i uke 4 eller uke 6 som påvirker hvile- eller timekontrollen.
- **Målskift** – vakten som mangler bemanning etter et fravær.
- **Udekket behov** – en bemanningsplass på en vakt som ingen aktiv tildeling dekker.
- **Økt** – det aktive besøket i én nettleserfane. Avsluttes når fanen lukkes.
- **Kandidat** – intern ansatt eller forhåndsgodkjent ekstern vikar som undersøkes.
- **Alternativ** – en hypotetisk sluttplan som dekker målskiftet: direkte
  erstatning eller omfordeling med én flytting.
- **Flytting** – en eksisterende, framtidig, ulåst tildeling flyttes til
  målskiftet, og en annen person dekker vakten som blir ledig.
- **Søkegrense** – 0 (bare direkte erstattere) eller 1 (også én flytting). Standard er 1.
- **Kontrollstatus** – *oppfyller scenarioreglene*, *regelavvik* eller *uavklart*.
- **Dekning** – full eller delvis/udekket.
- **Søkestatus** – fullført, avbrutt/feilet eller ikke kjørt – utenfor omfang.
- **Vurderingstidspunkt** – demoens faste «nå». Styrer hva som regnes som påbegynt.
- **Lås** – lederens markering av at en tildeling ikke skal foreslås flyttet.
- **Sorteringskriterium** – P1 (færrest planlagte timer etter tildeling) eller
  P2 (lavest andel av avtalt timetall).
- **Standardforklaring** – regelbasert tekst generert fra kontrollresultatet.
- **KI-forklaring** – tekst fra en språkmodell som bygger på samme grunnlag.
- **Dataversjon** – identifikator for datasettet en vurdering bygger på.

## 4. Funksjoner og krav

Hvert krav har prioritet og Jira-sak. Kontrolltilfellene (S, H, F, D) står i
demoscenarioet og er fasiten for testene.

### 4.1 Datagrunnlag

**Beskrivelse:** Lederen ser arbeidsuken, historikken, ansatte, kompetanser og
bemanningsbehov fra et syntetisk datasett. Datasettet er en versjonert fil.
Realiserer UJ-1 og UJ-4.

#### FR-1: Laste demodatasett (Må · SCRUM-19, SCRUM-20)
Systemet laster et syntetisk datasett med ansatte, vikarer, kompetanser,
tilgjengelighet, vakter for uke 1–6 der det trengs, avtalte timer og dataversjon.
- Datasett som ikke følger datamodellen avvises med en forståelig feilmelding;
  appen krasjer ikke.
- Dataversjonen vises i grensesnittet.
- Datasettet dekker alle kontrolltilfellene som testene bruker.
- Datasettet har 8–10 interne ansatte og minst én forhåndsgodkjent ekstern
  vikar, som i briefens omfang.

#### FR-2: Vise datagrunnlaget (Må · SCRUM-21)
Lederen ser ansatte, vakter og bemanningsbehov for arbeidsuken.
- Udekket behov er synlig uten å åpne detaljer.
- Fungerer på mobil og PC (NFR-2).

#### FR-3: Simulere fravær (Må · SCRUM-22)
Lederen velger en ansatt og en vakt i arbeidsuken og simulerer fravær.
Realiserer UJ-1.
- Den fraværende teller ikke som bemanning, og målskiftet vises som udekket (D1).
- Handlingen endrer ikke datasettfilen.
- Ugyldige valg (ingen ansatt, vakt utenfor uke 5, påbegynt vakt) gir en
  forklarende melding.

### 4.2 Regelkontroll R1–R5

**Beskrivelse:** Regelmotoren kontrollerer hver kandidat mot R1 kompetanse,
R2 tilgjengelighet, R3 kollisjon, R4 minst 11 timer hvile og R5 høyst 40 timer
på sju dager, slik demoscenarioet definerer dem. Dette er produktets viktigste
løfte. Realiserer UJ-1, UJ-2 og UJ-3.

#### FR-4: Kontrollere en kandidat (Må · SCRUM-24, SCRUM-25, SCRUM-26)
Systemet kontrollerer en kandidat mot R1–R5 i den hypotetiske sluttplanen.
- Resultatet for A02–A08 og V01 i hovedeksemplet stemmer med demoscenarioets tabell.
- Grenseverdier stemmer: nøyaktig 11 timer hvile og nøyaktig 40 timer består;
  slutt lik start er ikke overlapp.
- Ved kjent kollisjon vises R3-bruddet, og hvile kan markeres som ikke vurdert.

#### FR-5: Sette kontrollstatus (Må · SCRUM-24)
Systemet gir hver kandidat én kontrollstatus.
- *Oppfyller scenarioreglene* bare når alle fem regler er bekreftet oppfylt.
- *Regelavvik* når minst ett brudd er kjent, også om andre data mangler.
- *Uavklart* når ingen brudd er kjent, men nødvendige data mangler. Det vises
  hvilken kontroll som hindres.

#### FR-6: Ta med nabovakter (Må · SCRUM-56)
Hvile- og timekontrollen bruker nabovakter i uke 4 og uke 6.
- H4 og H5 gir forventet resultat.
- Manglende nabovaktgrunnlag gir uavklart, ikke bestått.

#### FR-7: Vise regelgrunnlaget (Må · SCRUM-24)
Lederen kan se hva hver regel kontrollerer, kilde og begrensning.
- R4 og R5 merkes som forenklede scenarioregler, ikke en garanti for lovlighet.

#### FR-8: Konsekvenser for andre vakter (Må · SCRUM-27)
Systemet beregner timer og hvile etter tildeling for alle berørte ansatte.
- For hver berørt person vises timer før og etter og hvile før og etter.
- Ved flytting (F2) vises konsekvensene for både personen som flyttes og
  personen som dekker vakten som blir ledig.
- A02s timer forblir 24 når A03 undersøkes (demoscenarioet, «Lederen velger»).

### 4.3 Finn alternativer

**Beskrivelse:** «Finn alternativer» søker etter direkte erstattere og, ved
søkegrense 1, omfordeling med én flytting. Søket følger
[forslag ved frafall](../../../../docs/forslag-ved-frafall.md). Realiserer UJ-1 og UJ-2.

#### FR-9: Søke med søkegrense (Må · SCRUM-32, SCRUM-37)
Lederen velger søkegrense 0 eller 1 (standard 1) og starter søket.
- F1–F4 gir forventet resultat.
- Bare komplette alternativer med full dekning og bestått kontroll for alle
  berørte rangeres som løsninger.

#### FR-10: Respektere låser og vurderingstidspunkt (Må · SCRUM-37)
Historikk, påbegynte vakter og låste tildelinger foreslås ikke flyttet.
- Vurderingstidspunktet kommer fra datasettet, ikke maskinens klokke.
- Målskift som har startet, gir søkestatus «Ikke kjørt – utenfor omfang».
- I Må-versjonen kommer låser fra datasettet. At lederen kan låse og låse opp i
  grensesnittet, er Bør (FR-22). Besluttet av Stian 29.10.26.

#### FR-11: Vise dekning og søkestatus hver for seg (Må · SCRUM-31, SCRUM-38)
Systemet viser dekning, kontrollstatus og søkestatus separat.
- Fullført søk uten beståtte alternativer gir «Ingen kontrollerte alternativer
  funnet innenfor valgt søkeomfang», uten påstand om at ingen løsning finnes.
- Delvis dekning viser hvilken vakt som blir udekket (F3).
- Avbrutt søk merkes som ufullstendig.

### 4.4 Sammenligning og prioritering

**Beskrivelse:** Alternativene vises i et fast format. Lederen styrer
sorteringen, undersøker hvem hen vil og velger selv. Realiserer UJ-1.

#### FR-12: Fast svarformat (Må · SCRUM-29, SCRUM-30, SCRUM-34)
Hvert alternativ viser kandidat, kontrollstatus per regel, timer før og etter,
hvile før og etter, konsekvenser for andre og manglende opplysninger.
- Kandidater med regelavvik og uavklart status vises atskilt fra rangerte løsninger.

#### FR-13: Prioritere sorteringskriterier (Må · SCRUM-35)
Lederen aktiverer og ordner P1 og P2. Standard er bare P1.
- S1: P1 gir A02 før A03; P2 gir A03 før A02.
- Endret sortering endrer ikke kontrollstatus eller planen.
- Valgte kriterier vises sammen med rangeringen.

#### FR-14: Lik rangering og manglende sorteringsdata (Må · SCRUM-36)
- S4: like kandidater vises som likeverdige.
- S5: kandidat uten avtalte timer vises utenfor den komplette rangeringen,
  beholder bestått status, og systemet bytter ikke stille til P1.

#### FR-15: Undersøke og velge et alternativ (Må · SCRUM-33, SCRUM-53)
Lederen kan undersøke enhver kandidat, også lavt rangerte og de med avvik, og
markere et alternativ som valgt i den aktive økten.
- Å undersøke eller velge endrer ingen vakter.
- Et alternativ med regelavvik eller uavklart status kan ikke markeres som et
  bestått valg.
- Valget lever bare i økten og forsvinner når fanen lukkes. Lagring er Bør
  (FR-23). Besluttet av Stian 29.10.26.

#### FR-16: Historikk som kontekst (Må · SCRUM-55)
For hver kandidat vises relevant historikk fra uke 1–4 med kilde og periode.
- Historikken endrer ikke sortering eller status (H1).
- Ufullstendig historikk vises som mangel (H2).

### 4.5 Forklaring

**Beskrivelse:** Forklaringen gjør kontrollresultatet og prioriteringen
forståelig. Standardforklaringen finnes alltid. KI-forklaringen er én avgrenset
handling som bygger på det samme grunnlaget. Realiserer UJ-1.

#### FR-17: Standardforklaring (Må · SCRUM-40)
Systemet genererer en regelbasert forklaring av rangering, avvik og manglende
data, uten KI-nøkkel.
- Tall, statuser og prioriteringer i teksten er identiske med kontrollresultatet.
- Teksten sier at vaktene ikke er endret.

#### FR-18: KI-forklaring av valgt alternativ (Må · SCRUM-39, SCRUM-59)
Lederen ber om en KI-forklaring av alternativet hen undersøker, sammenlignet
med det øverst rangerte.
- Modellen får bare kontrollresultatet, prioriteringen og relevante data som input.
- Svaret har faste felt: kort svar, avveining, konsekvenser og usikkerhet.
- Testene kjører med en testmodus uten modellkall og uten nøkkel.
- Handlingen er «Forklar forskjellen» fra demoscenarioet (besluttet av Stian
  29.10.26). Modell og leverandør avgjøres i SCRUM-59.

#### FR-19: KI endrer aldri grunnlaget (Må · SCRUM-41)
- KI-forklaringen kan ikke endre status, rangering eller valg.
- Uten nøkkel, ved tidsavbrudd eller ved modellfeil vises standardforklaringen,
  og brukeren får vite det.
- En test sjekker at tall og statuser i KI-svaret samsvarer med kontrollresultatet.

### 4.6 Utvidelser (Bør)

Disse bygges når kjernen (FR-1 til FR-19) fungerer og er testet. Begrunnelse i §7.2.

#### FR-20: Simulere tilbud og svar (Bør · SCRUM-52)
Tilbud sendt, venter, akseptert og avslått for valgt alternativ, som i F5–F7.
Ingen status endrer vakter.

#### FR-21: Laste oppdaterte data med endringsoversikt (Bør · SCRUM-23, SCRUM-57)
Bytte til et forhåndslaget datasett, vise endringer og vurdere på nytt, som i D2–D4.

#### FR-22: Låse tildelinger i grensesnittet (Bør · SCRUM-37)
Lederen låser og låser opp framtidige tildelinger; tidligere søk blir utdatert.

#### FR-23: Varig beslutningslogg (Bør · SCRUM-54)
Valgfri, avslått som standard, frivillig begrunnelse, som i D5–D7.

## 5. Tverrgående ikke-funksjonelle krav

- **NFR-1 Lokal kjøring (Må · SCRUM-48):** En person uten kjennskap til
  prosjektet starter appen etter README på en ren maskin på under 20 minutter,
  uten konto eller nøkkel. README har forutsetninger med versjoner, kopierbare
  kommandoer, `.env.example`, testkommandoer, skjermbilde og lenker til planene.
- **NFR-2 Tilgjengelighet og skjermstørrelser (Må · SCRUM-42, SCRUM-47):**
  Tekstkontrast minst 4,5:1 (WCAG 2.1 AA). Alle handlinger kan utføres med
  tastatur, med synlig fokus. Alle skjemafelt har etikett. Hver visning har en
  tomtilstand og feilmelding som sier hva brukeren kan gjøre. Fungerer fra 360 px
  bredde (mobil) til PC uten vannrett rulling. Status vises med tekst, ikke bare
  farge. En UX-spesifikasjon med skisser ligger i repoet før grensesnittet bygges.
- **NFR-3 Robusthet:** API-et validerer all input og svarer på ugyldige
  forespørsler med en feilkode og en norsk melding, aldri med en uhåndtert feil.
  Grensesnittet viser meldingen og en vei videre. Når backend ikke svarer, sier
  grensesnittet det. Ende-til-ende-testen prøver minst én ugyldig handling og
  én gjentatt handling.
- **NFR-4 Testbarhet (Må · SCRUM-28, SCRUM-43):** Regelmotoren har automatiske
  tester for alle kontrolltilfellene i demoscenarioet og metodebeskrivelsen.
  Minst én ende-til-ende-test går gjennom UJ-1. CI kjører alle tester på pull
  requests.
- **NFR-5 Determinisme:** Samme datasett, fravær, søkegrense og prioritering gir
  alltid samme resultat, uavhengig av maskinens klokke.
- **NFR-6 Hemmeligheter:** Nøkler leses fra miljøvariabler og ligger aldri i
  repoet eller historikken.
- **NFR-7 Ytelse (SCRUM-58):** Ingen responstid loves. Søketid med grense 0 og 1
  måles og dokumenteres før større søkeomfang vurderes.
- **NFR-8 Sporbarhet (Må · SCRUM-44):** Hvert FR har Jira-sak; commits viser til
  saken; avvik fra PRD-en føres i PRD-ens memlog og ved behov i endringsloggen.
  KI-bruk og funn i kodegjennomgang dokumenteres med kobling til konkrete endringer.
- **NFR-9 Språk:** Grensesnitt og forklaringer er på norsk bokmål.

## 6. Ikke-mål

- VaktMatch gjennomfører ikke vaktendringer og sender ikke ekte tilbud.
- Ingen chat eller friteksttolkning.
- Ingen generering av hele turnuser eller planlegging over lengre perioder.
- Ingen reelle persondata, innlogging, roller eller integrasjoner med HR- og turnussystemer.
- Ingen garanti for at en plan er lovlig. R4 og R5 er forenklede scenarioregler.
- Ingen solver og ingen påstander om «optimal» eller «bevist uløselig».
- Ingen produksjonsdrift eller hosting i førsteversjonen.

## 7. Omfang

### 7.1 Førsteversjon

**Må:** FR-1 til FR-19 og NFR-1 til NFR-6, NFR-8 og NFR-9. Det gir én
sammenhengende flyt: datagrunnlag → simulert fravær → finn alternativer
(grense 0–1) → sammenligning med R1–R5, konsekvenser og manglende data →
prioritering og undersøkelse → standard- og KI-forklaring.

**Bør:** FR-20 til FR-23, i den rekkefølgen, når kjernen er testet.

**Utenfor:** Se §6.

### 7.2 Endringer fra product brief

| Hva | I briefen | I PRD-en | Begrunnelse og opphav |
|---|---|---|---|
| Simulert tilbud og aksept | Del av førsteversjonen og suksesskriteriene. | Bør (FR-20). | Kjernen må fungere og være testet først. Fristen er ukjent, og gruppen er to. Stian besluttet prioriteringen 29.10.26 etter forslag fra Claude Code; Odin er ikke konsultert ennå. |
| Datasettbytte med endringsoversikt | Del av førsteversjonen og suksesskriteriene. | Bør (FR-21). | Som over. |
| Varig beslutningslogg | Valgfri funksjon i MVP. | Bør (FR-23). | Som over. |
| Lederlåser i grensesnittet | Lederen kan låse tildelinger. | Låser fra datasettet er Må; låsing i grensesnittet er Bør (FR-22). | Holder kjernen liten. Foreslått av Claude Code, besluttet av Stian 29.10.26. |
| KI-forklaring | KI forklarer avveininger, konsekvenser og usikkerhet. | Én avgrenset KI-handling (FR-18) i tillegg til standardforklaringen. | Researchen fant ingen påvist merverdi av KI-tekst; handlingen skal kunne sammenlignes med standardteksten. Del av Stians beslutning 29.10.26. |

Briefen og endringsloggen må oppdateres når prioriteringen er avklart med Odin.

## 8. Suksessmål

**Primære**
- **SM-1 Ingen falske «oppfyller scenarioreglene»:** 0 av alle kontrolltilfellene
  gir bestått status til en kandidat som bryter en regel eller mangler data.
  Validerer FR-4, FR-5, FR-6.
- **SM-2 Kjerneflyten fungerer fra start til slutt:** UJ-1, UJ-2 og UJ-3 kan
  gjennomføres med demodataene og dekkes av automatiske tester. Validerer FR-1 til FR-17.
- **SM-3 Sensor får appen til å kjøre:** En person utenfor gruppen følger README
  på en ren maskin og kjører UJ-1 på under 20 minutter. Validerer NFR-1.

**Sekundære**
- **SM-4 Forklaringer følger dataene:** Alle tall og statuser i standard- og
  KI-forklaringen stemmer med kontrollresultatet i testsettet. Validerer FR-17 til FR-19.
- **SM-5 (valgfri) Forståelse og tid:** En testbruker kan forklare en avveining,
  en konsekvens og manglende informasjon i S1, og gjennomfører UJ-1 på under fem
  minutter (SCRUM-45). Sammenlign gjerne standardtekst og KI-tekst.

**Mål vi ikke skal optimalisere for**
- **SM-C1 Antall funksjoner:** Flere halvferdige funksjoner teller mindre enn en
  testet kjerne. Motvekt til omfang i briefen.
- **SM-C2 Hvor flytende eller overbevisende KI-teksten er:** Researchen viser at
  forklaringer kan øke tillit også når rådet er feil. Motvekt til SM-5.
- **SM-C3 Flest mulig alternativer:** Reglene skal ikke mykes opp for å vise flere
  løsninger. Motvekt til SM-2.

## 9. Åpne spørsmål

| Nr. | Spørsmål | Ansvarlig | Tas opp igjen |
|---|---|---|---|
| 1 | Hva er sluttfristen for kode og refleksjonsrapport? Den avgjør hvor mye av Bør som er realistisk. | Odin (SCRUM-49) | Når faglærer svarer. |
| 2 | Slutter Odin seg til Må/Bør-delingen og endringene i §7.2? | Odin (SCRUM-46) | Før briefen og endringsloggen oppdateres. |
| 3 | Hvilken modell og leverandør, og hvilken kostnadsgrense? | Odin (SCRUM-59) | Før FR-18 implementeres. |
| 4 | Hvordan modelleres en ekstern vikars øvrige arbeid? | Stian (SCRUM-19) | I datamodellen. |
| 5 | Hvilken type skiftleder skal scenarioet være troverdig for? | Begge | Ved UX-spesifikasjonen (SCRUM-47). |

## 10. Antakelser

Ingen gjenstående. Antakelsene i utkastet om låser (FR-10), økt (FR-15) og
KI-handling (FR-18) ble besluttet av Stian 29.10.26.
