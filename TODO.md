# Backlog

- [ ] Make `tests/test_cli.py::test_write_traps_and_cameras_posterior_summary` pass; treat that test as the gold contract and do not edit it. It invokes `write-traps-and-cameras-posterior-summary` with `--traps-path`, `--cameras-path`, `--initial-parameters-path`, and `--output-path`, asserting exit 0, a 200 status, and the JSON output file (`tests/test_cli.py:316-341`). Focused run currently fails with exit 2 because the command is absent from `geci-caller`/`geci_caller/cli.py`.
  - Fixture names differ from the paths the gold test uses: `tests/data/esfuerzo_detecciones_camaras_trampa_mensuales.csv` vs `..._gatos_socorro.csv`, and `tests/data/init_traps_cameras_model.json.` vs `...json` (both added in `c071143`).
  - Adding the command is a public-interface change: sync `DOCS.md` and `CHANGELOG.md` when it lands.
