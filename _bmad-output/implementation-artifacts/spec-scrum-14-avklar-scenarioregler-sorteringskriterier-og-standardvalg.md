---
title: 'SCRUM-14: Avklar scenarioregler, sorteringskriterier og standardvalg'
type: 'feature'
created: '2026-10-21'
status: 'done'
route: 'dispatch'
review_loop_iteration: 0
baseline_commit: '20e1ff3c85efce4e6f0d248fd9a6c102a3f08e15'
context:
  - '{project-root}/AGENTS.md'
  - '{project-root}/productbrief.md'
  - '{project-root}/docs/demoscenario-fravaer.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Produktbriefen kan ikke danne et stabilt grunnlag for PRD og implementering før de foreslåtte scenarioreglene, regelkildene, sorteringskriteriene, standardvalget og håndteringen av lik rangering er avklart. Eksisterende scenario inneholder et godt forslag, men markerer det korrekt som ikke vedtatt.

**Approach:** Vedta fem eksplisitte regler, nøkterne kildekategorier og deterministisk sortering. Odin opplyste 2026-10-21 at han og Stian samme dag ble enige om at begge kan ta prosjektbeslutninger alene for å få arbeidet i gang. Valgene i denne saken behandles derfor som prosjektbeslutninger innenfor den felles delegeringen, med Odin som kilde til møtereferatet.

## Boundaries & Constraints

**Always:** Skill scenarioregel fra full juridisk kontroll; vis regel-ID, terskel, kategori, kilde og begrensning. Regelstatus og sortering skal være separate. Bare kandidater som består alle reglene rangeres. Kandidater med avvik eller uavklart kontrollgrunnlag skal fortsatt kunne undersøkes. Oppgi at beslutningsmyndigheten bygger på felles delegering gjengitt av Odin, ikke på taushet eller antatt godkjenning av de konkrete reglene.

**Never:** Ikke lov generell lovlighet, ikke modeller tariffunntak eller overtid som om de var dekket, ikke la manglende sorteringsdata endre regelstatus, og ikke skriv at Stian personlig valgte de konkrete reglene når kilden bare er den delegerte beslutningsmyndigheten.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Komplett og godkjent kandidat | R1–R5 består; valgte sorteringsdata finnes | Kandidaten inngår i rangeringen med synlig begrunnelse | Ingen |
| Kjent regelbrudd | Minst én regel har et dokumentert brudd | Status `regelavvik`; kandidaten rangeres ikke, men kan undersøkes | Vis regel, verdier og konsekvens |
| Manglende kontrolldata | Ingen kjent feil, men en nødvendig verdi mangler | Status `uavklart`; kandidaten rangeres ikke | Vis hva som mangler og hvilken kontroll som stoppet |
| Manglende sorteringsdata | R1–R5 består, men valgt kriterium mangler data | Regelstatus beholdes; kandidaten vises separat som ikke fullstendig rangerbar | Ikke bytt kriterium uten å vise det |
| Lik verdi | To kandidater er like på alle valgte kriterier | Kandidatene vises som likeverdige | Stabil ID kan styre visningsrekkefølge, men er ikke et faglig skille |

## Beslutninger

* R1 kompetanse, R2 tilgjengelighet og R3 kollisjon vedtas som interne scenarioregler.
* R4 minst 11 timers hvile og R5 høyst 40 timer i sju dager vedtas som forenklede scenarioregler med lovutgangspunkt og tydelige forbehold om unntak og andre grenser.
* P1 færrest planlagte timer etter tildeling er standard. P2 lavest andel av avtalt timetall er valgfritt. Valgte kriterier kan prioriteres; full likhet vises som lik rangering.
* Valgene innarbeides i produktbrief, scenario, endringslogg og memlog.
* Beslutningen er tatt av Odin innenfor felles delegert beslutningsmyndighet avtalt i møte 2026-10-21, slik Odin har gjengitt møtet.

</frozen-after-approval>

## Code Map

- `productbrief.md` — gjeldende brief; åpne regler og sortering står særlig under The Solution og Scope.
- `docs/demoscenario-fravaer.md` — eksisterende R1–R5, P1–P2, fasit, kanttilfeller og regneeksempel som skal gjenbrukes.
- `docs/productbrief-endringslogg.md` — obligatorisk endringslogg dersom produktbriefen endres; må bevare opphav og beslutningsstatus.
- `.memlog.md` — kort prosesshukommelse; nytt innslag skal skrives via `_bmad/scripts/memlog.py append`.
- `tilbakemelding-product-brief.md` — faglærerens krav om 3–5 tallfestede regler, enkel synlig prioritering og regneeksempel.
- Lovdata, arbeidsmiljøloven §§ 10-4 og 10-8 — primærkilder for henholdsvis 40 timer i sju dager og 11 timers arbeidsfri; kildene gir også grunn til tydelige forbehold om unntak.
- `SCRUM-51` — Jira-regelen må samkjøres med den felles delegeringen uten å etablere en parallell beslutningslogg.

## Tasks & Acceptance

