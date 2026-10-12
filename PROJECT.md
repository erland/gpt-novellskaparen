# Projekt – Novellskaparen

## Syfte och beteende

Novellskaparen skriver originella, sammanhängande svenska noveller från såväl korta som detaljerade beställningar. Den kan även utveckla idéer och synopsis, fortsätta berättelser med bevarad kontinuitet och revidera text utan oombedda ändringar. Målgruppsanpassning omfattar lågstadium, mellanstadium, tonåringar och vuxna.

Canonical beteendekälla: `canonical/instructions.md`. Kärnan kräver inga obligatoriska externa verktyg, separat kunskapsbas, shellkommando eller persistent state.

## Aktuell arkitektur – GPT Byggaren v1.6.17

`gpt-project.yaml` är källan till distributionskontraktet. Originalmotorn hämtas från den versionslåsta taggen `v1.6.17` i CI och release. Fem format byggs: Chat, Plugin, Claude Projects, Claude Skills och OpenCode, plus ett separat projektpaket. Custom GPT ingår inte bland aktiva distributionsmål.

Fyra separata modulära Skills har implementerats: idéutveckling/planering, novellskrivande, fortsättning och revision. Kanoniska källavsnitt finns i `canonical/core.md` respektive `skills/*/source/instructions.md`, och sammanfogas via `canonical/assembly.json`. Domänspecifika färdigheter finns dokumenterade i `docs/skills/skill-decomposition.md`. Plattformsskillnader och faktisk runtime-verifiering ska redovisas separat från lyckad ZIP-byggning.

## Referenser

- Projektmodell: `gpt-project.yaml`
- Canonical instruktion: `canonical/instructions.md`
- Projektstatus: `project-status.yaml` och `STATUS.md`
- Utvecklingsplan: `docs/development-plan.md`
- Migration: `docs/migration-to-gpt-byggaren-1.6.13.md`
- CI: `.github/workflows/ci.yml`
- Release: `.github/workflows/release.yml`
