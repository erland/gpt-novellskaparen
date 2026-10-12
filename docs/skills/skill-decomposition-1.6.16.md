# Novellskaparen – Skill-indelning (GPT Byggaren 1.6.16)
## Källa och migreringsprincip
Basen är `main`, inte den tidigare migrationsgrenen. `canonical/instructions.md` behålls byte-för-byte oförändrad i första migreringssteget som beteendereferens och regression-orakel.
## Fyra ansvar
- `ideutveckling-och-planering`: premiss, synopsis, karaktär, scenplan; producerar inte oombedd färdig novell.
- `novellskrivande`: ny färdig berättelsetext.
- `fortsattning`: nytt material i etablerad berättelse, med kontinuitet.
- `revision`: ändring av befintlig text med begränsat ingrepp.
## Gemensam kärna
Identitet, grundbeteende, val av arbetsläge, prioritering, användarstyrning, målgrupp, språk, genre/ton, originalitet och generella kvalitetskrav är tvärgående. Ingen Skill får ersätta dessa med egna motstridiga varianter.
## Integrationsregel
Den sammanhängande kanoniska instruktionen är fortsatt auktoritativ tills den nya modulära kompileringen implementerats och verifierats. Skill-filerna är funktionsavgränsningar och arbetsinstruktioner, inte en ursäkt för att duplicera hela kanoniska instruktionen.
## Nästa grind
Installera oförändrad originalmotor 1.6.16; inför en kompilator eller motorns stödda assembly-kontrakt; jämför sammanfogad instruktion semantiskt mot denna bas; kör canonical lint, acceptanstester, fem byggen och validering. Uppdatera först därefter CI/release och klassificera migrationen som klar.
