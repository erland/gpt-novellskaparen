# Utvecklingsplan – Novellskaparen

**Projekt:** Novellskaparen  
**Projekt-id:** `novellskaparen`  
**Profil:** `simple`  
**Planversion:** 2  
**Utgångspunkt:** GPT Byggaren 1.2.1, migreras till GPT Byggaren 1.5.0

## Mål

Bygga en kreativ skriv-GPT som kan ta en enkel idé eller en detaljerad brief till en färdig, originell novell. GPT:n ska kunna anpassa språk, innehåll, dramaturgi, tonalitet och komplexitet efter målgrupp, vara självgående när tillräcklig information finns och kunna samarbeta stegvis när användaren vill utveckla berättelsen tillsammans.

Alla aktiva runtime-distributioner ska byggas från samma canonical beteendekontrakt. Chat ZIP och Custom GPT finns redan; Claude Projects bedöms som en kompatibel peer-runtime och införs i migreringsstegen.

## Arkitekturbeslut

- Projektprofil: `simple`.
- Canonical instruktion är primär källa för allt kritiskt beteende.
- Ingen obligatorisk Knowledge-bas i första versionen.
- Ingen webbsökning krävs för kärnflödet.
- Inga runtime-schemas eller scripts behövs för själva novellskapandet.
- Bildgenerering kan stödjas som kompletterande funktion för illustrationer, men ligger utanför kärnflödet.
- GitHub Actions för CI och release-byggning ingår som standard.
- Release-taggen ska styra versionsnumret för releaseartefakter.
- Projektet ska efter varje genomfört steg kunna byggas till en komplett projekt-ZIP.

---

## Steg 1 – Initiera projektet och skapa canonical kärna

### Mål

Skapa den första kompletta projektstrukturen och formulera Novellskaparens canonical instruktion utifrån den gamla instruktionen och den beslutade målbilden.

### Leveranser

- Grundläggande projektstruktur.
- `README.md`.
- `PROJECT.md`.
- `STATUS.md`.
- `gpt-project.yaml`.
- `project-status.yaml`.
- `docs/development-plan.md`.
- Canonical instruktion för Novellskaparen.
- Första kompletta projekt-ZIP:en.

### Canonical instruktionen ska minst definiera

- identitet och syfte,
- när GPT:n ska fråga och när den ska skriva direkt,
- målgruppsanpassning,
- genre och tonalitet,
- längdtolkning,
- originalitet,
- dramaturgiska kvalitetskrav,
- hur kreativa luckor fylls i,
- hantering av befintliga berättelser,
- upphovsrättsliga gränser,
- avslutande fortsättningsmöjligheter utan att bli mekanisk.

### Validering

- Kritiska beteenderegler finns i canonical instruktionen.
- Kärnflödet kräver ingen Knowledge-fil.
- Instruktionen är tillräckligt komplett för att kunna testas fristående.
- Projektstatus och plan är synkroniserade.

### Klart när

- projektstrukturen finns,
- canonical instruktionen är användbar,
- projektstatus visar steg 1 som klart,
- project hygiene är bedömd,
- en komplett projekt-ZIP kan levereras.

---

## Steg 2 – Förfina arbetsflödet för nya noveller

### Mål

Göra beteendet för ny novell konsekvent, smidigt och självgående.

### Funktioner som ska definieras

- Avgör om användarens brief redan är tillräcklig.
- Fråga bara efter verkligt avgörande information.
- Fyll automatiskt i mindre kreativa luckor.
- Skapa en intern berättelseplan innan längre berättelser skrivs.
- Anpassa planeringsdjupet efter berättelsens längd och komplexitet.
- Skriv direkt när användaren uttryckligen vill ha en färdig berättelse.
- Undvik att visa intern planering om den inte hjälper användaren.

### Testfall

Minst följande scenarier ska provas:

1. Mycket detaljerad brief – inga onödiga frågor.
2. Kort men tillräcklig brief – GPT:n fyller i detaljer själv.
3. Otillräcklig brief där målgrupp saknas och är avgörande – relevant fråga ställs.
4. Användaren anger exakt ordantal – detta går före standardlängd.
5. Användaren ber bara GPT:n hitta på något – GPT:n kan vara kreativ utan frågeformulär.

### Klart när

- frågebeteendet är konsekvent,
- GPT:n inte fastnar i slentrianmässig informationsinsamling,
- samtliga kärnscenarier ger förväntat beteende,
- canonical instruktion och status är uppdaterade,
- ny projekt-ZIP kan byggas.

---

## Steg 3 – Förfina målgrupp, ton och innehållsnivå

### Mål

Göra målgruppsanpassningen kvalitativ snarare än enbart språklig.

### Områden

För målgrupperna:

- lågstadiet,
- mellanstadiet,
- tonåring,
- vuxen,

ska GPT:n anpassa:

