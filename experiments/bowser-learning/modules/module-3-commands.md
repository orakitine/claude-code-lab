# Module 3: Understanding Commands (Layer 3 — Orchestration)

## Tiny Lecture: Commands = The Team Manager

If a skill is a tool, and an agent is a worker, then a **command is the team manager**. It doesn't do the work itself — it:

1. **Discovers** what work needs to be done (finds YAML story files)
2. **Distributes** work to agents (spawns parallel browser-qa-agents)
3. **Collects** results (gathers pass/fail reports)
4. **Reports** the summary (aggregate table of all results)

This is the **orchestration** pattern. The command knows the WHAT and the WHO, but delegates the HOW to agents.

> "The prompt controls the sub-agents. The sub-agents use the skills." — Video

### The Meta-Prompting Pattern

Here's the mind-bending part. The `/ui-review` command doesn't just tell agents "go test this." It teaches the **orchestrator** (the Claude instance running the command) *how to prompt* the sub-agents.

It's a prompt that contains instructions for writing prompts. Meta-prompting.

Why? Because the orchestrator needs to:
- Include the specific story details in each agent's prompt
- Tell each agent where to save screenshots
- Configure headed/headless mode
- Pass through vision settings

Without meta-prompting, you'd get generic, badly-configured agents.

### The Higher-Order Prompt (HOP) Pattern

The second command (`hop-automate`) introduces another powerful idea: **a prompt that takes another prompt as input**.

Think of it like a higher-order function in programming:
```javascript
// Regular function
function buyOnAmazon(items) { ... }

// Higher-order function
function automate(workflow) {
  setup();
  workflow();  // ← runs whatever you pass in
  cleanup();
  report();
}

automate(buyOnAmazon);  // consistent wrapper, custom workflow
```

The HOP wraps any workflow in consistent setup/teardown/reporting. You write the WHAT (buy stuff on Amazon, summarize a blog), and the HOP handles the HOW (which skill, headed/headless, where to save results).

---

## Adaptation Walkthrough: Bowser → Our Lab

### Decision 1: User Stories in YAML

**Bowser's format:**
```yaml
stories:
  - name: "Front page loads with posts"
    url: "https://news.ycombinator.com/"
    workflow: |
      Navigate to the URL
      Verify at least 10 posts are visible
```

**Our version:** Same format — it's clean, human-readable, and easy to add new stories. Each story has:
- `name`: identifier for reports
- `url`: where to test
- `workflow`: natural language steps (the QA agent parses these)

No adaptation needed here. The format is already excellent.

### Decision 2: UI Review Command — 4-Phase Orchestration

**Bowser's version:** Uses `TeamCreate` and `TaskCreate` (experimental agent team features). These are cutting-edge Claude Code features that may not be stable.

**Our version:** Uses the standard `Agent` tool with parallel spawning instead. This is:
- More widely available (doesn't require experimental flags)
- Simpler to understand (just "spawn N agents in parallel")
- Still gets the job done (parallel execution, result collection)

The 4 phases stay the same: Discover → Spawn → Collect → Report.

### Decision 3: HOP Command — Flexible Skill Routing

**Bowser's version:** Supports both `playwright-bowser` AND `claude-bowser` skills, with keyword detection for mode/skill/vision.

**Our version:** Simplified to just `playwright-browser` since we're not building the Chrome MCP skill. But kept the keyword detection pattern — it's clever:
- "headed" in args → sets MODE=headed
- "headless" in args → sets MODE=headless
- "vision" in args → sets VISION=true
- Everything else → becomes the PROMPT

This means you can write natural commands like:
```
/bowser:hop-automate blog-summarizer https://example.com headed vision
```
And the HOP parses it into structured config.

### Decision 4: Command File Structure

Commands in Claude Code are just markdown files in `.claude/commands/`. The filename becomes the slash command:
- `.claude/commands/ui-review.md` → `/ui-review`
- `.claude/commands/bowser/hop-automate.md` → `/bowser:hop-automate`

Nested directories create namespaced commands (using `:` separator). We put browser-specific workflows under `bowser/` to keep them organized.

---

## Key Takeaways

1. **Commands orchestrate, agents execute** — the command is the team manager
2. **Meta-prompting** — teaching the orchestrator how to prompt sub-agents is critical for quality results
3. **Higher-order prompts** — wrap variable workflows in consistent setup/teardown
4. **YAML user stories** — human-readable test definitions that agents parse into steps
5. **4-phase pattern** — Discover → Spawn → Collect → Report is reusable for any fan-out workflow
6. **Keyword detection** — natural language arguments parsed into structured config
7. **Namespace with directories** — `commands/bowser/` creates `/bowser:*` commands

---

## Your Notes

(Add your own observations, questions, or ideas here as you review the commands)


