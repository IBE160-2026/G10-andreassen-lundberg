# Kildeavstemming og avklaringsgrunnlag – SCRUM-47

Skrevet av Codex 08.11.2026. Kildene nedenfor er lest på gjeldende arbeidsgren.
Odin ga i prosjektsamtalen samme dag mandat til å avklare detaljene selv og
gjøre mest mulig videre arbeid. Forslagene her er Codex sine konkretiseringer
på dette mandatet; de er ikke nye felles detaljbeslutninger eller brukertestfunn.

## Kilder og status

- [Produktbrief](../../../../../productbrief.md), oppdatert 30.10.2026: gjeldende utkast og omfang.
- [PRD](../../../prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md), oppdatert 31.10.2026: nummererte krav; `final` angir avsluttet planleggingsrunde.
- [Demoscenario](../../../../../docs/demoscenario-fravaer.md), oppdatert 30.10.2026: R1–R5, P1/P2 og S/H/F/D/M-tilfeller.
- [Forslag ved frafall](../../../../../docs/forslag-ved-frafall.md): søk, låser og separate resultatdimensjoner.
- [Kostnadsanslag](../../../../../docs/kostnadsanslag.md): syntetisk beregning, mangler og O1–O5.
- [UX-memlog](../.memlog.md): senere rettelse til kalenderdager overstyrer tidligere vakttelling.
- Tidligere [kravuttrekk](source-requirements.md), [scenariouttrekk](source-scenarios.md) og [flytskisse](flow-fravaer-v1.md) er arbeidsgrunnlag, underordnet kildene og senere avklaringer.

## Eksakte brukerreisenavn

Kari er en konstruert eksempelperson fra PRD, ikke en intervjuet bruker.

1. **UJ-1. Kari finner en erstatter før vakten starter.** Mobil, A01, onsdag 14.10.2026 kl. 07.00, målskift 08.00–16.00. Registrer fravær, søk, undersøk/ranger, velg og eventuelt simuler tilbud. Kanttilfelle: A05 har åtte timers hvile før vakten og kan ikke velges som bestått.
2. **UJ-2. Ingen direkte erstatter, men én flytting løser det.** Bytt søkegrense fra 0 til 1; B dekker X og C dekker Y. Kanttilfelle: Y blir udekket; alternativet er ikke komplett.
3. **UJ-3. En mulig kandidat mangler opplysninger.** V01 mangler tilgjengelighet. Last komplettert forhåndslaget datasett, vis endring og ny kontroll; gamle svar videreføres ikke som aksept.
4. **UJ-4. Sensor kjører appen.** Lokal oppstart uten konto/nøkkel, gjennomfør UJ-1/UJ-2, ugyldig input og tester etter README. Oppstartsbeskrivelsen eies av README, ikke UX-dokumentene.

Hver reise må ende i en synlig avklaring: mulig valg med kontrollert grunnlag,
synlig udekket behov eller konkret datamangel. Ingen reise ender i en
vaktendring utført av VaktMatch.

## Krav som trenger en UX-flate

| Krav | Hva må leveres i grensesnittet |
|---|---|
| FR-1/2 | Arbeidsuke, ansatte, vakter, behov og dataversjon; udekket behov uten detaljåpning. Innlasting kan feile uten å fjerne forståelig kontekst. |
| FR-3 | Ansatt og ett målskift i uke 5, eksplisitt fraværssimulering, senere fravær på gjeldende grunnlag. Ingen ansatt, feil uke og påbegynt skift gir norsk forklaring. |
| FR-4–7 | R1–R5, verdier, kilder og begrensninger; nødvendig nabovaktgrunnlag i uke 4/6; statusforrang regelavvik før uavklart. |
| FR-8/12 | Fast alternativformat; timer/hvile før og etter, konsekvenser for alle berørte og mangler. Ikke bare hovedkandidaten ved omfordeling. |
| FR-9–11 | Søkegrense 0/1, standard 1; låser/vurderingstidspunkt fra datasett; dekning, kontroll og søkestatus hver for seg. |
| FR-13/14 | Minst ett aktivt P-kriterium, bare P1 som standard; aktivering og rekkefølge; lik rangering; bestått men ikke fullstendig rangerbar kandidat ved manglende sorteringsdata. |
| FR-15 | Undersøk enhver kandidat. Marker komplett, bestått alternativ som øktvalg uten automatisk planendring. Historisk valg etter versjonsbytte. |
| FR-16 | Relevant uke 1–4-historikk med periode, kilde og mangler; ingen historisk poengsum. |
| FR-17–19 | Standardforklaring alltid; «Forklar forskjellen» om undersøkt mot øverste alternativ; fire faste tekstfelt; modellfeil/ingen nøkkel faller tilbake uten å endre valg eller rangering. |
| FR-20 | Separat tilbudssimulering, sendt/venter/akseptert/avslått per berørt; full aksept først når alle berørte aksepterer. Ingen faktisk utsending. |
| FR-21 | Begrenset sett forhåndslagde oppdateringer, endringsoversikt og ny kontroll; gammel versjon/valg/svar forståelig atskilt. |
| FR-24 | NOK-anslag, referanse og differanse, dataversjon, timer, syntetiske satser/tillegg og utelatte kostnader; uavklart ved mangler. |
| FR-22/23 (Bør) | Lederstyrt låsing og varig logg inngår ikke i førsteversjonens handlingsflate. Datasettets låser og øktbevaring er fortsatt Må. |

