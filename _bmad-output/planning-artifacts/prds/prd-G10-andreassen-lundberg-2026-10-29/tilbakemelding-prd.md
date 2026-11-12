# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G10 – G10-andreassen-lundberg |
| **PRD vurdert** | `_bmad-output/planning-artifacts/prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md` (status `final`, sist endret 2026-10-31, commit 26bf827) |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

Dette er en av de sterkeste PRD-ene å bygge videre på: en tydelig tese, nummererte krav med testbare konsekvenser, ærlige ikke-mål og konkrete NFR-er. Største risiko er omfanget. «Må» har vokst til 22 av 24 FR-er pluss ni NFR-er for to personer, og mange tester peker ut av PRD-en til andre dokumenter.

## 2. Dette fungerer godt

1. **Tesen er skarp og målbar.** §1 «Kjernesetning»: «uten at appen noen gang viser et regelbrudd som gyldig». SM-1 («0 av alle kontrolltilfellene») gjør den testbar, og FR-5 skiller *oppfyller*, *regelavvik* og *uavklart*. Dette er et produktspesifikt løfte, ikke pynt.
2. **KI er avgrenset og kontrollert.** FR-18/19: modellen får bare kontrollresultatet, svaret har faste felt, standardforklaring tar over ved manglende nøkkel eller feil, og tester kjører i testmodus uten nøkkel. SM-C2 («Hvor flytende ... KI-teksten er») er en god motmåling.
3. **Ærlig om hva som ikke er bevist.** §1 sier at merverdien «ennå ikke [er] dokumentert», §6 utelukker «optimal», og §7.2 viser hvilke omfangsvalg som er endret fra briefen og hvorfor.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet | god | Valg og avveininger er synlige (§7.2), men beslutningsspor ligger inne i kravtekstene. |
| Substans | sterk | Én konstruert persona som styrer valg, NFR-er med tall (20 min, 4,5:1, 360 px). |
| Strategisk sammenheng | god | Regeltesen er sterk. «Fair fordeling» og kostnad i §1 er en andre tese som PRD-en selv sier ikke dekkes. |
| Testbarhet | god | De fleste FR-er har konsekvenser, men flere henviser til eksterne tabeller (S1, F1–F4, O1–O5). |
| Scope og avgrensning | god | Må/Bør og ikke-mål er eksplisitte, men Må er stort for to personer og ett semester. |
| Brukbarhet for neste fase | god | Glossar og kontinuerlige FR-IDer finnes, men PRD-en kan ikke leses alene. |
| Formtilpasning | god | Passer et UI-produkt. UJ-1 er overlesset, og prosessnotater fyller toppen. |

## 4. Viktigste forbedringer

### 4.1 «Må» er for stort, og det mangler en kuttlinje
- **Alvorlighet:** høy
- **Hvor:** §7.1 «Må: FR-1 til FR-21, FR-24 og NFR-1 til NFR-6, NFR-8 og NFR-9»; §7.2 (tilbud, datasettbytte og kostnad er flyttet fra Bør til Må)
- **Problem og hvorfor det betyr noe:** Kjerneflyten, KI-forklaring, tilbudssimulering, datasettbytte, kostnadsanslag og sekvensielle fravær er alle Må. Rubrikken ber om ærlig scope, og dere gjør neste fase (epics og sprintplan) vanskelig når alt er like viktig. Tilbakemeldingen på briefen anbefalte en smal v1.
- **Forslag:** Del Må i to trinn med en kuttrekkefølge, for eksempel: «Må-kjerne: FR-1–17, FR-19 (standardforklaring), NFR-1–6. Må-hvis-kjernen-er-grønn: FR-18, FR-20, FR-21, FR-24. Hvis kjernen ikke er testet grønn innen [dato], faller FR-24 først, deretter FR-20.»

### 4.2 Testene hviler på dokumenter utenfor PRD-en
- **Alvorlighet:** medium
- **Hvor:** FR-4 «stemmer med demoscenarioets tabell»; FR-9 «F1–F4 gir forventet resultat»; FR-24 «O1–O5»; FR-22 og FR-23 har ingen konsekvenser
- **Problem og hvorfor det betyr noe:** Story-skriving og testing må åpne tre andre filer for å vite hva «ferdig» er. FR-22 («Lederen låser og låser opp ...») kan ikke bli et testtilfelle som den står.
- **Forslag:** Gjengi minst ett nøkkeltilfelle per FR i selve kravet, f.eks. FR-13: «Konsekvens: Med P1 står A02 (32 t) før A03 (40 t); med P2 står A03 først; kontrollstatus og plan er uendret.» Legg til for FR-22: «Når en tildeling låses, foreslås den ikke flyttet i neste søk, og et søk kjørt før låsingen merkes utdatert.»

