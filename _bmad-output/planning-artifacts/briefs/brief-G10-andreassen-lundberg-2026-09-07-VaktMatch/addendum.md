# Addendum: VaktMatch

Utdypende materiale som ikke fikk plass i selve brief'en, men som er relevant for PRD, arkitektur eller senere diskusjon.

## Opprinnelig turnusgenerator-idé (Stian) — "Minimum"-nivå nå i MVP, resten fortsatt parkert

**Oppdatert 2026-09-07:** Stians "Minimum"-nivå (under) er tatt inn i MVP som ukesgrunnlag-generator, se brief'ens Scope-seksjon. "Middels" og "Avansert" er fortsatt visjon, ikke MVP.

Stians opprinnelige forslag var en full periode-turnusgenerator (f.eks. 4 uker), skissert i tre nivåer:

1. **Minimum:** Registrere ansatte og bemanningsbehov, generere en turnus som ikke bryter harde regler, vise den som kalender/tabell.
2. **Middels:** Fordele helg/natt/uønskede vakter, behandle ønsker som myke preferanser, forklare manglende dekning, eksportere planen.
3. **Avansert:** Håndtere sykefravær, gi naturlig-språk-forklaringer, kjøre "hva om"-scenarioer, skille leder-/ansattilgang.

Anbefalt datamodell: `Ansatt`, `Skift`, `Regelsett`, `Turnusplan` (med planstatus og avvikslogg). Anbefalt teknisk retning: regel-/optimaliseringsbasert kjerne (constraint solver) for selve turnusoppgaven, språkmodell kun for tolkning/forklaring/justeringsforslag — ren LLM-generering ble vurdert som for risikabelt siden en språkmodell ikke pålitelig garanterer at harde regler følges.

VaktMatch (akutt matching, ett skift om gangen) og full turnusgenerering løser ulike kjerneoppgaver og bør ikke begge inngå i samme MVP. Langsiktig visjon kan koble dem: udekkede skift fra en turnusgenerator kan mate VaktMatchs matchingsflow.

## "Uber for jobb"-metaforen — droppet 2026-09-07

Opprinnelig brukt uformelt om vikarsiden av ideen: arbeidstakere melder seg tilgjengelige og blir del av et nettverk; virksomheter sender inn akutte behov. Denne framingen er nå droppet av Odin: en åpen markedsplass der folk blir "tilgjengelige" uten formell ansettelse ligner på spøkelseskontrakter, som ikke er lovlig i Norge slik Odin forstår det. Et bemanningsforetak (jf. Arbeidstilsynets regler om innleie) må gi ansatte en reell kontrakt med stillingsprosent.

**Ny modell:** eksterne vikarer er allerede ansatt hos et bemanningsforetak med kontrakt og stillingsprosent. VaktMatch matcher mot denne allerede formaliserte poolen — det er ikke systemet som oppretter ansettelsesforholdet eller lar folk melde seg inn løst. Dette bør inn i datamodellen (Ansatt/Vikar bør ha felt for arbeidsgiver, stillingsprosent, kontraktstype) når PRD/arkitektur lages.

## Kursets forventede AI-utviklingsverktøystakk (fra pensum, ikke produktarkitektur)

Oppgitt av Odin 2026-09-07, sannsynlig kilde: "IBE160 – Verktøystakk fra pensum" (Ressurser fra Canvas). Dette er verktøyene kurset forventer brukt i *utviklingsprosessen*, ikke nødvendigvis appens endelige kjøretidsarkitektur — de to bør ikke forveksles når arkitektur besluttes senere (`bmad-architecture`):

1. Claude Code — primær agent på alle flater.
2. Alternative agenter — Gemini CLI, Codex CLI, Cursor.
3. VS Code med utvidelser (Python, Markdown).
4. Git og GitHub — lokal versjonskontroll og eksternt samarbeid.
5. Node.js og NPM — JavaScript-kjøremiljø, driver også agentøkosystemet.
6. Python og uv — backend-språk og pakkehåndtering.
7. Docker — containere for reproduserbare bygg/kjøringer.
8. MCP-servere — kobler agent til databaser, filer, API-er.
9. Tjenestekontoer — GitHub Actions, Supabase, hosting.

Merk: Supabase nevnes som tjenestekonto her, og AquaTools (Odins private prosjekt) bruker allerede Supabase-autentisering — mulig, men ikke bekreftet, retning for VaktMatchs egen backend.

## Skalering utover MVP — hva som bevisst ikke er løst

Odin ønsker at brief/PRD dokumenterer, ikke bare utelater, hva som kreves for å håndtere:
- større datamengder
- sikkerhet
- infrastruktur/drift

Dette skal ikke faktisk bygges i MVP-en, siden det normalt krever penger (betalte tjenester/skalert infrastruktur) som et studieprosjekt ikke har. Det bør bli en egen seksjon i PRD eller arkitekturdokumentet ("hva ville vi gjort med budsjett"), ikke noe som forsvinner stille fra scope.

## Konkurrentsjekk 2026-09-07 (Simployer, Quinyx, 4Human)

Full rapport: [`research.md`](../../research/competitive-simployer-quinyx-4human-akutt-bemannings-2026-09-07/research.md). Kort versjon: alle tre dekker fraværsregistrering, varsling og manuell erstatningssøk godt, men ingen dokumenterer i dag en rangert/forklart, regelsjekket sammenligning av alternativer ved et akutt dekningsgap — det VaktMatch bygger differensieringen på. Confidence medium, ikke høy (quick-preset, offentlige kilder, én runde). To ting bør sjekkes videre hvis dette skal inn i PRD/refleksjonsrapport med høyere sikkerhet:

