---
title: 'SCRUM-15: Avklar søkeomfang og fraværshåndtering'
type: 'chore'
created: '2026-10-21'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="Avklart av Odin i samtalen; behold beslutningen">

## Intent

**Problem:** Søkeomfang, grense for interne flyttinger og simulering av tilbud og aksept står fortsatt åpne i produktgrunnlaget, selv om Odin nå har avklart SCRUM-15.

**Approach:** Dokumenter lederstyrt søkegrense 0 eller 1 eksisterende vakttildeling, med 1 som standard og grense i førsteversjonen. Direkte erstattere inngår også når grensen er 1. To flyttinger er neste mulige utvidelse etter vurdering av kompleksitet og målt responstid; flere er bare en senere mulighet. Tilbud og aksept skal kunne simuleres som sendt, venter, akseptert eller avslått; det enkle eksemplet kan kjøres uten steget. Demogrunnlaget skal vise flere fungerende alternativer og lederens valg. Registrer valgene som tatt av Odin innenfor tidligere dokumentert felles delegering. Oppdater eksisterende brief, demo, endringslogg, memlog og README, kontroller konsistens og lukk avklaringssaken med commit-referanse. Dette er en dokumentasjonsleveranse; komplette datasett og applikasjonskode hører til videre implementering.

</frozen-after-approval>

## Implementation Notes

- Liten, reverserbar dokumentendring med avklart innhold; ingen ny funksjonsimplementering eller publisering inngår.
- Oppdatert produktbrief, demoscenario, README og endringslogg E29. Kort beslutningsinnslag er skrevet med memlog-verktøyets append-kommando.
- Kontrollert lokal lenkeoppløsning, hele diffen og whitespace. Fullstendige datasett og kode er fortsatt videre implementeringsarbeid; avklaringssaken krever beslutningsgrunnlaget.

## Review Triage Log

- medium, patch: R1–R3 var bundet til hovedvaktens K1 og 08–16; presisert per-vakt-kontroll og fjerning av flyttede tildelinger før sluttplankontroll.
- medium, patch: P1/P2 ved omfordeling manglet angitt person; videreført kandidatbasert sortering for den som dekker fraværsvakten etter hele omfordelingen, med eget sammenligningseksempel. Opphav er ført som Codex-presisering.
- low, patch: F2 manglet negativt tilfelle med grense 0; forventningen er nå eksplisitt for både 0 og 1.
- medium, patch: Simulert aksept manglet avgrensning til forslag og data; presisert at endringer krever ny vurdering og ikke arver aksept automatisk.
