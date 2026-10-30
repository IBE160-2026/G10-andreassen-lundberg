# Utdrag: produktgrunnlag for VaktMatch-PRD

*Utarbeidet 2026-10-28 som kildebelagt arbeidsgrunnlag for PRD. Utdraget er et lesende sammendrag; ingen kildefiler er endret. Der kildene ikke sier noe, står det «ikke angitt i kildene». Kreditering følger kildene: Odin/Stian/Codex er slik kildene oppgir det, ikke vurdert her.*

## Kildenøkkel

| Kode | Fil |
|---|---|
| B | `productbrief.md` (status `draft`, oppdatert 2026-10-26) |
| L | `docs/productbrief-endringslogg.md` (innslag E01–E32 og E34; E33 finnes ikke) |
| D | `docs/demoscenario-fravaer.md` |
| F | `docs/forslag-ved-frafall.md` |
| T | `docs/teknologivalg.md` |
| S14 | `_bmad-output/implementation-artifacts/spec-scrum-14-avklar-scenarioregler-sorteringskriterier-og-standardvalg.md` |
| S15 | `.../spec-scrum-15-sokeomfang-og-fravaershandtering.md` |
| S16h | `.../spec-scrum-16-historikk-som-beslutningsgrunnlag.md` |
| S16s | `.../spec-scrum-16-sok-las-og-resultatstatuser.md` |
| S17 | `.../spec-scrum-17-datatilforing-og-beslutningslogg.md` |

Henvisning «B:26» = productbrief.md, linje 26. Linjenumre er fra lesing 2026-10-28.

---

## 1. Problem og målgruppe

### Slik briefen formulerer det
- **Produkt:** VaktMatch er en planlagt responsiv webapp som gir en skiftleder informasjon og kontekst når en vakt plutselig mangler bemanning (B:20). Grensesnittet skal fungere i nettleser på mobil og PC (B:100).
- **Problem:** En skiftleder får beskjed om fravær kort før vaktstart, må finne tilgjengelig erstatter, kontrollere kompetanse og nabovakter og vurdere om flyttingen skaper nytt bemanningsproblem. Når dette sammenstilles manuelt fra planer, lister og telefonhenvendelser, kan det være vanskelig å få oversikt og forklare valget i ettertid (B:26).
- **Primærbruker:** Skiftleder med bemanningsansvar som trenger forståelig beslutningsgrunnlag under tidspress (B:72). «Vellykket resultat» = lederen kan velge en kandidat og forklare hvorfor vedkommende passer, eller forstå hvorfor vakten fortsatt står udekket (B:72).
- **Beslutningsmyndighet:** Lederen beholder den; KI forklarer muligheter og konsekvenser uten å gjennomføre valget (B:20).
- **Demomiljø:** Generell, fiktiv arbeidsplass uten bransjetilknytning, valgt av Odin 06.10.26 (B:74; L:E13).
- **«Helhetsoversikt»** er avgrenset til å gjøre tilgjengelig, relevant informasjon forståelig, med synlige begrensninger i grunnlaget (B:20; L:E19).
- **Utenfor målgruppen i førsteversjonen:** egne brukerflater for ansatte og forhåndsgodkjente vikarer (B:74).

### Uttrykkelig ikke validert
- Problemet er merket **[ANTAKELSE]**: arbeidsflyten er en problemhypotese; hyppighet og mulig tidsbesparelse er ikke validert med målgruppen (B:28).
- Det er ikke dokumentert at funksjonen er unik i markedet; en tidligere, begrenset konkurrentsjekk er bakgrunnsmateriale med beskrevne usikkerheter (B:68, vedlegg `addendum.md` er lenket, ikke lest her).
- Brukertest og tidsbruk mot manuell oversikt er bare et valgfritt testforslag fra Codex, ikke leveransekrav (B:94; L:E22).
- Faktiske lov- og avtaleregler på en arbeidsplass er ikke avklart; prototypen gir ingen generell garanti om lovlighet (B:48, B:42).
- Eventuelle lovkrav til logging/begrunnelse ved reell bruk er ikke avklart (B:54; D:375–377; L:E22).
- Leverandørtilgang, integrasjonsmuligheter og oppdateringsfrekvens (eksemplet Quinyx) er ikke undersøkt eller lovet (B:118).
- Ansvar for datakvalitet på en virkelig arbeidsplass er ikke avklart; det legges ikke automatisk til mellomlederen (B:50; D:285–286).
- Reell bruk krever eget arbeid med tilgangsstyring, personvern, regelgrunnlag og drift (B:118).
- Ytelse: det er ikke dokumentert at søket er raskt nok; ingen responstid er lovet (B:62; F:77, F:124).

