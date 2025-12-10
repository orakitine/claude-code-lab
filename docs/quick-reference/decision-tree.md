# Decision Tree - When to Use What

## Quick Decision Flow

```
START: I want to extend Claude Code
    ↓
    Q: What do I need?
    │
    ├─→ Shortcut for a prompt I type often
    │   → CREATE COMMAND (/mycommand.md)
    │
    ├─→ Workflow that auto-triggers on user phrases
    │   → CREATE SKILL (SKILL.md)
    │
    ├─→ New capability Claude doesn't have
    │   ├─→ Single function → CREATE TOOL (tool.py)
    │   └─→ Multiple related functions → CREATE MCP SERVER
    │
    ├─→ Automatic action on events
    │   → CREATE HOOK (in settings.json)
    │
    └─→ Persistent behavioral instructions
        → UPDATE CLAUDE.md
```

## Detailed Decision Trees

### Creating Extensions

#### "I type this prompt all the time..."

```
Q: Do I type this exact request frequently?
   ├─→ YES: Is it the same every time?
   │   ├─→ YES → CREATE COMMAND
   │   │   Example: /review, /test, /commit
   │   └─→ NO: Does it vary based on context?
   │       └─→ YES → CREATE SKILL
   │           Example: Auto-review when user mentions "review"
   └─→ NO: Is this a one-off?
       └─→ YES → Just type the prompt
```

#### "Claude can't do something I need..."

```
Q: Can Claude currently do this?
   ├─→ NO: How complex is it?
   │   ├─→ Single function
   │   │   └─→ CREATE CUSTOM TOOL
   │   │       Example: Database query, image processing
   │   │
   │   └─→ Multiple related functions
   │       └─→ CREATE MCP SERVER
   │           Example: Full API integration, database suite
   │
   └─→ YES: Check built-in tools
       Example: WebFetch, Bash, Read, Write, etc.
```

#### "I want to automate something..."

```
Q: When should this happen?
   ├─→ On specific events (after Write, before Bash, etc.)
   │   └─→ CREATE HOOK
   │       Example: Auto-format, auto-commit, notifications
   │
   ├─→ When user says certain phrases
   │   └─→ CREATE SKILL
   │       Example: "fork terminal" → spawn terminal
   │
   └─→ Always (every session)
       └─→ UPDATE CLAUDE.md
           Example: Coding standards, preferences
```

### Parallel Execution

#### "I need to do multiple things at once..."

```
Q: What kind of parallelism?
   ├─→ Run multiple Claude agents in parallel
   │   ├─→ Want results back?
   │   │   └─→ YES → USE BACKGROUND AGENTS
   │   │       Task(..., run_in_background=True)
   │   │       AgentOutputTool(agentId)
   │   │
   │   └─→ Don't need results / want separate terminals?
   │       └─→ USE FORK TERMINAL SKILL
   │           Example: Spawn Claude Code in new terminal
   │
   ├─→ Run other AI tools (Codex, Gemini)
   │   └─→ USE FORK TERMINAL SKILL
   │       Example: "fork terminal use codex to..."
   │
   └─→ Run long CLI commands
       ├─→ Need terminal window?
       │   └─→ USE FORK TERMINAL SKILL
       │
       └─→ Just background process?
           └─→ USE Bash(run_in_background=True)
```

### Research Tasks

#### "I need to research something..."

```
Q: How many sources?
   ├─→ Single URL
   │   ├─→ Quick summary → WebFetch directly
   │   └─→ Detailed analysis → Background agent + WebFetch
   │
   ├─→ Multiple URLs (2-5)
   │   └─→ CREATE BACKGROUND AGENTS (parallel)
   │       One agent per URL, all in single message
   │
   └─→ Many URLs (5+)
       └─→ CREATE SKILL
           Orchestrates background agents systematically
```

### Code Analysis

#### "I need to analyze code..."