### 4.3 KI-kontrollen mangler tall og kjøretidssjekk
- **Alvorlighet:** medium
- **Hvor:** FR-19 «ved tidsavbrudd»; §9 spørsmål 3 («Hvilken modell og leverandør, og hvilken kostnadsgrense?»); FR-19 «En test sjekker at tall og statuser ...»
- **Problem og hvorfor det betyr noe:** Tidsavbrudd, kostnadsgrense og antall kall er ikke tallfestet, og spørsmålet står åpent selv om FR-18 snart skal bygges. Samsvar mellom KI-svar og kontrollresultat testes bare, men sjekkes ikke når appen kjører.
- **Forslag:** «Tidsavbrudd er 10 s. Maks 20 KI-kall per økt. Før visning sammenlignes tall og statuser i svaret med kontrollresultatet; ved avvik forkastes svaret og standardforklaringen vises med meldingen "KI-svaret ble ikke brukt".» Lukk spørsmål 3 nå, tallene kan justeres senere.

### 4.4 Beslutningsspor og prosessnotater forstyrrer kravene
- **Alvorlighet:** medium
- **Hvor:** innledningen i parentes («Skrevet: Claude Code ... Oppdatert av Codex ...»); FR-10, FR-15, FR-18 («Besluttet av ... 29.10.26»); §9 om Jira-status; §10 «Antakelser»
- **Problem og hvorfor det betyr noe:** Hvem som besluttet hva hører hjemme i §7.2 og memloggen. I kravtekst gjør det FR-ene lengre og vanskeligere å gjøre om til stories. §10 beskriver opphav, ikke antakelser: det finnes ingen `[ASSUMPTION]`-merker og ingen indeks. Statusen `final` stemmer dårlig med fire åpne spørsmål.
- **Forslag:** Flytt beslutningsopphav til én kolonne i §7.2. Gjør §10 til en ekte liste, f.eks. «Syntetiske satser i FR-24 er tilstrekkelig realistiske til å vise en kostnadsforskjell», og merk dem `[ASSUMPTION]` der de brukes. Vurder `draft` til spørsmål 3–5 er lukket.

### 4.5 UJ-1 bærer for mye
- **Alvorlighet:** lav
- **Hvor:** UJ-1; UJ-2 og UJ-3; FR-20, FR-21, FR-24 (ingen «Realiserer UJ»)
- **Problem og hvorfor det betyr noe:** UJ-1 rommer søk, sortering, KI, tilbud, kostnad og datasettbytte i én tekst. Det gjør UX-flyt og epics uoversiktlige. UJ-2 («Som UJ-1») og UJ-3 har ingen egen protagonist.
- **Forslag:** Behold UJ-1 til «Kari velger A03». Flytt tilbud, kostnad og datasettbytte til en ny UJ-5, og knytt FR-20, FR-21 og FR-24 til den. Navngi hvem som er i UJ-2 og UJ-3.

## 5. Mekaniske funn

- FR-1–FR-24 er kontinuerlige, men FR-24 står i §4.7 foran FR-22/23. SM-6 står mellom SM-2 og SM-3.
- Åpne spørsmål hopper over nr. 2 (forklart som lukket i teksten).
- Glossaret mangler *fravær*, *vikar*, *tilbud* og *R1–R5*/*P1/P2* som begreper. «Målskift» og «vakten» brukes om hverandre i UJ-ene, og «økt» betyr både nettleserøkt (§3) og arbeidsøkt (NFR-8).
- Interne lenker (`../../../../docs/...`, research) løser seg fra PRD-mappen. Ingen sensitive opplysninger funnet.

## 6. Før dere går videre

**Må avklares før UX, arkitektur og epics:** kuttlinjen i Må (4.1), modell/leverandør og kostnadsgrense (spørsmål 3), og hvordan en ekstern vikar modelleres (spørsmål 4, påvirker datamodellen).

**Kan vente:** skiftlederprofil (spørsmål 5), sluttfrist for rapport (spørsmål 1), varig logg (FR-23).

**Oppfølging av briefen: delvis.** Én gjeldende brief er valgt, KI er definert i v1 med testmodus og drift uten nøkkel, fasit-scenarioer finnes (S/H/F/D) og suksesskriterier er knyttet til dem. Rådet om en smal v1 er ikke fulgt fullt ut, se 4.1.

## 7. Refleksjonsspørsmål

1. §7.2 viser at flere funksjoner gikk fra Bør til Må. Hvilke argumenter vurderte dere for og mot, og hvordan kontrollerte dere at KI-forslagene om å utvide omfanget var realistiske for to personer?
2. FR-24 bygger på en kostnadsformel som er laget ved hjelp av KI. Hvordan har dere kontrollert at O1–O5 faktisk er riktig regnet, og hva godtok dere uten egen kontroll?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
