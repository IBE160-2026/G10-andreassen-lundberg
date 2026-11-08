---
name: VaktMatch
description: Lesbar arbeidsflate for sammenligning av bemanningsalternativer i en lokal studieprototype.
title: VaktMatch – visuell utforming
status: final
created: 2026-10-31
updated: 2026-11-08
issue: SCRUM-47
authorship: Codex-konkretisering på Odins gjennomføringsmandat 2026-11-08.
validation: KI-kontrollert designgrunnlag; ikke brukertestet eller felles detaljgodkjenning.
sources:
  - ../../prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md
  - ../../../../productbrief.md
  - ../../../../docs/demoscenario-fravaer.md
  - ../../../../docs/kostnadsanslag.md
  - ../../research/domain-egenmelding-varsling-og-fravarsperiode-2026-10-31/research.md
  - ../../../../docs/forslag-ved-frafall.md
colors:
  background: '#F3F5F2'
  surface: '#FFFFFF'
  ink: '#172C2A'
  ink-secondary: '#52645E'
  primary: '#123D3A'
  on-primary: '#FFFFFF'
  primary-soft: '#E5F0E9'
  positive: '#22563A'
  positive-soft: '#E5F0E9'
  caution: '#79520C'
  caution-soft: '#FFF3D6'
  negative: '#9A2D30'
  negative-soft: '#FBE9E8'
  border: '#708079'
  divider: '#D7DFD8'
  focus: '#1A665D'
typography:
  heading:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.025em
  section:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1.25rem
    fontWeight: '650'
    lineHeight: '1.35'
  body:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 0.875rem
    fontWeight: '650'
    lineHeight: '1.45'
  meta:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 24px
  '6': 32px
  '7': 48px
  margin-mobile: 16px
  margin-desktop: 32px
  content-max: 1280px
  control-min: 44px
components:
  app-header:
    backgroundColor: '{colors.surface}'
    textColor: '{colors.ink}'
    padding: '{spacing.5}'
  demo-banner:
    backgroundColor: '{colors.primary-soft}'
    textColor: '{colors.primary}'
  step-navigation:
    textColor: '{colors.ink-secondary}'
  week-overview:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  absence-form:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  affected-shifts:
    backgroundColor: '{colors.background}'
    rounded: '{rounded.md}'
  shift-context:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  search-controls:
    backgroundColor: '{colors.surface}'
  alternative-card:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  status-badge:
    rounded: '{rounded.full}'
  alternative-detail:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  plan-proposal:
    backgroundColor: '{colors.primary-soft}'
    rounded: '{rounded.md}'
  fact-table:
    textColor: '{colors.ink}'
  explanation-panel:
    backgroundColor: '{colors.background}'
    rounded: '{rounded.md}'
  offer-panel:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  dataset-panel:
    backgroundColor: '{colors.surface}'
    rounded: '{rounded.lg}'
  session-history:
    backgroundColor: '{colors.background}'
  message-panel:
    backgroundColor: '{colors.caution-soft}'
    textColor: '{colors.caution}'
  action-button:
    backgroundColor: '{colors.primary}'
    textColor: '{colors.on-primary}'
    rounded: '{rounded.md}'
    height: '{spacing.control-min}'
---

# VaktMatch – visuell kontrakt

## Brand & Style

VaktMatch fremstår som et rolig arbeidsverktøy: tydelige tall, korte forklaringer
og én fremhevet handling per oppgavesteg. Hovedinnholdet er vakter og konsekvenser,
med plass til å lese både alternativer og forbehold. Retningen er valgt av Codex
på [Odins mandat](.working/delegated-decisions-2026-11-08.md), ikke hentet fra en
etablert profil eller brukerundersøkelse. `final` betyr ferdigstilt UX-grunnlag.

