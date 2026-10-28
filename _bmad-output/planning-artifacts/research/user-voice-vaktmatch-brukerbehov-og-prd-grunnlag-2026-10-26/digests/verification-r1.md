# Uavhengig kontroll av bærende syntese – runde 1

Skrevet av Codex, 2026-10-26. Kun `user-needs-r1-1.md` og `ai-explanations-r1-1.md` er lest som inngang; ingen øvrige prosjektfiler. Originalkildene nedenfor er hentet på nytt. Dette er kildekontroll, ikke en ny empirisk replikasjon.

## Forskningsregler

1. Never conclude from training data alone. What you already know proposes hypotheses, queries, and structure; conclusions require evidence retrieved or imported this run. A claim you cannot evidence is stated as an unverified belief or not at all.
2. The research firewall. Project context — briefs, PRDs, code, memory, persistent facts — shapes what to ask, never what is true. It is inadmissible as evidence: every claim in a research artifact traces to a digest or import file with a source. Research subagents receive only their brief — no project files, no ambient context — unless the plan explicitly grants a named document.

## A – Bemanningsbehov

**A1. Smal påstand:** Kompetanse ved fraværsdekning er et begrunnet tema å undersøke videre i en helsefaglig bemanningskontekst. **Status: verified. Confidence: middels.** Norsk survey [S1] og svensk intervjustudie [S2] har ulike datainnsamlinger og støtter relevansen av kompetanse. Dette bekrefter et undersøkelsestema, ikke et bestemt produktkrav, en løsning eller dagens utbredelse.

**A2. Smal påstand:** Hele arbeidstidsbildet og konsekvenser for senere vakter er relevante undersøkelseshypoteser. **Status: unverified som uavhengig korroborert påstand; kildegjengivelsen er kontrollert. Confidence: middels for hypotesen, lav for generalisering.** [S2] beskriver oversikt på tvers av avdelinger og at dekning kan forskyve en ledig vakt. Dette er én datakilde, selv om flere avsnitt omtaler temaet. [S3] måler blant annet ubemannede vakter og uplanlagte vaktendringer, men abstractet bekrefter ikke den presise mekanismen eller informasjonsbehovet.

**A3. Formulering som krever rettelse:** «Flere uavhengige studier bekrefter alle tre behovene.» **Status: disputed. Confidence: høy.** Kildene er komplementære; hvert enkelt detaljbehov har ikke flere uavhengige bekreftelser. Forsvarlig syntese: «Ulike historiske helsestudier gir samlet grunn til å undersøke kompetanse, arbeidstidsoversikt og følger av vaktendringer. Detaljene har ulik evidensstyrke og må undersøkes i målgruppen.» Dette er en KI-syntese, ikke en formulering fra kildene.

## B – Forklaringer og beslutningskvalitet

**B1. Smal påstand:** At en forklaring øker aksept eller får gode subjektive vurderinger, er alene utilstrekkelig dokumentasjon på bedre beslutninger. **Status: verified. Confidence: middels.** [S4] og [S5] gir uavhengige, komplementære eksperimentfunn: økt etterfølgelse er ikke nødvendigvis bedre treffsikkerhet, og subjektive vurderinger kan favorisere grensesnitt som gir mer overavhengighet. Dette er en begrunnelse for å måle oppgaveutfall separat, ikke bevis for at alle forklaringer er skadelige.

**B2. Overføring til produktet:** Ingen av de to eksperimentene tester moderne generativ LLM-tekst i bemanningsarbeid. **Status: unverified for produktets effekt; avgrensningen er kontrollert mot studienes oppgaver og modeller.** Ingen sammenligning av KI-omskriving og maltekst i denne målgruppen foreligger i materialet. [S6] bidrar med et metodeargument om trofasthet, ikke en tredje empirisk bekreftelse.

## Originalkilder, ordlyd og dataproveniens

Alle kilder nedenfor er åpnet eller hentet via nettverktøy 2026-10-26. Tall og metodebeskrivelser er kildegjengivelse; de er ikke uavhengig validert mot rådata.

### S1 – Norsk lederundersøkelse

