# Konkurrentfordypning – runde 1, del 1

Skrevet av Codex, 2026-10-26. Avgrensning: offentlig dokumentasjon om erstatning ved fravær, kvalifikasjoner/regler, rangering og forklaringer hos Simployer/Capitech, Quinyx og 4human. Fem underliggende kildesider er åpnet og relevante avsnitt lest. Dette er leverandørers egenbeskrivelser, ikke produkttest eller uavhengig effektmåling.

## Forskningsregler og kildegrense

1. Never conclude from training data alone. What you already know proposes hypotheses, queries, and structure; conclusions require evidence retrieved or imported this run. A claim you cannot evidence is stated as an unverified belief or not at all.
2. The research firewall. Project context — briefs, PRDs, code, memory, persistent facts — shapes what to ask, never what is true. It is inadmissible as evidence: every claim in a research artifact traces to a digest or import file with a source. Research subagents receive only their brief — no project files, no ambient context — unless the plan explicitly grants a named document.

Tillatt eldre dokument: `competitive-simployer-quinyx-4human-akutt-bemannings-2026-09-07/research.md`, lest utelukkende som spørsmålsgrunnlag. Ingen tidligere produktpåstander er importert som bevis. Publiseringsdato og tilgangsdato holdes atskilt; nylig søkemotorinnhenting beviser ikke nylig publisering.

## Kilder og påstander

### C1 – Simployer/Capitech: erstatningsflyt ved fravær

