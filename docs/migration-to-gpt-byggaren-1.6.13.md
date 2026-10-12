# Migrering: Novellskaparen → GPT Byggaren 1.6.13

Status: **påbörjad – inte redo för merge eller release**.

## Källinventering (2026-10-12)

Verifierade källor i `main`:

- `canonical/instructions.md`: identitet, direkt skrivande, idé/synopsis, målgrupp, fortsättning, revision, originalitet och svenska.
- `gpt-project.yaml`: schema_version 1, tre aktiva runtime-distributioner (Chat ZIP, Custom GPT, Claude Projects), registrerade men ej aktiva OpenCode och Plugin.
- `project-status.yaml`: avslutad äldre migration till GPT Byggaren 1.5.0.
- `.github/workflows/ci.yml`: lint/test/build av tidigare fyra ZIP-artefakter med lokala projektskript.

## Icke-förhandlingsbara regressionskrav

1. Bevara `canonical/instructions.md` och dess kreativa uppdrag; ingen beteendeomskrivning vid teknisk migration.
2. Bevara stöd för att skriva direkt på tillräcklig brief, fylla kreativa luckor utan formulär, följa ordantal, anpassa efter läsarålder, bibehålla karaktärer och kontinuitet, redigera lokalt och skapa originella verk.
3. Använd den **originalmotor som följer med GPT Byggaren 1.6.13**. Ingen hemmabyggd ersättare för `build_distributions.py`.
4. Skilj byggverifiering från verklig host-/runtimeverifiering.

## Genomförande

- [ ] Inventera samtliga källfiler och tester; ta baslinjeresultat före ändring.
- [ ] Kör originalmotorns legacy-inventering och migrationsverktyg på arbetskopia. Behandla `manual_review` separat.
- [ ] Anpassa projektunik `gpt-project.yaml` till det fullständiga v1.6.13-kontraktet. `build_system.runtime_targets` måste vara en **mapping** med `chat`, `plugin`, `claude_project`, `claude_skills`, `opencode`, var och en med builder/runtime_key/runtime_id/artifact_type/filename_pattern. `build_system.targets` ska inkludera `project` och alla fem.
- [ ] Behåll eventuellt legacy Custom GPT-material som referens, men sätt `runtime.custom_gpt.enabled: false` och ta bort Custom GPT från aktiva byggen. Dokumentera denna medvetna förändring.
- [ ] Beskriv Novellskaparens egna färdigheter i `docs/skills/skill-decomposition.md`; återanvänd inte GPT Byggarens projektspecifika färdigheter.
- [ ] Installera *medföljande* `distribution-engine/` genom `install_distribution_engine.py` först när projektkontraktet klarar installationskraven; ersätt inte projektspecifika resurser.
- [ ] Migrera lokal lint, byggning, validering och GitHub Actions till kanonisk motor. Använd GitHub Actions för CI i stället för extern körmiljö.
- [ ] Uppdatera projektstatus, READMEs, utvecklingsplan och release-workflow i samma ändring.
- [ ] Lägg till regressionstester som särskilt kontrollerar målgruppsanpassning, kontinuitet, revision och originalitet.
- [ ] Kör lint, tester, fem distributionsbyggen, leveransvalidering, parity och reproducerbarhetskontroll.
- [ ] Bygg sex artefakter: projekt-ZIP och separata Chat, Plugin, Claude Projects, Claude Skills och OpenCode. Kontrollera namn, filstruktur och SHA256.
- [ ] Uppdatera `project-status.yaml` till `release: ready` **endast** efter godkända verifieringar.

## Kompatibilitetsbedömning

Kärnfunktionerna kräver inga obligatoriska externa verktyg, shellkommandon eller persistent state. Det talar för hög portabilitet till samtliga fem distributionsformat, men säger **inte** att adapters är validerade. Plugin- och OpenCode-aktivering ska stoppas om motorns kompatibilitetsbedömning är `reduced` eller `blocked`; manuella frågor får inte döljas.

## Fortsättningspunkt

Nästa konkreta steg är att bygga den fullständiga nya projektkonfigurationen, installera motorn och köra migrations-/valideringsskripten. **Denna plan är ingen färdig migration.**

## Städning efter migrering (2026-10-12)

- Ersatt äldre huvuddokumentation i `README.md`, `PROJECT.md` och `STATUS.md` med aktuellt v1.6.13-innehåll.
- Tagit bort `scripts/validate_workflow_parity.py`, `scripts/validate_release_readiness.py` och `scripts/validate_runtime_parity.py`. De kontrollerade gamla distributionsnamn och har ersatts av kanonisk lint och distributionsvalidering i den installerade motorn.
- Behållit `scripts/project_hygiene.py` som projektspecifikt städverktyg, även om det inte är en CI-gate.
- Behållit `canonical/instructions.md`, tester, scenariomaterial och mallar; de är projektets egna resurser.
- Behållit legacy-kompatibilitetsmetadata i `gpt-project.yaml` och `runtime-parity.yaml` tills ett separat kontraktstest visar att det kan tas bort utan dataförlust. Detta är metadata, inte aktiva distributionsmål.
- GitHub CI #130 passerade efter skriptborttagning och dokumentationsuppdateringar. En publicerad release är fortfarande inte testad.

## Slutlig legacy-bedömning

Runtime-paritetsmodellen och runtime-kandidatlistan avser nu Chat, Plugin, Claude Projects, Claude Skills och OpenCode, och regressionskontrollerna har uppdaterats. Ett test med borttagen `runtime.custom_gpt` misslyckades redan vid originalmotorns installationssteg. Den inaktiva mappningen återställdes därför av kompatibilitetsskäl (`enabled: false`), utan att Custom GPT återaktiverades som byggmål. Senaste verifierade CI efter återställningen: #148, godkänd. Detta är ett dokumenterat kompatibilitetsberoende i originalmotorn och bör tas bort först vid en framtida motorversion som uttryckligen tillåter det.