## Regler, rangering og tall som må bevares

- **R1:** kompetanse K1. **R2:** bekreftet tilgjengelig gjennom hele vakten; ledig kalender er ikke bekreftelse. **R3:** ingen overlapp; slutt lik start er ikke overlapp.
- **R4:** minst 11 timer på begge sider. **R5:** høyst 40 planlagte timer i scenarioets faste sjudagersperiode. Lik grense består. R4/R5 er forenklede scenarioregler med lovutgangspunkt, ikke full lovkontroll.
- **Kontroll:** «Oppfyller scenarioreglene» bare med alle fem bekreftet; minst ett kjent brudd gir «Regelavvik» også ved andre mangler; ellers nødvendig datamangel gir «Uavklart». Kjent kollisjon kan ha hvile «Ikke vurdert», ikke «Ukjent».
- **P1:** færrest planlagte timer etter hele forslaget. **P2:** lavest andel av kjent, positivt avtalt timetall i samme periode. Ved omfordeling gjelder P1/P2 kandidaten på målskiftet; øvrige konsekvenser vises separat.
- Bare komplette, beståtte alternativer rangeres som løsninger. Manglende sorteringsdata påvirker ikke regelstatus; vis kandidaten utenfor fullstendig rangering og ikke bytt skjult til P1.
- Likhet på alle aktive kriterier vises som lik rangering. ID er bare stabil visningsrekkefølge. Ingen bonus for intern kandidat, færre flyttinger, historikk eller lavere kostnad.
- S1: A02 24 → 32 timer, 16 t hvile før/etter; A03 32 → 40 timer, 12/16 t hvile. P1 gir A02 først. P2 gir A03 først: 40/40 = 100 %, mot A02 32/24 = 133,3 %.
- A04 mangler K1; A05 har 8 t hvile før; A06 har 4 t etter; A07 har 4 t overlapp; A08 får 48 timer; V01 mangler bare tilgjengelighet i hovedtabellen.
- Hovedtabellen gir ikke kostnad eller komplett historikk. Ikke tildel O1s 1 800 NOK til A02/A03 som om kilden gjorde det. Nye mockdata må merkes konstruerte, med eget beregningsgrunnlag og uten å hevde ferdig demodatasett.

## Separate dimensjoner i resultatet

| Dimensjon | Tilstander og presis betydning |
|---|---|
| Gjeldende bemanning | Målskiftet er fortsatt udekket selv om komplette forslag finnes eller har simulert aksept. Først oppdaterte kildedata kan vise endret bemanning. |
| Forslagets dekning | Full, delvis/udekket; vis alle berørte udekkede plasser. X dekket og Y udekket er ikke komplett. Andre eksisterende hull er fortsatt synlige. |
| Kontroll | Oppfyller scenarioreglene, regelavvik eller uavklart. Bemannet betyr ikke automatisk bestått kontroll. |
| Søk | Fullført; avbrutt/feilet; ikke kjørt – utenfor omfang. Avbrutte funn/rangering merkes ufullstendige. |
| Rangering | Rangert, lik rangering eller ikke fullstendig rangerbar. Søkeavbrudd kan gjøre rangeringen ufullstendig selv med komplette data for funnet. |
| Øktvalg | Ikke valgt, valgt på gjeldende grunnlag eller historisk valg på gammel dataversjon. Undersøkelse er ikke valg. |
| Tilbudssvar | Aksept ikke simulert, tilbud sendt, venter på svar, akseptert eller avslått. Ingen av disse endrer kontroll eller vaktplan. |

Fullført søk uten beståtte løsninger bruker «Ingen kontrollerte alternativer
funnet innenfor valgt søkeomfang». Uavklarte kandidater og begrensninger er
fortsatt synlige. Et avbrutt søk kan aldri hevde at ingen løsning finnes.

## Forslag til avklaringer på mandatet 08.11.2026

Dette er Codex sin anbefalte detaljering til hovedagenten, ikke ferdig
innarbeidede beslutninger i dokumentparet.

