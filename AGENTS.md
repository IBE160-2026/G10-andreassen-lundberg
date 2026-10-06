# Prosjektregler

## Språkhygiene og omtale av personer

Gjelder dokumentasjon, BMAD-output, research, beslutningslogger (også skjulte
`.memlog.md`), commit-meldinger og pull requests. Skriv med tanke på at repoet
kan leses offentlig.

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
