# Status – Novellskaparen

## Migration till GPT Byggaren v1.6.15

Migrationen genomförs i PR #4 (`migration/gpt-byggaren-1.6.15`). Projektets canonical instruktion har bevarats, medan projektmodellen och distributionsbyggningen anpassats till Chat, Plugin, Claude Projects, Claude Skills och OpenCode.

Originalmotor v1.6.15 installeras via GitHub Actions från en versionslåst källa. Byggkedjan har passerat kanonisk lint, projektets regressionstester, fem distributionsbyggen och reproducerbarhetskontroll. En tillfällig motor-checkout som tidigare hamnade i projekt-ZIP har avlägsnats och en senare CI-körning har passerat.

## Kvarvarande kontroll

- Säkerställ att slutlig CI passerar efter dokumentations- och städförändringar.
- Första faktiska GitHub Release-publiceringen och hostspecifika runtimeprov är ännu inte verifierade.
- Bedöm eventuella kvarvarande legacy-valideringsskript separat före borttagning.

## Beslut

Se `project-status.yaml` för maskinläsbar status. Canonical instruktion, scenarier och relevanta tester bevaras. Äldre v1.5.0-projektbeskrivningar har ersatts av denna aktuella status; migrationshistorik bevaras i `docs/migration-to-gpt-byggaren-1.6.13.md`.

## Uppgradering till GPT Byggaren v1.6.15 (PR #4)

Originalmotorn i CI och release är versionslåst till v1.6.15. Två portabla Skills och `portable-skills.json` har lagts till för separat strukturell validering. Den tidigare canonical instruktionen behålls oförändrad för att skydda novell- och revisionsbeteendet. Den slutliga CI- och runtimeverifieringen krävs före merge.

## Modulär Skills-aktivering på PR #4

Kärnan och två Skills är nu separata källmoduler. Den deterministiska sammanfogningen till `canonical/instructions.md` verifieras i CI och release. Källuppdelningen har genomförts utan avsiktliga textförändringar i den kompilerade instruktionen. Nytt beteende ska införas genom redigering av källmodulerna, följt av kompilering och tester. Hostspecifik automatisk aktivering och en faktisk GitHub Release är ännu inte verifierade.
