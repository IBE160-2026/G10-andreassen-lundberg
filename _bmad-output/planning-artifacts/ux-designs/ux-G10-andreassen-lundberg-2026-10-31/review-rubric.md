# Gjennomgang av UX-kontraktene – VaktMatch

Utført av Codex 08.11.2026 etter rubric walker i `bmad-ux/references/validate.md`.
De tre DESIGN-eksemplene og de to EXPERIENCE-eksemplene i skillen er lest.
Kontrollen gjelder dokumentparet, ikke app, regelmotor, modell eller brukertest.

## Samlet vurdering

Dokumentparet gir et sammenhengende grunnlag for videre implementering, med
tydelig opphav og avgrensning. Alle fire PRD-reiser og de relevante
resultatdimensjonene har flater og tilstander. Tre middels alvorlige
presisjonsfunn ble rettet og lest tilbake under gjennomgangen. Ingen
kritiske eller høye funn er registrert, og ingen innholdsfunn står åpne.

Alle fire statiske nøkkelskjermer og den klikkbare prototypen er levert og
kildekontrollert. [Siste kontrollkjøring](.working/verification-results.json)
har 95 beståtte kontroller og ingen feil, inkludert nettleser-, tilgjengelighets-
og interaksjonskontroller. Det er kontroll av UX-artefaktene, ikke bevis for
ferdig regelmotor, fullstendig datasett eller appverifikasjon.

## 1. Flytdekning — strong

