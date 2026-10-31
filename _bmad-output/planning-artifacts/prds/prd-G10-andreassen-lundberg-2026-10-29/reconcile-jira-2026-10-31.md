# Avstemming av PRD mot Jira – SCRUM-46

*(Utført av Codex · 31.10.2026. Kilde: [PRD](prd.md), gjeldende repo og
et uttrekk av alle 60 SCRUM-saker hentet 31.10.2026. Dette dokumentet beskriver
førtilstanden og nødvendige rettelser; hovedoppfølgingen i SCRUM-46 viser hva
som faktisk er oppdatert. Ingen appkode eller tester er kjørt her.)*

## Resultat

Alle 24 funksjonelle krav har minst én eksisterende sak. Det er ikke behov for
en ny produktsak bare for å dekke et manglende FR. Derimot er flere eksisterende
sakstekster eldre eller mindre presise enn PRD-en, og fire NFR mangler
uttrykkelig saksreferanse i PRD-en. Rettelsene nedenfor samordner vedtatt omfang
og eksisterende KI-konkretiseringer; de er ikke nye produktbeslutninger.

## Dekning av funksjonelle krav

| PRD | Eksisterende saker | Avstemming som trengs |
|---|---|---|
| FR-1 | SCRUM-19/20 | Versjonert og validert datagrunnlag, kostnadsfelt og nye kontrolltilfeller må inn i kriteriene. |
| FR-2 | SCRUM-21 | Dekket; mobil/PC følger NFR-2 og SCRUM-42. |
| FR-3 | SCRUM-22 | Sekvensielle fravær er innarbeidet. Legg til ugyldige valg, uendret datasettfil og avtalt felles feilhåndtering. |
| FR-4 | SCRUM-24/25/26 | Legg inn navngitte R1–R5 og grenseverdier i relevante saker; unngå å behandle «3–5 regler» som fortsatt åpent. |
| FR-5 | SCRUM-24 | Samlet kontrollstatus og forrang ved kjent brudd mangler i kriteriene. |
| FR-6 | SCRUM-56 | Dekket; henvis H4/H5 og testsuiten. |
| FR-7 | SCRUM-24 | Dekket i tema; presiser de fem valgte reglene og begrensningene. |
| FR-8 | SCRUM-27 | Legg til før/etter for timer og hvile for hver berørt person, også begge personer ved flytting. |
| FR-9/10 | SCRUM-32/37 | Søk og fast vurderingstidspunkt er dekket. Skill datasettlåser som Må fra låsing i grensesnittet som Bør. |
| FR-11 | SCRUM-31/38 | Dekket. SCRUM-38 skiller dekning, kontroll og søk. |
| FR-12 | SCRUM-29/30/34 | Tema og manglende data er dekket; legg til timer før/etter og skillet mellom rangerte løsninger og avvik/uavklarte. |
| FR-13/14 | SCRUM-35/36 | Erstatt henvisninger til en ventende avklaring med P1/P2, P1 som standard, S1/S4/S5 og ingen stille fallback ved manglende P2-data. |
| FR-15 | SCRUM-33/53 | Undersøkelse er dekket; presiser gyldig øktvalg, fanens levetid og historikk på gammel dataversjon ved D8. |
| FR-16 | SCRUM-55 | Legg til kilde/periode og synlig mangel ved ufullstendig historikk (H2). |
| FR-17 | SCRUM-40 | Dekket i tema; krev identiske beregnede tall og tydelig beskjed om at vaktene ikke er endret. |
| FR-18 | SCRUM-39/59 | Modellvalg har egen sak; avgrens SCRUM-39 til «Forklar forskjellen», faste felt, testmodus og tilfelle der undersøkt alternativ allerede er øverst. |
| FR-19 | SCRUM-41 | Legg til bevart valg, nøkkelløs kjøring/timeout/modellfeil og eksplisitt varsel om standardforklaring, samt kontroll av tall og statuser. |
| FR-20 | SCRUM-52 | Må-omfanget og F5–F7 er innarbeidet. |
| FR-21 | SCRUM-23/57 | Må-omfang, ny vurdering, D8 og kostnad på ny dataversjon er innarbeidet. |
| FR-22 | SCRUM-37 | Samme sak som FR-9/10; merk grensesnittdelen Bør separat. |
| FR-23 | SCRUM-54 | Bør-avgrensningen er innarbeidet; historisk kildereferanse E30 bør suppleres med gjeldende E35. |
| FR-24 | SCRUM-60 | Dekket; avhenger uttrykkelig av SCRUM-19/20. Kostnadsgrunnlag og fasit må følges opp der. |

