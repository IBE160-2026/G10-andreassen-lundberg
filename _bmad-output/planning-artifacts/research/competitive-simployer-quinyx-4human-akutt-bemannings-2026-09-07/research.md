---
title: 'competitive research: Simployer/Quinyx/4Human vs. VaktMatch'
type: 'competitive'
topic: 'Dekker Simployer, Quinyx, 4Human akutt bemanningsavvik med forklart, sammenlignet beslutningsstøtte?'
decision: 'Om VaktMatchs differensiering ("What Makes This Different" i product brief'en) er ærlig og faktabasert, eller fabrikerer en fordel som allerede finnes'
source: 'native run'
status: complete
preset: 'quick'
validation: 'normal'
claims_verified: 3
claims_unverified: 1
created: '2026-09-07'
updated: '2026-09-07'
---

# competitive research: Simployer/Quinyx/4Human vs. VaktMatch

**Decision this research serves:** Om VaktMatchs differensiering ("What Makes This Different" i product brief'en, `_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07/brief.md`) er ærlig og faktabasert, eller fabrikerer en fordel som allerede finnes hos etablerte WFM/HR-systemer.

## Executive Summary

Ingen av de tre undersøkte leverandørene — Simployer, Quinyx, 4Human — dokumenterer i dag (offentlig markedsføring/produktdokumentasjon) den spesifikke egenskapen VaktMatch bygger differensieringen sin på: et lite sett **rangerte, forklarte** alternativer (intern omfordeling / overtid / ekstern vikar) ved et akutt bemanningsavvik, hver annotert med kompetansematch, hviretidsoverholdelse, beregnet overtid og konsekvens for andre vakter. Alle tre er dokumentert på nivået "registrer fravær → varsle leder → la leder manuelt finne/tildele erstatning", pluss generell compliance-/lovverkstøtte som eget innholdstema, ikke en sanntids beslutningsmotor.

**Konklusjon for brief'en:** Differensieringspåstanden i "What Makes This Different" holder — men bør formuleres presist ("forklart, rangert, regelsjekket beslutningsstøtte i akuttøyeblikket", ikke "ingen andre gjør bemanningsplanlegging") og med **medium**, ikke høy, sikkerhet — se forbehold under.

**Viktigste forbehold:** Dette er et raskt søk (quick-preset, 1 runde, offentlige kilder). Ingen av produktenes salgs-gatede/dybde AI-funksjoner (f.eks. Quinyx' AI-planlegging/"Copilot"-linje) eller demo-/videomateriale ble undersøkt. Simployers "Finn vikar"-funksjon — den nærmeste kandidaten til å allerede løse dette — kunne ikke inspiseres direkte (dokumentasjonssiden ga 502-feil). Én Quinyx-påstand om "intelligent logikk" for omfordeling er uverifisert (ref [3]).

## Funksjons-teardown for akutt fraværshåndtering

**Spørsmål:** Når et skift blir udekket pga. sykefravær, viser produktet rangerte/sammenlignede handlingsalternativer med forklaring på kompetanse- og hviletidsoverholdelse — eller er håndteringen begrenset til registrering, varsling og manuelt søk/tildeling?

**Simployer** (inkl. Capitech Tid & Plan) — fraværs-/vikarhåndtering er dokumentert som registrering (OAS-modulen), varsling til leder, oversikt, vaktplan-integrasjon og en "Finn vikar"-funksjon for manuelt å finne og tildele erstatning, pluss automatisk overtids-/lønnsberegning på faktisk arbeidet tid. Ingen kilde beskriver rangering eller forklaring av alternativer før leder velger. [1] "Finn vikar" er den nærmeste kandidatfunksjonen, men dens beslutningslogikk (filtrerer den på kompetanse/hviletid internt?) kunne ikke bekreftes — dokumentasjonen var utilgjengelig ved henting (502). Dette er et åpent hull, ikke et negativt funn.

**Quinyx** — Absence Management og "Shift Cover" markedsføres som "finn erstattere raskt" og "få andre til å dekke umiddelbart" ved sent sykefravær, samt generell AI-drevet planlegging basert på ferdigheter/tilgjengelighet/arbeidsmengde (for *plangenerering*, ikke sykefraværserstatning). [2] Et søketreff antydet at Quinyx har "intelligent logikk" som vurderer ferdigheter/tilgjengelighet/avtaler/tidsregler ved omfordeling av vakter — nærmest konseptet av alle tre — men dette kunne ikke bekreftes ved direkte gjenhenting av kildesiden. [3, uverifisert] Bør undersøkes videre før det eventuelt siteres som et konkurransetrekk i PRD.

**4Human** — Arbeidsplan- og Sykefraværsoppfølging-modulene dekker fraværsregistrering, automatiske varsler, visuell fraværskalender, NAV/Altinn-integrasjon for oppfølgingsplan og statisk kompetanseregistrering på stillingsnivå. Ingen rangert/forklart beslutningsstøtte ved et konkret dekningsgap funnet. [4]

**Konklusjon:** Alle tre leverandører løser *registrering og oversikt* godt, og har (i varierende grad) en "finn noen til å dekke"-mekanisme — men ingen dokumenterer en **forklarende, regelsjekket sammenligning** av alternativer på beslutningsøyeblikket. Dette er det konkrete hullet VaktMatchs kjernekonsept sikter mot.

## Kildetabell

| # | Kilde | Publisert av | Hentet |
|---|---|---|---|
| [1] | support.simployer.com (OAS), simployer.com/products/hrm/absence-time-tracking, capitech.no/produkter/tid-og-fravar, support.simployer.com (versjon 15.19), simployer.com/no/artikler, g2.com/products/simployer/reviews | Simployer / Capitech / G2 | 2026-09-07 |
| [2] | quinyx.com/absence-management-software, quinyx.com/staff-rota, g2.com/products/quinyx/features | Quinyx / G2 | 2026-09-07 |
| [3] | quinyx.com/absence-management-software (søketreff, ikke bekreftet ved direkte henting) | Quinyx | 2026-09-07 |
| [4] | 4human.no/hrm/arbeidsplan, 4human.no/hrm/sykefravaersoppfolging, 4human.no/hrm/core-hr/kompetanse, 4human.no/hrm/kompetanseoversikt | 4human | 2026-09-07 |

## Tverrdimensjonale innsikter

Kun én dimensjon ble kjørt denne runden (funksjons-teardown) — ingen tverrdimensjonal innsikt å rapportere.

## Motstridende funn

Ingen red-team-runde ble kjørt (utenfor omfanget for denne quick-sjekken).

## Anbefalinger

1. **Behold differensieringspåstanden i brief'ens "What Makes This Different", men presiser den.** Skriv eksplisitt at VaktMatch fyller et hull i *forklart, regelsjekket beslutningsstøtte i akuttøyeblikket* — ikke en påstand om at ingen konkurrenter finnes i bemanningsplanlegging generelt. Confidence: medium (basert på [1][2][4]). **Feeds:** brief → "What Makes This Different"; senere PRD → differensieringsgrunnlag.
2. **Ikke siter Quinyx' "intelligente omfordelingslogikk" som et konkurransefortrinn VaktMatch mangler**, siden påstanden er uverifisert [3]. Hvis dette skal brukes i refleksjonsrapporten som "vi undersøkte konkurrenter grundig", bør denne ene påstanden enten verifiseres først eller utelates.
3. **Simployers "Finn vikar" er den reelle risikoen å holde øye med** — den nærmeste kandidatfunksjonen kunne ikke inspiseres. Hvis gruppen har mer tid før PRD, er dette det ene stedet en dypere sjekk (Deepen) gir mest verdi.

## Åpne spørsmål / ikke undersøkt

- Simployers "Finn vikar"-beslutningslogikk i detalj (dokumentasjon utilgjengelig denne runden).
- Quinyx' AI-planlegging/"Copilot"-produktlinje, som kan ligge nærmere konseptet enn det som ble funnet.
- Salgs-gatede/demo-only funksjoner hos alle tre — kun offentlig markedsføring/dokumentasjon er dekket.
- Faktisk brukeropplevelse (få relevante anmeldelser funnet for noen av de tre på akkurat denne funksjonaliteten).

**Stoppet fordi:** dekning — spørsmålet er besvart for alle tre med medium-høy sikkerhet innenfor quick-presetets én runde; gjenværende hull er rapportert over, ikke forsøkt lukket i denne runden (jf. avtalt omfang).

## Staleness-kart

Alle fire kjernepåstander er klassifisert som `features` (kursets pack-terskel: funksjoner/pricing ≤ 3 mnd). Beregnet med `recon_kit.py staleness`, ikke telt for hånd:

| Ref | Påstand | Publisert | Bør sjekkes på nytt |
|---|---|---|---|
| [1] | Simployer: ingen rangert/forklart beslutningsstøtte funnet | 2026-09 | 2026-12-01 |
| [2] | Quinyx: varsling + manuell dekning, ikke rangert/forklart | 2026-09 | 2026-12-01 |
| [3] | Quinyx: uverifisert påstand om intelligent omfordelingslogikk | 2026-09 | 2026-12-01 |
| [4] | 4Human: ingen rangert/forklart beslutningsstøtte funnet | 2026-09 | 2026-12-01 |

Ingen påstander er foreldet i dag. Tidligste re-sjekk: **2026-12-01** — godt utenfor proposal-fristen, så dette blokkerer ikke leveransen. Bruk `bmad-deep-recon` Refresh senere hvis dette skal gjenbrukes i PRD mot slutten av semesteret.
