---
title: 'VaktMatch: brukerbehov og PRD-grunnlag'
type: user-voice
topic: 'VaktMatch brukerbehov og PRD-grunnlag'
decision: 'Hvilke behov, avgrensninger og spørsmål bør tas med til PRD-arbeidet?'
source: native-web-research
status: complete
preset: quick
validation: normal
created: '2026-10-26'
updated: '2026-10-26'
claims_verified: 2
claims_unverified: 3
---

# VaktMatch: brukerbehov og PRD-grunnlag

Research utført av Codex. Kildegrunnlag for diskusjon; anbefalinger er KI-vurderinger, ikke nye produktbeslutninger.

## Hva researchen gir oss

**Anbefaling til diskusjon:** Behold den avgrensede fraværssituasjonen som arbeidsgrunnlag, og prioriter en forståelig sammenligning av kandidater og konsekvenser. Behov for kompetanseoversikt har støtte i flere nordiske helsetjenestestudier. Dette gir et saklig problemgrunnlag, men validerer ikke vår generiske målgruppe eller forventet tidsbesparelse. [4][6]

Etablerte løsninger dokumenterer allerede vikarsøk, sammenligningsinformasjon eller kompetansestøtte. Vi har derfor ikke grunnlag for å hevde at kombinasjonen er unik. KI-tekst har heller ingen påvist merverdi i vår oppgave; sammenligning med standardtekst bør komme før modellvalg. [7][8][9][1][2]

**Viktigste kunnskapshull:** Vi har ikke undersøkt hvordan en faktisk målbruker håndterer fravær, hvilke opplysninger vedkommende mangler, eller om KI-forklaringen gjør vurderingen lettere. Rapporten er forberedelse til PRD, ikke en ferdig kravspesifikasjon.

## Avgrensning og bevisstyrke

Én kort innsamlingsrunde med tre spor, inntil to samtidige researchassistenter og høyst fem nye kilder per spor. Elleve kilder er brukt: tre om brukerbehov, fem leverandørsider og tre om forklaringer. Arbeidsgrunnlag, kildeutdrag og kontroll finnes i [brief.md](brief.md) og `digests/`. Prosjektets dokumenter har styrt spørsmålene og er ikke brukt som eksternt bevis.

**Verified** betyr at en snever syntese er støttet av uavhengige kilder; sikkerheten ved overføring til vårt produkt kan fortsatt være middels. **Unverified** betyr at uavhengig bekreftelse mangler, selv om kildegjengivelsen er kontrollert. Leverandørfunksjoner er dokumenterte egenbeskrivelser og ikke testet. Historiske studier beholdes som historiske; de beskriver ikke automatisk situasjonen i 2026.

## Brukerbehov: se både kandidaten og følgene for vaktlaget

En norsk undersøkelse av førstelinjeledere i sykehjem, hjemmesykepleie og somatiske sykehusavdelinger beskriver vansker med å skaffe ekstravakter med samme kompetanse ved korttidsfravær. Det støtter kompetanse som et relevant spørsmål å undersøke. Undersøkelsen fra 2022 validerer ikke dagens behov eller utbredelsen i andre bransjer. **Middels sikkerhet for overføring; historisk og avgrenset utvalg.** [4]

I en svensk kvalitativ studie beskrev ledere og bemanningsassistenter nytte av oversikt over arbeidstid på tvers av avdelinger, overtid og vaktlagets kompetanse. En flytting kunne samtidig skape et nytt bemanningshull. Studien peker også på uklare varsler og avveininger mellom ønsker og restitusjon. Dette er deltakerbeskrivelser, ikke mål på hvor vanlige problemene er. **Middels sikkerhet, enkeltstudie.** [6]

En finsk før/etter-studie fant færre lederoppgaver og ubemannede vakter etter innføring av IT-støtte. Bare artikkelens abstract er lest, og studien hadde ingen kontrollgruppe. **Middels sikkerhet for den rapporterte sammenhengen; lav for kausalitet og overføring til vår demo.** Vi kan undersøke koordinering som problem, men ikke love en bestemt tidsbesparelse. [5]