---

## 2. Kjerneflyt og foreslåtte funksjoner

### Kjerneflyt (B:32, B:22; D:26–28)
1. Lederen starter med ansatte, vakter og bemanningsbehov for en ferdig planlagt uke 5; uke 1–4 er historikk (B:32).
2. Demohandling **«Simuler fravær»**: markerer valgt ansatt som utilgjengelig på valgt vakt i uke 5 og viser bemanningsmangelen (B:32; D:295–299).
3. **«Finn alternativer»** åpner sammenligningen (B:32). Alt på én side gjennom en fast handling (B:100).
4. Lederen sammenligner forslag med regelkontroll R1–R5, udekket behov og konsekvenser for berørte ansatte og vakter (B:34).
5. Lederen kan velge/prioritere sorteringskriterier og undersøke også en lavere rangert kandidat (B:40, B:52).
6. Valgfritt: simulere tilbud og aksept for valgt alternativ (B:38).
7. **«Last inn oppdaterte vaktdata»** bytter til et forhåndslaget datasett, viser endringsoversikt og beregner vurderingen på nytt; gjeldende dataversjon skal være synlig (B:32; D:301–326).
8. Forslag og undersøkelser endrer aldri selve vaktene eller historikken (B:34, B:52).

### Foreslåtte/beskrevne funksjoner
- **Forslag ved frafall** i eksisterende plan, basert på tidligere planer som synlig kontekst; erstatter separat plangenerering i MVP (B:34, B:102; L:E31).
- **Fast svarformat:** sammenlignbare alternativer, begrunnelser, regelkontroll, konsekvenser, manglende opplysninger (B:40). Per alternativ: kompetanse, tilgjengelighet, hviletid før/etter, beregnet arbeidstid, konsekvenser for andre vakter (B:40).
- **Søkeomfang** i innstillinger: grense 0 (direkte erstattere) eller 1 (også én intern flytting) (B:36).
- **Lederstyrt sortering:** P1/P2, rekkefølge kan endres, rangering og begrunnelse oppdateres uten å endre planen (B:40, B:44).
- **Kandidater med regelavvik eller uavklart status** kan undersøkes med avvik/usikkerhet synlig; dersom ingen er bekreftet, skal det fremgå (B:40).
- **Tilbuds-/aksept-simulering:** tilbud sendt, venter på svar, akseptert, avslått; for omfordeling vises svar fra alle berørte; full simulert aksept først når alle har akseptert; manglende svar = ventende; enkelt eksempel kan kjøres uten steget («aksept ikke simulert») (B:38; D:103–112).
- **Endringsoversikt** ved datasettbytte; viser også om ingenting er endret eller bemanningen avviker fra undersøkt alternativ (B:52).
- **KI-forklaring** gjennom faste handlinger («Forklar forskjellen», «Vis konsekvensene av dette valget», «Hva mangler?» — handlingsnavn er Codex sine UI-forslag) uten chat (B:50; D:262–265). Uten KI-nøkkel eller ved modellfeil: regelbaserte standardforklaringer (B:50, B:92).
- **Valg og simulerte svar** beholdes i aktiv demoøkt, knyttet til forslag og dataversjon; **valgfri varig beslutningslogg**, avslått som standard, frivillig begrunnelse (B:54; S17).
- **Lås av framtidige tildelinger** (lederlåser) som søkebegrensning (B:60; F:29–31).
- **Synlig vurderingstidspunkt** fra demoen (B:60; F:25–27).
- **Manglende opplysninger** og hvilke vurderinger de hindrer vises (B:50).
- **Ansvarsgrenser** for datatilgang, regelberegning, KI-forklaring og visning, for mulig senere chat (B:114; L:E12).

---

## 3. Besluttede regler og valg

