# Utdrag: research og krav til PRD-arbeidet (VaktMatch)

Utarbeidet 2026-10-28 som arbeidsgrunnlag til PRD-en. Dette er et utdrag og ikke nye krav, beslutninger eller produktfunn. Hver påstand har filhenvisning. Anbefalinger i kildene er KI-vurderinger (Codex), ikke felles beslutninger. Ingen egne intervjuer eller brukertester er gjennomført.

Forkortelser for kildefiler (alle stier er relative til reporoten):

- **R** = `_bmad-output/planning-artifacts/research/user-voice-vaktmatch-brukerbehov-og-prd-grunnlag-2026-10-26/research.md`
- **RB** = samme mappe, `brief.md`
- **D-brukere** = samme mappe, `digests/user-needs-r1-1.md`
- **D-konk** = samme mappe, `digests/competitors-r1-1.md`
- **D-ki** = samme mappe, `digests/ai-explanations-r1-1.md`
- **D-verif** = samme mappe, `digests/verification-r1.md`
- **PF** = `docs/prd-forberedelser.md`
- **TB** = `tilbakemelding-product-brief.md` (faglærers tilbakemelding 2026-10-06 på `productbrief.md`)
- **LK** = `docs/ibe160-leveringskrav.md`

Henvisninger som [1]–[11] viser til kildenummer i R, tabellen «Kilder».

---

## 1. Hva researchen støtter, med styrke

### 1.1 Omfang og metode

- Én kort innsamlingsrunde, tre spor, inntil to samtidige assistenter, høyst fem nye kilder per spor. Elleve kilder: tre om brukerbehov, fem leverandørsider, tre om forklaringer. (R, «Avgrensning og bevisstyrke»; RB; PF, «Godkjent researchplan»)
- Prosjektets egne dokumenter styrte spørsmålene og er ikke brukt som eksternt bevis. (R, «Avgrensning og bevisstyrke»; RB)
- Rapportstatus: `claims_verified: 2`, `claims_unverified: 3`. (R, frontmatter og «Kontroll og status»)
- «Verified» betyr at en snever syntese har uavhengig støtte, ikke at produktets effekt er vist. (R, «Avgrensning og bevisstyrke», «Kontroll og status»)

### 1.2 Førstehånds originalstudier (empiri)

| Kilde | Hva den støtter | Styrke og forbehold | Henvisning |
|---|---|---|---|
| [4] Agenda Kaupang for NSF, 2022-09-16 (tverrsnittsundersøkelse, 708 førstelinjeledere totalt; 82 % enige på spørsmål med n=624) | Det er vanskelig å skaffe vikar/ekstravakt med samme kompetanse ved korttidsfravær | Middels sikkerhet for overføring. Historisk, selvrapportert, helsetjeneste. Svarprosent og rådata ikke kontrollert. Tallet er ikke et nåtidsestimat. | R «Brukerbehov»; D-brukere F1; D-verif S1 |
| [6] Svensk kvalitativ intervjustudie, 2023-12-09 (11 førstelinjeledere og 9 bemanningsassistenter, fire regioner) | Nytte av oversikt over arbeidstid på tvers av avdelinger, overtid og vaktlagets kompetanse. En flytting kan skape nytt bemanningshull. Uklare varsler og avveininger mellom ønsker og restitusjon. | Middels, enkeltstudie. Deltakerbeskrivelser, ikke prevalens eller effekt. Flere avsnitt fra samme studie gir ikke flere uavhengige kilder. | R «Brukerbehov»; D-brukere F3, F4; D-verif A2, S2 |
| [5] Finsk før/etter-studie, 2020-03 (61 ledere, 5 800 oppgaver, 2 628 fraværshendelser) | Færre lederoppgaver, ubemannede vakter og uplanlagte vaktendringer etter IT-støtte | Middels for sammenhengen, lav for kausalitet og overføring. Bare abstract lest. Ingen kontrollgruppe. Kan ikke love tidsbesparelse. | R «Brukerbehov»; D-brukere F2; D-verif S3 |
| [1] Bansal mfl., ACM CHI 2021 (sentiment og LSAT) | Forklaringer ga ikke statistisk signifikant bedre beslutningsnøyaktighet enn KI-råd med konfidensanslag. Aksept økte også ved feil råd. | Middels, enkeltstudie. «Ikke signifikant» er ikke bevist null effekt. Ikke bemanning, ikke moderne språkmodell. | R «KI-forklaringer»; D-ki A1; D-verif S4 |
| [2] Buçinca mfl., CSCW 2021 (199 deltakere i analysen, ernæringsoppgave, simulert KI) | Aktiv vurdering reduserte overavhengighet, men de mest effektive utformingene fikk svakere subjektive vurderinger | Middels, enkeltstudie. Annen oppgave og målgruppe. | R «KI-forklaringer»; D-ki A2; D-verif S5 |