**KI-vurdering til PRD-diskusjonen:** Beskriv problemet som å få tilstrekkelig oversikt til å vurdere erstatningsalternativer. Skill mellom at en person er ledig, har riktig kompetanse, oppfyller de kontrollerte reglene og faktisk har takket ja. De siste detaljene er våre designspørsmål; kildene avgjør ikke skjermbildet, sorteringskriteriene eller MVP-omfanget.

## Lignende løsninger: dokumentert overlapp, åpne detaljer

| Løsning | Dette beskriver kildene | Dette er fortsatt uavklart |
|---|---|---|
| Simployer/Capitech | «Finn vikar» søker tilgjengelige ansatte; behov kan publiseres for interesse. En annen hjelpeside beskriver beregnet kostnad for ulike tilgjengelige vikarer. [7][8] | Hvilke regler vikarsøket anvender, hvordan kandidatene sorteres, og detaljert begrunnelse. Kildene er udaterte; kostnadssidens URL indikerer redigering. |
| Quinyx | Hjelpesenteret beskriver kompetansesortering og varsler som navngir manglende ferdigheter. Markedsføringen beskriver ny beregning av dekning ved fravær og andre akutte endringer. [9][10] | Samlet rangering, nøyaktige regelvalg og presentasjon av flere forklarte omfordelingsalternativer er ikke verifisert. |
| 4human | Produktsiden beskriver arbeidsplanendringer og fraværsvarsler sammen med time-/fraværsmodulen. [11] | Siden avklarer ikke erstatningsforslag, kandidatkontroll, rangering eller forklaring. |

**Alle funksjonspåstander: middels / unverified.** Vi har lest leverandørsidene, ikke prøvd produktene. For Quinyx Skills er oppdateringsdato innen tre måneder; de andre sidene mangler sikker datering. Manglende dokumentasjon er ikke bevis på manglende funksjoner. Dette utdyper [undersøkelsen fra september](../competitive-simployer-quinyx-4human-akutt-bemannings-2026-09-07/research.md); dens funn er ikke brukt som nytt bevis.

**KI-vurdering til brief/PRD:** Beskriv VaktMatch som en avgrenset studieprototype som gjør alternativer og konsekvenser etterprøvbare. En påstand om bedre oversikt eller forståelse må fortsatt testes. Kostnadssammenligning hos en leverandør er inspirasjon, ikke et vedtak om å utvide MVP.

## KI-forklaringer: nytte må undersøkes

**Middels sikkerhet, enkeltstudie:** Bansal mfl. fant ingen statistisk signifikant økning i beslutningsnøyaktighet med forklaringer sammenlignet med KI-råd og et anslag for hvor sikkert rådet var. Aksepten av rådene økte også når rådene var feil. Oppgavene var tekstanalyse og logikk, ikke bemanningsvalg. Studien avgjør ikke om forklaringer kan spare tid eller hjelpe VaktMatch-brukere. [1]

Et annet eksperiment fant mindre overavhengighet når deltakerne måtte vurdere rådene mer aktivt, men de mest effektive utformingene fikk svakere subjektive vurderinger. Dette var en ernæringsoppgave med 199 nettbaserte deltakere. Tilfredshet alene blir derfor et svakt grunnlag for å hevde bedre beslutningsstøtte; overføring til vår målgruppe er fortsatt en hypotese. **Middels sikkerhet, enkeltstudie.** [2]

Jacovi og Goldberg skiller mellom en overbevisende forklaring og en forklaring som gjengir beslutningsgrunnlaget riktig. Arbeidet er et metodeargument om modellfortolkning, ikke en effektstudie. **Middels sikkerhet; anvendelsen nedenfor er vår vurdering.** [3]

**KI-vurdering til PRD-diskusjonen:** Sammenlign standardtekst og KI-tekst på samme scenario. Kontroller først at teksten gjengir regelresultat, rangering og manglende data riktig. Undersøk deretter om leseren forstår avveiningen, oppdager feil og bruker mindre tid. En flytende tekst er ikke alene et mål på merverdi. Dette er et forslag til evaluering, ikke vedtatte akseptansekriterier.

## Hva sporene betyr sammen

**KI-syntese:** Brukerbehovene peker mot forståelig oversikt, mens konkurrentene viser at deler av denne støtten allerede finnes. Forklaringsstudiene gir samtidig grunn til å måle om brukeren forstår grunnlaget, fremfor å bruke tillit eller pen tekst som eneste suksessmål. Dette er en begrunnelse for å konkretisere og teste den planlagte sammenligningen, ikke for flere funksjoner. [4][6][8][9][1][2]

