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

### Exercise 1.3: Test the Skill
Activate the skill manually and ask Claude to:
1. Open a headless browser session named "test-hn"
2. Navigate to https://news.ycombinator.com
3. Take a screenshot
4. Close the session

### Checkpoint
- [x] Skill file follows SKILL_CREATION_PRINCIPLES.md format
- [ ] Can explain the difference between a skill and just prompting Claude directly
- [ ] Successfully used the skill to screenshot Hacker News
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

### Exercise 2.1: Analyze Agent Patterns
Answer in `module-2-notes.md`:
1. What's the difference between the simple `playwright-bowser-agent` and the specialized `bowser-qa-agent`?
2. How does the QA agent structure its output (pass/fail, screenshots)?
3. What is the "agent frontmatter" pattern (model, skills activation)?
4. How do agents enable parallelism that a single skill can't?

### Exercise 2.2: Build a Simple Browser Agent
Create `../../.claude/agents/playwright-browser-agent.md`:
- Thin wrapper that activates the playwright-browser skill
- Takes a prompt, executes browser work, returns results
- Keep it simple — this is the "general purpose" agent

### Exercise 2.3: Build a QA Agent
Create `../../.claude/agents/browser-qa-agent.md`:
- Specialized agent that accepts user stories
- Parses stories into discrete steps
- Creates screenshot directory per story
- Executes steps with screenshots at each stage
- Returns structured pass/fail report

### Exercise 2.4: Test the QA Agent
Use the agent directly (via `@browser-qa-agent` reference) with this story:
```
Name: Hacker News Front Page
URL: https://news.ycombinator.com
Steps:
1. Navigate to the URL
2. Verify the page title contains "Hacker News"
3. Confirm at least 10 story links are visible
4. Take a screenshot of the front page
```

### Checkpoint
- [ ] Can explain why agents exist as a separate layer from skills
- [ ] Simple agent works for ad-hoc browser tasks
- [ ] QA agent produces screenshots and a pass/fail report
- [ ] Understand the frontmatter pattern for agent configuration
- [ ] Notes written in `module-2-notes.md`

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

### Exercise 3.1: Understand Orchestration Patterns
Answer in `module-3-notes.md`:
1. What are the 4 phases of `/ui-review`? (Discover, Spawn, Collect, Report)
2. How does the command teach the orchestrator agent to prompt sub-agents? (Meta-prompting)
3. What is a "higher-order prompt" (hop)? How is it like a function that takes a function?
4. How do user stories get discovered and distributed?

### Exercise 3.2: Create User Story Files
Create `../../ai_review/user_stories/hackernews.yaml` (see `./reference/user-stories/hackernews.yaml` for format)

### Exercise 3.3: Build the UI Review Command
Create `../../.claude/commands/ui-review.md`:
- Phase 1: Discover — glob YAML files from `ai_review/user_stories/`
- Phase 2: Spawn — fan out stories to parallel `@browser-qa-agent` instances
- Phase 3: Collect — gather pass/fail results from all agents
- Phase 4: Report — generate summary table

### Exercise 3.4: Build a Higher-Order Prompt
Create `../../.claude/commands/bowser/hop-automate.md`:
- Accepts $ARGUMENTS as a workflow file path
- Loads the workflow, wraps it in consistent setup/teardown
- Executes via the playwright skill

### Exercise 3.5: Test Orchestration
Run `/ui-review` and verify:
- Multiple agents spawn in parallel
- Each produces screenshots in its own directory
- Summary report shows pass/fail for all stories

### Checkpoint
- [ ] Can explain the orchestration pattern (discover -> spawn -> collect -> report)
- [ ] User stories in YAML format drive the test suite
- [ ] `/ui-review` successfully coordinates parallel agents
- [ ] Understand the higher-order prompt pattern
- [ ] Notes written in `module-3-notes.md`

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

### Exercise 4.1: Design Your Justfile
Plan recipes in `module-4-notes.md`:
- What recipes do you need for each layer?
- What default parameters make sense?
- How should variables be overridable?

### Exercise 4.2: Build the Justfile
Create `../../justfile` (project root) with recipes for each layer:
```
default              — list all commands
test-skill prompt    — test the raw playwright skill
test-qa story        — test a single QA agent run
ui-review            — run full parallel UI review
automate workflow    — run a browser automation workflow
```

### Exercise 4.3: Test End-to-End
Run `just ui-review` from terminal and verify the entire 4-layer stack fires:
```
justfile → command → agents → skill → Playwright CLI → browser
```

### Checkpoint
- [ ] Justfile has recipes for every layer
- [ ] `just` (no args) lists all available commands
- [ ] `just ui-review` triggers the full stack
- [ ] Can explain why a justfile is valuable as the reusability layer
- [ ] Notes written in `module-4-notes.md`

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

**What you'll build:**

| Layer | File | Purpose |
|-------|------|---------|
| 1 | `.claude/skills/playwright-browser/SKILL.md` | Playwright CLI capability |
| 2 | `.claude/agents/playwright-browser-agent.md` | Simple browser agent |
| 2 | `.claude/agents/browser-qa-agent.md` | Specialized QA agent |
| 3 | `.claude/commands/ui-review.md` | Parallel story orchestrator |
| 3 | `.claude/commands/bowser/hop-automate.md` | Higher-order prompt runner |
| 3 | `ai_review/user_stories/hackernews.yaml` | Test story definitions |
| 4 | `justfile` | Terminal entry points |

**Notes you'll write:**
- `module-1-notes.md` through `module-4-notes.md`
- `LEARNINGS.md`

**Reference material** (already saved):
- `./reference/skills/` — Bowser's Playwright skill
- `./reference/agents/` — Bowser's agent definitions
- `./reference/commands/` — Bowser's command summaries
- `./reference/justfile` — Bowser's justfile
- `./reference/user-stories/` — Bowser's YAML test stories
