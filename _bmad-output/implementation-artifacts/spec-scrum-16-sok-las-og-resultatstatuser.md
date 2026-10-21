---
title: 'SCRUM-16: Avklar søk, låste vakter og resultatstatuser'
type: 'chore'
created: '2026-10-22'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="Odins tilslutning til anbefalingene med ulike implementeringsnivåer">

## Intent

**Problem:** SCRUM-16 mangler konkrete nivåer for låste tildelinger, søkemetode og resultatstatuser etter avklart historikk og arbeidsuke.

**Approach:** Konkretiser anbefalingene Odin sluttet seg til: låste/påbegynte/gjennomførte vakter beskyttes; førsteversjonen bruker avgrenset regelbasert søk etter direkte erstatning og opptil én flytting, med P1/P2 og synlig historikk; tilbud/aksept simuleres; full dekning, delvis dekning, ingen funn, manglende data og avbrutt søk skilles. Solver og to eller flere flyttinger er vurderingspunkter for senere utvidelse. Dokumenter begrunnelse, kontrolltilfeller og målemetode uten løfte om responstid. Oppdater brief, demo, README, endringslogg og memlog med tydelig skille mellom Odins overordnede tilslutning og Codex sine detaljer. Kontroller dokumentasjonen og avslutt avklaringssaken dersom kriteriene er oppfylt. Ingen appkode, komplett datasett eller fullført funksjonsimplementering skal påstås.

</frozen-after-approval>

## Implementation Notes

- Liten dokumentleveranse med ett mål: ferdigstille beslutningsgrunnlaget i SCRUM-16. Tidligere kilder og historikk bevares.
- Avklart metode, låsegrenser, separat dekning/regelfunn/søkestatus og målemetode i docs/forslag-ved-frafall.md; brief, demo, README, E32 og memlog samkjørt. Ingen appfunksjoner eller måltall er påstått ferdige.
- Kontrollert diff, interne lenkemål og whitespace; uavhengig gjennomgang er behandlet nedenfor.

## Review Triage Log

- medium, patch: Fraværendes opprinnelige tildeling var ikke eksplisitt deaktivert i sluttplanberegning. Presisert kildehistorikk/fraværsmarkering og utelatelse fra aktiv bemanning og arbeid, med fraværstid separat.
- medium, patch: Søket beskrev bare komplette B/C-kombinasjoner selv om delvis dekning skulle vises. Lagt til konsekvensalternativ med B på X og Y udekket, uten rangering eller full løsningsaksept.
- medium, patch: Låser manglet tilknytning til data og overgangsregler. Presisert versjonstilknytning, synlige endringer og ny vurdering; gamle svar arves ikke automatisk.
- medium, patch: Påbegynt målskift ga ingen passende søkestatus. Lagt til «Ikke kjørt – utenfor omfang» og kontrolltilfelle ved nøyaktig vaktstart.
