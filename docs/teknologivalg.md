# Teknologi og arbeidsdeling – SCRUM-13

Registrert av Codex 26.10.2026 etter Odins uttrykkelige beskjed om å dokumentere
avklaringen i repo og Jira. Dette dokumentet viser utgangspunktet for oppstarten.

## Avklart utgangspunkt

| Tema | Avklaring | Opphav og status |
|---|---|---|
| Frontend | React. | Valgt av Stian i SCRUM-13, 24.10.26; Odin sluttet seg til utgangspunktet 26.10.26. |
| Backend og regelmotor | Python med FastAPI. | Samme grunnlag som frontendvalget. FastAPI er API-laget; scenarioreglene beregnes i egen kode. |
| Kjøring | Lokal kjøring i oppstartsfasen. | Foreslått av Stian 24.10.26 og bekreftet av Odin 26.10.26. Formålet er å få kjerneflyten til å fungere før hosting settes opp. |
| KI-modell | Modell og leverandør velges når KI-oppgavene, input og svarformat er mer konkrete. | Utsettelsen er registrert av Stian i SCRUM-59 og støttet av Odin 26.10.26 med denne begrunnelsen. Regelbaserte standardforklaringer lages først, jf. SCRUM-40. |
| Hosting og Supabase | Nett-demo, Supabase og RLS kan vurderes senere. | Ingen leverandør, skylagring, innlogging eller RLS-løsning er valgt nå. Lokal oppstart utelukker ikke en senere nett-demo. |

Kjerneflyten skal fortsatt fungere uten KI-nøkkel. Krav om miljøvariabler og
hemmeligheter utenfor repoet videreføres. Modellkostnader, kostnadsgrense og
test-/mockmodus avklares i [SCRUM-59](https://stiodi.atlassian.net/browse/SCRUM-59)
før en modellintegrasjon tas i bruk.

## Arbeidsdeling som kan justeres

| Hovedansvar for oppfølging | Område |
|---|---|
| Odin | UX, grensesnitt, sammenligning av alternativer, prioritering og KI-/standardforklaringer. |
| Stian | Datagrunnlag, regelmotor, søk og teknisk oppsett. |

Fordelingen bygger på Stians forslag i SCRUM-13 og Jira-tildelingene, med Odins
tilslutning 26.10.26 som et utgangspunkt. Den er ikke en låst detaljfordeling.
Ansvar betyr oppfølging; beslutningsmyndigheten følger prosjektreglene. Det er
ikke gjort nye tildelinger eller endringer i pågående arbeid gjennom denne føringen.

## Detaljer og verifikasjon

Vite/TypeScript, JSON-demodata, SQLite og CI er omtalt som forslag i Stians
kommentar 24.10.26 og behandles i SCRUM-18. Denne avklaringen godkjenner ikke
disse detaljene eller det lokale kodeskjelettet. Kjørbarhet, nøkkelhåndtering og
tester må kontrolleres mot tilgjengelig kode før sakene ferdigstilles.

## Kilder og samordning

- [SCRUM-13](https://stiodi.atlassian.net/browse/SCRUM-13), Stians kommentar 24.10.2026, kommentar-ID `10019`.
- Odins tilslutning og beskjed om lokal oppstart i samtalen 26.10.2026, med uttrykkelig tillatelse til dokumentasjon. Bare den avklarte konklusjonen er oppsummert her.
- [Gjeldende produktbrief](../productbrief.md), [E34 i endringsloggen](productbrief-endringslogg.md#261026--teknologi-lokal-oppstart-og-arbeidsdeling) og [prosjektreglene](../AGENTS.md).

Stians kommentar viser til en tidligere versjon av `docs/teknologivalg.md` og
E33. Disse var ikke tilgjengelige på de eksterne grenene ved kontroll 26.10.26.
Denne filen dokumenterer avklaringen nå og må samordnes med den versjonen når
den blir tilgjengelig. E34 brukes for å unngå kollisjon med det omtalte E33.
