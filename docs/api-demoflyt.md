# Delt data- og HTTP-kontrakt for demoflyten

Codex · 08.11.2026 · implementeringsvalg på Odins gjennomføringsmandat.
Kontrakten konkretiserer eksisterende krav uten ny produktprioritering.
Endepunktene er lokale og endrer aldri datasettfilene. Frontend har ingen
egen regelmotor. FastAPI/OpenAPI viser de eksakte implementerte felttypene.

## Datagrunnlag

Behold `DatasetInfo` og eksisterende metadatakatalog. Full `Dataset` har
`dataset`, `assessment_time`, `week_start`, `week_end`, `coverage_start`,
`coverage_end`, `employees`, `shifts`, `assignments`, `supplements`.
Metadata har `id`, `version`, `title`, `description`, `family_id`.

| Objekt | Felter og betydning |
|---|---|
| Interval | `start`, `end`: tidssonebevisste dato/tider; start < slutt. |
| Employee | `id`, `name`, `kind` (internal/external), `skills` (liste eller null), `availability` (liste intervaller eller null), `contract_hours` og `hourly_rate` (desimal eller null), `work_context_complete`, `history_complete`, `history_source`. |
| Shift | `id`, `start`, `end`, `required_skill`, `required_count` (positivt heltall). Én kompetansekategori per vakt i dette datasettet. |
| Assignment | `id`, `employee_id`, `shift_id`, `locked`, `absent`. Fraværende tildeling er kildehistorikk, ikke aktiv dekning/arbeid. |
| Supplement | `start`, `end`, `rate`; valgfri `employee_id` og `shift_id` avgrenser tillegget. Uten avgrensning gjelder intervallet alle. |
| Absence | `employee_id`, `shift_id`. Aktive simulerte fravær sendes i hver forespørsel og lagres i fanens minne. |

Alle ID-referanser og unike ID-er valideres. Manglende nødvendig informasjon
skal være uttrykkelig representerbar, men feil struktur eller referanse avvises.
`availability=null` er ukjent; `[]` er kjent utilgjengelighet. Listen er komplett
innen kontrollperioden; tilstøtende intervaller kan sammen dekke en hel vakt.
`supplements=null` er ukjent tilleggsgrunnlag; `[]` er kjent uten tillegg.
`work_context_complete=false` betyr at nødvendig øvrig arbeid kan mangle,
også for eksterne. Historikkens fullstendighet er en separat opplysning.

Regn intervalloverlapp og forløpt tid i UTC; vis kalender/tider i Europe/Oslo.
P1/P2/R5 bruker faktisk del av vaktene innen den faste arbeidsuken. R4 bruker
nødvendige nabovakter og tilstrekkelig bekreftet kontrollperiode. Ingen
lagrede ukesummer erstatter beregning fra vaktene. Kostnad bruker `Decimal`,
intervallsplitting og halv-opp-avrunding per tildeling til øre før summering.

## Endepunkter

| Metode og sti | Inndata / resultat |
|---|---|
| GET `/api/health` | Behold eksisterende helse-/forklaringsstatus. |
| GET `/api/datasets` | Metadata for de tilgjengelige forhåndslagde datasettene. |
| GET `/api/datasets/{id}` | Behold eksisterende metadatarespons. |
| GET `/api/datasets/{id}/state` | Fullt validert datasett. |
| POST `/api/state` | `{dataset_id, version, absences}`. Fullt datasett med aktiv dekning og kontroll av gjeldende bemanning. |
| POST `/api/absences/preview` | Samme grunnlag pluss `employee_id`, `start_shift_id`, `calendar_days` (heltall ≥1). Returner lokal kalenderperiode og berørte hele vakter med valgbart målskift/begrensning. |
| POST `/api/absences/simulate` | `{dataset_id, version, absences, absence}`. Valider ny hendelse, behold gyldige tidligere hendelser og returner `{dataset_id, version, absences, coverage}`. Gjentatt identisk hendelse er idempotent. |
| POST `/api/evaluate` | `{dataset_id, version, absences, target_shift_id, search_limit: 0|1, criteria: ['P1']}`. Returner kontrollert vurdering nedenfor. Kriterier er en ikke-tom, unik ordnet delmengde av P1/P2. |
| POST `/api/datasets/compare` | `{previous_id, next_id}`. Returner ID/versjon for begge og navngitte, konkrete endringer i ansatte, tilgjengelighet, vakter, tildelinger/låser, historikk og kostnadsgrunnlag. |
| POST `/api/explain` | Samme gyldige vurderingsgrunnlag pluss `alternative_id`. Kontroller resultatet på nytt og returner standardforklaring/reservemelding. Ingen modell/leverandør velges i denne runden. |

`version` kontrolleres mot serverens fil; gammel versjon gir 409. Ukjent
datasett gir 404, ugyldig input/referanse 422 og uleselig datasett 503.
Bruk en felles norsk feilrespons med `message` og eventuelle feltfeil.
Interne filstier eller stacktraces skal ikke vises i grensesnittet.

Uke/historikk/påbegynt målskift er ikke gyldig som nytt fravær i denne flyten.
Evaluering av et påbegynt, allerede dekket eller på annen måte utenfor
omfang målskift returnerer forståelig `utenfor_omfang` med bemanningsbehovet
synlig, ikke en påstand om at søket fant null løsninger.