### 1.3 Metodeargument (ikke effektstudie)

- [3] Jacovi og Goldberg, ACL 2020: skiller mellom en forklaring som virker overbevisende (plausibilitet) og en som gjengir beslutningsgrunnlaget riktig (trofasthet). Middels sikkerhet. Metodebidrag, ikke empirisk replikasjon. Anvendelse på VaktMatch er Codex sin vurdering. (R «KI-forklaringer»; D-ki A3; D-verif S6)

### 1.4 Leverandørpåstander (egenbeskrivelser, ikke testet)

- [7]–[11] er leverandørers hjelpesider, produktsider eller markedsføring. Alle funksjonspåstander er merket «middels / unverified». Funksjonene er ikke prøvd. (R «Lignende løsninger»; D-konk, innledning)
- Datering: Quinyx Skills [9] er publisert 2026-07-29 og oppdatert 2026-08-18. Sidene [7], [8], [10], [11] har ukjent publiseringsdato. Besøksdato (2026-10-26) erstatter ikke publiseringsdato. (R «Kilder» og «Når bør funnene sjekkes igjen?»; D-konk C1–C5)
- [10] Quinyx Scheduling Automation er markedsføring. [8] har «forelopig-under-redigering» i URL-en, og status er uavklart. (R «Kilder»; D-konk C2, C4)

### 1.5 Overføringsgrunnlag (hva som ikke er VaktMatchs målgruppe)

- Alle tre brukerbehovskildene gjelder helsetjenesten (sykehjem, hjemmesykepleie, sykehusavdelinger). Kompetansefunn er et overføringsgrunnlag, ikke validering av en annen målgruppe. (R «Brukerbehov» og «Spørsmål til diskusjon» nr. 1; D-brukere F1–F4)
- Forklaringsstudiene bruker andre oppgaver (tekstanalyse, logikk, ernæring) og crowd-deltakere. De er overføringsgrunnlag og ikke målgruppevalidering. (R «KI-forklaringer»; D-ki A1–A2; PF, tabellen over sporene)
- Historiske studier beholdes som historiske uten automatisk utløpsvindu. (R «Avgrensning og bevisstyrke», «Når bør funnene sjekkes igjen?»)

### 1.6 Samlet støtte (smale formuleringer fra kontrollen)

- Verifisert, middels sikkerhet: kompetanse ved fraværsdekning er et begrunnet tema å undersøke i en helsefaglig kontekst. Dette er ikke et produktkrav og ikke dagens utbredelse. (D-verif A1)
- Ikke uavhengig korroborert: behovet for oversikt over hele arbeidstiden og følger for senere vakter. Kilden er i praksis én studie (svensk). (D-verif A2; R «Kontroll og status»)
- Omstridt formulering som skal rettes: «Flere uavhengige studier bekrefter alle tre behovene». Forsvarlig lesning: ulike historiske helsestudier gir samlet grunn til å undersøke kompetanse, arbeidstidsoversikt og følger av vaktendringer, og detaljene har ulik evidensstyrke. (D-verif A3)
- Verifisert, middels sikkerhet: at en forklaring øker aksept eller gir gode subjektive vurderinger, er alene utilstrekkelig dokumentasjon på bedre beslutninger. (D-verif B1)
- Rapportens anbefaling: behold den avgrensede fraværssituasjonen som arbeidsgrunnlag, og prioriter forståelig sammenligning av kandidater og konsekvenser. Dette er en anbefaling til diskusjon. (R «Hva researchen gir oss»)

---

## 2. Hva researchen IKKE validerer

