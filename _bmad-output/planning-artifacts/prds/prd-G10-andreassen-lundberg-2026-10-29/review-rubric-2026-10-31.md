# PRD-gjennomgang – VaktMatch, 31.10.2026

Skrevet av Codex med en egen underagent i SCRUM-46. Hele [PRD-en](prd.md)
og BMAD-rubrikken `prd-validation-checklist.md` er lest, sammen med
[forrige gjennomgang](review-rubric-2026-10-30.md),
[leveringskravene](../../../../docs/ibe160-leveringskrav.md) og relevante
[prosjektregler](../../../../AGENTS.md#sesjonslogg). Gjennomgangen gjelder
planleggingsgrunnlaget for en studieprototype; den verifiserer ingen appkode,
brukereffekt eller gjennomføring av Jira-saker. Første lesing gjaldt
PRD-versjonen med `updated: 2026-10-30`. Identifiserte kilde- og prosessmangler
er kontrollert etter retting i versjonen med `updated: 2026-10-31`.

## Samlet vurdering

PRD-en gir et brukbart og avgrenset grunnlag for UX, datamodell og stories.
Den skiller beregningsgrunnlag, regelkontroll, sortering, forklaring og simulert
aksept, og viser både prioritering og opphav. Ingen kritiske eller høye funn
er avdekket. NFR-8s manglende henvisning til sesjonslogg og fristspørsmålets
manglende muntlige status er rettet og kontrollert i denne økten.

## Beslutningsgrunnlag – adequate

§7.2 viser endret prioritering og hvem som tok valgene. §9 skiller åpne valg
om modell, målgruppe og eksterne vikarers arbeid fra fastsatt omfang. Åpent
spørsmål 2 er en reell samordningsoppgave i SCRUM-46, ikke et ubesvart
prioriteringsvalg fra 30. oktober.

### Funn

- **low, rettet – Fristspørsmålet utelot eksisterende muntlig grunnlag** (§9, nr. 1).
  Den eldre PRD-en spurte bare «Hva er sluttfristen», mens leveringskravenes tabell og
  «BMAD og arbeidslogg» registrerer omtrent 15. desember som muntlig utgangspunkt
  og samtidig levering av app og rapport. *Kontrollert rettelse:* §9 nr. 1 viser
  nå denne statusen, med forbehold om at eksakt frist og leveringskanal ikke er
  skriftlig bekreftet. SCRUM-49 og oppfølgingseieren er beholdt; anslaget er
  ikke gjort til en bindende dato.

## Innhold fremfor pynt – strong

Eksempelpersonen Kari er uttrykkelig konstruert. Visjonen kaller tid, fordeling,
trygghet og økonomi ønsket merverdi uten dokumentert effekt; ingen markedsmessig
unikhet eller generell lovlighetsgaranti hevdes. NFR-2 og NFR-1 har målbare
grenser fremfor generiske kvalitetsord.

## Strategisk sammenheng – adequate

Den komplette demoflyten forklarer hvorfor tilbudssimulering og datasettbytte
er Må, mens varig logg og låsing i grensesnittet er Bør. Kostnadsanslaget er
et synlig sammenligningsgrunnlag, og overtar ikke P1/P2 eller R1–R5. SM-1,
SM-2, SM-4 og SM-6 kontrollerer det som produktet lover; motmålene motvirker
funksjonsmengde, overbevisende KI-tekst og flest mulig alternativer.

Femminuttersmålet i visjonen er fortsatt knyttet til en valgfri brukertest.
Dette ble vurdert 30. oktober og gjenåpnes ikke som et nytt krav.

## Tydelig «ferdig» – adequate

FR-1–24 har etterprøvbare konsekvenser eller henvisninger til konkrete
kontrolltilfeller. FR-15/20/21 og M1–M2 skiller øktvalg, simulert svar og nytt
datagrunnlag. O1–O5 gjør kostnad kontrollerbar uten å utvide modellen til reell
lønn eller tariff. NFR-4s tidligere feil om obligatorisk testing av Bør-funksjoner
er rettet; den gjentas ikke som et åpent funn.

### Funn

- **medium, rettet – Arbeidslogg per økt manglet i sporbarhetskravet** (§5, NFR-8).
  Den eldre NFR-8 omfattet Jira, commits, memlog og KI-/gjennomgangsspor, men
  ikke den gjeldende sesjonsloggen. AGENTS.md krever automatisk logg ved avsluttet økt
  som endret tilstand, med Oppgave, Plan, Resultat og åpne punkter i
  `.logs/<bruker>/`, lokal commit av bare loggfilene og ingen automatisk push.
  *Kontrollert rettelse:* NFR-8 viser nå til regelen, de fire loggdelene,
  separat lokal commit og uttrykkelig godkjenning før push. Dette tar inn et
  eksisterende dokumentasjonskrav og vedtar ingen ny loggpraksis. Faglærers
  eksempel og Odins prosessvalg holdes atskilt. Jira-samordning av SCRUM-44
  håndteres av hovedagenten og er ikke verifisert av denne dokumentkontrollen.

## Ærlig avgrensning – strong

§6 og §7 er tydelige om syntetiske data, ett fravær om gangen, avgrenset søk,
ingen gjennomføring av vaktendringer og ingen leverandørintegrasjon. FR-24
merker beregningsmodellen som Codex sin konkretisering. Manglende full
godkjenning av alle detaljkrav skjules ikke av dokumentets `final`-status.
Den reviderte §10 skiller dessuten vedtatte omfangsvalg fra Codex sin
konkretisering av kostnadsmodell og sekvensielle kontrolltilfeller.

## Bruk videre i UX, arkitektur og stories – adequate

Begrepslisten og stabile krav-ID-er gir et godt uttrekksgrunnlag. Kontrollstatus,
dekning og søkestatus er atskilt, og gammelt valg eller aksept er knyttet til
dataversjonen. Jira-dekning og konkrete avhengigheter må fortsatt samordnes
som oppgaven i §9 nr. 2 angir; denne rubrikkgjennomgangen påstår ikke at det
arbeidet er fullført. FR-16s presisering skiller historisk visningskontekst
fra korrigert historikk i kontrollgrunnlaget; ny kontroll kan endre status
uten å innføre en skjult historisk poengsum.

## Form – strong

Dokumentet passer en studieprototype med en meningsfull brukerflyt og separat
lokal oppstart for sensor. Den funksjonsdelte kravlisten og fire korte
brukerreiser er tilstrekkelige. Ingen større omstrukturering er nødvendig.

## Mekaniske merknader

- FR-1–24, NFR-1–9, UJ-1–4 og SM-1–6 er entydige. FR-24 står før Bør-kravene
  FR-22/23 for å samle Må-omfanget; stabile ID-er bør beholdes.
- UJ-2 går fra valgt søkegrense 0 til formuleringen «beholder standardgrensen 1».
  Bytt til «setter søkegrensen tilbake til 1» for å gjøre handlingen entydig.
- NFR-4 innledes med «Regelmotoren» selv om kildetilfellene også omfatter
  grensesnitt, økt og oppdatering. Presiser passende testnivå uten å endre
  Må/Bør-grensen. Den tidligere gjennomgangen registrerte samme presiseringsbehov.
- NFR-5s «samme resultat» kan presiseres til beregnede alternativer, statuser,
  rangering og kostnad. FR-18/19 krever samsvar i fakta, ikke identisk ordlyd
  fra en språkmodell.
- Leveringskravenes avsnitt om arbeidslogg omtalte både en eldre regel som
  «i dag» og den nyere regelen av 29. oktober. Den foreldede
  nåtidsbeskrivelsen er rettet til historisk omtale, med bevart historikk.
- Ingen `addendum.md` finnes i PRD-mappen. Støttedokumentene er allerede
  lenket, og ingen ny inline-antakelse er nødvendig for rettelsene ovenfor.

## Funnstatus og avgrensning

Ved første kontroll: 0 kritiske, 0 høye, 1 middels og 1 lavt funn.
Begge funn er rettet og kontrollert; ingen av disse står åpne.
De redaksjonelle presiseringene står i [språkrapporten](review-editorial-2026-10-31.md)
som forslag til hovedagentens triage. Gjennomgangen beslutter
verken produktendringer, godkjenning fra begge deltakere eller Done i Jira.

## Hovedagentens oppfølging etter gjennomgangen

De tre redaksjonelle presiseringene er anvendt. Jira-samordningen og
NFR-referansene er fullført og kontrollert, og det tidligere spørsmål 2
er lukket i PRD-en. Se [kontrollgrunnlaget](../../../../docs/scrum-46-prd-avstemming.md).
SCRUM-46s avhengighet til SCRUM-13 består; ingen appverifikasjon er gjort.
