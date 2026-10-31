# Kildeuttrekk til UX – brief og PRD

Utført av Codex 31.10.2026 for SCRUM-47. Dette er et uttrekk av krav og
føringer, ikke en skisse eller ny UX-beslutning. Brukeren har bekreftet
kildene og valgt stegvis arbeid. Innspillet om å velge fraværende først
registreres av hovedagenten med sitt eget opphav.

Kilder: [produktbriefen](../../../../../productbrief.md), oppdatert 30.10.26,
og [PRD](../../../prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md), oppdatert
31.10.26. Briefen er gjeldende utkast. PRD-ens `final` betyr ferdigstilt
planleggingsrunde, ikke full godkjenning av alle detaljkrav. PRD §7.2/10 og
briefens status skiller Stians valg, Odins revisjon innenfor delegert
myndighet og KI-konkretiseringer.

## Inngang, fravær og søk

- **Gjeldende krav:** lederen har ansatte, vakter og behov for planlagt uke 5
  tilgjengelig. Udekket behov er synlig uten å åpne detaljer. Dataversjon
  vises. Kilde: brief «The Solution», første avsnitt (linje 34); PRD
  FR-1/2 (linje 169–182).
- **Gjeldende krav:** fravær velges for både en ansatt og en vakt. Fraværet
  gjør målskiftet udekket uten å endre datasettfilen. Ingen ansatt, vakt
  utenfor uke 5 og påbegynt vakt gir forklarende melding. Kilde: PRD FR-3
  (linje 184–194).
- **Eksplisitt beskrevet flyt:** Kari velger A01 og vakten, trykker
  «Simuler fravær» og deretter «Finn alternativer». Kari er en konstruert
  eksempelperson. Kilde: PRD UJ-1 (linje 89–105); brief linje 34.
- **Gjeldende krav:** lederen kan velge søkegrense 0 eller 1; standard er 1.
  Søket kontrollerer direkte erstattere og eventuelt én flytting. Kilde:
  PRD FR-9/10 og §3; brief «The Solution» (linje 40 og 66).
- **Gjeldende omfang:** fravær håndteres ett etter ett, ett målskift om
  gangen. Tidligere fravær beholdes. **KI-konkretisering:** tidligere valg
  eller simulert aksept reserverer ingen ansatte; ny bemanning må vises
  i oppdaterte data før neste fravær bruker den som gjennomført. Kilde:
  brief linje 36, PRD FR-3 og §7.2/10.

## Hva sammenligningen må formidle

- Kandidat/alternativ, kontrollstatus per regel, timer før/etter, hvile
  før/etter, konsekvenser for andre og manglende opplysninger inngår i fast
  svarformat. Regelavvik/uavklarte kandidater skilles fra rangerte komplette
  løsninger. Kilde: PRD FR-8/12; brief linje 44.
- Valgte kriterier og rangering vises. Standard er bare P1; P2 kan velges
  og kriterier prioriteres. Likhet vises som likeverdig rangering. Manglende
  P2-grunnlag må ikke gi stille overgang til P1. Kilde: PRD FR-13/14;
  brief linje 48.
- Relevant historikk fra uke 1–4 har kilde/periode og synlige mangler.
  Historikk er kontekst uten skjult poengsum. Kilde: PRD FR-16.
- Kostnadsanslag, referanse/differanse og syntetisk beregningsgrunnlag skal
  kunne etterprøves. Manglende kostnadsgrunnlag er uavklart, ikke null.
  Kostnad endrer ikke rangering eller regelstatus. **Opphav:** kostnad som
  omfang er Odins valg 30.10; formel og O1–O5 er Codex-konkretisering.
  Kilde: PRD FR-24 og §7.2/10; brief linje 50.
- Standardforklaring finnes uten KI-nøkkel. Første KI-handling er «Forklar
  forskjellen»; den endrer ikke kontroll, rangering eller valg. Kilde:
  PRD FR-17–19; brief linje 50/56.

