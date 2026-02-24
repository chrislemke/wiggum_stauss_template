# Operational Guide

This file contains operational knowledge for the AI agent. Update this as you learn about the codebase.

---

## Commands

### Build
```bash
uv sync
```

### Test, Lint & All Checks
```bash
make test
```
> Runs all 8 checks in sequence (format, lint, typecheck, complexity, security scan, tests, security audit, mutation testing). Continues on failure and prints a pass/fail summary at the end. Use hypothesis for property-based testing.

### Run
```bash
uv run project_name
```

---

## Project Structure

- `src/project_name/`: package code (`main.py`, `__main__.py`, `__init__.py`)
- `tests/`: pytest suite (`test_main.py`, shared `conftest.py`)
- `skills/`: local Codex skills used in this repo
- `docs/README.md`: project readme
- `pyproject.toml`: tool, lint, test, coverage, and mutation config

---

## Operational Notes

<!-- Add learnings here as you work on the codebase -->

- Python baseline is 3.13 (`requires-python >=3.13`, Ruff target `py313`).
- Pytest discovery includes `tests` and `src` (doctest modules enabled).
- Full quality gate enforces `--cov-fail-under=90`.
- Mutation testing is configured through `mutmut` and runs tests with `-n 0 --no-cov`.

---

## Codebase Patterns

<!-- Document patterns and conventions you discover -->

- Test naming pattern is `test_*`; class pattern is `Test*` (configured in `pyproject.toml`).
- Existing tests use typed pytest fixtures (example: `capsys: pytest.CaptureFixture[str]`).
- `tests/conftest.py` exists for shared fixtures; currently minimal and ready for expansion.
- Prefer property-based tests with Hypothesis (explicit project guidance in this file and toolchain).
- Marker conventions available: `unit`, `integration`, `performance`, `slow`, `asyncio`.

---

## Known Issues

<!-- Track issues that affect development -->

-

---

## Dependencies

- Dev/test tooling includes `pytest`, `pytest-xdist`, `pytest-randomly`, `pytest-asyncio`, `hypothesis`, `mutmut`, `ruff`, `mypy`, `bandit`, `pip-audit`, and `xenon`.
