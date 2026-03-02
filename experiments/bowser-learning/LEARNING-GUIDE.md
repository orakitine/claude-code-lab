# Learning Guide: 4-Layer Agentic Browser Automation

Based on IndieDevDan's [Bowser](https://github.com/disler/bowser) repo and [video](https://www.youtube.com/watch?v=efctPj6bjCY).

**How to use this guide**: Work through each module in order. Each builds on the previous. Write notes, build the files, test them, check the boxes. Ask Claude for help when stuck — that's the point.

**The 4-Layer Architecture:**
```
Layer 4: Justfile         (Reusability)    → Terminal entry points
Layer 3: Commands         (Orchestration)  → Coordinate agent teams
Layer 2: Subagents        (Scale)          → Parallel execution
Layer 1: Skills           (Capability)     → Raw browser control
```

Each layer builds on the one below. Each is independently testable.

**Reference files** from the original Bowser repo are saved in `./reference/` for study.

---

## Pre-work: Setup (DONE)

- [ ] Installed `@playwright/cli` — run `npx @playwright/cli --help`
- [ ] Installed `just` command runner — run `just --version` (at `~/.local/bin/just`)
- [x] Created `experiments/bowser-learning/` directory
- [x] Downloaded Bowser reference files to `./reference/`

---

## Module 1: Understanding Skills (Layer 1 — Capability)

### Concept
A **skill** teaches Claude a new capability by wrapping an external tool (CLI, API, etc.) in a structured prompt. It's the foundation — without it, Claude doesn't know the tool exists or how to use it.

> "The skill is the capability. This is the foundational layer." — Video

### What to Study
1. Read the Bowser skill: `./reference/skills/playwright-bowser-SKILL.md`
2. Read your lab's principles: `../../.claude/skills/SKILL_CREATION_PRINCIPLES.md`
3. Compare: How does Bowser's skill differ from your lab's conventions?

### Exercise 1.1: Analyze the Bowser Skill (DONE — see modules/module-1-skills.md)
Detailed adaptation walkthrough with every decision narrated.

### Exercise 1.2: Build Your Own Playwright Skill (DONE)
Created `../../.claude/skills/playwright-browser/SKILL.md` — adapted from Bowser with:
- Explicit frontmatter (trigger: manual, allowed-tools as list)
- Variables section (HEADED, VISION, VIEWPORT_SIZE, SCREENSHOTS_DIR)
- Bold step names + inline examples in every workflow step
- Removed forbidden sections (Quick Reference, Key Details, Sessions, Configuration)
- Added CLI reference doc at `docs/playwright-cli-reference.md`

### Exercise 1.3: Test the Skill (DONE)
Tested against luna.rakitine.com — opened session, navigated to homepage, clicked into first story, screenshotted, closed.

### Checkpoint
- [x] Skill file follows SKILL_CREATION_PRINCIPLES.md format
- [x] Can explain the difference between a skill and just prompting Claude directly
- [x] Successfully used the skill to screenshot luna.rakitine.com
- [x] Learning doc written in `modules/module-1-skills.md`

### Reflection Questions
- Why use a CLI instead of an MCP server? (Token efficiency — video covers this)
- What makes a good skill vs a bad skill?
- How does your skill compare to Bowser's? What did you customize?

---

## Module 2: Understanding Subagents (Layer 2 — Scale)

### Concept
A **subagent** wraps a skill into an autonomous unit that can be spawned multiple times in parallel. Each agent gets its own context, session, and can work independently.

> "The agent is where we start to specialize and scale, where the skill is just our raw capability." — Video

### What to Study
1. Read Bowser's agents: `./reference/agents/playwright-bowser-agent.md` and `./reference/agents/bowser-qa-agent.md`
2. Read your lab's docs: `../../docs/concepts/background-agents.md`
3. Notice: simple agent (thin wrapper) vs specialized agent (QA with screenshots)

### Exercise 2.1: Analyze Agent Patterns (DONE — see modules/module-2-subagents.md)
Covers: simple vs specialized agents, frontmatter pattern, session isolation for parallelism.

### Exercise 2.2: Build a Simple Browser Agent (DONE)
Created `../../.claude/agents/playwright-browser-agent.md` — thin 2-line wrapper activating playwright-browser skill.

### Exercise 2.3: Build a QA Agent (DONE)
Created `../../.claude/agents/browser-qa-agent.md` — structured pass/fail reporting with screenshots at every step.

### Exercise 2.4: Test the QA Agent (DONE)
Tested against luna.rakitine.com with 2 stories in parallel: character pill filters (8/8 PASS) and story page font sizing (8/8 PASS). Screenshots saved to `screenshots/browser-qa/`.

### Checkpoint
- [x] Can explain why agents exist as a separate layer from skills
- [x] Simple agent works for ad-hoc browser tasks
- [x] QA agent produces screenshots and a pass/fail report
- [x] Understand the frontmatter pattern for agent configuration
- [x] Learning doc written in `modules/module-2-subagents.md`

### Reflection Questions
- When would you use the simple agent vs the QA agent?
- How does named session isolation enable parallelism?
- What would happen if two agents shared the same session name?

---

## Module 3: Understanding Commands (Layer 3 — Orchestration)

### Concept
A **command** (slash command) orchestrates multiple agents into coordinated workflows. This is the "team" layer — it discovers work, distributes it to agents, and collects results.

> "The prompt controls the sub-agents. The sub-agents use the skills." — Video

### What to Study
1. Read: `./reference/commands/ui-review-summary.md`
2. Read: `./reference/commands/hop-automate-summary.md`
3. Read your lab's docs: `../../docs/concepts/commands.md`

