---
title: 'SCRUM-17: Avklar datatilføring og beslutningslogg i MVP'
type: 'chore'
created: '2026-10-21'
status: 'done'
route: 'oneshot'
review_loop_iteration: 0
context: []
---

<frozen-after-approval reason="Odins godkjenning av forslaget i samtalen om SCRUM-17">

## Intent

**Problem:** Produktgrunnlaget mangler avklart mekanisme for fravær, datasettbytte og lagring av lederens valg.

**Approach:** Dokumenter «Simuler fravær» på valgt ansatt og vakt og «Last inn oppdaterte vaktdata» med forhåndslagde datasett, synlig endringsoversikt og ny regelvurdering. Manglende opplysninger vises med konsekvens; et komplettert datasett kan lastes inn i demoen, mens ansvar ved reell bruk avklares senere. Behold valgt alternativ og simulerte tilbud/svar i aktiv demoøkt. Ta med valgfri varig beslutningslogg, avslått som standard, og frivillig begrunnelse. Oppdater brief, demo, README, endringslogg og memlog med riktig opphav, kontroller dokumentene og lukk avklaringssaken med lokal commit som inkluderer SCRUM-17. Lagringsteknikk og komplette datasett velges i videre implementering; dette arbeidet er dokumentasjon av avklart produktretning.

</frozen-after-approval>

## Implementation Notes

- Liten, reverserbar dokumentendring uten åpne produktvalg innenfor avklaringen. Eksisterende demo og loggstruktur gjenbrukes.
- Brief, demo, README, E30 og memlog er oppdatert. Lokale lenkemål og whitespace er kontrollert, og diffen er lest. Data og appkode er fortsatt videre implementering.

## Review Triage Log

- medium, patch: Fraværshandlingen var formulert som en tilbakestilling til D0. Den virker nå på gjeldende grunnlag; D0 er kun startpunkt i eksemplet.
- medium, patch: Logging av/på manglet overgangsregler. Presisert kun nye registreringer ved aktivering og ingen sletting ved deaktivering, med kontrolltilfelle D7.
- medium, patch: Aktiv økt manglet observerbar slutt. Konkretisert som lukking av fanen, med synlig skille mellom økt og varig logg.
- medium, patch: Tidligere valg manglet historisk status ved dataendring. Presisert gammel dataversjon og krav til ny kontroll, med D8.
- low, patch: Komplettering av V01 var ikke isolert til S3. D4 beholder A02/A03 utilgjengelige og gir eksplisitt forventet kontrollutfall for V01.