**Execution:**
- [x] `productbrief.md` — erstatt det åpne regel-/sorteringspunktet med vedtatt prosjektretning og dokumentert grunnlag for delegasjonen.
- [x] `docs/demoscenario-fravaer.md` — oppdater kategorier, kilder, standardvalg og deterministisk håndtering av likhet/manglende sorteringsdata.
- [x] `docs/productbrief-endringslogg.md` — registrer før/etter, begrunnelse, opphav og at beslutningen er tatt innenfor den felles delegeringen gjengitt av Odin.
- [x] `.memlog.md` — før ett kort innslag med verktøyet prosjektreglene krever.
- [x] `SCRUM-51` — samkjør administratorregelen med delegert beslutningsmyndighet; behold krav om sporbarhet og avklaring ved sletting eller historikkomskriving.
- [x] `SCRUM-14` — kommenter resultat og flytt først til review når dokumentene er kontrollert.

**Acceptance Criteria:**
- Given en kandidat og komplett grunnlag, when R1–R5 kontrolleres, then hvert utfall kan etterprøves fra navngitt regel, terskel og kildekategori.
- Given flere godkjente kandidater, when prioriteringen endres, then rangeringen følger valget uten å endre regelstatus.
- Given manglende data eller lik verdi, when resultatet vises, then systemet hevder verken komplett kontroll eller et faglig skille uten grunnlag.
- Given den felles delegeringen gjengitt av Odin, when Odin tar dette valget, then det registreres som prosjektbeslutning med tydelig kilde uten å tilskrive Stian de konkrete regelvalgene.

## Implementation Notes

- Dokumentkontroller dekker alle fem radene i I/O- og kanttilfelletabellen.
- Denne installasjonen av `memlog.py` har ikke `check`-kommandoen som var foreslått under Verification. Innslaget ble skrevet med obligatorisk `append`, og frontmatter samt det nye innslaget ble kontrollert lesende.

## Spec Change Log

## Review Triage Log

| ID | Funn | Dom | Rute og kontrollgrunnlag |
|---|---|---|---|
| BH1 | E28 ble fortsatt brukt som mal-ID. | low | patch — E28 er nå et faktisk innslag; malen er flyttet til E29. |
| BH2 | Verification viser en `memlog.py check`-kommando som ikke finnes. | low | rejected — funnet er reelt, men minste rettelse er bare å redigere denne build-spesifikasjonen; faktisk append og lesende kontroll står i Implementation Notes. |
| BH3 | R1–R3 viste kategori, men ikke beslutningskilde på regelnivå. | low | patch — hver tabellrad viser nå Odin 21.10.26 som beslutningskilde. |
| BH4 | Standardlisten og hvordan P1/P2 aktiveres og ordnes var tvetydig. | medium | patch — standard er `[P1]`; aktivering, deaktivering og rekkefølge er presisert. |
| BH5 | Kandidat med manglende data i en prioritert kriterieliste var underspesifisert. | medium | patch — kandidaten holdes utenfor komplett rangering; tidligere verdier kan vises, mens komplette kandidater fortsatt rangeres. |
| BH6 | Lik rangering og manglende sorteringsdata manglet regneklare scenarioer. | medium | patch — S4 og S5 er lagt til med forventet resultat. |
| BH7 | Scope beholdt det gamle intervallet «3–5» etter at fem regler var vedtatt. | low | patch — Scope viser nå R1–R5. |
| BH8 | Tidsperioden var omtalt som uke, samme periode og sju dager uten én beregningsregel. | medium | patch — P1, P2 og R5 bruker samme faste mandag–mandag-periode, og bare overlappende tid ved grensene teller. |
| BH9 | Implementation Notes oppga matrisedekning uten reproducerbare påstander i Verification-listen. | low | rejected — matrisepåstandene ble faktisk kjørt og besto i implementeringssteget; en rettelse av kommandolisten ville bare endre build-spesifikasjonen. |
| EC1 | Manglende forrige eller neste vakt skilte ikke komplett historikk fra manglende data. | medium | patch — komplett fravær av nabovakt består den siden; ufullstendig historikk gir uavklart. |
| EC2 | En vakt over periodegrensen manglet regel for hvilke timer som teller. | medium | patch — samme rotårsak som BH8; bare skjæringen med den faste perioden teller. |
| EC3 | Den ikke-eksisterende `check`-kommandoen ville feile. | low | rejected — duplikat av BH2 og rettelsen ville bare endre build-spesifikasjonen. |
| VG1 | Verifikasjonsgap: `check` er angitt selv om verktøyet bare støtter `init`, `append` og `set`. | low | rejected — duplikat av BH2/EC3; faktisk lesende kontroll er dokumentert i Implementation Notes. |

## Verification

**Commands:**
- `python _bmad/scripts/memlog.py check .memlog.md` -- forventet: gyldig loggformat.
- `rg -n "R1|R2|R3|R4|R5|P1|P2|11 timer|40 timer|lik rangering" productbrief.md docs/demoscenario-fravaer.md docs/productbrief-endringslogg.md` -- forventet: konsistent terminologi og sporbarhet.
- `git diff --check` -- forventet: ingen whitespace-feil.
