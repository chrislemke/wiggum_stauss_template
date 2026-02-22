---
description: Generate an index of all spec files with plan coverage and summaries
---

# Generate Specification Index

Create or update `thoughts/shared/specs/index.md` with a table summarizing all specification files.

## Steps

1. **Discover spec files**: Read all specification files in `thoughts/shared/specs/`, excluding `.gitkeep`, `.DS_Store`, and `index.md` itself.

2. **For each spec file**:
   - Write the file name in the column `File`. 
   - Read the file and write a single-sentence summary capturing its purpose.
   - Mark "No" in the `In IMPLEMENTATION_PLAN.md` column.

3. **Write `thoughts/shared/specs/index.md`** with this format:

```markdown
# Specification Index

| File | In IMPLEMENTATION_PLAN.md | Summary |
|------|---------------------------|---------|
| `filename.md` | Yes / No | One-sentence summary |
```

If no spec files are found, write the index with an empty table.

5. **Report** the result to the user: how many specs were indexed, how many are covered by the plan, and any that are missing from the plan.
