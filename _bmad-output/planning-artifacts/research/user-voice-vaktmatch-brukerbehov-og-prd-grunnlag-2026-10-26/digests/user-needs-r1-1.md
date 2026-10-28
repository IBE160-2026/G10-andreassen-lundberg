# Brukerbehov ved korttidsfravær – forskningsdigest

Skrevet av Codex, 2026-10-26. Runde 1, avgrenset nettsøk. Formål: grunnlag for spørsmål og hypoteser til en liten bemanningsdemo. Ingen prosjektfiler er lest. Prosjektkonteksten brukes bare til å stille spørsmål; funnene nedenfor kommer fra eksterne kilder hentet i denne runden. Ingen intervjupersoner identifiseres, og ingen deltakersitater gjengis.

## Stående forskningsregler

1. Never conclude from training data alone. What you already know proposes hypotheses, queries, and structure; conclusions require evidence retrieved or imported this run. A claim you cannot evidence is stated as an unverified belief or not at all.
2. The research firewall. Project context — briefs, PRDs, code, memory, persistent facts — shapes what to ask, never what is true. It is inadmissible as evidence: every claim in a research artifact traces to a digest or import file with a source. Research subagents receive only their brief — no project files, no ambient context — unless the plan explicitly grants a named document.

## Funn

### F1 – Kompetanse er en dokumentert utfordring i det norske utvalget

