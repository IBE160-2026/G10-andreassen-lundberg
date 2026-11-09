# Etterkontroll K1–K11 og sensorkrav

## 2026-11-09 kl. 15:44 — Stian Lundberg

### Oppgave
Gjennomgå prosjektstatus og gjøre så mye som mulig i økten. Utført med Claude
Code (Opus 5.5): rette de elleve åpne tiltakene fra gjennomgangen tidligere
samme dag og vurdere repoet mot sensorveiledningen for del 1.

### Plan
- Kjøre CI-kontrollene på `scrum-19-demoflyt` og lese
  [gjennomgangen](../../_bmad-output/implementation-artifacts/review-status-2026-11-09.md)
  og [Odins logg](../sirclaudealot/995-2026-11-09-09-07-25-statusgjennomgang-med-agenter.md).
- Rette K1–K5 og K10, deretter testhullene K6–K8 og bevisføringen K9/K11.
  Teste hver retting med samme mutasjon som slapp gjennom før.
- Kjøre benchmark og nettleserkontroll mot den faktiske appen med proveniens.
- Lese sensorveiledningen og skrive en egenkontroll per kriterium.

### Resultat
- Backend `d37f92a`: K2 viser vaktpar og timer bak R4-avvik. K5 gjør at tom
  `family_id` ikke bekrefter samme scenario. Nye tester dekker K6–K8.
- Frontend `dd046ad`: K1 gjør at «Prøv igjen» henter forhåndsvisningen på
  nytt, K3 viser plan og forslags-ID i valg og historikk, K4 holder
  «Øvrige funn» åpen og gir fokus tilbake, og K10 retter neste datasett etter
  innlasting.
- Måleskript `c7679d8`, `a706007`, `1bbfdec`, `6b1d15b`: K9 skriver
  tidsstemplede målinger for ti datasett og overskriver aldri originalen. K11
  legger proveniens i nettleserrapporten. Underveis ble det rettet at
  skjermbildene fra 08.11 ble overskrevet (gjenopprettet fra Git), at `tzdata`
  manglet på Windows, og at standard-URL-en var feil.
- Mutasjonskontroll: alle fem backendmutasjonene og alle fem
  frontendmutasjonene gir nå testfeil.
- Kontroller på HEAD: 70 backendtester (fra 64), ruff, 24 frontendtester (fra
  20), oxlint og build med Node 24.13.1. Nettleserkontroll 39/39 i Chromium 151
  (uten axe), med commit og datasettfingeravtrykk i rapporten.
- Dokumentasjon `cfc825f`, `e6f7434`: spesifikasjonen har K1–K11 avkrysset og
  status `done`. Rapporten har fått en etterkontroll. Nye dokumenter er
  [egenkontroll mot sensorveiledningen](../../docs/sensor-egenkontroll.md),
  vekting i leveringskravene, skjermbilde i README og et memlog-innslag.
  89 lokale lenker kontrollert.
- Jira er bare lest. Produktbrief og PRD er uendret. Ingen push, PR eller
  merge. Sensorveiledningens PDF ligger usporet lokalt og er ikke lagt i repoet.

### Åpne punkter
- `scrum-19-demoflyt` må merges til `main` gjennom en PR med CI, ellers ser
  sensor ikke appen.
- KI-sporet (SCRUM-59, SCRUM-39, SCRUM-41) er ikke startet. Det er
  funksjonalitetsgapet med størst konsekvens mot product brief og PRD.
- Jira-saker berørt av K1–K11 trenger kommentar med commit-ID etter push.
- SCRUM-48: en ny brukers installasjon på under 20 minutter er ikke målt.
  README-kommandoene er bare skrevet for PowerShell.
- Commit `14b187d` (15 757 linjer) er et varseltegn i sensorveiledningen. Det
  skal forklares, ikke skrives om.
- Småryddingen i rotmappen og `.gitignore` og oppdelingen av `App.tsx` er ikke
  gjort. Sletting må koordineres med Odin.