Motvektene er vesentlige: programvare skaper ikke tilgjengelig kompetanse; flytting kan bare forskyve problemet; mer krevende kontroll kan oppleves mindre brukervennlig. Den finske studien viser et forbedringsforløp, men kan ikke isolere programvarens effekt. Kildene gir dermed både støtte til å undersøke problemet og grenser for hva vi kan love. [4][6][2][5]

## Forslag å vurdere før PRD-en

Dette er Codex sine anbefalinger, ikke vedtatte krav.

| Forslag | Hvorfor og sikkerhet | Bruk i videre arbeid |
|---|---|---|
| Konkretiser én målbruker og én fraværshendelse. | Kompetansebehov støttes av uavhengige studier, men i helsetjenesten; overføring til andre arbeidsplasser er uavklart. [4][6] | Brief: problem/målgruppe. PRD: scenario og antakelser. |
| La demoen vise både kandidatens grunnlag og følger for andre vakter. | Direkte støtte i én kvalitativ studie; middels sikkerhet, ikke ny målgruppevalidering. [6] | PRD: tydeliggjør eksisterende sammenligning og konsekvensvisning. |
| Beskriv alternativer uten en udokumentert unikhetspåstand. | Konkret funksjonsoverlapp i leverandørdokumentasjon; faktisk bruk er ikke uavhengig kontrollert. [7][8][9] | Brief: alternativer/differensiering. Ingen produktbrief endres i denne runden. |
| Formuler hva KI-teksten skal gjøre bedre enn standardteksten. | Uavhengige eksperimenter støtter behov for flere kvalitetsmål; produktspesifikk nytte er ukjent. [1][2][3] | PRD: KI-oppgave og evalueringsforslag; SCRUM-59 når oppgaven er konkret. |

## Spørsmål til diskusjon

1. Hvilken type skiftleder skal det første scenarioet være troverdig for? Helsetjenestefunn gjør ikke automatisk helsetjenesten til valgt målgruppe.
2. Hva trenger lederen å forstå når to kandidater begge oppfyller reglene, men konsekvensene er ulike?
3. Hvilke opplysninger kan være utdaterte eller mangle, og hvordan skal lederen se hvilken vurdering det hindrer?
4. Kan vi vise en situasjon der KI-teksten hjelper mer enn standardteksten, uten å legge til udokumenterte fakta?
5. Hvilke antakelser er tilstrekkelig tydelige for en studieprototype, og hvilke ønsker vi å undersøke med en målbruker?

Egne målgruppeintervjuer, leverandørdemoer, fulltekst til den finske studien og nyere oppgavespesifikk KI-forskning er mulige videre undersøkelser. Ingen av dem gjennomføres eller gjøres obligatoriske her. Runden stopper ved avtalt én-rundesgrense; konkurransesporet brukte hele femkildersrammen. Spørsmålene over står fortsatt åpne.

## Kilder

