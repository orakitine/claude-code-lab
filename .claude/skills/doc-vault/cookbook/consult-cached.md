# Purpose

Automatically consult cached documentation when user explicitly requests docs (conservative mode).

## Variables

INDEX_FILE: .claude/skills/doc-vault/README.md
CACHE_DIR: .claude/skills/doc-vault/cache
CITE_SOURCES: true
TRIGGER_SENSITIVITY: conservative

## Instructions

### Trigger Detection (Conservative Mode)

Only trigger when user says:
- "docs", "documentation", "api reference"
- "check docs", "latest docs", "fresh docs", "according to docs", "consult docs"

Do NOT trigger on topic names alone.

### Search for Relevant Docs

Once triggered:

1. Read INDEX_FILE (if not already in conversation context)

2. Analyze user's request for topics/keywords:
   - Technology names (React, Stripe, Docker, etc.)
   - API names (Payments API, User API, etc.)
   - Tools/services (Git, AWS, PostgreSQL, etc.)
   - Concepts (authentication, webhooks, migrations, etc.)

3. Match request to cached docs:
   - Check index for matching doc names
   - Search descriptions for keywords
   - Find best match(es)

4. IF relevant doc(s) found:
   - READ the cached doc from CACHE_DIR
   - Use content as authoritative reference
   - Prefer cached docs over training data

5. IF CITE_SOURCES is true:
   - Always state: "Using cached [Doc Name] docs (YYYY-MM-DD)"
   - Be transparent about source

6. IF no relevant doc found:
   - Proceed with training data (silently)
   - Do not mention missing docs
   - Just answer the question

## Matching Examples

### Direct Name Match
```
User: "check the Stripe docs for webhooks"
→ Trigger: "docs" ✓
→ Topic: "Stripe"
→ Index match: "stripe-webhooks"
→ Use this doc
```

### Keyword Match
```
User: "consult docs for OAuth 2.0 flows"
→ Trigger: "docs" ✓
→ Keywords: "OAuth", "flows"
→ Index match: "oauth-authorization"
→ Use this doc
```

### Concept Match
```
User: "according to the docs, how do I handle retries?"
→ Trigger: "docs" ✓
→ Concept: "retries"
→ Search descriptions for "retry", "retries"
→ Use best match
```

## Example Execution

User: "Check the Stripe API docs and implement webhook handling"

1. Trigger: "docs" ✓
2. Read INDEX_FILE (if not already in context)
3. Extract topic: "Stripe API"
4. Search index for "stripe*"
5. Find match: "stripe-webhooks"
6. READ: cache/stripe-webhooks-2025-12-11.md
7. Use content for implementation
8. State: "Using cached Stripe Webhooks docs (2025-12-11)"

## Notes

- INDEX_FILE persists in conversation context once read
- No need to re-read on subsequent requests in same session
- Docs can be for any technology, API, tool, or concept
- Not limited to JavaScript/frontend - works for anything with documentation