1. **Behold de to eksplisitte handlingene.** Person → startvakt/kalenderperiode → forhåndsvis berørte vakter → «Simuler fravær» for ett valgt målskift → «Finn alternativer». Dette løser avviket mellom den korte flytskissen og PRD UJ-1/FR-3 samt D1. Å endre felt alene endrer ikke aktivt grunnlag eller starter søket.
2. **Periodeoversikten velger ikke alle vakter automatisk.** Standard er én kalenderdag, med startvaktens lokale dato som første dag. Startvakt foreslås fra datasettets vurderingstidspunkt og kan endres. Ett målskift behandles nå; flere kan følges opp ett etter ett. Perioden gir kontekst uten samlet søk eller automatisk massefravær.
3. **Nattvakter forhåndsvises ved tidsmessig overlapp med perioden.** Vis hele start- og sluttdatoen når vakten krysser midnatt, og marker at hele vakten undersøkes. Kalenderperioden går fra første dato kl. 00.00 til dagen etter siste dato kl. 00.00 i Europe/Oslo; den er ikke et fast antall 24-timersblokker. En påbegynt vakt eller vakt utenfor uke 5 vises med begrensningen og kan ikke søkes på. Førsteversjonen deler aldri vakter.
4. **Ikke utled kjent sykefraværsvarighet.** Forklar at dagtallet angir perioden som undersøkes i demoen og kan endres, ikke en prognose eller dokumentasjonsrett. En helt ukjent varighet håndteres ved å undersøke ett konkret kjent målskift nå; ingen automatisk sluttfrist, egenmeldingsmaksimum eller løpende massefravær innføres. En egen «ukjent varighet»-funksjon er ikke nødvendig i Må.
5. **Oversikt først, kandidatdetaljer ved handling.** Oversikten viser identitet, direkte/én flytting, kontroll, foreslått dekning, aktivt rangeringstall, kort timer/hvile, kostnad med differanse/mangler og berørte vakter. Detaljer viser alle R1–R5 med faktiske verdier, før/etter for alle, kildehistorikk og kostnadsgrunnlag. «Undersøk» åpner detaljer; «Velg alternativ» er en egen handling.
6. **Rangering og øvrige funn er egne grupper.** Vis komplette, beståtte løsninger først; beståtte uten komplett sorteringsgrunnlag tydelig separat; deretter uavklarte, avvik og delvis dekning som undersøkbare funn. Alle grupper viser antall og forklaring. Et lavere rangert, men komplett/bestått alternativ kan velges uten automatisk omprioritering.
7. **Stabil desktop- og mobilflyt.** Samme rekkefølge og komponentnavn på begge. Desktop kan ha liste og detaljer ved siden av hverandre; mobil åpner detaljflate med tydelig tilbake til samme liste og bevarer filter, prioritering og rulleposisjon. Ingen nødvendige tall skjules bare fordi skjermen er liten.
8. **Generisk arbeidssituasjon bevares.** Konkretiser Kari som skiftleder ved morgenskiftbytte, med telefon i hånden og tilgang til PC. Dette er en konstruert brukssituasjon i en generell fiktiv arbeidsplass, uten å velge helse, industri eller andre bransjeregler.
9. **Oppdaterte data får egen endringsflate.** Vis gammel/ny versjon, bemanning, mangler, låser, historikk og kostnadsgrunnlag som endres. Deretter ny kontroll før forslag kan brukes. Gammelt valg/svar forblir historisk; ingen aksept arves skjult. Innlasting som feiler lar siste gyldige grunnlag være tydelig merket tilgjengelig.
10. **Tilbud er enkel simulator for gjeldende valgt forslag.** Én handling starter simuleringen; svarhandlinger per berørt person gir ventende, aksept eller avslag. Bare fullstendig, bestått forslag kan presenteres som en kontrollert valgt løsning. Etter avslag beholdes utfallet og et annet alternativ kan undersøkes. Uten tilbudssteg står «aksept ikke simulert».

## Avgrensninger som ikke skal avgjøres gjennom UX

- Ingen automatisk registrering av alle berørte vakter, samlet flerfraværssøk, vaktdeling eller økning av søkegrense til 2.
- Ingen ny kostnadsrangering, rettferdighetspoeng, regelunntak eller «godkjenn avvik»-handling. Å undersøke avvik er påkrevd; et bestått resultat kan ikke skapes av en knapp.
- Ingen ekte meldinger, ansattportal, leverandørintegrasjon, innlogging, produksjonsdrift eller varig logg som Må.
- Modell/leverandør/kostnadsgrense i SCRUM-59, full modellering av ekstern vikars øvrige arbeid i SCRUM-19 og skriftlige leveringskrav i SCRUM-49 forblir egne avklaringer. UX beskriver synlig mangel/fallback og fastsetter ikke svaret.
- Nye eksempeltall og visuelt uttrykk er Codex-valg på mandat; ikke fremstill dem som tidligere kildefunn, observerte arbeidsrutiner eller felles godkjenning.

## Tilgjengelighet og kontrollgrunnlag

NFR-2 krever minst 4,5:1 tekstkontrast, tastatur for alle handlinger, synlig
fokus, etiketter, tekststatus og tom-/feiltilstand med vei videre per visning.
360 px til PC skal fungere uten vannrett rulling. NFR-3 krever norsk
input-/backendfeil og gjenforsøk; NFR-5 krever determinisme og demoens klokke;
NFR-9 krever bokmål. Ingen responstid loves (NFR-7). Modellstatus eller feil
må ikke hindre regelbasert sammenligning (FR-17/19).

UX kan verifiseres med dekning av alle fire UJ-er, S1–S5, H1–H5, F1–F7,
D1–D5/D8, M1–M2 og O1–O5; dette er kilde- og designdekning. Det er ikke
bevis for kjørbar regelmotor, fullstendige demodata eller appens ende-til-ende-test.