- **Målgruppebehov.** Ingen lokal målbruker er intervjuet. Roller, datakvalitet, aktualitet, tilgjengelighet og bekreftelse fra ansatte må avklares i valgt demo-kontekst. (D-brukere «Kunnskapshull»; R «Hva researchen gir oss»: validerer ikke «vår generiske målgruppe»)
- **Valg av målgruppe.** Helsetjenestefunn gjør ikke automatisk helsetjenesten til valgt målgruppe. (R «Spørsmål til diskusjon» nr. 1; TB «Who This Serves» sier at demodomenet (lager/logistikk) må bestemmes endelig)
- **Merverdi.** Etablerte løsninger dokumenterer allerede vikarsøk, sammenligningsinformasjon eller kompetansestøtte, så det finnes ikke grunnlag for å hevde at kombinasjonen er unik. KI-tekst har ingen påvist merverdi i vår oppgave. (R «Hva researchen gir oss»; D-konk «Samlet vurdering»)
- **Tidsbesparelse.** Den finske studien har ingen kontrollgruppe, og bare abstract er lest. Den kan ikke brukes til å love tids- eller kostnadsbesparelse. (R «Brukerbehov»; D-brukere F2)
- **Utbredelse og dagens situasjon.** Alle utbredelsestall er historiske og utvalgsavgrensede. Ingen ny prevalenspåstand. (D-brukere «Kunnskapshull»; R «Brukerbehov»)
- **Effekt av KI-forklaringer.** Ingen av eksperimentene tester moderne generativ språkmodelltekst i bemanningsarbeid. Det finnes ingen sammenligning av KI-omskriving og maltekst i målgruppen. (D-verif B2; D-ki «Syntese til kontroll»)
- **Regler, lov og avtale.** Ingen dokumentasjon fastsetter norske lov- eller avtalegrenser, eller en korrekt kvalifikasjonsmodell. Studienes praksiseksempler skal ikke brukes som rettsregler. Researchen undersøker ikke juridisk etterlevelse og velger ikke modell eller hosting. (D-brukere «Kunnskapshull»; RB)
- **Rangering og vekting.** Kildene dokumenterer ikke at kombinasjonen deterministiske regler + kandidatsammenligning + menneskelig valg er foretrukket, eller hvordan en rangering bør vektes. Kandidaten er et testforslag. (D-brukere, slutten av «KI-forslag til PRD-arbeidet»; R «Brukerbehov», siste avsnitt)
- **Skjermbilde og MVP-omfang.** Kildene avgjør ikke skjermbildet, sorteringskriteriene eller MVP-omfanget. (R «Brukerbehov», KI-vurdering til PRD-diskusjonen)
- **Konkurrentenes faktiske funksjon.** Funksjonene er lest, ikke prøvd. Manglende dokumentasjon er ikke bevis på manglende funksjon. (R «Lignende løsninger»; D-konk «Samlet vurdering»)
- **Ansattes behov.** Svenskstudien peker mot ansatte som egen forskningsgruppe; deres behov kan ikke erstattes av ledernes beskrivelser. (D-brukere «Kunnskapshull»)
- **Produktstatus i prosjektet.** Researchrunden endret ingen produktbrief, PRD, Jira-sak eller personlige notater. Ingen produktkrav er vedtatt. (R «Kontroll og status»; RB)

---

## 3. Konkurransebildet: Simployer (Capitech), Quinyx, 4human

Alle opplysninger her er leverandørens egenbeskrivelse. Ingen er testet. (D-konk, innledning; R «Lignende løsninger»)

### 3.1 Hva som er lært

| Løsning | Dokumentert (leverandørpåstand) | Henvisning |
|---|---|---|
| Simployer/Capitech | «Finn vikar» søker tilgjengelige ansatte for en vakt, uttrykkelig også ved sykdom og fravær. «Meld behov for vikar» publiserer behov i MinCapitech der ansatte kan melde interesse. Beregnet kostnad vises for ulike tilgjengelige vikarer. Satser knyttes til lønnsarter (blant annet overtid og tillegg). | R [7][8]; D-konk C1, C2 |
| Quinyx | Skills: filtrering/sortering etter nødvendige ferdigheter, antall samsvarende ferdigheter. Warnings: varsler som navngir manglende ferdighet, og leder kan likevel tildele vakten. Markedsføringens FAQ: ny beregning av dekning ved siste-liten-endringer (fravær, vaktbytte) med vurdering av tilgjengelighet, ferdigheter, kvalifikasjoner, preferanser og arbeidsbelastning. Leder kan overstyre. | R [9][10]; D-konk C3, C4 |
| 4human | «Detaljert plan» beskriver løpende endringer i faktiske arbeidsplaner. «Digital arbeidsplan» beskriver varsler ved fravær sammen med time-/fraværsmodulen. Ledere kan justere planer, og ansatte ser dem på mobil. | R [11]; D-konk C5 |

Læring til PRD-en (Codex-vurdering): beskriv dokumenterte delkapabiliteter presist, og unngå en unikhets- eller differensieringspåstand. Beskriv VaktMatch som en avgrenset studieprototype som gjør alternativer og konsekvenser etterprøvbare. En påstand om bedre oversikt eller forståelse må testes. Kostnadssammenligning hos en leverandør er inspirasjon, ikke vedtak om å utvide MVP. (D-konk «Samlet vurdering»; R «Lignende løsninger», KI-vurdering til brief/PRD)

### 3.2 Overlapp med VaktMatch

