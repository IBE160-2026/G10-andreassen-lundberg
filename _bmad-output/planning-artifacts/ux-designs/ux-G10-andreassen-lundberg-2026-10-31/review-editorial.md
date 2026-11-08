# Struktur- og språkkontroll – SCRUM-47

KI-kontroll 08.11.2026 med `bmad-review`, linsene `structure` og deretter
`prose`. Kontrollert innhold: [DESIGN.md](DESIGN.md),
[EXPERIENCE.md](EXPERIENCE.md) og [implementeringsoverleveringen](implementation-handoff.md).
Formålet er at utviklere kan slå opp visuelle regler, oppførsel og arbeidsrekkefølge.

## Struktur

Referansemodellen passer de to UX-kontraktene; overleveringen følger en
lineær arbeidsrekkefølge. Komponenttabeller, avvikstilstander og brukerreiser
beholdes: de støtter ulike oppslag, selv der dataversjon og uendret vaktliste
gjentas. Ingen strukturelle kutt anbefalt. Målingen før språkpasset var
4 463 ord samlet, inkludert frontmatter; anbefalt reduksjon var 0 ord.

## Språk

| Pass | Opprinnelig tekst | Rettelse | Resultat |
|---|---|---|---|
| prose | «Bare komplett, bestått forslag på gjeldende grunnlag kan markeres som bestått valg.» | «Bare et komplett forslag som oppfyller scenarioreglene på gjeldende grunnlag, kan markeres som valgt.» | Rettet i `alternative-detail`; kontroll og valg har separate begreper. |
| prose | «Perioden bruker startvaktens lokale dato til midnatt etter siste kalenderdag i Europe/Oslo.» | «Perioden går fra midnatt på startvaktens lokale dato til midnatt etter siste kalenderdag i Europe/Oslo.» | Rettet i `affected-shifts`; startgrensen er uttrykkelig. |

Ingen utestående rettelser fra disse to linsene. Denne kontrollen vurderer
formidling og struktur, ikke korrekte regelberegninger eller brukbarhet hos faktiske brukere.
