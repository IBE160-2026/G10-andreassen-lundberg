# IBE160 – leverings- og dokumentasjonskrav

Kontrollert 22. oktober 2026 mot emneforsiden og kunngjøringer i Canvas,
ressursene i modulen «Prosjektoppgaven» og Høgskolen i Moldes emneside. Dette
dokumentet gjengir prosjektkrav som er relevante for repoet. Private
studienotater er brukt til å finne åpne spørsmål, men er ikke kopiert inn eller
brukt som bekreftende kilde.

## Kort status

| Tema | Gjeldende grunnlag | Status |
|---|---|---|
| Product brief / proposal | En separat `proposal.md` er utgått. Canvas beskriver godkjent `productbrief.md` som leveringsvilkår, og faglærer har sagt at gruppen kan gå videre med justeringer. | Kravet er bekreftet; gruppens eventuelle separate formelle godkjenningsstatus er ikke dokumentert. |
| Frist for product brief | Søndag 27. september 2026 kl. 23:59. Den opprinnelige fristen 20. september ble forlenget. Gruppen leverte 20. september. | Bekreftet i Canvas-kunngjøring og faglærers tilbakemelding. |
| Sluttfrist for prosjektkode og refleksjonsrapport | Ingen dato er publisert i de kontrollerte Canvas-flatene eller på emnesiden. Del 1 hentes fra gruppens repository slik det står ved fristen; leveringskanal for refleksjonsrapporten er ikke oppgitt. | **Ikke avklart. Må bekreftes av faglærer eller i en ny oppgave-/eksamenspublisering.** |
| Vurderingsdeler | Prosjektkode og funksjonalitet 70 %, refleksjonsrapport 30 %. Begge er gruppebesvarelser. | Bekreftet på emnesiden; del 1 er utdypet i sensorveiledningen. |
| Individuelle bidrag | Refleksjonsmalen har en egen personlig refleksjon for hvert gruppemedlem. | Bekreftet i Canvas-malen. |
| «Delvurdering 3» | Canvas-emneforsiden sier at vurderingen består av tre deler og nevner «delvurdering 3», men beskriver bare to deler som til sammen utgjør 100 %. Den formelle emnesiden sier uttrykkelig to deler og nevner ingen tredje del. | **Motstridende tekst. Krever skriftlig avklaring fra faglærer.** |
| Visuelt uttrykk | Vurderes under design og brukeropplevelse med 10 % av del 1, tilsvarende 7 % av samlet karakter. | Bekreftet i sensorveiledningen. |