- Vikarsøk ved fravær og publisering av behov (Capitech). (D-konk C1)
- Kostnadsvisning per tilgjengelig vikar (Capitech). (D-konk C2)
- Kompetansesortering og navngitte mangler, med leders mulighet til å overstyre (Quinyx). (D-konk C3)
- Automatisk ny beregning ved akutte endringer, leverandørpåstand (Quinyx). (D-konk C4)
- Fraværsvarsler og planjustering (4human). (D-konk C5)
- Konsekvens: en generell påstand om at forklart beslutningsstøtte eller kvalifikasjonsstøtte mangler hos konkurrentene kan ikke videreføres. (D-konk C3, «Nytt mot gammelt hull»)

### 3.3 Åpne hull (ikke verifisert, «ikke verifisert» betyr ikke «finnes ikke»)

- Capitech: hvilke regler vikarsøket anvender, hvordan kandidatene sorteres, og begrunnelse per kandidat. Ikke spesifisert. AML- og kompetansevarsler inne i «Finn vikar» er ikke lest. (R «Lignende løsninger»; D-konk C1, «Samlet vurdering»)
- Capitech: ikke dokumentert at kandidater rangeres etter kostnad, eller at en forklart modell sammenligner intern omfordeling, overtid og ekstern innleie. (D-konk C2)
- Quinyx: samlet rangering, nøyaktige regelvalg og presentasjon av flere forklarte omfordelingsalternativer er ikke verifisert. Hjelpesidene «Absence handling» og «Auto Schedule and Auto Assign Warnings» er bare søkespor, ikke lest. (R «Lignende løsninger»; D-konk C3, C4, «Samlet vurdering»)
- 4human: erstatningsforslag, kandidatkontroll, rangering og forklaring er ikke avklart. (R «Lignende løsninger»; D-konk C5)
- Datering: Capitech-sidene, Quinyx-markedsføringen og 4human-siden har ukjent publiseringsdato og bør kontrolleres før de brukes til en påstand om dagens konkurransefortrinn. (R «Når bør funnene sjekkes igjen?»)
- Mulige videre spor, ikke vedtatt: leverandørdemoer med akutt sykefravær og to mulige erstattere; mer detaljert hjelpedokumentasjon. (D-konk «Samlet vurdering»; R, siste avsnitt i «Spørsmål til diskusjon»)
- Neste beregnbare kontroll: 2026-11-18 (Quinyx Skills). (R «Når bør funnene sjekkes igjen?»)
- Det eldre konkurransedokumentet fra 2026-09-07 er brukt som spørsmålsgrunnlag, ikke som nytt bevis. (R «Lignende løsninger»; RB; D-konk «Forskningsregler og kildegrense»)

---

## 4. KI-forklaringer: foreslått evalueringsmetode og kvalitetskrav

Status: forslag fra Codex, ikke vedtatte akseptansekriterier. (R «KI-forklaringer», siste avsnitt; D-ki «Syntese til kontroll»; PF «Godkjent researchplan», rad 3)

### 4.1 Foreslått evalueringsmetode

1. Sammenlign standardtekst (mal) og KI-tekst på samme scenario. (R «KI-forklaringer»; D-ki «Syntese»; R «Forslag å vurdere», rad 4)
2. Kontroller først at teksten gjengir regelresultat, rangering og manglende data riktig (trofasthet mot regelmotoren). (R «KI-forklaringer»; basert på [3])
3. Undersøk deretter om leseren forstår avveiningen, oppdager feil og bruker mindre tid. (R «KI-forklaringer»; D-ki «Syntese»)
4. Registrer feil og tid hver for seg. (D-ki «Syntese til kontroll»)
5. En flytende tekst, tillit, aksept eller tilfredshet er ikke alene mål på merverdi eller beslutningskvalitet. (R «KI-forklaringer», [1][2]; D-verif B1)
6. Sammenligning med standardtekst bør komme før modellvalg. (R «Hva researchen gir oss»; PF, tabellen, rad 3: «testbare kvalitetskrav før modellvalg»)
7. Produktspesifikke terskler og en eventuell brukertest er ikke vedtatt. (D-ki «Syntese til kontroll»)

### 4.2 Kvalitetskrav som kildene peker mot (ikke vedtatt)

- Faktasamsvar: KI-teksten skal ikke legge til udokumenterte fakta. (R «Spørsmål til diskusjon» nr. 4; R «Forslag å vurdere», rad 4)
- Sporbarhet til data og regelkontroll. Dette er faglærers allerede nevnte styrke i briefens suksesskriterier. (TB «Det som er bra» nr. 3)
- Forklaringene må ikke kunne si noe annet enn regelmotoren. (TB, tabell «KI-funksjonalitet i appen»)
- PRD-en bør formulere hva KI-teksten skal gjøre bedre enn standardteksten. Anbefalingen kobles til SCRUM-59 når oppgaven er konkret. (R «Forslag å vurdere», rad 4)
- Forklaringen bør vise hvilken vurdering manglende eller utdaterte opplysninger hindrer. (R «Spørsmål til diskusjon» nr. 3)
- PRD-en bør ta stilling til om KI-teksten skal gjøre bedre enn standardteksten i et scenario, og når standardforklaringen er nok. (PF «Brainstorming-temaer»; R «Spørsmål til diskusjon» nr. 4)

