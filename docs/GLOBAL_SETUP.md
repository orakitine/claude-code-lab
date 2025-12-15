# Global Claude Code Setup

This documents Oleg's global Claude Code configuration that works across all projects.

## Directory Structure

```
~/.claude/
├── CLAUDE.md              # Skippy Protocol (personality + preferences)
├── settings.json          # Global settings (permissions, hooks, MCP servers)
├── skills/                # Universal skills available to all projects
│   ├── quality-gate/     # Swarmified quality checks (75% faster)
│   ├── project-context/  # Swarmified project analysis (29% faster)
│   ├── fork-terminal/    # Context handoff to new terminals
│   └── doc-vault/        # Auto-activating documentation cache
└── commands/              # Global slash commands
    └── (any universal commands)
```

## Skills Overview

### quality-gate
- **Purpose**: Comprehensive code quality verification
- **Features**: Linting, formatting, type checking, tests, build, security
- **Optimization**: 6 parallel agents (75% faster than sequential)
- **Supports**: JavaScript/TypeScript, Python
- **Location**: `~/.claude/skills/quality-gate/`

### project-context
- **Purpose**: Analyze project structure and generate context documentation
- **Features**: Framework detection, dependency analysis, structure mapping, entry points
- **Optimization**: 3 parallel agents (29% faster than sequential)
- **Supports**: JavaScript/TypeScript, Python
- **Location**: `~/.claude/skills/project-context/`

### fork-terminal
- **Purpose**: Spawn new terminal sessions with context handoff
- **Features**: Pass conversation history to new Claude instances
- **Use case**: Parallel work, specialized tasks
- **Location**: `~/.claude/skills/fork-terminal/`

### doc-vault
- **Purpose**: Auto-activating documentation cache
- **Features**: Fetches and caches documentation for libraries/frameworks
- **Use case**: Quick access to API docs during development
- **Location**: `~/.claude/skills/doc-vault/`

## Global CLAUDE.md

Contains the **Skippy Protocol** - Claude's personality and behavioral instructions:
- Sarcastic, helpful AI persona
- Technical communication style
- Code preferences and standards
- Workflow requirements

**Location**: `~/.claude/CLAUDE.md`

## Global settings.json

**Recommended Configuration**:
```json
{
  "dangerouslySkipPermissions": ["Read", "Grep", "Glob", "Bash"],
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [{
          "type": "command",
          "command": "afplay /System/Library/Sounds/Glass.aiff"
        }]
      }
    ]
  },
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

## MCP Servers

### memory
- **Purpose**: Knowledge graph persistence across sessions
- **Use case**: Remember preferences, context, reminders
- **Setup**: `npm install -g @modelcontextprotocol/server-memory`

### brave-search
- **Purpose**: Web search capabilities
- **Use case**: Look up current information, documentation
- **Setup**: `npm install -g @modelcontextprotocol/server-brave-search`
- **Requires**: `BRAVE_API_KEY` environment variable

## Per-Project Setup

For new projects, only create project-specific config if needed:

```
project/.claude/
├── CLAUDE.md              # Project-specific instructions only
└── settings.json          # Project overrides (optional, usually not needed)
```

**Global skills are automatically available** - no need to copy them!

## Setup on New Machine

1. **Install Claude Code**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

2. **Copy Skills**
   ```bash
   mkdir -p ~/.claude/skills
   cp -r /path/to/claude-code-lab/.claude/skills/* ~/.claude/skills/
   ```

3. **Copy Global CLAUDE.md**
   ```bash
   cp /path/to/your/CLAUDE.md ~/.claude/CLAUDE.md
   ```

4. **Create settings.json**
   ```bash
   # Use the template above or copy your existing one
   cp /path/to/settings.json ~/.claude/settings.json
   ```

5. **Install MCP Servers**
   ```bash
   npm install -g @modelcontextprotocol/server-memory
   npm install -g @modelcontextprotocol/server-brave-search
   ```

6. **Set Environment Variables**
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   export BRAVE_API_KEY="your_key_here"
   ```

## Philosophy

**Global > Project-Specific**
- Most skills are universally useful → Live in `~/.claude/skills/`
- Most settings are universal → Live in `~/.claude/settings.json`
- Only project-specific details → Live in `project/.claude/`

This approach:
- ✅ Avoids duplication
- ✅ Maintains consistency across projects
- ✅ Makes skills available everywhere
- ✅ Reduces per-project setup to minutes

## Related Resources

- [Configuration Guide](concepts/configuration.md) - Complete configuration reference
- [Skill Patterns](examples/skill-patterns.md) - How to build skills
- [MCP Servers Guide](concepts/mcp-servers.md) - MCP server integration
- [README.md](../README.md) - Learning path and examples

## Reference Implementation

This `claude-code-lab` repository serves as a reference implementation and learning resource. The skills here demonstrate:
- Swarm optimization patterns
- Context handoff techniques
- Tool integration
- Best practices following SKILL_CREATION_PRINCIPLES.md
