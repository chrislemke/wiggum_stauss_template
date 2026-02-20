# CLAUDE.md - Operational Guide

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

[Add project structure here]

---

## Operational Notes

<!-- Add learnings here as you work on the codebase -->

-

---

## Codebase Patterns

<!-- Document patterns and conventions you discover -->

-

---

## Known Issues

<!-- Track issues that affect development -->

-

---

## Dependencies

- **pytest-xdist** — parallel test execution (`-n auto`)
- **pytest-randomly** — randomizes test order to catch hidden inter-test dependencies
- **hypothesis** — property-based / generative testing
- **mutmut** — mutation testing to validate test quality
