# Requirement Writing Guide

Use this guide to write clear, testable, single-purpose requirements.

## 1. Requirement Structure

Use this compact pattern:

```text
**FR-001**: *Title* - The system shall [action] [object] [qualifier].
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP
```

## 2. Modal Verbs

- `shall`: mandatory requirement.
- `should`: recommended requirement.
- `may`: optional capability.

Do not use weak language like `will`, `can`, or `might` in normative requirements.

## 3. Single Requirement Rule

Write one requirement per statement.

Bad:

```text
The system shall validate email and send a welcome message.
```

Good:

```text
The system shall validate email format against RFC 5322 syntax.
The system shall send a welcome message after successful account creation.
```

## 4. Testability Rule

Each requirement must be objectively verifiable.

Bad:

```text
The API shall respond quickly.
```

Good:

```text
The API shall return a response within 500 ms for 95% of requests under 200 RPS sustained load.
```

## 5. Completeness Rule

Where applicable, include:

- Input conditions and data shapes.
- Processing behavior and business rules.
- Output behavior (success and failure).
- Error handling and recovery behavior.

## 6. Avoid Ambiguity

Avoid words that cannot be measured:

- appropriate
- sufficient
- fast
- user-friendly
- robust
- flexible

Replace with measurable terms, thresholds, or enumerated criteria.

## 7. Requirement ID Rules

| Category | Prefix | Example |
| --- | --- | --- |
| Interface | `IR` | `IR-001` |
| Functional | `FR` | `FR-001` |
| Data | `DR` | `DR-001` |
| Non-Functional | `NFR` | `NFR-101` |
| Constraint | `CR` | `CR-001` |

Guidelines:

- Use zero-padded IDs.
- Never reuse IDs for different requirements.
- Preserve IDs when editing existing requirement text.

## 8. Common Defects Checklist

Check each requirement for:

- Compound statements joined with `and`/`or`.
- Missing actor (`system`, `user`, `administrator`, service).
- Missing measurable criterion.
- Missing error behavior.
- Non-verifiable language.
- Cross-category misclassification (for example, performance written as FR).

## 9. Rewrite Examples

Ambiguous:

```text
The system shall provide secure login.
```

Improved:

```text
The system shall require MFA for all administrator logins.
Input: Username and password | Output: Time-based one-time passcode challenge
Error: Reject login after 5 failed attempts within 15 minutes
Priority: Must | Verify: Test | Release: MVP
```

Ambiguous:

```text
The dashboard should be easy to use.
```

Improved:

```text
The dashboard shall allow first-time users to complete the weekly report workflow in 3 minutes or less, with at least 90% task success in usability testing.
Input: Weekly report data | Output: Submitted report confirmation
Error: Present field-level guidance on validation failure
Priority: Should | Verify: Demonstration | Release: Phase 2
```
