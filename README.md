# G10 — Claude's disipler

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Gruppen har valgt **VaktMatch**, en webapp for å sammenligne bemanningsalternativer
ved et udekket skift. Repoet inneholder foreløpig produktgrunnlaget og BMAD-oppsettet.

## Produktbrief

**[productbrief.md](productbrief.md) er repoets eneste gjeldende produktbrief.**
Den er fortsatt et utkast: detaljert MVP-omfang, teknologistakk og arbeidsdeling
gjenstår å avklare. At dokumentet er gjeldende, betyr ikke at alle forslagene
i det er endelig vedtatt.

Arbeidsretningen er oppdatert etter Odins innspill 6.–7. oktober: førsteversjonen
bruker en ferdig syntetisk vaktplan som grunnlag og kan generere et enkelt
planforslag, med regelkontroll og konkrete KI-forklaringer. Genereringen beholdes
i MVP; VaktMatch innfører ikke forslaget i den faktiske vaktlisten. Reell
leverandørtilkobling ligger utenfor MVP; hvordan endrede demodata skal
lastes inn og vises, gjenstår å konkretisere. Chat er en mulig senere utvidelse.
Endringene fra 6.–7. oktober er Odins innspill, bearbeidet med Codex, og er ennå
ikke avklart med Stian. De publiseres som et arbeidsutkast for felles vurdering.
Publiseringen innebærer ingen felles godkjenning av endringene.

[Endringsloggen for produktbriefen](docs/productbrief-endringslogg.md) viser
endringene fra første versjon 17. september, med korte begrunnelser, opphav og
status for valgene. Den viser også hvordan alle tekstendringer kan leses i Git.
Start gjerne med [den samlede begrunnelsen for arbeidsutkastet](docs/productbrief-endringslogg.md#hvorfor-arbeidsutkastet-er-endret).

### Dokumentoversikt

| Dokument | Rolle |
|---|---|
| [productbrief.md](productbrief.md) | **Gjeldende produktbrief.** Samle avklarte endringer her før PRD. |
| [Demoscenario for fravær](docs/demoscenario-fravaer.md) | Forslag til kontrollerbare data og forventede svar. Oppdatert til forslag uten vaktendring; ikke et komplett datasett eller vedtatt regelsett. |
| [VaktMatch-vedlegget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/addendum.md) | Supplerende bakgrunn og åpne innspill til hovedbriefen. Ingen selvstendig brief eller utvidelse av vedtatt omfang. |
| [Turnusgenerator – alternativforslag fra Stian](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/brief.md) | Forslag til vurdering. Erstatter ikke hovedbriefen. [Teknisk vedlegg](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/addendum.md) tilhører forslaget. |
| [Forslag til felles retning fra Odin](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/forslag-til-felles-retning.md) og [svar fra Stians KI-assistent](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/svar-til-felles-retning.md) | Beslutningsgrunnlag for gruppen. Ingen felles beslutning om sammenslåing. |
| [Historisk henvisning fra 7. september](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/brief.md) | Erstattet av hovedbriefen 17. september. Beholdt for sporbarhet; skal ikke brukes som grunnlag for PRD. |

Dokumentrollene ble tydeliggjort 6. oktober 2026 etter tilbakemeldingen fra
faglærer. Filplasseringene er beholdt slik at eksisterende referanser fortsatt
virker. Hovedbriefen revideres som arbeidsutkast. Åpne regler, prioriteringer og
omfangsvalg konkretiseres videre før PRD; individuelle innspill og felles
beslutninger skal fortsatt skilles tydelig.

### Tilbakemelding fra faglærer

Bårds tilbakemeldinger fra 6. oktober gjelder dokumentene slik de forelå ved
vurderingen: [hovedbriefen](tilbakemelding-product-brief.md),
[turnusforslaget](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/tilbakemelding-product-brief.md)
og [den historiske henvisningen](_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/tilbakemelding-product-brief.md).

Andre prosjektkandidater og tilhørende research er arkivert i Obsidian, utenfor
repoet. Eldre versjoner finnes fortsatt i Git-historikken.

Se [prosjektreglene](AGENTS.md) for språkhygiene og saklig omtale av personer
i dokumentasjon, beslutningslogger, commits og pull requests.

## Medlemmer

- Odin A Andreassen
- Stian Lundberg

## BMAD

BMAD **6.12.0** er installert for Claude Code og Codex. Produktbriefen utarbeides
med `bmad-product-brief`. Applikasjonens teknologistakk er fortsatt åpen.

Se [BMAD – oppsett og oppstart](docs/bmad-setup.md) for å komme i gang på egen maskin.
