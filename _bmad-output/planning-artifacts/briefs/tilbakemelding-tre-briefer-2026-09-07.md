# Tilbakemelding på tre produktbriefer

Dato: 2026-09-07. Lest: brief.md, addendum.md og beslutningslogg for VaktMatch, Forplanner og PantBuddy i planning-artifacts/briefs. Vurderingen gjelder produktargumentasjon, avgrensning og indre konsistens; konkurranse- og regelverkspåstander er ikke eksternt faktasjekket i denne gjennomgangen. Åpne spørsmål er innspill til videre avklaring, ikke krav om at briefen skal være en full implementasjonsspesifikasjon.

## Produktargumentasjon

**VaktMatch — Scope / The Solution**

- Funn: Generatoren lover et gyldig ukesgrunnlag uten definert utfall ved umulig bemanning.
- Forslag: Definer delvis plan med udekkede skift, eller tydelig stopp med årsak.
- Konsekvens: Demoen kan bli avhengig av spesielt tilrettelagte data.

**VaktMatch — The Solution / addendum: Åpne valg**

- Funn: Rangering og rettferdighet loves, men kriteriene står åpne.
- Forslag: Velg ett rangeringsprinsipp og vis sammenligning av to gyldige kandidater.
- Konsekvens: Anbefalingen kan fremstå vilkårlig.

**VaktMatch — Success Criteria**

- Funn: Raskere beslutninger loves uten sammenligningsgrunnlag.
- Forslag: La en testperson løse samme avvik manuelt og i appen; vurder tid og forståelse.
- Konsekvens: Demoen underbygger ikke forbedringspåstanden.

**VaktMatch — addendum: Leverandøragnostisk lag**

- Funn: Syntetisk arbeidsplass sies å omgå manglende brukerkunnskap helt.
- Forslag: Skill mellom bortfalt integrasjonsbehov og fortsatt antatt brukerbehov.
- Konsekvens: Arbeidsflyten kan bomme på lederens faktiske behov.

**PantBuddy — What Makes This Different / addendum: Landskap**

- Funn: Begrenset søk brukes som bevis for at konkurrenter mangler funksjoner.
- Forslag: Skriv ikke funnet i undersøkt materiale; skill observasjon fra antatt fravær.
- Konsekvens: Differensieringen hevdes sikrere enn kildegrunnlaget tillater.

**PantBuddy — KI-funksjonen / Vision**

- Funn: Det er uklart hva som bekrefter at en henting faktisk skjedde.
- Forslag: Tell fullførte hentinger; definer bekreftelse og behandling av delvis eller avlyst henting.
- Konsekvens: Anslag kan inkludere pant som aldri ble overlevert.

**PantBuddy — KI-funksjonen**

- Funn: Kjente gjennomsnittstall for poser og sekker mangler angitt grunnlag.
- Forslag: Bruk eksplisitte demoantakelser inntil kalibrering; vurder verdiintervall.
- Konsekvens: Samme verdi kan tilskrives svært ulike mengder.

**PantBuddy — What Makes This Different / Success Criteria**

- Funn: KI-oppsummeringens brukerverdi testes ikke av suksesskriteriene.
- Forslag: Sammenlign KI-oppsummering med talloversikt i brukertest.
- Konsekvens: KI-funksjonen kan mangle dokumenterbar nytte.

**PantBuddy — Scope / The Solution**

- Funn: Forbindelsen mellom privat innsamler og laget vedkommende henter for er uavklart.
- Forslag: Avgrens lagrollen og tilordne hver henting til privatperson eller ett lag.
- Konsekvens: Uventet medlemskapsarbeid og feilførte bidrag.

**Forplanner — Executive Summary / Success Criteria**

- Funn: Med/uten-BMAD-sammenligning skiller ikke metode fra læring og endrede verktøy.
- Forslag: Beskriv kvalitativ refleksjon og dokumenter forskjeller i erfaring, omfang og verktøy.
- Konsekvens: Forbedringer kan feilaktig tilskrives BMAD.

**Forplanner — Uavklarte blokkere / Scope**

