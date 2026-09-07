# BMAD – oppsett og oppstart

BMAD Core og BMad Method (BMM) **6.12.0** er installert for gruppen.
Metodevalget er avklart; prosjektidé, MVP og teknologistakk er fortsatt åpne.
Dette oppsettet velger ikke produktretning eller starter produktutvikling.

## Hva som deles

- `_bmad/`: felles konfigurasjon, katalog og støtteskript.
- `.claude/skills/`: ferdigheter for Claude Code.
- `.agents/skills/`: ferdigheter for Codex.
- `_bmad-output/`: dokumenter som arbeidsflytene oppretter etter hvert.
  Tomme mapper følger ikke med i Git; manglende output-mappe i en ny klone er normalt.
- `docs/`: felles prosjektkunnskap, foreløpig denne veiledningen.

Oppsettet bruker norsk dokumenttekst. Installerte BMAD-instruksjoner beholdes
slik leverandøren leverer dem. Begge verktøyene bruker samme prosjektkonfigurasjon.

## Første oppstart hos Odin eller Stian

1. Hent branchen eller versjonen som inneholder BMAD-oppsettet.
2. Kontroller `node --version` og `uv --version`. Installeren krever Node.js
   20.12 eller nyere; BMAD bruker uv til Python-skriptene sine.
3. Åpne Claude Code eller Codex i roten av dette repoet.
4. Start en ny samtale og be verktøyet kjøre `bmad-help`, for eksempel:

   > Bruk bmad-help. Vi har installert BMAD, men har ikke valgt prosjektidé.
   > Forklar hvilke muligheter vi har for å utforske ideer sammen.

I Claude Code kan ferdigheten også startes med `/bmad-help`.
Hvis ferdigheten ikke oppdages, åpne verktøyet på nytt fra repoet og kontroller
at ferdighetsmappen for verktøyet finnes. Filene er installert for begge verktøy;
oppdagelse i Stians lokale økt må kontrolleres på hans maskin.

## Personlige innstillinger

Opprett `_bmad/custom/config.user.toml` lokalt hvis du vil ha ditt eget navn
og språk i samtalen. Eksempel for Stian:

```toml
[core]
user_name = "Stian"
communication_language = "Norwegian"
```

Denne filen og `_bmad/config.user.toml` er ignorert av Git. Personlige innstillinger
skal ikke kopieres inn i de felles konfigurasjonsfilene. Felles standardnavn er G10.

## Reinstallasjon med samme versjon

De installerte filene følger repoet når oppsettet deles. Reinstallasjon er først
nødvendig hvis filer mangler eller integrasjonen må repareres. Kjør fra repoets rot:

```powershell
npx --yes bmad-method@6.12.0 install --directory . --modules bmm --tools claude-code,codex --user-name G10 --communication-language Norwegian --document-output-language Norwegian --yes
```

Versjonen er eksplisitt i kommandoen slik at en reinstallasjon ikke automatisk
velger en nyere BMAD-utgave. `_bmad/_config/manifest.yaml` viser installert versjon.
En oppgradering bør gjøres som en egen, gjennomgått endring for begge medlemmer.

## Kontroll av konfigurasjon

```powershell
uv run _bmad/scripts/resolve_config.py --project-root .
```

Kommandoen skal returnere samlet konfigurasjon som JSON. `bmad-help` bruker samme
resolver og katalogen `_bmad/_config/bmad-help.csv` for å finne arbeidsflytene.
Start gjerne en ny samtale for hver arbeidsflyt, med relevant felles grunnlag.

Oppsettet ble installert av Codex 07.09.26 etter Odins bestilling. Dette dokumentet
er en teknisk startveiledning; det er ikke en samarbeidsavtale godkjent av Stian.