---

## 5. Faglærers råd som bør påvirke PRD-en

Kilde: TB (gjelder `productbrief.md` slik den var 2026-10-06, ikke nødvendigvis dagens løsning). (PF, tabell, rad «Faglærers tilbakemelding»)

### 5.1 Avgrensning

- Gruppen har to retninger (avvikshåndtering ved ett sykefravær og turnusgenerering med constraint-solver) og et forslag om sammenslåing, men faglærer noterte ingen felles beslutning. Avklar retning og samle i én oppdatert brief før PRD. (TB «De viktigste endringene» nr. 1; «Neste steg» nr. 1)
- Faglærers råd: behold avvikshåndteringen som hovedfunksjon med et enkelt, regelbasert ukesgrunnlag, og legg full periodeplanlegging med solver, rettferdighet og helgefordeling i et senere trinn. Velges sammenslåing: hold den til én uke, to kompetansetyper og ett fravær. (TB «Forslag til justering» nr. 1)
- Definer en minimal versjon som sikkert kan bli ferdig, og legg resten i tydelige trinn. (TB «Hva vanskelighetsgraden betyr for dere»)
- Vurdert vanskelighetsgrad: vanskelig, i nedre del hvis v1 holdes til ett ukesgrunnlag og ett fravær. (TB «Vurdert vanskelighetsgrad»)
- Bestem demodomenet (lager/logistikk) endelig. (TB «1. Gjennomgang», rad «Who This Serves»)
- Simulering av tilbud og aksept holdes utenfor. (TB, tabell, rad «Sanntid, samtidighet»)
- Hold siste suksesskriterium (tidsbruk og forståelse mot manuell oversikt) som brukertest, ikke som hovedkriterium. (TB «1. Gjennomgang», rad «Success Criteria»)

### 5.2 Konkrete regler

- Skriv ned 3–5 regler med konkrete verdier (for eksempel minst 11 timers hvile) og et regneeksempel. (TB «De viktigste endringene» nr. 2; «Forslag» nr. 2)
- Skriv rangeringen som en enkel, synlig prioritering (for eksempel dekning først, deretter færrest endringer). (TB «Forslag» nr. 2)
- Rammen 8–10 ansatte, 3–5 regler og ett fravær er god. Reglene, rangeringen, teknologistakken og forholdet til turnusforslaget var uavklart. (TB «1. Gjennomgang», rad «Scope»)
- Uten regler og rangering vil PRD-en enten gjette eller utsette det viktigste. (TB «Gjennomførbarhet», rad «BMAD-flyten»)
- Begrunn teknologivalget i arkitekturen, og vurder om en solver trengs i v1 eller om enkel regelbasert kode holder. (TB «2. Utgangspunkt», kriterium 5)

### 5.3 Scenarier

- Lag håndregnede scenarioer med fasit. Faste demoscenarioer med fasit gir grunnlag for automatiske tester. (TB, tabell «Kontroll på KI-ens arbeid»; kriterium 3)
- To–tre demoscenarioer med forventet resultat, inkludert ett fravær uten gyldig erstatter. (TB «Neste steg» nr. 2)
- Ett løsbart og ett uløsbart fraværsscenario er verdt å følge. (TB, tabell «Testbarhet»)
- Forventede statuser: godkjent, utelukket, uavklart, udekket. (TB, tabell «Testbarhet»)
- Faglærer anbefaler at demonstrasjonsforløpet i «forslag til felles retning» brukes som utgangspunkt for minimal versjon, med hvert steg enkelt. (TB «Hva vanskelighetsgraden betyr for dere»)
- Skisser ukesvisningen og sammenligningssiden, og hvordan «utelukket» og «uavklart» vises. (TB, kriterium 4)

### 5.4 Kjøring uten KI-nøkkel

- Sørg for at kjerneflyten virker uten KI, for eksempel med regelbaserte standardforklaringer, og at syntetiske data lastes automatisk. (TB, tabell «Kjørbar for sensor»)
- Gjør KI-forklaringen til et lag på toppen av en ferdig regelbasert flyt. Flytt friteksttolkning av behov til etter v1, slik at sensor kan kjøre og teste kjernen uten nøkkel. (TB «Forslag» nr. 3)
- Bestem hva KI gjør i v1 og hvordan appen virker uten nøkkel. Språkmodell er ikke valgt, og det finnes ingen plan for kostnad eller testmodus. Unngå eksterne tjenester sensor må sette opp. (TB «De viktigste endringene» nr. 3; tabell «Avhengigheter og kostnader»)
- Planlegg `.env.example` og demodata. (TB, kriterium 6 og 7)

