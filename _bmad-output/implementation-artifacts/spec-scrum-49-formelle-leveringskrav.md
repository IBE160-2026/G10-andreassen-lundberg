---
title: 'SCRUM-49: Formelle leverings- og dokumentasjonskrav for IBE160'
type: 'chore'
created: '2026-10-22'
status: 'blocked'
route: 'oneshot'
review_loop_iteration: 0
context:
  - '{project-root}/AGENTS.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** Prosjektet mangler ett kildekontrollert, offentlig lesbart grunnlag
for leveringsfrister, godkjenningskrav, KI-dokumentasjon, individuelle bidrag og
vurdering av visuelt uttrykk i IBE160.

**Approach:** Kontroller Canvas, publiserte oppgaver og sensorressurser, samle
bekreftede krav i repoet og marker kun de punktene som kildene faktisk ikke
avgjør. Private studienotater brukes bare som indeks over åpne spørsmål.

</frozen-after-approval>

## Implementation Notes

- `docs/ibe160-leveringskrav.md` samler de bekreftede kravene og lenker til
  Canvas- og HiMolde-kildene med kontrolldato.
- README peker til kravdokumentet som del av dokumentoversikten.
- En separat `proposal.md` er bekreftet utgått; godkjent `productbrief.md` er
  arbeidskravet. Fristen ble forlenget til 27. september 2026 kl. 23:59.
- Sensorveiledningen er registrert med konkrete krav til prosesspor,
  KI-dokumentasjon, kvalitetssikring, README, repository og design/UX.
- Refleksjonsmalen bekrefter individuell refleksjon per gruppemedlem.
- Sluttfrist for prosjektkode/refleksjonsrapport og betydningen av
  «delvurdering 3» avgjøres ikke av de kontrollerte kildene. Canvas-modulen har
  heller ingen publisert overordnet sensorveiledning eller egen veiledning for
  del 2. Saken forblir derfor blokkert i `To Do` i tråd med prosjektets
  Jira-regel, med Odin som oppfølgingseier.
- `productbrief.md` er ikke endret; dette arbeidet dokumenterer emnekrav og
  utløser derfor ingen endring i produktbriefens endringslogg.

## Review Triage Log

| ID | Dom | Evidens og behandling |
|---|---|---|
| BH1 | high | Formell emneside sier to deler, mens Canvas har resttekst om tre. Begge kilder og nødvendig avklaring er nå uttrykkelig dokumentert. |
| BH2 | high | README-kravene var for bredt parafrasert. Erstattet med sensorveiledningens konkrete krav til versjoner, kommandoer, miljøvariabler, testgrunnlag, mappeoversikt og oppdatering. |
| BH3 | medium | KI-krav manglet kobling til endringer, planavvik og rettede KI-feil. Lagt til og kildeattribusjonen mellom emneside og sensorveiledning er presisert. |
| BH4 | medium | Leveringsmåten for del 1 var kjent. Registrert at sensor bruker siste commit før fristen i gruppens repository; bare dato og kanal for refleksjonsrapport er åpne. |
| BH5 | medium | Fristen 20. september i briefen er faktisk innleveringsdato. Kravdokumentet forklarer at fristen senere ble forlenget til 27. september og lenker til tilbakemeldingen som viser at briefen ble levert. |
| BH6 | medium | Faglærers «kan gå videre» er registrert som praktisk klarsignal, men formell godkjenningsstatus er fortsatt eksplisitt åpen. Product brief er presisert som 2026-erstatning for proposal. |
| BH7 | medium | Neste handling og oppfølgingseier er lagt til. Jira får en egen blokkeringskommentar etter commit. |
| BH8 | medium | Canvas-modulen er kontrollert; manglende overordnet sensorveiledning og del-2-veiledning er dokumentert uten å hevde at de ikke finnes andre steder. |
| BH9 | medium | Midlertidige PDF-uttrekk ligger bare lokalt; `tmp/` er lagt til i `.gitignore` og inngår ikke i commit eller offentlig repo. |
| BH10 | low | Navnet er rettet til «Prosjektkode og funksjonalitet». |
| BH11 | low | Designkriteriet angir nå 10 % av del 1 / 7 % samlet, app-tilpasning og alle karakternivåene. |
| BH12 | low | Specens kildepåstand er avgrenset til kontrollerte kilder; memloggens designpåstand blir dekket av det utvidede dokumentet. |