- språk och meningsbyggnad,
- berättelsens komplexitet,
- konflikt och spänningsnivå,
- emotionellt djup,
- graden av antydan och undertext,
- dialog,
- tempo,
- teman,
- hur mycket läsaren själv förväntas tolka.

### Särskilda principer

- Barnberättelser ska inte automatiskt bli moraliserande.
- “Mörk” eller “spännande” ska tolkas olika beroende på målgrupp.
- Tonalitet ska hållas jämn genom hela berättelsen.
- Användarens uttryckliga innehållsönskemål går före standardantaganden när de är lämpliga för målgruppen och tillåtna.

### Testfall

Samma grundidé skrivs för minst två olika målgrupper och ska tydligt skilja sig i språk, struktur och emotionell komplexitet.

### Klart när

- målgruppsanpassningen märks i mer än ordval,
- ton och komplexitet är konsekventa,
- relevanta testfall passerar,
- projektstatus och ZIP är uppdaterade.

---

## Steg 4 – Lägg till skrivpartnerlägen

### Mål

Utöka Novellskaparen från ren berättelsegenerator till flexibel skrivpartner.

### Lägen som ska stödjas

- utveckla en lös idé,
- skapa premiss,
- skapa synopsis,
- utveckla karaktärer,
- skapa berättelse- eller scenplan,
- fortsätta en befintlig berättelse,
- bygga ut en kort text,
- revidera en befintlig novell,
- förbättra dialog,
- förbättra tempo,
- förbättra gestaltning och miljö,
- föreslå eller förbättra avslut.

### Viktig regel

GPT:n ska förstå användarens avsikt från begäran och inte tvinga användaren att välja ett formellt “läge”.

### Klart när

- samtliga centrala skrivpartnerfunktioner fungerar från naturliga instruktioner,
- GPT:n bevarar etablerade fakta, karaktärer och tonalitet vid fortsatt skrivande,
- canonical instruktion och tester är uppdaterade,
- ny projekt-ZIP finns.

---

## Steg 5 – Förbättra litterär kvalitet och revisionsbeteende

### Mål

Höja kvaliteten så att berättelserna inte bara är korrekta utan också känns medvetet skrivna.

### Kvalitetsområden

- tydlig men inte mekanisk dramaturgi,
- levande miljöer,
- karaktärer med mål och drivkrafter,
- dialog med funktion,
- variation i tempo,
- gestaltning där det passar bättre än förklaring,
- undvikande av upprepningar och övertydlighet,
- konsekvent perspektiv,
- tydligt men inte nödvändigtvis överförklarat slut,
- naturliga övergångar.

### Revision

Vid revision ska GPT:n:

- bevara sådant användaren inte bett den ändra,
- prioritera de efterfrågade förbättringarna,
- kunna göra både lätt språkputs och djupare omskrivning,
- inte utan skäl förändra berättelsens kärna.

### Testfall

- förbättra dialog utan att ändra handlingen,
- höj spänningen utan att skriva om hela berättelsen,
- korta en text med bibehållen kärna,
- gör en berättelse mer gestaltande,
- förbättra ett svagt slut.

### Klart när

- revisionsbeteendet är precist,
- centrala litterära kvalitetsproblem fångas upp,
- regressionstester inte visar försämrat grundbeteende,
- ZIP och status är uppdaterade.

---

## Steg 6 – Hantera originalitet, inspirationsönskemål och kontinuitet

### Mål

Säkerställa att Novellskaparen kan hantera inspiration från befintliga verk eller författare utan att bli en direkt imitation, samtidigt som återkommande egna karaktärer och världar fungerar.

### Funktioner

- skapa originella berättelser,
- omvandla för nära inspirationsönskemål till mer generell känsla, tema eller berättarteknik,
- undvika reproduktion av skyddade berättelser,
- behålla kontinuitet i en pågående användarskapad berättelse,
- kunna skapa uppföljare med etablerade karaktärer och fakta.

### Klart när

- relevanta gränsfall ger säkert och användbart beteende,
- fortsatt skrivande bibehåller kontinuitet,
- instruktion och testfall är uppdaterade,
- projekt-ZIP kan byggas utan fel.

---

## Steg 7 – Skapa Chat ZIP och Custom GPT-distributioner

### Mål

Kompilera båda distributionsmålen från samma canonical källa.

### Chat ZIP

Ska minst innehålla:

- tydlig `START-HERE.md`,
- runtimeinstruktion,
- nödvändiga policies eller referenser,
- versionsinformation,
- manifest.

### Custom GPT

Ska minst innehålla:

- kompilerad instruktion inom plattformens gränser,
- namn och beskrivning,
- rekommenderade conversation starters,
- rekommenderade capabilities,
- tydlig information om eventuella skillnader mot Chat ZIP.

### Rekommenderade capabilities

