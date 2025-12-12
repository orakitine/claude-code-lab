---
name: Doc Vault Skill
description: Auto-activating documentation cache with fresh API docs. Fetches and automatically consults cached documentation when user works with libraries/frameworks.
---

# Purpose

Fetch and automatically consult cached documentation from official sources. Provides fresh, up-to-date API documentation that overrides stale training data.

Follow the `Instructions`, execute the `Workflow`, based on the `Cookbook`.

## Variables

CACHE_DIR: .claude/skills/doc-vault/cache
INDEX_FILE: .claude/skills/doc-vault/README.md
TRIGGER_SENSITIVITY: conservative
CITE_SOURCES: true
INDEX_TOOL: .claude/skills/doc-vault/tools/manage_index.py

## Instructions

- TRIGGER_SENSITIVITY is conservative: Only activates on explicit "docs" keywords
- Once triggered in a session, INDEX_FILE stays loaded in context for entire session
- Based on the user's request, follow the `Cookbook` to determine the appropriate action
- IF CITE_SOURCES is true, always state source and date when using cached docs
- Prefer cached docs over training data when available

## Workflow

1. Detect trigger (explicit "docs" keywords per conservative mode)
2. IF first trigger in session, READ INDEX_FILE (loads into context, persists for session)
3. Follow the `Cookbook` based on user's request
4. Execute the appropriate cookbook scenario
5. IF using cached docs, cite source and date

## Cookbook

### Fetch New Documentation

- IF: User provides URL with "save docs from" or "cache docs"
- THEN: Read and execute `.claude/skills/doc-vault/cookbook/fetch-new-doc.md`
- EXAMPLES:
  - "save docs from https://zod.dev as zod-validation"
  - "cache docs: https://prisma.io/docs/orm as prisma-orm"
  - "add to doc vault: https://trpc.io/docs as trpc-api"

### Consult Cached Documentation

- IF: User mentions "docs" OR "documentation" OR "api reference" (conservative trigger)
- THEN: Read and execute `.claude/skills/doc-vault/cookbook/consult-cached.md`
- EXAMPLES:
  - "check the TanStack Query docs and implement caching"
  - "according to the latest Prisma docs, add migrations"
  - "consult the React docs for Suspense"
  - "use fresh Zod docs for validation"

### List Available Documentation

- IF: User asks what documentation is cached
- THEN: Read and execute `.claude/skills/doc-vault/cookbook/list-docs.md`
- EXAMPLES:
  - "what docs do we have?"
  - "list cached documentation"
  - "show me the doc vault"
  - "what's in the cache?"

## Notes

- Conservative mode: Only triggers on explicit "docs" keywords
- Session persistence: Index loads once, stays for entire session
- The skill learns over time (more docs = more useful)
- Docs are dated so freshness is always visible
- Index is lightweight (just list + descriptions)
- WebFetch provides clean markdown (no HTML cruft)
- Context-optimized (only loads when user says "docs")
