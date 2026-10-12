# Novellskaparen

Novellskaparen är en svensk kreativ skrivassistent för noveller, idéutveckling, fortsatt skrivande och textrevision. `canonical/instructions.md` definierar samma centrala skrivbeteende i alla distributioner.

## Distributioner – GPT Byggaren v1.6.13

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

GitHub Actions hämtar **originalmotorn** från `erland/gpt-byggaren` tagg `v1.6.13` och installerar den innan lint, tester och byggning. Motorfilerna ska inte handmodifieras. CI bygger projektpaketet och fem distributioner, validerar dem och kontrollerar reproducerbara checksummor. Den temporära checkout-katalogen tas bort före paketeringen.

` .github/workflows/ci.yml ` innehåller exakta byggkommandon. Vid publicering av en GitHub Release med tagg `vX.Y.Z` används `.github/workflows/release.yml` för att publicera sex ZIP-filer, `SHA256SUMS.txt` och `DELIVERY-MANIFEST.json`. Verifiera den första faktiska releasekörningen innan migrationen markeras som helt slutförd.
