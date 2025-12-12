# List Available Documentation

Show user what documentation is currently cached in the doc vault.

## Workflow

1. **Read Index**
   - Tool: Read INDEX_FILE (`.claude/skills/doc-vault/README.md`)
   - Parse "## Cached Documents" section
   - Example: INDEX_FILE contains 2 TanStack Query docs

2. **Format Output**
   - Group by library/framework
   - Show: doc name, date cached, description
   - Include total count and last updated date
   - Example format:
     ```
     Doc Vault - Cached Documentation:

     ### TanStack Query
       • tanstack-query-optimistic-updates (2025-12-11)
         Two strategies for optimistically updating UI
       • tanstack-query-options (2025-12-11)
         Query configuration helper for type safety

     ---
     Total: 2 documents
     Last updated: 2025-12-11
     ```

3. **Present to User**
   - Display formatted list
   - Alternative: Can also use `tools/manage_index.py list` for quick file listing
   - Example: Show complete formatted list with all cached docs grouped by library
