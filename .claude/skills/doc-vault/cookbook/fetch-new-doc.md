# Purpose

Fetch fresh documentation from a URL and cache it for future use.

## Variables

CACHE_DIR: .claude/skills/doc-vault/cache
INDEX_TOOL: .claude/skills/doc-vault/tools/manage_index.py

## Instructions

1. Extract the URL and doc name from the user's request
2. Use the WebFetch tool to retrieve clean content:
   - Prompt: "Extract the main documentation content. Focus on API reference, guides, and code examples. Convert to clean markdown. Ignore navigation, footer, sidebars, and ads. Include the page title."
3. Save the fetched content to: `CACHE_DIR/<name>-YYYY-MM-DD.md`
4. Include frontmatter metadata:
   ```yaml
   ---
   url: <source-url>
   fetched: YYYY-MM-DD
   title: <page-title>
   description: <one-sentence-description>
   ---
   ```
5. Update the index by running: `INDEX_TOOL update "<name>" "<description>" "YYYY-MM-DD"`
6. Confirm to user:
   - ✓ Fetched and cached [Library] docs
   - ✓ Saved to: cache/<name>-YYYY-MM-DD.md
   - ✓ Updated doc vault index

## Description Guidelines

If user doesn't provide a description:
- Extract from page title and first paragraph
- Keep it one sentence
- Focus on what the doc covers

## Example Execution

User: "save docs from https://zod.dev as zod-validation"

1. WebFetch https://zod.dev
2. Save to cache/zod-validation-2025-12-11.md with frontmatter
3. Run: manage_index.py update "zod-validation" "TypeScript-first schema validation library"
4. Confirm to user
