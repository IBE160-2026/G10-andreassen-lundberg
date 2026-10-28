# KI-forklaringer – kildedigest, runde 1

Skrevet av Codex 26.10.2026. Tre originalarbeider lest direkte; ingen kilde er en test av VaktMatch eller dagens språkmodeller. Nettlesøk og direkte PDF-lesing, tre web-kall. Dette er historisk metodegrunnlag, ikke dokumentasjon på at KI gir produktet merverdi.

## A1 – Forklaring er ikke i seg selv bedre beslutninger

- Claim: Bansal mfl. fant i eksperimenter med sentimentoppgaver og LSAT at forklaringer ikke økte den komplementære teamprestasjonen; de økte aksept av KI-råd også når rådet var feil.
- Source: https://aiweb.cs.washington.edu/ai/pubs/bansal-chi21.pdf
- Publisher: ACM CHI; forfatterkopi ved University of Washington.
- Pub_date: 2021-05. Accessed: 2026-10-26.
- Confidence: medium, unverified in independent check. Class: empirical-explanation-study.
- Locator: abstract og introduksjon side 1–2; oppgaver er sentiment i bok-/ølanmeldelser og LSAT, deltakere rekruttert som crowd workers. Ikke bemanningsledere og ikke tekst fra en moderne språkmodell.

## A2 – Mindre overavhengighet kan koste brukervennlighet

- Claim: Buçinca mfl. sammenlignet beslutningsstøtteutforminger i et eksperiment med 199 deltakere. Tiltak som krevde mer aktiv vurdering reduserte overavhengighet sammenlignet med enkle forklaringer, men de mest effektive fikk svakere subjektive vurderinger.
- Source: https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf
- Publisher: ACM CSCW/PACMHCI; forfatterkopi ved Harvard.
- Pub_date: 2021-04. Accessed: 2026-10-26.
- Confidence: medium, unverified in independent check. Class: empirical-explanation-study.
- Locator: abstract side 1 og studiedesign avsnitt 3.1–3.2: ernæringsoppgave og simulert KI. Uavhengig eksperiment fra A1. Støtter forsiktighet med å likestille tilfredshet/tillit og beslutningskvalitet, men ikke en bestemt skjermflyt i VaktMatch.

## A3 – Plausibilitet og trofasthet er ulike vurderinger

- Claim: Jacovi og Goldberg argumenterer for at hvor overbevisende en forklaring virker og hvor riktig den beskriver beslutningsgrunnlaget, må vurderes separat. Tekst generert etter beslutningen gir ikke i seg selv noen trofasthetsgaranti.
- Source: https://aclanthology.org/2020.acl-main.386.pdf
- Publisher: Association for Computational Linguistics.
- Pub_date: 2020-07. Accessed: 2026-10-26.
- Confidence: medium; teoretisk metodeargument, ikke effektstudie. Class: explanation-evaluation-method.
- Locator: avsnitt 2, side 4199. Gjelder fortolkning av modellbeslutninger. Anvendelse på tekst om en deterministisk regelmotor er vår metodeoverføring og må testes separat.

## Syntese til kontroll

De to uavhengige eksperimentene gir grunn til å avvise antakelsen om at en forklaring automatisk forbedrer bruken av et KI-råd. Ingen av dem avgjør om en kort KI-omskriving av kontrollerte bemanningsdata er bedre enn en mal. Kritisk påstand for verifikasjon: kvalitet/nytte kan ikke vurderes gjennom tillit eller tekstens overbevisning alene.

KI-forslag, ikke kildefunn: sammenlign samme scenario med standardtekst og KI-tekst; sjekk først faktasamsvar med regelresultatene, deretter om leseren forstår forskjellene og oppdager manglende data. Registrer feil og tid hver for seg. Produktspesifikke terskler og en eventuell brukertest er ikke vedtatt her.

Gjenstår: direkte effekt på målgruppen, nyere undersøkelser av denne konkrete oppgaven og hvilket informasjonsbehov en standardtekst faktisk ikke dekker. Innsamlingsrunden avsluttes ved én-rundesgrensen; tre av fem mulige kilder brukt.
