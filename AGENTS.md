# Prosjektregler

## Språkhygiene og omtale av personer

Gjelder dokumentasjon, BMAD-output, research, beslutningslogger (også skjulte
`.memlog.md`), Jira-saker og -kommentarer, commit-meldinger og pull requests.
Skriv med tanke på at repoet og delte prosjektflater kan leses offentlig.

- Beskriv prosjektets behov, avklaringer og beslutninger saklig. Ikke skriv
  vurderinger av navngitte personers evner, motivasjon, følelser eller vilje
  til å bidra, og ikke utled slike vurderinger fra interne samtaler eller taushet.
- Formuler åpne spørsmål som felles prosjektavklaringer: «Prosjektvalg,
  MVP-omfang og arbeidsdeling gjenstår», fremfor å fremstille ett gruppemedlem
  som problemet eller en blokker.
- Skill mellom forslag, individuelle innspill og felles beslutninger. Ikke
  fremstille en kandidat som valgt, eller et forslag som godkjent av begge,
  uten uttrykkelig grunnlag.
- Behold relevant og korrekt kreditering av faktiske bidrag. Språkhygiene skal
  ikke anonymisere forfatterskap eller skjule faglige uenigheter, begrensninger
  og beslutningsgrunnlag; beskriv saken og konsekvensen fremfor personen.
- Ta bare med personopplysninger og sitater fra interne samtaler når de er
  nødvendige for dokumentets formål og avklart for deling. Bruk ellers en
  nøytral oppsummering. Merk konstruerte personaer som eksempler.
- Kontroller også vedlegg og skjulte logger før commit eller push. Ikke flytt
  personlige vurderinger fra hoveddokumentet til en annen publisert fil.
- Dersom uheldig omtale allerede er publisert, rett dagens dokumenter og gjør
  oppmerksom på at eldre versjoner kan finnes i historikken. Ikke omskriv
  Git-historikken uten en egen avtale.

Regelen ble innført 2026-09-07 etter gjennomgang av prosjektbriefene.

## Endringer i produktbriefen

- Ved hver endring i `productbrief.md`, oppdater samtidig
  [endringsloggen](docs/productbrief-endringslogg.md) med dato, berørt del,
  hva som endres fra og til, og en enkel forklaring på hvorfor.
- Oppgi kilde og opphav, og skill mellom forslag, individuell arbeidsretning,
  KI-presisering og felles beslutning. Ikke utled godkjenning fra taushet.
- Rene språk-, metadata- og lenkerettelser kan grupperes, men skal også omtales.
  Marker om produktinnholdet er uendret. Begrunnelser som mangler i kildene,
  merkes som udokumenterte; ikke finn på forklaringer i ettertid.
- Behold tidligere innslag. Når et valg endres, legg til et nytt innslag som
  viser til det gamle. Første versjon og alle tekstendringer skal fortsatt kunne
  spores i Git; loggen angir det faste sammenligningsgrunnlaget.
- Hold lenkene fra hovedbriefen og README til loggen oppdatert. En skjult
  `.memlog.md` eller commit-melding alene erstatter ikke den lesbare forklaringen.

## Føring og lesing av memlog

*(Skrevet: Codex · 07.10.26, etter Odins gjennomgang av loggbruken)*

- Bruk `.memlog.md` som kort prosesshukommelse. Før én vesentlig hendelse
  per innslag, normalt én–to setninger med begrunnelse og lenke til detaljer.
  Produktbriefen viser gjeldende arbeidsutkast; endringsloggen forklarer endringene.
- Nye innslag skal ha dato (`YYYY-MM-DD`), konkret opphav i `--by` og en
  relevant type. Skill mellom innspillets opphav og hvem som har tolket det:
  KI-tolkninger føres som `assumption` med KI som opphav, ikke som brukerens
  `decision`. Bruk `decision` bare når kilden støtter den konkrete beslutningen.
- Registrer praktiske demovalg i forhold til betydningen de har. Ikke gjør
  eksempler eller enkle svar til sterkere produktkrav eller prinsippvalg.
- Skriv nye innslag gjennom `_bmad/scripts/memlog.py append`. Bevar eldre
  innslag; rett feil med et kort `override` som identifiserer innslaget og
  forklarer rettelsen. Les senere rettelser før eldre utsagn brukes som grunnlag.
  Eldre datoer eller opphav som ikke kan dokumenteres, skal ikke gjettes.
- Ved flytting av aktiv logg skal både gammel og ny logg ha en henvisning
  til den andre. Hovedbriefens aktive logg er [rotloggen](.memlog.md);
  logger for alternativforslag og research gjelder sine egne dokumenter.

## Robust bruk av Jira

*(Skrevet: Codex · 22.10.26, på grunnlag av SCRUM-51 og Odins gjengivelse av
prosjektavklaringen 21.10.26)*

- Jira brukes til prioritering, fordeling og oppfølging. Repoet er autoritativt
  for produktbrief, arkitektur, kode og prosjektbeslutninger; Jira-kommentarer
  eller sakshistorikk erstatter ikke relevant dokumentasjon i repoet.
