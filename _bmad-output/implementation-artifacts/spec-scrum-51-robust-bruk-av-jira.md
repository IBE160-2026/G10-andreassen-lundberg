---
title: 'SCRUM-51: Prosjektregel for robust bruk av Jira'
type: 'chore'
created: '2026-10-22'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context:
  - '{project-root}/AGENTS.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Jira-regelen i SCRUM-51 er ikke innarbeidet i repoets autoritative prosjektregler, selv om Jira-saken fastsetter at repoet skal være kilde for prosjektbeslutninger og arbeidspraksis.

**Approach:** Legg en kort, operativ Jira-seksjon i `AGENTS.md`, registrer innføringen i rotloggen og verifiser at regelen samsvarer med SCRUM-51 uten å endre produktinnholdet.

</frozen-after-approval>

## Implementation Notes

- `AGENTS.md` fikk en kort Jira-regel som plasserer beslutningsgrunnlaget i repoet, beskriver delegert myndighet, skiller oppfølging fra beslutningsmyndighet og avgrenser endringer som må koordineres.
- `.memlog.md` fikk ett beslutningsinnslag via det påkrevde `memlog.py append`-verktøyet med Odin som opphav og SCRUM-51 som grunnlag.
- `productbrief.md` ble ikke endret; Jira-regelen endrer arbeidspraksis, ikke produktinnhold.
- Sammenligning mot SCRUM-51 bekreftet dekning av dokumentroller, delegert myndighet, koordineringsplikt, sakskvalitet og statusbruk. Gjennomgangen førte i tillegg til tydeligere kryssreferanser mellom Jira, commits og repoet.
- Første memlog-innslag manglet dato og blandet beslutningsgrunnlag med implementeringen. Det ble bevart og korrigert med et `override`-innslag, etterfulgt av et eget `change`-innslag med Codex som opphav.

## Review Triage Log

| ID | Dom | Evidens og behandling |
|---|---|---|
| BH1 | medium | Første memlog-innslag manglet dato. Rettet append-only med datert `override`. |
| BH2 | medium | Innslaget blandet Odins beslutningsgrunnlag og Codex sin innarbeiding. Rettet med `override` og separat `change by Codex`. |
| BH3 | low | Linjesluttvarselet skyldes Git-normalisering i arbeidskopien; `git diff --check` er ren og commit-innholdet normaliseres. Ingen innholdsrettelse nødvendig. |
| BH4 | medium | Status for blokkert arbeid var tvetydig. Presisert aktiv undersøkelse som `In Progress` og venting på avklaring som `To Do`. |
| BH5 | medium | Koblingen mellom Jira og repo var ikke operativ. Jira-nøkkel i commit og verifikasjonskommentar med commit-ID er lagt til. |
| BH6 | medium | Sted for beslutningsspor var uklart. Presisert gjeldende dokument, `.memlog.md` og produktbriefens endringslogg. |
| BH7 | false | Administratorene er bevisst omtalt som roller; SCRUM-51 fastsetter lik myndighet, og listen over koordineringsplikt avgrenser ordinære beslutninger. |
| BH8 | medium | Koordinering manglet mottaker og spor. Presisert berørte prosjektadministratorer og registrering i Jira/repo. |
| BH9 | medium | Språkhygienens virkeområde manglet Jira. Jira-saker og -kommentarer er lagt til. |
| BH10 | low | README beskrev bare språkhygiene. Oppdatert med direkte lenke til Jira-regelen. |
| BH11 | low | Verifikasjon mot Jira-saken var ikke dokumentert. Resultatet er lagt til i Implementation Notes. |
| BH12 | false | `in-progress` var korrekt under review og settes til `done` i sluttføringen; frozen-begrunnelsen følger malen, og `context` er frivillig og kort. |
| BH13 | false | SCRUM-51 er en stabil saksreferanse, mens memloggen bevarer beslutningsgrunnlaget lokalt; en hardkodet Jira-URL er ikke nødvendig for repoets lesbarhet. |
