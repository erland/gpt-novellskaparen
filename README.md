# Novellskaparen

Novellskaparen är en svensk kreativ skrivassistent för noveller, idéutveckling, fortsatt skrivande och textrevision. `canonical/instructions.md` definierar samma centrala skrivbeteende i alla distributioner.

## Distributioner – GPT Byggaren v1.6.15

| Paket | Syfte |
| --- | --- |
| Projekt-ZIP | Portabel källmodell och projektresurser |
| Chat ZIP | Användning direkt i ChatGPT-konversation |
| Plugin ZIP | ChatGPT-plugin utan krav på egna MCP-servrar |
| Claude Projects ZIP | Claude Projects |
| Claude Skills ZIP | Claude Skills |
| OpenCode ZIP | OpenCode |

Custom GPT är inte längre ett aktivt distributionsmål. Äldre referenser till Custom GPT hör endast till migrationshistoriken.

## Struktur

- `gpt-project.yaml` – kanonisk projektmodell och distributionskontrakt
- `canonical/instructions.md` – skrivbeteende
- `docs/skills/skill-decomposition.md` – projektspecifika färdigheter
- `tests/` – regressionsfall och instruktionsevalueringar
- `project-status.yaml`, `STATUS.md` – projektstatus
- `docs/migration-to-gpt-byggaren-1.6.13.md` – migrationshistorik

## Byggning och release

GitHub Actions hämtar **originalmotorn** från `erland/gpt-byggaren` tagg `v1.6.15` och installerar den innan lint, tester och byggning. Motorfilerna ska inte handmodifieras. CI bygger projektpaketet och fem distributioner, validerar dem och kontrollerar reproducerbara checksummor. Den temporära checkout-katalogen tas bort före paketeringen.

` .github/workflows/ci.yml ` innehåller exakta byggkommandon. Vid publicering av en GitHub Release med tagg `vX.Y.Z` används `.github/workflows/release.yml` för att publicera sex ZIP-filer, `SHA256SUMS.txt` och `DELIVERY-MANIFEST.json`. Verifiera den första faktiska releasekörningen innan migrationen markeras som helt slutförd.

## Portabla färdigheter (v1.6.15)

`portable-skills.json` deklarerar två projektspecifika Skills: `novellskrivande` och `fortsattning-och-revision`, med egna `SKILL.md` och referenser under `skills/`. CI och release verifierar deras struktur med originalmotorns `validate_portable_skills.py`. Canonical skrivinstruktionen i `canonical/instructions.md` förblir auktoritativ. Skills-kontraktets strukturella validering innebär inte att host-beteende har provats.

## Modulär canonical Skills-modell

Novellskaparen har nu tre auktoritativa källområden: `canonical/core/`, `skills/novellskrivande/source/` och `skills/fortsattning-och-revision/source/`. `canonical/assembly.json` definierar originalordningen för samtliga 17 avsnitt. Kör `python scripts/compile_canonical_skills.py --project-root .` för att generera `canonical/instructions.md` efter en källändring; CI och release kör motsvarande kommando med `--check` för att stoppa inkonsekventa leveranser. Den kompilerade instruktionen är fortsatt gemensam för alla distributioner, oberoende av om värdplattformen stöder automatisk Skill-aktivering.
