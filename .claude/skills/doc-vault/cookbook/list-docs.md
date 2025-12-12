# Purpose

Show user what documentation is currently cached in the doc vault.

## Variables

INDEX_FILE: .claude/skills/doc-vault/README.md

## Instructions

1. READ the INDEX_FILE
2. Parse the "## Cached Documents" section
3. Present to user in formatted view:
   - Group by library/framework
   - Show doc name, date, and description
   - Include total count

## Output Format

```
Doc Vault - Cached Documentation:

### [Library Name]
  • [doc-name] (YYYY-MM-DD) - Description

### [Library Name]
  • [doc-name] (YYYY-MM-DD) - Description
  • [doc-name] (YYYY-MM-DD) - Description

---
Total: X documents
Last updated: YYYY-MM-DD
```

## Example Execution

User: "what docs do we have?"

1. READ INDEX_FILE
2. Parse cached docs section
3. Output:

```
Doc Vault - Cached Documentation:

### TanStack Query
  • tanstack-query-optimistic-updates (2025-12-11)
    Two strategies for optimistically updating UI before mutations complete

  • tanstack-query-options (2025-12-11)
    Query configuration helper for sharing queryKey and queryFn with type safety

---
Total: 2 documents
Last updated: 2025-12-11
```

## Alternative: Use Python Tool

Can also use: `tools/manage_index.py list` for quick file listing