EXPERIENCE.md, [Key Flows](EXPERIENCE.md#key-flows), gjengir PRD-ens fire
UJ-titler ordrett. Hver har nummerert rekkefølge, konkret avklaring og
feil-/kantvei. Kari er korrekt merket konstruert, og Sensor følger PRD-rollen.
Ukesoversikt, fravær, alternativer, detaljer, valg/tilbud og datagrunnlag har
innganger; tidligere valg har en angitt seksjonsinngang.

«Simuler fravær» og «Finn alternativer» er separate handlinger som krevd av
PRD UJ-1/FR-3 og demoscenario D1. Periodeoversikten registrerer ikke automatisk
fravær på alle berørte vakter, og hvert søk gjelder ett målskift. Nattvakter
vises hele med datoer; påbegynte vakter er synlige, men ikke valgbare.
Dagfeltet gjøres ikke til en prognose for sykdom eller egenmeldingsrett.

### Funn

Ingen utestående funn i denne kategorien.

## 2. Tokenfullstendighet — strong

DESIGN.md har 16 konkrete hex-farger og 19 navngitte komponenttokenobjekter.
YAML er lest maskinelt. Alle 33 unike tokenreferanser i DESIGN.md og alle tre
i EXPERIENCE.md peker på definerte verdier eller definerte tokengrupper.
Alle nødvendige tokenkategorier er til stede; ingen UI-systemarv brukes til
å skjule manglende verdier.

Kontrast er regnet fra de definerte hexverdiene: hovedtekst 13,39:1 eller
bedre, sekundærtekst minst 5,73:1, primærhandling 11,97:1 og statuspar minst
6,29:1. Fokus mot lyse flater er minst 6,17:1; kontrollgrense minst 3,79:1.
Dette kontrollerer tokenparene, ikke alle faktiske kombinasjoner i HTML eller app.

### Funn

Ingen utestående funn i denne kategorien.

## 3. Komponentdekning — strong

De 19 produktkomponentene i [DESIGN.Components](DESIGN.md#components) har
samme navn og samme antall rader i
[EXPERIENCE.Component Patterns](EXPERIENCE.md#component-patterns).
Visuelle spesifikasjoner og atferd er skilt. Native `select`, radio og
knapper brukes som interaksjonsprimitiver uten ny komponentbibliotekavhengighet.

Kort og detaljflate skiller undersøkelse fra øktvalg. Før/etter inkluderer
alle berørte vakter/personer ved én flytting. Tilbud, økthistorikk og
datasettbytte har egne regler fremfor å bli implisitte følger av et kortklikk.

### Funn

Ingen utestående funn i denne kategorien.

## 4. Tilstandsdekning — strong

[State Patterns](EXPERIENCE.md#state-patterns) dekker oppstart, tomme flater,
inputfeil, backendfeil, gjentatt handling, endret utkast, ventende/avbrutt søk,
lik rangering, manglende sorteringsdata, utdatert grunnlag, regelavvik,
kostnads-/historikkmangel, KI-reserve, tilbudssvar og datasettfeil.
Fokus og tilbakeføring er spesifisert i Interaction Primitives.
Innlogging/roller finnes ikke i førsteversjonen; en egen tilgangsfeil er derfor
ikke en manglende flate. Offline er avgrenset til lest kontekst og forståelig
backendfeil, uten løfte om synkronisering.

### Rettet under kontrollen

- **[medium, rettet] Sammenligning uten referanse var udefinert.** Den første
  versjonen av `explanation-panel` beskrev bare sammenligning mot øverst
  rangert, selv når resultatet bare kunne inneholde avvik, uavklarte eller
  ikke rangerbare funn. Det kunne gitt implementeringen en oppdiktet referanse.
  **Rettelse:** EXPERIENCE.md, Component Patterns, `explanation-panel`, har nå
  «Ingen rangert referanse på dette grunnlaget» som begrunnelse for utilgjengelig
  sammenligningshandling, mens standardforklaringen beholdes. Ved avbrutt søk
  avgrenses referansen uttrykkelig til foreløpige funn. Rettelsen er lest tilbake.

Ingen utestående funn i denne kategorien.

## 5. Visuell referansedekning — strong

DESIGN.md lenker inline til de fire statiske nøkkelskjermene og
prototypen. EXPERIENCE.md knytter de samme referansene til relevante IA-flater;
tilbud, datagrunnlag og historiske valg vises i prototypen. Tidligere valg er spesifisert
som en seksjon med atferd/tilstander, uten krav om egen statisk referanse.
Begge dokumentene fastsetter at dokumentparet gjelder foran mockups.

[Ukesoversikt](mockups/key-ukeplan.html), [fravær](mockups/key-fravaer.html),
[alternativer](mockups/key-alternativer.html), [detaljer](mockups/key-detaljer.html)
og [prototype](mockups/prototype.html) er lest. Samtlige fem filer har lenke fra
begge kontraktene; ingen mockfil er uten dokumentreferanse og ingen mocklenke
er brutt. De fire statiske filene inneholder ingen script og lenker tydelig
videre til prototypen.

S1-lignende A02/A03-eksempler står atskilt fra det egne M01/PART-flytteeksemplet,
uten felles rangering eller påstand om ferdige F2-demodata. Kontroll, dekning,
rangering, øktvalg og tilbudssvar er navngitte størrelser. Nye kostnadsbeløp
er merket illustrative, med eget synlig regnestykke. Ingen regelmotor eller
modell er tilkoblet. Kalenderperioden forhåndsviser hele overlappende vakter;
én vakt simuleres om gangen, og andre målskift enn onsdagens morgenvakt får
en uttrykkelig avgrensning uten gjenbruk av onsdagens kontrollresultater.

Nettleserkontrollen i Chromium 145 og åtte axe 4.10.3-kjøringer er registrert i
[kontrollresultatet](.working/verification-results.json). Blant kontrollene er
tolv flate-/breddekombinasjoner, interaksjoner, kontrastpar, versjonsbytte og
regresjon for låst målskift. Ingen ny nettleserkjøring er utført av denne
kildegjennomgangen etter at resultatfilen ble lest.

### Funn

Ingen utestående funn i denne kategorien. Kildepresiseringene som ble rettet
etter første mockleveranse er bevart i kategori 7.

## 6. Omfang og presisjonsnivå — strong

Tabeller samler komponenter, tilstander og flater. Kildene eier omfang,
regeldefinisjoner og beregningsformler; kontraktene eier hvordan resultatene
presenteres og brukes. Kildegrunnlaget er lenket uten å kopiere hele PRD-en.
Tall, personbilder, dekorative illustrasjoner og nye apptjenester brukes ikke
som unødvendige forutsetninger. Desktop- og mobiloppførsel er konkret nok til
å implementere uten å låse hele grensesnittet til faste pikselhøyder.

### Funn

Ingen utestående funn i denne kategorien.

## 7. Kildearv og begreper — strong

Alle seks `sources`-stier i hvert dokument finnes. Ordlyden for kontroll,
dekning og søk er i samsvar med PRD/metodebeskrivelsen. Kjent brudd har forrang
for datamangel; «Ikke vurdert» er en regelrad, ikke ny samlet kontrollstatus.
Beståtte uten sorteringsdata skilles fra komplette rangeringer, og likhet
gjøres ikke til et faglig skille gjennom stabil ID-rekkefølge.

P1/P2 beholdes som aktive kriterier med synlig rekkefølge, bare P1 som
standard og minst ett aktivt kriterium. Metrikkene og leksikografisk
sortering arves fra PRD og demoscenarioet, ikke fra illustrative mocktall.
Kostnad og historikk blir ikke nye skjulte rangeringskriterier.

Tilbud krever svar fra alle berørte ved omfordeling. Nytt datasett arver ikke
aksept; gamle valg/svar blir historiske. Neste fravær bruker gjeldende data
og tidligere simulerte fravær, uten å behandle et valgt forslag som innført
bemanning. Codex sine detaljvalg er uttrykkelig knyttet til Odins mandat;
ingen felles detaljgodkjenning eller reell brukertest utledes.

### Rettet under sluttkontrollen

- **[medium, rettet] Lås ble brukt til å blokkere fravær.** Første mockversjon
  deaktiverte fredagens målskift fordi tildelingen var låst. Det stred mot
  [metodebeskrivelsens «Hva ligger fast?»](../../../../docs/forslag-ved-frafall.md#hva-ligger-fast),
  der en lås ikke skal skjule fravær eller udekket behov. **Rettelse:**
  `absence`, `affectedHTML` og simuleringens validering i prototype.html
  tillater nå fravær på låst, ikke påbegynt målskift. Låseteksten forklarer
  forskjellen fra flyttebeskyttelse; ukeoversikten viser også fredagens nye
  udekkede behov. EXPERIENCE.md, `affected-shifts`, presiserer regelen.
  Rettelsen er lest tilbake og dekkes av regresjonskontroller i resultatfilen.
- **[medium, rettet] Eksternt kontrollgrunnlag var tvetydig.** Første
  historikkhjelpetekst sa generelt at eksterne kandidaters øvrige arbeid ikke
  var bekreftet, samtidig som d2-eksemplet kunne vise V01 som bestått.
  Manglende nødvendig kontrollgrunnlag skal gi Uavklart, jf. PRD FR-5/6.
  **Rettelse:** Prototype.html og de regenererte statiske referansene sier
  nå at eksemplet illustrerer komplett kontrollgrunnlag for viste vakter og
  nabovakter; modelleringen av eksternt arbeid følges i SCRUM-19, og nødvendig
  datamangel skal gi Uavklart i appen. Dette er ikke en påstand om innhentet
  arbeidsinformasjon eller ferdig datamodell. Rettelsen er lest tilbake.

Ingen utestående funn i denne kategorien.

## 8. Dokumentform — strong

DESIGN.md følger de åtte kanoniske seksjonene i riktig rekkefølge.
EXPERIENCE.md har alle obligatoriske seksjoner og Responsive & Platform.
Ingen kilde eller avklaring velger et referanseprodukt eller avviser en
bestemt konkurrents design; en egen Inspiration & Anti-patterns-seksjon er
derfor ikke påkrevd. Handoff og kontrollgrenser har en konkret mottaker og
avgrenser hva ferdig UX faktisk betyr.

### Funn

Ingen utestående funn i denne kategorien.

## Mekaniske merknader og kontrollgrenser

- Ingen udefinerte tokenreferanser, manglende kildefiler eller komponentnavnavvik.
- Alle fire UJ-titler er bevart ordrett. Mermaid finnes ikke i dokumentparet.
- Dokumentstatus `final` er eksplisitt avgrenset fra appverifikasjon og godkjenning.
- Alle fem mockfiler finnes og har referanser fra begge kontraktene.
  Det faktiske responsive oppsettet og utvalgte prototypeinteraksjoner er
  kontrollert gjennom [kontrollskriptet](.working/verify-ux.py) og det lenkede resultatet.
- Full UJ-2-søkemotor og den ferdige appens øvrige Må-kontroller er uttrykkelig
  senere implementeringsarbeid. De er ikke utestående leveranser i UX-oppdraget.
- Registrerte innholdsfunn: 0 kritiske, 0 høye, 3 middels (alle rettet), 0 lave.
  Utestående innholdsfunn etter sluttkontroll: 0.
