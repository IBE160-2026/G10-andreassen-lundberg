# Svar på forslag til felles retning

**Fra:** Stians KI-assistent (Claude Code), på oppfordring i [forslag-til-felles-retning.md](forslag-til-felles-retning.md)
**Til:** Odin og Stian, som beslutningsgrunnlag for gruppen — ikke en godkjenning på vegne av Stian, og ikke en felles gruppebeslutning.
**Dato:** 2026-09-27

Svarene under skiller mellom **hva som allerede står** i turnusgenerator-briefen/dagens productbrief.md, **min tolkning** av hvordan forslagene forholder seg til hverandre, og **nye forslag** jeg legger til.

## 1. Ivaretar sammenslåingen de viktigste intensjonene i turnusgenerator-forslaget?

**Fra briefene:** Turnusgenerator-forslagets kjerneintensjon er en regelbasert optimaliseringsmotor (constraint-solver) som genererer en hel periodeplan, med KI som tolknings-/forklaringslag på toppen — trappet opp mot rettferdighet, myke preferanser, what-if-simulering og rollestyring.

**Min tolkning:** Sammenslåingen beholder selve mekanismen (solver genererer, KI forklarer) fullt ut — det arkitektoniske kjernepoenget er intakt, og det er ikke i konflikt med turnusgenerator-forslaget i seg selv, som selv trappet funksjonalitet opp fra MVP til avansert. Det som forsvinner fra MVP i sammenslåingen er ambisjonsnivået: rettferdighet over tid, fritekst-tolkning, what-if og rollestyring er alle utsatt. Odins forslag legger seg omtrent på turnusgenerator-forslagets MVP-nivå, litt smalere.

**Nytt forslag:** Hvis det å vise fram selve optimaliseringen er viktig for karaktergrunnlaget, bør minst ett mykt hensyn (f.eks. rettferdig fordeling av helgevakter) være med allerede i MVP. Uten et myk-hensyn i objektivfunksjonen degenererer «optimalisering» til et rent constraint-satisfaction-problem (finn *en* gyldig løsning, ikke *den beste*) — og da blir det lite å vise fram utover det en enklere heuristikk også ville løst.

## 2. Er noen av løsningsforslagene teknisk eller produktmessig i konflikt med hverandre?

**Fra Odins forslag:** «Bevar eksisterende plan mest mulig» ved fravær — se etter en direkte erstatter først, og vis konsekvenser før mer omfordeling godkjennes.

**Min tolkning (teknisk spenning jeg ser):** Dette er i reell spenning med hvordan en CP-SAT-solver naturlig oppfører seg. Kjøres solveren på nytt etter et fravær uten videre, optimaliserer den fritt og kan omorganisere hele perioden — stikk i strid med «endre minst mulig». Dette løses ikke automatisk av at «samme regelmotor» brukes begge steder; det krever et eksplisitt ledd i objektivfunksjonen som straffer avvik fra forrige godkjente plan (i praksis et «minimal-endring»-hensyn, forankret i den godkjente planen).

Utover dette ser jeg ingen produktmessige motsetninger — «harde regler skal ikke kunne oppveies av andre hensyn» stemmer godt overens med at harde regler i turnusgenerator-forslaget allerede er tenkt som constraints, ikke objektivledd.

**Nytt forslag:** Legg «minimal endring ved omplanlegging» inn som et eksplisitt punkt i regelsett-/objektivfunksjon-beskrivelsen i den felles briefen, ikke bare underforstått av at én motor brukes til begge steg.

## 3. Hva bør være med i minimumsproduktet for at både turnusgenerering og avvikshåndtering skal gi mening?

**Min tolkning:** Begge funksjonene krever at planen faktisk er «stram» nok til å vise noe interessant:

- For at *generering* skal vise noe utover triviell oppfylling, må minst én hard regel og minst ett mykt hensyn faktisk komme i konflikt i testdataene — ellers løses alt trivielt, og det er ingenting for KI-laget å forklare.
- For at *avvikshåndtering* skal gi mening etter generering, må minst ett scenario i demodataene være tett nok til at en direkte erstatter faktisk ikke finnes — ellers demonstreres aldri «udekket behov»-varselet som allerede står i success-kriteriene i dagens productbrief.md.

**Nytt forslag:** Design demodatasettet bevisst med minst to scenarioer: (a) ett fravær som løses med en ren erstatter, og (b) ett fravær uten gyldig erstatter som utløser et udekket-varsel. Dette bør stå som et eksplisitt krav til testdataene i den felles briefen, ikke overlates til tilfeldighetene i et generert eller håndplukket datasett.

## 4. Hvilke endringer foreslår jeg før gruppen utarbeider en felles produktbrief?

1. **Eksplisitt objektivfunksjon for MVP** — ta med minst ett mykt hensyn (f.eks. rettferdig helgefordeling), se pkt. 1.
2. **Eksplisitt «minimal endring»-hensyn** ved omplanlegging etter fravær, se pkt. 2.
3. **Bevisst utformede demoscenarioer** — én løsbar og én uløsbar fraværssituasjon, se pkt. 3.
4. **Fest periodelengden til to uker i MVP**, ikke «én uke, ev. to». Én ukes horisont gir maks én helg — for tynt til å vise rettferdig fordeling eller ringvirkninger av omplanlegging. To uker er fortsatt trivielt raskt for CP-SAT.
5. **Oppdater dagens productbrief.md sin Solution-seksjon** («KI hjelper med å tolke behovet... i fritekst») slik at den samsvarer med at fritekst-tolkning er utsatt til etter MVP, som foreslått her — ellers lover de to dokumentene mer enn det felles MVP-omfanget faktisk holder.
6. **Behold en eksplisitt, navngitt solver-teknologi** (Google OR-Tools CP-SAT, Python) i scope-delen av den felles briefen. Det er selve begrunnelsen for hvorfor og hvor KI *ikke* brukes til optimaliseringen — uten et navngitt valg mister historien sin konkretisering.

## Oppsummert

Sammenslåingen ivaretar kjernemekanikken i turnusgenerator-forslaget godt, men trenger tre konkrete presiseringer før den kan bli felles brief: et eksplisitt mykt hensyn/objektivfunksjon i MVP, et eksplisitt minimal-endring-hensyn ved omplanlegging, og bevisst utformede demoscenarioer som faktisk tester begge funksjonene. Dette er analyse til samtalen mellom dere to — ikke en beslutning tatt på vegne av noen av dere.
