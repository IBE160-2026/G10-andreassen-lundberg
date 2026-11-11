# Fra UX til implementering – SCRUM-47

Skrevet av Codex 08.11.2026 på Odins gjennomføringsmandat. Dette er en
overlevering av UX-grunnlaget til eksisterende implementeringssaker,
ikke en ny sprintplan eller endring av ansvar.

Begynn med [den klikkbare prototypen](mockups/prototype.html),
[EXPERIENCE.md](EXPERIENCE.md) og [DESIGN.md](DESIGN.md).
Prototypens eksempelinnhold er konstruert; bruk de kildeførte scenarioene
og fasitdatasettet ved implementering av beregninger og søk.

## Anbefalt rekkefølge

| Del | Eksisterende oppfølging | Når delen kan regnes som verifisert |
|---|---|---|
| Datakontrakt og demoens klokke | SCRUM-19/20 | Uke 1–4, arbeidsuke, nabovakter, behov, tilgjengelighet, låser og dataversjon har et entydig format og kontrollgrunnlag. |
| Ukesoversikt og fraværsskjema | SCRUM-22/42 | Ett gyldig målskift kan simuleres. Ugyldig input, beskyttede vakter og feil ved innlasting har norske meldinger og vei videre. |
| Kontrollerte alternativer | SCRUM-24–28/37 | Resultater viser dekning, kontroll og søkestatus separat. Alle berørte kontrolleres; søkegrense 0/1, låser og grenseverdier verifiseres med fasit. |
| Sammenligning og detaljer | SCRUM-30/35/36/55/60 | P1/P2, prioritering, likeverdig rangering, mangler, historikk og syntetisk kostnad viser faktiske beregningsresultater med kilder. Kostnad endrer ikke rangeringen. |
| Øktvalg, tilbud og nye data | SCRUM-53 og eksisterende tilbuds-/datasettoppfølging | Valg og svar beholdes per forslag og dataversjon. Oppdatering krever ny kontroll; aksept endrer ikke vaktlisten og arves ikke av et nytt grunnlag. |
| Forklaring | SCRUM-39/40/41/59 | Standardforklaring fungerer uten nøkkel. KI forklarer fakta i fast format og endrer aldri rangering, kontroll eller valg. Modellvalget tas i SCRUM-59. |
| Samlet demoflyt og levering | SCRUM-43/44/48 | Kjørbare tester og en faktisk lokal gjennomføring dekker UJ-1–4, mobil/PC og feiltilfellene. UX-prototypekontrollen alene lukker ikke disse sakene. |

Rekkefølgen uttrykker tekniske avhengigheter. Utvikling av visuelle
komponenter, eksempelkontrakter og standardforklaringer kan foregå samtidig.
Kontroller eksisterende Jira-saker før ny oppdeling eller tildeling.

## Informasjon som grensesnittet må få fra beregningene

Frontend skal presentere resultater fra data-/regel-/søkelagene, ikke
rekonstruere lovgrunnlag, tilgjengelighet eller regelstatus fra farger og tekst.

| Resultatgruppe | Nødvendig innhold |
|---|---|
| Grunnlag | Dataversjon, vurderingstidspunkt, ukegrenser, kjente mangler og tilgjengelige oppdateringer. |
| Forslag | Stabil forslags-ID, målskift, alle berørte tildelinger før/etter og udekkede plasser. |
| Kontroll | R1–R5 per berørt person, bekreftede verdier, mangler, regelkilde og samlet status med riktig forrang. |
| Rangering | Aktive kriterier i prioritert rekkefølge, P1/P2-verdier eller konkret mangel, likeverdig gruppe og ufullstendig søk. |
| Kostnad | Total før/etter, differanse, timer, satser/tillegg, enhet NOK, kilde og mangler; ingen beregnet totalsum når nødvendige satser mangler. |
| Forklaring | Fire avtalte tekstfelt basert på fakta, modell-/standardmodus og forståelig reservemelding. |
| Økt | Valg og svar knyttet til dataversjon, målskift, forslag og alle berørte personer; tidligere grunnlag kan vises som historikk. |

Dette er et innholdskrav til kontraktene, ikke et nytt vedtatt API-skjema.
Eksakte typer og endepunkter avklares i implementeringssakene og
[arkitekturen](../../../../docs/arkitektur.md).

## Avgrensning av ferdigstatus

UX-grunnlaget kan være ferdig uten at appen er ferdig. Prototypen har
forhåndslagde illustrasjoner av resultater, ingen regelmotor, modellkall,
leverandørtilkobling eller varig beslutningslogg. Kontrollrapporten skal
skille dokumentdekning, prototypeoppførsel og appverifikasjon.

Alle åpne spørsmål i [kildeavstemmingen](.working/source-reconciliation-2026-11-08.md)
om modell, ekstern vikars øvrige arbeid og leveringskrav følges fortsatt
i sine eksisterende saker. De gis ikke nye svar gjennom visuelle skisser.
