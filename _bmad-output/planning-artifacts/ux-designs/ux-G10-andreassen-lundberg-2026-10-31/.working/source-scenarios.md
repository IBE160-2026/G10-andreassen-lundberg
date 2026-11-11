# Kildeuttrekk: fravær, alternativer og kostnad

Utført av Codex 31.10.2026 for SCRUM-47, fra brukerbekreftede kilder:
[demoscenarioet](../../../../../docs/demoscenario-fravaer.md) og
[kostnadsanslaget](../../../../../docs/kostnadsanslag.md).
Dette er et uttrekk av føringer og åpne UX-spørsmål, ikke en skjermskisse
eller nye produktvalg.

## Opphav og avgrensning

- Odin avklarte R1–R5, P1/P2, søkegrense 0–1 og tilbudssimulering i oktober.
  Førsteversjonen håndterer frafall i eksisterende uke 5, med uke 1–4 som
  kontekst. Generell arbeidsplass er valgt; ingen bransje er valgt.
- Odin valgte 30.10 sekvensielle morgenfravær, enkel tilbudssimulering og
  begrensede dataoppdateringer som del av sluttresultatet; varig logg er Bør.
  Syntetiske kostnadsanslag er valgt, mens formel, avrunding og O1–O5 er
  Codex sine konkretiseringer, ikke særskilt felles detaljgodkjenning.
- Ansatte, vakter, satser og hendelser i kildene er konstruerte eksempler.
  Hovedtabellen og F2–F4 er ikke et komplett kjørbart datasett.

## Inngang og nødvendig granularitet

| Kilde | Føring |
|---|---|
| «Situasjonen og avgrensningen», D1 | Første eksempel gjelder A01 på onsdag 14.10.2026 kl. 08–16, med behov for én person med K1. D1 krever valg av både ansatt og målskift, deretter «Simuler fravær». |
| «Forslag til demonstrasjon av oppdaterte data» | Fravær gjør valgt ansatt utilgjengelig på valgt vakt i gjeldende datagrunnlag. Tidligere fravær og oppdateringer beholdes. Handlingen registrerer ingen erstatter. |
| «Flere morgenfravær ett etter ett», M1–M2 | Hvert søk gjelder ett målskift. Samlet løsning for samtidige fravær er senere arbeid. Simulert aksept reserverer ingen ansatte. |

**UX-gap:** Brukerens innspill om å velge hvem som er fraværende først
passer D1, men bestemmer ikke hvordan aktuell vakt velges hvis personen har
flere vakter. Kildene fastsetter heller ikke fravær for en hel dag eller en
fri periode. Det bør ikke utledes fra personvalget alene.

Kilden beskriver at lederen velger «Finn alternativer». Om fraværsvalget
skal starte søket automatisk, eller etterfølges av denne handlingen, er et
UX-spørsmål å avklare mot brukerens siste innspill; ingen endring er valgt her.

## Hva sammenligningen må gjøre synlig

- **S1:** A02 og A03 består R1–R5. Med P1 kommer A02 først (24 → 32 timer),
  mens A03 får 32 → 40 timer. P2 kan gi A03 først. Lederen kan undersøke
  og velge A03 uten at P1 byttes automatisk eller A02s timer endres.
- Kontroll, prioritering og lederens valg holdes atskilt. Manglende data,
  relevante timer/hvile, berørte ansatte/vakter og konsekvenser må fremgå.
  Historikk viser kilde/periode og eventuelle mangler, uten skjult poengsum
  (H1–H3). Nødvendige nabovakter inngår i kontrollene (H4–H5).
- S4 viser full likhet som lik rangering. S5 viser manglende sorteringsdata
  separat fra regelstatus: bestått kandidat uten avtalt timetall er ikke
  fullstendig rangerbar med P2, og systemet bytter ikke stille til P1.
