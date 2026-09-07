# Addendum: PantBuddy

## KI-funksjon: «Oppsummer min innsats»
*Utviklet av Odin med Codex, parallelt — 2026-09-07*

Erstatter den tidligere fritekst-til-annonse-antakelsen i brief.md. Samme «kode beregner, KI formulerer»-arbeidsdeling som i VaktMatch.

**Testbarhet for IBE160** (konkret nok til å bygges og evalueres som kursets KI-krav):
- Er oppsummeringen korrekt, relevant og motiverende?
- Blander den aldri giverens og innsamlerens bidrag?
- Dobbeltteller den aldri penger (f.eks. samme beløp i både personlig og lag-oppsummering uten at det er tydelig at det er samme bidrag)?
- Hevder den aldri større miljøeffekt enn datagrunnlaget faktisk støtter?

**Datagrunnlag i MVP (oppdatert 2026-09-07):** giverens selvrapporterte anslag ved annonseopprettelse, ikke en obligatorisk etterregistrering fra innsamleren. Opprinnelig plan (innsamler registrerer faktisk resultat/bilde av pantekvittering etter henting) ble vurdert, men Odin flagget dette som et eget friksjonspunkt — sannsynligheten for at folk faktisk gjør denne ekstra registreringen i etterkant er lav, og en påkrevd, upopulær handling etter at verdien allerede er overlevert svekker hele funksjonen. Selvrapportert anslag ved opprettelse er en del av den naturlige opprettelsesflyten og dermed lavere friksjon.

**Konsekvens — alle tall er anslag, ikke bekreftet:** siden datagrunnlaget nå er selvrapportert, må KI-en og UI-et konsekvent kommunisere tallene som anslag («anslagsvis», «cirka»), aldri som eksakte bekreftede beløp. Dette er spesielt viktig for lagets dugnad-total, som handler om ekte penger og et reelt sparemål — en KI-oppsummering som fremstiller et anslag som bekreftet inntekt kan gi et lag et falskt bilde av hvor nære de er målet sitt.

**Klimaeffekt:** eksplisitt utsatt fra MVP med mindre et dokumentert beregningsgrunnlag (kilde for CO₂ per beholder e.l.) finnes før PRD skrives. Antall beholdere og kroner er langt enklere å vise presist og prioriteres. Hvis klimaestimat tas med senere, skal det merkes tydelig som estimat med kilde — KI-en skal aldri dikte opp CO₂-tall eller anta at panten ellers ville havnet i naturen.

## Landskap og sammenlignbare konsepter
*Bakgrunnssøk — 2026-09-07*

**Konklusjon:** PantBuddy-konseptet finnes allerede delvis — i Norge og internasjonalt. Dette er ikke et argument mot å bygge det (studieprosjekt, ikke et krav om markedsnyhet), men "What Makes This Different" må formuleres ærlig rundt dette, ikke late som feltet er tomt.

