---
description: Audit implementation plan against spec files for completeness and alignment
---

# Audit Implementation Plan

You are tasked with auditing the implementation plan against all specification files to ensure full coverage and alignment.

## Launch the Audit

Use the Task tool to launch the `implementation-plan-auditor` agent:

- `subagent_type`: `implementation-plan-auditor`
- `description`: `Audit plan against specs`
- `prompt`: Include the following in the prompt:
  ```
  Perform a full audit of the implementation plan at thoughts/shared/plan/IMPLEMENTATION_PLAN.md against all specification files in thoughts/shared/specs/. Follow your complete workflow (Discovery, Deep Analysis, Consolidation, Plan Updates, Final Verification). Report all findings back when complete.
  ```

## After the Audit

Report the agent's findings back to the user with a concise summary including:
- Number of spec files analyzed
- Coverage statistics
- Critical gaps found (if any)
- Actions taken (tasks added/modified in the plan)