- Simployers «Finn vikar»-funksjon kunne ikke inspiseres i detalj (dokumentasjon utilgjengelig ved henting).
- En Quinyx-påstand om "intelligent logikk" for omfordeling er uverifisert — ikke bekreftet ved direkte gjenhenting av kildesiden.

## Leverandøragnostisk lag — vurdert og bevisst holdt utenfor MVP (2026-09-07)

Odin kjenner igjen mønsteret fra oppdrettsnæringen: flere ulike systemer (der Odin kommer fra, mange leverandører styrer forflåter/fortøyning) gjør stort sett det samme med ulikt grensesnitt. Aktører som Akva og Pisada jobber aktivt med å selge inn egne systemer som kobler seg over/styrer andre leverandørers programvare, inkludert konkurrenters og egne eldre løsninger. Samme mønster gjelder trolig WFM-markedet (Simployer, Quinyx, 4Human m.fl.), og konkurrentsjekken over støtter at et forklaringshull faktisk finnes.

**Hvorfor ikke i MVP:** (1) Reell integrasjon krever partner-API-tilgang og forretningsavtaler — ikke noe et studentprosjekt kan skaffe på dager. (2) Gruppen har ikke førstehåndskunnskap om hvordan disse systemene faktisk brukes/oppleves av en mellomleder — å bygge integrasjoner mot noe man ikke forstår innenfra er høy risiko. MVP-ens syntetiske, fiktive arbeidsplass omgår dette problemet helt, siden den ikke etterligner noe reelt systemgrensesnitt — dette kunnskapshullet blokkerer derfor ikke MVP, kun en eventuell fremtidig integrasjonsfase.

**Hvis dette skal forfølges senere:** Det ville krevd enten (a) tilgang til noen som faktisk bruker et av systemene som mellomleder (intervju/observasjon), eller (b) en bmad-deep-recon user-voice-runde mot brukeranmeldelser/forum for å hente reelle frustrasjoner uten direkte tilgang.

## Juridiske/etiske kontrollpunkter (grunnlag for "aldri påstå lovlig")

- [Arbeidstilsynet – innleie fra bemanningsforetak](https://www.arbeidstilsynet.no/lonn-og-ansettelse/innleie-av-arbeidskraft/innleie-fra-bemanningsforetak/) — bemanningsforetak har arbeidsgiveransvar, innleie er regulert. Ikke en funksjonsspesifikasjon for studieprototypen, men relevant bakgrunn.
- [Datatilsynet – rettigheter ved automatiserte avgjørelser](https://www.datatilsynet.no/rettigheter-og-plikter/den-registrertes-rettigheter/rettar-ved-automatiserte-avgjerder/) — grunnlag for at mennesket alltid må ta den endelige beslutningen, og at forklaring/kontroll er reelle krav, ikke bare god UX.

## Åpne valg gruppen ikke har tatt ennå (fra vaultnotatene, fortsatt åpne per 2026-09-07)

- ~~Om MVP-en primært skal matche ett akutt behov eller også generere deler av grunnturnusen~~ — avklart 2026-09-07: begge deler. Grunnlaget genereres (Minimum-nivå); akutt-matching er hovedflyten som demonstreres mest.
- Endelig demonstrasjonsdomene (lager/logistikk foreslått, ikke formelt låst).
- ~~Åpent vs. lukket vikarnettverk~~ — avklart 2026-09-07: lukket, vikarer er ansatt hos bemanningsforetak med kontrakt/stillingsprosent, se over.
- Hva som er absolutte krav vs. ønskede krav vs. valgfrie fordeler i matchingen.
- Om førsteversjonen stopper ved en anbefalt kandidatliste, eller også simulerer tilbud/aksept.
- Hvordan rangering, rettferdighet, personvern og menneskelig overstyring skal testes og dokumenteres.

## Hvorfor VaktMatch, ikke Stingray-sporet

Et tidligere Stingray/AquaTools-spor ble lagt bort 2026-09-04. VaktMatch ble deretter utforsket som et alternativ med et annet domene og en avgrenset bemanningsoppgave. Per 2026-09-07 vurderes VaktMatch, Forplanner og PantBuddy som tre kandidater; endelig prosjektvalg og arbeidsdeling er ikke avklart i gruppen.

## Akademisk ramme (relevant for proposal, ikke for produktets brukere)

- IBE160, Høgskolen i Molde, høst 2026. Faglærer: Bård Inge Austigard Pettersen.
- Karaktervekting: 70 % prosjektkode/funksjonalitet, 30 % refleksjonsrapport, ingen muntlig eksamen (bekreftet av faglærer i Teams 2026-08-20; Canvas oppdatert, HiMoldes offisielle emneside henger etter og skal ikke stoles på).
- BMAD er bekreftet påkrevd metode.
- Proposal må være godkjent innen søndag 2026-09-13 (ekstern frist); internt gruppemål 2026-09-10.
- Uavklart: eksakt krav til KI-dokumentasjon, hvilke samtalelogger som må leveres, hvordan individuelle bidrag dokumenteres i gruppearbeidet, og hva "delvurdering 3" faktisk er.