[Agenda Kaupang / NSF: Førstelinjeledere i døgnkontinuerlige tjenester](https://www.nsf.no/sites/default/files/2022-10/R1021942%20NSF%20rapport_F%C3%B8rstelinjeledere%20i%20d%C3%B8gnkontinuerlige%20tjenester.pdf), publisert 2022-09-16. Side 3 og 17–18 kontrollert. Rapporten oppgir 708 førstelinjeledere samlet; figur 4-3 angir n=624 og teksten 82 prosent enige i utfordringen med å skaffe tilsvarende kompetanse ved korttidsfravær. Dette er selvrapportering fra norsk helsetjeneste. Datagrunnlaget er en egen survey, ikke gjenbruk av den svenske eller finske studien. Svarprosent og rådata er ikke kontrollert. Det historiske prosenttallet kan ikke brukes som nåtidsestimat.

### S2 – Svenske intervjuer

[Epstein mfl.: Managing Sustainable Working Hours](https://onlinelibrary.wiley.com/doi/10.1155/2023/8096034), Journal of Nursing Management, publisert 2023-12-09. Metode og avsnitt 3.3–3.4 kontrollert. Egen svensk kvalitativ datainnsamling mars 2020–oktober 2021; separat fra norsk survey og finsk før/etter-studie. Avsnitt 3.4.1 beskriver manglende oversikt på tvers av avdelinger og forskyvning av ledige vakter. Avsnitt 3.4.4 beskriver nytte av samlet arbeidstids- og kompetanseoversikt samt uklare varsler. Dette er deltakernes erfaringer, ikke målt effekt eller prevalens. Flere utsagn fra samme studie øker ikke antallet uavhengige kilder.

### S3 – Finsk før/etter-studie

[Tuominen mfl.: Comparing the Two Techniques for Nursing Staff Rescheduling](https://pubmed.ncbi.nlm.nih.gov/31652140/), Computers, Informatics, Nursing, publisert i nummeret 2020-03. Forfatterabstract hentet via PubMed-søk etter at første direkte åpning ga tomt innhold; samme abstract finnes i [Universitetet i Turkus publikasjonspost](https://research.utu.fi/converis/portal/detail/Publication/44910140?lang=fi_FI). Dette er samme studie, ikke to kilder. Eget finsk før/etter-materiale: 61 ledere, 5800 oppgaver, 2628 fraværshendelser. Færre oppgaver, ubemannede vakter og uplanlagte vaktendringer rapporteres etter innføring. Ingen kontrollgruppe; fulltekst og rådata er ikke kontrollert. Understøtter arbeidsflyt som undersøkelsestema, ikke alle detaljbehovene i A2.

### S4 – Eksperimenter med sentiment og LSAT

[Bansal mfl.: Does the Whole Exceed its Parts?](https://aiweb.cs.washington.edu/ai/pubs/bansal-chi21.pdf), ACM CHI, publisert 2021-05. Abstract, metode 4.2–4.3 og resultat 5.1 kontrollert. Egne amerikanske MTurk-eksperimenter med bok-/ølanmeldelser og LSAT; blant annet finjustert RoBERTa for LSAT. Forklaringer ga ikke signifikant bedring over konfidensbasert støtte i disse oppsettene; aksept økte også ved feil råd. «Ikke signifikant bedring» må ikke omskrives til bevist null effekt. Deltakere, stimuli og utfall er samlet for dette arbeidet, ikke hentet fra S5.

### S5 – Eksperiment med matvalg

[Buçinca mfl.: To Trust or to Think](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf), ACM PACMHCI/CSCW1, publisert 2021-04. Abstract og metode 3.3–3.6 kontrollert. Egen rekruttering: 260 amerikanske MTurk-deltakere, 199 beholdt i analysen etter oppgitte eksklusjoner. Simulert KI med styrte feil i en oppgave om ingredienser/karbohydrater; ikke en trent modell. Aktiviserende grep reduserte overavhengighet relativt til enkle forklaringer, mens de mest effektive fikk svakere subjektive vurderinger. Studieopplegg og innsamlede oppgavesvar er separate fra S4. Begge bruker MTurk; eventuell personoverlapp kan ikke utelukkes uten deltakeridentifikatorer. Det finnes ikke tegn til gjenbruk av samme underliggende forsøksdata.

### S6 – Metodeargument

[Jacovi og Goldberg: Towards Faithfully Interpretable NLP Systems](https://aclanthology.org/2020.acl-main.386.pdf), ACL, publisert 2020-07. Artikkelen betegner seg som et menings-/metodebidrag og skiller trofasthet fra plausibilitet. Den gir ikke egne eksperimentdata som validerer produktets tekst. Registreres som metodekilde, ikke empirisk replikasjon.

## Kildetelling og avslutning

- Fire web-kall; ingen nye primærkilder lagt til.
- A: tre eksisterende empiriske originalstudier kontrollert. To gir direkte støtte til kompetanse som tema; én gir direkte støtte til de presise arbeidstids-/forskyvningspåstandene.
- B: to eksisterende empiriske originalarbeider med separate forsøksdata, pluss én eksisterende metodeartikkel. To ulike oppgaver gir komplementær støtte, ikke replikasjon av samme effekt.
- Seks unike originalarbeider totalt; fem empiriske. Ny kildeøkning: **0**. Speil, søketreff, ny lesing og flere avsnitt teller ikke som nye kilder.
- Stopp: bærende syntese kan brukes med A2/A3-presiseringen. Lokal behovsvalidering og direkte effekt av produktets forklaringer står fortsatt åpne.
