# Claude Code Reference Documentation

> Your personal knowledge base for mastering Claude Code

## Overview

This documentation covers the key concepts, patterns, and techniques for extending and customizing Claude Code.

## Quick Navigation

### 📚 Core Concepts
- [Skills](concepts/skills.md) - Auto-invoked workflows and patterns
- [Commands](concepts/commands.md) - User-invoked prompt shortcuts
- [Tools](concepts/tools.md) - Custom capabilities and functions
- [Hooks](concepts/hooks.md) - Event-driven automation
- [MCP Servers](concepts/mcp-servers.md) - External tool providers
- [Background Agents](concepts/background-agents.md) - Parallel execution patterns
- [Configuration](concepts/configuration.md) - Settings, CLAUDE.md, and setup

### 💡 Examples
- [Skill Patterns](examples/skill-patterns.md) - Common skill architectures
- [Command Recipes](examples/command-recipes.md) - Useful command templates
- [Tool Examples](examples/tool-examples.md) - Custom tool implementations
- [Workflows](examples/workflows.md) - Multi-concept orchestration

### ⚡ Quick Reference
- [Cheat Sheet](quick-reference/cheatsheet.md) - Quick lookup guide
- [Decision Tree](quick-reference/decision-tree.md) - When to use what

## The Mental Model

```
┌─────────────────────────────────────────────────┐
│  USER INTERACTION                               │
│  Commands (/foo) + Natural Language             │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│  CONFIGURATION                                  │
│  CLAUDE.md + settings.json + Hooks              │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│  ORCHESTRATION                                  │
│  Skills + Task Tool + Background Agents         │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│  EXECUTION                                      │
│  Built-in Tools + Custom Tools + MCP Tools      │
└─────────────────────────────────────────────────┘
```

## Learning Path

### Beginner
1. Start with [Skills](concepts/skills.md) - Understand workflow patterns
2. Read [Commands](concepts/commands.md) - Create prompt shortcuts
3. Review [Tools](concepts/tools.md) - Add custom capabilities

### Intermediate
4. Explore [Background Agents](concepts/background-agents.md) - Parallel work
5. Study [Hooks](concepts/hooks.md) - Automate workflows
6. Configure [Settings](concepts/configuration.md) - Customize behavior

### Advanced
7. Implement [MCP Servers](concepts/mcp-servers.md) - External integrations
8. Master [Workflows](examples/workflows.md) - Complex orchestration
9. Build integrated systems using all concepts

## Key Distinctions

| Concept | Purpose | Invoked By | Contains |
|---------|---------|------------|----------|
| **Skills** | Workflow patterns | Claude (auto) | Instructions |
| **Commands** | Prompt shortcuts | User (manual) | Text templates |
| **Tools** | New capabilities | Claude (auto) | Code/functions |
| **Hooks** | Event automation | Events | Shell commands |
| **MCP** | External tools | Claude (auto) | Server config |

## Getting Started

Pick a concept that interests you and dive in! Each doc includes:
- Detailed explanations
- Real-world examples
- Best practices
- Common patterns
- Gotchas and tips

## Your Current Setup

This project includes:
- ✅ Fork Terminal Skill (hybrid skill + tool)
- ✅ Slash commands (/prime, /load_ai_docs, etc.)
- ✅ Custom tool (fork_terminal.py)
- ✅ Global Skippy protocol (CLAUDE.md)

Ready to expand your toolkit!
