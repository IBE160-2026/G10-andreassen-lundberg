---
name: VaktMatch
title: VaktMatch – brukeropplevelse og oppførsel
status: final
created: 2026-10-31
updated: 2026-11-08
issue: SCRUM-47
authorship: Codex-konkretisering på Odins gjennomføringsmandat 2026-11-08.
validation: KI-kontrollert designgrunnlag; ikke brukertestet eller felles detaljgodkjenning.
sources:
  - ../../prds/prd-G10-andreassen-lundberg-2026-10-29/prd.md
  - ../../../../productbrief.md
  - ../../../../docs/demoscenario-fravaer.md
  - ../../../../docs/kostnadsanslag.md
  - ../../research/domain-egenmelding-varsling-og-fravarsperiode-2026-10-31/research.md
  - ../../../../docs/forslag-ved-frafall.md
---

# VaktMatch – opplevelseskontrakt

## Foundation

Responsiv web i eksisterende React-app, fra 360 px til PC. Native HTML-kontroller
og egne enkle komponenter; kontrakten innfører ingen ny UI-avhengighet.
[DESIGN.md](DESIGN.md) eier visuell utforming og tokenverdier. Dokumentparet
gjelder foran illustrasjonene ved konflikt. `final` betyr ferdigstilt UX-grunnlag,
ikke godkjent app, brukertest eller felles detaljbeslutning.

Kari fra PRD er en konstruert skiftleder ved morgenskiftbytte på en generell,
fiktiv arbeidsplass. Hun kan bruke mobilen mens hun avklarer fravær og PC til
lengre sammenligning. Ingen bestemt bransje, faktiske personopplysninger eller
observerte arbeidsrutiner er innført. [Kildeavstemmingen](.working/source-reconciliation-2026-11-08.md)
skiller eksisterende krav fra [Codex sine avklaringer på mandat](.working/delegated-decisions-2026-11-08.md).

## Information Architecture

| Flate | Inngang og formål | Reise / referanse |
|---|---|---|
| Ukesoversikt | Oppstart og «Ukesoversikt»; gjeldende uke 5, ansatte, behov, hull, låser og dataversjon. | UJ-1/4; [ukesoversikt](mockups/key-ukeplan.html). |
| Fravær | «Registrer fravær» eller vakt fra ukesoversikten; person, kalenderperiode og ett målskift, deretter eksplisitt simulering. | UJ-1/2/3; [fravær](mockups/key-fravaer.html). |
| Alternativer | «Finn alternativer» etter fraværssimulering; sorter og undersøk resultater uten planendring. | UJ-1/2/3; [alternativoversikt](mockups/key-alternativer.html). |
| Alternativdetaljer og planforslag | «Undersøk»; hele forslaget og konsekvensene, regelgrunnlag, historikk, kostnad og forklaring. | UJ-1/2/3; [detaljer med flytting](mockups/key-detaljer.html). |
| Valg og tilbud | «Velg alternativ»; gjeldende øktvalg, eventuell simulering og svar per berørt person. | UJ-1/2; [klikkbar prototype](mockups/prototype.html). |
| Datagrunnlag | «Datagrunnlag» i apphodet; forhåndsvis og last et av de faste datasettene. | UJ-1/3; prototypens datagrunnlagsflate. |
| Tidligere valg | Åpne seksjonen fra Valg; vis historiske versjoner, valg og simulerte svar. | UJ-1/3; spesifisert i tabellene under. |

Apphodet og demobanneret er felles. Stegnavigasjonen viser Fravær → Alternativer
→ Valg; ukesoversikt og datagrunnlag er tydelige sideinnganger. Feltendring,
undersøkelse, sortering og navigasjon setter aldri fravær eller velger et forslag
automatisk. Tilbake bevarer gyldig skjema, søkeinnstillinger og listetilstand.

## Voice and Tone

Bokmål, korte konkrete setninger. Forklar både tilstanden og neste mulige handling.
Behold PRD-begrepene «kontrollstatus», «dekning» og «søkestatus» som separate felt.