- **claim:** I 2022-rapportens spørsmålsutvalg (n=624) var 82 prosent enige i at det var vanskelig å skaffe vikar/ekstravakt med samme kompetanse ved korttidsfravær. Dette er historiske, selvrapporterte svar fra et bestemt utvalg; det er ikke et estimat for alle norske ledere i dag.
- **source URL:** [Førstelinjeledere i døgnkontinuerlige tjenester, s. 8 og 17–19](https://www.nsf.no/sites/default/files/2022-10/R1021942%20NSF%20rapport_F%C3%B8rstelinjeledere%20i%20d%C3%B8gnkontinuerlige%20tjenester.pdf).
- **publisher:** Agenda Kaupang, på oppdrag fra Norsk Sykepleierforbund; publisert hos NSF.
- **pub_date:** 2022-09-16.
- **accessed:** 2026-10-26.
- **confidence:** Høy for rapportens svarfordeling; begrenset for overføring til andre virksomheter eller tidspunkt.
- **class:** Empiri – tverrsnittsundersøkelse, opplevd kompetansebehov.
- **Populasjon og begrensning:** Rapportens samlede utvalg var 708 førstelinjeledere: 288 fra sykehjem, 106 fra hjemmesykepleie og 314 fra somatiske sykehusavdelinger. Antall svar varierer mellom spørsmålene. Metodedelen viser til en annen rapport for nærmere beskrivelse av gjennomføringen; svarprosent og fullstendig utvalgsramme er ikke kontrollert her. Ingen årsakssammenheng eller programvareeffekt er målt.

### F2 – Koordinering kan være et målbart forbedringsområde

- **claim:** En finsk studie sammenlignet papir, telefon og e-post med et IT-basert bemanningssystem ved plutselig fravær. Etter innføringen ble det registrert færre lederoppgaver, ubemannede vakter og uplanlagte vaktendringer (alle p<0,001). Studien dokumenterer et konkret historisk forbedringsforløp, ikke at enhver digital løsning gir samme effekt.
- **source URL:** [Comparing the Two Techniques for Nursing Staff Rescheduling to Streamline Nurse Managers' Daily Work in Finland](https://pubmed.ncbi.nlm.nih.gov/31652140/), DOI 10.1097/CIN.0000000000000567.
- **publisher:** Computers, Informatics, Nursing / Wolters Kluwer; forfatterabstract hentet fra PubMed/NLM.
- **pub_date:** 2020-03, bind 38(3), s. 148–156.
- **accessed:** 2026-10-26.
- **confidence:** Middels for den beskrevne sammenhengen; lavere for kausal effekt og overførbarhet.
- **class:** Empiri – kvasi-eksperimentell før/etter-studie med én gruppe.
- **Populasjon og begrensning:** 61 sykepleieledere, 5 800 oppgaver og 2 628 plutselige fraværshendelser i Finland. Bare abstract er lest. Det oppgir ikke detaljert utvalgsramme, absolutte effektstørrelser eller nok informasjon om samtidige endringer. Ingen kontrollgruppe. En liten demo kan derfor ikke love tids- eller kostnadsbesparelse ut fra denne studien.

### F3 – Oversikt over hele arbeidstiden og vaktlaget ble beskrevet som nyttig

- **claim:** Svenske deltakere beskrev nytte av oversikt over hele arbeidsplanen, arbeid på andre avdelinger, overtid, vaktendringer og kompetansesammensetning. Ved korttidsfravær kunne en vaktendring flytte bemanningshullet til en senere vakt.
- **source URL:** [Managing Sustainable Working Hours within Participatory Working Time Scheduling for Nurses and Assistant Nurses](https://onlinelibrary.wiley.com/doi/10.1155/2023/8096034), særlig 3.3.4, 3.4.1 og 3.4.4.
- **publisher:** Journal of Nursing Management / Wiley.
- **pub_date:** 2023-12-09.
- **accessed:** 2026-10-26.
- **confidence:** Middels; direkte kvalitative utsagn, ikke prevalens eller effektmåling.
- **class:** Empiri – informasjonsbehov og arbeidsflyt.
- **Populasjon:** Strategisk utvalg: 11 førstelinjeledere og 9 bemanningsassistenter ved sykehusavdelinger i fire svenske regioner. Intervjuer mars 2020–oktober 2021 om deltakende turnusplanlegging.

### F4 – Teknologi og vilje til ekstravakt løste ikke alle avveiinger

- **claim:** Samme svenske studie beskrev både nyttige systemer og uklare varsler som kunne avvises. Ansattes ønsker og restitusjon kunne trekke i forskjellige retninger. Bemanningsmangel begrenset mulighetene også når teknologi var tilgjengelig.
- **source URL:** [Samme originalstudie, 3.3.2, 3.4.1 og 3.4.4](https://onlinelibrary.wiley.com/doi/10.1155/2023/8096034).
- **publisher:** Journal of Nursing Management / Wiley.
- **pub_date:** 2023-12-09.
- **accessed:** 2026-10-26.
- **confidence:** Middels for deltakernes beskrivelser; ingen målt effekt på beslutningskvalitet.
- **class:** Empiri – avveiinger og motvekt til teknologiløfter.
- **Begrensning:** F3 og F4 er én studie, ikke uavhengig bekreftelse. Bare fire regioner; pandemiperioden kan ha påvirket svarene selv om pandemitopper ble utelatt fra analysen. Studien er bredere enn akutt fraværshåndtering.

## KI-forslag til PRD-arbeidet – ikke validerte krav

Funnene gir grunn til å undersøke følgende, men avgjør ikke hvilke funksjoner målbrukeren trenger:

1. **Kompetanse:** Be en målbruker vise hvordan nødvendig kompetanse bestemmes for én konkret vakt. Hvilke krav kan registreres presist, og hvilke vurderinger krever lokalkunnskap? Grunnlag: F1.
2. **Arbeidsflyt og resultatmål:** Kartlegg en nylig fraværshendelse fra melding til avklart dekning. Tell søk, kontakter, venting og endringer. Bruk disse målene i en brukertest, uten å love økonomisk gevinst. Grunnlag: F2.
3. **Datadekning:** Undersøk hvor arbeidstid på tvers av enheter hentes fra, og hvordan ukjent informasjon vises. Grunnlag: F3.
4. **Forklaring og konsekvens:** Test om brukeren forstår et avslag og ser følgene for senere vakter. Grunnlag: F3–F4.

Deterministiske regler, kandidatsammenligning og menneskelig valg er oppdragskontekst, ikke forskningsfunn. Disse kildene dokumenterer verken at akkurat denne kombinasjonen er foretrukket, eller hvordan en rangering bør vektes. En kandidat kan derfor omtales som et testforslag, ikke som en forskningsbekreftet anbefaling.

## Kunnskapshull og videre spor

- Ingen lokal målbruker er intervjuet. Roller, datakvalitet, aktualitet, tilgjengelighet og bekreftelse fra ansatte må avklares i den valgte demo-konteksten.
- Ingen dokumentasjon her fastsetter norske lov- eller avtalegrenser, eller en korrekt modell for kvalifikasjoner. Ikke bruk studienes praksiseksempler som rettsregler.
- Ingen ny prevalenspåstand: alle utbredelsestall er eksplisitt historiske og utvalgsavgrensede.
- Den finske originalartikkelens fulltekst er et relevant neste spor før effektstørrelser eller konkrete systemfunksjoner brukes. Svenskstudien peker mot ansatte som en egen forskningsgruppe; deres behov kan ikke erstattes av ledernes beskrivelser.
- En nærmere norsk arbeidsflytstudie ved akutt fravær mangler i denne runden. Søket fant også en Fafo/KS-rapport fra 2025 om vikarreduserende tiltak; den er bare søketreff, ikke lest eller brukt som belegg.

## Kilder lest og verktøybudsjett

Tre distinkte originalkilder: norsk rapport (utvalgte metode- og resultatdeler), finsk artikkel (kun abstract), svensk artikkel (utvalgte metode-, resultat- og begrensningsdeler). Seks web-kall: ett samlet søk og fem innhentings-/oppslagskall. Søketreff for øvrige kilder er ikke evidensgrunnlag. PMC og DOI-ruten til svenskstudien feilet; forlagets fulltekst fungerte. Én skriverunde med apply_patch. Ingen nye søkeomganger, prosjektfillesing, Git- eller Jira-endringer.

## Sterkeste påstander for uavhengig kontroll

1. **F1:** Kontroller at 82 prosent gjelder rapportens spørsmål med n=624, og at tallet omtales som et historisk utvalgsresultat – ikke dagens norske situasjon.
2. **F3:** Kontroller originalstudiens avsnitt 3.4.1 og 3.4.4 for behovet for oversikt over arbeidstid på tvers av avdelinger og risikoen for å flytte bemanningshullet.
