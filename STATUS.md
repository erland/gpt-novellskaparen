# Status – Novellskaparen

## Sammanfattning

Steg 1–8 är genomförda. Migrering till **GPT Byggaren 1.5.0** pågår i steg 9.

Novellskaparens canonical domänbeteende bevaras. Migreringen lägger först till plattformsneutrala kontrakt, explicit runtime-bedömning och `lightweight` modellrobusthet. Claude Projects, generaliserad runtime parity och uppdaterad releasekedja hanteras i efterföljande steg.

## Genomförda steg

- [x] Steg 1 – Initiera projektet och skapa canonical kärna
- [x] Steg 2 – Förfina arbetsflödet för nya noveller
- [x] Steg 3 – Förfina målgrupp, ton och innehållsnivå
- [x] Steg 4 – Lägg till skrivpartnerlägen
- [x] Steg 5 – Förbättra litterär kvalitet och revisionsbeteende
- [x] Steg 6 – Hantera originalitet, inspirationsönskemål och kontinuitet
- [x] Steg 7 – Skapa Chat ZIP och Custom GPT-distributioner
- [x] Steg 8 – Lägg till CI och release-byggning
- [ ] Steg 9 – GPT Byggaren 1.5-kontrakt och lightweight modellrobusthet
- [ ] Steg 10 – Lägg till Claude Projects som peer-distribution
- [ ] Steg 11 – Generalisera runtime parity och releasekedjan
- [ ] Steg 12 – Sluttest, hygiene och release readiness

## GPT Byggaren 1.5-migrering

Steg 9 omfattar:

- explicit peer-bedömning av ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin,
- capability-, artifact-, workspace/state- och tool-kontrakt,
- `lightweight` modellrobusthetsprofil,
- instruction-adherence-evals för minimal brief, uttryckliga begränsningar, revisionsscope och originalitet.

Claude Projects är bedömd som `ready` men hålls avsiktligt avstängd tills steg 10 bygger och validerar distributionen. OpenCode och OpenAI Plugin är `reduced` och aktiveras inte som standard.

## Befintlig CI och release

- CI kör lint, tester, distribution build och distribution validation.
- CI verifierar reproducerbarhet genom två identiska byggen och jämförelse av SHA-256-summor.
- Projekt-, Chat- och Custom GPT-ZIP får versionssatta filnamn.
- GitHub Release-taggen styr releaseversionen.

## Nästa rekommenderade steg

Slutför **steg 9** genom att låta CI verifiera migreringsändringarna. Först när CI är grön markeras steg 9 som klart och nästa rekommenderade steg blir Claude Projects-distributionen.

## Blockerare

Inga kända blockerare före CI-verifieringen.