Beslutningsgrunnlag: Odin opplyste 21.10.26 at han og Stian samme dag avtalte at begge kan ta prosjektbeslutninger alene; de konkrete valgene under er tatt av Odin innenfor denne delegeringen og tilskrives ikke Stian som personlige detaljvalg (B:14; L:E28, E29, E31; S14). Delegeringen er gjengitt av Odin (AGENTS.md-regel «Robust bruk av Jira» omtaler den som Odins gjengivelse; ikke lest i detalj her). Briefens status er `draft` (B:2–5).

### 3.1 Scenarioregler R1–R5 — BESLUTTET (Odin 21.10.26, innenfor delegering)
Kilde: D:127–148; B:42; L:E28; S14.

| Regel | Kontroll | Kategori | Merknad |
|---|---|---|---|
| R1 Kompetanse | Kandidaten har K1 | Intern scenarioregel | K1 er kode i konstruert datasett (D:131) |
| R2 Tilgjengelighet | Registrert tilgjengelig hele 08.00–16.00; fravær = utilgjengelig | Intern | Ledig kalender bekrefter ikke tilgjengelighet (D:132) |
| R3 Kollisjon | Ingen overlappende vakt; slutt = start er ikke overlapp | Intern | Gjelder registrerte vakter (D:133) |
| R4 Hvile | Minst 11 t fra forrige vakt til målskift og fra målskift til neste; nøyaktig 11 t består | Forenklet, lovutgangspunkt aml. § 10-8 | Unntak, tariff ikke modellert (D:134) |
| R5 Timetall | Høyst 40 planlagte timer i definert sjudagersperiode; nøyaktig 40 består | Forenklet, lovutgangspunkt aml. § 10-4 | Skift/turnus, gjennomsnitt, overtid ikke modellert (D:135) |

- Alle fem må være bekreftet før «oppfyller scenarioreglene»; kjent brudd = «regelavvik»; ingen kjente brudd men manglende data = «uavklart» (D:141–145; S14).
- Ved kollisjon kan hvile markeres «ikke vurdert»; kollisjon er ikke datamangel (D:146–148).
- Fast periode: mandag 12.10 kl. 00.00–mandag 19.10 kl. 00.00 for P1, P2 og R5; for vakt som krysser grensen teller bare delen i perioden (D:32, D:39–42). 8 timer per vakt, pausefradrag ikke modellert (D:33).
- Komplett historikk som viser at nabovakt ikke finnes = siden består R4; manglende nabovakt pga. ufullstendig historikk = uavklart (D:157–159; S14 triage EC1).

### 3.2 Sortering P1/P2 — BESLUTTET (Odin 21.10.26)
Kilde: B:44, B:46; D:183–223; L:E28.
- **P1** færrest planlagte timer etter tildeling = **standard**; standardkonfigurasjon `[P1]` (D:188).
- **P2** lavest andel av avtalt timetall (planlagte timer etter tildeling / avtalte timer samme periode, stigende) = **valgfritt**; krever kjent, positivt avtalt timetall (D:196, D:210–212).
- Lederen kan aktivere P2, deaktivere kriterier så lenge minst ett gjenstår, og ordne rekkefølge; neste kriterium brukes bare ved likhet (D:188–191).
- Full likhet vises som likeverdig; stabil ID styrer bare visningsrekkefølge, ikke faglig skille (B:44; D:220–223).
- Manglende sorteringsdata endrer ikke regelstatus; kandidaten vises utenfor komplett rangering, systemet bytter ikke stille kriterium (B:44; D:212–218).
- Ved intern omfordeling beregnes P1/P2 for kandidaten som dekker fraværsvakten etter hele omfordelingen; konsekvenser for øvrige berørte vises separat uten samlet poengsum (B:46; D:96–101; L:E29 – Codex-presisering).
- Det finnes ingen vedtatt prioritering av intern foran ekstern eller kostnadsberegning (D:222–223).

