# API Docs Fetcher Skill - Learning Notes

**Date:** 2025-12-11
**Phase:** Phase 3 - Power Features
**Topics Covered:** Skills, Tools, Parallel Execution, Caching Strategies

---

## What We Built

A complete **API Documentation Fetcher** skill that:
- Auto-triggers when user mentions "api docs" + library name
- Fetches documentation from official sources
- Caches docs locally with date stamps (7-day TTL)
- Maintains a learning registry of libraries
- Supports parallel fetching of multiple libraries

### File Structure

```
.claude/skills/api-docs-fetcher/
├── SKILL.md                  # Orchestrator (triggers, instructions)
├── tools/
│   └── fetch_docs.py         # Python tool (fetch/cache/registry logic)
└── parallel-demo.sh          # Demo script for Phase 3 learning

docs/api-cache/
├── .gitignore                # Ignore *.md, keep registry.json
├── registry.json             # Library → URL mappings + config
├── tanstack-query-2025-12-11.md
├── react-2025-12-11.md
└── ... (cached docs with datestamps)
```

---

## Key Concepts Learned

### 1. Skills + Tools Pattern

**SKILL.md** = The brain (orchestration)
- Detects trigger phrases
- Extracts context (library names)
- Invokes tools
- Uses results for the actual task

**Python Tool** = The hands (execution)
- Does the heavy lifting
- Handles complex logic
- Returns structured data (JSON)

### 2. Registry Pattern (Cookbook + Learning)

The registry.json serves as:
- **Cookbook**: Pre-populated with common libraries
- **Memory**: Learns new libraries when added
- **Alias Resolver**: "react-query" → "tanstack-query"
- **Configuration**: Per-library cache TTL

This creates a **self-improving system** that gets smarter over time!

### 3. Caching Strategy

**File Naming:** `library-YYYY-MM-DD.md`
- Easy to identify freshness
- Automatic cleanup possible (delete old dates)
- Git-friendly (.gitignore keeps cache out of repo)

**TTL (Time To Live):**
- Default: 7 days
- Configurable per library in registry
- Stable libs (React): 14 days
- Fast-moving libs (Prisma, Next.js): 7 days

### 4. Phase 3: Parallel Execution

**The Problem:**
Fetching 3 libraries sequentially:
- Library 1: 2s
- Library 2: 2s
- Library 3: 2s
- **Total: 6 seconds**

**The Solution:**
Fetching 3 libraries in parallel:
- All three fetch simultaneously
- **Total: 2 seconds**

**The Pattern:**
```bash
# Sequential (blocking)
fetch_docs.py "lib1"
fetch_docs.py "lib2"
fetch_docs.py "lib3"

# Parallel (non-blocking)
fetch_docs.py "lib1" &
fetch_docs.py "lib2" &
fetch_docs.py "lib3" &
wait  # Wait for all to complete
```

