# Novellskaparen

Novellskaparen är en kreativ skrivassistent för svenska noveller, idéutveckling, fortsättning och revision.

## Kanonisk källa och fyra Skills

Den kanoniska instruktionen i `canonical/instructions.md` genereras från `canonical/assembly.json`, `canonical/core.md` och de separata källorna under `skills/*/source/instructions.md`. De fyra Skill-filerna har tydliga aktiveringsregler och ansvarsområden:

- `ideutveckling-och-planering`: premiss, synopsis, karaktärer och scenplan.
- `novellskrivande`: nya noveller och scener.
- `fortsattning`: vidareutveckling med berättelsekontinuitet.
- `revision`: avgränsade och djupa omskrivningar av befintlig text.

Vid ändringar i beteendet redigeras de modulära källorna. Kontrollera med `python scripts/compile_canonical_skills.py --check`, eller återskapa instruktionen med `--write`. Den ursprungliga instruktionstexten på main behölls exakt vid den initiala uppdelningen.

## Distributioner – GPT Byggaren v1.6.16

Byggsystemet producerar sex ZIP-arkiv: projektpaket, Chat ZIP, Plugin ZIP, Claude Project ZIP, Claude Skills ZIP och OpenCode ZIP. Custom GPT är inte aktivt distributionsmål.

## Byggning och verifiering

GitHub Actions hämtar originalmotorn från `erland/gpt-byggaren` tagg `v1.6.16` och installerar den utan egen modifiering. CI utför assembly-kontroll, kanonisk lint, regressionstester, sex byggmål, distributionsvalidering, arkivintegritet, SHA256 och reproducerbarhetskontroll. Temporär engine-checkout avlägsnas före paketering.

Se `.github/workflows/ci.yml` och `.github/workflows/release.yml`. Release-workflow aktiveras först när en GitHub Release publiceras; faktisk releasepublicering och hostspecifika runtimeprov behöver verifieras separat.

Se `docs/skills/skill-decomposition-1.6.16.md`, `STATUS.md` och `project-status.yaml` för migrationsstatus.