Kildene fastsetter innholdet som skal kunne sammenlignes, men ikke den
visuelle fordelingen mellom første oversikt og kandidatdetalj. Ingen
korttype, tabell, sideinndeling eller feltprioritering er valgt i dette uttrekket.

## Statuser, valg, tilbud og oppdatering

- **Tre separate dimensjoner:** kontroll (oppfyller scenarioreglene,
  regelavvik, uavklart), dekning (full/delvis/udekket) og søkestatus
  (fullført, avbrutt/feilet, ikke kjørt utenfor omfang). «Ingen kontrollerte
  alternativer funnet innenfor valgt søkeomfang» er ikke bevis for at ingen
  løsning finnes. Kilde: PRD §3, FR-5/11 og FR-9.
- Enhver kandidat kan undersøkes, men regelavvik/uavklart kan ikke markeres
  som et bestått valg. Å undersøke eller velge endrer ingen vakter. Valg
  lever i økten og knyttes til dataversjon. Kilde: PRD FR-15.
- Enkel tilbudssimulering er Må: sendt, venter, akseptert, avslått.
  Omfordeling har full aksept først når alle berørte har akseptert.
  Ingen status gjennomfører vaktendring. Kilde: PRD FR-20, §7.2;
  brief linje 42/60. Omfanget er Odins revisjon 30.10.
- Begrenset datasettbytte med endringsoversikt og ny vurdering er Må.
  Tidligere valg/svar beholdes som historikk på gammel versjon uten å
  fremstå gjeldende; kostnad beregnes på nytt. Kilde: PRD FR-21/15, §7.2.
- Datasettlåser er Må; lederens låsing i UI er Bør. Varig logg er Bør,
  ikke nødvendig for førsteversjonens flyt. Ingen ekte tilbud, ansattportal,
  leverandørintegrasjon eller gjennomføring av vaktendringer. Kilde: PRD
  FR-10/22/23, §6/7; brief «The Solution» og «Scope».

## Mobil, PC og tilgjengelighet

PRD NFR-2 krever 360 px til PC uten vannrett rulling, tekstkontrast minst
4,5:1, tastaturbetjening av alle handlinger, synlig fokus, etiketter på
skjemafelt og tekststatus i tillegg til farge. Hver visning har tomtilstand
og feilmelding med vei videre. Skisser skal ligge i repoet før hovedsidene
bygges. NFR-3 krever forståelig norsk feil og vei videre, også ved backendfeil;
NFR-9 fastsetter norsk bokmål. Brief «Scope» (linje 108) fastsetter responsiv
nettleserflate på mobil/PC. Ingen breakpoint- eller komponentløsning er valgt.

## Avklaringer som faktisk gjenstår

1. **Søkets utløser:** innspillet «velg fraværende først, så alternativer»
   passer rekkefølgen. Det avgjør ikke om alternativene vises automatisk.
   Gjeldende brief/UJ-1 har to navngitte handlinger. Automatikk må avklares
   og avstemmes mot disse før den fremstilles som valgt UX.
2. **Vaktvalg:** kildene krever valgt ansatt og aktuell vakt. De avgjør ikke
   om personen velges fra liste/ukevisning, hvordan flere aktuelle vakter
   skilles, eller om ett kjent målskift kan forhåndsfylles synlig.
3. **Første liste og detaljer:** nødvendige sammenligningsopplysninger er
   fastsatt, men deres plassering, tetthet og videre navigasjon er ikke.
4. **Arbeidssituasjon:** PRD §9 spørsmål 5 ber UX-arbeidet avklare konkret
   skiftlederkontekst. Brief «Who This Serves» (linje 80) sier samtidig
   generell fiktiv arbeidsplass uten bransjetilknytning; ny bransje velges
   ikke ved å omtale et eksempel som en beslutning.
5. Visuelt uttrykk, komponent-/UI-system og opplevelsesmessig retning er
   fortsatt åpne. Ingen reell bruker- eller kostnadseffekt er validert;
   Kari og scenariene er eksempler, ikke intervju- eller testbevis.
