# Anslått kostnad i VaktMatch-demoen

*(Skrevet: Codex · 30.10.26, som konkretisering av Odins valg i SCRUM-46.)*

Odin valgte at førsteversjonen skal vise anslått kostnad per alternativ med
syntetiske satser og tillegg. Formålet er å gi lederen et økonomisk
sammenligningsgrunnlag sammen med regelkontroll og fordeling av arbeid.
Formelen og kontrolltilfellene nedenfor er Codex sine implementeringsføringer;
de er ikke særskilt detaljgodkjent av begge prosjektdeltakerne.

## Beregningsgrunnlag

- Vis anslått kostnad for de berørte vakttildelingene i alternativet, tilsvarende
  kostnad i gjeldende datagrunnlag og differansen mellom dem. Ved omfordeling
  inngår både målskiftet og vakten personen forlater, for alle berørte ansatte.
- Bruk demotimer × (syntetisk timesats + summen av aktuelle syntetiske
  timetillegg). Del beregningen i tidsintervaller når et tillegg endres i vakten.
  Vis timer, satser, tillegg, valuta og dataversjon. Bruk NOK i demoen.
- Beregn med eksakte desimalverdier og avrund hver tildeling til nærmeste øre
  før summering; ved et halvt øre rundes opp. Tallene skal kunne etterregnes.
- Alle satser og regler for tillegg er fiktive, versjonerte demodata. De bygger
  ikke på reelle lønnsavtaler. Reell overtid, tariffregler, sykefraværskostnad,
  arbeidsgiveravgift og full arbeidsgiverkostnad modelleres ikke. Begrensningen
  vises ved anslaget; utelatte kostnader fremstilles ikke som null.
- Manglende sats, timer eller nødvendig tilleggsgrunnlag gir «kostnad uavklart»
  for den berørte beregningen. En kjent delsum kan vises med tydelig merking,
  men ikke som et fullstendig totalanslag eller en kjent differanse.
- Kostnad er et eget sammenligningsfelt og endrer ikke P1/P2 eller R1–R5.
  Delvis dekning eller regelavvik skal fortsatt være synlig ved siden av beløpet.
  Et udekket alternativ fremstilles ikke som en billig, komplett løsning.
- Ved ny dataversjon eller endret forslag beregnes kostnaden på nytt.
  Standard- og KI-forklaringer bruker det beregnede resultatet; KI finner ikke
  på satser, tillegg, besparelser eller nye kostnadsregler.

## Kontrolltilfeller

Alle beløp og roller her er konstruerte eksempler. Komplette demodata gjenstår.

| ID | Oppsett | Forventet resultat |
|---|---|---|
| O1 Direkte erstatning | En udekket åttetimersvakt får en kandidat med timesats 200 og timetillegg 25. Gjeldende berørte aktive tildelinger har anslag 0; fraværskostnad er utenfor modellen. | Alternativets anslag er 1 800 NOK, differanse +1 800 NOK. Utelatt fraværskostnad og syntetiske satser er synlig. |
| O2 Omfordeling | B har åtte timer på Y til sats 200. B flyttes til udekket X med samme sats og tillegg 25; C dekker Y til sats 180. | Referanse 1 600 NOK. Nytt anslag 1 800 + 1 440 = 3 240 NOK, differanse +1 640 NOK. Begge vakter og begge ansatte inngår. |
| O3 Manglende grunnlag | O2, men Cs sats mangler. | Fullstendig total og differanse er uavklart. En eventuell delsum merkes som ufullstendig. Regelstatus og rangering endres ikke av manglende sats. |
| O4 Ny dataversjon | Satsen eller tillegget i O1 endres i et oppdatert datasett. | Nytt beløp, dataversjon og endret beregningsgrunnlag vises. Gammel forklaring gjelder ikke som ny vurdering. |
| O5 Tilleggsgrense og avrunding | To av åtte timer har tillegg 25 ved grunnsats 200. En separat én-times tildeling har beregnet beløp 200,005. | Første anslag er 1 650 NOK. Det separate beløpet avrundes til 200,01 NOK. |

## Sporbarhet

Kravet står i PRD FR-24 og [SCRUM-60](https://stiodi.atlassian.net/browse/SCRUM-60). [Produktbriefens endringslogg](productbrief-endringslogg.md#301026--komplett-demoflyt-og-presisert-merverdi)
registrerer kilde, før/etter og beslutningsstatus. [Demoscenarioet](demoscenario-fravaer.md)
beskriver fravær, forslag, tilbud og datasettbytte som kostnadsanslaget følger.