[EXPERIENCE.md](EXPERIENCE.md) eier oppførselen. Dokumentparet gjelder foran
mockups ved konflikt. De [statiske skjermreferansene](mockups/key-alternativer.html)
viser komposisjon; [prototypen](mockups/prototype.html) viser utvalgte interaksjoner
med eksplisitt konstruert innhold, uten regelmotor eller modellkall.

## Colors

| Bruk | Tokenpar | Minstekrav |
|---|---|---|
| Hovedtekst | `{colors.ink}` på `{colors.surface}` / `{colors.background}` | 4,5:1 |
| Sekundærtekst, også metadata | `{colors.ink-secondary}` på de samme flatene | 4,5:1 |
| Primærhandling | `{colors.on-primary}` på `{colors.primary}` | 4,5:1 |
| Bestått kontroll | `{colors.positive}` på `{colors.positive-soft}` | 4,5:1 |
| Uavklart, mangler, utdatert | `{colors.caution}` på `{colors.caution-soft}` | 4,5:1 |
| Regelavvik og inputfeil | `{colors.negative}` på `{colors.negative-soft}` | 4,5:1 |
| Fokus og kontrollgrenser | `{colors.focus}` / `{colors.border}` på lys flate | 3:1 mot tilstøtende flate |

Farge suppleres alltid med tekst. «Oppfyller scenarioreglene» er grønt; rangering,
valg, tilbudssvar og faktisk bemanning er separate størrelser med egne etiketter.
`{colors.divider}` er dekorativ skillelinje og erstatter aldri en kontrollgrense.
Ingen gradienter, fargekodede personer eller dempet tekst under kontrastkravet.

## Typography

Systemfont brukes uten nedlasting. `{typography.heading}` brukes én gang per
oppgaveflate, `{typography.section}` på paneloverskrifter og kandidatnavn,
`{typography.body}` på forklaring og tall. `{typography.label}` er synlige
feltetiketter; `{typography.meta}` er dataversjon, periode og kilde.
Tall settes med tabulære sifre. NOK skrives «1 800 kr» og differanse «+1 800 kr»;
mangler skrives «Uavklart», aldri «0 kr». Ingen viktige tall eller navn avkortes.

## Layout & Spacing

Innholdet sentreres innen `{spacing.content-max}`. Ved minst 1024 px brukes
en kontekstkolonne på omtrent 320 px og en fleksibel arbeidskolonne, med
`{spacing.5}` mellom. Under 1024 px stables innholdet i samme DOM-rekkefølge.
Mobil har `{spacing.margin-mobile}` sidemarg, PC `{spacing.margin-desktop}`.
Avstand innad i en gruppe er `{spacing.2}`–`{spacing.4}`, mellom grupper
`{spacing.5}`–`{spacing.6}`. Bruk fleksible mål; tekstzoom skal kunne utvide felter.

[Ukesoversikten](mockups/key-ukeplan.html) viser én rad per dato/vakt i en
lesbar liste; PC kan samle radene i et rutenett. [Fraværsflaten](mockups/key-fravaer.html)
har skjema og forhåndsvisning før handling. [Alternativoversikten](mockups/key-alternativer.html)
viser sammenlignbare kort i én liste. [Detaljene](mockups/key-detaljer.html) viser
hele før/etter-forslaget, med alle berørte, uten å ligne en gjennomført planendring.

## Elevation & Depth

Hvite flater, avstand og `{colors.divider}` gir hierarki. Kort har ingen
obligatorisk skygge. Valgt kort får synlig kant og tekst «Valgt i økten»;
fokus får egen ring og må fortsatt skilles fra valg. Ingen dialog er nødvendig
for den lange detaljflaten, historikken eller tilbudssimuleringen.

## Shapes

Kontroller og faktagrupper bruker `{rounded.md}`, hovedpaneler `{rounded.lg}`.
Små markeringer bruker `{rounded.sm}`. `{rounded.full}` er for statusmerker.
Ikoner er enkle linjesymboler med tekst; personbilder og dekorative illustrasjoner
er ikke del av kontrakten.

