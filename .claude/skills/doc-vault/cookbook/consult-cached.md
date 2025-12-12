# Consult Cached Documentation

Automatically consult cached docs when user requests documentation using conservative trigger mode.

## Workflow

1. **Detect Trigger**
   - Check for: "docs", "documentation", "api reference", "check docs", "latest docs", "fresh docs"
   - Do NOT trigger on topic names alone (conservative mode)
   - Example: "check the Stripe docs" → TRIGGERED ✓

2. **Load Index**
   - Tool: Read INDEX_FILE (`.claude/skills/doc-vault/README.md`)
   - Only if not already loaded in session
   - Persists for entire session (no re-read needed)
   - Example: INDEX_FILE loaded → 3 docs available (TanStack Query, Stripe Webhooks, React)

3. **Extract Topics**
   - Parse user request for keywords
   - Categories: tech names (React, Stripe), API names, tools (Git, AWS), concepts (auth, webhooks)
   - Example: "check Stripe docs for webhooks" → Topics: ["Stripe", "webhooks"]

4. **Match to Cached Docs**
   - Search index: doc names and descriptions
   - Find best match(es)
   - Example: "Stripe" + "webhooks" → Match: "stripe-webhooks-2025-12-11.md"

5. **Read & Apply Cached Doc**
   - IF match found: Read from CACHE_DIR, use as authoritative reference, prefer over training data
   - IF no match: Use training data (silent fallback, don't announce missing doc)
   - Example: Read cache/stripe-webhooks-2025-12-11.md → Answer using cached content

6. **Cite Source**
   - IF CITE_SOURCES is true: State source and date
   - Format: "Using cached [Name] docs (YYYY-MM-DD)"
   - Example: "Using cached Stripe Webhooks docs (2025-12-11)"
