---
title: 'SCRUM-18: klargjør kodeskjelett for ny gjennomgang'
type: 'bugfix'
created: '2026-10-31'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Neste steg for SCRUM-46 er håndtering av SCRUM-13/18. PR #3
har konflikt med main, og P1–P7 fra gjennomgangen 29.10 er fortsatt åpne.
Odin ba 31.10 om å ta neste steg; dette gir grunnlag for lokal klargjøring,
ikke godkjenning av publisering eller omskriving av en delt gren.

**Tilnærming:** Samordne eksisterende kodeskjelett med lokal main på en egen
gren, rett P1–P7 og kontroller bygg, tester og lokal kjøring uten KI-nøkkel.
Bevar produktgrunnlag, opphav og logghistorikk. Datalaget får forståelig
feilkontekst og validering; felles HTTP-feilhåndtering forblir SCRUM-22 etter
Odins tidligere avklaring. Arkitekturstatus og W4 presiseres med eksisterende
kilder og append-only override. Ingen nye appfunksjoner, push, ekstern merge,
endret tildeling eller Done før nødvendig kontrollgrunnlag foreligger.

</frozen-after-approval>

## Implementation Notes

- Rutevalg: ingen åpne produktvalg eller irreversible operasjoner i lokal
  klargjøring. Fotavtrykket er avgrensede rettelser i det allerede skrevne
  skjelettet; oneshot brukes. Publisering/merge er et senere kontrollpunkt.
- Code Map: `backend/src/vaktmatch/data/repository.py` avviser ugyldig JSON,
  metadata, duplikat-ID og manglende mappe med datalagsfeil med kontekst;
  `config.py` forankrer relativ datasti i backendroten. Tester under
  `backend/tests/` dekker disse feilene og miljøkontrakten isolert.
- `backend/.env.example` dokumenterer CORS-liste og datasti. README får
  kopierbare kontroller med tilbakevending til rot og formatkontroll.
  `.github/workflows/ci.yml` får lesetillatelse og jobbtidsavbrudd.
- Frontend: eksplisitt cleanup i `src/App.test.tsx`; `src/api.ts` oversetter
  nettverksfeil uten å skjule HTTP-status. En avvist fetch testes.
- Merge bevarer main-versjonen av produktdokumenter og teknologikilder,
  henter oppstartsseksjon/arkitekturlenke fra PR-en og bevarer begge loggers
  innslag med `memlog.py`. D1/W4 får presis status uten nye beslutninger.
- Kontroll: backend pytest/ruff, frontend Vitest/oxlint/bygg, direkte health
  og health via Vite-proxy, metadataendepunkter, miljøeksempel uten nøkkel,
  dokumentlenker og konfliktmarkører. Ny GitHub-CI kan først kjøres etter
  godkjent push; tidligere grønn CI er ikke bevis for nye endringer.
- Startgrunnlag: lokal main `2900ac9f262231a3a568907ec548b43734855e78`
  og PR #3 `1958161427311a3b9da314c78f10a1e3744857c9`. Lokal merge
  på `scrum-18-klargjoring` hadde to konflikter, i memlog og teknologidokumentet.
  Main-innholdet er beholdt; PR-innslagene er bevart med skript og W4-override.
- Datavalidering avviser hele katalogen ved ugyldige metadata fremfor å
  skjule en ødelagt fil. Datalagsfeilen har fil-/mappekontekst og årsakskjede;
  HTTP-oversettelsen gjenstår i SCRUM-22. P1s HTTP-del er derfor ikke ferdig.
- En egen KI-reviewer fant ett reproduserbart avvik: metadata kunne ha ID-er
  som ikke kunne hentes fra item-ruten. ID-er er nå ikke-tomme ASCII-slugger
  (bokstaver, tall, understrek og bindestrek); tom ID og skråstrek avvises i tester.
- Lokal verifikasjon: 22 backendtester, tre frontendtester, ruff check/format,
  oxlint, TypeScript/Vite-bygg og health direkte/gjennom Vite bestod.
  [Kontrollrapporten](verification-scrum-18-2026-10-31.md) beskriver avgrensningene.
  Done her betyr ferdig lokal klargjøring; Jira-sakene er ikke lukket.

## Review Triage Log

- **medium → patch:** `DatasetInfo.id` godtok tom streng og skråstrek.
  Katalogen kunne annonsere en ID som item-ruten ikke kunne hente. Bevis:
  reviewerens TestClient-reproduksjon og to nye regresjonstester. Rettet
  med validering i eksisterende felt; ingen ny rute eller responsstruktur.
- Revieweren beregnet et funngulv på ti ut fra hele mergediffens størrelse,
  men fant bare ett selvstendig reproduserbart problem. Ingen ekstra funn
  er konstruert for å nå gulvet; tidligere avviste/utsatte forhold beholdes
  i deres dokumenterte oppfølging.
