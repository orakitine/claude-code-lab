# Skill Patterns

Common patterns for building Claude Code skills.

## Pattern 1: Simple Workflow Skill

**Use case:** Auto-invoke a specific workflow when user mentions trigger phrase

```markdown
---
name: code-formatter
description: Use when user asks to format code or fix code style
---

# Purpose
Auto-format code files according to project standards

## Workflow

1. Identify which files need formatting
2. Run appropriate formatter:
   - JavaScript/TypeScript: prettier
   - Python: black
   - Rust: rustfmt
3. Report what was formatted
```

**Triggers:**
- "format the code"
- "fix code style"
- "run prettier"

## Pattern 2: Multi-Variant Skill (Cookbook)

**Use case:** Different workflows based on user's specific request

**Structure:**
```
.claude/skills/api-integration/
├── SKILL.md
└── cookbook/
    ├── rest-api.md
    ├── graphql.md
    └── grpc.md
```

**SKILL.md:**
```markdown
---
name: api-integration
description: Integrate APIs when user mentions REST, GraphQL, or gRPC
---

# Workflow

IF user mentions REST: Read cookbook/rest-api.md
IF user mentions GraphQL: Read cookbook/graphql.md
IF user mentions gRPC: Read cookbook/grpc.md

Follow the cookbook instructions
```

**cookbook/rest-api.md:**
```markdown
# REST API Integration

1. Read existing API setup
2. Create new endpoint file
3. Add route handler
4. Implement request/response logic
5. Add tests
6. Update API documentation
```

## Pattern 3: Tool-Enhanced Skill

**Use case:** Skill needs custom capability not built into Claude

**Structure:**
```
.claude/skills/database-migrator/
├── SKILL.md
└── tools/
    └── run_migration.py
```

**SKILL.md:**
```markdown
---
name: database-migrator
description: Run database migrations when user asks
---

# Workflow

1. Check for pending migrations
2. Review migration files
3. Execute tools/run_migration.py
4. Verify migration success
5. Update schema documentation
```

**tools/run_migration.py:**
```python
#!/usr/bin/env -S uv run
"""Run database migrations."""

import subprocess

def run_migration(direction: str = "up") -> str:
    """Run database migrations up or down."""
    cmd = f"npm run migrate:{direction}"
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True
    )
    return f"Migration {direction} completed: {result.stdout}"
```

## Pattern 4: Background Agent Orchestration

**Use case:** Parallel research or analysis tasks

```markdown
---
name: parallel-analyzer
description: Analyze codebase in parallel when user requests analysis
---

# Workflow

1. Identify analysis dimensions:
   - Security
   - Performance
   - Code quality
   - Test coverage

2. Launch 4 background agents (single message):
   - Agent 1: Security scan (grep for vulnerabilities)
   - Agent 2: Performance analysis (identify bottlenecks)
   - Agent 3: Code quality (check complexity, duplication)
   - Agent 4: Test coverage (analyze test files)

3. Continue primary work

4. Retrieve all results with AgentOutputTool

5. Synthesize comprehensive report
```

## Pattern 5: Context Handoff

**Use case:** Pass current conversation context to spawned agent

**Structure:**
```
.claude/skills/delegator/
├── SKILL.md
└── prompts/
    └── handoff_template.md
```

**SKILL.md:**
```markdown
---
name: delegator
description: Delegate work to new agent with context
---

# Workflow

When user says "delegate this" or "hand off with context":

1. Read prompts/handoff_template.md
2. Fill template with:
   - Conversation history summary
   - Current task state
   - Next steps
3. Spawn new agent with filled template as initial prompt
4. Report delegation complete
```

**prompts/handoff_template.md:**
```markdown
# Context Summary

## Previous Discussion
<FILL: Summary of conversation so far>

## Current State
<FILL: What's been done>

## Your Task
<FILL: What needs to happen next>

## Important Context
<FILL: Key decisions, constraints, preferences>
```

## Pattern 6: Conditional Execution

**Use case:** Workflow varies based on project type or environment

```markdown
---
name: smart-tester
description: Run tests intelligently based on project type
---

## Workflow

1. Detect project type:
   - Check for package.json → Node.js
   - Check for requirements.txt → Python
   - Check for Cargo.toml → Rust

2. Run appropriate test command:
   - Node.js: npm test
   - Python: pytest
   - Rust: cargo test

3. If tests fail:
   - Parse error output
   - Identify failing tests
   - Attempt fixes
   - Re-run

4. Report results
```

## Pattern 7: Progressive Enhancement

**Use case:** Multi-pass implementation with increasing sophistication

