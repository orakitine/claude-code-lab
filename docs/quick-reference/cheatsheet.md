# Claude Code Quick Reference

## Core Concepts

| Concept | What | When | Example |
|---------|------|------|---------|
| **Skill** | Auto-invoked workflow | User says trigger phrase | "fork terminal" → runs skill |
| **Command** | Prompt shortcut | User types `/cmd` | `/review` → expands to prompt |
| **Tool** | Code capability | Claude calls during work | `fork_terminal(cmd)` |
| **Hook** | Event automation | Event occurs | After Write → format file |
| **MCP** | External tools | Claude calls during work | Query database |

## File Structure

```
project/
├── .claude/
│   ├── settings.json          # Config
│   ├── CLAUDE.md              # Instructions
│   ├── commands/              # /slash commands
│   │   └── mycommand.md
│   └── skills/                # Auto-invoked workflows
│       └── my-skill/
│           ├── SKILL.md       # Workflow definition
│           ├── cookbook/      # Scenario-specific
│           ├── prompts/       # Templates
│           └── tools/         # Custom Python
│               └── tool.py
```

## Skill Template

```markdown
---
name: Skill Name
description: Use when user says "trigger phrase"
---

# Purpose
What this does

## Variables (optional)
SETTING: value

## Instructions
How to do it

## Workflow
1. Step one
2. Step two
```

## Command Template

```markdown
Do something specific when user types /command.

Steps:
1. First action
2. Second action

Output: How to format results
```

## Tool Template

```python
#!/usr/bin/env -S uv run
"""Tool description."""

def tool_function(param: str) -> str:
    """What this tool does."""
    return result
```

## Settings Template

```json
{
  "dangerouslySkipPermissions": ["Read", "Grep"],
  "hooks": {
    "after-tool-call": "command here"
  },
  "mcpServers": {
    "server-name": {
      "command": "executable",
      "args": ["arg1"],
      "env": {"KEY": "${VALUE}"}
    }
  }
}
```

## Task Tool - Spawn Agents

### Background Agent (Async)
```python
agent = Task(
    subagent_type="general-purpose",
    description="Short description",
    prompt="Detailed instructions",
    run_in_background=True,
    model="haiku"  # or "sonnet", "opus"
)
# Returns: {"agentId": "agent_123"}
```

### Retrieve Results
```python
result = AgentOutputTool(
    agentId="agent_123",
    block=True,  # Wait for completion
    wait_up_to=150  # Seconds
)
```

### Agent Types
- `general-purpose` - Most common
- `Explore` - Fast codebase search
- `Plan` - Design implementation
- `claude-code-guide` - Documentation lookup

## Common Patterns

### Parallel Web Research
```python
# Spawn 3 agents in ONE message
Task(..., run_in_background=True)  # Research 1
Task(..., run_in_background=True)  # Research 2
Task(..., run_in_background=True)  # Research 3

# Continue work
Read("file.js")

# Retrieve all
result1 = AgentOutputTool(agentId="agent_1", block=True)
result2 = AgentOutputTool(agentId="agent_2", block=True)
result3 = AgentOutputTool(agentId="agent_3", block=True)
```

### Multi-Variant Skill (Cookbook Pattern)
```markdown
# Workflow

IF user mentions X: Read cookbook/x.md
IF user mentions Y: Read cookbook/y.md
IF user mentions Z: Read cookbook/z.md

Follow cookbook instructions
```

### Context Handoff
```markdown
# In skill workflow

IF user requests summary:
  1. Read prompts/summary_template.md
  2. Fill with conversation history
  3. Pass to spawned agent
```

## Hook Examples

```json
{
  "hooks": {
    // Auto-format after edit
    "after-tool-call": "if [[ $TOOL_NAME == 'Edit' ]]; then prettier --write $FILE_PATH; fi",

    // Notify on error
    "on-error": "osascript -e 'display notification \"$ERROR_MESSAGE\"'",

    // Log everything
    "user-prompt-submit": "echo \"[$(date)] $PROMPT\" >> ~/claude.log"
  }
}
```

