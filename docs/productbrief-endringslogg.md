# Produktbrief – endringer og begrunnelser

*(Skrevet: Codex · 06.10.26, etter Odins ønske om synlige endringer og enkle begrunnelser)*

## Utgangspunkt og lesemåte

Denne loggen forklarer utviklingen av [gjeldende produktbrief](../productbrief.md).
Fast utgangspunkt er [første versjon av productbrief.md, 17.09.26](https://github.com/IBE160-2026/G10-andreassen-lundberg/blob/587bc45893f56a2f6ce81e4fa7d7b5e447064bc7/productbrief.md),
commit `587bc45893f56a2f6ce81e4fa7d7b5e447064bc7`. Tidligere kandidatbriefer er
bakgrunn; [den historiske henvisningen](../_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/brief.md)
og [den tidligere prosessloggen](../_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-07-VaktMatch/.memlog.md)
bevarer forbindelsen til arbeidet før hovedbriefen ble opprettet.

Innslagene nedenfor er etterregistrert 06.10.26 fra Git-historikken, dagens
arbeidskopi, samtalens avklaringer og de lenkede kildene. De dekker alle
meningsbærende endringer fra utgangspunktet, inkludert dokumentrolle og metadata.
Git viser den nøyaktige ordlyden. Begrunnelser som er formulert av Codex, er
merket som det; de er ikke selvstendige gruppebeslutninger.

## Hvorfor arbeidsutkastet er endret

*Oppsummert av Codex 07.10.26 fra Odins innspill i BMAD-samtalen og innslagene
nedenfor. Dette er prosjektbegrunnelser, ikke nye beslutninger eller antakelser
om personlige motiver.*

Odin presiserte 07.10.26 at endringene ennå ikke er avklart med Stian. Utkastet
publiseres nå slik at endringene og begrunnelsene kan vurderes sammen. Det skal
ikke leses som en felles godkjenning eller en ferdig kravspesifikasjon.

- **Gi lederen bedre beslutningsgrunnlag.** Odin ønsker at KI viser muligheter,
  konflikter, arbeidstidsgrenser, hvile og interne føringer, mens lederen beholder
  myndigheten og kan prioritere hensyn selv. Dette begrunner tydelig informasjon,
  lederstyrt sortering og ønsket om innstillinger for søkeomfang (E15–E19).
- **Beholde plangenerering som et forslag.** Lederen skal kunne få en generert
  plan og forstå konsekvensene uten at VaktMatch innfører den i faktisk vaktliste.
  Demodata og generering kan inngå sammen. Den midlertidige
  fjerningen av generering var Codex sin tolkning, korrigert av Odin (E20–E24).
- **Demonstrere ideen uten å være avhengig av leverandørtilgang.** Odin ser for
  seg en mulig fremtidig kobling til oppdaterte bemanningsdata, men tilgang er
  uavklart. Fiktive data er et praktisk demogrunnlag (presisert i E26). To dataversjoner som
  demonstrasjon av en endring er et forslag fra Codex, ikke et valgt krav (E20, E23).
- **Starte med konkrete KI-svar.** Odin prioriterer faste handlinger og
  situasjonstilpassede forklaringer først, med chat som mulig senere utvidelse.
  [Faglærerens tilbakemelding](../tilbakemelding-product-brief.md) støtter å
  utsette friteksttolkning og la kjernen fungere uten KI-nøkkel (E04, E07–E08, E12).
- **Skille informasjon fra ekstra plikter.** Opplysninger som mangler skal
  synliggjøres, men ansvar for å rette dem er ikke fordelt. Odin ønsker mulighet
  til å slå av logging og begrunnelseskrav når de bare følger interne retningslinjer
  og ikke er lovpålagt; eventuelle lovkrav er ikke fastslått. Brukertesten er et
  valgfritt KI-forslag, ikke et nytt dokumentert leveransekrav (E19, E22).

Til felles vurdering gjenstår særlig omfanget av generering og omfordeling,
scenarioregler og sorteringsvalg, oppdatering av data, eventuell logging,
teknologistakk og arbeidsdeling. Konkrete regeltall og demomekanismer som er
merket som KI-forslag, er ikke automatisk godkjent ved publisering.

## 06.10.26 – dokumentrolle og sporbarhet

Dokumentryddingen i E01 finnes i commit `8060981a73ef9c461406959d19ba180cc7f9ffdf`.
E02 innføres med denne loggen. Begge bevarer briefens status som utkast.

| ID | Hva ble endret? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E01 | Briefen ble tydelig merket som eneste gjeldende produktbrief. `document_role: current_product_brief` ble lagt til, `updated` ble endret fra 17.09 til 06.10, og teksten peker til dokumentoversikten. | Gjøre det lett å skille hovedbriefen fra alternativforslaget og den erstattede briefen. Selve produktinnholdet ble bevart i denne runden. | Odin ba om opprydding etter [Bårds tilbakemelding](../tilbakemelding-product-brief.md). Dokumentrolle presisert av Codex; ingen ny godkjenning av produktomfang. |
| E02 | Briefen lenker til denne lesbare endringsloggen. Oppdateringene får opphav, status og begrunnelse; [.memlog.md](../.memlog.md) bevarer den løpende prosesshistorikken. | Gjøre det mulig å forstå både hva som er endret siden første versjon, og hvorfor. | Odin ba uttrykkelig om synlige endringer og korte forklaringer 06.10.26. Regel lagt til i [AGENTS.md](../AGENTS.md#endringer-i-produktbriefen). |

## 06.10.26 – arbeidsretning og KI i førsteversjonen

Disse endringene er innarbeidet i arbeidsutkastet etter samtalen 06.10.26.
De er ikke registrert som felles godkjenning av alle valg. Den tidligere
statussetningen om at produktinnholdet ennå var uendret fra 17.09, er samtidig
erstattet med en beskrivelse av denne oppdateringen.

| ID | Hva ble endret fra første versjon? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E03 | Innledningen beskrev et utkast til innlevering med detaljer som skulle bekreftes sammen. Nå beskriver den videre arbeid etter Odins innspill, med mulighet for tilbakemelding fra Stian underveis. Rangeringen skal konkretiseres før implementering, uten at en ny felles avklaringsrunde er satt som vilkår for å redigere utkastet. | Gjøre arbeidsutkastet konkret nok til at videre innspill kan gis til en synlig løsning. | Odins uttrykkelige ønske om å arbeide videre nå. Arbeidsdeling og endelig omfang står fortsatt åpne. |
| E04 | KI skulle tolke behov i fritekst. Førsteversjonen bruker nå skjemaer og faste handlinger; chat og friteksttolkning av behov og ønsker er uttrykkelig utenfor v1. | Prioritere konkrete svar først og vurdere samtalegrensesnitt når et behov viser seg. | Odin valgte faste svar før chat. Utsettelse av friteksttolkning følger også [Bårds råd](../tilbakemelding-product-brief.md) og [svaret fra Stians KI-assistent](../_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/svar-til-felles-retning.md). |
| E05 | Sammenligningssiden har fått en fast struktur: anbefaling med begrunnelse, andre alternativer, regelkontroll, konsekvenser og manglende opplysninger. Handlingen «Finn alternativer» er konkretisert. | Gjøre svarene enkle å sammenligne og teste, samtidig som innholdet tilpasses vakten og ansattdataene. | Odin ønsket faste, konkrete svar. Feltene og handlingsnavnet er Codex sin konkretisering av denne retningen; detaljert grensesnitt er ikke ferdig bestemt. |
| E06 | Godkjenning av den genererte grunnplanen og visning av planen etter en godkjent endring er gjort eksplisitt. Første versjon krevde allerede bekreftelse før planen endres. | Vise hele forløpet fra plan til fravær og oppdatert plan, med tydelige beslutningspunkter for lederen. | Hentet fra [Odins forslag til felles retning fra 18.09](../_bmad-output/planning-artifacts/briefs/brief-G10-andreassen-lundberg-2026-09-18-turnusgenerering/forslag-til-felles-retning.md) og samtalens videreføring. Presisert av Codex i arbeidsutkastet. |
| E07 | Regelkontroll i kode er videreført og presisert: regelmotoren finner og kontrollerer kandidater og beregner konsekvenser. KI-forklaringen skal følge kontrollresultater og definerte prioriteringer, og ikke endre kandidatstatus eller rangering. Sporbarhetskriteriet er utvidet tilsvarende. | Unngå at forklaringen gir en annen anbefaling eller status enn det beregningsgrunnlaget støtter. | Odin beskrev vurdering ut fra regler og relevante ansattdata. Ansvarsdelingen er Codex sin presisering av dette, den opprinnelige briefen og [Bårds tilbakemelding](../tilbakemelding-product-brief.md). Konkrete prioriteringer og beregningsmetode er fortsatt åpne. |
| E08 | Kjerneflyten skal fungere uten KI-nøkkel og ved modellfeil, med regelbaserte standardforklaringer. Dette er også lagt inn som suksesskriterium for generering, sammenligning og godkjenning. | Gjøre kjernefunksjonene demonstrerbare og testbare selv når språkmodellen ikke er tilgjengelig. | Kjørbarhet uten nøkkel er anbefalt av Bård. Oppførselen ved modellfeil er en presisering fra Codex i arbeidsutkastet. Ingen modell eller leverandør er valgt. |
| E09 | «Ingen kandidat passer» er presisert til udekket behov uten anbefalt erstatter. Fast svarformat og forbud mot å presentere et uavklart alternativ som gjennomførbart er lagt inn som suksesskriterier. | Gjøre eksisterende prinsipper om udekket behov og manglende data synlige og testbare i resultatet. | Codex sin konkretisering av opprinnelige suksesskriterier og det nye svarformatet. Prinsippene om udekket og uavklart var allerede med. |
| E10 | «Ukesgrunnlag» er flere steder blitt «plangrunnlag», og én uke er nå uttrykkelig et foreløpig utgangspunkt. Planhorisont er lagt til som et åpent valg. | Synliggjøre at materialet også inneholder et toukersforslag, uten å registrere to uker som valgt. | Codex sin markering av en uavklart forskjell mellom briefene. Odin har ikke i samtalen valgt en ny periodelengde. Dette er en åpnet avklaring, ikke en vedtatt utvidelse. |
| E11 | Omfanget av intern omfordeling, demoscenarioer med fasit og modellvalg er lagt til under åpne spørsmål. Domene, regler, rangering, tilbud/aksept, teknologistakk og arbeidsdeling var allerede åpne. | Synliggjøre valg som påvirker gjennomførbarhet og testing før de blir antakelser i PRD eller kode. | Codex sin oppfølging av [Bårds tilbakemeldinger](../tilbakemelding-product-brief.md) og diskusjonen. Ingen konkrete verdier eller løsninger er valgt her. |
| E12 | Scope krever tydelige ansvarsgrenser mellom datatilgang, regelberegning, KI-forklaring og visning. Vision nevner chat hvis bruk eller testing viser behov. Chatgrensesnitt, samtalehistorikk og generell agentplattform er ikke del av v1. | Gjøre senere chat mulig å koble til eksisterende funksjoner, samtidig som første leveranse holdes avgrenset. | Odin ønsket å bygge for en enklere senere utvidelse. Ansvarsgrensene er Codex sitt designforslag; det er ikke en garanti for at chat kan legges til uten mer arbeid. |

Problemhypotesen, målgruppen, konkurranseforbeholdene og åtte hovedseksjoner er
bevart. Forslaget om 8–10 ansatte, eksterne vikarer, 3–5 regler og ett fravær står
fortsatt i briefen. Intern omfordeling er ikke fjernet, og én uke er ikke erstattet
med et vedtak om to uker. Tidligere avgrensninger utenfor v1 er også beholdt.

## 06.10.26 – demonstrasjonsmiljø og konkret fraværsscenario

| ID | Hva ble endret? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E13 | Antakelsen om lager/logistikk i Who This Serves er erstattet med en generell arbeidsplass uten bransje. Demonstrasjonsdomene er fjernet fra listen over åpne valg. | Følge Odins valg av et bransjeuavhengig demonstrasjonsmiljø. Eksemplet trenger dermed ingen lager- eller oppdrettsspesifikke oppgaver. | Odin valgte «En generell arbeidsplass uten bransje» i samtalen 06.10.26. Innarbeidet i arbeidsutkastet. |
| E14 | Scope lenker til et konkret forslag med ansattdata, fem regler og tre fraværsutfall. Det er uttrykkelig skilt fra vedtatte krav og implementert funksjonalitet. | Gi et håndkontrollerbart grunnlag for å velge regler, rangering og forventet oppførsel før PRD. | [Demoscenarioet](demoscenario-fravaer.md) er skrevet av Codex etter Odins beskjed om å fortsette. Regeltall og rangering er foreløpige forslag, ikke nye beslutninger på vegne av Odin eller gruppen. |

## 06.10.26 – mellomlederen styrer prioriteringen

| ID | Hva ble endret? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E15 | Hovedbriefens åpne rangering og scenarioets forslag om færrest uketimer er videreført til lederstyrt valg og prioritering blant definerte sorteringskriterier. Valget skal være synlig og styre rekkefølge og forklaring, uten å endre regelstatus eller planen. Suksesskriteriene dekker bytte av prioritering og synlig manglende sorteringsgrunnlag. | La mellomlederen vektlegge hensyn som er viktige i situasjonen, samtidig som regelkontrollen ligger fast. | Odin ønsket at mellomlederen skal kunne styre og sortere etter hva som er viktig for dem. Synlig valgt kriterium og håndtering av manglende sorteringsdata er Codex sine presiseringer. [Eksemplet](demoscenario-fravaer.md) viser to mulige valg, P1 uketimer og P2 andel av avtalte timer; kriterieutvalg, beregningsmåter og avtaleverdier er fortsatt forslag. Bygger videre på E07 og E14. |

## 06.10.26 – informasjon og kontekst til lederens valg

| ID | Hva ble endret? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E16 | Sammendrag, løsning, differensiering og suksesskriterier presiserer verktøyet som beslutningsstøtte. Lederen kan velge en lavere rangert kandidat, få KI-veiledning og se konsekvenser før bekreftelse. Resultatet beskrives som en sammenligning med kontekst fremfor et pålagt førstevalg. Regelkontroll, sortering og lederbeslutning skilles. | Lederen skal kunne vektlegge egne hensyn og forstå implikasjonene av valget; verktøyet skal informere og gi kontekst. | Odin presiserte verktøyets rolle og lederens handlingsrom 06.10.26. Faste veiledningshandlinger og eksempel på valg av A03 er konkretiseringer fra Codex. Viderefører E15 og arbeidet med faste svar i E04–E05. |
| E17 | Kravet «godkjent forslag bryter ingen regler» er presisert til at ingen kandidat feilaktig merkes som å oppfylle reglene. Hvordan lederbekreftelse ved regelavvik håndteres står åpent. [Demoscenarioet](demoscenario-fravaer.md#åpent-valg--bekreftelse-ved-regelavvik) beskriver A: sperre ved avvik, og B: bekreftelse med advarsel og registrert begrunnelse. Kandidater med avvik skal fortsatt kunne undersøkes. | Unngå å blande kontrollresultatet med lederens beslutning, og synliggjøre et viktig produktvalg uten å avgjøre det på forhånd. | Odin valgte å avgjøre dette senere og ba om at begge mulighetene beskrives. Ingen modell for bekreftelse ved avvik eller manglende kontrolldata er valgt. Dette justerer E07 og E09 uten å svekke kravet om korrekte kontrollresultater. |

## 06.10.26 – helhetsoversikt og lederens beslutningsmyndighet

| ID | Hva ble endret? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E18 | Executive Summary tydeliggjør produktprinsippet: KI skal styrke lederens oversikt over muligheter, vurderingspunkter og konsekvenser, mens lederen beholder beslutningsmyndigheten. The Solution presiserer synlige avveininger, uavklarte forhold og begrensninger i datagrunnlaget. Det eksisterende forståelseskriteriet utvides med hva som må avklares og virkningen på øvrig plan. | Odin fremhevet at verdien av KI-støtten ligger i å gjøre det enklere for mellomlederen å se helheten og ta en informert beslutning. | Odins innspill i BMAD-samtalen 06.10.26, formulert inn i briefen av Codex. Testkriteriet og presiseringen om begrenset datagrunnlag er KI-konkretiseringer. Viderefører E16; ingen felles godkjenning av detaljene er registrert. Omfanget av omfordeling og bekreftelse ved regelavvik i E17 står fortsatt åpne. |

## 07.10.26 – forslag fra syntetiske data og endringer i datakilden

**Senere rettelser:** E21 inneholder Codex sin for brede tolkning av et svar
om demogrunnlag. Fjerningen av plangenerering er korrigert i E24; omtalen av
syntetiske data som et uttrykkelig produktvalg er korrigert i
[E26](#071026--demodata-og-presis-loggføring). E21 bevares som historikk,
ikke som dokumentasjon på at Odin vedtok disse avgrensningene.

Innslagene bygger på Odins videre avklaringer i BMAD-samtalen 07.10.26, samt
presiseringen om logging fra 06.10.26. De oppdaterer arbeidsutkastet, ikke en
felles godkjenning av detaljert omfang. Tidligere innslag beholdes som historikk.

| ID | Hva endres, fra og til? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E19 | Sammendrag og løsning konkretiserer «helhetsoversikt» fra et bredt mål om å forstå eget valg til tilgjengelig informasjon om konflikter, arbeidstid, hvile og interne føringer. Lederstyrt søkeomfang i innstillinger legges til. Manglende data skal forklares, men ansvar for å forbedre grunnlaget står åpent. | Følge Odins beskrivelse av hvilken informasjon som skal støtte lederen, og ønsket om å kunne styre hvor langt appen leter. Odin uttrykte usikkerhet om mellomlederens ansvar for datagrunnlaget. | Odins innspill 07.10.26, viderefører E15–E18. Synlig regelkilde, synlig søkeomfang og skillet mellom søkeinnstilling og regelkontroll er Codex sine konkretiseringer. Søkemåter, grenser, standardvalg og faktiske lov- og avtaleregler er ikke vedtatt. |
| E20 | Løsning, suksesskriterier, Scope og Vision går fra godkjenning og vaktendring i VaktMatch til forslag og vurderinger av mottatte data. Gjennomføring av foreslåtte vaktendringer legges utenfor v1. Oppdatert datagrunnlag kan gi en ny vurdering; reell leverandørtilkobling er en fremtidig mulighet. | Odin beskrev at endringer kan gjøres i et annet bemanningssystem og observeres i datasettet. Prosjektet skal kunne demonstrere ideen uten avhengighet av leverandørtilgang. | Odins arbeidsretning 07.10.26. Endrer E06, E08 og bekreftelsesflyten omtalt i E16–E17. Quinyx er Odins eksempel, ikke en undersøkt eller valgt integrasjon. Skillet mellom forslag og observert endring, og at endringen ikke beviser hvem eller hvorfor, er KI-presiseringer. Oppdateringsmekanismen er åpen. |
| E21 | Executive Summary og Scope erstatter enkel plangenerering med en ferdig syntetisk vaktplan. Kravene om generering og godkjenning av grunnplanen tas ut av løsningen og suksesskriteriene; plangenerering legges utenfor MVP. | Konsentrere demonstrasjonen om beslutningsstøtten fra et eksisterende datagrunnlag. Codex anbefalte dette alternativet; Odin valgte det uttrykkelig. | Odins svar «Ferdig syntetisk vaktplan (anbefalt)» 07.10.26. Dette er en ny individuell arbeidsretning som endrer E06 og E08. Det tidligere bidraget fra Stians turnusgenerator-idé og begrunnelsene bevares i vedlegget og historikken. Ingen ny felles godkjenning utledes. |
| E22 | Løsningen skiller beslutningslogg og begrunnelseskrav fra regelkontroll og fra selve vaktendringen. Begge står som åpne produktvalg med ønsket om avslagbar funksjonalitet når den bare følger interne retningslinjer. Forståelses- og tidsbrukstesting flyttes fra listen over hovedkriterier til et uttrykkelig valgfritt KI-forslag. | Unngå å gjøre beslutningsstøtte til et automatisk krav om at lederen må forklare seg, eller å gjøre et ekstra testforslag til et dokumentert leveransekrav. | Odins presisering 06.10.26 gjaldt lagring og begrunnelsesplikt, ikke regeloverstyring; korrigerer den tidligere assistenttolkningen og nyanserer E17–E18. Omfang og standardinnstillinger er uavklart, og eventuelle lovkrav er ikke fastslått. Omplasseringen av brukertesten er Codex sin korrigering etter Odins spørsmål, støttet av [faglærerens råd](../tilbakemelding-product-brief.md); det er ikke et nytt brukerkrav. |
| E23 | Metadata oppdateres til 07.10.26, README viser den nye arbeidsretningen og lenker til demoscenarioet. Demoen erstatter bekreftelse som utfører en endring med undersøkelse av forslag; gammel A/B-modell merkes som historikk. Vedlegget får datakildeinnspillet og gjeldende avgrensning, og lenken merket endringslogg rettes fra skjult logg til denne lesbare loggen. | Holde inngang, brief og eksempel konsistente og bevare sporbarheten uten å slette tidligere forslag. | Skrevet av Codex som følge av E19–E22. D1/D2, stabile ID-er, synlig dataversjon, kodebasert sammenligning og kontrolltilfeller er KI-forslag i [demoscenarioet](demoscenario-fravaer.md#forslag-til-demonstrasjon-av-oppdaterte-data), ikke ferdige datasett eller vedtatte tekniske løsninger. Selve metadata- og lenkerettelsene endrer ikke produktinnholdet. |

## 07.10.26 – korrigering: plangenerering beholdes som forslag

| ID | Hva endres, fra og til? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E24 | Executive Summary, The Solution og Scope gjeninnfører enkel plangenerering som et separat forslag. «Plangenerering utenfor MVP» erstattes med at innføring av forslaget i faktisk vaktliste er utenfor. Suksesskriteriene dekker regelkontroll, synlig udekket behov, uendret faktisk vaktliste og generering uten KI-nøkkel. README, demoscenario og vedlegg er rettet tilsvarende. | Ferdig syntetisk datagrunnlag utelukker ikke generering. Codex tolket det tidligere svaret for bredt og fjernet funksjonalitet Odin fortsatt ønsker. | Odins uttrykkelige korrigering i BMAD-samtalen 07.10.26. Korrigerer E21 og tilhørende formuleringer i E23; disse innslagene bevares som historikk. E21 skal ikke leses som gjeldende beslutning om å fjerne generering. Skillet mellom forslag og innføring følger Odin; separat visning og testkriteriene er Codex sine konkretiseringer, med videreføring av tidligere regelbasert generering og drift uten nøkkel. Omfanget av generering og hvilke tildelinger som kan endres, er fortsatt åpent. Dette er Odins arbeidsretning, ikke ny felles godkjenning. |

## 07.10.26 – publisering som grunnlag for felles vurdering

| ID | Hva endres, fra og til? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E25 | Briefens innledning går fra generelt forbehold om manglende felles godkjenning til uttrykkelig status: endringene 06.–07.10.26 er ikke avklart med Stian og publiseres som Odins innspill til felles vurdering. README får samme status og lenke til den samlede begrunnelsen øverst i denne loggen. | Gjøre opphav, hensikt og beslutningsstatus tydelig for den som leser endringene etter publisering. | Odin opplyste dette og ba om push 07.10.26. Sammendraget er skrevet av Codex fra allerede dokumenterte prosjektbegrunnelser. Produktinnholdet er uendret i denne presiseringen; publisering er ikke felles godkjenning. |

## 07.10.26 – demodata og presis loggføring

| ID | Hva endres, fra og til? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E26 | Briefens innledning, Executive Summary, The Solution, Who This Serves og Scope går fra gjentatte formuleringer om en «ferdig syntetisk vaktplan» som føring til demodata som praktisk grunnlag. Scope forklarer én gang at dataene er fiktive. Prosesshistorikken om feiltolkningen tas ut av Scope og beholdes her og i memlog. README, demo, vedlegg og sammendraget øverst i denne loggen får samme språk. | Odin påpekte at omtalen av syntetiske data som et uttrykkelig valg var for sterk. Codex hadde tillagt svaret større betydning enn det ga grunnlag for. | Kilde: Odins oppfølging av memlog-gjennomgangen i samtalen 07.10.26. Skrevet av Codex. Korrigerer tilskrivingen i E21 og nyanserer E24; ingen ny funksjonalitet eller felles beslutning. Demoen har fortsatt fiktive data, plangenerering beholdes, og reelle persondata og integrasjoner er fortsatt utenfor førsteversjonen. Produktfunksjonene er uendret. |

Samme gjennomgang oppdaterer [føringsreglene](../AGENTS.md#føring-og-lesing-av-memlog)
og presiserer opphav og loggplassering i fire memlogger. Eldre innslag bevares
uten konstruerte datoer eller forfattere; eldre formuleringer finnes også i Git-historikken.

## 07.10.26 – kortere innledning og tydeligere åpne valg

| ID | Hva endres, fra og til? | Enkel begrunnelse | Grunnlag og status |
|---|---|---|---|
| E27 | Briefens innledning og valgfrie brukertest kortes ned. Den samlede listen over åpne valg deles i seks temaer med konkrete spørsmål. Forklaringen om loggvedlikehold over kortes ned; E01–E26 beholdes. | Gjøre produktet lettere å finne og vise hva som må avklares før planlegging. | Odin ba 07.10.26 om nødvendige endringer etter gjennomgangen av ukommitterte filer. Redigert av Codex. Produktinnhold og beslutningsstatus er uendret; ingen åpne valg er avgjort. |

## Se alle tekstendringer

Git bevarer hver versjon. Kjør fra repoets rot for å se alle forskjeller mellom
første versjon og dagens arbeidskopi, også endringer som ennå ikke er committet:

```powershell
git diff 587bc45893f56a2f6ce81e4fa7d7b5e447064bc7 -- productbrief.md
```

For å følge hver lagrede endring i rekkefølge:

```powershell
git log --reverse --format=fuller -p -- productbrief.md
```

[Filhistorikken på GitHub](https://github.com/IBE160-2026/G10-andreassen-lundberg/commits/main/productbrief.md)
viser publiserte commits. Lokale endringer blir synlige der etter commit og push.
Den lesbare loggen forklarer valg; Git-diffen viser også hver mindre ordlydsendring.

## Slik føres neste endring

Legg til et nytt datert innslag med neste ID og følgende innhold:

| ID | Hva endres, fra og til? | Hvorfor? | Grunnlag og status |
|---|---|---|---|
| E28 | Berørt del og kort før/etter-beskrivelse. | Én eller to enkle setninger. | Hvem ga innspillet, kilde og om det er forslag, arbeidsretning eller felles beslutning. |

E28-raden er en mal, ikke et tatt valg. Rene språk- og lenkerettelser kan samles
i ett innslag med beskjed om at produktinnholdet er uendret. Et omgjort valg får
et nytt innslag som viser til det gamle. Ikke skriv om tidligere begrunnelser
slik at de fremstår som kjent da valget ble tatt. Bruk «begrunnelse ikke dokumentert»
dersom kildene ikke forklarer et eldre valg, og marker senere vurderinger særskilt.