De tre åpne punktene gjør at [SCRUM-49](https://stiodi.atlassian.net/browse/SCRUM-49)
ikke kan regnes som ferdig selv om øvrige krav nå er samlet her.

## Arbeidskrav: godkjent product brief

Canvas-emneforsiden beskriver innlevering av proposal/product brief som et
arbeidskrav og som en forutsetning for å levere prosjektkode og
refleksjonsrapport. En senere kunngjøring presiserer at gruppen **bare** skal
levere `productbrief.md`; `proposal.md` var fjorårets innlevering og er utgått.

Fristen ble først oppgitt som 20. september kl. 23:59 og deretter forlenget til
**27. september 2026 kl. 23:59**. Leveringen skulle ligge i gruppens tildelte
GitHub-repository, ikke lastes opp separat. Repoets `productbrief.md` bruker
20. september som faktisk innleveringsdato, ikke som gjeldende frist. Faglærers
tilbakemelding 6. oktober viser at briefen ble lest og sier at gruppen kan gå
videre med justeringer. Det er prosjektets praktiske klarsignal, men kilden bruker
ikke ordet «godkjent» og viser ikke en egen formell godkjenningsstatus.

Sensorveiledningen bruker fortsatt ordet «proposal» som vurderingsgrunnlag.
Canvas-kunngjøringen er mer spesifikk for 2026 og fastslår at `productbrief.md`
har erstattet den separate proposal-filen. Product brief må derfor leses som
gruppens proposal/vurderingsgrunnlag. Canvas-emnesiden sier at godkjenningen
gjelder hele gruppen.

Kilder:

- [Canvas-emneforsiden](https://himolde.instructure.com/courses/4498), kontrollert 22.10.2026.
- [Kunngjøring: Kun product-brief.md ikke proposal](https://himolde.instructure.com/courses/4498/discussion_topics/67631), publisert 17.09.2026.
- [Kunngjøring: Ny frist for product brief](https://himolde.instructure.com/courses/4498/discussion_topics/67714), publisert 19.09.2026.
- [Faglærers tilbakemelding på gruppens product brief](../tilbakemelding-product-brief.md), datert 06.10.2026.

## Vurdering og dokumentasjon av KI-bruk

Mappevurderingen består etter det publiserte grunnlaget av:

1. **Prosjektkode og funksjonalitet – 70 %:** gruppebesvarelse med en KI-generert
   applikasjon. Dokumentasjonen skal vise hvordan KI er brukt og hvordan koden
   er kvalitetssikret.
2. **Refleksjonsrapport – 30 %:** gruppebesvarelse om utviklingsprosess,
   utfordringer og løsninger, kritisk vurdering av KIs påvirkning samt etiske og
   teknologiske implikasjoner.

Sensorveiledningen konkretiserer hva repoet bør dokumentere:

- planleggingsdokumenter som faktisk er brukt og oppdatert underveis, ikke bare
  generert én gang;
- sporbarhet fra plan til implementasjon gjennom saker, små beskrivende commits,
  grener eller pull requests der det er relevant, med forklaring av avvik fra
  planen eller product brief;
- lagrede prompter og KI-sesjoner koblet til konkrete endringer, inkludert flere
  eksempler der gruppen har kritisert, korrigert eller forkastet KI-forslag;
- begrunnede teknologi- og arkitekturvalg;
- samarbeid og utvikling over tid;
- meningsfulle automatiserte tester og relevante manuelle kontroller;
- spor etter kodegjennomgang, blant annet feil som ble funnet i KI-generert kode
  og hvordan de ble rettet, samt validering, sikkerhetstiltak og kontroll av at
  hemmeligheter ikke ligger i repoet;
- en prosjektspesifikk og oppdatert README med kort målgruppe- og
  funksjonsbeskrivelse, gjerne skjermbilde, forutsetninger med versjoner,
  kopierbare kommandoer for installasjon og oppstart, nødvendige miljøvariabler
  og `.env.example` uten hemmeligheter, testdata eller testbrukere ved behov,
  testkommandoer, mappeoversikt og lenker til planleggings- og prosessdokumenter;
- et ryddig repository uten hemmeligheter, unødvendige byggfiler eller store
  artefakter.

Commit-antall alene skal ikke brukes til å trekke for samarbeid eller
arbeidsfordeling. Prosessporene må vurderes samlet.

Sensor skal klone gruppens repository i organisasjonen `IBE160-2026` og bruke
siste commit før innleveringsfristen; senere endringer skal ses bort fra.

Kilder:

- [Sensorveiledning del 1 i Canvas](https://himolde.instructure.com/courses/4498/files/786568), kontrollert 22.10.2026.
- [Offisiell emneside for IBE160 høsten 2026](https://www.himolde.no/studier/emner/log/2026/host/ibe160.html), kontrollert 22.10.2026.

## Individuelle bidrag og refleksjonsrapport

Refleksjonsrapporten er en gruppebesvarelse, men Canvas-malen krever en
**personlig refleksjon for hvert gruppemedlem**. Rapporten skal ellers dekke
arbeidsmetodikk, teknologi og verktøy, utviklingsfaser, tekniske og
samarbeidsrelaterte utfordringer, KI-spesifikke utfordringer, KIs fordeler og
begrensninger, etikk, personvern, kodekvalitet, læring og anbefalinger. Oppgitt
forventet lengde er 3 000–5 000 ord, avhengig av gruppestørrelse og kompleksitet.

Canvas-emneforsidens resttekst om en tredje del er ikke presis nok til å fastslå
om det finnes en separat, ikke-vektet vurdering av individuelle bidrag. Den
formelle emnesiden sier i stedet at vurderingen består av **to** deler, begge som
gruppebesvarelser. Siden Canvas er den prioriterte kilden for undervisning og
oppgaver, kan motstriden ikke avgjøres bare ved å velge emnesiden. Det kan heller
ikke utledes at den personlige refleksjonen alene er «delvurdering 3».

Kilde: [Refleksjonsrapportmal i Canvas](https://himolde.instructure.com/courses/4498/files/762259), kontrollert 22.10.2026.

## Detaljerte kriterier for visuelt uttrykk

Design og brukeropplevelse utgjør **10 % av del 1**, tilsvarende 7 % av samlet
karakter. Kriteriet tilpasses typen app; eksempelvis vurderes et
kommandolinjeverktøy etter tydelige meldinger og strukturert utdata.
Sensorveiledningen vurderer:

- konsistent bruk av farger, typografi, avstand og komponenter;
- tydelig navigasjon og informasjonsarkitektur;
- klare tilbakemeldinger, feilmeldinger og tomtilstander;
- grunnleggende tilgjengelighet, blant annet kontrast, tastaturnavigasjon,
  alternativ tekst og skjemafeltetiketter;
- relevante skjermstørrelser;
- spor etter designarbeid, som skisser, wireframes eller UX-spesifikasjoner.

Karakterkjennetegnene er:

- **A–B:** gjennomarbeidet, konsistent og intuitiv; bevisste designvalg tilpasset
  målgruppen og grunnleggende tilgjengelighet ivaretatt;
- **C:** ryddig og brukbar, men med enkelte inkonsistenser eller uklarheter i
  flyt og tilbakemeldinger;
- **D–E:** fungerer, men er lite gjennomtenkt, uoversiktlig, inkonsistent eller
  vanskelig å bruke uten forklaring;
- **F:** så uoversiktlig eller ufullstendig at appen i praksis ikke kan brukes
  som tiltenkt.

Kilde: [Sensorveiledning del 1 i Canvas](https://himolde.instructure.com/courses/4498/files/786568), kontrollert 22.10.2026.

## Åpne avklaringer

Canvas-modulen «Prosjektoppgaven» ble kontrollert 22.10.2026. Den publiserte
sensorveiledningen gjelder bare del 1, og modulen inneholder ingen overordnet
sensorveiledning eller egen sensorveiledning for del 2. Følgende må derfor
besvares skriftlig av faglærer eller i en senere offisiell publisering før
prosjektplanen kan låses helt:

1. Hva er innleveringsfristen for prosjektkode og refleksjonsrapport høsten
   2026, og hvor skal refleksjonsrapporten leveres?
2. Er «delvurdering 3» på Canvas foreldet resttekst, eller finnes det en ekstra,
   ikke-vektet del med krav til individuelle bidrag utover den personlige
   refleksjonen i rapportmalen?
3. Er faglærers beskjed om at gruppen kan gå videre den formelle registreringen
   av godkjent product brief, eller finnes det en separat godkjenningsstatus?

**Neste handling:** Odin følger opp de tre spørsmålene skriftlig med faglærer.
SCRUM-49 beholdes i `To Do` til svaret er registrert i Jira og dette dokumentet
er oppdatert.
