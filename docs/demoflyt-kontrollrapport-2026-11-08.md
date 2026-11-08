# Kontrollgrunnlag for SCRUM-19

Codex · 08.11.2026 · implementering på Odins gjennomføringsmandat.
Dette dokumenterer utført arbeid og tekniske kontroller, ikke brukertest,
felles detaljgodkjenning eller attest på lov-/avtalesamsvar.

## Levert og kontrollert

Den lokale appen viser nå ukeplan, eksplisitt fravær på ett målskift, beregnede
direkte alternativer/én flytting, P1/P2, alle berørtes R1–R5, historikk,
syntetisk kostnad, valg og tilbud/svar i økten samt forhåndsvisning og innlasting
av faste dataoppdateringer. Kildeplan og datasettfiler muteres aldri av API-et.
Grunnlaget er [implementeringsspesifikasjonen](../_bmad-output/implementation-artifacts/spec-scrum-19-demoflyt.md),
[HTTP-kontrakten](api-demoflyt.md) og kildene der.

| Kjørt kontroll | Faktisk resultat |
|---|---|
| `cd backend; uv run pytest` | 64 beståtte tester. Én avhengighetsadvarsel om Starlettes fremtidige TestClient/httpx-adapter; ingen testfeil. |
| `uv run ruff check .` / `uv run ruff format --check .` i backend | Bestått. |
| `cd frontend; npm test` | 20 beståtte tester i tre filer. |
| `npm run lint` / `npm run build` i frontend | Bestått uten lintadvarsler; TypeScript og produksjonsbygg bestått. |
| Playwright mot faktisk app | 50 beståtte kontroller, inkludert elleve axe-pass. Ingen JavaScript-feil eller eksterne modellkall. |
| Reproduksjon av demodata | Alle elleve JSON-datasett samsvarer semantisk med generatorens resultat i en separat midlertidig mappe. |

Testene bruker faktiske backendberegninger for regel-, sorterings- og
kostnadsfasit. Frontendens små kontraktfiksturer tester grensesnittets
tilstandsoverganger og gjør ingen påstand om beregningsfasit.

## Fasit og regresjoner

| Kontrollgrunnlag | Konkret bevis i `backend/tests/test_demoflow.py` eller frontendtestene |
|---|---|
| S1 / R1–R5 / P1/P2 | A02 24 → 32 t og 16/16 t hvile; A03 32 → 40 t og 12/16 t. P1/P2 bytter rekkefølge; A04–A08 har forventede avvik og V01 er uavklart. Kildeobjektet forblir identisk. |
| S2–S5 | Ingen direkte beståtte, manglende/komplettert tilgjengelighet, lik rang og manglende P2 uten skjult P1-reserve. |
| F2–F4 | Bare grense 1 gir B→X/C→Y. Manglende erstatter gir synlig udekket Y og konkrete kontrollfunn. Låst Y flyttes ikke; låst X kan ha fravær. |
| H4/H5 | Eksakt 11 t ved arbeidsukens start består, 10 t gir avvik og nødvendig ukjent nabogrunnlag gir uavklart uten kjent brudd. Ved ukeslutt gir utilstrekkelig kontrollperiode uavklart; bekreftet uke-6-vakt 11 t etter består. |
| Tid og datagrenser | UTC-varighet over sommertidsgrensen, faktisk del av nattvakt i arbeidsuken, slutt=start uten overlapp og sammensatte tilgjengelighetsintervaller. |
| O1/O2 | 1 800/0/+1 800 NOK ved direkte erstatning; 3 240/1 600/+1 640 NOK ved flytting. |
| O3/O5 | Manglende sats/tillegg gir ukjent total/differanse; intervalltillegg gir 1 650 NOK; 200,005 avrundes til 200,01 per tildeling. |
| O4 | Ny sats og versjon beregner A03s nye berørte vakt på nytt: 1 600 → 1 800 NOK, med sats 225 og ny forslag-ID. |
| M1/M2 | To kumulative fravær beholdes både med og uten planoppdatering. X er fortsatt udekket uten oppdatering; oppdatert kilde viser A03 på X og 40 timer som inngår i neste kontroll. |
| Feil / utdatert grunnlag | 409 ved gammel versjon, 422 ved ugyldig referanse/uke/kriterier, blokkert historisk fraværsinput og 503 ved ugyldig JSON/fullmodell uten interne filstier. Ukjent datasett gir 404 i eksisterende API-test. |
| Økt og tilbud | Separate fraværs-/søkehandlinger, A→B→A med bevart avslag, gyldig fravær ved datasettbytte, historiske valg/svar og alle berørtes aksept. Flyttevalg som forsvinner ved grense 0 kan ikke få tilbud på nytt resultat. |
| Nøkler | Gjentatt fravær er idempotent; duplikatfravær gir samme forslag-ID. Øktnøkler skiller versjoner og ID-er som inneholder kolon. |

