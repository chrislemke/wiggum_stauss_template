# SRS Template (ISO/IEC/IEEE 29148-Aligned)

Use this template to assemble modular SRS files under `specs/<project-name>/`.

## `00-introduction.md`

```markdown
# Introduction

## Purpose
[Why the system exists and what this SRS defines.]

## Intended Audience
[Developers, testers, stakeholders, regulators, operations, etc.]

## Scope
[In scope, out of scope, and system boundaries.]

## Definitions and Acronyms
| Term | Definition |
| --- | --- |
| SRS | Software Requirements Specification |
| RTM | Requirements Traceability Matrix |
| MoSCoW | Must/Should/Could/Won't prioritization |
| IADT | Inspection, Analysis, Demonstration, Test |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| DR | Data Requirement |
| IR | Interface Requirement |
| CR | Constraint Requirement |
[Add project-specific terms.]

## References
[List standards, documents, contracts, or policies.]

## Document Overview
[Summarize the modular file structure and reading order.]
```

## `01-product-perspective.md`

```markdown
# Product Perspective

## System Context
[Context diagram narrative, upstream/downstream systems.]

## Product Functions (Summary)
[High-level capabilities; detailed behavior lives in FRs.]

## Stakeholders and User Classes
[Roles, frequency of use, domain proficiency.]

## Operating Environment
[Platforms, browsers, hosting, infrastructure constraints.]

## Assumptions
[Technical, organizational, operational assumptions.]

## Dependencies
[Third-party services, hardware, projects, contracts.]
```

## `02-external-interfaces.md`

```markdown
# External Interface Requirements

## User Interfaces
**IR-001**: *UI Requirement Title* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP

## Software/API Interfaces
**IR-002**: *API Requirement Title* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP

## Hardware Interfaces
[Add IR requirements if applicable.]

## Communication Interfaces
[Add IR requirements for network/protocol behaviors.]
```

## `03-functional-requirements.md`

```markdown
# Functional Requirements

## Feature Area: [Name]
**FR-001**: *Requirement Title* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP

**FR-002**: *Edge Case Requirement* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Should | Verify: Test | Release: MVP
```

If this file exceeds about 150 lines, split by feature area:

- `03a-<area>-requirements.md`
- `03b-<area>-requirements.md`

## `04-data-requirements.md`

```markdown
# Data Requirements

## Data Entities and Relationships
**DR-001**: *Entity Rule* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Inspection | Release: MVP

## Validation and Integrity Constraints
**DR-002**: *Constraint Rule* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP

## Retention, Deletion, and Archival
[Add DR requirements with measurable retention/deletion criteria.]

## Migration and Import/Export
[Add DR requirements where data movement is required.]
```

## `05-non-functional-requirements.md`

```markdown
# Non-Functional Requirements

## Performance (NFR-1xx)
**NFR-101**: *API Latency* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Test | Release: MVP

## Reliability and Availability (NFR-2xx)
**NFR-201**: *Availability* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Analysis | Release: MVP

## Security and Privacy (NFR-3xx)
**NFR-301**: *Encryption* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Inspection | Release: MVP

## Maintainability and Operability (NFR-4xx)
## Scalability (NFR-5xx)
## Usability and Accessibility (NFR-6xx)
## Portability and Compatibility (NFR-7xx)
```

All NFRs must be quantified and testable.

## `06-constraints.md`

```markdown
# Constraints

**CR-001**: *Regulatory Constraint* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Must | Verify: Inspection | Release: MVP

**CR-002**: *Technology Constraint* - The system shall ...
Input: ... | Output: ... | Error: ... | Priority: Should | Verify: Analysis | Release: MVP
```

## `07-change-control.md`

```markdown
# Change Control

## Version History
| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 0.1 | YYYY-MM-DD | [Author] | Initial draft |

## Baselining Policy
Requirements are baselined when SRS reaches version 1.0.

## Change Request Process
[Describe how post-baseline changes are proposed, reviewed, approved, and traced.]

## Impact Analysis Requirements
[Define mandatory impact dimensions: scope, cost, schedule, risk, verification.]
```

## Optional `RTM.md`

```markdown
# Requirements Traceability Matrix

| Req ID | Requirement | Source/Need | Design Ref | Test Case | Status |
| --- | --- | --- | --- | --- | --- |
| FR-001 | ... | ... | ... | ... | Draft |
```

## Authoring Rules

- Keep one requirement per statement.
- Use mandatory modal verbs correctly (`shall`, `should`, `may`).
- Include measurable acceptance in each requirement block.
- Include `Priority`, `Verify`, and `Release` for each requirement.
- Keep each file short and focused (about 150 lines max).
