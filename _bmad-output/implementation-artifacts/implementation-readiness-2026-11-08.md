# Implementeringsklarhet – avgrenset demoflyt

**PASS for implementering av den kildeførte demoflyten.** Kontrollert av
Codex 08.11.2026 på Odins mandat om å gjennomføre arbeidet selvstendig.

Grunnlaget er gjeldende produktbrief, PRD fra 29.10 med senere rettelser,
arkitekturen, demoscenarioets R1–R5/S/H/F/D/M-tilfeller, kostnadsanslagets
O1–O5 og UX-kontraktene ferdigstilt 08.11. De beskriver den avgrensede
kjernen uten at nye produktvalg må finnes på.

Eksisterende saker SCRUM-19/20/22 dekker datakontrakt, fasit og fravær;
SCRUM-24–28/37/56 dekker kontroller og søk; SCRUM-21/30/35/36/42/53/55/60
dekker visning, rangering, økt, historikk og kostnad. Jira ble lest ved
oppstart: SCRUM-19/20/22 var To Do; SCRUM-47 var In Progress.
Ingen aktivt kodearbeid eller sprintplassering er lagt om.

Modell og kostnadsgrense i SCRUM-59, reell ekstern vikars øvrige arbeid i
SCRUM-19 og skriftlige leveringsavklaringer i SCRUM-49 er fortsatt egne
avklaringer. De hindrer ikke den lokale kjernen: nødvendig manglende
kontrollgrunnlag gir Uavklart, og standardforklaring virker uten modell.

Det finnes ingen lokal epics-/stories-fil eller sprint-statusfil å generere
fra; eksisterende arbeidsoppfølging er i Jira. Denne runden er en
readiness-kontroll og oppretter derfor ingen parallell sprintplan.
Implementeringen følger [spesifikasjonen](spec-scrum-19-demoflyt.md).

Arbeidskopien var ren ved start, på full revisjon
`3277c041f56d08e66232b2408bfd077747c43795`. Arbeidet utføres på lokal gren
`scrum-19-demoflyt` med UX-grunnlaget bevart. Ingen deploy, push eller ekstern
dataendring inngår. Nye detaljvalg føres som Codex-konkretiseringer på mandat;
de er ikke nye felles detaljbeslutninger.