**Key Symbols:**
- `&` = Run in background (don't wait)
- `wait` = Wait for all background jobs

---

## How To Use

### Basic Usage

User says naturally:
> "Implement query caching with TanStack Query and consult real api docs"

The skill:
1. Detects "api docs" + "TanStack Query"
2. Runs: `fetch_docs.py "tanstack query"`
3. Returns cached docs (or fetches if stale)
4. Uses docs as context for implementation

### Testing the Tool Directly

```bash
# Known library (uses registry)
.claude/skills/api-docs-fetcher/tools/fetch_docs.py "tanstack query"

# Unknown library (provide URL)
.claude/skills/api-docs-fetcher/tools/fetch_docs.py "zod" "https://zod.dev"

# Force refresh (ignore cache)
.claude/skills/api-docs-fetcher/tools/fetch_docs.py "react" --force

# Test parallel execution
.claude/skills/api-docs-fetcher/parallel-demo.sh
```

### Adding New Libraries

**Option 1: Let the skill ask**
- User: "Check ramda docs"
- Skill: "I don't have a URL for ramda. What's the docs URL?"
- User provides URL
- Tool adds to registry automatically

**Option 2: Add manually to registry.json**
```json
{
  "ramda": {
    "url": "https://ramdajs.com/docs/",
    "aliases": ["ramda.js", "ramda functional"],
    "description": "Ramda functional programming library",
    "cache_days": 14
  }
}
```

---

## Technical Details

### Tool Output Format

```json
{
  "status": "cached" | "fetched" | "error",
  "path": "/full/path/to/cached-file.md",
  "message": "Human readable description",
  "library": "canonical-library-name",
  "age_days": 0
}
```

### Path Resolution Gotcha

**Initial bug:** Path calculation was off by one level!

```python
# WRONG (missing one parent)
project_root = script_dir.parent.parent.parent

# RIGHT
project_root = script_dir.parent.parent.parent.parent
# tools → skill → skills → .claude → project
```

**Lesson:** When building tools, always test path resolution!

### Content Cleaning

The tool does basic HTML cleaning:
- Removes `<script>` and `<style>` tags
- Removes HTML comments
- Strips tags (basic conversion)
- Adds metadata header with source URL and fetch date

**Future Enhancement:** Use `html2text` or `BeautifulSoup` for better conversion.

---

## What I Learned

### Phase 3 Concepts

1. **Parallel vs Sequential Execution**
   - When tasks don't depend on each other → parallelize!
   - Massive time savings for I/O-bound operations
   - Use `&` and `wait` in bash, or background agents in Claude

2. **Self-Improving Systems**
   - Registry learns new libraries over time
   - Each new library request improves the system
   - Balances convenience (cookbook) with flexibility (add new)

3. **Caching Strategies**
   - TTL-based caching reduces network requests
   - Datestamped files make freshness explicit
   - Per-library configuration allows fine-tuning

### Practical Skills

1. **Building Custom Tools**
   - Python tools extend Claude's capabilities
   - Return JSON for structured data
   - Use stderr for logs, stdout for results

2. **Registry Patterns**
   - Canonical names + aliases for flexible matching
   - Configuration alongside data
   - JSON for easy editing and versioning

3. **Skill Architecture**
   - SKILL.md is the orchestrator
   - Tools do the heavy lifting
   - Clear separation of concerns

---

## Next Steps

### Enhancements to Try

- [ ] Add `--format` flag for JSON/markdown/text output
- [ ] Implement automatic stale cache cleanup
- [ ] Add summary extraction (use LLM to summarize docs)
- [ ] Support multiple URLs per library (fallbacks)
- [ ] Add `--search` to search within cached docs
- [ ] Create MCP server version for external access
- [ ] Add telemetry (track most-used libraries)

### Phase 3 Experiments

- [ ] Fetch 5+ libraries in parallel and measure speedup
- [ ] Build a "research mode" that fetches related libraries automatically
- [ ] Create background agent pattern for long-running fetches
- [ ] Implement progress reporting for parallel fetches

### Phase 4 Ideas

- [ ] Multi-variant skill (cookbook pattern) for different doc sources
- [ ] Context handoff: pass fetched docs to specialized agents
- [ ] Hook integration: auto-fetch docs when package.json changes

---

## Reflections

**What worked well:**
- Registry + cookbook pattern is brilliant
- Parallel execution demo made the concept click
- Real-world utility ensures I'll actually use this

**What was challenging:**
- Path resolution bug took time to debug
- HTML cleaning is basic (could be better)
- Initial alias matching confusion

**Key Insight:**
Building tools you'll actually use is the best way to learn. This skill solves a real problem (outdated training data) while teaching Phase 3 concepts (parallel execution).

---

## Related Documentation

- [Skills Concept Guide](../../docs/concepts/skills.md)
- [Tools Concept Guide](../../docs/concepts/tools.md)
- [Background Agents Guide](../../docs/concepts/background-agents.md)
- [Skill Patterns Examples](../../docs/examples/skill-patterns.md)

---

**Session completed:** 2025-12-11
**Status:** ✅ Fully functional, tested, and documented
**Phase 3 Progress:** Complete - ready for Phase 4!
