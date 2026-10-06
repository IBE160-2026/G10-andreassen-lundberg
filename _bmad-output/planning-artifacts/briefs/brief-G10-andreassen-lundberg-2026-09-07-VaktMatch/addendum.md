# Vedlegg: VaktMatch

**Dokumentrolle (presisert 06.10.26):** Supplerende bakgrunn til den gjeldende
[productbrief.md](../../../../productbrief.md), ikke en egen brief. Innholdet
fra 17.09.26 bevarer innspill og åpne spørsmål; det vedtar ikke ytterligere
omfang. Se [dokumentoversikten](../../../../README.md#dokumentoversikt).

**Senere avklaring 06.10.26:** Hovedbriefen videreutvikles etter Odins innspill
med faste handlinger og et fast svarformat for KI-forklaringer. Chat og
friteksttolkning er utsatt fra førsteversjonen. Beregning, forklaring og visning
skal kunne brukes gjennom en eventuell chat senere. Eldre omtale av KI-tolkning
nedenfor er historisk bakgrunn; gjeldende omfang står i hovedbriefen. Videre
avklaringer logges i [hovedbriefens endringslogg](../../../../docs/productbrief-endringslogg.md).

**Senere avklaring, presisert 07.10.26:** En ferdig syntetisk vaktplan brukes som
datagrunnlag. Enkel plangenerering beholdes som forslag i MVP, etter Odins
korrigering av Codex sin tolkning om å fjerne generering. VaktMatch kan generere
og forklare et planforslag uten å innføre det i den faktiske vaktlisten. Reell
leverandørtilkobling er en fremtidig mulighet, ikke en forutsetning for prosjektet.
Omtalen nedenfor av generering og godkjenning bevares som historikk; gjeldende
retning står i hovedbriefen. Dette er Odins presiserte arbeidsretning, ikke en ny
felles beslutning. Korrigeringen er dokumentert i endringsloggen som E24.

## Datagrunnlag og oppdateringer – innspill 07.10.26

Odin ser for seg en mulig senere tilkobling til løpende oppdaterte bemanningsdata,
med Quinyx nevnt som eksempel. Tilgang hos leverandører er uavklart og ikke
undersøkt her. Studieprototypen skal demonstrere ideen med syntetiske data.
VaktMatch skal kunne gi nye vurderinger når datagrunnlaget endres; om oppdatering
skjer manuelt, automatisk eller ved en demosimulering, er et åpent designvalg.

Codex foreslår å sammenligne dataversjoner med vanlig kode og la KI forklare
påviste endringer. Forslaget skiller mellom undersøkt alternativ og observert
vaktendring, og utleder ikke hvem som valgte eller hvorfor. Dette er en
KI-konkretisering til senere PRD og arkitektur, ikke en valgt teknisk løsning.
Se [demoscenarioets forslag til oppdatering](../../../../docs/demoscenario-fravaer.md#forslag-til-demonstrasjon-av-oppdaterte-data).

## Historisk grunnlag fra september

Oppdatert 17. september 2026. Gjeldende [produktbrief](../../../../productbrief.md)
er utkastet til innlevering. Dette vedlegget bevarer produktinnspill og
utdypinger til videre BMAD-arbeid. Prosjektvalget er bekreftet av Odin på
vegne av gruppen; detaljert omfang og arbeidsdeling er fortsatt åpne.

## Turnusgeneratoren og førsteversjonen

Stians opprinnelige turnusgenerator-idé hadde tre nivåer:

1. **Minimum:** Registrere ansatte og bemanningsbehov, generere en turnus som følger harde regler, og vise den som kalender eller tabell.
2. **Middels:** Fordele helg, natt og uønskede vakter, håndtere ønsker som myke preferanser, forklare manglende dekning og eksportere planen.
3. **Avansert:** Håndtere sykefravær, forklare på naturlig språk, kjøre «hva om»-scenarioer og skille leder- og ansattilgang.

I arbeidet 7. september ble minimumsnivået tatt inn i MVP-utkastet som et
ukesgrunnlag. Akutt avvikshåndtering er hovedflyten. Utvidet periodeplanlegging,
preferanser og eksport er fortsatt fremtidige muligheter. Dette videreføres
som foreslått avgrensning, ikke som en ny felles godkjenning av alle detaljer.

Forslag til datamodell fra tidligere arbeid: `Ansatt`, `Skift`, `Regelsett` og
`Turnusplan`, med planstatus og avvikslogg. Regel- eller optimaliseringsbasert
kode skal generere og kontrollere planer. Ren turnusgenerering med språkmodell
ble vurdert og lagt bort; KI brukes til tolkning og forklaring.

Presiseringer fra gjennomgangen av kandidatene er tatt inn i briefen:
umulig bemanning må gi synlig udekket behov, og manglende nabovakter eller
andre kontrollopplysninger må gi uavklart status. En intern flytting må vise
konsekvensene for vakten personen flyttes fra.

## Vikarer og beslutningsmyndighet

Førsteversjonen bruker et lukket, forhåndsgodkjent sett syntetiske vikarer
modellert som tilknyttet et bemanningsforetak. Tidligere idé om en åpen
markedsplass er lagt bort. Arbeidsgiver, stillingsprosent og kontraktstype
ble foreslått som mulige datafelt; behovet for dem må avklares i datamodellen.

Dette er produktavgrensninger. Det tidligere materialets juridiske begrunnelser
er ikke verifisert på nytt. Prototypen gir bare kontroll mot et eksplisitt
scenarioregelsett. Menneskelig godkjenning før planendring er en produktregel.

## Teknologi og videre drift

Tidligere kursnotater omtaler Claude Code, alternative KI-agenter, VS Code,
Git/GitHub, Node/NPM, Python/uv, Docker, MCP og tjenestekontoer som GitHub
Actions og Supabase. Dette er bakgrunn om utviklingsverktøy, ikke en vedtatt
teknologistakk for VaktMatch. Arkitektur og nødvendige tjenester velges senere.

Odin har ønsket at begrensninger rundt datamengder, sikkerhet og drift blir
dokumentert. Før eventuell reell bruk må gruppen utrede tilgangsstyring,
personvern, driftsansvar, kostnader, kapasitet og relevante regler. Slike
produksjonsegenskaper er ikke lovet i studieprototypen.

## Konkurrentsjekk og integrasjoner

[Researchrapporten fra 7. september](../../research/competitive-simployer-quinyx-4human-akutt-bemannings-2026-09-07/research.md)
er en avgrenset historisk undersøkelse av offentlig materiale om Simployer,
Quinyx og 4Human. Undersøkelsen fant ikke dokumentasjon på akkurat den
sammenligningen VaktMatch ønsker å demonstrere. Det dokumenterer ikke at
funksjonen mangler hos leverandørene, eller at et markedshull er bekreftet.

Simployers «Finn vikar» kunne ikke undersøkes i detalj, en Quinyx-påstand om
intelligent omfordeling var uverifisert, og salgsstyrte demonstrasjoner ble
ikke undersøkt. Markedsposisjonen og brukerbehovet må derfor valideres videre.

Et forklaringslag over eksisterende systemer er en mulig langsiktig retning.
Reelle integrasjoner ligger utenfor MVP og krever avklaring av brukernes
arbeidsflyt, API-tilgang og eventuelle avtaler. Intervjuer med skiftledere er
et mulig neste tiltak for å undersøke nytte og praktiske begrensninger.

## Åpne valg

- Endelig demonstrasjonsdomene; lager/logistikk er et forslag.
- Konkrete harde regler, rangeringskriterier og hvordan belastning fra ekstravakter skal synliggjøres og testes.
- Om demonstrasjonen også skal simulere tilbud og aksept etter lederens valg.
- Teknologistakk, arbeidsdeling og mål for brukertesten.

## Innleveringsgrunnlag og BMAD-spor

Oppdateringen bygger på den eksisterende VaktMatch-briefen, vedlegget,
beslutningsloggen og tilbakemeldingene fra 7. september. Strukturen følger
lærerens `product-brief-template.md`, lagret under «Ressurser fra Canvas»
i Obsidian. `bmad-product-brief` er brukt til oppdateringen, med struktur- og
språkgjennomgang gjennom `bmad-review`.

Odin bekreftet 17. september at gruppen har valgt VaktMatch, at BMAD-ferdighetene
skal brukes, og at `productbrief.md` skal leveres søndag. Innleveringsdatoen
settes derfor til 20. september 2026. Tidligere frister i historiske logger er
utgått. Utkastet er utarbeidet med Codex; det er ikke registrert som innlevert
eller godkjent av faglærer.

Memloggens produktvalg og avgrensninger er innarbeidet i briefen. Tekniske
innspill, kreditering og researchbegrensninger er samlet her. Gamle frister,
kandidatstatus og prosesshendelser er bevart som historikk i loggen, og gjelder
ikke som nåværende status. PantBuddy, Forplanner og tilhørende materiale er
flyttet til Obsidian etter brukerens instruksjon.
