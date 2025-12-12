# Fetch New Documentation

Fetch fresh documentation from a URL and cache it for future use.

## Workflow

1. **Extract URL and Name**
   - Parse user request for source URL and doc name
   - Example: "save docs from https://zod.dev as zod-validation" → URL: zod.dev, Name: zod-validation

2. **Fetch Documentation**
   - Tool: WebFetch with prompt: "Extract main documentation content. Focus on API reference, guides, code examples. Convert to clean markdown. Ignore navigation, footer, sidebars, ads. Include page title."
   - Result: Clean markdown content
   - Example: WebFetch https://zod.dev → Markdown content about Zod schema validation

3. **Save to Cache**
   - Save to: `CACHE_DIR/<name>-YYYY-MM-DD.md`
   - Include frontmatter: url, fetched date, title, description
   - If user didn't provide description: Extract from page title and first paragraph (one sentence)
   - Example: Save to cache/zod-validation-2025-12-11.md with metadata

4. **Update Index**
   - Tool: Run INDEX_TOOL update command
   - Command: `manage_index.py update "<name>" "<description>" "YYYY-MM-DD"`
   - Example: manage_index.py update "zod-validation" "TypeScript-first schema validation" "2025-12-11"

5. **Confirm to User**
   - Report success with details
   - Format: "✓ Fetched and cached <name> docs\n✓ Saved to: cache/<name>-YYYY-MM-DD.md\n✓ Updated doc vault index"
   - Example: "✓ Fetched and cached Zod docs\n✓ Saved to: cache/zod-validation-2025-12-11.md\n✓ Updated doc vault index"
