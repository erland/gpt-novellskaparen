# Novellskaparen

Novellskaparen är en kreativ skriv-GPT för att utveckla, skriva, fortsätta och revidera originella noveller anpassade efter målgrupp, genre, ton och längd.

## Distributioner

Projektet är utformat för två jämbördiga runtime-distributioner från samma canonical kontrakt:

- Chat ZIP
- Custom GPT

Den canonical instruktionen finns i `canonical/instructions.md`.

## Projektstatus

Se `STATUS.md` och `project-status.yaml`. Utvecklingsplanen finns i `docs/development-plan.md`.

## Lokal validering

Kräver Python 3.12+ med `pyyaml` och `pytest`.

```bash
python -m pip install pyyaml pytest
python scripts/lint_gpt_project.py --project-root .
python -m pytest -q -p no:cacheprovider
python scripts/build_distributions.py --project-root . --version 0.8.0-dev --targets project,chat,custom-gpt
python scripts/validate_distributions.py --project-root .
```

Varje byggning rensar `build/` och `dist/` först. ZIP-filer skapas deterministiskt med stabil filordning och fasta ZIP-tidsstämplar. `SHA256SUMS.txt` kan därför användas för att kontrollera att två byggen från samma källor och version är identiska.

## Versionshantering

Byggscriptet tar en SemVer-liknande version, exempelvis `0.8.0-dev`, `1.0.0` eller `1.0.0-rc.1`. Versionen används i runtime-filer, manifest och artefaktnamn:

- `novellskaparen-project-<version>.zip`
- `novellskaparen-chat-<version>.zip`
- `novellskaparen-custom-gpt-<version>.zip`

## GitHub Actions

### CI

CI kör lint, tester, bygger båda runtime-distributionerna och projekt-ZIP:en, validerar distributionerna och bygger sedan en andra gång för att verifiera reproducerbara SHA-256-kontrollsummor.

### Release

När en GitHub Release publiceras ska taggen följa formen `v<version>`, exempelvis `v1.0.0` eller `v1.0.0-rc.1`. Workflowen:

1. validerar taggen,
2. härleder versionen genom att ta bort det inledande `v`,
3. kör lint och tester,
4. bygger rena distributioner,
5. validerar dem,
6. kontrollerar de förväntade filnamnen,
7. laddar endast upp de tre versionssatta ZIP-filerna samt `SHA256SUMS.txt` och `DELIVERY-MANIFEST.json` till releasen.

Release-taggen är därmed versionskälla för releaseartefakterna.