## Vurderingsrespons

Eksakte hjelpeklasser kan tilpasses i implementeringen, men feltene som
frontend bruker dokumenteres i `api.ts` og skal samsvare med OpenAPI.

| Innhold | Påkrevd informasjon |
|---|---|
| Vurdering | `dataset_id`, `version`, `assessment_time`, `target_shift_id`, `search_limit`, `criteria`, `search_status` (fullfort/avbrutt/utenfor_omfang), `message`, `alternatives`, `coverage`, antall undersøkte kombinasjoner og målt beregningstid. |
| Alternativ | Stabil `id`, hovedkandidat, direkte/flytting/delvis, samlet kontrollstatus, separat dekning, før/etter for berørte vakter, udekkede plasser, alle berørtes kontroll/konsekvenser, historikk, kostnad, P1/P2, rang eller sorteringsmangel og standardforklaring. |
| Regelrad | R1–R5, status (bestatt/regelavvik/uavklart/ikke_vurdert), verdi, konkret forklaring, kilde og begrensning. |
| Personkonsekvens | Ansatt-ID, timer før/etter, hvile før/etter, alle regelrader og mangler. |
| Kostnad | NOK, fullstendighet, total/referanse/differanse eller null, merket kjent delsum, tildelinger/intervaller med timer/satser/tillegg/beløp, mangler og utelatte kostnader. |
| Historikk | Uke 1–4 med periode, kilde, timer/vakter fra datasettet og fullstendighetsmerke. Ingen ny poengsum. |
| Standardforklaring | Fire felt: kort svar, avveining, konsekvenser og usikkerhet; beregnede tall og synlig uendret vaktliste. |

ID-en er stabil for samme grunnlag/sluttplan og uavhengig av sortering.
Bare identiske sluttplaner kan slås sammen. Bare komplette, beståtte
alternativer med nødvendige sorteringsdata får rang; like kriterieverdier
gir lik rang. Ukjent P2 gir ikke automatisk P1-reserve. Kostnad og historikk
endrer ikke rangering eller kontroll utover faktisk nødvendig grunnlag.

Implementerte hjelpeklasser finnes i `backend/src/vaktmatch/api/models.py` og
beskrives av OpenAPI. `StateResponse` utvider datasettet med `coverage` og
`current_controls`. `EvaluationResponse` inkluderer også de aktive `absences`.
`AlternativeResult` bruker `candidate_id`, `kind`, `moves`, `control_status`,
`coverage_status`, `complete`, `selectable`, `affected_employee_ids`,
`affected_shift_ids`, `plan`, `uncovered`, `consequences`, `history`, `cost`,
`p1`, `p2`, `rank`, `sorting_missing` og `explanation`.
Delvis dekning inkluderer `coverage_reason` og `replacement_findings`, slik at
årsaken til ubekreftet Y-dekning kan undersøkes. Kontroll og dekning forblir separate.

Alle desimaler i resultatene er JSON-strenger, også timesatser med flere enn to
desimaler. `CostResult.assignments` og `reference_assignments` inneholder
`segments` med start/slutt, timer, sats, tillegg og uavrundet intervallbeløp;
tildelingens `amount` er avrundet til øre. `known_subtotal` merkes som ufullstendig
når `complete=false`. Nullverdier blir aldri et nullkronersanslag.

Datasettdifferanser har rå `before`/`after` for etterprøving og norske
`label`, `before_label`, `after_label` for visning. Endringer i metadata-ID og
versjon vises i sammenligningshodet; `unchanged` gjelder selve datainnholdet.
Kumulativ fraværsinput valideres også ved vurdering, slik at klienten ikke kan
fjerne en historisk nabovakt. Kildeført fravær i uke 5 kan fortsatt beholdes ved
oppdatering. Vakters tilhørighet til uke 5 bestemmes av starttid i arbeidsuken;
en nattvakt kan slutte etter periodegrensen og kontrolleres som hel vakt.

## Økt og oppdateringer

React eier utkast, aktive fravær, valgt/undersøkt forslag og simulerte svar.
API-et er tilstandsløst. Valg/svar nøkles til innlastingsnummer,
datasett-ID/versjon, kanoniske aktive fravær, målskift og stabil forslag-ID.
Forslag A → B → A bevarer As svar innen samme innlasting. Hver ny datainnlasting
krever ny vurdering og nye svar, også ved retur til et tidligere datasett.

Nye data forhåndsvises før bytte. I samme `family_id` beholdes gyldige tidligere
fravær, også når en oppdatert plan viser en faktisk ny erstatter. Bortfalte
referanser forklares. Bytte til et annet forhåndslaget scenario opplyser at
nytt scenariogrunnlag startes; tidligere valg/svar beholdes som økthistorikk.
Sene API-svar fra gammelt grunnlag ignoreres. Navigasjon sperres under handlinger;
klientforespørsler avsluttes etter 15 sekunder med norsk feil og gjenforsøk.
Ingen `localStorage` eller ekte
utsending brukes. Full simulert aksept krever ja fra alle berørte personer.