| Situasjon | Ordlyd / regel |
|---|---|
| Demo | «Syntetiske data. Ingen endringer i vaktlisten.» |
| Før simulering | «Velg én vakt å undersøke. Dagene viser en periode, ikke kjent fraværsvarighet.» |
| Fravær simulert | «Fraværet er simulert for valgt vakt. Finn alternativer når du er klar.» |
| Fullført, ingen beståtte funn | «Ingen kontrollerte alternativer funnet innenfor valgt søkeomfang.» |
| Kontroll | «Oppfyller scenarioreglene», «Regelavvik» eller «Uavklart». Ingen «lovlig» eller «godkjent plan». |
| Mangel | «Tilgjengelighet for V01 må avklares.» Vis hvilken regel mangelen hindrer. |
| Valg | «Valgt i økten. Vaktlisten er uendret.» |
| Tilbud | Bruk «Simuler tilbud», «Simuler aksept» og «Simuler avslag». Ingen påstand om ekte utsending. |
| KI-reserve | «KI-forklaring er ikke tilgjengelig. Standardforklaringen vises fortsatt.» |
| Gammelt resultat | «Tidligere vurdering på dataversjon … Kjør ny vurdering på gjeldende grunnlag.» |

## Component Patterns

Felles navn med DESIGN.md. Visuelle verdier arves via blant annet
`{typography.body.fontSize}`, `{spacing.control-min}` og `{colors.focus}`.

| Komponent | Atferd |
|---|---|
| app-header | Vis arbeidsuke, dataversjon og datasettets vurderingstidspunkt. «Ukesoversikt» og «Datagrunnlag» er navngitte innganger; maskinens klokke styrer ingen vurdering. |
| demo-banner | Synlig på alle flater. Prototypen merker dessuten egne nye tall som konstruerte illustrasjoner, uten å fremstille dem som fasitdatasett. |
| step-navigation | Gjeldende steg har `aria-current="step"`. Tilbake er alltid mulig; fremover som krever gyldig grunnlag har lesbar begrunnelse når utilgjengelig. |
| week-overview | Vis uke 5 med tildelte, K-behov, udekkede plasser og låser. En vakt kan forhåndsfylle fraværsskjemaet, men utfører ingen handling. Påbegynt/historisk/låst tildeling har forklaring. |
| absence-form | Person først. Neste planlagte, ikke påbegynte uke-5-vakt foreslås som redigerbar startvakt. Kalenderdager er heltall ≥1, standard 1; velg ett målskift fra berørte vakter. «Simuler fravær» er egen handling før «Finn alternativer». |
| affected-shifts | Perioden går fra midnatt på startvaktens lokale dato til midnatt etter siste kalenderdag i Europe/Oslo. List hele vakter som overlapper perioden; vis begge datoene ved nattvakt. Påbegynte eller utenfor uke 5 vises med begrensning og kan ikke velges. Et låst målskift kan få simulert fravær; lås beskytter andre tildelinger mot flytting og skjuler ikke udekket behov. Ingen vaktdeling eller automatisk massefravær. |
| shift-context | Vis målskift, fraværende, behov, dataversjon og faktisk udekket plass ved resultatene. Et forslag eller en aksept gjør ikke gjeldende grunnlag bemannet. |
| search-controls | Søkegrense 0/1, standard 1; forklar «Direkte erstattere» / «Også én flytting». P1 aktivt alene som standard. Minst ett P-kriterium; et navngitt `select` velger P1–P2 eller P2–P1 når begge er aktive. Endret grense krever nytt søk, endret sortering omrangerer samme gyldige funn uten ny kontrollstatus. |
| alternative-card | Del i rangerte komplette/beståtte forslag, beståtte uten komplett sorteringsgrunnlag og øvrige undersøkbare funn. Vis kandidat, direkte/flytting, forslagets dekning, kontroll, aktive sorteringstall, timer/hvile, kostnad/differanse eller mangel og berørte vakter. «Undersøk» er separat fra valg. |
| status-badge | Vis én navngitt dimensjon om gangen. Kjent brudd gir Regelavvik selv ved andre mangler; ellers datamangel gir Uavklart. Bestått krever alle R1–R5. «Ikke vurdert» er en mulig regelrad, ikke en fjerde samlet kontrollstatus. |
| alternative-detail | Enhver kandidat kan undersøkes. Tilbake gjenoppretter liste, prioritering og rulleposisjon. Vis alle regelverdier, før/etter for alle berørte, mangler, historikk, kostnadsgrunnlag og forklaring. Bare et komplett forslag som oppfyller scenarioreglene på gjeldende grunnlag, kan markeres som valgt. |
| plan-proposal | Vis gjeldende og foreslått tildeling for hver berørt vakt, særlig X og Y ved én flytting. Oppgi om en ny vakt blir udekket. Egen «Forslag»-etikett; ingen skriv-til-plan-handling. |
| fact-table | Navngi person, måltall, enhet, før, etter, kilde/periode og eventuell mangel. R1–R5 kan åpne kort kilde/begrensning. Vis begge sider av hvile og uke-4/6-grunnlag. Kostnad har alternativ, tilsvarende referanse og differanse med timer/satser/tillegg. |
| explanation-panel | Standardforklaringen finnes alltid. «Forklar forskjellen» sammenligner undersøkt mot øverst rangert med feltene Kort svar, Avveining, Konsekvenser og Usikkerhet. Er alternativet øverst, si det. Uten rangert referanse er handlingen utilgjengelig med «Ingen rangert referanse på dette grunnlaget». Ved avbrutt søk avgrenses referansen til foreløpige funn. Modelltekst kan aldri endre fakta, rangering eller valg. |
| offer-panel | «Simuler tilbud» gjelder gjeldende øktvalg og dataversjon. Behold sendt-hendelsen og vis ventende svar per berørt person. Full aksept først når alle berørte har akseptert; avslag er synlig og bevares ved ny undersøkelse. Uten simulering: «Aksept ikke simulert». |
| dataset-panel | Forhåndsvis gammel/ny versjon og endringer i bemanning, mangler, låser, historikk og kostnadsgrunnlag. Bekreftet innlasting gir ny kontroll og kostnad, aldri arvet aksept. Ingen filopplasting eller leverandørkobling. |
| session-history | Bevar valg/svar på opprinnelig versjon, atskilt fra gjeldende valg. Valg lever i aktiv fane; lukking avslutter økten. Ingen varig lagring som Må. |
| message-panel | Tomtilstand, feil og utdatert resultat har forklaring og relevant vei videre. API-feil gjengis på norsk uten intern stacktrace. Bevar siste gyldige grunnlag ved innlastingsfeil og merk det tydelig. |
| action-button | Native knapp/lenke etter handlingens type. Dobbeltklikk skal ikke duplisere fravær/tilbud. Deaktivering under arbeid suppleres med tekst; «Prøv igjen» beholder gyldige felt. |

