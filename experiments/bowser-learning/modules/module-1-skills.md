# Module 1: Understanding Skills (Layer 1 — Capability)

## Tiny Lecture: What IS a Skill?

A skill is a **structured prompt** that teaches Claude how to use a tool. Without it, Claude would have to guess commands, forget flags, and make up workflows. With a skill, Claude has a reliable cheat sheet baked into its context.

**Why not just tell Claude "use playwright-cli"?**
You *could*, but every time you'd need to re-explain the commands, the flags, the session management pattern, what order to do things in. A skill makes this **reusable** — write it once, use it forever.

**Why a CLI instead of an MCP server?** (from the video)
> "You want to be using CLIs, not MCP servers. MCP servers chew up your tokens and they're very rigid."

CLIs are token-efficient because Claude just runs bash commands. MCP servers inject tool schemas, accessibility trees, and response overhead into the context window. The Playwright CLI keeps things lean.

---

## Adaptation Walkthrough: Bowser → Our Lab

Here's what I changed from Bowser's `playwright-bowser/SKILL.md` and **why**:

### 1. Frontmatter — Added `trigger: manual`

**Bowser's version:**
```yaml
---
name: playwright-bowser
description: ...
allowed-tools: Bash          # ← string, not a list
---
```

**Our version:**
```yaml
---
name: Playwright Browser
description: ...
trigger: manual               # ← ADDED (principles require explicit trigger)
allowed-tools:                 # ← Changed to list format
  - Bash
  - Read
  - Write
---
```

**Why `manual`?** Browser automation has side effects (opens browsers, takes screenshots, writes files). You don't want Claude auto-launching browsers every time you mention "playwright". Manual = user explicitly activates.

**Why `Read` and `Write`?** The skill needs to read config files and write screenshots. Bowser only listed `Bash`, which is technically enough (you can read/write via bash), but our principles say to be explicit about tool intentions.

### 2. Removed Forbidden Sections

Bowser had these sections that our principles forbid:
- **"Key Details"** → merged into Purpose paragraph
- **"Sessions"** → merged into Workflow step 1
- **"Quick Reference"** → DELETED (duplicates Workflow)
- **"Configuration"** → merged into Workflow step 1 as a conditional
- **"Full Help"** → merged as inline note in Workflow

**Principle violated:** "Single Source of Truth — every piece of information exists in exactly ONE place."

The Quick Reference in Bowser literally duplicated every command already shown in the Workflow. That's the kind of thing that rots — someone updates the Workflow but forgets to update Quick Reference.

### 3. Added Variables Section

**Bowser:** No variables section. Defaults scattered throughout prose.

**Our version:**
```
HEADED: false                    # Show browser window. Options: true, false
VISION: false                    # Return screenshots as images in context
VIEWPORT_SIZE: 1440x900          # Browser viewport dimensions
SCREENSHOTS_DIR: ./screenshots   # Where screenshots are saved
```

**Why?** Our principles say: "Only include configurable values." These four things are the knobs you'd want to turn. Everything else (session naming, command syntax) is workflow logic, not configuration.

### 4. Workflow Steps — Added Bold Names + Inline Examples

**Bowser:** Numbered steps but NO bold names, NO consistent inline examples.

**Our version:** Every step follows the pattern:
```markdown
1. **Open Session**
   - Derive kebab-case session name from user's prompt
   - Example: "test checkout on mystore.com" → `-s=mystore-checkout`
   - Tool: Bash `PLAYWRIGHT_MCP_VIEWPORT_SIZE=... playwright-cli -s=<name> open <url> --persistent`
```

**Why bold names?** Scanability. You can glance at the workflow and see the shape: Open → Snapshot → Interact → Screenshot → Close. Bowser's version was a wall of code blocks.

**Why inline examples?** Our principles: "EVERY step has at least one inline example." This prevents Claude from misinterpreting what a step means.

### 5. Added Cookbook Section

**Bowser:** No cookbook. Everything in one file.

**Our version:** Added cookbooks for headless vs headed modes, since they have different command flags and use cases.

**Why?** Our principles say use cookbooks "when different workflows for different contexts." Headless mode (for CI/testing) and headed mode (for debugging/demos) are different enough to warrant separate guidance. But for now, the skill is simple enough that we keep it all in SKILL.md with inline conditionals.

---

## Key Takeaways

1. **A skill = structured prompt wrapping a CLI tool** — it gives Claude reliable, reusable knowledge
2. **CLI over MCP** — token-efficient, flexible, composable
3. **Frontmatter matters** — explicit trigger + allowed-tools = security + intent documentation
4. **Single Source of Truth** — never duplicate information across sections
5. **Bold step names + inline examples** — make workflows scannable and unambiguous
6. **Variables = knobs** — only things you'd want to configure belong here
7. **Named sessions** — the key enabler for parallelism (each agent gets its own session)

---

## Your Notes

(Add your own observations, questions, or ideas here as you review the skill)