### Exercise 3.1: Understand Orchestration Patterns (DONE — see modules/module-3-commands.md)
Covers: meta-prompting, higher-order prompts, 4-phase orchestration, keyword detection pattern.

### Exercise 3.2: Create User Story Files (DONE)
Created `../../ai_review/user_stories/hackernews.yaml` — 3 stories (front page, pagination, comments).

### Exercise 3.3: Build the UI Review Command (DONE)
Created `../../.claude/commands/ui-review.md` — 5-step workflow: Parse Args → Discover → Spawn → Collect → Report.

### Exercise 3.4: Build a Higher-Order Prompt (DONE)
Created `../../.claude/commands/bowser/hop-automate.md` — workflow runner with keyword detection for mode/vision.

### Exercise 3.5: Test Orchestration (DONE)
Ran `/ui-review` — discovered 2 YAML files (5 stories), spawned 5 parallel QA agents, all PASS. Screenshots in `screenshots/browser-qa/2026-03-01_22-56-58_c18c5b90/`.

### Checkpoint
- [x] Can explain the orchestration pattern (discover -> spawn -> collect -> report)
- [x] User stories in YAML format drive the test suite
- [x] `/ui-review` successfully coordinates parallel agents
- [x] Understand the higher-order prompt pattern
- [x] Learning doc written in `modules/module-3-commands.md`

### Reflection Questions
- Why is meta-prompting (teaching the orchestrator how to prompt sub-agents) important?
- How does this compare to traditional test frameworks (Jest/Vitest)?
- When would you use the hop-automate pattern vs a direct command?

---

## Module 4: Understanding Justfiles (Layer 4 — Reusability)

### Concept
A **justfile** is the top-level entry point — terminal-accessible recipes that compose all lower layers into quick, repeatable commands. It's how you (and other agents) discover and run everything.

> "After you have all these different ways to execute with your agent, you're going to want a repeat single place to call all these tools." — Video

### What to Study
1. Read Bowser's justfile: `./reference/justfile`
2. Read about `just`: https://just.systems/

### Exercise 4.1: Design Your Justfile (DONE — see modules/module-4-justfile.md)
Covers: layer-by-layer organization, default variables, model override, --dangerously-skip-permissions.

### Exercise 4.2: Build the Justfile (DONE)
Created `../../justfile` — 9 recipes across all 4 layers, verified with `just --list`.

### Exercise 4.3: Test End-to-End (DONE)
Ran `just ui-review` from separate terminal — full 4-layer stack fired successfully. Noted: uses `claude` (interactive) not `--print`; for CI/hooks would need `--print`.

### Checkpoint
- [x] Justfile has recipes for every layer
- [x] `just` (no args) lists all available commands
- [x] `just ui-review` triggers the full stack
- [x] Can explain why a justfile is valuable as the reusability layer
- [x] Learning doc written in `modules/module-4-justfile.md`

---

## Module 5: Synthesis & Customization

### Goal
Bring it all together. Customize the system for YOUR needs.

### Exercise 5.1: Architecture Diagram
Draw the full 4-layer stack showing data flow:
```
User runs `just ui-review`
  → justfile recipe invokes Claude with /ui-review command
    → command discovers stories, spawns parallel agents
      → each agent uses playwright-browser skill
        → skill drives Playwright CLI
          → CLI controls headless browser
```

### Exercise 5.2: Create Your Own Workflow
Pick a real use case YOU care about and build a workflow for it:
- Testing your own app, scraping data, automating a repetitive task
- Create the user story YAML, verify with the existing stack

### Exercise 5.3: Write Your Learnings
Create `LEARNINGS.md` right here in this directory:
- Key takeaways about each layer
- What surprised you
- How you'd apply this pattern to other problems (not just browsers)
- Ideas for your own specialized agents

### Final Checkpoint
- [ ] Can explain the 4-layer architecture to someone else
- [ ] Built and tested all 4 layers
- [ ] Created at least one custom workflow for your own needs
- [ ] Updated project CLAUDE.md with new skills/commands
- [ ] Written LEARNINGS.md with key insights

---

## File Summary

**Built (all 4 layers):**

| Layer | File | Status |
|-------|------|--------|
| 1 | `.claude/skills/playwright-browser/SKILL.md` | DONE |
| 1 | `.claude/skills/playwright-browser/docs/playwright-cli-reference.md` | DONE |
| 2 | `.claude/agents/playwright-browser-agent.md` | DONE |
| 2 | `.claude/agents/browser-qa-agent.md` | DONE |
| 3 | `.claude/commands/ui-review.md` | DONE |
| 3 | `.claude/commands/bowser/hop-automate.md` | DONE |
| 3 | `ai_review/user_stories/hackernews.yaml` | DONE |
| 4 | `justfile` | DONE |

**Learning docs (tiny lectures + adaptation walkthroughs):**

| Module | File | Status |
|--------|------|--------|
| 1 | `modules/module-1-skills.md` | DONE |
| 2 | `modules/module-2-subagents.md` | DONE |
| 3 | `modules/module-3-commands.md` | DONE |
| 4 | `modules/module-4-justfile.md` | DONE |
| 5 | `LEARNINGS.md` | TODO (after testing) |

**Still to do:** Exercise 4.3 (justfile end-to-end) + Module 5 synthesis.

**Note:** In Module 5, build a `hop-automate` workflow file to exercise the higher-order prompt runner hands-on.

**Reference material** (from Bowser repo):
- `./reference/skills/` — Bowser's Playwright skill
- `./reference/agents/` — Bowser's agent definitions
- `./reference/commands/` — Bowser's command summaries
- `./reference/justfile` — Bowser's justfile
- `./reference/user-stories/` — Bowser's YAML test stories