## State Patterns

Alle flater har lesbar overskrift, synlig fokus og norsk feilmelding med vei videre.

| Flate / tilstand | Synlig behandling og gjenoppretting |
|---|---|
| Felles oppstart / backend utilgjengelig | «Laster demodata …»; ved feil «Får ikke kontakt med backend» og «Prøv igjen». Ikke vis konstruerte resultater som en vellykket API-respons. |
| Ukesoversikt tom / feil | «Ingen vakter i dette grunnlaget» og datagrunnlagsinngang; feil beholder identifisert siste gyldige versjon. Udekket behov vises uten detaljåpning. |
| Fravær tomt / ugyldig | Ingen ansatt/vakt: feil ved felt og feilsammendrag. Ingen egnede vakter: forklar dato/uke eller påbegynt vakt, tilby annet målskift. Ingen simulering utføres. |
| Fravær allerede registrert / gjentatt handling | Behold samme registrering og opplys «Fravær er allerede simulert for denne vakten». Tidligere fravær mistes ikke. |
| Felt endret etter simulering | Behold aktivt fraværsgrunnlag atskilt fra utkastet. Nytt målskift krever eksplisitt ny simulering; gamle resultater får målskift/versjon ved seg. |
| Alternativer før søk / søker | Vis innstillinger og «Finn alternativer»; under søk vis søkegrense og «Søker …». Ingen responstid loves. Gammelt resultat vises bare som tidligere vurdering. |
| Fullført søk, ingen kontrollerte forslag | Bruk den avgrensede tomteksten over. Behold uavklarte/avvik/delvis dekning synlige og tilby ny grense eller komplettert datasett der relevant. |
| Søk avbrutt / feilet / utenfor omfang | Skill «Avbrutt – ufullstendige resultater», «Søket feilet» og «Ikke kjørt – utenfor omfang». Forklar og tilby nytt søk eller nytt målskift; ingen uløselighetspåstand. |
| Alternativer likt rangert / manglende P2-data | Samme rang ved likhet på alle aktive kriterier. Stabil ID-rekkefølge er bare visning. Bestått uten avtalt positivt timetall står utenfor full rangering; ingen skjult P1-reserve. |
| Detaljer tomme / utdatert / feil | Ingen undersøkt: velg fra listen. Ved gammel versjon: vis historikkmerke og krev ny vurdering før gjeldende valg/tilbud. Feil beholder listen og tilbyr tilbake eller gjenforsøk. |
| Detaljer med regelbrudd / mangler / delvis dekning | Vis alle kjente funn og den konkrete mangelen. «Velg alternativ» som bestått er utilgjengelig med forklaring; «Undersøk» er fortsatt tilgjengelig. |
| Kostnad eller historikk mangler | «Uavklart anslag» / «Historikk ufullstendig» med manglende felt/periode. Ingen null, skjult delsum som total eller ny fairness-poengsum. Kontrollstatus endres bare hvis nødvendig kontrollgrunnlag mangler. |
| KI venter / mangler nøkkel / feil | Standardforklaring blir stående. Ny forespørsel viser ventestatus; feil gir reservebeskjeden uten å fjerne fakta eller øktvalg. Ingen automatiske modellkall ved kortåpning. |
| Valg og tilbud tomt / venter / avslag | Uten valg: tilbake til alternativer. Med valg: «Aksept ikke simulert» frem til tilbud; ventende, aksept og avslag vises per person. Avslag tillater ny undersøkelse uten å slette utfallet. |
| Datagrunnlag tomt / uendret / feil | Ingen andre forhåndslagde datasett: si det. Uendret innhold merkes uttrykkelig. Feilet bytte beholder siste gyldige versjon og gir gjenforsøk. |
| Tidligere valg tomt / gjeldende grunnlag byttet | «Ingen tidligere valg i denne økten». Etter bytte vises gammel versjon, valg og svar historisk; ny kontroll og nytt valg kreves. |
| Nett av / lokal server stoppet | Ingen antatt offline-synkronisering. Behold lest kontekst, si at backend er utilgjengelig og tilby gjenforsøk; KI-feil alene blokkerer ikke regelbasert flyt. |

