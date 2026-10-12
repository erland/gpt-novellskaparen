# Status – Novellskaparen

## Migrering till GPT Byggaren v1.6.17

Ren migration från `main` i [PR #5](https://github.com/erland/gpt-novellskaparen/pull/5) på grenen `migration/gpt-byggaren-1.6.16-clean`. Äldre migrationsgrenar och PR #3 används inte som teknisk bas.

Fyra distinkta Skills har införts. Den kanoniska instruktionens 16 avsnitt har extraherats till gemensam kärna och Skill-källor utan textförlust. En deterministisk kompilator kontrollerar byte-exakt återställning. GitHub CI #38292749872 verifierade originalmotorn v1.6.17, exakt assembly, lint, regressionstester, sex ZIP-arkiv samt innehållskontroll av de fyra kanoniska Skill-beteendena i samtliga fem distributioner.

## Kvarvarande gränser

- Hostspecifika funktionstester i ChatGPT Plugin, Claude och OpenCode är inte genomförda.
- Faktisk publicerad GitHub Release är inte testad.
- Arkivintegritet, checksummor och innehållskontroll passerar i CI. Verkligt värdbeteende återstår att prova.

## Beslut

PR #5 lämnas omergad för granskning. Historisk migrationsdokumentation för v1.6.13 bevaras som historik, inte som nuvarande status. Se `project-status.yaml`.

## v1.6.17

Aktiverat `instructions.mode: modular_skills` med nuvarande granskade källägarskap. GitHub Actions använder originalmotor v1.6.17. Hostspecifika tester och verklig release kvarstår.

## Slutkorrigering av Skill-källor

Alla fyra `skills.definitions[].source` pekar på egna `source/instructions.md` i stället för beskrivande `SKILL.md`. Testet `tests/test_modular_distribution_archives.py` öppnar de faktiska ZIP-arkiven och verifierar core + egen specialisering i Plugin/Claude Skills, utan annan Skills specialbeteende, samt sammansatt beteende i Chat, Claude Projects och OpenCode. PR #5 är fortfarande omergad.
