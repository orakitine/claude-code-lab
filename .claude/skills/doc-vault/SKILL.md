# Doc Vault Skill

Auto-activating documentation cache. Provides fresh, up-to-date API documentation that overrides stale training data.

## Purpose

Fetch and automatically consult cached documentation from official sources. When user works with libraries/frameworks, automatically use the latest cached docs instead of potentially outdated training data.

## Triggers

### Auto-Activation Triggers (loads index on first use)
- Library/framework names: "TanStack Query", "Prisma", "React", "Next.js", "Zod", etc.
- Doc keywords: "latest docs", "fresh docs", "according to docs", "api reference"
- Technical implementation: "implement", "configure", "set up" (with technical context)

### Cache Management Triggers (explicit)
- "save docs from <URL> as <name>"
- "cache docs: <URL>"
- "add to doc vault: <URL>"

## Auto-Activation Behavior

### First Trigger in Session

When ANY trigger detected for the first time in a conversation:

1. **Load the index:**
   - Read `.claude/skills/doc-vault/README.md`
   - Load cache index into context memory
   - Index stays loaded for remainder of session

2. **Announce activation (optional):**
   ```
   "Doc vault activated. Fresh docs available:
    • TanStack Query Options (2025-12-11)
    • Prisma Migrations (2025-12-10)
    • [etc.]"
   ```
   OR silently activate (just use docs without announcement)

3. **Search for relevant docs:**
   - Check if user query matches any cached doc
   - Match by: library name, keywords in description, topic

4. **Auto-consult if found:**
   - Read the full cached doc
   - Use it as authoritative reference
   - Always mention: "Using cached [Library] docs (YYYY-MM-DD)"

### Subsequent Triggers in Same Session

Once index is loaded:

1. **Skip re-loading** (index already in context)
2. **Search index** for relevant docs
3. **Auto-consult** matching docs
4. **Cite source** and date

## Automatic Consultation

Once doc vault is active (index loaded):

**ALWAYS:**
- Check cache first when user mentions technical topics
- Prefer cached docs over training data
- Auto-consult without asking permission
- Mention what docs were used: "Using cached X docs (YYYY-MM-DD)"
- Be transparent about sources

**MATCHING:**
- Library names: "TanStack Query" → find "tanstack-query-options"
- Keywords: "migrations" → search descriptions for "migration"
- Topics: "caching", "validation", etc. → match to relevant docs
- Best match: Use most relevant doc automatically

**TRANSPARENCY:**
Always state when cached docs are used:
- "Using cached TanStack Query docs (2025-12-11)"
- "According to cached Prisma docs (2025-12-10)"
- User always knows the source

## Cache Management

### Adding New Docs

When user says: "save docs from <URL> as <name>"

**Steps:**

1. **Fetch content:**
   - Use WebFetch tool with prompt:
     "Extract the main documentation content. Focus on API reference, guides, and code examples. Convert to clean markdown. Ignore navigation, footer, sidebars, and ads."

2. **Save to cache:**
   - File: `.claude/skills/doc-vault/cache/<name>-YYYY-MM-DD.md`
   - Include frontmatter:
     ```yaml
     ---
     url: <source-url>
     fetched: YYYY-MM-DD
     title: <page-title>
     description: <one-sentence-description>
     ---
     ```

3. **Update index:**
   - Edit `.claude/skills/doc-vault/README.md`
   - Add new entry with description
   - Update total count and timestamp
   - Group by library/framework if applicable

4. **Update in-memory index:**
   - If index already loaded, update the in-context version
   - New doc immediately available for consultation

5. **Confirm to user:**
   ```
   ✓ Fetched and cached [Library] docs
   ✓ Saved to: cache/<name>-YYYY-MM-DD.md
   ✓ Updated doc vault index
   ✓ Available for use
   ```

### File Naming

- User provides base name: `"save docs as tanstack-query-options"`
- You append date: `tanstack-query-options-2025-12-11.md`
- Dated files ensure freshness is visible

### Description

If user doesn't provide description:
- Auto-extract from page title + first paragraph
- Or use: `"<Library> documentation"`
- Keep it one sentence, descriptive

### Multiple Versions

If doc with same base name exists:
- Create new dated version (don't overwrite old)
- Update README.md to show only latest
- Old versions remain in cache/ (historical reference)

## Context Optimization

**When skill triggers:**
- First trigger: Load index (~small overhead)
- Subsequent: Index already in context (no overhead)

**When skill doesn't trigger:**
- No library names mentioned
- No technical keywords
- Skill stays dormant
- No index loaded
- Saves context window

## Example Workflows

### Example 1: Auto-activate and use

```
User: "Implement query caching with 5-minute staleTime"

Skill:
  - Detects "query caching" (technical + potentially cached)
  - First trigger → loads README.md index
  - Finds "tanstack-query-options" in index
  - Reads cache/tanstack-query-options-2025-12-11.md
  - Uses it for implementation

Response:
  "Using cached TanStack Query docs (2025-12-11)

   Here's how to implement query caching with staleTime:
   [implementation using fresh docs]"
```

### Example 2: Add new doc mid-session

```
User: "Save docs from https://zod.dev as zod-validation"

Skill:
  - Loads index (if not loaded)
  - Fetches via WebFetch
  - Saves to cache/zod-validation-2025-12-11.md
  - Updates README.md
  - Updates in-memory index

Response:
  "✓ Fetched and cached Zod docs
   ✓ Saved to: cache/zod-validation-2025-12-11.md
   ✓ Updated doc vault index"

---

User: "Add Zod validation to the form"

Skill:
  - Index already loaded
  - Finds newly added zod-validation
  - Reads and uses it

Response:
  "Using cached Zod docs (2025-12-11)
   [implementation]"
```

### Example 3: No activation when not needed

```
User: "Refactor variable names for clarity"

Skill:
  - No triggers detected
  - Doesn't activate
  - No index loaded
  - Saves context window

Response:
  [Normal refactoring without doc vault]
```

## Files

- **Index:** `.claude/skills/doc-vault/README.md` (auto-loaded on first trigger)
- **Cache:** `.claude/skills/doc-vault/cache/*.md` (dated docs with frontmatter)
- **Tool:** `.claude/skills/doc-vault/tools/manage_docs.py` (WebFetch + save + update)

## Best Practices

1. **Always cite sources** - User should know when cached docs are used
2. **Prefer cached over training** - Fresh docs beat stale memory
3. **Auto-consult, don't ask** - Seamless experience
4. **Be transparent** - State doc source and date
5. **Keep descriptions short** - One sentence in README.md
6. **Date all files** - Freshness should be visible
7. **Update index atomically** - Add doc + update README together

## Notes

- This skill learns over time (more docs = more useful)
- Docs are dated so freshness is always visible
- Index is lightweight (just list + descriptions)
- WebFetch provides clean markdown (better than crude scraping)
- User never needs to manually activate (auto-loads on first use)