### 3.3 Søkegrense — BESLUTTET (Odin, SCRUM-15, 21.10.26)
Kilde: B:36; D:76–90; L:E29; S15.
- Lederstyrt grense **0 eller 1**; **standard og maksimum i førsteversjonen = 1**. Direkte erstattere inngår også ved 1.
- En flytting = allerede tildelt person flyttes til annen vakt mens en erstatter dekker vakten personen forlater. Ny tildeling til ledig person teller ikke som flytting.
- Alle berørte vakter må være dekket og R1–R5 kontrollert på foreslått sluttplan; forslag som flytter mangelen er ikke komplett.
- **To flyttinger** = mulig neste utvidelse etter vurdering av kompleksitet og målt responstid; flere = senere vurdering. **Ikke vedtatt.**
- Innstillingen endrer ikke regelgrunnlaget; resultatet viser søkegrense og konsekvenser (B:36).

### 3.4 Historikk — BESLUTTET (Odin, SCRUM-16, 22.10.26)
Kilde: B:34, B:58; D:47–72; L:E31; S16h.
- Fire uker historikk (relative uke 1–4: 14.09–12.10 i demoen), ferdig planlagt uke 5 (12.–18.10.2026) som arbeidsuke (D:34–37).
- Historikk vises som synlig kontekst; **ingen skjult poengsum**, påvirker ikke P1/P2-sortering (B:34).
- Historikk ligger fast for søk/forslag; en korrigert datakilde lastes som ny dataversjon, endringer vises, berørte kontroller kjøres på nytt (B:58).
- Planlagte vakter dokumenterer ikke faktisk utført arbeid (D:51–53).
- Nabovakter på begge sider av arbeidsuken (også uke 6) følger med for hvilekontroll (B:34; D:38).
- Kontrolltilfeller H1–H5 (D:66–72).

### 3.5 Statuser
- **Regelstatus per kandidat/forslag:** oppfyller scenarioreglene / regelavvik / uavklart (D:141–145; S14). F bruker «Bestått / Regelavvik / Uavklart» (F:93–95).
- **Dekning:** full / delvis (udekket) (F:91–92).
- **Søk:** fullført / avbrutt-feilet / «Ikke kjørt – utenfor omfang» (F:96–98). Avbrutt søk gir aldri «ingen løsning finnes» (F:107–109; B:62).
- **Fullført søk uten bestått:** «Ingen kontrollerte alternativer funnet innenfor valgt søkeomfang»; ingen garanti om umulighet (F:105–107).
- **Tilbud/svar:** tilbud sendt, venter på svar, akseptert, avslått; «aksept ikke simulert» når steget hoppes over (B:38; D:103–108). Ingen status gjennomfører vaktendring.
- Dekning, regelstatus og søkestatus vises hver for seg (B:62).
- Metodens detaljer er Codex sin konkretisering etter Odins samlede tilslutning til anbefalingene i SCRUM-16 (L:E32; F:3–5; S16s) — ikke særskilte valg tilskrevet begge.

### 3.6 Låste vakter og beskyttelse — BESLUTTET som retning; detaljer Codex-konkretisert (E32)
Kilde: B:60; F:29–49; S16s.
- Beskyttet: historikk, gjennomførte/påbegynte vakter, lederlåste tildelinger. Bare framtidige, ulåste tildelinger i uke 5 kan inngå i omfordeling.
- Vakttider, varighet og bemanningskrav endres ikke; vakter deles ikke.
- Lås er søkebegrensning, ikke bekreftelse av regelstatus; knyttes til tildeling og dataversjon; endret lås gjør tidligere resultat utdatert; låser arves ikke skjult til ny dataversjon (F:42–49).
- Fraværet vises som udekket behov; den fraværende teller ikke som bemanning (F:35–40). Påbegynt målskift: «Ikke kjørt – utenfor omfang» (F:39–40, F:98, F:132).
- Søk: direkte erstatning; ved grense 1 B flyttes fra framtidig ulåst Y til X og C dekker Y (F:56–60). Separat konsekvensalternativ der Y blir udekket vises, men rangeres ikke (F:81–85).
- Metode: avgrenset regelbasert søk; **solver ikke i førsteversjonen** (F:111–113; B:62).

