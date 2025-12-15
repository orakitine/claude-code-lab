# Claude Code Lab 🧪

> A hands-on learning laboratory for mastering [Claude Code](https://docs.anthropic.com/en/docs/claude-code) extensibility

This repository is a **practical learning workspace** where theory meets practice. Read concepts, implement features, experiment with patterns, and cement your knowledge through hands-on work.

## What's Inside

```
claude-code-lab/
├── docs/                           # 📚 Complete reference documentation
│   ├── concepts/                   # Deep-dive guides (7 topics)
│   ├── examples/                   # Practical patterns
│   └── quick-reference/            # Cheat sheets & decision trees
├── experiments/                    # 🧪 Your playground for learning
│   ├── commands/                   # Slash commands you create
│   ├── skills/                     # Skills you build
│   ├── tools/                      # Custom tools you write
│   └── notes/                      # Your learning notes
├── .claude/                        # Working Claude Code setup
│   ├── skills/fork-terminal/       # Example skill (fully functional)
│   └── commands/                   # Utility commands
└── README.md                       # This file (tracks your progress!)
```

## Learning Path

Track your progress through Claude Code mastery:

### Phase 1: Foundation ✅

- [x] Understand Skills vs Commands vs Tools
- [x] Read [Skills Concept Guide](docs/concepts/skills.md)
- [x] Read [Commands Concept Guide](docs/concepts/commands.md)
- [x] Read [Tools Concept Guide](docs/concepts/tools.md)
- [x] Study [Decision Tree](docs/quick-reference/decision-tree.md)

### Phase 2: First Experiments 🎯

- [x] Create your first slash command
- [x] Build a simple workflow skill
- [x] Write a custom tool
- [x] Test the fork-terminal example skill

### Phase 3: Power Features ⚡

- [x] Read [Background Agents Guide](docs/concepts/background-agents.md)
- [x] Experiment with parallel task execution
- [x] Read [Hooks Guide](docs/concepts/hooks.md)
- [x] Set up an automation hook
- [x] Read [MCP Servers Guide](docs/concepts/mcp-servers.md)
- [x] Install and test an MCP server

### Phase 4: Advanced Patterns 🚀

- [x] Study [Skill Patterns](docs/examples/skill-patterns.md)
- [x] Build a multi-variant skill (cookbook pattern)
- [x] Create a tool-enhanced skill
- [x] Implement background agent orchestration
- [ ] Set up context handoff pattern

### Phase 5: Mastery 🏆

- [x] Read [Configuration Guide](docs/concepts/configuration.md)
- [x] Set up global CLAUDE.md with your preferences
- [x] Create a complete project template
- [x] Build an integrated workflow (skill + tool + hook)
- [ ] Contribute patterns back to community

## Quick Start

### 1. Explore the Documentation

```bash
# Start with the overview
open docs/README.md

# Or jump to a specific concept
open docs/concepts/skills.md
```

### 2. Try the Example Skill

This repo includes a fully functional **fork-terminal** skill:

```
# Try it out (if you have Claude Code, Codex, or Gemini installed)
"fork terminal use claude code to analyze this README"
```

Study its structure in `.claude/skills/fork-terminal/` to see a real-world implementation.

### 3. Create Your First Command

```bash
# Create a simple command
echo "Review my code changes and provide feedback." > .claude/commands/review.md

# Use it
# Type: /review
```

### 4. Start Experimenting

Use the `experiments/` directory for your learning projects.

## Experiments

Document your learning experiments here:

### Completed Experiments ✅

- [x] Built comprehensive documentation system
- [x] **Doc Vault Skill** - Auto-activating documentation cache with fresh API docs
  - WebFetch integration for clean content extraction
  - Auto-loads on first technical trigger per session
  - Auto-consults cached docs when relevant
  - Self-documenting with README.md index
  - Context-optimized (only loads when needed)
  - See: `.claude/skills/doc-vault/`

### In Progress 🔄

- [ ] _Nothing currently - ready for next experiment!_

### Planned 📋

- [ ] Create personal slash commands collection
- [ ] Build a code review skill
- [ ] Set up auto-format hooks
- [ ] Install GitHub MCP server
- [ ] Create custom database tool
- [ ] Build multi-agent orchestration

## Key Concepts Quick Reference

| Concept     | What                  | When                     | File Location                       |
| ----------- | --------------------- | ------------------------ | ----------------------------------- |
| **Skill**   | Auto-invoked workflow | User says trigger phrase | `.claude/skills/name/SKILL.md`      |
| **Command** | Prompt shortcut       | User types `/cmd`        | `.claude/commands/cmd.md`           |
| **Tool**    | Custom capability     | Claude calls it          | `.claude/skills/name/tools/tool.py` |
| **Hook**    | Event automation      | On events                | `settings.json`                     |
| **MCP**     | External tools        | Claude calls them        | `settings.json`                     |

See [Cheat Sheet](docs/quick-reference/cheatsheet.md) for more!

## Documentation Guide

### 📚 Concept Guides

Start here for deep understanding:

- [Skills](docs/concepts/skills.md) - Auto-invoked workflows
- [Commands](docs/concepts/commands.md) - User shortcuts
- [Tools](docs/concepts/tools.md) - Custom capabilities
- [Hooks](docs/concepts/hooks.md) - Event automation
- [MCP Servers](docs/concepts/mcp-servers.md) - External integrations
- [Background Agents](docs/concepts/background-agents.md) - Parallel execution
- [Configuration](docs/concepts/configuration.md) - Settings & setup

### 💡 Practical Examples

- [Skill Patterns](docs/examples/skill-patterns.md) - 10 common patterns to copy

### ⚡ Quick Reference

- [Cheat Sheet](docs/quick-reference/cheatsheet.md) - Fast syntax lookup
- [Decision Tree](docs/quick-reference/decision-tree.md) - "What should I build?"

## Example: Fork Terminal Skill

This repo includes a complete, working skill as a learning reference:

**Location:** `.claude/skills/fork-terminal/`

**What it does:** Spawns new terminal windows to run Claude Code, Codex CLI, Gemini CLI, or raw CLI commands in parallel.

**Key learnings:**

- ✅ Tool-enhanced skill (includes custom Python tool)
- ✅ Multi-variant pattern (cookbook for different scenarios)
- ✅ Context handoff (can pass conversation history)
- ✅ Cross-platform support (macOS + Windows)

**Try it:**

```
"fork terminal use claude code to analyze docs/concepts/skills.md"
```

Study the source code to see how it all works!

## Learning Resources

### Official Documentation

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Model Context Protocol](https://spec.modelcontextprotocol.io)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

### This Repository

- Complete concept guides in `docs/concepts/`
- Practical examples in `docs/examples/`
- Quick reference materials in `docs/quick-reference/`

### Community

- [IndyDevDan YouTube](https://www.youtube.com/@indydevdan) - Agentic coding tutorials
- [Fork Terminal Skill Video](https://youtu.be/X2ciJedw2vU) - Building skills from scratch

## Tips for Learning

1. **Read, then do** - Don't just read docs, implement what you learn
2. **Start simple** - Begin with commands, move to skills, then advanced features
3. **Copy patterns** - Use examples as templates, customize for your needs
4. **Experiment freely** - The `experiments/` directory is your sandbox
5. **Track progress** - Check off items in this README as you learn
6. **Document learnings** - Add notes in `experiments/notes/`

## What to Build

Not sure where to start? Try these:

### Beginner Projects

- [ ] `/commit` - Smart git commit command
- [ ] `/test` - Run tests and fix failures
- [ ] Simple code formatter skill

### Intermediate Projects

- [ ] Multi-pass code review skill
- [ ] Database query tool with MCP
- [ ] Auto-format hook

### Advanced Projects

- [ ] Multi-agent research orchestration
- [ ] Context-aware deployment skill
- [ ] Custom MCP server for your APIs

## Progress Notes

### Session Log

**2025-12-10**: Initial setup

- Created comprehensive documentation system
- Set up repository structure
- Ready to start hands-on learning!

**2025-12-11**: Phase 3 - Doc Vault Skill

- Built auto-activating documentation cache (doc-vault)
- Integrated WebFetch for clean content extraction
- Learned auto-activation pattern (loads on first trigger)
- Implemented context optimization (only loads when needed)
- Created Python tool for README.md index management
- Self-documenting system with frontmatter metadata
- Tested with real TanStack Query docs
- Iterated from complex registry to simple README index
- Completed Phase 3 & advanced Phase 4 patterns!

---

## Next Steps

Ready to dive in? Start here:

1. **Foundations** → Read [docs/concepts/skills.md](docs/concepts/skills.md)
2. **Quick Win** → Create your first slash command
3. **Deep Dive** → Study the fork-terminal example skill
4. **Experiment** → Build something in `experiments/`

Happy learning! 🚀
