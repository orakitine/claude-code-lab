# Background Agents - Parallel Execution

## What Are Background Agents?

Background agents are **Task tool agents that run asynchronously** while the primary agent continues working.

Think of them as spawning parallel workers for independent tasks.

## Key Characteristics

- **Async execution**: Run in background, don't block primary agent
- **Full tool access**: Can use all tools (Read, WebFetch, Bash, etc.)
- **Result retrieval**: Primary agent can get results later
- **True parallelism**: Multiple agents work simultaneously

## How It Works

```
Primary Agent                    Background Agent 1         Background Agent 2
      |                                   |                        |
      |--Task(run_in_background=true)-->START                     |
      |--Task(run_in_background=true)----------------------->START|
      |                                   |                        |
 Continue work                        Researching              Analyzing
      |                                   |                        |
   Do other stuff                     WebFetch                   Grep
      |                                   |                        |
AgentOutputTool(agent1)------------->RETURN                       |
AgentOutputTool(agent2)------------------------------------->RETURN|
      |
 Synthesize results
```

## Basic Usage

### Spawn Background Agent

```python
Task(
    subagent_type="general-purpose",
    description="Research topic A",
    prompt="Use WebFetch to retrieve https://example.com and summarize",
    run_in_background=True  # KEY: Makes it async!
)
```

### Retrieve Results

```python
AgentOutputTool(
    agentId="agent_abc123",  # Returned from Task call
    block=True  # Wait for completion
)
```

## Complete Example

### Parallel Web Research

```python
# User asks: "Research these 3 blog posts about React hooks"

# PRIMARY AGENT SPAWNS 3 BACKGROUND AGENTS
agent1 = Task(
    subagent_type="general-purpose",
    description="Research first blog post",
    prompt="Use WebFetch to get https://blog1.com/hooks and summarize key points",
    run_in_background=True,
    model="haiku"  # Fast model for simple task
)
# Returns: {"agentId": "agent_001"}

agent2 = Task(
    subagent_type="general-purpose",
    description="Research second blog post",
    prompt="Use WebFetch to get https://blog2.com/hooks and summarize key points",
    run_in_background=True,
    model="haiku"
)
# Returns: {"agentId": "agent_002"}

agent3 = Task(
    subagent_type="general-purpose",
    description="Research third blog post",
    prompt="Use WebFetch to get https://blog3.com/hooks and summarize key points",
    run_in_background=True,
    model="haiku"
)
# Returns: {"agentId": "agent_003"}

# PRIMARY AGENT CONTINUES OTHER WORK
Read("src/hooks/useAuth.js")
Edit("src/hooks/useAuth.js", ...)

# NOW RETRIEVE RESULTS
result1 = AgentOutputTool(agentId="agent_001", block=True)
result2 = AgentOutputTool(agentId="agent_002", block=True)
result3 = AgentOutputTool(agentId="agent_003", block=True)

# SYNTHESIZE
"Based on the research:
- Blog 1 suggests: {result1}
- Blog 2 recommends: {result2}
- Blog 3 proposes: {result3}

Here's how we should update our hooks..."
```

## Spawn Multiple in Parallel

**CRITICAL**: Launch all background agents in **single message** for true parallelism!

```python
# ✅ GOOD - All spawn simultaneously
Message:
  Task(..., run_in_background=True)  # Agent 1
  Task(..., run_in_background=True)  # Agent 2
  Task(..., run_in_background=True)  # Agent 3

# ❌ BAD - Sequential spawning (slower)
Message 1: Task(..., run_in_background=True)
Message 2: Task(..., run_in_background=True)
Message 3: Task(..., run_in_background=True)
```

## AgentOutputTool Options

### Blocking (Wait for Completion)
```python
AgentOutputTool(
    agentId="agent_123",
    block=True,  # Wait until done
    wait_up_to=150  # Max 150 seconds (default)
)
```

### Non-Blocking (Check Status)
```python
AgentOutputTool(
    agentId="agent_123",
    block=False  # Return immediately
)
```

Returns:
- If done: Full results
- If running: Status update
- If failed: Error message

## Agent Types for Background Work

```python
# General purpose - most common
Task(
    subagent_type="general-purpose",
    run_in_background=True
)

# Fast exploration
Task(
    subagent_type="Explore",
    run_in_background=True
)

# Planning (usually don't background this)
Task(
    subagent_type="Plan",
    run_in_background=False  # Want to review plan before implementing
)
```

## Common Patterns

### Pattern: Parallel Research
```python
# User: "Research 5 different approaches to caching"

# Spawn 5 agents in parallel
agents = []
for i, approach in enumerate(["Redis", "Memcached", "In-Memory", "CDN", "Database"]):
    agent = Task(
        subagent_type="general-purpose",
        description=f"Research {approach} caching",
        prompt=f"Research {approach} caching approach. Use WebSearch and WebFetch. Provide pros, cons, and use cases.",
        run_in_background=True,
        model="haiku"
    )
    agents.append(agent["agentId"])

# Continue other work...
Read("src/cache/index.js")

# Retrieve all results
results = [AgentOutputTool(agentId=id, block=True) for id in agents]

# Synthesize into comparison
```

### Pattern: Parallel File Analysis
```python
# User: "Analyze all controllers for security issues"

# Find all controllers
controllers = Glob("src/controllers/*.js")

# Spawn agent for each
agents = []
for controller in controllers:
    agent = Task(
        subagent_type="general-purpose",
        description=f"Analyze {controller}",
        prompt=f"Read {controller} and identify security vulnerabilities. Check for: SQL injection, XSS, auth bypass, input validation.",
        run_in_background=True
    )
    agents.append(agent["agentId"])

# Retrieve results
issues = [AgentOutputTool(agentId=id, block=True) for id in agents]

# Compile security report
```

