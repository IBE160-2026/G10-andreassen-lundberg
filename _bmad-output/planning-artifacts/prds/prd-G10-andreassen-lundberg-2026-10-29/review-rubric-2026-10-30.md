# PRD-gjennomgang – VaktMatch, 30.10.2026

Skrevet av Codex etter lesing av hele [PRD-en](prd.md),
[kostnadsanslaget](../../../../docs/kostnadsanslag.md) og den installerte
BMAD-rubrikken `prd-validation-checklist.md`. M1–M2 er kontrollert mot
[demoscenarioet](../../../../docs/demoscenario-fravaer.md). Gjennomgangen er
kalibrert til en avgrenset dokumentoppdatering for en studieprototype; den er
ikke en kjøretest, brukertest eller bekreftelse på produktets effekt. Den eldre
[gjennomgangen fra 29. oktober](review-rubric.md) er bevart.

## Samlet vurdering

PRD-en gir et brukbart grunnlag for den valgte komplette demoflyten: tilbud,
oppdaterte data, nye fravær og kostnad følger samme avgrensede beslutningsstøtte.
Ambisjoner om tid, fordeling og økonomi skilles fra dokumentert effekt, og
forslag eller simulert aksept fremstilles ikke som gjennomførte tildelinger.
Avstemmingen av NFR-4 mot utsatte Bør-funksjoner ble rettet og kontrollert i
denne gjennomgangen. Ingen kritiske eller høye funn gjenstår i den avgrensede
oppdateringen; kjøretester og produktvalidering gjenstår som eget arbeid.

## Beslutningsgrunnlag – adequate

§7.2 viser tidligere og nåværende prioritering, begrunnelse, dato og opphav.
Odins valg av sekvensielle fravær og syntetisk kostnadsanslag er synlige;
formelen er særskilt merket som Codex sin konkretisering. §9 gir ansvar og
tidspunkt for reelle åpne spørsmål om frist, oppgavesamordning, modellvalg,
ekstern vikars arbeid og målbruker. Dette er tilstrekkelig til å fortsette
planleggingen uten å fremstille alle detaljer som felles godkjent.

## Innhold fremfor pynt – strong

Én navngitt eksempelperson er merket som konstruert. §1 merker raskere arbeid,
fair fordeling, tryggere beslutninger og økonomiske avveininger som ønsket
merverdi uten dokumentert effekt. FR-24 presiserer at P1/P2 og historikk ikke
utgjør en full rettferdighetsmodell. Ingen ny unikhets-, lønns- eller juridisk
garanti er innført.

## Strategisk sammenheng – adequate

FR-20/21 er Må fordi den valgte demoen skal vise hele avklaringsflyten, mens
varig lagring og lederlåser kan vente. Kostnad er et ekstra
sammenligningsgrunnlag; den overtar verken regelstatus eller P1/P2. SM-2 dekker
oppdatert flyt og M1–M2, og SM-6 knytter økonomien til kontrollerbare beløp og
manglende grunnlag. SM-5 er fortsatt valgfri: femminuttersmålet i visjonen er
dermed en ambisjon, ikke dokumentert tidsgevinst eller en obligatorisk
brukertest. Dette er akseptabelt for den avtalte studieprototypen.

## Tydelig «ferdig» – adequate

FR-3, FR-15 og FR-20/21 skiller fravær, øktvalg, simulert aksept og faktisk
datagrunnlag. M1 krever ny kontroll etter en oppdatering; M2 viser at aksept
ikke reserverer ansatte eller beviser samlet dekning. FR-24 og O1–O5 fastsetter
referanse, alle berørte vakter, sats/tillegg, avrunding, ny dataversjon og
ufullstendig grunnlag. Eksempelbeløpene kan etterregnes: O1 gir 1 800 NOK, O2
gir differanse 1 640 NOK, og O5 gir 1 650 NOK samt 200,01 NOK.

### Funn

- **medium, rettet – Testomfanget omfattet den utsatte loggfunksjonen** (§5
  NFR-4 mot FR-23 og §7.1): Den første ordlyden «alle kontrolltilfellene i
  demoscenarioet» omfattet også D6–D7, som FR-23 legger til Bør. NFR-4 er nå
  kontrollert på nytt: obligatorisk testing gjelder Må-tilfellene og O1–O5;
  D6–D7 og andre Bør-tilfeller testes når funksjonene bygges. Produktomfanget
  er bevart. Ved nedbryting i testsaker bør grensesnitt- og økttilfeller
  plasseres på relevante testnivåer selv om NFR-4 innledes med «regelmotoren».

## Ærlig avgrensning – strong

FR-3 og §7.1 sier ett målskift om gangen og utsetter samlet løsning for flere
fravær. FR-20 sender ingen ekte tilbud. FR-21 bruker et begrenset sett
forhåndslagde datasett. FR-24 og kostnadsnotatet avgrenser beløpene fra reell
lønn, overtid, tariff, fraværskostnad og full arbeidsgiverkostnad; en kjent
delsum får ikke bli et komplett totalanslag. §6 avviser garanti om lovlighet.
Researchen brukes til å holde KI-nytten åpen, uten å hevde at den beviser et
bestemt antall KI-handlinger.

## Bruk videre i UX, arkitektur og stories – adequate

Begrepslisten skiller kontrollstatus, dekning, søkestatus og dataversjon.
FR-24s «kostnad uavklart» påvirker ikke kontrollstatus, og kostnadsnotatet
krever at delvis dekning eller regelavvik vises ved siden av beløpet. UJ-1 og
UJ-3 viser versjonsavhengig valg og svar, slik at UX og datamodell kan hente
konkrete tilstandsoverganger. NFR-4-funnet er rettet og kontrollert.
Oppgavesamordning er allerede et åpent punkt i §9.

## Form – strong

Fire korte brukerreiser er passende for et produkt med meningsfull UX og en
egen lokal oppstart for sensor. De nummererte kravene og de separate
kontrolltilfellene gir nok presisjon uten en full modell av lønn eller
samtidig bemanningsoptimalisering. Ingen større omstrukturering er nødvendig
for denne oppdateringen.

## Mekaniske merknader

- FR-1–24, NFR-1–9, UJ-1–4 og SM-1–6 har entydige ID-er; SM-6 er plassert
  blant de primære målene foran SM-3. Dette er ikke et sporbarhetsproblem.
- Ingen `addendum.md` finnes i denne PRD-mappen. Kostnadsnotatet er det
  relevante nye støttevedlegget og er lenket fra FR-24.
- Ingen nye inline-antakelser er innført. Kjente uløste valg står i §9;
  syntetiske beregningsdetaljer er merket med opphav i FR-24 og notatet.
- FR-24 er koblet til SCRUM-60 i den ferdigstilte PRD-teksten.
- Gjennomgangen endrer ingen produktkrav. Den er grunnlag for retting av
  testordlyden og videre planlegging, ikke en beslutning om å lukke SCRUM-46.
