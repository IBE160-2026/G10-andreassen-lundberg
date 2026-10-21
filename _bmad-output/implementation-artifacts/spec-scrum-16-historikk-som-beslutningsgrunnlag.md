---
title: 'SCRUM-16: Historikk som synlig beslutningsgrunnlag'
type: 'chore'
created: '2026-10-22'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="Avklart med Odin i samtalen om SCRUM-16">

## Intent

**Problem:** Gjeldende brief beskriver separat plangenerering, mens Odin nå vil støtte lederens valg ved frafall i en eksisterende plan, med tidligere planer som synlig kontekst.

**Approach:** Dokumenter fire uker historikk og ferdig planlagt uke 5 som arbeidsuke. Forslag gjelder håndtering av frafall i uke 5 og erstatter separat generering av en ny ukeplan i MVP. Historikken vises som beslutningsgrunnlag; P1/P2 beholder arbeidsuken som periode, uten skjult historisk rangering. Historikk forblir uendret, forslag gjennomfører ingen vaktendring, og R1–R5 kontrollerer nye foreslåtte tildelinger med nødvendige nabovakter. Oppdater brief, demo, README, VaktMatch-vedlegg, endringslogg og memlog med kilde og riktig opphav. Bevar tidligere innslag og kreditering. Oppdater SCRUM-16 med avklart retning og gjenstående metodevalg, og behold saken In Progress. Ikke velg solver, algoritme, nye prioriteringsregler eller ytelsesløfter i denne dokumentendringen.

</frozen-after-approval>

## Implementation Notes

- Avgrenset dokumentleveranse av allerede avklarte valg; resten av SCRUM-16 er fortsatt åpent. Ingen kode eller komplette datasett inngår.
- Oppdatert brief, demo, README, vedlegg, E31 og memlog; Jira-saken viser gjeldende retning og gjenstående avklaringer. Kontrollert diff, lenkemål og whitespace.
- Kilde: [SCRUM-16](https://stiodi.atlassian.net/browse/SCRUM-16) og kildeoppsummeringen i E31. Odin avklarte historikk/arbeidsuke og synlig kontekst. Codex konkretiserte dataversjon ved kildekorrigering og eksempler for hvilekontroll.

## Review Triage Log

- medium, patch: Innledende begrunnelsessammendrag omtalte fortsatt plangenerering som gjeldende. Merket punktlisten som historisk og lagt til gjeldende retning/gjenstående punkter.
- medium, patch: H1 kunne endre nabovakter med betydning for R4. Begrenset kontrolltilfellet til historikk uten virkning på kontrollgrunnlaget og tydeliggjort at relevante endringer krever ny kontroll.
- low, patch: Ukegrenseeksemplet dekket bare uke 6. Lagt til H5 for uke 4/5 med 11 og 10 timer samt ukjent nødvendig grunnlag.
- medium, patch: Historikkens uforanderlighet var tvetydig ved datasettbytte. Avgrenset til forslag; kildekorrigeringer vises som ny dataversjon og utløser ny berørt vurdering.
- low, patch: Kildehenvisningen var ikke klikkbar. Lagt til Jira-lenke og nøytral kildeoppsummering som skiller brukerens valg og Codex-presiseringer.