```
Q: Scope of analysis?
   ├─→ Single file
   │   └─→ Read + analyze directly
   │
   ├─→ Few files (2-5)
   │   ├─→ Related files → Read sequentially
   │   └─→ Independent files → Read in parallel (one message)
   │
   ├─→ Many files (5-20)
   │   └─→ Background agents (one per file/category)
   │
   └─→ Entire codebase
       └─→ Task(subagent_type="Explore")
           Use Explore agent for efficient search
```

### Workflow Automation

#### "I have a multi-step process..."

```
Q: How is it triggered?
   ├─→ I manually start it
   │   ├─→ Type it often? → CREATE COMMAND
   │   └─→ Rarely? → Just type the prompt
   │
   ├─→ Auto-trigger on user phrases
   │   └─→ CREATE SKILL
   │       Example: "deploy to production" → deployment skill
   │
   └─→ Auto-trigger on events
       └─→ CREATE HOOK
           Example: After Edit → run linter
```

## Choosing Tool Types

### Custom Tool vs MCP Server

```
Custom Tool (.py in skills/)
    ↓
Q: Single focused function?
   ├─→ YES → Custom Tool
   │   Example: fork_terminal.py
   │
   └─→ NO: Multiple related functions?
       └─→ MCP Server
           Example: Database (query, schema, insert, update)
```

### Background Agent vs Fork Terminal

```
Need Parallelism
    ↓
Q: What are you running?
   ├─→ Claude Code / Codex / Gemini agents
   │   ├─→ Need results back?
   │   │   ├─→ YES → Background Agent (Task tool)
   │   │   └─→ NO → Fork Terminal
   │   │
   │   └─→ Want visible terminal?
   │       └─→ Fork Terminal
   │
   ├─→ Long-running CLI command
   │   ├─→ Need to see output?
   │   │   └─→ Fork Terminal
   │   │
   │   └─→ Just run in background?
   │       └─→ Bash(run_in_background=True)
   │
   └─→ Research/Analysis tasks
       └─→ Background Agents
           Multiple Task(..., run_in_background=True)
```

## Model Selection

### Choosing Agent Model

```
Spawning Background Agent
    ↓
Q: Task complexity?
   ├─→ Simple (fetch URL, run command, read file)
   │   → model="haiku" (fast & cheap)
   │
   ├─→ Medium (code analysis, review, testing)
   │   → model="sonnet" (balanced - default)
   │
   └─→ Complex (architecture design, debugging)
       → model="opus" (most capable)
```

## Configuration Scope

### Global vs Project

```
Adding Configuration
    ↓
Q: Should this apply to...
   ├─→ All my projects?
   │   └─→ Global (~/.claude/)
   │       Example: Personal coding style, common commands
   │
   ├─→ Just this project?
   │   └─→ Project (.claude/)
   │       Example: Project-specific workflows, deploy commands
   │
   └─→ Both?
       └─→ Global for defaults, Project to override
           Example: Base in global, customizations in project
```

## Permission Settings

### Security Configuration

```
Setting Permissions
    ↓
Q: Trust level?
   ├─→ Maximum security (default)
   │   → dangerouslySkipPermissions: []
   │   Ask for everything
   │
   ├─→ Trust read operations
   │   → dangerouslySkipPermissions: ["Read", "Grep", "Glob"]
   │   Good for daily work
   │
   ├─→ Trust specific operations
   │   → dangerouslySkipPermissions: ["Read", "Bash"]
   │   Customize based on workflow
   │
   └─→ Trust everything (dangerous!)
       → dangerouslySkipPermissions: ["*"]
       Only for completely isolated environments
```

## Real-World Scenarios

### Scenario 1: "I want Claude to auto-format my code"

```
Solution: CREATE HOOK
    ↓
{
  "hooks": {
    "after-tool-call": "if [[ $TOOL_NAME == 'Edit' || $TOOL_NAME == 'Write' ]]; then prettier --write $FILE_PATH; fi"
  }
}
```

