# UX-avklaringer på gjennomføringsmandat – SCRUM-47

Dato: 2026-11-08. Utarbeidet av Codex etter Odins uttrykkelige mandat i
prosjektsamtalen om å avklare detaljene selv og gjøre mest mulig med det
påbegynte UX-arbeidet. Dette er KI-konkretiseringer på mandat, ikke uttrykk
for at Odin og Stian har valgt hvert detaljpunkt eller at løsningen er brukertestet.

## Mål og leveranse

Ferdigstill DESIGN.md og EXPERIENCE.md som implementerbart UX-grunnlag,
med kildekontroll, representative skjermreferanser og en klikkbar lokal
prototype. Prototypens syntetiske eksempelinnhold illustrerer visning og
interaksjon; den erstatter ikke regelmotor, søk, KI-integrasjon eller fasitdatasett.

## Konkrete valg

| Tema | Konkretisering fra Codex | Begrunnelse og avgrensning |
|---|---|---|
| Plattform | Responsiv web med PC som arbeidsflate og full énkolonneflyt på mobil. | Eksisterende React-webapp og PRD-krav om mobil/PC; ingen ny appplattform. |
| Uttrykk | Lys arbeidsflate, varm grå bakgrunn, hvite paneler, mørk grønn hovedhandling og lesbar systemfont. | Synlig hierarki og lokal/offline gjengivelse uten nye font- eller UI-avhengigheter. Ikke en etablert merkevareprofil. |
| Oppsett | Kompakt toppfelt, tydelig oppgavesteg, fraværskontekst ved siden av alternativer på bred skjerm; samme leserekkefølge stablet på mobil. | Sammenligningsinformasjonen får mest plass, uten å miste hvilken vakt vurderingen gjelder. |
| Fravær | Behold person → redigerbar startvakt → kalenderdager (1 som standard) → berørte vakter → ett valgt målskift. | Bevarer Odins uttrykkelige valg 31.10. Kalenderperioden utløser ikke automatisk registrering for alle vakter. |
| Handlinger | «Simuler fravær» oppdaterer demoens fraværsgrunnlag for valgt målskift; «Finn alternativer» starter deretter et eksplisitt søk. | PRD UJ-1/FR-3 og demoscenario D1. Den gamle skissen manglet første handling. |
| Ukjent varighet | Behold 1 dag som redigerbar scenarioverdi; hjelpeteksten sier at faktisk varighet kan være ukjent. Ingen automatisk medisinsk eller rettslig slutning. | Førsteversjonen trenger en konkret simulert periode, ikke en ny ordning for sykefraværsadministrasjon. |
| Nattvakt | List hele vakter som overlapper kalenderperioden; vis begge datoene ved midnatt. Perioden går fra lokal midnatt til midnatt etter siste dato i Europe/Oslo. | Hindrer at en vakt som startet kvelden før forsvinner. Påbegynte vakter vises som beskyttet og kan ikke velges. Ingen oppdeling av vakter eller juridisk periodetolkning. |
| Alternativkort | Vis rangering, hvem/flytting, dekning, regelstatus, kostnad og differanse, valgte sorteringstall og dataforbehold før valg. | Brukeren skal se konsekvensen før detaljlesing og valg; kostnad holdes atskilt fra P1/P2. |
| Detaljer | Egen innholdsflate i samme arbeidsflyt med tilbakehandling; regelkontroll, før/etter, berørte vakter, historikk og forklaring i lesbar rekkefølge. | Samme struktur på mobil og PC. Ikke en modal med lang tabell eller skjult viktig forbehold. |
| Historikk | Egen utvidbar seksjon i alternativdetaljene med uke 1–4 og datagrunnlag. | Kontekst, ikke en ny poengsum eller automatisk fairness-rangering. |
| Tilbud | Behold eksplisitt simulerte svar og egen valgt-status; «akseptert» betyr ikke innført i faktisk vaktliste. | Eksisterende komplett Må-flyt. Ingen ekte meldinger eller leverandørintegrasjon. |
| Nye data | Forhåndsvis endringer før bytte av forhåndslaget datasett; ny vurdering knyttes til ny dataversjon. | Tidligere forslag kan ikke brukes som ferskt grunnlag etter bytte. Bevar tidligere øktvalg som historikk med gammel versjon. |
| KI | Én eksplisitt «Forklar forskjellen»-handling for undersøkt mot øverste alternativ; beregnede fakta og standardforklaring er tilgjengelige uavhengig av modell. | Eksisterende krav; ingen modell velges og ingen nøkkel eller ekstern forespørsel trengs i prototypen. |
| Tilgjengelighet | Synlige etiketter, tydelig tastaturfokus, tekst ved status, ingen hoveravhengige handlinger, fleksibel zoom og hensyn til redusert bevegelse. | Kontrollerbar implementeringskontrakt. Full tilgjengelighet i den endelige appen må testes ved implementering. |

## Dekning av skjermreferanser

Fire statiske referanser: ukesoversikt, fravær, alternativoversikt og
alternativdetaljer med planforslag ved én flytting.
Tilbud/svar og datasettbytte vises i den klikkbare prototypen og spesifiseres
i EXPERIENCE.md. Oppstart, tomme tilstander, feil og KI-reserve beskrives
i tilstandstabellen og utvalgte prototypekontroller. Ingen egen
kontoside, administrasjon, varig logg eller planredigering innføres.

## Kontroll og videre bruk

Kildeavstemming og mekanisk kontroll av lenker, tokenreferanser,
komponentdekning og kontrast følges av kjøring av prototypen på PC- og
mobilbredde. KI-kontrollen dokumenteres med tydelig skille mellom
spesifikasjonskontroll, prototypekontroll og faktisk appverifikasjon.
Åpne spørsmål som allerede følges i andre Jira-saker flyttes ikke inn i
SCRUM-47 og blir ikke gjort til nye generelle blokkeringer.
