# G10 — Claude's disipler

Gruppeprosjekt i **IBE160 Programmering med KI** ved Høgskolen i Molde, høsten 2026 (15 studiepoeng).

Gruppen har valgt **VaktMatch**, en webapp for å sammenligne bemanningsalternativer
ved et udekket skift. Repoet inneholder produktgrunnlaget, BMAD-oppsettet og et
kodeskjelett for appen (se [Kom i gang](#kom-i-gang)).

## Kom i gang

Appen kjøres lokalt. Den trenger ingen konto eller KI-nøkkel.

**Forutsetninger:** Python 3.12 eller nyere, [uv](https://docs.astral.sh/uv/) 0.5
eller nyere, og Node.js 24 med npm.

Start backend i én terminal (fra repoets rot):

```powershell
cd backend
uv sync
uv run uvicorn vaktmatch.main:app --reload --port 8000
```

Start frontend i en annen terminal:

```powershell
cd frontend
npm install
npm run dev
```

Åpne <http://localhost:5173>. API-dokumentasjonen ligger på
<http://localhost:8000/docs>.

**Tester og kontroller:**

```powershell
Push-Location backend
uv run pytest
uv run ruff check .
uv run ruff format --check .
Pop-Location
Push-Location frontend
npm test
npm run lint
npm run build
Pop-Location
```

**Miljøvariabler:** se [`backend/.env.example`](backend/.env.example). Alle er
valgfrie; uten språkmodellnøkkel brukes regelbaserte forklaringer.

**Mappeoversikt:**

| Mappe | Innhold |
|---|---|
| `backend/` | FastAPI-app (`src/vaktmatch`), tester og demodatasett (`data/datasets`). |
| `frontend/` | React/TypeScript-app med Vite. |
| `docs/` | Planlegging, beslutninger og [arkitektur](docs/arkitektur.md). |
| `_bmad/`, `_bmad-output/` | BMAD-oppsett og planleggingsartefakter. |

## Produktbrief

**[productbrief.md](productbrief.md) er repoets eneste gjeldende produktbrief.**
Den er fortsatt et utkast: tekniske detaljer og implementering gjenstår.
At dokumentet er gjeldende, betyr ikke at alle forslagene
i det er endelig vedtatt.

[Teknologi og arbeidsdeling – SCRUM-13](docs/teknologivalg.md) registrerer
React og Python/FastAPI som utgangspunkt for lokal oppstart, med justerbar
hovedfordeling av arbeid. Grunnlaget er Stians forslag 24.10.26 og Odins
tilslutning 26.10.26. Modellvalg utsettes til KI-oppgavene er mer konkrete;
hosting og Supabase/RLS kan vurderes senere.

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
i økten. Odin valgte 30. oktober en komplett, avgrenset demoflyt med enkel
tilbudssimulering og begrenset datasettbytte som Må; varig logg utsettes til Bør.
Flere morgenfravær håndteres ett etter ett. [Anslått kostnad](docs/kostnadsanslag.md)
med syntetiske satser og tillegg vises separat fra P1/P2 og regelstatus.
Rask/enkel bruk, fair fordeling, tryggere beslutningsgrunnlag og økonomisk
oversikt er ønsket merverdi; effekten er ikke validert. Se endringsloggen E35.

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
| [Teknologi og arbeidsdeling](docs/teknologivalg.md) | SCRUM-13: lokal oppstart med React og Python/FastAPI, justerbar arbeidsdeling og utsatte valg. |
| [PRD](_bmad-output/planning-artifacts/prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md) | SCRUM-46: nummererte krav, Må/Bør og avvik fra briefen. Omfang og verdiambisjon oppdatert etter Odins valg 30.10.26; ikke en full godkjenning av alle krav. |
| [PRD- og Jira-avstemming – SCRUM-46](docs/scrum-46-prd-avstemming.md) | Kontroll 31.10.26 av kildegrunnlag, alle FR/NFR og eksisterende saker. PR #4 er merget med grønn main-CI; SCRUM-13/18/46 er Done. |
| [UX – visuelt](_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/DESIGN.md) og [oppførsel](_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/EXPERIENCE.md) | SCRUM-47 pågår stegvis. Kilder er bekreftet, og [første flytskisse](_bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/.working/flow-fravaer-v1.md) viser person/vakt → «Finn alternativer» → alternativer. Visuelt uttrykk og detaljert skjermoppsett er fortsatt åpne. |
| [Kostnadsanslag](docs/kostnadsanslag.md) | Syntetiske satser og tillegg, synlig beregningsgrunnlag og kontrolltilfeller for økonomisk sammenligning. |
| [Egenmelding, varsling og fraværsperiode](_bmad-output/planning-artifacts/research/domain-egenmelding-varsling-og-fravarsperiode-2026-10-31/research.md) | Avgrenset kildesjekk til SCRUM-47. Skiller offentlige veiledninger, lokale rutiner og UX-forslag; ingen ny produktregel eller automatisk fraværsperiode. |
| [PRD-forberedelser til 29. oktober](docs/prd-forberedelser.md) | Kursbeskjeden 26. oktober, eksisterende grunnlag og foreslåtte research-/brainstorming-temaer før PRD-arbeidet. |
| [Forslag ved frafall – søk og resultat](docs/forslag-ved-frafall.md) | Konkretisering av SCRUM-16: nivåer, låste vakter, avgrenset søk, dekning og søkestatuser samt målemetode. |
| [Demoscenario for fravær](docs/demoscenario-fravaer.md) | Vedtatte scenarioregler, sortering, søkeomfang og tilbudssimulering med forventede svar. Eksempler og kontrollbeskrivelser; komplett datasett og kode gjenstår. |
| [Arkitektur](docs/arkitektur.md) | SCRUM-18: moduler, ansvarsgrenser, konfigurasjon og kvalitetssikring for kodeskjelettet. |
| [Leverings- og dokumentasjonskrav for IBE160](docs/ibe160-leveringskrav.md) | Kildekontrollert oversikt over arbeidskrav, vurdering, KI-dokumentasjon, individuelle bidrag og design/UX. Sluttfrist og «delvurdering 3» er fortsatt uavklart. |
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
med `bmad-product-brief`. React og Python/FastAPI er utgangspunktet for oppstart;
tekniske detaljer behandles videre i SCRUM-18.

Se [BMAD – oppsett og oppstart](docs/bmad-setup.md) for å komme i gang på egen maskin.