- Funn: Bare én blokker omtales som åpen, men MVP-kjernefunksjonen er ikke valgt.
- Forslag: Vis domeneavklaring og valg av konkret leveranse som separate åpne beslutninger.
- Konsekvens: Gruppen kan mangle felles forståelse av leveransen.

**Forplanner — addendum: KI-utkast og testeksempel**

- Funn: Årstall antas i fasiten, og Legg inn vises ved nødvendige uavklarte felt.
- Forslag: Angi referansedato i testen og sperr godkjenning til nødvendige felt er avklart.
- Konsekvens: Eksemplet kan legitimere datogjetting og ufullstendig lagring.

## Grensetilfeller

**VaktMatch — Scope / The Solution**

- Funn: Bemanningsbehovet kan ikke dekkes ved generering.
- Forslag: Definer stopp eller delvis plan med årsaker.
- Konsekvens: Hovedflyten mangler definert starttilstand.

**VaktMatch — The Solution**

- Funn: Hviletidskontroll ved ukegrensen mangler nabovakter utenfor grunnlaget.
- Forslag: Ta med nødvendig historikk og neste vakt, eller merk kontrollen uavklart.
- Konsekvens: Hviletid kan fremstå kontrollert uten datagrunnlag.

**PantBuddy — The Solution**

- Funn: Flere vil hente samme annonse, eller bekreftet henting avlyses eller uteblir.
- Forslag: Definer reservasjon, bekreftelse og gjenåpning.
- Konsekvens: Flere møter opp, eller pant blir utilgjengelig uten henting.

**PantBuddy — The Solution / KI-funksjonen**

- Funn: Partene er uenige om henting er gjennomført.
- Forslag: Definer bekreftelse før bidrag telles og vurdering åpnes.
- Konsekvens: Ugjennomførte hentinger kan gi bidrag og vurderinger.

**Forplanner — The Solution**

- Funn: Avrunding til bestillingstrinn overskrider kompatibel silokapasitet.
- Forslag: Vis bestillingen som uløst med årsak.
- Konsekvens: Foreslått bestilling kan være umulig å motta.

Overlapp: umulig ukesgrunnlag og bekreftelse av panthenting dukker opp i begge gjennomgangene; funnene er bevart fordi de belyser både produktløfte og atferd.

## Dokumentstruktur

| Pass | Original Text | Revised Text | Changes |
|---|---|---|---|
| structure | VaktMatch — Executive Summary / The Solution | MOVE: Presenter generert ukesgrunnlag sammen med avviksflyten i sammendraget. | Generatoren er vesentlig byggearbeid som nå introduseres senere. Omtrent 0 ord netto. |
| structure | Forplanner — innledning / Uavklarte blokkere | CONDENSE gjeldende status; MOVE avsluttede blokkere til addendum. | Behold interesse og omfang synlig. Anslått 110 færre ord i brief; historikk bevares. |
| structure | PantBuddy — What Makes This Different | CONDENSE Infinitum-drøftingen til konklusjon og henvisning til addendum. | Detaljert argumentasjon gjentas fra vedlegget. Anslått 120 færre ord. |
| structure | PantBuddy — addendum: Landskap og sammenlignbare konsepter | MOVE til underoverskrifter for norske tilbud, internasjonale tilbud, tillit, pantelapper og ubekreftede funn. | Gjør grunnlaget lettere å finne igjen. Omtrent 0 ord netto. |
| structure | Forplanner — addendum: KI-flyt og utkast | PRESERVE diagram og eksempel. | Konkretiserer tolkning, kontroll og godkjenning uten domenekunnskap. Ingen reduksjon. |

## Maskinlesbare funn