### Scenario 2: "I want to research 5 blog posts about React hooks"

```
Solution: BACKGROUND AGENTS
    ↓
1. Spawn 5 agents (one message, all with run_in_background=True)
2. Each uses WebFetch on one URL
3. Continue other work
4. Retrieve all with AgentOutputTool
5. Synthesize findings
```

### Scenario 3: "I always ask Claude to review my PRs the same way"

```
Solution: CREATE COMMAND
    ↓
.claude/commands/review-pr.md:
Review the current PR changes.
Check for: logic, security, tests, performance.
Format as markdown with severity levels.
```

### Scenario 4: "I want Claude to automatically invoke my linter"

```
Solution: TWO OPTIONS

Option A: HOOK (runs every time)
{
  "hooks": {
    "before-tool-call": "if [[ $TOOL_NAME == 'Write' ]]; then eslint $FILE_PATH || exit 1; fi"
  }
}

Option B: SKILL (runs on request)
.claude/skills/lint-check/SKILL.md
- Triggers when user says "check linting"
- Runs linter on specified files
- Reports issues
```

### Scenario 5: "I need to query my database from Claude"

```
Solution: MCP SERVER
    ↓
{
  "mcpServers": {
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}

Then: Claude can use query_database(sql) tool
```

### Scenario 6: "I want to spawn 3 different AI agents to try different approaches"

```
Solution: FORK TERMINAL (if want separate terminals + other AI tools)
    ↓
"Fork terminal use claude code to try approach A,
 fork terminal use codex to try approach B,
 fork terminal use gemini to try approach C"

OR

Solution: BACKGROUND AGENTS (if all Claude Code + want results)
    ↓
Task(...approach A..., run_in_background=True)
Task(...approach B..., run_in_background=True)
Task(...approach C..., run_in_background=True)
```

## Common Mistakes

### ❌ Creating a skill when you need a command
```
Problem: "I want /deploy to run my deployment"
Wrong: Creating a skill that triggers on "deploy"
Right: Creating .claude/commands/deploy.md
```

### ❌ Using custom tool when built-in exists
```
Problem: "I need to fetch a URL"
Wrong: Writing custom_web_fetch.py tool
Right: Using built-in WebFetch tool
```

### ❌ Spawning agents sequentially
```
Problem: Want parallel research
Wrong:
  Message 1: Task(..., run_in_background=True)
  Message 2: Task(..., run_in_background=True)
  Message 3: Task(..., run_in_background=True)

Right:
  Message 1:
    Task(..., run_in_background=True)
    Task(..., run_in_background=True)
    Task(..., run_in_background=True)
```

### ❌ Blocking immediately after spawning
```
Problem: Want to work while agent runs
Wrong:
  Task(..., run_in_background=True)
  AgentOutputTool(block=True)  # Blocks immediately!

Right:
  Task(..., run_in_background=True)
  # Do other work here
  Read(...)
  Edit(...)
  # NOW retrieve
  AgentOutputTool(block=True)
```

## Summary Matrix

| Need | Solution | File Location |
|------|----------|---------------|
| Prompt shortcut | Command | `.claude/commands/cmd.md` |
| Auto-workflow | Skill | `.claude/skills/name/SKILL.md` |
| New capability | Tool | `.claude/skills/name/tools/tool.py` |
| External service | MCP Server | Config in `settings.json` |
| Event automation | Hook | Config in `settings.json` |
| Behavioral rules | Instructions | `.claude/CLAUDE.md` |
| Parallel work (results) | Background Agent | `Task(..., run_in_background=True)` |
| Parallel terminals | Fork Terminal | Use fork-terminal skill |
| Long CLI command | Bash Background | `Bash(..., run_in_background=True)` |

## Next Steps

After deciding what to build:
1. Read the relevant [concept guide](../README.md#quick-navigation)
2. Check [examples](../examples/) for patterns
3. Start with simple version
4. Test thoroughly
5. Iterate and improve