| Nr. | Støtter | Utgiver og kilde | Publisert | Besøkt | Sikkerhet |
|---|---|---|---|---|---|
| [1] | Forklaring og beslutningsnøyaktighet i avgrensede eksperimenter | [Bansal mfl., ACM CHI / University of Washington](https://aiweb.cs.washington.edu/ai/pubs/bansal-chi21.pdf) | 2021-05 | 2026-10-26 | Middels; historisk, annen målgruppe |
| [2] | Aktiv vurdering, overavhengighet og subjektive vurderinger | [Buçinca mfl., ACM CSCW / Harvard](https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf) | 2021-04 | 2026-10-26 | Middels; historisk, annen oppgave |
| [3] | Skillet mellom plausibilitet og trofasthet | [Jacovi og Goldberg, ACL](https://aclanthology.org/2020.acl-main.386.pdf) | 2020-07 | 2026-10-26 | Middels; metodeargument |
| [4] | Kompetanseutfordringer ved korttidsfravær i et norsk utvalg | [Agenda Kaupang for Norsk Sykepleierforbund, Førstelinjeledere i døgnkontinuerlige tjenester](https://www.nsf.no/sites/default/files/2022-10/R1021942%20NSF%20rapport_F%C3%B8rstelinjeledere%20i%20d%C3%B8gnkontinuerlige%20tjenester.pdf) | 2022-09-16 | 2026-10-26 | Middels; historisk utvalgsundersøkelse |
| [5] | Registrerte endringer etter IT-støtte i Finland | [Comparing the Two Techniques for Nursing Staff Rescheduling, Computers, Informatics, Nursing / PubMed](https://pubmed.ncbi.nlm.nih.gov/31652140/) | 2020-03 | 2026-10-26 | Middels; bare abstract lest |
| [6] | Informasjonsbehov og avveininger i svensk turnusplanlegging | [Managing Sustainable Working Hours, Journal of Nursing Management / Wiley](https://onlinelibrary.wiley.com/doi/10.1155/2023/8096034) | 2023-12-09 | 2026-10-26 | Middels; kvalitativ enkeltstudie |
| [7] | Vikarsøk og publisering av behov | [Capitech: Jobbe med vakter i operativ plan](https://help.capitech.no/nb/article/673d4f65-294e-4331-a061-1af71d63ebee) | Ukjent | 2026-10-26 | Middels; udaterte leverandørutsagn |
| [8] | Beregnet kostnad for vikaralternativer | [Capitech: Satser for kostnadsberegning](https://help.capitech.no/nb/article/satser-for-kostnadsberegning-forelopig-under-redigering) | Ukjent | 2026-10-26 | Middels; dato/status uavklart |
| [9] | Kompetansesortering og navngitte mangler | [Quinyx Help Centre: Skills](https://help.quinyx.com/help-centre/docs/skills) | 2026-07-29; oppdatert 2026-08-18 | 2026-10-26 | Middels; leverandørdokumentasjon |
| [10] | Leverandørpåstand om ny beregning ved akutte endringer | [Quinyx: Scheduling Automation](https://www.quinyx.com/workforce-management/scheduling-automation) | Ukjent | 2026-10-26 | Middels; markedsføring |
| [11] | Arbeidsplanendringer og fraværsvarsler | [4human: Arbeidsplan](https://4human.no/hrm/arbeidsplan/) | Ukjent | 2026-10-26 | Middels; produktbeskrivelse |

## Når bør funnene sjekkes igjen?

Datokontrollen er beregnet med `recon_kit.py staleness` fra [daterte registerpåstander](digests/claims-dated.json), med tre måneder som vindu for funksjoner. For Quinyx Skills brukes sidens dokumenterte oppdatering 18.08.2026; neste kontroll er **18.11.2026**. [9]

Capitech-sidene, Quinyx-markedsføringen og 4human-siden har ukjent publiseringsdato. De kan ikke gis en pålitelig aldersgrense og bør kontrolleres før de brukes til en påstand om dagens konkurransefortrinn. Besøksdatoen erstatter ikke publiseringsdatoen. [7][8][10][11]

De eldre studiene brukes som historiske funn og metodegrunnlag, uten et automatisk utløpsvindu. Dette er ikke en attest om at de beskriver dagens praksis: nyere eller lokal empiri trengs før påstander om nåværende utbredelse og produktets effekt. **Tidligste beregnbare kontroll er 18.11.2026; de udaterte funksjonspåstandene har kontrollbehov allerede ved videre bruk.**

## Kontroll og status

Kildereferansene er kontrollert maskinelt og innholdet kontrollert i en separat kildegjennomgang. To snevre synteser har uavhengig støtte; tre andre bærende påstander mangler uavhengig bekreftelse. Tallene kommer fra påstandsregisteret i [.memlog.md](.memlog.md), ikke fra en opptelling av alle setninger. «Verified» gjelder kildegrunnlaget, ikke produktets effekt.

Strukturkontrollen fant ingen vesentlige problemer. Språk- og kildekontrollen førte til presisering av konfidensinformasjon og av forskjellen mellom manglende statistisk signifikans og bevist null effekt. Se [kildekontroll](digests/citation-check.md) og [verifikasjon](digests/verification-r1.md). Rapporten er lokal og ikke committet eller pushet. Ingen produktbrief, PRD, Jira-sak eller personlige studienotater er endret i denne researchrunden.
