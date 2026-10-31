# Kildeavstemming av brief og PRD – SCRUM-46

*Utført av Codex · 31.10.2026. Dette er KI-kontroll av dokumentgrunnlaget,
ikke en ny produktbeslutning eller verifikasjon av appkode.*

Kontrollen bygger på [PRD-en](prd.md), dens [.memlog.md](.memlog.md),
[produktbriefen](../../../../productbrief.md),
[demoscenarioet](../../../../docs/demoscenario-fravaer.md),
[søkemetoden](../../../../docs/forslag-ved-frafall.md),
[kostnadsanslaget](../../../../docs/kostnadsanslag.md),
[teknologivalgene](../../../../docs/teknologivalg.md) og
[endringsloggen E28–E35](../../../../docs/productbrief-endringslogg.md).
De eldre avklaringene om prosess og frist er kontrollert mot
[AGENTS.md](../../../../AGENTS.md#sesjonslogg) og
[leveringskravene](../../../../docs/ibe160-leveringskrav.md#bmad-og-arbeidslogg).
Det finnes ikke et eget addendum i PRD-mappen.

## Resultat og rettelser

| Sted | Kilde og konkret avvik | Presis rettelse |
|---|---|---|
| PRD FR-16 | «Historikken endrer ikke sortering eller status» er videre enn H1. Briefens siste avsnitt om korrigert historikk og demoens historikkavsnitt sier at en ny dataversjon med korrigerte nabovakter kan endre nødvendig kontrollgrunnlag og dermed regelstatus. | Si at historikk ikke gir et eget rangeringskriterium. Historikk som ikke påvirker R1–R5 eller P1/P2, endrer ikke resultatet; korrigert nødvendig kontrollgrunnlag utløser ny kontroll. |
| PRD NFR-8 | Sporbarhetskravet nevner KI-bruk og kodegjennomgang, men ikke den gjeldende prosjektregelen om arbeidslogg ved avsluttet økt. AGENTS.md krever sesjonslogg og lokale loggcommits; leveringskravene gjengir faglærers begrunnelse for prosesspor. | Henvis til AGENTS.md for øktloggen og skill mellom prosjektets valgte gjennomføringsregel og faglærers generelle krav til arbeidslogg. Ikke gjør et bestemt loggformat til et nytt eksternt krav. |
| PRD §9, spørsmål 1 | Spørsmålet viser ikke den muntlige delavklaringen som allerede finnes i leveringskravenes tabell: omtrent 15. desember som utgangspunkt, applikasjon og refleksjon samtidig. Skriftlig sluttfrist og leveringskanal mangler fortsatt. | Ta med den muntlige statusen og kildehenvisningen, og behold SCRUM-49 åpen for skriftlig bekreftelse. Ikke fremstille omtrent-datoen som bindende frist. |
| PRD §10 | «Ingen gjenstående» er bare begrunnet med tre antakelser avgjort 29.10.26. §7.2, briefen og E35 skiller fortsatt mellom Odins omfangsvalg og Codex sine konkretiseringer av kostnadsberegning og sekvensiell håndtering. | Presiser at de tre eldre antakelsene er avklart, mens de nyere KI-konkretiseringene beholder sitt opphav og ikke innebærer særskilt detaljgodkjenning. Dette krever ikke at omfangsvalgene tas på nytt. |

## Samordnet grunnlag

Ingen ny mangel er funnet i gjengivelsen av omfangsvalgene fra 30.10:
enkel tilbudssimulering og begrenset datasettbytte er Må, varig logg og
lederlåser i grensesnittet er Bør, og én KI-handling bygges først. Det samme
gjelder sekvensielle fravær, kostnadsanslag med syntetiske satser og skillet
mellom kostnad, P1/P2 og R1–R5. Se den tidligere
[avstemmingen fra 30.10](reconcile-2026-10-30.md) for detaljene; de gjentas ikke her.

S1–S5, H1–H5, F1–F7, D1–D8, M1–M2 og O1–O5 beskriver forventet oppførsel.
Hovedtabellen og F2–F4 er uttrykkelig ufullstendige som kjørbart datasett.
Komplette vakter, øvrig relevant arbeid for eksterne, historikk, kostnadsdata
og fasit må fortsatt leveres gjennom dataarbeidet; dette er ingen påvist feil
i at PRD-en er et planleggingsgrunnlag. Låser fra datasettet og senere
UI-låsing er skilt i PRD FR-10/22 og §7.2, og krever ingen ny omfangsavklaring.

Teknologidokumentets samordningsavsnitt gjengir status ved kontroll 26.10.
Eventuell nyere samordning må knyttes til konkret Jira-/grenbevis før teksten
ajourføres; denne avstemmingen utleder ingen ny godkjenning av kodeskjelettet.

## Oppfølging i samme økt

Codex har rettet de fire presiseringene i PRD-en. E33/E34-statusen i
teknologidokumentet er oppdatert med SCRUM-13-kommentar `10023` som kilde.
Se [samlet kontrollgrunnlag](../../../../docs/scrum-46-prd-avstemming.md)
for faktisk Jira-oppfølging og gjenværende saksavhengighet.
