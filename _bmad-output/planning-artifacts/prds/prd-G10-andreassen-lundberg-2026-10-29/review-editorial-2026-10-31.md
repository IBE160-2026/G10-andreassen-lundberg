# Struktur- og språkgjennomgang – PRD, 31.10.2026

PRD-en skal hjelpe gruppen og sensor å finne testbare produktkrav og
beslutningsgrunnlag, og gi videre BMAD-arbeid et presist utgangspunkt.
Utført av Codex etter eksplisitt `skill:bmad-review lenses=structure,prose`
fra PRD-skillens `doc_standards`; bare dokumentet er vurdert.

Strukturmodell: **Strategic/Context (Pyramid)**. Målgruppe: mennesker som
leser dokumentet sammenhengende og slår opp enkeltkrav. Stilgrunnlag:
Microsoft Writing Style Guide, underlagt prosjektets språk- og opphavsregler.
Intendert stil som bevares: konkret norsk bokmål, faste krav-ID-er, tydelige
eksempler og uttrykkelige begrensninger. Ingen ny produktretning foreslås.

`word_metrics.py` målte PRD-versjonen med `updated: 2026-10-30` til **3 910 ord**.
§7.2 har 318 ord, §5 har 303 ord og §2.3 har 393 ord. Ingen lengdegrense er oppgitt.
Strukturpasset er gjennomført før språkpasset, og funnene er ikke anvendt i PRD-en.

| Pass | Original tekst | Revidert tekst / anbefaling | Endring |
|---|---|---|---|
| structure | §7.2 – endringer fra briefen (318 ord) | PRESERVE | Gjentar noe av kravene, men samler før/etter, begrunnelse og opphav som sensor og videre arbeid trenger. Ordreduksjon: 0. |
| structure | §4.7 FR-24 før §4.8 FR-22/23 | PRESERVE | Gruppering etter Må/Bør gjør omfanget lettere å lese. Behold de stabile ID-ene; ikke renummerer for numerisk rekkefølge. Ordreduksjon: 0. |
| prose | UJ-2: «Kari beholder standardgrensen 1 og søker på nytt.» | «Kari setter søkegrensen tilbake til 1 og søker på nytt.» | Flyten har nettopp brukt grense 0; verbet «beholder» beskriver ikke overgangen. |
| prose | NFR-4: «Regelmotoren har automatiske tester for kontrolltilfellene som gjelder Må-krav» | «Automatiske tester på relevante nivåer dekker kontrolltilfellene som gjelder Må-krav» | Kontrolltilfellene omfatter også økt og grensesnitt. Presiser testplasseringen uten å endre omfanget. |
| prose | NFR-5: «gir alltid samme resultat» | Vurder: «gir alltid de samme beregnede alternativene, statusene, rangeringen og kostnadsanslagene» | Gjør det tydelig at determinisme gjelder beregningene, mens KI-tekst skal samsvare i fakta etter FR-19. |

Strukturpasset har ingen anbefalte kutt eller flyttinger. Språkpasset gir tre
små presiseringer, hvorav den siste er formulert som et forslag fordi
«resultat» kan forstås snevrere i den eksisterende sammenhengen. Ingen
reduksjon anbefales: **0 ord / 0 %**. Gjennomgangen ofrer verken eksempler,
opphav eller lesbarhet for kortere tekst. Innholdsmangler og kildesamordning
står i [rubrikkgjennomgangen](review-rubric-2026-10-31.md).

## Hovedagentens triage

De tre ordlydspresiseringene er anvendt og kontrollert i PRD-en 31.10.26.
De endrer ikke funksjonsomfanget. Strukturpunktene er beholdt som anbefalt.
