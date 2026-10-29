# PRD-grunnlag og loggregel

## 2026-10-29 kl. 18:34 — SirClaudealot

### Oppgave
Starte PRD-arbeidet for SCRUM-46, føre inn faglærer Bårds beskjed om BMAD og
arbeidslogg i repoet, og finne en loggregel Odin kan stå inne for. Underveis kom
Stians første PRD på `main`, og arbeidet gikk over til å bygge videre på den.

### Plan
- Føre Bårds beskjed (gjengitt av Odin, med lenke til Panopto-opptaket) inn i
  [kravoversikten](../../docs/ibe160-leveringskrav.md#bmad-og-arbeidslogg) og
  memlog, uten å utvide kravene.
- Starte `bmad-prd` i hurtigspor, med to lesende agenter som trakk ut
  produktgrunnlag og research/krav.
- Da Stians PRD dukket opp: legge bort eget utkast, hente inn hans commit og
  bruke hans PRD som utgangspunkt.
- Sette en loggregel i AGENTS.md. Første forslag (KI spør før den skriver, ingen
  auto-commit) ble erstattet av Odin med Bårds originale oppsett.

### Resultat
- Leveringskravene har ny rad og seksjon om BMAD og logg. Sluttfristen er
  oppdatert til «delvis avklart muntlig: rundt 15. desember».
- Memlog har nye innslag 28.–29.10 (Bårds beskjed, transkripsjonen,
  loggregelen og overstyringen 29.10).
- AGENTS.md, «Sesjonslogg»: skillen brukes som Bård har satt den opp. Logg og
  `issues.md` skrives ved slutten av hver økt, loggfilene committes lokalt
  straks, og skillen pusher aldri. Push krever fortsatt Odins godkjenning.
- Eget PRD-utkast fjernet. De to utdragsfilene ligger i
  `_bmad-output/planning-artifacts/research/utdrag-prd-grunnlag-2026-10-28/`.
- `main` er oppdatert til `f967a96` (Stians PRD, `status: final`) med
  fast-forward. Memlog-konflikten ble løst ved å beholde begge sider.
- Gjennomgang av Stians PRD mot briefen og Bårds krav er gjort muntlig i
  samtalen, ikke skrevet inn i PRD-en.
- Forkastet KI-forslag: Claudes forslag om «KI spør, skriver bare etter ja,
  ingen auto-commit» ble godkjent 28.10 og forkastet av Odin 29.10 til fordel
  for Bårds original. Overstyringen er ført i memlog.
- Rettet underveis: det første memlog-innslaget om Bårds beskjed sa «ikke
  kontrollert mot opptaket». Transkripsjonen støttet det senere, og et nytt
  innslag la det til uten å endre det gamle.

### Åpne punkter
- Odins stilling til Må/Bør-delingen og endringene i PRD §7.2 (PRD åpent
  spørsmål 2). Briefen og endringsloggen oppdateres først etterpå.
- Stian er ikke konsultert om loggregelen i AGENTS.md.
- PRD bør få en setning i NFR-8 om arbeidslogg per økt, og åpent spørsmål 1
  (sluttfrist) bør oppdateres med den muntlige datoen.
- FR-18 (KI-forklaring, Må) avhenger av modellvalget i SCRUM-59.
- SCRUM-49: tre avklaringer fra faglærer gjenstår (sluttfrist skriftlig,
  «delvurdering 3», formell status for briefen).
- Stians gren `scrum-18-kodeskjelett` (kodeskjelett og CI) er ikke merget til
  `main` og ikke gjennomgått her.
