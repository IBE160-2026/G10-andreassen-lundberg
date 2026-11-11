# Kontrollrapport – VaktMatch UX, SCRUM-47

- **Dokumenter:** [DESIGN.md](DESIGN.md) og [EXPERIENCE.md](EXPERIENCE.md).
- **Kontrolldato:** 2026-11-08. Utført av Codex med egne underagenter og nettleserverktøy.
- **Mandat:** Odins oppdrag om å avklare detaljene og drive det påbegynte UX-arbeidet videre.
- **Start med:** [klikkbar prototype](mockups/prototype.html) eller [HTML-rapport](validation-report.html).

## Samlet vurdering

Dokumentparet og skjermreferansene gir et sammenhengende grunnlag for
implementering. Alle fire PRD-reiser, relevante resultatdimensjoner og
Må-flytens flater er beskrevet. Tre kilde-/presisjonsfunn ble rettet.
Ingen utestående kritiske, høye, middels eller lave funn er registrert
i denne gjennomgangen.

Prototypen er en illustrasjon, ikke VaktMatch-regelmotoren. Den viser
forhåndslagde resultater for onsdagens morgenvakt og et separat konstruert
flyttescenario. Andre målskift får en uttrykkelig beskjed om at
prototypeberegning mangler. `final` i UX-dokumentene angir ferdigstilt
designgrunnlag; det betyr ikke ferdig app eller dokumentert brukereffekt.

## Kategorivurderinger

| Kategori | Vurdering | Kontrollgrunnlag |
|---|---|---|
| Flytdekning | strong | Alle fire UJ-titler, nummererte reiser og feil-/kantveier; fraværssimulering og søk er separate handlinger. |
| Tokenfullstendighet | strong | YAML, konkrete farger, definerte tokenreferanser og elleve målte kontrastpar. |
| Komponentdekning | strong | Samme 19 navn i begge dokumentene, med visuelle regler og oppførsel. |
| Tilstandsdekning | strong | Tomt, ugyldig, ventende, feil, utdatert, mangler, tilbudssvar og KI-reserve er spesifisert. |
| Visuell referansedekning | strong | Fire statiske skjermer og klikkbar prototype, lenket fra begge dokumenter; ingen uomtalte mockfiler. |
| Omfang og presisjonsnivå | strong | Kildene eier produktreglene; dokumentparet eier presentasjon og interaksjon. Ingen nye integrasjoner innføres. |
| Kildearv og begreper | strong | P1/P2, dekning, kontroll, søk, valg og svar holdes atskilt; opphav og prototypebegrensning er uttrykkelige. |
| Dokumentform | strong | Kanonisk DESIGN-struktur og alle obligatoriske EXPERIENCE-seksjoner. |

## Funn etter alvorlighet

**Kritiske: 0. Høye: 0. Middels: 3, alle rettet. Lave: 0.**

| Middels funn | Rettelse og kontroll |
|---|---|
| Sammenligning uten rangert referanse var udefinert. | «Forklar forskjellen» er utilgjengelig uten sammenlignbar referanse. Standardforklaringen beholdes. Avbrutt søk gir bare foreløpig referanse. |
| Et låst målskift kunne ikke få fravær i den første mockversjonen. | Lås hindrer flytting av andre tildelinger og skjuler ikke fravær. Fredagens låste målskift kan simuleres; udekket behov vises i ukesoversikten. Tre regresjonskontroller bestod. |
| Ekstern-kandidatteksten kunne motsi illustrert bestått kontroll. | Det konstruerte eksemplet oppgir komplett kontrollgrunnlag for viste vakter/nabovakter. Appens manglende nødvendige grunnlag gir Uavklart; modellering av eksternt arbeid følges i SCRUM-19. |

Se [rubrikkgjennomgangen](review-rubric.md) for kildeplassering og
[struktur-/språkkontrollen](review-editorial.md) for de to presiserte formuleringene.

## Faktisk kontroll av prototypen

[Den siste maskinlesbare kjøringen](.working/verification-results.json)
har **95 beståtte kontroller og 0 feil**. Nettleser: Chromium 145,
Playwright 1.58.0; tilgjengelighetsmotor: axe-core 4.10.3.