## Interaction Primitives

- Feltendring er utkast; «Simuler fravær» muterer demoens aktive fraværstilstand
  for ett målskift, og «Finn alternativer» starter søket etterpå.
- Bruk native `select`, radio og heltallsfelt. Tastatur kan utføre alle handlinger;
  P-rekkefølge har et eksplisitt valgfelt og krever ikke dra-og-slipp.
- En liste med 0/1 søkegrense er ikke et løfte om globalt komplett søk.
  Fullført funn, avbrutte funn og kandidatkontroll beholdes som separate fakta.
- «Undersøk» flytter fokus til detaljoverskriften. Tilbake returnerer til samme
  undersøk-knapp når den finnes. Ved nytt resultat flyttes fokus til resultatoverskriften.
- Bruk `aria-live="polite"` til korte søke-/valg-/tilbudsmeldinger; inputfeil kan
  bruke `role="alert"`. Ikke annonser hele kandidatlisten på hver endring.
- Et valgt alternativ låser eller reserverer ingen ansatte. Neste fravær bruker
  gjeldende data og tidligere simulerte fravær. Separat dataoppdatering må vise
  ny bemanning før et tidligere forslag regnes som gjennomført.
- Datasettbytte arkiverer gjeldende valg/svar på gammel versjon. Bevar tidligere
  fravær der de fortsatt gjelder; eventuelle manglende referanser forklares før
  nytt målskift velges. Skjul aldri et bortfalt grunnlag gjennom automatisk aksept.
