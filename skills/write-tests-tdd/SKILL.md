---
name: write-tests-tdd
description: Enforce strict Red-Green-Refactor TDD for Python unit testing with pytest and Hypothesis. Use when adding new behavior, fixing bugs, expanding unit-test coverage, or reviewing test quality in this repository. Apply for test design, AAA structure, naming, fixtures, parametrization, property-based testing, and mutation-resistant assertions.
---

# Write Tests TDD

Apply strict TDD for Python changes: write tests first, make the smallest code change to pass, then refactor with tests green.

## Follow the Three Laws

1. Write no production code unless it is required to make one failing unit test pass.
2. Write no more of a test than needed to fail (compilation/import errors count as failure).
3. Write no more production code than needed to pass the current failing test.

## Execute Red Green Refactor

1. Red:
- Write one focused failing test.
- Keep scope minimal: one behavior.
- Confirm failure for the expected reason.
2. Green:
- Implement the smallest production change that passes that one test.
- Avoid extra features and broad refactors in this step.
3. Refactor:
- Improve names, duplication, and structure without changing behavior.
- Keep tests green after each refactor.

Repeat the cycle until the requested behavior is complete.

## Plan Tests Before Writing

For each unit, enumerate:

1. Happy path.
2. Edge cases (empty, boundary, single-element, max/min).
3. Error cases (invalid input, exceptions, failure states).
4. Type variations (if multiple valid input types exist).
5. State transitions (before/after behavior for stateful units).
6. Property-based invariants with Hypothesis.

## Use AAA in Every Test

```python
def test_behavior_condition_expected_result():
    # Arrange
    input_data = ...
    expected = ...

    # Act
    result = function_under_test(input_data)

    # Assert
    assert result == expected
```

Keep one behavior per test. Keep assertions specific enough to fail meaningful mutations.

## Apply Naming and Organization Rules

- Name tests as executable specs: `test_<what>_<condition>_<expected_outcome>`.
- Group related behavior in classes, for example `class TestEmailValidation:`.
- Prefer `@pytest.mark.parametrize` to reduce duplicated test logic.

## Use Pytest Patterns

- Use fixtures for setup reuse; prefer factory fixtures when data variations are needed.
- Use `pytest.raises(..., match=...)` for exception behavior.
- Use `monkeypatch` or `unittest.mock.patch` to isolate external dependencies.
- Use `tmp_path` for filesystem interactions.
- Use `capsys` for stdout/stderr verification.
- Keep tests isolated and order-independent.

## Use Hypothesis Deliberately

- Encode invariants and properties, not only examples.
- Use `@given(...)` with focused strategies.
- Add `@example(...)` for known edge cases.
- Use `assume()` only when truly necessary.

Example properties:

- Sorting is idempotent.
- Encoding then decoding returns the original value.
- Output length never exceeds input length (when required by design).

## Meet Quality Standards

1. Keep tests deterministic.
2. Keep unit tests fast; mock I/O and external systems.
3. Keep tests isolated; avoid shared mutable state.
4. Keep tests readable; treat tests as executable documentation.
5. Keep tests maintainable; use fixtures/parametrize without over-abstraction.
6. Keep tests mutation-resistant with precise assertions.

## Follow Project Test Workflow

1. Sync dependencies when needed:
```bash
uv sync
```
2. Run full quality gate before finalizing:
```bash
make test
```

`make test` runs eight checks in sequence: format, lint, typecheck, complexity, security scan, tests, security audit, and mutation testing.

## Produce Output in This Format

When writing tests for a task, present work in this order:

1. Analyze requirements and identify required test coverage.
2. List planned test cases with short descriptions.
3. Write complete test file updates.
4. Explain key design decisions and trade-offs.
5. Note assumptions about interfaces or behavior.

## Run Self-Verification

- [ ] Keep AAA in every test.
- [ ] Use clear behavior-focused test names.
- [ ] Cover happy path, edge cases, and error cases.
- [ ] Include Hypothesis properties where appropriate.
- [ ] Ensure order independence (`pytest-randomly` safe).
- [ ] Use fixtures only where they improve clarity/reuse.
- [ ] Use `parametrize` for input matrices.
- [ ] Keep assertions specific enough for mutation testing.
- [ ] Keep tests safe for parallel execution (`pytest-xdist`).

## Update Project Memory

When discovering project-specific testing conventions, append concise notes to `AGENTS.md`:

- Add fixture patterns and where they live.
- Add recurring edge cases and failure modes.
- Add mocking conventions for external dependencies.
- Add test layout and naming conventions.
- Add useful Hypothesis strategies for local data models.
- Add mutation-testing survivors and how to kill them.