## Dekning av ikke-funksjonelle krav

| PRD | Saksdekning | Nødvendig presisering |
|---|---|---|
| NFR-1 | SCRUM-48 | Ta inn under 20 minutter og README-innholdet som må kunne kontrolleres. |
| NFR-2 | SCRUM-42/47 | Ta inn 360 px, ingen vannrett rulling, 4,5:1 kontrast, tastatur/fokus, etiketter, tekststatus og tom-/feiltilstander. |
| NFR-3 | SCRUM-22/43 | Mangler referanse i PRD. SCRUM-22 skal levere feilkode/norsk melding ved første input-endepunkt, jf. Odins valg 29.10 i rotmemlog; SCRUM-43 verifiserer ugyldig og gjentatt handling samt backendfeil. |
| NFR-4 | SCRUM-28/43, SCRUM-60 for O1–O5 | Avgrens til Må-tilfeller; D6–D7 testes når Bør bygges. SCRUM-43 må kreve minst én automatisert UJ-1 og dekke UJ-2/3 samt F5–F7, D2–D5/D8 og M1–M2. |
| NFR-5 | SCRUM-37/28 | Mangler referanse i PRD. Fast demo-tidspunkt finnes i SCRUM-37; krev test av samme datasett/fravær/grense/prioritering med samme resultat. |
| NFR-6 | SCRUM-18/59/48 | Mangler referanse i PRD. Sakene dekker miljøvariabel og nøkkelløs kjøring; bevar dette og verifiser at hemmeligheter ikke følger leveransen. |
| NFR-7 | SCRUM-58 | Dekket med måling av grense 0 og 1 uten responstidsløfte. |
| NFR-8 | SCRUM-44 | Ta inn kobling krav–sak–commit–kontrollbevis og arbeidslogg etter AGENTS.md. Dette er en eksisterende prosessregel. |
| NFR-9 | SCRUM-42/39/40 | Mangler referanse i PRD og eksplisitt bokmålskriterium i sakene. Suppler de respektive UI-/forklaringssakene. |

## Presis endringsliste for Jira

1. **SCRUM-19/20:** Modell og demodata må støtte dataversjon, fast
   vurderingstidspunkt, låser, stabile ID-er, avtalte timer og eksplisitt manglende
   grunnlag. Ta inn syntetiske satser, versjonerte tilleggsregler og nødvendige
   tidsintervaller etter FR-24/[kostnadsanslaget](../../../../docs/kostnadsanslag.md).
   SCRUM-20 må dekke alle Må-kontrolltilfellene, inkludert M1–M2 og O1–O5,
   med forventet resultat. Laster/validering må avvise ugyldige data uten krasj
   etter FR-1. Den konkrete kodefordelingen kan følge modulgrensene i SCRUM-18;
   dette er leveransekrav, ikke krav om å samle alt i én modul.
2. **SCRUM-24/25/26:** Navngi R1–R5, statusene og kildegrunnlaget.
   SCRUM-24 må gi samlet «regelavvik» ved minst ett kjent brudd, selv om andre
   data mangler; «uavklart» når ingen brudd er kjent, men grunnlag mangler;
   bestått først når alle regler er bekreftet. Test 11 timer/40 timer som
   beståtte grenser, slutt lik start uten overlapp og kjent kollisjon med
   eventuell hvile ikke vurdert, etter FR-4/5 og demoscenarioet.
3. **SCRUM-27/30:** Før/etter-tall og alle berørte i omfordeling må fremgå.
   Undersøkelse av A03 endrer ikke A02s timer. Avvik og uavklarte kandidater
   skal vises atskilt fra rangerte komplette løsninger, etter FR-8/12.
4. **SCRUM-35/36:** Kriteriene er allerede avklart i SCRUM-14; skriv P1/P2,
   P1-standard, lik rangering og manglende P2-data uten automatisk bytte til P1.
5. **SCRUM-37:** Del kriteriene i Må (låser fra datasettet, fast demo-tid,
   beskyttede tildelinger) og Bør (lederen låser/åpner i UI). Ikke gjør hele
   søkeleveransen Bør fordi begge deler ligger i samme sak.
6. **SCRUM-53/55:** Presiser henholdsvis øktens levetid og D8 uten automatisk
   gjenbruk av gammelt valg, og H2 med synlig manglende historikk/kilde/periode.
   Valg som bestått krever komplett alternativ med bestått kontroll.