- Begge prosjektadministratorene har samme delegerte myndighet til å ta
  ordinære prosjektbeslutninger alene. Registrer hvem som tok beslutningen og
  kilden i dokumentet beslutningen gjelder, med kort prosesspor i `.memlog.md`
  og ved produktbriefendringer også i `docs/productbrief-endringslogg.md`.
  Ikke fremstille et individuelt valg som om begge valgte detaljene.
- Tildeling betyr ansvar for oppfølging, ikke større beslutningsmyndighet.
  Oppdater språk, metadata, status, prioritet, sprint, avhengigheter og
  akseptansekriterier direkte når grunnlaget er dokumentert.
- Koordiner med berørte prosjektadministratorer før sletting,
  historikkomskriving, endring av arbeidsflyt,
  statuser, sakstyper, tillatelser eller board-filter, vesentlig omlegging av
  aktiv sprint eller arbeid som allerede utføres, og endring av
  administratorrettigheter eller delegert myndighet. Registrer avklaringen i
  den berørte Jira-saken og, når den gjelder en prosjektbeslutning, i repoet.
- Før en sak tas inn i en sprint bør formål, testbart resultat, ansvar,
  prioritet, avhengigheter og nødvendig kildegrunnlag fremgå. Sett ikke saken
  til `Done` før akseptansekriteriene er kontrollert og nødvendig test- eller
  dokumentasjonsbevis er tilgjengelig.
- Blokkert arbeid beholder korrekt arbeidsstatus og får en kort kommentar om
  blokkeringen og nødvendig neste handling. Bruk `In Progress` mens saken
  undersøkes aktivt, og `To Do` når arbeidet er klart eller venter på en
  dokumentert avklaring.
- Bruk Jira-nøkkelen i tilhørende commit-melding. Når saken er verifisert,
  kommenter kort med kontrollgrunnlag og commit-ID før den settes til `Done`.

## Prosjekthistorikk og personlige studienotater

*(Skrevet: Codex · 22.09.26; generalisert: Codex · 06.10.26, etter instruksjon fra Odin)*

Bevar vesentlige prosjektavklaringer, begrunnede valg, læringspunkter, endret
omfang, frister og oppfølging i prosjektets eksisterende dokumentasjon, slik
at alle som arbeider i repoet kan finne grunnlaget. Bruk korte oppsummeringer
og lenker til kildene fremfor parallelle kopier av samme informasjon.

- Repoet er felles kilde for produktbrief, arkitektur, kode og prosjektbeslutninger.
  Felles krav og faglærerbeskjeder skal være tilgjengelige eller referert her,
  ikke bare i én deltakers personlige notater. Bruk README som inngang til
  gjeldende dokumenter; bevar tilbakemeldinger som kilder.
- Skill mellom felles beslutninger, individuelle innspill og KI-vurderinger.
  Registrer kilde, dato, usikkerhet og hvem som har skrevet eller vurdert innholdet.
- Personlige studie- eller prosjektnotater oppdateres når brukeren har bedt om
  det i oppdraget eller gjennom stående instrukser. Bruk det avtalte notatsystemet
  og dets eksisterende prosjekt-, emne- og dagsnotater der det passer. Regelen
  forutsetter verken Obsidian eller at deltakerne bruker samme verktøy og stier.
- Les notatsystemets egne instrukser, eventuell AGENTS.md og målnotatene før
  endring. Personlige oppsett og stier hører hjemme i brukerens lokale instrukser.
  Bevar studiesammenheng, refleksjoner og lenker der; ikke kopier hele
  prosjektgrunnlaget eller hver kodeendring til personlige notater.
- En forespørsel om vurdering eller råd alene er lesende arbeid, med mindre
  notering er uttrykkelig autorisert. Den gir ikke tillatelse til å endre
  produktbriefen eller gjøre vurderingen til en gruppebeslutning.
- Ikke kopier private refleksjoner, personopplysninger eller andre personlige
  notater tilbake til repoet uten uttrykkelig instruksjon. Ikke lagre hemmeligheter
  i repoet eller notatsystemet.
- Hvis avtalt notering ikke kan utføres fordi notatsystemet er utilgjengelig,
  opplys kort hva som bør noteres senere. Fortsett repoarbeidet; ikke opprett
  et erstatningssystem eller anta at andre maskiner har samme lokale oppsett.
- Avslutt med kort status på hvilke dokumenter og eventuelle personlige notater
  som ble oppdatert, og hva som fortsatt er uavklart. Kontroller nye lenker.

## Sesjonslogg

Når en oppgave eller økt avsluttes, før sluttoppsummeringen, bruk `sesjonslogg`-skillen: dokumenter Oppgave + Plan + Resultat + åpne punkter i `.logs/<bruker>/`, og før åpne punkter i `.logs/<bruker>/issues.md`. Skillen committer loggfila lokalt; push gjør du selv. Gruppens egne regler for commit og språk gjelder foran dette.
