# Verification and Traceability Guide

Use this guide to assign verification methods and build traceable requirement sets.

## IADT Verification Methods

| Method | Use When | Evidence |
| --- | --- | --- |
| Inspection | Static review of documents/config/code can verify requirement intent | Review checklist, signed review record |
| Analysis | Mathematical/model/simulation evidence is needed | Analysis report, model output |
| Demonstration | Behavior can be shown without full instrumentation | Demo script, observed outcomes |
| Test | Controlled execution with defined expected results is needed | Test case, logs, pass/fail results |

## Method Selection Heuristics

- Use `Inspection` for policy, naming, documentation, static structure.
- Use `Analysis` for capacity planning, reliability projections, formal constraints.
- Use `Demonstration` for human-observable flows and UX tasks.
- Use `Test` for functional correctness, limits, error handling, and regressions.

When uncertain, prefer `Test` because it provides stronger objective evidence.

## Acceptance Criteria Rules

For every requirement, define acceptance criteria that are:

- Measurable (latency, percentages, counts, durations).
- Reproducible (known setup and conditions).
- Binary (pass/fail outcome possible).

Examples:

- `Pass if p95 latency <= 500 ms at 200 requests per second over 15 minutes.`
- `Pass if failed logins lock account after 5 attempts within 15 minutes.`
- `Pass if audit record contains actor, action, object, timestamp for 100% of admin actions.`

## Requirement Metadata Minimum

Each requirement should include:

- `Priority` (MoSCoW)
- `Verify` (IADT method)
- `Release` (MVP / Phase 2 / Future)
- `Source` or rationale (stakeholder, contract, regulation, operational need)

## Traceability Matrix Template

Use this structure for `RTM.md` (or `RTM-<project-name>.md`):

```markdown
# Requirements Traceability Matrix

| Req ID | Requirement | Source/Need | Design Ref | Test Case | Status |
| --- | --- | --- | --- | --- | --- |
| FR-001 | ... | Stakeholder interview (Ops) | docs/design/auth.md#session-policy | tests/test_auth.py::test_session_timeout | Draft |
```

## Traceability Rules

- Every requirement ID appears exactly once in the RTM.
- `Source/Need` links to origin (stakeholder, regulation, incident, business goal).
- `Design Ref` points to implementation design artifact.
- `Test Case` points to executable or planned verification artifact.
- `Status` reflects lifecycle state (`Draft`, `Approved`, `Implemented`, `Verified`, `Deferred`).

## Coverage Review Checklist

- Every `FR`, `IR`, `DR`, `NFR`, and `CR` has a verification method.
- Every `Must` requirement has planned or implemented tests.
- Every security/privacy requirement maps to a specific control/test.
- Every deferred requirement has rationale and target phase.