| Kontroll | Resultat |
|---|---|
| Fire skjermer ved 1440, 768 og 360 px | Ingen vannrett rulling. Skjermbildene for alternativoversikt og detaljer på PC/mobil er også sett gjennom visuelt. |
| axe, fire skjermer på PC og mobil | Åtte kjøringer uten rapporterte brudd i de valgte WCAG A/AA-reglene. Dette er ikke en full tilgjengelighetsattest. |
| Tekstforstørrelse og tastatur | Alternativoversikt flyter om ved 200 % tekststørrelse. Tab/Enter kan gjennomføre fravær til resultat; tilbake fra detaljer gjenoppretter fokus. |
| Fravær og periode | Manglende ansatt og ugyldig dagtall avvises; overlappende påbegynt nattvakt vises beskyttet. Endret utkast fjerner ikke aktivt fravær. Låst målskift kan ha fravær. |
| Sortering og søkeomfang | P1 gir A02 før A03; P2 gir A03 før A02. Siste kriterium kan ikke fjernes. Endret søkegrense krever eksplisitt søk; grense 0 viser ingen flytteeksempler. |
| Valg og svar | Regelavvik kan undersøkes, men ikke velges som kontrollert løsning. A → B → A bevarer svar. Flytteeksemplet krever aksept fra begge berørte. |
| Ny dataversjon | Forhåndsvisning før bytte, ny vurdering og ingen arvet aksept. Tidligere valg/svar vises med gammel dataversjon. |
| Reserve og feil | Standardforklaringen og valget beholdes uten modell; tomt søk har avgrenset konklusjon; søke-/innlastingsfeil har vei videre. |
| Lokal kjøring | Ingen JavaScript-feil eller HTTP(S)-forespørsler fra prototypen under kontrollen. Fire statiske referanser er uten script. |
| Dokumenter | Kildestier, lenker fra hoveddokumentene, tokenreferanser, komponentnavn og kontrastpar består. |

Første nettleserpass fant ugyldig struktur i noen definisjonslister.
Strukturen ble rettet og axe-kontrollene kjørt på nytt. Mobiltekst ble
økt til minst 14 px ved standard tekststørrelse; tallgrupper flyter over
flere rader der de trenger plass.

### Gjenta kontrollen

Fra repoets rot, med `uv` installert:

```powershell
uv run --with playwright==1.58.0 playwright install chromium
uv run _bmad-output/planning-artifacts/ux-designs/ux-G10-andreassen-lundberg-2026-10-31/.working/verify-ux.py
```

`--browser <sti>` kan bruke en eksisterende Chromium. `--axe <sti-til-axe.min.js>`
tar med tilgjengelighetskontrollene. Denne kjøringen brukte axe-core 4.10.3
installert i en midlertidig mappe utenfor repoet. `--export-mocks` regenererer
de fire statiske referansene fra prototypen. Uten `--axe` blir kontrolltallet
lavere; det skal ikke rapporteres som en ny kjøring av alle 95 kontrollene.

## Akseptansekriterier i SCRUM-47

| Kriterium | Bevis i repoet |
|---|---|
| Ukesoversikt, sammenligning, kandidatdetalj og planforslag | [Ukesoversikt](mockups/key-ukeplan.html), [fravær](mockups/key-fravaer.html), [alternativer](mockups/key-alternativer.html) og [detaljer med før/etter-forslag](mockups/key-detaljer.html). |
| Oppfylt, regelavvik, uavklart og udekket | Separate statuser i alternativoversikt/detaljer; udekket faktisk bemanning i konteksten og ukesoversikten. |
| Mobil og PC | Samme HTML flyter om; 360/768/1440 px er kontrollert. |
| Forslag kan ikke forveksles med gjeldende plan | Demobanner, egne før/etter-felt og uttrykkelig uendret plan etter valg/aksept. |
| Lesbarhet, kontrast og tastatur er vurdert | Tokenmålinger, axe, Tab/Enter-kontroll og visuell inspeksjon. |
| UX-dokumentasjon lenket fra README | README lenker til begge kontrakter, prototype og implementeringsoverlevering. |
| Tilbud, øktvalg, datasettbytte og kostnad | Interaktive visninger og kontrollsekvenser; kostnadsgrunnlaget er konstruert, separat fra P1/P2 og kildeførte O-tester. |

Dette er kontrollbevis for UX-leveransen. Jira-status og publisering
følger prosjektets vanlige sporbarhet; rapporten hevder ingen ekstern merge.

## Kontrollgrenser og neste arbeid

Ingen faktisk regelmotor, søkealgoritme, KI-tjeneste, backendfeilhåndtering,
komplett demodatasett eller varig lagring er implementert gjennom dette
UX-arbeidet. Appens eksisterende backend-/frontendtester er derfor ikke
kjørt på nytt som bevis for disse funksjonene.

Full skjermleserkontroll, flere nettlesermotorer, brukertest og appens
ende-til-ende-verifikasjon gjenstår i implementeringen. Visuelle referanser
dekker hovedkomposisjonene; tilstander som ikke kan utløses i prototypen
bygges fra dokumentparets tabeller. Se [overleveringen](implementation-handoff.md)
for eksisterende Jira-oppfølging.

## Kontrollfiler

- [Rubrikk](review-rubric.md).
- [Struktur og språk](review-editorial.md).
- [Kildeavstemming](.working/source-reconciliation-2026-11-08.md).
- [Kontrollskript](.working/verify-ux.py) og [resultat](.working/verification-results.json).
- [PC: alternativer](.working/results-1440.png) og [detaljer](.working/details-1440.png).
- [Mobil: alternativer](.working/results-360.png) og [detaljer](.working/details-360.png).