```markdown
---
name: progressive-builder
description: Build features progressively when user requests implementation
---

# Workflow

1. **Pass 1 - Basic Implementation**
   - Core functionality only
   - No error handling yet
   - Minimal validation

2. **Pass 2 - Robustness**
   - Add error handling
   - Input validation
   - Edge case handling

3. **Pass 3 - Testing**
   - Unit tests
   - Integration tests
   - Test edge cases

4. **Pass 4 - Documentation**
   - Code comments
   - API documentation
   - Usage examples

Each pass builds on previous pass
```

## Pattern 8: File Template Generator

**Use case:** Create files from templates

**Structure:**
```
.claude/skills/component-generator/
├── SKILL.md
└── prompts/
    ├── react-component.md
    ├── vue-component.md
    └── api-route.md
```

**SKILL.md:**
```markdown
---
name: component-generator
description: Generate component files when user asks to create component
---

# Workflow

1. Determine component type from user request
2. Read appropriate template from prompts/
3. Fill in component name and specifics
4. Create file with filled template
5. Create corresponding test file
6. Report files created
```

**prompts/react-component.md:**
```markdown
import React from 'react';

interface <COMPONENT_NAME>Props {
  // TODO: Define props
}

export const <COMPONENT_NAME>: React.FC<<COMPONENT_NAME>Props> = (props) => {
  return (
    <div>
      {/* TODO: Implement component */}
    </div>
  );
};
```

## Pattern 9: Validation Gate

**Use case:** Check conditions before proceeding

```markdown
---
name: safe-deployer
description: Deploy with safety checks
---

# Workflow

1. **Pre-flight Checks:**
   - All tests passing?
   - No uncommitted changes?
   - On correct branch?
   - Version bumped?

2. If any check fails:
   - Report what failed
   - Ask user if should proceed anyway
   - If no: abort

3. If all pass:
   - Run deployment
   - Verify deployment
   - Report success
```

## Pattern 10: Learning Skill

**Use case:** Skill that improves based on feedback

```markdown
---
name: adaptive-reviewer
description: Code review that learns from user feedback
---

## Variables

FOCUS_AREAS: security, performance, tests
STRICTNESS: medium
PREVIOUS_FEEDBACK: (none yet)

# Workflow

1. Read code changes
2. Review focusing on FOCUS_AREAS
3. Apply STRICTNESS level
4. Consider PREVIOUS_FEEDBACK patterns
5. Report findings
6. If user provides feedback:
   - Update FOCUS_AREAS
   - Adjust STRICTNESS
   - Note PREVIOUS_FEEDBACK
```

User can then update the Variables section based on experience!

## Combining Patterns

### Example: Full-Featured Deployment Skill

```
.claude/skills/smart-deploy/
├── SKILL.md
├── cookbook/
│   ├── staging.md
│   ├── production.md
│   └── rollback.md
├── prompts/
│   └── deployment_checklist.md
└── tools/
    ├── deploy.py
    └── verify_deployment.py
```

**Combines:**
- Multi-variant (cookbook for different environments)
- Tool-enhanced (custom deployment scripts)
- Validation gate (pre-flight checks)
- Progressive enhancement (deploy → verify → notify)

## Best Practices Across Patterns

1. **Clear trigger descriptions** - Make it obvious when skill applies
2. **Numbered workflows** - Step-by-step clarity
3. **Error handling** - What if things fail?
4. **User feedback** - Report what was done
5. **Documentation** - Explain the workflow
6. **Testing** - Try various trigger phrases

## Anti-Patterns to Avoid

❌ **Overly broad triggers**
```markdown
description: Use when user asks for help
```
Too vague! Won't trigger reliably.

❌ **Too many responsibilities**
```markdown
description: Code review, testing, deployment, documentation, and refactoring
```
Split into separate skills!

❌ **No clear workflow**
```markdown
# Workflow
Do the thing
```
Be specific!

❌ **Duplicating built-in capabilities**
```markdown
# Workflow
1. Read the file
2. Search for pattern
```
Use built-in Read and Grep!

## Template for New Skills

```markdown
---
name: my-skill-name
description: Use when user [specific trigger phrases]. Include examples: "phrase 1", "phrase 2"
---

# Purpose

[Clear statement of what this skill accomplishes]

## Variables (optional)

SETTING_NAME: default_value
ANOTHER_SETTING: value

## Instructions

[High-level guidance for Claude]

## Workflow

1. [First step - be specific]
2. [Second step]
3. [Third step]
4. [Return results / report completion]

## Examples

User phrases that trigger this skill:
- "example trigger phrase 1"
- "example trigger phrase 2"
- "example trigger phrase 3"
```

## Next Steps

1. Pick a pattern that matches your need
2. Copy the template
3. Customize for your use case
4. Test with various trigger phrases
5. Iterate based on results