### 5.5 Andre råd

- Briefen er positivt vurdert på arbeidsdeling mellom regelkontroll i kode og KI som kun tolker og forklarer, på ærlig usikkerhet, og på testbare suksesskriterier. Dette er forutsetninger som PRD-en bør bevare. (TB «Det som er bra»)
- Faglærer sier at gruppen kan gå videre med justeringer. Kilden bruker ikke ordet «godkjent». (TB «Samlet vurdering»; LK «Arbeidskrav: godkjent product brief»)
- Det finnes én tilbakemelding per brief (VaktMatch 2026-09-07 og turnusgenerering 2026-09-18) under `_bmad-output/planning-artifacts/briefs/…/tilbakemelding-product-brief.md`. Vurderingen i TB gjelder `productbrief.md` i roten. (TB, innledning)
- Gjeldende prosjektgrunnlag har siden levert besluttede scenarioregler, søkegrenser (0–1), lokal oppstart og utsatt modellvalg. PRD-en bør forholde seg til dem som arbeidsgrunnlag; endring må begrunnes. (PF «Grunnlag som allerede finnes» og «Brainstorming-temaer»)

---

## 6. Leveranse- og vurderingskrav som PRD-en må ta hensyn til

Kilde: LK, kontrollert mot Canvas 2026-10-22 og utvidet 2026-10-28, ellers som angitt.

### 6.1 Frister

| Tema | Status | Henvisning |
|---|---|---|
| Product brief | Frist 2026-09-27 kl. 23:59 (forlenget fra 20.09). Gruppen leverte 20.09. | LK «Kort status» og «Arbeidskrav» |
| PRD-forberedelse | Forberedelse til undervisning torsdag 2026-10-29, ikke ny sluttfrist. PRD-en trenger ikke være ferdig. | LK «Forberedelse til PRD»; PF «Kursbeskjeden» |
| Sluttfrist prosjektkode og refleksjonsrapport | Ingen skriftlig dato. Muntlig omtrent 15. desember som utgangspunkt (opptak 0:39–1:51). Rapporten leveres samtidig med applikasjonen. Leveringskanal ikke oppgitt. | LK «Kort status» |
| Sensors grunnlag | Siste commit før innleveringsfristen i organisasjonen `IBE160-2026`; senere endringer ses bort fra. | LK «Vurdering og dokumentasjon av KI-bruk» |

### 6.2 Vurdering

- Prosjektkode og funksjonalitet 70 %, refleksjonsrapport 30 %. Begge er gruppebesvarelser. (LK «Kort status»)
- Del 1-kriterier med vekt, fra faglærers utgangspunkt: prosess og KI-styring 30 %, funksjonalitet og omfang 20 %, kvalitetssikring og testing 15 %, design og brukeropplevelse 10 %, kodekvalitet og arkitektur 10 %, README og kjørbarhet 10 %, ryddighet i repoet 5 %. (TB «2. Utgangspunkt for del 1»)
- Refleksjonsrapporten krever personlig refleksjon for hvert gruppemedlem; forventet lengde 3 000–5 000 ord. (LK «Individuelle bidrag og refleksjonsrapport»)

### 6.3 BMAD

- Muntlig gjengitt (Odin 2026-10-28, støttet av transkripsjon ca. 3:05–3:22): BMAD med en KI-agent er ufravikelig; uten BMAD i repoet gis ikke karakter. Claude Code er ikke krav; annen KI-agent er tillatt (ca. 4:11–4:37). Ikke funnet i skriftlige Canvas-flater. (LK «Kort status», «BMAD og arbeidslogg»)
- BMAD-sporet (brief, PRD, arkitektur, epics og stories, sprintplan, implementasjon, gjennomgang) følges og dokumenteres i `_bmad-output/`. (LK «BMAD og arbeidslogg»)
- Sporbar vei fra plan til ferdig app: brief → PRD → arkitektur → stories → kode. (TB «Hvorfor product brief er viktig for mappen»; LK «Vurdering og dokumentasjon av KI-bruk»)

### 6.4 Logg

