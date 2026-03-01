# Module 4: Understanding Justfiles (Layer 4 — Reusability)

## Tiny Lecture: Why a Justfile on Top of Everything?

You've now got skills, agents, and commands. But here's the problem: **how do you remember all the ways to run things?**

- `claude "/playwright-browser go to example.com and screenshot it"`
- `claude "Use @browser-qa-agent: test Hacker News front page"`
- `claude "/ui-review headed"`
- `claude "/bowser:hop-automate blog-summarizer https://example.com headed"`

That's a lot to memorize. And if you work with a team (or multiple agents), they need to discover what's available too.

A **justfile** solves this by being the **single entry point** for all your agentic workflows. It's a task runner (like Makefile, but sane) that wraps everything into simple, discoverable commands:

```bash
just                    # lists everything available
just test-skill         # test Layer 1 directly
just test-qa            # test Layer 2
just ui-review          # run Layer 3
just summarize-blog     # Layer 4 convenience recipe
```

> "After you have all these different ways to execute with your agent, you're going to want a repeat single place to call all these tools." — Video

### Why `just` Instead of Make, npm scripts, or shell aliases?

- **`just`** is a task runner, not a build system. No implicit targets, no file dependencies, no magic.
- Variables with defaults that can be overridden: `just ui-review headed="true"`
- Clean syntax, good error messages, cross-platform
- No `package.json` pollution — keeps your task runner separate from your dependencies

---

## Adaptation Walkthrough: Bowser → Our Lab

### Decision 1: Layer-by-Layer Organization

**Bowser's justfile:** Organized by layer with clear section comments. Excellent pattern.

**Our version:** Same structure. Each section maps to a layer:
```
# Layer 1: Skill (Capability)     — test the raw CLI skill
# Layer 2: Subagent (Scale)       — test agents in isolation
# Layer 3: Command (Orchestration) — run orchestration commands
# Layer 4: Just (Reusability)     — convenience recipes
```

This makes the justfile self-documenting. You can see the architecture just by reading `just --list`.

### Decision 2: Default Prompts as Variables

**Bowser's approach:** Defines default prompts at the top of the justfile:
```
default_prompt := "Get the current date, go to simonwillison.net..."
```

**Our approach:** Same pattern. Default prompts let you test recipes without typing anything:
```bash
just test-skill              # uses default prompt
just test-skill prompt="..."  # override with your own
```

This is crucial for **repeatability** — anyone can run `just test-skill` and get a meaningful test without having to think about what to type.

### Decision 3: Removed Chrome/MCP Recipes

**Bowser:** Has recipes for `--chrome` flag (Chrome MCP browser). Requires logged-in Chrome session.

**Our version:** Removed Chrome-specific recipes since we're focused on Playwright CLI (headless, parallelizable). Kept the Playwright path clean and simple.

### Decision 4: The `--dangerously-skip-permissions` Flag

Every recipe in Bowser uses this flag. It tells Claude Code to skip all permission prompts. This is necessary for non-interactive automation (you can't click "allow" when running from a justfile).

**Our version:** Uses the same flag. Without it, the justfile recipes would hang waiting for permission prompts that nobody's there to click.

### Decision 5: Model Selection

**Bowser:** Hard-codes `--model opus` everywhere.

**Our version:** Uses a `model` variable with `opus` as default, so you can override:
```bash
just test-skill model="sonnet"   # cheaper for testing
just ui-review model="opus"       # full power for real runs
```

---

## Key Takeaways

1. **Justfile = single entry point** — discoverable commands for everything in your agentic stack
2. **Layer-by-layer organization** — the justfile mirrors the 4-layer architecture
3. **Default variables** — make recipes runnable without arguments for quick testing
4. **Override via args** — `just recipe var="value"` for customization
5. **`--dangerously-skip-permissions`** — required for non-interactive automation
6. **The full stack is now**: `just` → `claude /command` → agents → skill → CLI → browser

---

## Your Notes

(Add your own observations, questions, or ideas here as you review the justfile)