- Hovedtabellen har ingen kostnadsdata. O1/O2s separate konstruerte roller
  må ikke gis til A02/A03 som om de var deres dokumenterte satser/beløp.

## Statuser og søkeomfang

| Tilstand | Betydning for UX |
|---|---|
| Oppfyller scenarioreglene | Alle fem kontroller er bekreftet. Bare komplette, kontrollerte forslag rangeres som løsninger. Dette er ingen generell lovlighetsgaranti. |
| Regelavvik | Minst ett kjent brudd, også om annet grunnlag mangler. Kandidaten kan undersøkes; bruddet skal ikke skjules eller bli bestått ved lederens valg. |
| Uavklart | Ingen kjent brudd, men nødvendig grunnlag mangler. S3 må vise hva som mangler, eksempelvis V01s tilgjengelighet; ikke hevde at ingen kan ta vakten. |
| Udekket behov | Bemanningsmangel i gjeldende grunnlag. S1 er fortsatt udekket selv når gode forslag finnes, til oppdaterte data viser ny bemanning. Dekning og kandidatens kontrollstatus er forskjellige størrelser. |

Grense **0** gir direkte erstattere; **1** inkluderer opptil én intern
flytting og er standard/maksimum. Hovedtabellen bruker 0 som kontrollert
eksempel, ikke som appens standard. F2 flytter B fra Y til X og tildeler
ledige C til Y: begge vakter og alle berørte må bestå. F3 dekker X men lar
Y stå udekket og er ikke en komplett løsning. F4 med to flyttinger er utenfor
begge grenser. Tomt resultat beskriver bare undersøkt omfang/kandidatsett;
det beviser ikke at enhver løsning er umulig.

## Kostnadsgrunnlag og differanse

Kostnadsdokumentets «Beregningsgrunnlag» krever alternativets anslag,
tilsvarende referanse i gjeldende grunnlag og differanse i NOK. Ved flytting
inngår begge vakter og alle berørte. Timer, syntetiske satser/tillegg,
modellbegrensning og dataversjon skal kunne etterprøves.

- O1: 8 timer × (200 + 25) = 1 800 NOK; differanse +1 800 mot referanse 0.
- O2: referanse 1 600; nytt anslag 3 240; differanse +1 640 for B/C og X/Y.
- O3: manglende sats gir uavklart total/differanse. En delsum er ikke et
  fullstendig anslag. Manglende kostnad endrer ikke R1–R5 eller P1/P2.
- O4: ny dataversjon krever ny beregning/forklaring. O5 dekker tilleggsgrense
  og avrunding; detaljer finnes i kilden og skal ikke fylles inn av KI.

Udekket behov eller regelavvik forblir synlig ved beløpet; et ufullstendig
forslag skal ikke fremstå som en billig, komplett løsning. Syntetiske satser
er ikke reell tariff, overtid eller full arbeidsgiver-/fraværskostnad.

## Tilbud, økt og nytt grunnlag

- F5–F7 skiller sendt/venter/akseptert/avslått. Ved flytting må alle berørte
  akseptere for full simulert aksept. Ubesvart er ikke aksept; uten simulering
  vises «aksept ikke simulert».
- Verken undersøkelse, øktvalg eller aksept gjennomfører vaktendring.
  Tilbud/svar gjelder konkret forslag og dataversjon.
- D2–D4 viser innlasting av et forhåndslaget datasett med endringsoversikt
  og ny kontroll. Oppdateringen kan vise annen eller uendret bemanning.
  Den fremstilles som data fra kilden, ikke utført lederbeslutning.
- D5/D8 bevarer valg/svar i aktiv økt. Gammelt valg blir historikk på gammel
  dataversjon, uten automatisk gjeldende aksept etter oppdatering.
  Varig logg og overgangene D6–D7 er Bør.
- M1/M2 krever at neste fravær bruker gjeldende grunnlag; en tidligere
  løsning regnes først som innført når separat oppdatering viser den.