- Faglærer har ifølge Odins gjengivelse sagt at gruppen må ha en logg over arbeidet, og at mangel på logg kan påvirke sensuren (transkripsjon ca. 31:15–32:02). Eksempelformat: `.logs/` med plan, resultat og åpne punkter per økt, committet separat (ca. 43:25–46:09). Ett eksempel, ikke eneste godkjente format. (LK «BMAD og arbeidslogg»)
- Prosessen spores i `.memlog.md`, `docs/productbrief-endringslogg.md`, spec-filer per sak, Jira og commit-meldinger. (LK «BMAD og arbeidslogg»)
- Sensorveiledningen ber om spor etter KI-bruk: lagrede prompter og KI-sesjoner koblet til endringer, med eksempler på kritikk, korrigering eller forkasting av KI-forslag, og spor etter kodegjennomgang. (LK «Vurdering og dokumentasjon av KI-bruk»)
- Odin godkjente 2026-10-28 logg per arbeidsøkt (KI spør og skriver bare etter ja, brukeren leser før commit). Stian er ikke konsultert ennå. (LK «BMAD og arbeidslogg»)

### 6.5 Design og tilgjengelighet

- Design og brukeropplevelse: 10 % av del 1 (7 % av samlet karakter). (LK «Detaljerte kriterier for visuelt uttrykk»)
- Vurderes: konsistent bruk av farger, typografi, avstand og komponenter; tydelig navigasjon og informasjonsarkitektur; klare tilbakemeldinger, feilmeldinger og tomtilstander; grunnleggende tilgjengelighet (kontrast, tastaturnavigasjon, alternativ tekst, skjemafeltetiketter); relevante skjermstørrelser; spor etter designarbeid (skisser, wireframes, UX-spesifikasjoner). (LK, samme seksjon)
- Briefens krav om mobil og PC gir et godt designfokus. (TB, kriterium 4) Spørsmålet om hvilke opplysninger som skal være synlige med én gang på mobil er et brainstorming-tema. (PF «Brainstorming-temaer»)

### 6.6 Tester og kvalitetssikring

- Meningsfulle automatiserte tester og relevante manuelle kontroller. (LK «Vurdering og dokumentasjon av KI-bruk»)
- Regler og forventede statuser gir et svært godt grunnlag for automatiske tester. (TB, kriterium 3)
- Ingen forslag som vises som godkjent skal bryte regelsettet. (TB «Det som er bra» nr. 1)
- Sikkerhet: validering, sikkerhetstiltak og kontroll av at hemmeligheter ikke ligger i repoet. (LK, samme seksjon)

### 6.7 README og kjørbarhet

- Prosjektspesifikk, oppdatert README: kort målgruppe- og funksjonsbeskrivelse, gjerne skjermbilde, forutsetninger med versjoner, kopierbare installasjons- og oppstartskommandoer, nødvendige miljøvariabler og `.env.example`, testdata/testbrukere, testkommandoer, mappeoversikt og lenker til planleggings- og prosessdokumenter. (LK «Vurdering og dokumentasjon av KI-bruk»)
- Appen må kunne kjøres lokalt uten betalte kontoer, uten gruppens nøkler og uten egen infrastruktur. (TB, kriterium 6; tabell «Kjørbar for sensor»)
- Ryddig repo uten hemmeligheter, unødvendige byggfiler eller store artefakter. Gjeldende planleggingsdokumenter bør samles ett sted. (LK, samme seksjon; TB, kriterium 7)

### 6.8 Åpne avklaringer (leveranse)

1. Innleveringsfrist for prosjektkode og refleksjonsrapport, og hvor rapporten leveres. (LK «Åpne avklaringer» nr. 1)
2. Om «delvurdering 3» er foreldet tekst eller en ekstra del med krav til individuelle bidrag. Canvas-emneforsiden og den formelle emnesiden er motstridende. (LK «Kort status», «Åpne avklaringer» nr. 2)
3. Om faglærers «gå videre» er den formelle registreringen av godkjent product brief. (LK «Åpne avklaringer» nr. 3)
4. Om BMAD-beskjeden hører sammen med «delvurdering 3» eller den formelle vurderingsfordelingen. (LK «BMAD og arbeidslogg», siste avsnitt i første del)
- Odin følger opp punkt 1–3 skriftlig med faglærer; SCRUM-49 forblir `To Do` til svar er registrert. (LK «Neste handling»)
- Direkte brukerundersøkelse (SCRUM-50) og brukertest (SCRUM-45) er fortsatt valgfrie. Kunngjøringen gjør dem ikke obligatoriske. (PF «Videre arbeid før undervisningen»)

---

## 7. Rapportens åpne spørsmål og forslag til research topics/brainstorming

### 7.1 Rapportens spørsmål til diskusjon

Alle fra R «Spørsmål til diskusjon», står fortsatt åpne (R, siste avsnitt):

