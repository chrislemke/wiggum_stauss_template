---
name: write-srs-29148
description: Produce ISO/IEC/IEEE 29148-aligned Software Requirements Specifications with testable shall-statements, verification criteria, and traceability outputs. Use when creating a new SRS from scratch, transforming notes/user stories/PRDs into an SRS, filling gaps in a partial SRS, or validating and improving an existing SRS package.
---

# Write SRS 29148

Produce modular, standards-aligned SRS files in `specs/<project-name>/` with requirement IDs, measurable acceptance criteria, and validation-ready structure.

## Workflow Decision Tree

Select the entry point before drafting:

| Situation | Entry Point |
| --- | --- |
| No existing material | Phase 1: Full elicitation from scratch |
| Notes, user stories, or PRD exist | Transform: Map existing material to SRS sections, then fill only gaps |
| Draft/partial SRS exists | Gap Analysis: Identify missing sections, then fill them |
| User requests SRS review | Validate & Improve: Run validator, then quality review |

For Transform, Gap Analysis, and Validate flows, avoid re-eliciting information already present.

## Modular Output Structure

Write each section to a dedicated file inside `specs/<project-name>/`:

| File | Content |
| --- | --- |
| `00-introduction.md` | Purpose, scope, definitions, references, overview |
| `01-product-perspective.md` | System context, product functions, stakeholders, environment, assumptions |
| `02-external-interfaces.md` | IR-requirements (user, API, hardware, communication) |
| `03-functional-requirements.md` | FR-requirements |
| `04-data-requirements.md` | DR-requirements |
| `05-non-functional-requirements.md` | NFR-requirements |
| `06-constraints.md` | CR-requirements |
| `07-change-control.md` | Version history and baselining policy |
| `RTM.md` | Optional traceability matrix |

Keep each file under about 150 lines. If a file exceeds this, split it by domain (for example, `03a-auth-requirements.md` and `03b-payment-requirements.md`).

## Phase 1: Scope and Context

Elicit foundational context with 3 to 4 questions per turn. Draft sections immediately after each answer set, then confirm before moving on.

Ask about:

- Purpose and audience: system name, problem, goals, SRS consumers, decisions supported.
- Scope: explicit in-scope and out-of-scope boundaries, relationship to larger systems.
- Stakeholders: user classes, operators/admins/regulators, replacement/integration targets.
- Context: operating environment, assumptions, and external dependencies.

## Phase 2: Requirements Elicitation

Process categories one at a time. For each category:

1. Ask targeted elicitation questions.
2. Draft requirements with unique IDs.
3. Present drafted statements for confirmation.
4. Revise before moving to the next category.

### 2a. External Interfaces (`IR-NNN`)

- User interface flows and interaction patterns.
- API/software contracts and protocols.
- Hardware integrations.
- Communication protocols, ports, and network limits.

### 2b. Functional Requirements (`FR-NNN`)

- Core behavior.
- Input validation.
- Output behavior.
- Normal, exception, and edge-case flows.
- Error handling and recovery.

### 2c. Data Requirements (`DR-NNN`)

- Entities and relationships.
- Validation and integrity constraints.
- Retention, archival, and deletion.
- Migration and import/export behavior.

### 2d. Non-Functional Requirements (`NFR-NNN`)

Quantify each requirement with measurable targets:

- `NFR-1xx`: Performance.
- `NFR-2xx`: Reliability and availability (SLO, RTO, RPO).
- `NFR-3xx`: Security and privacy.
- `NFR-4xx`: Maintainability and operability.
- `NFR-5xx`: Scalability.
- `NFR-6xx`: Usability and accessibility.
- `NFR-7xx`: Portability and compatibility.

### 2e. Constraints (`CR-NNN`)

- Regulatory/standards obligations.
- Technology or platform constraints.
- Operational/site constraints.

## Phase 3: Refinement

After category drafting is complete:

1. Assign verification method and acceptance criteria to each requirement using IADT.
2. Assign MoSCoW priority (`Must`, `Should`, `Could`, `Won't`).
3. Assign release target (`MVP`, `Phase 2`, `Future/Deferred`).
4. Add rationale for key or controversial requirements.
5. Review completeness:
- Every FR has error handling.
- Every NFR is quantified.
- Every interface requirement defines inputs and outputs.
- Assumptions are explicit where uncertainty exists.

For details, load:

- [references/verification-traceability.md](references/verification-traceability.md)
- [references/requirement-writing-guide.md](references/requirement-writing-guide.md)

## Phase 4: Assembly and Validation

1. Assemble content using [references/srs-template.md](references/srs-template.md).
2. Write modular files in `specs/<project-name>/`.
3. Validate with:

```bash
python3 scripts/validate_srs.py specs/<project-name>/
```

4. Fix reported errors and re-run until validation passes.
5. Present finalized files for user review.

## Phase 5: Traceability (Optional)

When formal traceability is requested, generate `RTM-<project-name>.md` with:

| Req ID | Requirement | Source/Need | Design Ref | Test Case | Status |
| --- | --- | --- | --- | --- | --- |

Use [references/verification-traceability.md](references/verification-traceability.md) for full RTM guidance.

## Requirement Writing Rules

Follow these rules for every requirement:

- Use `shall` for mandatory, `should` for recommended, `may` for optional.
- Keep one requirement per statement.
- Make each requirement testable and measurable.
- Include inputs, outputs, and error behavior where applicable.
- Avoid ambiguous words such as "appropriate", "sufficient", "fast", or "user-friendly".

ID scheme:

| Category | Prefix | Example |
| --- | --- | --- |
| Interface | `IR` | `IR-001` |
| Functional | `FR` | `FR-001` |
| Data | `DR` | `DR-001` |
| Non-functional | `NFR` | `NFR-101` |
| Constraint | `CR` | `CR-001` |

Compact requirement format:

> **FR-001**: *Title* - The system shall [action] [object] [qualifier].  
> Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP

## Required Definitions and Acronyms

Include the following in every SRS:

- `SRS`: Software Requirements Specification.
- `RTM`: Requirements Traceability Matrix.
- `MoSCoW`: Must/Should/Could/Won't prioritization.
- `IADT`: Inspection, Analysis, Demonstration, Test.
- `FR`: Functional Requirement.
- `NFR`: Non-Functional Requirement.
- `DR`: Data Requirement.
- `IR`: Interface Requirement.
- `CR`: Constraint Requirement.

Add project-specific terms as they emerge.

## Change Control Requirements

Ensure `07-change-control.md` includes:

- Version history table with columns: `Version | Date | Author | Changes`.
- Initial row:

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | [Author] | Initial draft |

Baseline requirements at version `1.0`. After baselining, require formal change requests with impact analysis.

## Completion Checklist

Track completion with:

```text
SRS Progress:
- [ ] Purpose, scope, and audience defined
- [ ] Definitions and acronyms listed
- [ ] Stakeholders and user classes identified
- [ ] System context and product perspective documented
- [ ] Assumptions and dependencies listed
- [ ] All external interfaces documented (IR-NNN)
- [ ] Functional requirements complete (FR-NNN)
- [ ] Data requirements specified (DR-NNN)
- [ ] Non-functional requirements quantified (NFR-NNN)
- [ ] Constraints documented (CR-NNN)
- [ ] Verification criteria assigned to all requirements
- [ ] Priorities (MoSCoW) and release allocation set
- [ ] Rationale documented for key requirements
- [ ] Change control metadata included
- [ ] validate_srs.py passes with no errors
- [ ] Traceability matrix generated (if required)
```