### 3.7 Fravær, datatilføring, økt og logg — BESLUTTET (Odin, SCRUM-17: «ser greit ut det ja»)
Kilde: B:32, B:54–56; D:288–356; L:E30; S17.
- «Simuler fravær» virker på gjeldende grunnlag og tilbakestiller ikke tidligere oppdateringer (D:295–296).
- Forhåndslagde datasett (D0/D1/D2 er beskrivelser, ikke laget; D:311–312).
- Valg og simulerte svar beholdes i aktiv demoøkt; **varig beslutningslogg valgfri, avslått som standard**; begrunnelse frivillig (B:54).
- Codex-konkretiseringer (L:E30): økten slutter når fanen lukkes; aktivering gjelder bare nye registreringer; deaktivering stanser nye men sletter ikke gamle; etter datasettbytte beholdes tidligere valg som historikk på gammel dataversjon og fremstår ikke som gjeldende før ny kontroll (B:56; D:340–345, D:323–326).
- Loggen er ikke bevis på gjennomførte vaktendringer (B:54).
- E30 oppgir at Codex tolker Odins svar som tilslutning til det samlede forslaget inkludert valgfri varig logg; «økt alene» ble ikke valgt særskilt (L:E30).

### 3.8 Standardvalg (samlet)
- Søkegrense 1 (B:36); sortering `[P1]` (D:188); varig logg av; begrunnelse frivillig (B:54); tilbudssteg kan hoppes over (B:38); kjerneflyt uten KI-nøkkel (B:50, B:92; T:16); vurderingstidspunkt fra demoen, ikke maskinklokke (F:25–27, F:131).

### 3.9 Teknologi og arbeidsdeling
Kilde: T:8–38; B:110; L:E34.
- **Frontend React** og **backend Python/FastAPI**: valgt av Stian i SCRUM-13 (24.10.26); Odin sluttet seg til utgangspunktet 26.10.26 (T:10–11). Scenarioreglene beregnes i egen kode, ikke i FastAPI som sådan (T:11).
- **Lokal kjøring** i oppstartsfasen: foreslått av Stian, bekreftet av Odin 26.10.26 (T:12).
- **KI-modell/leverandør:** valg utsatt til oppgaver, input og svarformat er konkrete; utsettelsen registrert av Stian (SCRUM-59), støttet av Odin. Regelbaserte standardforklaringer lages først (SCRUM-40). Kostnad, kostnadsgrense og test-/mockmodus avklares i SCRUM-59 (T:13, T:17–19).
- **Hosting/Supabase/RLS:** kan vurderes senere; ingenting valgt (T:14).
- **Arbeidsdeling (justerbar, utgangspunkt):** Odin følger opp UX, grensesnitt, sammenligning, prioritering og KI-/standardforklaringer; Stian følger opp datagrunnlag, regelmotor, søk og teknisk oppsett. Bygger på Stians forslag i SCRUM-13 og Jira-tildelinger, med Odins tilslutning 26.10.26. «Ansvar» = oppfølging, ikke beslutningsmyndighet (T:23–31; B:110).
- **Bare forslag, ikke godkjent:** Vite/TypeScript, JSON-demodata, SQLite, CI, lokalt kodeskjelett — behandles i SCRUM-18 (T:35–38).

---

## 4. MVP-grenser / utenfor omfang

### Inne i førsteversjonen (B:100)
Én fiktiv arbeidsplass, 8–10 ansatte og noen forhåndsgodkjente eksterne vikarer; fiktive data med fire ukers historikk, ferdig planlagt uke 5, kompetanse, tilgjengelighet og nødvendige nabovakter; ett simulert sykefravær i uke 5 gir sammenligning på én side; KI forklarer i fast svarformat; R1–R5; P1/P2 for uke 5; søkegrense 0–1 (standard 1); forhåndslagde datasett med endringsoversikt og ny kontroll; økt-tilstand og valgfri varig logg; mobil og PC.

