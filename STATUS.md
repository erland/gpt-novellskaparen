# Status – Novellskaparen

## Migrering till GPT Byggaren v1.6.16

Ren migration från `main` i [PR #5](https://github.com/erland/gpt-novellskaparen/pull/5) på grenen `migration/gpt-byggaren-1.6.16-clean`. Äldre migrationsgrenar och PR #3 används inte som teknisk bas.

Fyra distinkta Skills har införts. Den kanoniska instruktionens 16 avsnitt har extraherats till gemensam kärna och Skill-källor utan textförlust. En deterministisk kompilator kontrollerar byte-exakt återställning. GitHub CI #38288256868 passerade installation av originalmotorn v1.6.16, assembly-kontroll, canonical lint, tester, distributionsbyggning, validering och reproducerbarhetskontroll.

## Kvarvarande gränser

- Hostspecifika funktionstester i ChatGPT Plugin, Claude och OpenCode är inte genomförda.
- Faktisk publicerad GitHub Release är inte testad.
- Den kompletterade CI-kontrollen av arkivintegritet och checksummor behöver passera vid nästa körning.

## Beslut

PR #5 lämnas omergad för granskning. Historisk migrationsdokumentation för v1.6.13 bevaras som historik, inte som nuvarande status. Se `project-status.yaml`.