- Bildgenerering: på, för valfria illustrationer.
- Webbsökning: inte nödvändig för kärnfunktionen.
- Dataanalys/kod: inte nödvändig för kärnfunktionen.

### Validering

- Båda distributionerna härleds från samma canonical beteendekontrakt.
- Kritiska beteenden finns i båda.
- Eventuella verkliga plattformsskillnader dokumenteras.

### Klart när

- Chat ZIP byggs och valideras,
- Custom GPT-paketet byggs och valideras,
- runtime-paritet är bedömd,
- komplett projekt-ZIP är uppdaterad.

---

## Steg 8 – Lägg till CI och release-byggning

### Mål

Göra projektet reproducerbart och enkelt att releasa via GitHub.

### Leveranser

- GitHub Actions för CI.
- GitHub Actions för release-byggning.
- Lint/validering av projektstrukturen.
- Byggning av Chat ZIP och Custom GPT-artefakter.
- Release-taggen används som versionskälla.
- Dokumenterad lokal byggväg.

### Klart när

- CI-konfigurationen validerar projektet,
- release-workflow kan bygga distributionsartefakter från en tagg,
- versionshanteringen är konsekvent,
- README beskriver bygg- och releaseflödet,
- projekt-ZIP är uppdaterad.

---

## Steg 9 – GPT Byggaren 1.5-kontrakt och lightweight modellrobusthet

### Mål

Migrera projektmodellen till GPT Byggaren 1.5.0 utan att ändra Novellskaparens domänbeteende.

### Leveranser

- explicit bedömning av ChatGPT Chat, Custom GPT, Claude Projects, OpenCode och OpenAI Plugin,
- capability-, artifact-, workspace/state- och tool-kontrakt,
- modellrobusthetsnivå `lightweight`,
- instruction-adherence-evals för kritiskt beteende,
- plattformsneutrala kontrakts- och eval-schemas.

### Klart när

- befintlig canonical instruktion är oförändrad,
- kärnbeteendet kräver högst ett obligatoriskt filhopp och ingen Knowledge-fil,
- fyra instruction-adherence-evals finns,
- befintliga tester och distributioner inte regresserar,
- CI passerar.

---

## Steg 10 – Lägg till Claude Projects som peer-distribution

### Mål

Bygga Claude Projects från samma canonical kontrakt utan att införa Claude-specifikt domänbeteende.

### Klart när

- Claude Projects innehåller Project Instructions och runtime-kontrakt,
- Chat, Custom GPT och Claude Projects bär samma kritiska kärnbeteende,
- distributionsvalideringen passerar.

---

## Steg 11 – Generalisera runtime parity och releasekedjan

### Mål

Utöka build, parity, validering och release readiness till GPT Byggaren 1.5-modellen.

### Klart när

- aktiva peer-runtimes jämförs för behavior, capability, artifact, workspace/state och tool,
- OpenCode och OpenAI Plugin har explicit reducerad/inaktiv status,
- releaseartefakter, checksummor och delivery manifest täcker aktiva distributioner,
- CI och release-workflow passerar.

---

## Steg 12 – Sluttest, hygiene och release readiness

### Mål

Verifiera helheten innan första stabila release.

### Sluttest ska täcka

- ny novell från minimal idé,
- ny novell från detaljerad brief,
- barn- och vuxenanpassning,
- olika genrer och toner,
- kort, medel och explicit ordantal,
- idéutveckling,
- planering,
- fortsatt berättelse,
- revision,
- uppföljare och kontinuitet,
- inspirationsönskemål nära befintliga verk,
- Chat ZIP,
- Custom GPT,
- Claude Projects,
- runtime parity och release-readiness för alla registrerade runtimes.

### Project hygiene

- inga överflödiga genererade filer,
- inga dubbletter eller föråldrade instruktioner,
- canonical källa är tydlig,
- dokumentationen speglar verkligt projektläge,
- statusfiler är synkroniserade,
- distributionerna innehåller bara avsedda filer.

### Release readiness

Blockerande fel ska rättas innan projektet betraktas som releaseklart. Icke-blockerande skillnader eller begränsningar ska dokumenteras.

### Klart när

- tester och valideringar passerar,
- final hygiene passerar,
- runtime-paritet är accepterad,
- release readiness är godkänd,
- projektet kan märkas som första stabila version.

---

## Förväntad fortsatt arbetsgång

Efter denna plan kan fortsatt utveckling normalt ske genom att användaren skriver:

> Gör nästa steg

GPT Byggaren ska då läsa faktisk projektstatus och utföra nästa lämpliga steg. Planens nummer är vägledande; blockerare, valideringsfel eller nödvändiga korrigeringssteg går före ett mekaniskt nästa nummer.

## Nästa steg enligt nuvarande status

Samtliga steg 1–12 är genomförda och verifierade. Projektet är i förvaltningsläge efter migreringen till GPT Byggaren 1.5.0.
