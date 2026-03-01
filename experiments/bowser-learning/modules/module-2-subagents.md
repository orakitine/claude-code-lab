# Module 2: Understanding Subagents (Layer 2 — Scale)

## Tiny Lecture: Why Do We Need Agents on Top of Skills?

A skill gives Claude a capability. But a skill runs in the **main conversation** — there's only one of it. What if you need to test 5 user stories simultaneously? You can't run 5 skills in one conversation.

**Agents solve this.** An agent is an autonomous unit that:
- Gets its own context window (isolated from the main conversation)
- Can be spawned multiple times in parallel
- Can be specialized for a specific workflow
- Reports results back to whoever spawned it

Think of the skill as a **tool in a toolbox**, and the agent as a **worker who knows how to use that tool**. You can hire 5 workers, each with their own toolbox, working on different tasks simultaneously.

> "The agent is where we start to specialize and scale, where the skill is just our raw capability." — Video

### Two Types of Agents

**1. Simple Agent (thin wrapper)**
Just activates a skill and passes through whatever you ask. It's a "general purpose worker" — flexible but not specialized. Bowser's `playwright-bowser-agent` is literally 2 lines of workflow.

**2. Specialized Agent (structured workflow)**
Has its own opinions about HOW to do work. Bowser's `bowser-qa-agent` doesn't just "use playwright" — it:
- Parses user stories into steps
- Creates screenshot directories
- Executes step-by-step with evidence capture
- Returns structured pass/fail reports

The specialization is the value. Anyone can say "use playwright." The QA agent knows the *process* of quality assurance.

---

## Adaptation Walkthrough: Bowser → Our Lab

### Agent Frontmatter Pattern

Agents in Claude Code use YAML frontmatter similar to skills, but with different fields:

```yaml
---
name: agent-name
description: What this agent does and when to use it. Keywords for discovery.
model: opus                    # Which model to use
color: green                   # Visual identifier in logs
skills:
  - playwright-browser         # Skills this agent has access to
---
```

**Key fields:**
- `model`: Which Claude model runs this agent. Opus for complex work, Haiku for simple tasks.
- `color`: Just for visual distinction when multiple agents run in parallel.
- `skills`: Declares which skills are activated. This is how the agent "inherits" capabilities.

### Decision 1: Simple Agent — Keep It Minimal

**Bowser's version:** 2-line workflow (activate skill, report back). Perfect.

**Our version:** Same philosophy. A thin wrapper shouldn't have opinions — that's the specialized agent's job. We just:
- Updated the skill reference from `playwright-bowser` to `playwright-browser` (our name)
- Kept the description keyword-rich for discoverability

**Why keep it thin?** Because you compose UP, not DOWN. The simple agent is a building block. If you need structure, use the QA agent. If you need flexibility, use the simple agent.

### Decision 2: QA Agent — Structured Output Format

**Bowser's version:** Detailed report format with emojis (✅ ❌), step tables, failure details, console error capture.

**Our version:** Same structure but adapted:
- Kept the pass/fail report format (it's excellent for review)
- Kept screenshot naming convention (`00_step-name.png`, `01_step-name.png`)
- Kept the "on failure: capture console, stop, mark remaining SKIPPED" pattern
- Removed emojis per our lab convention (plain PASS/FAIL text)
- Added VISION variable to match our skill's variable

### Decision 3: Session Isolation = Parallelism

This is the critical insight. Each agent derives its **own** named session:
- Agent 1 testing "front page" → `-s=front-page-qa-a1b2c3d4`
- Agent 2 testing "comments" → `-s=view-comments-qa-e5f6g7h8`
- Agent 3 testing "pagination" → `-s=pagination-qa-i9j0k1l2`

Three independent browsers, three independent sessions, three independent results. THIS is why the skill uses named sessions — it was designed for this from the start.

---

## Key Takeaways

1. **Simple agents = flexible building blocks** — thin wrappers that pass through requests
2. **Specialized agents = structured workflows** — opinionated about process, output format, evidence capture
3. **Agent frontmatter** declares model, color, and skill dependencies — making agents self-describing
4. **Session isolation** is what enables parallelism — each agent gets its own browser session
5. **Compose UP** — skill → simple agent → specialized agent. Each layer adds structure, not duplication
6. **The agent is the unit of parallelism** — you can't parallelize a skill, but you can spawn N agents

---

## Your Notes

(Add your own observations, questions, or ideas here as you review the agents)