1. Hvilken type skiftleder skal det første scenarioet være troverdig for? Helsetjenestefunn gjør ikke helsetjenesten til valgt målgruppe.
2. Hva trenger lederen å forstå når to kandidater begge oppfyller reglene, men konsekvensene er ulike?
3. Hvilke opplysninger kan være utdaterte eller mangle, og hvordan ser lederen hvilken vurdering det hindrer?
4. Kan vi vise en situasjon der KI-teksten hjelper mer enn standardteksten, uten å legge til udokumenterte fakta?
5. Hvilke antakelser er tydelige nok for en studieprototype, og hvilke ønsker vi å undersøke med en målbruker?

### 7.2 Rapportens forslag å vurdere (Codex, ikke krav)

| Forslag | Bruk | Henvisning |
|---|---|---|
| Konkretiser én målbruker og én fraværshendelse | Brief: problem/målgruppe. PRD: scenario og antakelser. | R «Forslag å vurdere» rad 1 |
| La demoen vise både kandidatens grunnlag og følger for andre vakter | PRD: tydeliggjør eksisterende sammenligning og konsekvensvisning | R rad 2 |
| Beskriv alternativer uten udokumentert unikhetspåstand | Brief: alternativer/differensiering. Ingen produktbrief endres i denne runden. | R rad 3 |
| Formuler hva KI-teksten skal gjøre bedre enn standardteksten | PRD: KI-oppgave og evalueringsforslag; SCRUM-59 når oppgaven er konkret | R rad 4 |

Skille som rapporten foreslår for problemformulering: få tilstrekkelig oversikt til å vurdere erstatningsalternativer, og skille mellom at en person er ledig, har riktig kompetanse, oppfyller de kontrollerte reglene og faktisk har takket ja. De siste detaljene er designspørsmål. (R «Brukerbehov», KI-vurdering)

Motvekter å huske: programvare skaper ikke tilgjengelig kompetanse; flytting kan bare forskyve problemet; mer krevende kontroll kan oppleves mindre brukervennlig. (R «Hva sporene betyr sammen»)

### 7.3 Foreslåtte research topics (fra kildene, ikke vedtatt)

- Målbrukerkartlegging: be en målbruker vise hvordan nødvendig kompetanse bestemmes for én vakt; kartlegg en fraværshendelse fra melding til avklart dekning (søk, kontakter, venting, endringer); datadekning på tvers av enheter og hvordan ukjent informasjon vises; om brukeren forstår et avslag og ser følgene for senere vakter. (D-brukere «KI-forslag til PRD-arbeidet» nr. 1–4)
- Fulltekst av den finske studien før effektstørrelser eller konkrete systemfunksjoner brukes. (D-brukere «Kunnskapshull»; R, siste avsnitt)
- Norsk arbeidsflytstudie ved akutt fravær (mangler). Fafo/KS-rapport 2025 om vikarreduserende tiltak er bare et søketreff, ikke lest. (D-brukere «Kunnskapshull»)
- Nyere, oppgavespesifikk forskning på KI-forklaringer og direkte effekt på målgruppen. Hvilket informasjonsbehov en standardtekst ikke dekker. (D-ki «Gjenstår»; R, siste avsnitt)
- Leverandørdemoer og dypere dokumentasjon, se punkt 3.3. (D-konk «Samlet vurdering»)
- Egne målgruppeintervjuer. Ingen av de mulige videre undersøkelsene er gjennomført eller gjort obligatoriske. (R, siste avsnitt)
- Kontroll av udaterte leverandørsider før bruk i konkurransepåstander; neste beregnbare kontroll 2026-11-18. (R «Når bør funnene sjekkes igjen?»)

### 7.4 Foreslåtte brainstorming-temaer (PF)

Spørsmål, ikke vedtatte funksjoner (PF «Brainstorming-temaer»):

- Hva må lederen forstå for å velge mellom to gyldige alternativer?
- Hvordan skiller vi «ingen funn innenfor søkegrensen» fra manglende opplysninger?
- Hvilken historisk kontekst hjelper i beslutningen uten å gi en skjult rangering?
- Hvilken merverdi kan KI-forklaringen gi, og når er standardforklaringen nok?
- Hvilke opplysninger og konsekvenser bør være synlige med én gang på mobil?

### 7.5 Kilde- og kvalitetsforbehold å ta med videre

- Kunngjøringen fra Istvan Hadhazi (2026-10-26 kl. 20.27) er gjengitt i prosjektsamtalen, ikke kontrollert på nytt i Canvas, og har ingen direkte lenke. (PF «Kursbeskjeden»; LK «Forberedelse til PRD»)
- Beslutninger om hvilke research-funn som tas inn i brief/PRD, skal skje etter diskusjon av rapportens åpne spørsmål. (PF «Videre arbeid før undervisningen»)
- Researchrapporten er lokal og var ved utarbeidelsen verken committet eller pushet. (R «Kontroll og status»)