## Components

Navnene under er felles med EXPERIENCE.md. Alle fokuserbare kontroller har
synlig ring på minst 3 px, med 2 px avstand og `{colors.focus}`.

| Komponent | Visuell spesifikasjon |
|---|---|
| app-header | Produktnavn, arbeidsuke, dataversjon og tilgang til datagrunnlag; kompakt lys flate. |
| demo-banner | Vedvarende tekst om syntetiske data og at ingen vakter endres; markert lys grønn flate. |
| step-navigation | Nummer og navn «Fravær», «Alternativer», «Valg»; aktuelt steg har understrek og tekstmarkering. |
| week-overview | Dato, start/slutt, kompetansebehov, tildelte og udekket behov; lås vises med forklarende tekst. |
| absence-form | Synlige etiketter over ansatt, startvakt, kalenderdager og valgt målskift; innrammede kontroller, hjelpetekst og lokal feiltekst. |
| affected-shifts | Full datoperiode og vaktliste med radiovalg; begge datoer ved nattvakt, beskyttede vakter tydelig merket. |
| shift-context | Aktuelt målskift, fraværende, behov og gjeldende udekket bemanning; kort sammendrag synlig ved resultatet. |
| search-controls | Merket søkegrense, aktive P-kriterier og felt for prioritert rekkefølge; nøytral flate. |
| alternative-card | Rangering, kandidat/flytting, dekning og kontroll øverst; timer/hvile, kostnad/differanse og datamangler følger før «Undersøk». |
| status-badge | Tekst innen kontrastparet for den aktuelle dimensjonen; korte merker brytes over flere linjer ved behov. |
| alternative-detail | Overskrift, tilbakehandling og samme status/kostnad som kortet; videre rekkefølge er plan, regler, konsekvenser, historikk, forklaring og valg. |
| plan-proposal | Før/etter for hver berørt vakt, med egen etikett «Forslag» og synlig påminnelse om uendret faktisk plan. |
| fact-table | Radetiketter og enheter, synlig før/etter og kilde/mangler; på mobil stablede navngitte rader uten horisontal rulling. |
| explanation-panel | Standardforklaring først; KI-svar får fire navngitte tekstfelt og egen opphavs-/reservestatus. |
| offer-panel | Valgt forslag/versjon og en rad per berørt person med svarstatus og demohandlinger. |
| dataset-panel | Gammel/ny versjon og endringsoversikt før innlasting; endrede data fremheves med tekst. |
| session-history | Egen seksjon merket «Tidligere valg»; gammel versjon og svar står sammen, aldri med nåværende valgtmarkering. |
| message-panel | Overskrift, konkret årsak og vei videre; inputfeil bruker negativt fargepar, mangler/advarsler varselfargeparet. |
| action-button | Minst `{spacing.control-min}` høyde, tydelig tekst; sekundær hvit variant med `{colors.border}`; deaktivert har lesbar grunn ved siden av. |

## Do's and Don'ts

| Gjør | Unngå |
|---|---|
| Vis oppgave, dataversjon og begrensninger ved tallene. | Gjør informasjon avhengig av hover eller små ikoner. |
| Behold samme feltrekkefølge på mobil og PC. | Skjul hvile, mangler eller berørte personer på smal skjerm. |
| Skill «Valgt», kontroll, forslagets dekning og tilbudssvar med tekst. | La et grønt merke bety at vakten er bemannet eller juridisk godkjent. |
| Bruk synlig knapp til å undersøke og en egen til å velge. | Gjør hele kortet til flere overlappende klikkmål. |
| Merk nye eksempeldata som konstruerte. | Presenter prototypens tall som ferdig beregnet fasit. |

[Kontrollrapporten](validation-report.md) viser kilde-, kontrast- og
prototypekontrollen. [Overleveringen](implementation-handoff.md) knytter
kontrakten til eksisterende implementeringssaker.