**Infinitum (systemeieren selv) — «Bestill pantehenting» / «Pant for lag og foreninger»** (funnet av Odin, sjekket direkte 2026-09-07):
- Infinitum, som eier og drifter det norske pantesystemet, tilbyr gratis henting av pantesekker for «bedrifter, lag og organisasjoner med større mengder pant», registrering på customerportal.infinitum.no.
- **Håndteringsgodtgjørelse:** 5 øre per boks, 10 øre per flaske, i tillegg til selve panteverdien — utbetales etter at Infinitum har mottatt og behandlet sekkene.
- **Tjenestebeskrivelsen forutsetter at klubben allerede har samlet inn tomgodset:** «Ta imot tomgodset fra kunden og betal ut panten. Saml tomgodset i pantesekker og forsegl», deretter «Bestill gratis henting». Ingen hjelp til å finne/oppdage spredte individuelle givere er beskrevet — kun henting av allerede fylte, forseglede sekker.
- Ingen eksplisitt minstemengde funnet, men Infinitum ber om at «sekken fylles helt opp, slik at vi kan ha en miljøeffektiv transport».
- **Konklusjon:** dette er ikke direkte konkurranse mot PantBuddy, men et komplementært siste steg — Infinitum løser innløsning/utbetaling av allerede innsamlet pant, PantBuddy løser oppdagelse/matching av spredte givere. Bør nevnes eksplisitt i en eventuell proposal/PRD som en integrasjonsmulighet, ikke skjules som en trussel.
- Kilder: [infinitum.no/no/pantesystemet/bestill-pantehenting](https://infinitum.no/no/pantesystemet/bestill-pantehenting/), [test.infinitum.no/lag-og-foreninger](https://test.infinitum.no/lag-og-foreninger/) (merk: «test.»-subdomene, kan være en forhåndsvisning/staging-versjon av siden — bør bekreftes mot produksjons-URL før dette siteres eksternt).

**Norge (øvrige, tidligere funn):**
- **«Pant»** (iOS-app, App Store id1530729533) — lar giver velge hvem som skal få panten og varsler ved henting. Ligger tett opptil PantBuddys giver→formål-mekanikk. Utvikler/aktør bak appen er ikke bekreftet (kan være nedlagt studentprosjekt eller aktiv aktør) — ikke undersøkt videre.
- **Pantit** (pantit.no) — mulig nedlagt/under omlegging (nettsiden ga 404 ved henting), indeksert som «pant og resirkulering»-plattform.
- **Pantes.no** — bekreftet levende. Lag/foreninger oppretter en delbar innsamlingsside; givere får en unik digital «pantelapp» de kan dele; innsamlere bruker et interaktivt kart for å se og markere hentede flasker; organisasjonen kan bulk-innløse (utbetaling tar opptil en måned) eller innløse lokalt. **Ingen giver-profiler, ingen rating, ingen avtalt-henting-funksjon** — bekreftet fraværende, altså nettopp det PantBuddy legger til.
- **Pantedugnad.no** — betaverktøy for lag som skal samle pant enklere enn dør-til-dør. Funksjonssett ikke bekreftet (JS-rendret side).
- **Spleis «Digital flaskeinnsamling»** (SpareBank1) — brukt av skolekorps/speidergrupper som digitalt alternativ til dør-til-dør-innsamling.
- **Pantelotteriet** (Norsk Pantelotteri AS, Thon Group + Røde Kors) — panteautomat-knapp konverterer pantverdi til lotteribillett, ~150 mill. kr/år til Røde Kors siden 2008. Ikke person-til-person, men er den dominerende eksisterende «gi bort pant til godt formål»-vanen i Norge — konkurrerer om samme impuls som PantBuddys giver-side.
- Analog forløper: speidergrupper og skoleklasser har lenge samlet pant dør-til-dør (nyttår, 17. mai) som dugnad — det PantBuddy ville digitalisert på lag/forening-siden.

**Internasjonalt:**
- **Pfandgeben** (Tyskland) — den nærmeste direkte parallellen til PantBuddys privatperson-til-privatperson-for-penger-del. Formaliserer den kjente uformelle «flaskesamler»-praksisen: folk poster tomflasker, innsamlere i nærheten (ofte folk som er avhengige av denne inntekten) tar dem imot — kontaktløst/anonymt alternativ finnes, snittid tilbud→aksept ca. 17 minutter, pluss SMS-fallback for innsamlere uten smarttelefon. Eksplisitt rammet som å bedre arbeidsforholdene for uformelle innsamlere.
- Danmark/Sverige: kun funnet innløsning-bekvemmelighet-apper (digitaliserer utbetaling/kvitteringer), ikke giver-til-innsamler-matching. Ingen nordisk motpart til Pfandgeben funnet utenfor Norges egne forsøk over — kan være et reelt regionalt hull, men ikke bekreftet med sikkerhet.

**Tillitsmodell — trolig løst problem, ikke noe å finne opp på nytt:**
- Finn.no Torget: gjensidig vurdering etter handel (publiseres først når begge har vurdert, eller etter 3 uker) — forhindrer gjengjeldelses-vurderinger.
- Buy Nothing-grupper: uformell men sterk sosial håndheving — et no-show gir varig rykte i gruppen. Norm er henting på «verandaen» fremfor direkte møte, for å redusere ubehag ved fremmedkontakt.
- Ingen av forbildene har hard identitetsverifisering eller forsikring/escrow for fysisk sikkerhet — det forblir et åpent designspørsmål hvis PantBuddy skal gå lenger enn dette.

**Pantelapp-overførbarhet (praktisk, ikke juridisk friksjon):**
- En pantelapp fra en panteautomat er IKKE personbundet (bearer-instrument — den som har kvitteringen kan innløse), men ER butikk-/kjedebundet (kan ikke innløses på tvers av konkurrerende kjeder). Gyldighetstid varierer (Coop/Rema oppgis å aldri utløpe, Norgesgruppen rundt ett år/999 dager — kildene spriker noe på eksakt tall).
- **Praktisk konsekvens for UX:** ingen overføringsproblem hvis giveren gir bort fysiske flasker/bokser (innsamleren panter selv i egen automat/butikk). Problemet oppstår kun hvis giveren panter først og gir bort selve kvitteringen — da er innsamleren låst til å innløse i nettopp den butikken/kjeden. Appen bør derfor oppmuntre til å gi bort ugjenløste flasker/bokser, ikke ferdig-pantede kvitteringer, med mindre giver og innsamler handler i samme kjede.

**Ikke bekreftet / bør sjekkes videre hvis dette blir hovedretningen:**
- infinitum.no er ikke sjekket direkte for autoritativ pantelapp-regel (kun sekundærkilder brukt).
- Pantit.no sin faktiske status (nedlagt? relansering?) — Wayback Machine ikke sjekket.
- Ingen bruks-/nedlastingstall funnet for noen av de nevnte appene — eksistens er bekreftet, skala/suksess er ikke.
- Juridisk/forsikringsmessig ansvar ved hjemme-hentinger i norsk sammenheng — ikke funnet adressert noe sted.

Full digest fra bakgrunnssøket finnes i samtalehistorikken (2026-09-07); ikke lagret som egen fil siden dette er et raskt grunnlagssøk, ikke en formell bmad-deep-recon-kjøring.