Hovedtabellens S1-fasit gjelder direkte erstatning, grense 0. Standardgrense 1
undersøker flere sluttplaner og kan gi andre hovedkandidater/flyttinger øverst.
Ingen forslag slås sammen bare fordi de har samme hovedkandidat.

## Faktisk nettleserkontroll

Samlet kontroll av den kjørende appen med Playwright og axe dokumenteres i
[nettlesergrunnlaget](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/browser-results.json)
og den kjørbare [kontrollrutinen](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/verify-browser.py).
De faktiske skjermene finnes som [PC](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/live-alternatives-desktop.png)
og [mobil](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/live-alternatives-mobile.png).
Disse kontrollene bruker backend og JSON-datasettene, ikke den tidligere UX-mocken.
Nettlesergrunnlaget angir hvilke bredder, tekststørrelser, tastatur-/feilveier
og øktoverganger som faktisk ble kjørt. Automatisk axe-kontroll erstatter ikke
manuell skjermlesertest eller brukertest.

Kjør appens backend og frontend etter README. Fra reporoten kan kontrollen
gjentas med `uv run _bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/verify-browser.py`.
Rutinen trenger installert Playwright Chromium; `--browser` kan angi en
eksisterende Chromium-binær. For axe-kontroll angis en lokal `axe.min.js` med
`--axe`. Rapporten angir om axe faktisk var aktivert; denne kjøringen brukte
Chromium 145 og axe. Ingen av disse verktøyene legges inn som produksjonsavhengighet.

## Kodegjennomgang og etterkontroll

Tre separate KI-gjennomganger ga 16 konkrete funn, gruppert til 14 rettelser:
forklaring av alle berørte, lesbar P2/mangler, avgrensning av gamle kollisjoner,
aksept knyttet til hver datainnlasting, virksomme gjenforsøk, navigasjon under
forespørsler, riktig kriteriemerking, historikkens dekningsperiode og sommertid,
overføring av tidsmessig gyldig fravær, 15 sekunders klientfrist, fullstendige
flyttealternativer samt testdekning for historikk og gjeldende kontroller.
Alle ble rettet og kontrollert på nytt av den opprinnelige gjennomgangen;
ingen funn ble utsatt. Individuelt grunnlag og dommer står i spesifikasjonens
Review Triage Log. Dette er KI-kontroll, ikke menneskelig akseptansetest.

Sluttkontrollen over ble kjørt etter rettelsene. To tidligere demonstrerte
testgap ble også kontrollert med prosesslokale mutasjoner: feil historikk ga
tre testfeil, og tomme gjeldende kontroller ga én testfeil. Normal kjøring er grønn.

## Målt beregningstid

[Målerutinen](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark.py)
og [råmålingene](../_bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark-results.json)
kan gjentas fra roten med
`uv run --project backend python _bmad-output/implementation-artifacts/demoflyt-verifikasjon-2026-11-08/benchmark.py`.
Hovedscenarioet har ni ansatte og 73 vakter. Etter to oppvarminger og tolv
målinger per søkegrense var medianen 18,642 ms ved grense 0 (ni kombinasjoner)
og 282,338 ms ved grense 1 (109 kombinasjoner); nærmeste-rang-p95 var henholdsvis
22,239 og 313,504 ms. Ingen feil eller avbrudd ble registrert.
Dette er lokal motorberegning på Windows AMD64/Python 3.12.14, uten HTTP,
filinnlasting, grensesnitt eller modell. Målingen dokumenterer dette lille
scenarioet og etablerer ingen responstids- eller skaleringsgaranti.

## Bevisste grenser

- Ett målskift og én manglende plass per søk, høyst én flytting. Flere fravær
  beholdes, men appen løser dem ikke samlet og reserverer ingen ansatte.
- R1–R5 er avgrensede scenarioregler. Historiske registrerte vakter er ikke
  dokumentasjon på faktisk utført arbeid. Alle personer og satser er syntetiske.
- Ingen språkmodell/leverandør er valgt eller implementert. Standardforklaring
  og ærlig reserve virker uten nøkkel; dette oppfyller ikke full modellfunksjonalitet.
- Ingen konto, skytjeneste, filopplasting, faktisk utsending, varig logg eller
  innføring av foreslåtte vakter. Økten avsluttes når fanen lukkes.
- Søkestatus støtter `avbrutt`, men den lille synkrone søkemotoren har ingen
  avbryt-/tidsgrensefunksjon. Målt `duration_ms` gjelder bare backendberegningen;
  ingen garantert responstid eller større søkegrense er etablert.