## MCP Server Examples

```json
{
  "mcpServers": {
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {"DATABASE_URL": "${DATABASE_URL}"}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "${GITHUB_TOKEN}"}
    }
  }
}
```

## Built-in Tools

### File Operations
- `Read(file_path)` - Read file
- `Write(file_path, content)` - Create file
- `Edit(file_path, old_string, new_string)` - Modify file
- `Glob(pattern)` - Find files
- `Grep(pattern, output_mode="files_with_matches")` - Search content

### Web Access
- `WebFetch(url, prompt)` - Fetch and process URL
- `WebSearch(query)` - Search the web

### Execution
- `Bash(command)` - Run shell command
- `Bash(command, run_in_background=True)` - Background shell
- `Task(...)` - Spawn sub-agent

### Code Analysis
- `mcp__ide__getDiagnostics(uri=...)` - Get VS Code errors
- `mcp__ide__executeCode(code)` - Run Jupyter code

## CLAUDE.md Tips

```markdown
# Project Instructions

## Architecture
- Tech stack overview
- Key patterns used

## Important Files
- Where things are located
- What each directory contains

## Workflow
- Development process
- Testing approach
- Deployment steps

## Standards
- Code style
- Naming conventions
- Comment requirements
```

## Decision Trees

### "Should I create a..."

**Skill?**
→ User will trigger with natural language?
→ Needs to auto-invoke invisibly?
→ Complex multi-step workflow?
→ YES: Create skill

**Command?**
→ You type the same prompt often?
→ Need quick shortcut?
→ User-initiated action?
→ YES: Create command

**Tool?**
→ Need NEW capability?
→ Will execute code?
→ Returns data to Claude?
→ YES: Create tool

**Hook?**
→ Should happen automatically on events?
→ Want to validate/notify/log?
→ Modify standard behavior?
→ YES: Create hook

**MCP Server?**
→ Multiple related tools?
→ External service integration?
→ Need persistent state?
→ Want cross-tool compatibility?
→ YES: Create MCP server

## Common Commands

```bash
# Initialize Claude in project
claude init

# Run Claude
claude

# With specific model
claude --model opus

# Skip permissions (dangerous!)
claude --dangerously-skip-permissions

# View help
claude --help
```

## Debugging

```bash
# Check settings
cat ~/.claude/settings.json
cat .claude/settings.json

# View instructions
cat ~/.claude/CLAUDE.md
cat .claude/CLAUDE.md

# List commands
ls ~/.claude/commands/
ls .claude/commands/

# List skills
ls ~/.claude/skills/
ls .claude/skills/

# Test hook manually
TOOL_NAME="Write" bash -c "your-hook-command"

# Test MCP server
uvx mcp-server-postgres
```

## Environment Setup

```bash
# Add to ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_..."
export DATABASE_URL="postgresql://..."
export API_KEY="sk_..."

# Reload
source ~/.bashrc
```

## Best Practices

✅ **DO:**
- Use skills for auto-invoked workflows
- Use commands for repeated prompts
- Use background agents for parallel work
- Keep tools focused and simple
- Document in CLAUDE.md

❌ **DON'T:**
- Hardcode secrets in settings.json
- Create overly complex skills
- Block immediately after spawning background agents
- Duplicate built-in capabilities
- Skip testing hooks before deploying

## Quick Wins

1. **Personal Commands**: Create `/commit`, `/review`, `/test`
2. **Global CLAUDE.md**: Add your coding standards
3. **Auto-format Hook**: Format files after edit
4. **Background Research**: Use for web fetching
5. **MCP GitHub**: Integrate with your repos

## Resources

- [Full Documentation](../README.md)
- [Skills Guide](../concepts/skills.md)
- [Commands Guide](../concepts/commands.md)
- [Tools Guide](../concepts/tools.md)
- [Hooks Guide](../concepts/hooks.md)
- [MCP Guide](../concepts/mcp-servers.md)
- [Background Agents](../concepts/background-agents.md)
