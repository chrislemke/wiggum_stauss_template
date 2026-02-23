---
description: Resolve !! annotations in spec files or implementation plan
---

# Resolve Annotations

You are tasked with resolving `!!` annotations that the user has left in specification or implementation plan files.

## Step 1: Ask the User

Use `AskUserQuestion` to ask which files to scan:

- **Question**: "Which files should I scan for `!!` annotations?"
- **Header**: "Scan target"
- **Options**:
  1. **Specification files** — Scan all spec files in `thoughts/shared/specs/`
  2. **Implementation plan** — Scan `thoughts/shared/plan/IMPLEMENTATION_PLAN.md`
  3. **Both** — Scan specs and implementation plan

## Step 2: Launch the Agent

Use the Task tool to launch the `annotation-resolver` agent:

- `subagent_type`: `annotation-resolver`
- `description`: `Resolve !! annotations`
- `prompt`: Tell the agent which files/directories to scan based on the user's choice:
  - **Specification files**: `Scan all files in thoughts/shared/specs/ for !! annotations. Follow your complete workflow (Discovery, Resolution, Verification).`
  - **Implementation plan**: `Scan thoughts/shared/plan/IMPLEMENTATION_PLAN.md for !! annotations. Follow your complete workflow (Discovery, Resolution, Verification).`
  - **Both**: `Scan all files in thoughts/shared/specs/ and thoughts/shared/plan/IMPLEMENTATION_PLAN.md for !! annotations. Follow your complete workflow (Discovery, Resolution, Verification).`

## Step 3: Report Results

Report the agent's findings back to the user with a concise summary including:
- Number of annotations found
- Number of annotations resolved
- Any annotations that required clarification or could not be resolved
- Files that were modified