- Ingen tvungne modaler, hoverhandlinger, kontinuerlig autosøk eller snarveier
  med enkeltbokstaver. Navigasjon bruker synlige handlinger.

## Accessibility Floor

Dette er implementeringskrav og kontrollpunkter, ikke en attest på ferdig app.

- PRD NFR-2: minst 4,5:1 for all tekst. Bruk DESIGN.md sine kontrastpar;
  `{colors.focus}` får synlig ring mot lys flate. Status har alltid tekst.
- Alle skjemaelementer har koblet etikett, hjelpetekst og eventuell feil via
  `aria-describedby`; ugyldig felt har `aria-invalid`. Feilsammendrag lenker til felt.
- Ett `main`, semantiske overskrifter og «Hopp til innhold». Tab-rekkefølge følger
  leserekkefølge. Ingen musekrav, tastaturfelle eller skjulte fokusmål.
- Kontroller minst `{spacing.control-min}` høye. Tekst kan forstørres til 200 %
  uten avkorting; innhold skal flyte om ved 360 px uten vannrett rulling.
- Før/etter-tabeller har navngitte rader/kolonner eller tilsvarende semantiske
  definisjonslister på mobil. Enheter og mangler er lesbare uten farge.
- `prefers-reduced-motion` fjerner ikke nødvendig informasjon; animasjon er
  unødvendig for flyten. Ingen blink, autoavansering eller tidsbegrenset skjema.
- Kontroller tastatur, skjermleser, zoom, kontrast og mobilbredde ved appbygging.
  Prototypens visuelle kontroll erstatter ikke disse testene.

## Responsive & Platform

| Bredde | Oppførsel |
|---|---|
| 360–767 px | Én kolonne, fullbredde felt/handlinger ved behov, vaktliste stablet per dato, detaljer som egen innholdsflate med tilbake. |
| 768–1023 px | Én hovedkolonne med flere sammenligningstall per rad når de får plass. Ingen informasjon flyttes til hover. |
| Fra 1024 px | Kontekst ved siden av arbeidsflaten; detaljer kan erstatte listeflaten. Kilder, historikk og tilbud kan leses uten lang modal. |

Samme rekkefølge, innhold og handlinger på alle bredder. Appen er lokal web;
konto, pushvarsler, installasjon som mobilapp og bakgrunnssynkronisering inngår ikke.

## Key Flows

Kari er konstruert eksempelperson fra PRD. Reisetitlene under gjengis ordrett.

### UJ-1. Kari finner en erstatter før vakten starter.

1. Kari åpner ukesoversikten på mobilen. Uke 5, vurderingstidspunkt, behov og
   dataversjon er synlige. Hun åpner Fravær og velger A01.
2. Neste planlagte vakt foreslås; hun kontrollerer 14.10 kl. 08–16 og standard
   én kalenderdag. Berørte vakter vises; bare ett målskift velges.
3. Hun trykker «Simuler fravær» og ser udekket behov, så «Finn alternativer»
   med grense 1 og P1. Simuleringen og søket er separate bekreftede handlinger.
4. Hun sammenligner A02/A03 og undersøker også A05. A05s 8 t hvile/R4-brudd
   er synlig; kandidaten kan ikke velges som bestått.
5. Hun kan bytte til P2 eller undersøke et lavere rangert alternativ uten å
   endre kriteriene. Detaljene viser timer/hvile før/etter, historikk, kostnad
   og standardforklaring. «Forklar forskjellen» er valgfri KI-handling.
6. **Avklaring:** Kari markerer et komplett bestått alternativ som valgt;
   hun ser hvilket grunnlag valget gjelder og at vaktlisten fortsatt er uendret.
7. Hun kan simulere tilbud og svar, eller beholde «Aksept ikke simulert».
   Nytt fravær starter samme flyt på gjeldende data; gammel aksept reserverer ingen.

