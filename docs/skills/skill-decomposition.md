# Novellskaparens modulära Skills – v1.6.16

Denna fil sammanfattar den aktuella arkitekturen. Detaljerad analys: [skill-decomposition-1.6.16.md](skill-decomposition-1.6.16.md).

Fyra fristående funktionsansvar ersätter den äldre tvådelningen:

| Skill | Självständigt ansvar |
| --- | --- |
| ideutveckling-och-planering | Idé, synopsis, scenplan och karaktär |
| novellskrivande | Nyskriven novell eller scen |
| fortsattning | Ny text som respekterar etablerade fakta och utveckling |
| revision | Proportionerlig bearbetning av redan skriven text |

Gemensamma krav på identitet, användarstyrning, språk, målgrupp, originalitet och litterär kvalitet ligger i kanonisk core. `canonical/assembly.json` bygger den sammanhängande instruktionen från dessa källor; `scripts/compile_canonical_skills.py --check` verifierar exakt återgivning.

Skill-definitionerna beskriver aktivering, gränser och acceptans. Testning av paket är inte samma sak som hostspecifik runtime-verifiering.
