# Lokal klargjøring av SCRUM-18 – 31.10.2026

Utført av Codex etter Odins oppdrag om neste steg for SCRUM-46/13/18.
Arbeidet er en lokal klargjøring på `scrum-18-klargjoring`, med main
`2900ac9f262231a3a568907ec548b43734855e78` og PR #3
`1958161427311a3b9da314c78f10a1e3744857c9` som foreldregrunnlag.
Ingen delt gren er omskrevet, og ingen push eller ekstern merge er utført.

## Samordning

Lokal merge hadde konflikter i `.memlog.md` og `docs/teknologivalg.md`.
Main-versjonens produktgrunnlag, PRD-arbeid og E33/E34-kilder er beholdt.
PR-grenens historiske logginnslag er bevart med `memlog.py`, med et nytt W4-
override som skiller hendelsesdatoer fra oppgitt registreringstidspunkt.
README inneholder både oppstart og oppdatert planlegging.

## Oppfølging av gjennomgangen 29.10

| Funn | Lokal rettelse og kontroll |
|---|---|
| P1 | `DatasetLoadError` gir fil-/mappekontekst og bevarer årsak. Ugyldig JSON, metadata/rot, tegnkoding, duplikat-ID og manglende mappe avvises i tester. Katalogen avvises samlet; ugyldige filer ignoreres ikke stille. Felles HTTP-oversettelse gjenstår i SCRUM-22 etter D2; det påstås ikke at API-500 ved slike data er ferdig håndtert. |
| P2 | Isolerte tester av `VAKTMATCH_`, midlertidig `.env`, miljøforrang og tomme eksempelverdier. Ingen reelle nøkler inngår. |
| P3 | README-testkommandoer går tilbake til rot mellom backend og frontend og inkluderer `ruff format --check`. |
| P4 | Relative datastier forankres i backendroten og testes etter arbeidsmappeskifte. JSON-liste for CORS er dokumentert og testet. |
| P5 | CI har `contents: read` og ti minutters tidsavbrudd per jobb. Ny GitHub-kjøring krever publisering. |
| P6 | Frontend-testene rydder DOM eksplisitt mellom testene. |
| P7 | Avvist nettverkskall gir norsk melding; eksisterende HTTP-statusfeil er beholdt. Avvist fetch testes separat. |
| D1/W4 | Arkitekturen viser Odins eksisterende godkjenning 29.10 med kilde; loggpresisering er append-only. Ingen ny arkitekturavgjørelse. |

## Verifikasjon

- `uv sync --locked`: bestod med Python 3.12.14 og uv 0.12.6.
- `uv run pytest`: **22 bestått**.
- `uv run ruff check .` og `uv run ruff format --check .`: bestod.
- Frontend med Node 24: Vitest **tre bestått**, oxlint og TypeScript/Vite-bygg bestod.
- Direkte `GET /api/health` og samme rute gjennom Vite-proxyen svarte
  `status: ok`, versjon `0.1.0`, forklaring `regelbasert`.
- Metadataendepunktet svarte med det medfølgende skjelettdatasettet.
- Testserverne ble stoppet etter kontrollen. Ingen appkonto eller KI-kall
  var nødvendig for denne kjøringen.

En kontekstfri KI-underagent gjennomgikk endringene og fant ett
reproduserbart problem: tomme ID-er og ID-er med skråstrek kunne annonseres
uten å kunne hentes fra item-ruten. Ikke-tomme ASCII-slugger valideres nå;
to negative tester dekker avviket. Resten av de vurderte kandidatene
gjentok tidligere avviste/utsatte funn. Dette er KI-kontroll, ikke en
uavhengig menneskelig godkjenning. Se [spesifikasjonen](spec-scrum-18-klargjoring.md).

## Gjenværende kontrollpunkt

PR #3s tidligere grønne CI gjelder gammel kode. Nye lokale rettelser har
ennå ingen GitHub-CI. Publisering krever gjennomgang og uttrykkelig
godkjenning etter [AGENTS.md](../../AGENTS.md#sesjonslogg).

SCRUM-13, SCRUM-18 og SCRUM-46 settes ikke Done gjennom denne lokale
klargjøringen. Verifikasjon/merge og håndtering av den dokumenterte
saksavhengigheten må følges opp med korrekt commitgrunnlag. Eksisterende
arbeidsdeling er beholdt; ny gjennomgangsgren endrer ikke den delte PR-grenen.
W1–W3 og felles HTTP-feilhåndtering følger fortsatt de tidligere angitte
implementeringssakene.
