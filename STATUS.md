# Status – Novellskaparen

## Migration till GPT Byggaren v1.6.13

Migrationen genomförs i PR #3 (`migration/gpt-byggaren-1.6.13`). Projektets canonical instruktion har bevarats, medan projektmodellen och distributionsbyggningen anpassats till Chat, Plugin, Claude Projects, Claude Skills och OpenCode.

Originalmotor v1.6.13 installeras via GitHub Actions från en versionslåst källa. Byggkedjan har passerat kanonisk lint, projektets regressionstester, fem distributionsbyggen och reproducerbarhetskontroll. En tillfällig motor-checkout som tidigare hamnade i projekt-ZIP har avlägsnats och en senare CI-körning har passerat.

## Kvarvarande kontroll

- Säkerställ att slutlig CI passerar efter dokumentations- och städförändringar.
- Första faktiska GitHub Release-publiceringen och hostspecifika runtimeprov är ännu inte verifierade.
- Bedöm eventuella kvarvarande legacy-valideringsskript separat före borttagning.

## Beslut

Se `project-status.yaml` för maskinläsbar status. Canonical instruktion, scenarier och relevanta tester bevaras. Äldre v1.5.0-projektbeskrivningar har ersatts av denna aktuella status; migrationshistorik bevaras i `docs/migration-to-gpt-byggaren-1.6.13.md`.
