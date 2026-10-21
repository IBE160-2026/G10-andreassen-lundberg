# Forslag ved frafall – søk, låste vakter og resultat

*Avklart produktretning: 22.10.26. Konkretisert av Codex fra Odins tilslutning
til anbefalingene i [SCRUM-16](https://stiodi.atlassian.net/browse/SCRUM-16).
Dette beskriver planlagt oppførsel; funksjonene og målingene er ikke implementert.*

[Produktbriefen](../productbrief.md) viser omfanget. [Demoscenarioet](demoscenario-fravaer.md)
definerer R1–R5, P1/P2, historikk og tilbudssimulering. Uke 1–4 er historikk;
uke 5 er ferdig planlagt og er arbeidsuken. Lederen sammenligner alternativer
ved frafall og bestemmer selv. Tidligere planer vises som kontekst.

## Nivåer

| Del | Førsteversjon | Mulig videreutvikling |
|---|---|---|
| Beskyttelse av planen | Historikk, gjennomførte/påbegynte vakter og lederlåste tildelinger ligger fast. | Mer detaljert styring av hva som kan foreslås endret. |
| Søkeomfang | Direkte erstatning og opptil én flytting; grense 1 er standard, 0 kan velges. | To flyttinger etter vurdert kompleksitet og målt responstid; flere vurderes senere. |
| Metode | Avgrenset regelbasert søk med samme R1–R5 for alle alternativer. | Solver dersom større søkeomfang eller flere hensyn gjør den nyttig. |
| Sammenligning | Flere kontrollerte forslag, P1/P2, konsekvenser og synlig historikk. | Nye kriterier krever egen avklaring. |
| Tilbud/svar | Simulering av sendt, ventende, akseptert og avslått; enkelt eksempel kan hoppe over steget. | Reell utsending/aksept er utenfor MVP. |
| Resultat | Dekning, kontrollstatus og søkestatus vises hver for seg. | Solverstatuser defineres hvis solver velges senere. |

## Hva ligger fast?

Søket bruker et synlig vurderingstidspunkt fra demodataene. Det følger demoens
tid, ikke maskinens kalender. I hovedeksemplet kan dette være 14.10.2026 kl. 07.00
i Europe/Oslo, før målskiftet starter kl. 08.00.

Historikk og vakter som har startet ved vurderingstidspunktet, foreslås ikke
flyttet. Lederen kan i tillegg låse framtidige tildelinger. Bare framtidige,
ulåste tildelinger i uke 5 kan inngå i intern omfordeling. Andre tildelinger
ligger fast i det aktuelle forslaget. Vakttider, varighet og bemanningskrav endres
ikke av søket; vakter deles ikke opp i førsteversjonen.

Fraværet vises som udekket behov på målskiftet selv om det opprinnelig hadde en
tildeling. Den fraværende regnes ikke som tilgjengelig bemanning. Dette betyr
ikke at en lås eller den eksisterende planen skal skjule fraværet. Søket
undersøker erstatning for den manglende bemanningen; en eventuell annen låst
tildeling på samme vakt beholdes. Dersom selve målskiftet allerede har startet,
er dette utenfor førsteversjonens søk; vis behovet og begrensningen.

Låsing er en søkebegrensning, ikke en bekreftelse på at en tildeling består
reglene. Regelavvik i grunnlaget skal fortsatt vises.
Lederlåser knyttes til tildeling og dataversjon. Endring av en lås gjør tidligere
søkeresultat utdatert og krever ny vurdering; tidligere simulerte svar gjelder
ikke automatisk et forslag under de nye søkebegrensningene. Ved datasettbytte
lastes låsene fra det nye grunnlaget, og forskjeller fra forrige versjon vises.
Øktens tidligere lederlåser beholdes som historikk på gammel dataversjon og
overføres ikke skjult. Gjeldende låser skal være synlige før et nytt søk.

## Hvordan finner vi forslag?

Førsteversjonen undersøker én fraværshendelse og én manglende bemanningsplass
om gangen, med én hel vakt per tildeling:

1. Undersøk hver person i det oppgitte kandidatsettet som direkte erstatter.
2. Ved grense 1: undersøk også kombinasjoner der B flyttes fra én eksisterende,
   framtidig, ulåst tildeling Y til fraværsvakten X, og C dekker plassen B forlater.
   X og Y er ulike vakter, og B og C er ulike personer. C overtar Y uten at en
   annen eksisterende tildeling må flyttes; ellers overskrides denne flyttegrensen.
3. Bygg en separat hypotetisk sluttplan. Fjern den flyttede tildelingen og legg
   inn de nye før kollisjon, hvile og timer beregnes for alle berørte. Den
   fraværendes opprinnelige tildeling på X beholdes som kildehistorikk med
   fraværsmarkering, men er ikke aktiv bemanning eller arbeid i sluttplanens
   dekning, kollisjoner eller arbeidstidsberegning. Fraværstid vises separat;
   lønn eller øvrig behandling av sykefravær modelleres ikke her.
4. Kontroller vaktenes kompetansekrav og tidsrom, tilgjengelighet, R1–R5,
   bemanningsdekning, låser og flyttegrense. Behold øvrige tildelinger uendret.
5. Sammenlign de komplette, beståtte forslagene etter lederens P1/P2. Antall
   flyttinger og berørte ansatte vises som konsekvenser, uten skjult tilleggspoeng.

Ved fullført søk er alle kombinasjoner i dette avgrensede kandidatsettet og
søkeomfanget undersøkt; bare samme sluttplan kan slås sammen som duplikat.
Det er ikke det samme som å ha undersøkt alle tenkelige omplanlegginger.
Metoden velges fordi omfanget er avgrenset og kontrollene kan etterprøves direkte.
Vi trenger foreløpig ikke å optimalisere en hel periodeplan eller innføre et
eget samlet mål. Faktisk ytelse må måles; det er ikke dokumentert at den er rask nok.

Regelavvik og uavklarte alternativer kan fortsatt undersøkes, men inngår ikke
i rangeringen av beståtte forslag. Historikk erstatter ikke aktuelle kontrolldata.
Hvis B kan flyttes til X, men ingen C bekreftes å kunne dekke Y, beholdes også
et separat konsekvensalternativ med B på X og Y udekket. Vis hvorfor full dekning
ikke er bekreftet, inkludert manglende data der det er relevant. Alternativet
inngår ikke i rangeringen av komplette løsninger eller som et fullt akseptert
løsningsforslag. Det viser virkningen av flyttingen; det utføres ingen endring.

## Hva betyr resultatet?

| Dimensjon | Tilstand | Betydning |
|---|---|---|
| Dekning | Full | Manglende plass på X og eventuelle berørte plasser på Y er dekket uten å skape nye hull. |
| Dekning | Delvis/udekket | Vis nøyaktig hvilke vakter og hvor mange plasser som fortsatt mangler. Ikke presenter forslaget som en komplett løsning. |
| Kontroll | Bestått | Alle nødvendige kontroller for det viste forslaget er bestått. |
| Kontroll | Regelavvik | Minst ett kjent brudd vises med regel, verdi og konsekvens. |
| Kontroll | Uavklart | Nødvendige opplysninger mangler; si hvilke kontroller det hindrer. Kjent brudd vises selv om annet grunnlag mangler. |
| Søk | Fullført | Alle kombinasjoner innenfor oppgitt kandidatsett og søkegrense er undersøkt. |
| Søk | Avbrutt/feilet | Undersøkelsen ble ikke fullført; vis dette selv om noen kontrollerte forslag allerede finnes. |
| Søk | Ikke kjørt – utenfor omfang | Målskiftet har allerede startet, eller forespørselen er utenfor definert omfang. Vis årsak og udekket behov; ikke framstill dette som et søk uten funn. |

For én manglende plass er målet enten dekket eller udekket. «Delvis» kan for
eksempel bety at X er dekket, men at Y er blitt udekket. Slike alternativer vises
med konsekvensen og rangeres ikke som komplette løsninger. Andre hull som fantes
før søket, må fortsatt være synlige og kan ikke sies å være løst av dette forslaget.

Et fullført søk uten beståtte forslag gir «Ingen kontrollerte alternativer funnet
innenfor valgt søkeomfang». Ved manglende kontrolldata vises også uavklarte
alternativer; ingen garanti om umulighet gis. Et avbrudd gir aldri konklusjonen
«ingen løsning finnes». Beståtte forslag funnet før avbruddet kan vises, men
rangeringen gjelder bare de undersøkte forslagene og merkes som ufullstendig.

Solver brukes ikke i førsteversjonen. «Optimal» og «bevist uløselig» er derfor
ikke produktpåstander. Ved senere solvervalg må betydningen av disse statusene
og tidsgrenser defineres mot den konkrete modellen.

## Hvordan vurderer vi tidsbruk?

Mål søket fra forespørselen mottas til kontrollert resultat er klart, uten
språkmodellkall. Mål brukerens totale ventetid separat. Registrer dataversjon,
antall kandidater/vakter, søkegrense, undersøkte kombinasjoner, maskin og
programversjon. Kjør samme representative tilfeller gjentatte ganger, med
både oppvarming og målte kjøringer angitt, og rapporter median, p95 og antall
avbrudd/feil. Sammenlign grense 0 og 1 på samme grunnlag. En mulig utvidelse
til 2 må få tilsvarende målinger og test av resultatkvalitet før den tas inn.
Ingen konkret responstidsgrense eller utført måling påstås nå.

## Kontrolltilfeller for senere implementering

| Tilfelle | Forventning |
|---|---|
| Låst Y eller allerede påbegynt Y | B flyttes ikke fra Y. Framtidig ulåst Y kan undersøkes ved grense 1. |
| Datoen på maskinen endres | Samme demo og vurderingstidspunkt gir samme tidsmessige søkegrense. |
| Vurderingstidspunkt lik målskiftets start | Skiftet regnes som påbegynt; søket har status «Ikke kjørt – utenfor omfang», og behovet vises. |
| Lås endres eller nytt datasett lastes | Vis gjeldende låser og forskjeller. Gamle forslag og svar er historiske fram til ny vurdering; låser fra gammel dataversjon arves ikke skjult. |
| X var tildelt en fraværende | Fraværet er synlig som behov; personen teller ikke som dekning. |
| C kan ikke dekke Y | X-dekning alene er ikke en komplett løsning; Y vises som udekket. |
| Fullført søk, komplette data, ingen beståtte | Ingen funn innenfor kandidatsett/søkegrense, uten påstand om større søkeomfang. |
| Manglende tilgjengelighet for en mulig kandidat | Alternativet er uavklart; øvrige kontrollerte forslag kan fortsatt vises. |
| Avbrudd før eller etter et bestått funn | Vis avbruddet; eventuelle funn og rangering merkes som ufullstendig søk. |
| To forslag med lik P1/P2, ulikt antall berørte | Lik rangering beholdes; forskjellen vises som kontekst og lederen velger. |

## Faglig bakgrunn

Låsing og minst mulig forstyrrelse er dokumenterte mekanismer i
[Timefolds omplanlegging](https://docs.timefold.ai/employee-shift-scheduling/1.34.x/real-time-planning).
[Quinyx beskriver tilbud og ansattes bekreftelse](https://help.quinyx.com/help-centre/docs/manager-functionality).
[OR-Tools skiller funnet løsning, bevist uløselig modell og uavklart søk](https://developers.google.com/optimization/cp/cp_solver/).
Dette er eksempler som støtter begrepene, ikke valgte avhengigheter eller bevis
for ytelsen i vår løsning. Nivådelingen og den konkrete søkemetoden er Codex sin
tilpasning til prosjektets avgrensning, etter Odins tilslutning til anbefalingene.
