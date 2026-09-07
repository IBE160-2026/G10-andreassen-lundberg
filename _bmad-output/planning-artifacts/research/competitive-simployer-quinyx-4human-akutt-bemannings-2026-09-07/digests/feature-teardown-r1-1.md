# Digest: Simployer — akutt fraværshåndtering / shift-gap coverage

Round 1, assistant 1 of 2. Company: Simployer (inkl. Capitech Tid & Plan).

## Answer

**Nei — ikke funnet belegg for at Simployer i dag gir rangerte/forklarte alternativer (intern flytting / overtid / ekstern vikar) med kompetanse-, hviletid- og overtidssjekk ved et sykefravær.** Confidence: medium-high.

Simployers fraværs-/bemanningsmoduler (Simployer HRM + Capitech Tid og Plan) dekker: registrering/godkjenning av fravær, varsling til leder, oversikt over hvem som er borte, integrasjon mot vaktplan, og en "Finn vikar"-funksjon for å finne og tildele erstatning — samt automatisk overtids-/lønnsberegning på faktisk arbeidet tid. Ingen kilde beskriver et sett rangerte alternativer med forklaring av kompetansematch, hviletidsoverholdelse eller beregnet overtidskonsekvens *før* lederen velger.

## Funn

- OAS (Oppfølging av Sykefravær)-modulen gir lederdashboard, frist-/oppgaveoversikt og lovpålagt oppfølgingstidslinje — ingen omtale av forslag til skiftdekning. — Simployer, "Oppfølging av Sykefravær (OAS) i Simployer", https://support.simployer.com/dokumentasjon/simployer-tid-og-bemanning-brukerveiledninger/flow-tid/admin/oppfolging-av-sykefravaer-oas-i-simployer/, 2026-09-07
- Absence & Time Tracking-produktsiden beskriver søknad/godkjenning, kalender/liste/Gantt-visninger, egendefinerte permisjonsregler og varsling ved lange fraværstrender — ingen rangering, kompetansematch eller hviletidssjekk beskrevet. — Simployer, "HRM | Absence & Time Tracking", https://www.simployer.com/products/hrm/absence-time-tracking, 2026-09-07
- Capitech "Tid og Plan" beskrives som "helintegrert med plan for fravær... og håndtering av vikarbehov" med "rask oversikt ved fravær og enkel håndtering av midlertidig personell" — arbeidsflyt-/oversiktsspråk, ikke rangerte/forklarte alternativer. — Capitech (Simployer), "Tid og Fravær", https://www.capitech.no/produkter/tid-og-fravar, 2026-09-07
- Samme side: "Beregner automatisk fleksitid, overtid, tillegg" — beskriver lønns-/timeregistreringsberegning på faktisk arbeidet tid, ikke en prediktiv "hvis vi velger dette alternativet blir overtiden X"-sammenligning på tvers av kandidater. — Capitech (Simployer), "Tid og Fravær", https://www.capitech.no/produkter/tid-og-fravar, 2026-09-07
- "Finn vikar"-funksjon bekreftet å eksistere (nevnt i versjonsnotater for en visningsrettelse av beregnede timer) — men selve dokumentasjonssiden for funksjonens beslutningslogikk (rangering, regelsjekk) kunne ikke hentes (502-feil). — Simployer, "Simployer Capitech Tid & Plan - Versjon 15.19", https://support.simployer.com/dokumentasjon/simployer-tid-og-bemanning-brukerveiledninger/versjonsinfo/15-19/, 2026-09-07
- Simployer publiserer generelle rådgivningsartikler om norske arbeidstidsregler (11-timers hviletid, overtidsgrenser) som kunnskapshub-innhold for HR-publikum — pedagogisk/compliance-innhold, ikke en beskrivelse av en automatisert regelmotor koblet til skiftbeslutninger. — Simployer, "Ja, arbeidsgiver kan planlegge med overtid", https://www.simployer.com/no/artikler/arbeidsgiver-kan-planlegge-med-overtid, 2026-09-07
- G2-anmeldelser vektlegger compliance/policy-støtte, HR-dokumentstruktur og ansatt-selvbetjening; ingen anmeldelser fant spesifikt skiftdeknings-beslutningsstøtte. — G2, "Simployer Reviews 2026", https://www.g2.com/products/simployer/reviews, 2026-09-07

## Motsigelser
Ingen — alle kilder er samstemte om at fraværshåndtering er registrering/varsling/oversikt/manuell "finn og tildel"-arbeidsflyt.

## Hull (ikke funnet)
- "Finn vikar"-dokumentasjonen selv kunne ikke hentes (502, ingen cache funnet) — nærmeste kandidatfunksjon forblir kun indirekte karakterisert.
- Ingen brukeranmeldelser som spesifikt omtaler erstatnings-/skiftdekningsopplevelsen i egne ord.
- Ingen endringslogg-oppføringer om nye AI-/regelbaserte anbefalingsfunksjoner for skiftdekning (kun en mindre visningsrettelse).
- Kan ikke bekrefte eller avkrefte om "Finn vikar" filtrerer/sorterer kandidater på kompetanse eller hviletid internt — åpent spørsmål, ikke et negativt funn.

## Leads
- "Finn vikar" (Capitech Tid & Plan) — prøv support.simployer.com på nytt, eller Atlassian-wiki (simployer.atlassian.net/wiki/spaces/CTS/).
- Simployer HRConnect API (fraværs-endepunkter fra sept. 2024) — kan indikere om tredjeparter bygger rangeringslogikk på toppen av Simployer-data.
- Video-/demomateriale for "Finn vikar"-arbeidsflyten kunne avgjort spørsmålet visuelt.