Feilvei: ugyldig felt stopper simuleringen med feltlenke. Søkefeil beholder
grunnlaget og tilbyr gjenforsøk. KI-feil beholder standardforklaring og valg.
Et avbrutt søk merkes ufullstendig; Kari får ingen påstand om beste eller eneste løsning.

### UJ-2. Ingen direkte erstatter, men én flytting løser det.

1. Kari simulerer ett fravær og kjører søk med grense 0.
2. Ingen direkte erstatter er funnet innenfor reglene. Hun endrer grensen
   til 1 og trykker «Finn alternativer» igjen.
3. Hun undersøker forslaget B fra Y til X, med C som dekker Y.
   Planforslaget viser begge vakter før/etter og alle berørtes kontrollverdier.
4. **Avklaring:** Begge vakter er foreslått dekket og alle kontroller består;
   Kari kan velge forslaget. Gjeldende ukesoversikt er fortsatt uendret.
5. Ved tilbudssimulering kreves svar fra B og C. Bare begge akseptert gir
   full simulert aksept, uten at planen endres.

Kanttilfelle: hvis Y blir udekket, vises den konkrete vakten med delvis dekning;
forslaget står utenfor komplette løsninger og kan ikke velges som bestått.
Ingen forslag med to flyttinger sniker seg inn ved grense 1.

### UJ-3. En mulig kandidat mangler opplysninger.

1. Kari undersøker V01 som har K1, men mangler bekreftet tilgjengelighet.
2. «Uavklart» og «Tilgjengelighet for V01 må avklares» vises ved R2.
   Hun kan lese detaljer, men ikke velge kandidaten som bestått.
3. Hun åpner Datagrunnlag, velger et forhåndslaget komplettert datasett og
   ser gammel/ny versjon og akkurat hvilke opplysninger som endres.
4. Hun laster inn og kjører ny vurdering. Gamle valg og svar finnes i
   Tidligere valg på gammel versjon; verken rangering eller aksept arves skjult.
5. **Avklaring:** Den nye vurderingen viser enten bestått V01 på nytt grunnlag,
   fortsatt konkret mangel eller kjent brudd. Kostnaden beregnes på nytt.

Feilvei: mislykket innlasting lar siste gyldige versjon være tydelig tilgjengelig.
Komplettering er ingen garanti for bestått kontroll; kjent brudd har forrang.

### UJ-4. Sensor kjører appen.

Sensor er PRD-ens konstruerte evalueringsrolle, ikke dokumentasjon på utført test.

1. Sensor følger repoets README for lokal oppstart uten konto eller KI-nøkkel.
2. Ukesoversikt og dataversjon gjør startgrunnlaget identifiserbart.
3. Sensor følger UJ-1 og UJ-2 med demoens forhåndslagde data.
4. Sensor prøver «Simuler fravær» uten nødvendig felt, retter feltet og
   gjentar handlingen. Meldinger forklarer feil og hindrer duplikatregistrering.
5. **Avklaring:** Standardforklaring, status, konsekvenser og uendret vaktliste
   kan undersøkes uten nøkkel; tester kjøres etter README.

Feilvei: stoppet backend gir norsk melding og «Prøv igjen», uten en tilsynelatende
vellykket vurdering. Oppstartstid og ende-til-ende-funksjon må verifiseres i appen.

## Handoff og kontrollgrenser

Alle Må-flyter har en flate over. Før appbygging brukes [kildeavstemmingen](.working/source-reconciliation-2026-11-08.md)
mot PRD, S1–S5, H1–H5, F1–F7, D1–D5/D8, M1–M2 og O1–O5. Det er designdekning;
regelresultater og kostnader må fortsatt verifiseres av kjørbare tester.
Låsing i UI og varig logg er Bør og har ingen aktiv handlingsflate her.
Modellvalg/kostnadsgrense (SCRUM-59), ekstern vikars øvrige arbeid (SCRUM-19)
og leveringsavklaringer (SCRUM-49) forblir egne saker.

Se [kontrollrapporten](validation-report.md) for faktisk dokument- og
prototypekontroll og [overleveringen](implementation-handoff.md) for
arbeidsrekkefølge og innhold som beregningslagene må levere til grensesnittet.
