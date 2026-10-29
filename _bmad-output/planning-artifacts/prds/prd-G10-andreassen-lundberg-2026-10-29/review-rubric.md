# PRD-gjennomgang – VaktMatch

*(Claude Code · 29.10.26. Gjennomgang mot BMAD-rubrikken `prd-validation-checklist.md`
og kildene PRD-en bygger på. Utført av samme KI som skrev utkastet, så den er
ikke uavhengig. Odins gjennomgang gjenstår.)*

## Samlet vurdering

PRD-en har en tydelig tese (regelkorrekthet først) og en Må/Bør-deling som
følger av den. Kravene viser til demoscenarioets kontrolltilfeller og blir
dermed testbare. Det største gjenværende problemet er ikke teksten, men at
prioriteringen i §7.2 ikke er avklart med Odin, og at fire antakelser er ubekreftet.

## Beslutningsgrunnlag – god
§7.2 viser hva som er flyttet fra briefen, hvorfor og hvem som besluttet. Åpne
spørsmål i §9 er reelle.

## Innhold fremfor pynt – god
Én konstruert person (Kari), merket som eksempel. Ingen unikhetspåstand.

### Funn
- **medium** NFR-2 og NFR-3 brukte adjektiver («lesbar kontrast», «forståelige
  meldinger»). *Rettet:* WCAG-kontrast 4,5:1, tastatur med synlig fokus, 360 px,
  feilkode med norsk melding og testbare krav i ende-til-ende-testen.

## Strategisk sammenheng – god
Kjernesetningen, SM-1 og motvektsmålene peker samme vei.

### Funn
- **low** Fem-minuttersmålet i visjonen ble ikke målt i noen SM. *Rettet:* tatt inn i SM-5.

## Tydelig «ferdig» – tilstrekkelig
De fleste FR viser til fasit (S, H, F, D).

### Funn
- **medium** FR-8 hadde bare «vises per berørt person». *Rettet:* timer og hvile
  før/etter, flyttetilfellet F2 og A02-eksemplet.
- **medium** FR-18 sa «fast format» uten felt og uten testmodus. *Rettet:* faste
  felt og testmodus uten nøkkel (krav fra teknologivalget).

## Ærlig avgrensning – god
Ikke-mål i §6, avvik i §7.2, fire antakelser indeksert.

### Funn
- **low** Briefens omfang (8–10 ansatte og vikarer) manglet. *Rettet:* tatt inn i FR-1.

## Bruk videre (UX, arkitektur, stories) – god
FR-ID-er er sammenhengende, og hvert krav har Jira-sak.

### Funn
- **low** «Udekket behov» og «økt» ble brukt uten å stå i begrepslisten. *Rettet.*
- **low** SCRUM-53 (økttilstand) var koblet til FR-23. *Rettet:* flyttet til FR-15.

## Form – god
Brukerreiser passer siden appen har reell UX og sensor er en egen «bruker».

## Avstemming mot kildene
- **Sensorveiledningen:** UX-skisser som spor av designarbeid manglet. *Rettet:* krav i NFR-2.
- **Teknologivalg:** testmodus uten nøkkel manglet. *Rettet:* FR-18.
- **Briefens suksesskriterier:** Tilbud/aksept, datasettbytte og varig logg
  dekkes bare som Bør. Dette er forklart i §7.2, men briefen og endringsloggen
  er ikke oppdatert ennå.

## Mekanisk
ID-er FR-1–23, NFR-1–9, SM-1–5 og SM-C1–C3 er sammenhengende. Alle fire
`[ANTAKELSE]` står både i teksten og i §10. Alle relative lenker er kontrollert.

## Etter gjennomgangen
Stian besluttet de fire antakelsene 29.10.26 (låser, økt, KI-handling og flyttingen av låsing til Bør). Åpne spørsmål fikk ansvarlig og tidspunkt.