### Pattern: Mixed Sync/Async
```python
# User: "Refactor auth module, and research best practices"

# START: Background research (don't need results yet)
research = Task(
    subagent_type="general-purpose",
    description="Research auth best practices",
    prompt="Research modern authentication best practices. Focus on JWT, session management, CSRF protection.",
    run_in_background=True,
    model="haiku"
)

# MEANWHILE: Do the refactoring
Read("src/auth.js")
Edit("src/auth.js", ...)
Bash("npm test")

# NOW: Get research results to inform further changes
best_practices = AgentOutputTool(agentId=research["agentId"], block=True)

# Apply learnings from research
Edit("src/auth.js", ...)  # Incorporate best practices
```

### Pattern: Agent Racing
```python
# User: "Find the fastest way to solve this algorithm problem"

# Try 3 different approaches in parallel
agent1 = Task(
    description="Try brute force approach",
    prompt="Implement brute force solution...",
    run_in_background=True
)

agent2 = Task(
    description="Try dynamic programming",
    prompt="Implement DP solution...",
    run_in_background=True
)

agent3 = Task(
    description="Try greedy algorithm",
    prompt="Implement greedy solution...",
    run_in_background=True
)

# Check which completes first (non-blocking)
while True:
    for agent in [agent1, agent2, agent3]:
        result = AgentOutputTool(agentId=agent["agentId"], block=False)
        if result.status == "completed":
            return result  # First one wins!
```

## Monitoring Background Agents

### Check Status Without Blocking
```python
status = AgentOutputTool(
    agentId="agent_123",
    block=False
)

if status.status == "running":
    print("Still working...")
elif status.status == "completed":
    print("Done!")
elif status.status == "failed":
    print(f"Error: {status.error}")
```

### Progressive Updates
```python
# Check periodically while doing other work
research = Task(..., run_in_background=True)

# Do some work
Read("file1.js")

# Check status
status1 = AgentOutputTool(agentId=research["agentId"], block=False)
print(status1)  # "Agent is fetching URL..."

# Do more work
Edit("file1.js", ...)

# Check again
status2 = AgentOutputTool(agentId=research["agentId"], block=False)
print(status2)  # "Agent is analyzing content..."

# Finally block and get results
final = AgentOutputTool(agentId=research["agentId"], block=True)
```

## Model Selection for Background Agents

Choose model based on task complexity:

```python
# Simple tasks - use Haiku (fast + cheap)
Task(
    prompt="Fetch URL and summarize",
    run_in_background=True,
    model="haiku"  # Fast!
)

# Default tasks - use Sonnet
Task(
    prompt="Analyze code for issues",
    run_in_background=True,
    model="sonnet"  # Balanced
)

# Complex tasks - use Opus
Task(
    prompt="Design complete architecture for feature",
    run_in_background=True,
    model="opus"  # Most capable
)
```

## Background Agents in Skills

Skills can orchestrate background agents:

```markdown
---
name: parallel-analyzer
description: Analyze codebase in parallel
---

# Workflow

1. Identify analysis tasks:
   - Security analysis
   - Performance analysis
   - Code quality analysis

2. Launch 3 background agents (single message):
   - Agent 1: Security scan
   - Agent 2: Performance profiling
   - Agent 3: Linting/formatting check

3. Continue primary work

4. Retrieve all results with AgentOutputTool

5. Synthesize comprehensive report
```

## Error Handling

```python
try:
    result = AgentOutputTool(
        agentId="agent_123",
        block=True,
        wait_up_to=60  # Timeout after 60 seconds
    )

    if result.status == "completed":
        process(result.output)
    elif result.status == "failed":
        handle_error(result.error)

except TimeoutError:
    print("Agent took too long")
```

## Best Practices

### ✅ DO

- Spawn all background agents in single message (parallelism)
- Use fast models (haiku) for simple tasks
- Continue primary work while agents run
- Check status non-blocking if you can continue working
- Use block=True only when you need results

### ❌ DON'T

- Spawn agents sequentially (defeats purpose)
- Use Opus for simple fetch tasks (expensive + slow)
- Block immediately after spawning (defeats purpose)
- Forget to retrieve results
- Spawn too many agents (resource intensive)

## Limitations

- **No inter-agent communication**: Agents can't talk to each other
- **No shared state**: Each agent is independent
- **Results via primary agent**: Must use AgentOutputTool
- **Resource limits**: Don't spawn 100 agents simultaneously

## When to Use Background Agents

**✅ Use background agents when:**
- Tasks are independent
- Tasks take significant time (web fetches, analysis)
- You have other work to do meanwhile
- Order doesn't matter

**❌ Don't use background agents when:**
- Tasks depend on each other
- Tasks are very quick (< 1 second)
- You need results immediately
- Sequential execution is clearer

## Comparison with Fork Terminal

| Aspect | Background Agents | Fork Terminal |
|--------|------------------|---------------|
| **Returns results** | ✅ Yes | ❌ No |
| **Tool access** | All Claude tools | Spawned tool's capabilities |
| **Communication** | AgentOutputTool | Filesystem only |
| **Visibility** | Hidden | New terminal window |
| **Use case** | Parallel research | Other AI tools, dev servers |

## Next Steps

- Try spawning 2-3 background agents for web research
- Experiment with mixed sync/async workflows
- Build a skill that orchestrates background agents
- Practice with different agent types

## Related Concepts

- [Task Tool](../quick-reference/cheatsheet.md#task-tool) - How to spawn agents
- [Skills](skills.md) - Can orchestrate background agents
- [Fork Terminal](../README.md#fork-terminal) - Alternative parallelism