### Utenfor førsteversjonen (B:104, B:114; B:74)
- AI-chat og friteksttolkning av behov/ønsker; samtalehistorikk og generell agentplattform.
- Full periodeplanlegging med preferanser og helgefordeling.
- Åpen vikarmarkedsplass.
- Reelle persondata; reelle integrasjoner med HR-/turnussystemer; reell leverandørtilkobling.
- Innføring av planforslag og gjennomføring av foreslåtte vaktendringer i faktisk vaktliste.
- Produksjonsdrift.
- Egne brukerflater for ansatte og vikarer (B:74).
- Separat generering av ny ukeplan (tatt ut av MVP; B:34, B:102; D:386–387; L:E31).
- Reell utsending/aksept av tilbud (F:20).
- Solver; to eller flere flyttinger (mulige senere utvidelser; B:36, B:62; F:17–18).
- Modellering av tariffavtaler, overtid, gjennomsnittsberegning, unntak fra arbeidsmiljøloven (D:134–135, B:42).
- Lønn/øvrig behandling av sykefravær (F:65–66).
- Nye sorteringskriterier utover P1/P2 («krever egen avklaring»; F:19). Historikk gir ikke eget rangeringskriterium (B:34, B:58).
- Hosting, innlogging, Supabase/RLS, skylagring (T:14).
- Datasettbytte representerer en oppdatering fra datakilden, ikke en utført lederbeslutning (B:104).
- Kun én fraværshendelse og én manglende bemanningsplass om gangen, én hel vakt per tildeling (F:53–54).
- Kontroll av «alle tenkelige omplanlegginger» påstås ikke (F:72–74; B:81).

### Avgrensning av sammenligningen
- Bare kandidater som oppfyller scenarioreglene rangeres; øvrige kan undersøkes (B:40; S14).
- Det er ikke et mål at VaktMatch gir beslutningen eller gjennomfører den (B:20, B:52).

---

## 5. Suksesskriterier slik de står — og mangler

### Slik de står (B:76–96)
Briefen angir at kriteriene er **«foreslåtte kriterier som skal testes, ikke oppnådde resultater»** (B:78). Sammendrag av de 13 punktene:
1. Ingen kandidat vist som «oppfyller scenarioreglene» bryter regelsettet i testscenarioene; manglende kontrolldata = uavklart (B:80).
2. Udekket behov vises når ingen undersøkte alternativer består; søkeomfang og manglende grunnlag synlig; ingen påstand om at alle omplanlegginger er undersøkt (B:81).
3. Forslag ved frafall i uke 5 vises separat fra gjeldende plan med synlig kontekst fra uke 1–4; historikk og vaktliste endres ikke (B:82).
4. KI-forklaringens opplysninger kan spores til data, regelkontroll og definerte prioriteringer; endrer ikke status eller rangering (B:83).
5. Lederen kan endre prioritering og se rangering med begrunnelse; regelstatus beholdes; manglende sorteringsdata synliggjøres (B:84).
6. Fast format med alternativer/udekket behov, regelkontroll, konsekvenser og manglende opplysninger; ingen kandidat vist som ferdig kontrollert ved manglende data (B:85).
7. Lederen kan undersøke lavere rangert kandidat; KI bytter ikke kandidat eller prioritering (B:86).
8. Grense 0 viser direkte erstattere, standard 1 tillater én flytting; forslag som etterlater annen vakt udekket vises ikke som komplette; flere fungerende alternativer kan sammenlignes (B:87).
9. Tilbud/svar kan simuleres; ventende, avslag og full aksept skilles; ingen status gjennomfører vaktendring (B:88).
10. Ny vurdering bygger på oppdatert datasett; forslag vises ikke som gjennomført bare fordi det er undersøkt (B:89).
11. Fravær kan simuleres; datasettbytte viser dataversjon, endrede/uendrede vakter og mangler; aksept videreføres ikke (B:90).
12. Valg og svar tilgjengelige i aktiv økt; varig logg valgfri/avslått; logging endrer ikke regelstatus eller vaktliste (B:91).
13. Sammenligning, historisk kontekst og vurdering av oppdaterte data fungerer uten KI-nøkkel og ved modellfeil (B:92).

I tillegg: valgfri brukertest (Codex-forslag, ikke krav; B:94) og studiekrav om dokumentasjon av BMAD-bruk, egne valg og kvalitetssikring av KI-generert kode (B:96). Faglærerens råd er referert i B:94 og L (`tilbakemelding-product-brief.md`, ikke lest her); S14 nevner krav om 3–5 tallfestede regler, enkel synlig prioritering og regneeksempel.

