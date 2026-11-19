# AGENTS.md

## Public interface

- The public interface is the installed `geci-caller` CLI: its commands and their `--options`. Its elements are documented in `DOCS.md`; changes to them are recorded in `CHANGELOG.md`.

## Verification

- `make check` runs `black --check --line-length 100`, `flake8 --max-line-length 100`, and `mypy` over both `geci_caller` and `tests` (`Makefile`).
- `make coverage` runs `pytest --cov=geci_caller --cov-report=xml --verbose` then `coverage report --show-missing`; `make all` chains `check coverage mutants` (`Makefile`).
- `make setup` chains `clean` and `install`; `clean` deletes caches, `*.egg-info`, `.mutmut-cache`, and `coverage.xml` (`Makefile`).
- `make init_git` adds `/workdir` to Git's global `safe.directory` and sets author identity; required before Git commands in this environment (`Makefile`).
- CI builds the Docker image, runs `make check` in it, runs `docker compose run islasgeci make coverage`, and deploys only from `develop` (`.github/workflows/actions.yml`).

## Boundaries and conventions

- Entry point: `[tool.flit.scripts] geci-caller = "geci_caller.cli:cli"`; commands are `@cli.command()` functions in `geci_caller/cli.py` (`pyproject.toml`, `geci_caller/cli.py`).
- Command and option names are kebab-case (`geci-caller --help`, `tests/test_cli.py`).
- Tests call live APIs at `http://islasgeci.org:100` and `:200`; no HTTP mocking is used (`geci_caller/cli.py`, `tests/test_cli.py`).
- Tests write generated files into the repository root, for example `posteriors.csv`, `figure.png`, and `cumulative_by_flight.png`; those files are untracked (`tests/test_cli.py`, `git status --porcelain`).
- `geci_caller/call_api.py` defines only `construct_entrypoint_url`; no production code imports it (`geci_caller/`, `tests/test_call_api.py`).
- `Makefile` targets `red`, `green`, and `refactor` run `format` and `pytest`, then auto-commit on success and restore files on failure (`Makefile`).
- Those same targets end with `chmod g+w -R .` (`Makefile`).

## Preserved constraints

- `requires-python = ">=3.9"` (`pyproject.toml`).
- `LICENSE` is AGPL-3.0, while the `pyproject.toml` classifier currently says GPLv3+ (`LICENSE`, `pyproject.toml`).