7. **SCRUM-39/40/41:** Én KI-handling, feltformat, testmodus, toppkandidat som
   eget kontrolltilfelle, beregnede kostnadstall, identiske statuser og varslet
   fallback. Velging, rangering og status skal være uendret med/uten KI.
8. **SCRUM-22/42/43/44/48:** Ta inn de målbare tverrgående kriteriene i
   NFR-tabellen. «Automatisert test eller manuell sjekk» i SCRUM-43 er for svakt
   alene når NFR-4 krever automatisert UJ-1. Solver-kriteriet i samme sak er
   historisk/ikke aktuelt i førsteversjonen, jf. PRD §6.
9. **Epic SCRUM-8/10/11/12:** Samordne oversikten med FR-24, Må-tilbud/økt,
   Bør-varig logg/UI-låsing, én KI-handling og målbare UX-/leveringskrav.
   SCRUM-6/7/9 har riktig hovedretning; lenker til gjeldende PRD og E35 er
   tilstrekkelig uten å kopiere alle detaljkrav.
10. **SCRUM-46 og historiske avklaringer:** Gjeldende status må skille
    ferdige produktvalg fra kodeverifikasjonen i SCRUM-13/18. SCRUM-17s
    formulering om varig logg i MVP er historisk og overstyrt av E35;
    behold historikken og henvis til dagens Bør-avgrensning. Ikke presenter
    gamle beskrivelser av uavklart teknologi/E33 eller upubliserte filer som
    dagens verifiserte status uten kontroll av senere kommentarer og Git.

Ingen av punktene krever at ferdig appkode foreligger før planleggingskontrollen
i SCRUM-46 kan dokumenteres. De er heller ikke grunnlag for å markere
implementeringssakene Done.

## Avhengigheter: Jira-lenker og arbeidsrekkefølge

I uttrekket finnes ni rettede blokkeringer: SCRUM-13/14/15/16/17 → SCRUM-46,
SCRUM-46 → SCRUM-18/47 og SCRUM-19/20 → SCRUM-60. Det finnes ingen syklus i
disse Jira-lenkene alene. Den praktiske sirkelen oppstår fordi oppfølgingen av
SCRUM-13 i tillegg venter på merge av SCRUM-18; dette er kommentarkontekst,
ikke en ekstra blokkering i uttrekket. Samordnings-/beslutningsgrunnlaget og
kodeverifikasjonen må derfor vurderes hver for seg før status eller lenker endres.

Følgende er logiske leveranseforutsetninger utledet fra kravene, ikke allerede
registrerte Jira-blokkeringer eller nye beslutninger om arbeidsfordeling:

- SCRUM-19 → SCRUM-20 og resultat-/inputkontrakter for visning, regler og søk.
- SCRUM-20 og regelkontrollene → integrert søk, sammenligning og testfasit.
- Kontrollerte resultater og prioriteringer → SCRUM-40/39/41; standardforklaring
  lages før konkret modellvalg etter SCRUM-13/59. Modellvalget i SCRUM-59 er
  nødvendig før ekte modellintegrasjon, ikke før testmodus eller standardtekst.
- Alternativ og dataversjon → SCRUM-52/53; nytt datasett → SCRUM-23/57 og ny
  kontroll/kostnad. Dette hindrer ikke parallell UX eller kontraktarbeid.
- Testet Må-flyt → Bør-utvidelsene FR-22/23, samlet E2E-kontroll og endelig
  leveringskontroll i SCRUM-48.

Ingen ekstra Jira-blokkeringer bør opprettes utelukkende for å få en pen
rekkefølge: angi konkret hva som må leveres før integrasjon, og la uavhengig
forberedelse fortsette. SCRUM-49s eksterne avklaringer og SCRUM-59s modellvalg
skal fortsatt følges opp i egne saker; de er ikke dokumentert som blokkering
av hele PRD-/UX-arbeidet.

## Oppfølging etter avstemmingen

Codex har samordnet de 26 beskrivelsene angitt i
[kontrollgrunnlaget](../../../../docs/scrum-46-prd-avstemming.md), og lest
endringene tilbake fra Jira. NFR-3/5/6/9 har nå uttrykkelige saksreferanser
i PRD-en. Ingen nye blokkeringslenker, tildelinger eller sprintflyttinger er gjort.
Det ble ikke funnet et separat udekket FR som krevde en ny produktsak.