### Hva som mangler eller er uklart
- **Ingen tallfestede mål:** ingen mål for responstid, tidsbesparelse, antall testscenarioer, antall brukere/tester eller akseptgrenser. Ytelse: bare målemetode (median, p95, avbrudd/feil, grense 0 mot 1) uten måltall (F:115–124; B:62).
- **Målbarhet:** flere kriterier er formulert kvalitativt («kan spores», «forståelig», «synlig») uten testmetode eller terskel, f.eks. B:83 (sporbarhet), B:66/B:72 (lederen kan «forklare hvorfor»).
- **Brukerverdi er ikke målt:** den eneste verdimåten (forståelse, tidsbruk mot manuell oversikt) er valgfri og ikke et krav (B:94). Ingen brukervalidering av problemet (B:28).
- **Motmål/guardrails:** ikke formulert som egne mål. Det finnes negative begrensninger (ingen vaktendring, ingen rangering uten grunnlag, ingen «ingen løsning»-påstand ved avbrudd, ingen skjult poengsum), men ikke som definerte motmål med måling (f.eks. andel feilaktig «oppfyller»-merking, feil i tidsbruk, kostnad for KI-kall).
- **Ikke dekket av suksesskriteriene:** lederlåser, søkestatusene (avbrutt, «ikke kjørt – utenfor omfang»), vurderingstidspunkt, kontroll av historikkvisning ved ufullstendige data (H2) og tidsbruk/ytelse. Disse er beskrevet i F og D, men ikke som briefens kriterier.
- **Kriteriene er knyttet til «testscenarioene»** (B:80), men komplette datasett og fasit er ikke laget (B:109; D:161–163, D:312).
- **Kostnadsmål for KI** er ikke satt; kostnadsgrense avklares i SCRUM-59 (T:17–19).

---

## 6. Åpne spørsmål og motstrid/uklarheter

### 6.1 Åpne punkter (uttrykkelig åpne i kildene)
1. **Implementering og ytelse:** søkemetode, låser og statuser må implementeres/testes; responstid må måles før tidsmål eller større søkeomfang (B:108).
2. **Demodata:** fullstendige datasett (4 uker historikk, planlagt uke 5, nabovakter, fasit for fravær/oppdateringer) og lagringsteknikk for valgfri logg (B:109). Historikkfelt og presentasjon må spesifiseres (D:59). D0/D1/D2 og F2–F4 er beskrivelser, ikke ferdige datasett (D:124–125, D:311–312).
3. **Avtalte timer/stillingsprosent:** behandling må konkretiseres i datasettet for at P2 skal kunne beregnes (D:384–385).
4. **KI-modell:** valg, kostnad, kostnadsgrense og test-/mockmodus (SCRUM-59; T:13, T:17–19). KI-oppgaver, input og svarformat «mer konkrete» først (B:110).
5. **Teknisk detalj:** Vite/TypeScript, JSON-demodata, SQLite, CI og kodeskjelett (SCRUM-18; T:35–38). Hosting, Supabase/RLS (T:14).
6. **Datakvalitetsansvar og lovkrav ved reell bruk** (B:50, B:54, B:118; D:285–286).
7. **Arbeidsdeling** er et justerbart utgangspunkt (T:29–31).
8. **Utvidelser:** to flyttinger, solver, flere flyttinger (B:36, B:62).
9. **Samordning av E33 og teknologidokumentet:** Stians Jira-kommentar viser til en E33 og en tidligere versjon av `docs/teknologivalg.md` som ikke var tilgjengelig på eksterne grener 26.10.26; innholdet er ikke rekonstruert (L:236–239; T:46–49).