```json
[
  {
    "lens": "adversarial",
    "location": "VaktMatch — Scope / The Solution",
    "trigger_condition": "Generatoren lover et gyldig ukesgrunnlag uten definert utfall ved umulig bemanning.",
    "guard_snippet": "Definer delvis plan med udekkede skift, eller tydelig stopp med årsak.",
    "potential_consequence": "Demoen kan bli avhengig av spesielt tilrettelagte data."
  },
  {
    "lens": "adversarial",
    "location": "VaktMatch — The Solution / addendum: Åpne valg",
    "trigger_condition": "Rangering og rettferdighet loves, men kriteriene står åpne.",
    "guard_snippet": "Velg ett rangeringsprinsipp og vis sammenligning av to gyldige kandidater.",
    "potential_consequence": "Anbefalingen kan fremstå vilkårlig."
  },
  {
    "lens": "adversarial",
    "location": "VaktMatch — Success Criteria",
    "trigger_condition": "Raskere beslutninger loves uten sammenligningsgrunnlag.",
    "guard_snippet": "La en testperson løse samme avvik manuelt og i appen; vurder tid og forståelse.",
    "potential_consequence": "Demoen underbygger ikke forbedringspåstanden."
  },
  {
    "lens": "adversarial",
    "location": "VaktMatch — addendum: Leverandøragnostisk lag",
    "trigger_condition": "Syntetisk arbeidsplass sies å omgå manglende brukerkunnskap helt.",
    "guard_snippet": "Skill mellom bortfalt integrasjonsbehov og fortsatt antatt brukerbehov.",
    "potential_consequence": "Arbeidsflyten kan bomme på lederens faktiske behov."
  },
  {
    "lens": "adversarial",
    "location": "PantBuddy — What Makes This Different / addendum: Landskap",
    "trigger_condition": "Begrenset søk brukes som bevis for at konkurrenter mangler funksjoner.",
    "guard_snippet": "Skriv ikke funnet i undersøkt materiale; skill observasjon fra antatt fravær.",
    "potential_consequence": "Differensieringen hevdes sikrere enn kildegrunnlaget tillater."
  },
  {
    "lens": "adversarial",
    "location": "PantBuddy — KI-funksjonen / Vision",
    "trigger_condition": "Det er uklart hva som bekrefter at en henting faktisk skjedde.",
    "guard_snippet": "Tell fullførte hentinger; definer bekreftelse og behandling av delvis eller avlyst henting.",
    "potential_consequence": "Anslag kan inkludere pant som aldri ble overlevert."
  },
  {
    "lens": "adversarial",
    "location": "PantBuddy — KI-funksjonen",
    "trigger_condition": "Kjente gjennomsnittstall for poser og sekker mangler angitt grunnlag.",
    "guard_snippet": "Bruk eksplisitte demoantakelser inntil kalibrering; vurder verdiintervall.",
    "potential_consequence": "Samme verdi kan tilskrives svært ulike mengder."
  },
  {
    "lens": "adversarial",
    "location": "PantBuddy — What Makes This Different / Success Criteria",
    "trigger_condition": "KI-oppsummeringens brukerverdi testes ikke av suksesskriteriene.",
    "guard_snippet": "Sammenlign KI-oppsummering med talloversikt i brukertest.",
    "potential_consequence": "KI-funksjonen kan mangle dokumenterbar nytte."
  },
  {
    "lens": "adversarial",
    "location": "PantBuddy — Scope / The Solution",
    "trigger_condition": "Forbindelsen mellom privat innsamler og laget vedkommende henter for er uavklart.",
    "guard_snippet": "Avgrens lagrollen og tilordne hver henting til privatperson eller ett lag.",
    "potential_consequence": "Uventet medlemskapsarbeid og feilførte bidrag."
  },
  {
    "lens": "adversarial",
    "location": "Forplanner — Executive Summary / Success Criteria",
    "trigger_condition": "Med/uten-BMAD-sammenligning skiller ikke metode fra læring og endrede verktøy.",
    "guard_snippet": "Beskriv kvalitativ refleksjon og dokumenter forskjeller i erfaring, omfang og verktøy.",
    "potential_consequence": "Forbedringer kan feilaktig tilskrives BMAD."
  },
  {
    "lens": "adversarial",
    "location": "Forplanner — Uavklarte blokkere / Scope",
    "trigger_condition": "Bare én blokker omtales som åpen, men MVP-kjernefunksjonen er ikke valgt.",
    "guard_snippet": "Vis domeneavklaring og valg av konkret leveranse som separate åpne beslutninger.",
    "potential_consequence": "Gruppen kan mangle felles forståelse av leveransen."
  },
  {
    "lens": "adversarial",
    "location": "Forplanner — addendum: KI-utkast og testeksempel",
    "trigger_condition": "Årstall antas i fasiten, og Legg inn vises ved nødvendige uavklarte felt.",
    "guard_snippet": "Angi referansedato i testen og sperr godkjenning til nødvendige felt er avklart.",
    "potential_consequence": "Eksemplet kan legitimere datogjetting og ufullstendig lagring."
  },
  {
    "lens": "edge-case-hunter",
    "location": "VaktMatch — Scope / The Solution",
    "trigger_condition": "Bemanningsbehovet kan ikke dekkes ved generering.",
    "guard_snippet": "Definer stopp eller delvis plan med årsaker.",
    "potential_consequence": "Hovedflyten mangler definert starttilstand."
  },
  {
    "lens": "edge-case-hunter",
    "location": "VaktMatch — The Solution",
    "trigger_condition": "Hviletidskontroll ved ukegrensen mangler nabovakter utenfor grunnlaget.",
    "guard_snippet": "Ta med nødvendig historikk og neste vakt, eller merk kontrollen uavklart.",
    "potential_consequence": "Hviletid kan fremstå kontrollert uten datagrunnlag."
  },
  {
    "lens": "edge-case-hunter",
    "location": "PantBuddy — The Solution",
    "trigger_condition": "Flere vil hente samme annonse, eller bekreftet henting avlyses eller uteblir.",
    "guard_snippet": "Definer reservasjon, bekreftelse og gjenåpning.",
    "potential_consequence": "Flere møter opp, eller pant blir utilgjengelig uten henting."
  },
  {
    "lens": "edge-case-hunter",
    "location": "PantBuddy — The Solution / KI-funksjonen",
    "trigger_condition": "Partene er uenige om henting er gjennomført.",
    "guard_snippet": "Definer bekreftelse før bidrag telles og vurdering åpnes.",
    "potential_consequence": "Ugjennomførte hentinger kan gi bidrag og vurderinger."
  },
  {
    "lens": "edge-case-hunter",
    "location": "Forplanner — The Solution",
    "trigger_condition": "Avrunding til bestillingstrinn overskrider kompatibel silokapasitet.",
    "guard_snippet": "Vis bestillingen som uløst med årsak.",
    "potential_consequence": "Foreslått bestilling kan være umulig å motta."
  },
  {
    "lens": "structure",
    "Pass": "structure",
    "Original Text": "VaktMatch — Executive Summary / The Solution",
    "Revised Text": "MOVE: Presenter generert ukesgrunnlag sammen med avviksflyten i sammendraget.",
    "Changes": "Generatoren er vesentlig byggearbeid som nå introduseres senere. Omtrent 0 ord netto."
  },
  {
    "lens": "structure",
    "Pass": "structure",
    "Original Text": "Forplanner — innledning / Uavklarte blokkere",
    "Revised Text": "CONDENSE gjeldende status; MOVE avsluttede blokkere til addendum.",
    "Changes": "Behold interesse og omfang synlig. Anslått 110 færre ord i brief; historikk bevares."
  },
  {
    "lens": "structure",
    "Pass": "structure",
    "Original Text": "PantBuddy — What Makes This Different",
    "Revised Text": "CONDENSE Infinitum-drøftingen til konklusjon og henvisning til addendum.",
    "Changes": "Detaljert argumentasjon gjentas fra vedlegget. Anslått 120 færre ord."
  },
  {
    "lens": "structure",
    "Pass": "structure",
    "Original Text": "PantBuddy — addendum: Landskap og sammenlignbare konsepter",
    "Revised Text": "MOVE til underoverskrifter for norske tilbud, internasjonale tilbud, tillit, pantelapper og ubekreftede funn.",
    "Changes": "Gjør grunnlaget lettere å finne igjen. Omtrent 0 ord netto."
  },
  {
    "lens": "structure",
    "Pass": "structure",
    "Original Text": "Forplanner — addendum: KI-flyt og utkast",
    "Revised Text": "PRESERVE diagram og eksempel.",
    "Changes": "Konkretiserer tolkning, kontroll og godkjenning uten domenekunnskap. Ingen reduksjon."
  }
]
```