- **Kilde:** [Jobbe med vakter i operativ plan](https://help.capitech.no/nb/article/673d4f65-294e-4331-a061-1af71d63ebee)
- **Publisher:** Capitech hjelpesenter / Simployer Capitech.
- **pub_date:** Ukjent; ingen publiserings- eller oppdateringsdato synlig i lest side.
- **accessed:** 2026-10-26.
- **class:** features; leverandørens brukerdokumentasjon, ikke testet.
- **confidence:** Høy for hva siden beskriver; faktisk funksjon og konfigurasjon ikke verifisert.
- **Påstand/støtte:** «Finn vikar» søker tilgjengelige ansatte for en vakt, uttrykkelig også ved sykdom og fravær. «Meld behov for vikar» publiserer behov i MinCapitech, der ansatte kan melde interesse. Støttende avsnitt: «Finn vikar» og «Meld behov for vikar».
- **Støtter ikke:** Teksten spesifiserer ikke tilgjengelighetsalgoritmen, kompetanse-/hviletidsfilter, kandidatrangering eller begrunnelser per kandidat. Dette er dokumentasjonshull, ikke påvist manglende funksjonalitet.
- **Nytt mot gammelt hull:** Offentlig hjelpetekst om funksjonen er nå tilgjengelig; det tidligere tilgangshullet er delvis lukket, mens beslutningslogikken fortsatt er uavklart.

### C2 – Simployer/Capitech: kostnad for alternative vikarer

- **Kilde:** [Satser for kostnadsberegning](https://help.capitech.no/nb/article/satser-for-kostnadsberegning-forelopig-under-redigering)
- **Publisher:** Capitech hjelpesenter / Simployer Capitech.
- **pub_date:** Ukjent. URL-en inneholder «forelopig-under-redigering»; siden oppgir ikke synlig status/dato som avklarer dette.
- **accessed:** 2026-10-26.
- **class:** features; leverandørens brukerdokumentasjon, ikke testet.
- **confidence:** Høy for dokumentert visning, middels for bruk som påstand om gjeldende produktversjon fordi dato/status er uavklart.
- **Påstand/støtte:** Avsnittet «Finn vikar» sier at beregnet kostnad vises for ulike tilgjengelige vikarer, slik at kostnaden ved forskjellige erstattere kan vurderes. Satser knyttes til lønnsarter, blant annet overtid og tillegg; satsene brukes til kostnadsberegning, ikke lønnseksport.
- **Støtter ikke:** Siden dokumenterer ikke at kandidatene rangeres etter kostnad, eller at en forklart optimaliseringsmodell sammenligner intern omfordeling, overtid og ekstern innleie.
- **Nytt mot gammelt hull:** Konkret sammenligningsgrunnlag før valg er nå dokumentert. En generell omtale av Capitech som bare registrering og manuell søking blir derfor for grov.

### C3 – Quinyx: kompetansesortering og forklarte varsler

- **Kilde:** [Skills](https://help.quinyx.com/help-centre/docs/skills)
- **Publisher:** Quinyx Help Centre.
- **pub_date:** 2026-07-29; oppdatert 2026-08-18, ifølge selve siden. Innen tre måneder ved tilgang.
- **accessed:** 2026-10-26.
- **class:** features; leverandørens brukerdokumentasjon, ikke testet.
- **confidence:** Høy for dokumentasjonsinnhold; ingen uavhengig produktverifikasjon.
- **Påstand/støtte:** «Skills in Schedule view» beskriver filtrering/sortering etter nødvendige ferdigheter, antall samsvarende ferdigheter og navn ved pekerføring. «Warnings» beskriver varsler som navngir manglende ferdighet; lederen kan likevel velge å tildele vakten. Et omtalt unntak ved ubehandlede varsler under utrulling av grunnplan viser en eldre, generell varseltekst.
- **Støtter ikke:** Kompetansesortering er ikke dokumentasjon av samlet rangering etter alle regler, kostnad og konsekvenser. Denne siden knytter heller ikke hele visningen uttrykkelig til akutt fravær.
- **Nytt mot gammelt hull:** Quinyx har dokumentert forklaringsinformasjon og kvalifikasjonsstøtte. En generell påstand om fravær av forklart beslutningsstøtte kan ikke videreføres.

### C4 – Quinyx: automatisk ny beregning ved akutte endringer

- **Kilde:** [Workforce Optimization / Scheduling Automation](https://www.quinyx.com/workforce-management/scheduling-automation)
- **Publisher:** Quinyx.
- **pub_date:** Ukjent; ingen publiserings-/oppdateringsdato synlig. Copyright 2026 brukes ikke som publiseringsdato.
- **accessed:** 2026-10-26.
- **class:** features; leverandørmarkedsføring, ikke testet.
- **confidence:** Høy for at leverandøren fremsetter påstanden, middels for produktkapabiliteten uten demonstrasjon eller teknisk dokumentasjon av denne flyten.
- **Påstand/støtte:** FAQ-en hevder at Automation ved endringer i siste liten beregner dekningen på nytt under reglene. Den nevner fravær og vaktbytte, og vurdering av tilgjengelighet, ferdigheter, kvalifikasjoner, preferanser og arbeidsbelastning per vakt. Leder kan overstyre automatiske planer.
- **Støtter ikke:** Ikke dokumentasjon av nøyaktig regeloppsett, full norsk regelverksdekning, algoritmens korrekthet eller presentasjon av flere forklarte handlingsalternativer.
- **Nytt mot gammelt hull:** Den tidligere uverifiserte retningen om intelligent omfordeling har nå direkte støtte som leverandørpåstand. Markedsføringens presisjon og faktisk brukeropplevelse gjenstår å kontrollere.

### C5 – 4human: arbeidsplan og fraværsvarsling

- **Kilde:** [Arbeidsplan](https://4human.no/hrm/arbeidsplan/)
- **Publisher:** 4human HRM.
- **pub_date:** Ukjent; ingen publiserings-/oppdateringsdato synlig i lest side.
- **accessed:** 2026-10-26.
- **class:** features; leverandørens produktbeskrivelse, ikke testet.
- **confidence:** Høy for dokumentert innhold; lav dekning av spørsmålet om kandidatvalg.
- **Påstand/støtte:** «Detaljert plan» beskriver løpende endringer i faktiske arbeidsplaner. «Digital arbeidsplan» beskriver varsler ved fravær sammen med time-/fraværsmodulen. Ledere kan justere planer og ansatte se dem på mobil.
- **Støtter ikke:** Den undersøkte siden avklarer ikke hvem som foreslås som erstatter, kandidatregler, rangering eller forklaring. Omtale av kompetanse i generelle planleggingsråd dokumenterer ikke en automatisk kandidatsjekk.
- **Nytt mot gammelt hull:** Ingen løsning av det konkrete detaljhullet. Det gir ikke grunnlag for å si at 4human mangler slike funksjoner eller at andre produkter er unike.

## Samlet vurdering og gjenstående hull

**KI-vurdering basert på C1–C5:** Konkurransegrunnlaget bør beskrive dokumenterte delkapabiliteter presist. Det er ikke grunnlag her for en unikhets- eller differensieringspåstand. Kostnadsvurdering mellom vikarer og synlig kompetansegrunnlag finnes i leverandørenes dokumentasjon. Samlet forklaring av flere tiltakstyper er ikke verifisert i denne avgrensede runden. «Ikke verifisert» betyr ikke «finnes ikke».

Videre spor dersom mer undersøkelse autoriseres:

- Simployer/Capitech: verifiser i demonstrasjon eller mer detaljert hjelp hvilke AML- og kompetansevarsler som gjelder inne i «Finn vikar», og hvilken sortering som brukes. C1/C2 viser navigasjonslenker til AML-varsler, men disse sidene er ikke lest.
- Quinyx: undersøk den konkrete omfordelingsflyten og Auto Assign-dokumentasjonen for rangering, overstyringer og årsaksforklaringer. Søket fant hjelpesidene «Absence handling» og «Auto Schedule and Auto Assign Warnings»; de er bare søkespor, ikke brukt som bevis her.
- 4human: be om relevant brukerdokumentasjon eller en demonstrasjon med akutt sykefravær og to mulige erstattere. Den ene leste produktsiden gir utilstrekkelig detaljdekning.
- Datering: C1, C2, C4 og C5 mangler publiseringsdato. Ingen av dem kan merkes som nylig publisert alene fordi de ble åpnet nå.

**Omfang/stopp:** Én undersøkelsesrunde, 7 webverktøykall, 5 distinkte underliggende kildesider lest og brukt. Søkeresultater uten åpnet side er bare brukt til navigasjon/spor. Ingen produkttest, uavhengig bekreftelse eller full markedsdekning. Stopp ved avtalt kilderamme; åpne spørsmål er bevart.

**Bærende påstander:** (1) Capitech dokumenterer beregnet kostnad for ulike tilgjengelige vikarer i «Finn vikar» (C2). (2) Quinyx dokumenterer kompetansesortering og varsler som angir manglende ferdighet (C3). Disse er konkrete egenbeskrivelser som snevrer inn hva en senere konkurransepåstand forsvarlig kan si.
