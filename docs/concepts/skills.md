# Skills - Auto-Invoked Workflows

## What Are Skills?

Skills are **modular, context-aware capabilities** that Claude automatically invokes when user requests match the skill's description pattern.

## Key Characteristics

- **Auto-invoked**: Claude decides when to use them (invisible to user)
- **Pattern-matching**: Triggered by user's natural language
- **Workflow-focused**: Define HOW to do something, not WHAT you can do
- **Composable**: Can use tools, spawn agents, read prompts, etc.

## Anatomy of a Skill

```
.claude/skills/my-skill/
├── SKILL.md                  # Required: Skill definition
├── cookbook/                 # Optional: Scenario-specific instructions
│   ├── option-a.md
│   └── option-b.md
├── prompts/                  # Optional: Reusable templates
│   └── template.md
└── tools/                    # Optional: Custom Python tools
    └── custom_tool.py
```

## SKILL.md Structure

```markdown
---
name: My Skill Name
description: Use when user requests X, Y, or Z. Trigger phrases go here.
---

# Purpose

What this skill accomplishes

## Variables (Optional)

ENABLE_FEATURE_A: true
DEFAULT_MODE: fast

## Instructions

Step-by-step workflow Claude should follow

## Workflow

1. Detect user intent
2. Read relevant files
3. Execute logic
4. Return results

## Examples

- "User phrase that triggers this"
- "Another trigger phrase"
```

## Types of Skills

### 1. Pure Workflow Skills
No custom tools - just orchestration of existing capabilities

**Example: Multi-Pass Code Review**
```markdown
---
name: thorough-code-review
description: Use when user requests code review, PR review, or code audit
---

# Workflow

1. First pass: Read files, identify issues
2. Second pass: Check test coverage
3. Third pass: Security analysis
4. Synthesize into markdown report
```

Uses only: Read, Grep, Bash (git commands)

### 2. Tool-Enhanced Skills
Include custom Python tools for new capabilities

**Example: Fork Terminal**
```markdown
---
name: fork-terminal
description: Fork terminal sessions when user says 'fork terminal' or 'new terminal'
---

# Workflow

1. Parse user request
2. Read appropriate cookbook
3. Execute tools/fork_terminal.py
```

Includes: Custom `fork_terminal.py` tool

### 3. Multi-Variant Skills
Use cookbooks for different scenarios

**Example: API Integration**
```markdown
# Workflow

IF user mentions REST: Read cookbook/rest-api.md
IF user mentions GraphQL: Read cookbook/graphql.md
IF user mentions gRPC: Read cookbook/grpc.md
```

## Skill Invocation Flow

```
User: "Fork terminal use claude code to review the auth module"
         ↓
Claude detects: "fork terminal" matches fork-terminal skill
         ↓
Claude reads: .claude/skills/fork-terminal/SKILL.md
         ↓
Claude follows: Workflow instructions
         ↓
Claude reads: cookbook/claude-code.md (matched from request)
         ↓
Claude executes: tools/fork_terminal.py
         ↓
Result: New terminal spawns with Claude Code running
```

## Best Practices

### ✅ DO

- Write clear, specific descriptions with example trigger phrases
- Use existing tools when possible (Read, Grep, WebFetch, etc.)
- Break complex workflows into numbered steps
- Include examples of user requests
- Use cookbooks for multi-variant scenarios
- Store reusable prompts in prompts/ directory

### ❌ DON'T

- Create skills for one-off tasks (use commands instead)
- Duplicate built-in functionality
- Make descriptions too broad (won't trigger reliably)
- Skip the workflow section
- Forget to test trigger phrases

## Common Patterns

### Pattern: Background Research
```markdown
# Workflow

1. Launch Task tool with run_in_background=true
2. Continue primary work
3. Retrieve results with AgentOutputTool
4. Synthesize findings
```

### Pattern: Multi-Agent Parallel Work
```markdown
# Workflow

1. Identify subtasks
2. Launch multiple Task tools in parallel (single message)
3. Continue other work
4. Retrieve all results
5. Combine outputs
```

### Pattern: Cookbook Selection
```markdown
# Workflow

1. Parse user intent
2. IF condition A: Read cookbook/a.md
3. IF condition B: Read cookbook/b.md
4. Follow cookbook instructions
```

### Pattern: Context Handoff
```markdown
# Workflow

1. IF user requests summary: Read prompts/summary_template.md
2. Fill template with conversation history
3. Pass filled template to spawned agent
```

## Global vs Project Skills

**Global Skills**: `~/.claude/skills/`
- Available in ALL projects
- Good for: General workflows, common patterns
- Example: Personal code review style

**Project Skills**: `.claude/skills/`
- Available only in this project
- Good for: Project-specific workflows
- Example: Custom deployment process

**Precedence**: Project skills override global skills with same name

## Skill Variables

Define configuration at the top of SKILL.md:

```markdown
## Variables

ENABLE_FEATURE_X: true
DEFAULT_MODEL: opus
MAX_RETRIES: 3
API_ENDPOINT: https://api.example.com
```

Reference in instructions:
```markdown
If ENABLE_FEATURE_X is true, then...
Use DEFAULT_MODEL for spawned agents...
```

## Testing Skills

1. **Trigger Test**: Say the exact phrases from your description
2. **Workflow Test**: Verify each step executes correctly
3. **Edge Cases**: Test with variations of trigger phrases
4. **Integration Test**: Ensure tools/prompts/cookbooks work together

## Examples from This Project

### Fork Terminal Skill
- **Location**: `.claude/skills/fork-terminal/`
- **Type**: Tool-enhanced + Multi-variant
- **Triggers**: "fork terminal", "new terminal", "fork session"
- **Tools**: `fork_terminal.py`
- **Cookbooks**: claude-code.md, codex-cli.md, gemini-cli.md, cli-command.md

## Next Steps

- Create a simple workflow skill (no tools)
- Add a cookbook for multi-variant logic
- Build a tool-enhanced skill with custom Python
- Experiment with background agent orchestration

## Related Concepts

- [Commands](commands.md) - User-invoked shortcuts (vs auto-invoked skills)
- [Tools](tools.md) - Custom capabilities skills can use
- [Background Agents](background-agents.md) - Parallel execution in skills
