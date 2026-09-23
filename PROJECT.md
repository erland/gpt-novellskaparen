# Projekt – Novellskaparen

## Syfte

Novellskaparen ska vara en självgående kreativ skrivpartner som kan ta en enkel idé till en färdig novell och samtidigt stödja stegvis idéutveckling, planering, fortsatt skrivande och revision.

## Målgrupper

GPT:n ska kunna skriva för:

- lågstadiet,
- mellanstadiet,
- tonåring,
- vuxen.

Anpassningen ska påverka mer än ordval: även struktur, konfliktnivå, emotionellt djup, tempo, dialog och undertext.

## Projektprofil

`simple`

Kärnbeteendet ligger direkt i canonical instruktionen. Ingen Knowledge-fil krävs för kärnflödet.

## Runtime-strategi

Chat ZIP, Custom GPT och Claude Projects byggs som aktiva jämbördiga distributioner från samma canonical kontrakt. OpenCode och OpenAI Plugin är explicit bedömda som reducerade och inaktiva för detta användningsfall. Verkliga plattformsskillnader ska dokumenteras, inte döljas.

## Tekniska grundval

- Canonical instruktion: `canonical/instructions.md`
- Utvecklingsplan: `docs/development-plan.md`
- Statuskälla: `project-status.yaml`
- CI: `.github/workflows/ci.yml`
- Release-build: `.github/workflows/release.yml`

- Runtime parity: `runtime-parity.yaml`
- Modellrobusthet: `lightweight`
