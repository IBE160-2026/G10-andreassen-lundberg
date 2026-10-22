# G10 — Claude's disipler

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Gruppen har valgt **VaktMatch**, en webapp for å sammenligne bemanningsalternativer
ved et udekket skift. Repoet inneholder foreløpig produktgrunnlaget og BMAD-oppsettet.

## Produktbrief

**[productbrief.md](productbrief.md) er repoets eneste gjeldende produktbrief.**
Den er fortsatt et utkast: detaljert MVP-omfang, teknologistakk og arbeidsdeling
gjenstår å avklare. At dokumentet er gjeldende, betyr ikke at alle forslagene
i det er endelig vedtatt.

Arbeidsretningen er oppdatert etter avklaringen i SCRUM-16: førsteversjonen
bruker fire uker historikk og en ferdig planlagt uke 5. Ved frafall sammenligner
lederen forslag med regelkontroll, synlig historisk kontekst og KI-forklaringer.
Separat generering av en ny ukeplan er tatt ut av MVP. VaktMatch innfører ikke
forslagene i den faktiske vaktlisten. Reell
leverandørtilkobling ligger utenfor MVP; oppdaterte demodata lastes inn gjennom
en demohandling som viser endringer og beregner vurderingen på nytt. Chat er en mulig senere utvidelse.
Endringene fra 6.–7. oktober er Odins innspill, bearbeidet med Codex, og er ennå
ikke avklart med Stian. De publiseres som et arbeidsutkast for felles vurdering.
Publiseringen innebærer ingen felles godkjenning av endringene.

Avklaringer fra 21. oktober er innarbeidet i briefen og demoscenarioet: R1–R5,
sortering og lederstyrt søkegrense 0–1, med 1 som standard i førsteversjonen.
Tilbud og aksept skal kunne simuleres; det enkle eksemplet kan kjøres uten steget.
Valgene er tatt av Odin innenfor felles delegert beslutningsmyndighet, slik han
har gjengitt avtalen med Stian. Se endringsloggen E28–E32 for opphav og avgrensning.
SCRUM-17 avklarer simulert fravær, bytte mellom forhåndslagde datasett og
komplettering av manglende opplysninger i demoen. Valg og simulerte svar beholdes
i økten; varig beslutningslogg er valgfri, avslått som standard, med frivillig begrunnelse.

Avklaringen 22. oktober gjør tidligere planer til synlig beslutningsgrunnlag,
uten en ny historisk poengsum eller endring i P1/P2. [Søk og låste vakter](docs/forslag-ved-frafall.md)
beskriver førsteversjonens avgrensede regelbaserte søk, beskyttede tildelinger,
resultatstatuser og målemetode. Solver og lengre kjeder vurderes senere.
Dette er avklart produktgrunnlag; appkode og målinger gjenstår.

[Endringsloggen for produktbriefen](docs/productbrief-endringslogg.md) viser
endringene fra første versjon 17. september, med korte begrunnelser, opphav og
status for valgene. Den viser også hvordan alle tekstendringer kan leses i Git.
Start gjerne med [den samlede begrunnelsen for arbeidsutkastet](docs/productbrief-endringslogg.md#hvorfor-arbeidsutkastet-er-endret).

### Dokumentoversikt

| Dokument | Rolle |
|---|---|
| [productbrief.md](productbrief.md) | **Gjeldende produktbrief.** Samle avklarte endringer her før PRD. |
| [Forslag ved frafall – søk og resultat](docs/forslag-ved-frafall.md) | Konkretisering av SCRUM-16: nivåer, låste vakter, avgrenset søk, dekning og søkestatuser samt målemetode. |
| [Demoscenario for fravær](docs/demoscenario-fravaer.md) | Vedtatte scenarioregler, sortering, søkeomfang og tilbudssimulering med forventede svar. Eksempler og kontrollbeskrivelser; komplett datasett og kode gjenstår. |
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

Se [prosjektreglene](AGENTS.md) for språkhygiene, dokumentasjonspraksis og
[robust bruk av Jira](AGENTS.md#robust-bruk-av-jira).

## Medlemmer

- Odin A Andreassen
- Stian Lundberg

## BMAD

BMAD **6.12.0** er installert for Claude Code og Codex. Produktbriefen utarbeides
med `bmad-product-brief`. Applikasjonens teknologistakk er fortsatt åpen.

Se [BMAD – oppsett og oppstart](docs/bmad-setup.md) for å komme i gang på egen maskin.