### 6.2 Motstrid / uklarheter mellom dokumentene
1. **Søkegrense i hovedeksempel:** B og F sier standard og maksimum er 1; D bruker grense 0 i hovedeksempel og S1–S5 («Tabellen her viser direkte erstatning»; D:22, D:43–45). Fasit i S1–S5 gjelder derfor direkte erstatning, og forventet resultat med grense 1 (inkl. flyttinger) er bare beskrevet i F-tilfellene (D:114–122) uten komplett vaktsett (D:124–125).
2. **Statusvokabular:** D/S14 bruker «oppfyller scenarioreglene / regelavvik / uavklart»; F bruker «Bestått / Regelavvik / Uavklart». Sammenfallet er ikke uttrykkelig definert.
3. **Rolleord:** B bruker «skiftleder» (B:20, B:72), «leder» og «mellomleder» (B:50); L og D bruker «mellomleder» flere steder (L:E15, E19, E30; D:286). Om dette er samme rolle er ikke definert.
4. **Datasettstørrelse:** B:100 sier «8–10 ansatte og noen forhåndsgodkjente eksterne vikarer»; D:30 har åtte interne (A01–A08) og én vikar (V01). D sier selv at tabellen er håndregnet kontrollgrunnlag, ikke komplett plan (D:161–163).
5. **Timeverdier:** D:161–163 oppgir «timer før → etter» som syntetiske verdier som skal erstattes av summerte vakter; samtidig skal R5 og P1/P2 beregnes fra slike vakter.
6. **Kandidatsett uklart:** F:56 og F:72 refererer til «det oppgitte kandidatsettet», men sammensetningen er ikke definert. Ikke angitt i kildene om vikar kan inngå som flyttet person (B) eller bare som erstatter; D:222 sier ingen intern/ekstern-prioritering er vedtatt.
7. **Eldre tekst i endringsloggen:** avsnittet «Etter avklaringen 22.10.26 gjenstår særlig søkemetode, eventuelle låste tildelinger, … teknologistakk og arbeidsdeling» (L:57–58) er delvis overtatt av E32 og E34. «Hvorfor arbeidsutkastet er endret»-seksjonen (L:20–60) har punkt om at plangenerering beholdes (L:39–42), som E31 erstatter; seksjonen er merket «historisk sammendrag» (L:26–29). Gjeldende retning er E28–E32 og E34. E21 og E24 er historikk (L:125–129).
8. **Metadata i brief:** B:12 oppgir «Innlevering: søndag 20. september 2026», mens `updated` er 2026-10-26 og innholdet viser arbeid etter dette; om datoen er gjeldende, er ikke angitt i kildene.
9. **Delegeringsgrunnlag:** B:14 og L:E28 bygger på Odins gjengivelse av avtalen 21.10.26. Tidligere (07.10.26) ble endringer uttrykkelig ikke ansett avklart med Stian (L:31–33, E25). Kildene inneholder ingen egen registrering fra Stian av delegeringen eller av de konkrete scenario-/søke-/logg-valgene; briefen sier selv at Stian ikke tilskrives detaljvalgene (B:14, B:102).
10. **Økt-begrepet:** «økt slutter når fanen lukkes» er en Codex-konkretisering; E30 sier «økt alene ble ikke valgt særskilt» (L:E30; D:340). Lagringsteknikk for økt vs. varig logg er åpen (B:109; T:35 nevner SQLite som forslag).
11. **Svarformat over tid:** E05 beskrev «anbefaling med begrunnelse, andre alternativer» (L:E05); gjeldende B:40 beskriver «sammenlignbare alternativer» og E16 «ikke et pålagt førstevalg». Gjeldende ordlyd er B:40, men hvorvidt øverste rangerte vises som «anbefaling» er ikke uttrykkelig avklart.
12. **Hvilepunkter ved hvilekontroll av fraværende:** D:178 sier A01 «oppfyller ikke R2»; F:63–66 sier fraværsvakten beholdes som kildehistorikk, men teller ikke i dekning/arbeidstid. Dette er forenlig, men to ulike steder styrer det.
13. **Vurderingstidspunkt:** F:25–27 sier «kan være 14.10.2026 kl. 07.00»; hvordan tidspunktet settes/vises i grensesnittet er ikke spesifisert.
14. **Spec-/verktøynotat:** S14 refererer til en `memlog.py check`-kommando som ikke finnes (S14 triage BH2); gjelder prosess, ikke produktkrav.
15. **Status for SCRUM-16:** L:E31 sier «SCRUM-16 beholdes In Progress»; S16h og S16s har `status: done`. Ikke motstrid (ulike tidspunkt), men PRD bør bruke status per dato.
16. **Brukeromfang for lås:** F:29–31 sier «Lederen kan i tillegg låse framtidige tildelinger»; B:60 omtaler «lederlåste tildelinger». Selve grensesnittshandlingen for å låse er ikke beskrevet som funksjon i B:32 og ikke dekket av suksesskriteriene.
