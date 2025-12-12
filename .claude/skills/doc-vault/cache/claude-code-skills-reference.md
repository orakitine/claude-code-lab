# Claude Code Skills - Official Reference Documentation

**Source:** https://code.claude.com/docs/en/skills
**Cached:** 2025-12-12
**Status:** Comprehensive reference extracted via claude-code-guide agent

---

## **1. What Are Skills?**

Skills are **reusable AI capabilities** in Claude Code that extend Claude's functionality for specific tasks or workflows. Think of them as specialized modules that teach Claude how to perform particular operations.

### **Key Characteristics:**

- **Modular**: Each Skill is self-contained in its own directory
- **Discoverable**: Claude automatically finds and loads Skills from configured locations
- **Flexible**: Can be triggered automatically or invoked manually via slash commands
- **Shareable**: Can be personal, project-specific, or distributed via plugins
- **Contextual**: Can include supporting files, tools, and prompts

---

## **2. SKILL.md File Structure**

The heart of every Skill is the `SKILL.md` file. This file combines **YAML frontmatter** (metadata) with **Markdown content** (instructions).

### **Complete SKILL.md Format:**

```markdown
---
name: skill-name
description: Brief description of what this skill does (shown in /skills list)
trigger: auto|manual|both
allowed-tools:
  - ToolName1
  - ToolName2
---

# Skill Instructions

Detailed instructions for Claude on how to perform this skill.

You can include:
- Step-by-step procedures
- Examples
- Guidelines
- Context about when to use this skill
```

### **YAML Frontmatter Fields:**

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `name` | Yes | String | Unique identifier for the skill (used for slash commands like `/skill-name`) |
| `description` | Yes | String | Brief description shown when listing skills. Should clearly explain when Claude should use this skill. |
| `trigger` | No | String | How the skill is invoked: `auto` (Claude decides when to use), `manual` (only via slash command), or `both`. Default: `both` |
| `allowed-tools` | No | Array | List of specific tools this skill is permitted to use. Restricts tool access for security. |

---

## **3. Skill Triggering and Invocation**

### **Trigger Modes:**

1. **`trigger: auto`** (Automatic)
   - Claude automatically considers using this skill based on context
   - The `description` field becomes crucial - it's how Claude knows when to activate it
   - Example: A code review skill that Claude uses when you mention "review this code"

2. **`trigger: manual`** (Slash Command Only)
   - Only invoked when user explicitly runs `/skill-name`
   - Useful for skills you want complete control over
   - Example: A deployment skill you only want to run intentionally

3. **`trigger: both`** (Default)
   - Can be triggered automatically OR manually
   - Most flexible option

### **Slash Command Invocation:**

When you create a skill named `quality-gate`, you can invoke it with:
```bash
/quality-gate
```

Skills can also accept arguments through the `$ARGUMENTS` variable (similar to custom slash commands).

---

## **4. The Cookbook Pattern**

The **Cookbook Pattern** is a best practice for organizing Skills that involve multi-step procedures or complex workflows.

### **Concept:**

Instead of putting all instructions directly in `SKILL.md`, you create supporting files that act as "recipes" - detailed, step-by-step guides for specific operations.

### **Structure:**

```
my-skill/
├── SKILL.md                 # Main skill file (high-level orchestration)
├── prompts/
│   ├── step1-analysis.md    # Detailed prompt for step 1
│   ├── step2-execution.md   # Detailed prompt for step 2
│   └── step3-validation.md  # Detailed prompt for step 3
└── tools/
    └── helper-script.sh     # Supporting automation scripts
```

### **Example SKILL.md Using Cookbook Pattern:**

```markdown
---
name: deploy-app
description: Deploys application through staging and production environments
trigger: manual
---

# Application Deployment Skill

This skill orchestrates a multi-stage deployment process.

## Workflow:

1. First, read and follow `/prompts/pre-deployment-checks.md`
2. Then execute staging deployment using `/prompts/deploy-staging.md`
3. Run validation tests described in `/prompts/validate-deployment.md`
4. Finally, if validation passes, proceed with `/prompts/deploy-production.md`

Always use the helper scripts in `/tools/` for actual deployment commands.
```

### **Benefits:**

- **Modularity**: Each step is self-contained
- **Maintainability**: Easy to update individual steps
- **Clarity**: Complex workflows broken into digestible pieces
- **Reusability**: Prompts can be referenced by multiple skills

---

## **5. Supporting Directories**

Skills can include additional directories for organization:

### **`prompts/` Directory:**

Contains detailed prompt files that the skill references.

**Purpose:**
- Break complex instructions into manageable pieces
- Store templates for different scenarios
- Keep the main SKILL.md concise

**Example:**
```
prompts/
├── code-review-checklist.md
├── security-review.md
└── performance-analysis.md
```

### **`tools/` Directory:**

Contains executable scripts and automation tools.

**Purpose:**
- Bash scripts for common operations
- Helper utilities
- Integration scripts with external tools

**Example:**
```
tools/
├── run-linter.sh
├── check-types.sh
└── run-tests.sh
```

### **Other Common Directories:**

- **`docs/`**: Reference documentation
- **`templates/`**: File templates used by the skill
- **`examples/`**: Example outputs or usage scenarios
- **`config/`**: Configuration files

---

## **6. allowed-tools: Restricting Tool Access**

The `allowed-tools` field provides fine-grained security control.

### **Purpose:**

Limit which tools Claude can use when executing this skill. This prevents:
- Accidental file modifications
- Unintended command execution
- Security risks from compromised skills

### **Example:**

```yaml
---
name: read-only-analysis
description: Analyzes code without making any changes
trigger: auto
allowed-tools:
  - Read
  - Grep
  - Glob
---
```

This skill can ONLY use Read, Grep, and Glob - preventing any Write or Bash operations.

### **Available Tools:**

Common tools you might restrict:
- `Read` - Read files
- `Write` - Write/edit files
- `Bash` - Execute bash commands
- `Grep` - Search file contents
- `Glob` - Find files by pattern
- MCP tools (if configured)

---

## **7. Skill Locations (Scopes)**

Skills can be stored in three locations, each with different scope:

### **Personal Skills** (User-level)
- **Location**: `~/.claude/skills/`
- **Scope**: Available in ALL projects for this user
- **Use Case**: Personal workflow automation you use across projects

### **Project Skills** (Project-level)
- **Location**: `./.claude/skills/` (in your project root)
- **Scope**: Only available in this specific project
- **Use Case**: Project-specific workflows, shared with team via git
- **Team Sharing**: Committed to version control, auto-loaded for team members

### **Plugin Skills** (Plugin-level)
- **Location**: Inside plugin directory structure
- **Scope**: Available when plugin is installed
- **Use Case**: Distributable skills via plugin marketplace

### **Precedence:**

If skills with the same name exist in multiple locations:
1. Project skills override
2. Personal skills override
3. Plugin skills (lowest priority)

---

## **8. Best Practices**

### **Skill Design:**

1. **Keep Skills Focused**
   - One skill = one clear purpose
   - Don't create mega-skills that do everything
   - Break complex workflows into multiple skills

2. **Write Clear Descriptions**
   - The `description` is how Claude decides when to auto-trigger
   - Be specific about WHEN the skill should be used
   - Include keywords that match user intent

   **Bad**: "Code helper"
   **Good**: "Performs comprehensive code quality checks including linting, type checking, and tests before committing"

3. **Use Cookbook Pattern for Complexity**
   - If your SKILL.md is longer than ~100 lines, consider breaking it up
   - Use `prompts/` for detailed sub-procedures
   - Use `tools/` for executable automation

4. **Test Thoroughly**
   - Test both manual and auto-trigger modes
   - Verify `allowed-tools` restrictions work as expected
   - Test with different argument patterns

5. **Document Skill Versions**
   - Add version comments in SKILL.md
   - Document changes in commit messages
   - Maintain backwards compatibility when possible

### **Security Best Practices:**

1. **Use `allowed-tools` for sensitive operations**
2. **Review auto-triggered skills carefully** - they activate without explicit user approval
3. **Avoid hardcoded secrets** - use environment variables or prompts
4. **Test in isolation** before deploying to team

### **Team Collaboration:**

1. **Commit skills to git** for project skills
2. **Document skill usage** in project README
3. **Use consistent naming conventions** across skills
4. **Review skill changes in PRs** like regular code

---

## **9. Creating Skills: Quick Start**

### **Personal Skill:**

```bash
mkdir -p ~/.claude/skills/my-skill
cat > ~/.claude/skills/my-skill/SKILL.md <<'EOF'
---
name: my-skill
description: Does something awesome
trigger: manual
---

# My Awesome Skill

Instructions for Claude...
EOF
```

### **Project Skill:**

```bash
mkdir -p .claude/skills/project-skill
cat > .claude/skills/project-skill/SKILL.md <<'EOF'
---
name: project-skill
description: Project-specific functionality
trigger: both
---

# Project Skill

Project-specific instructions...
EOF
```

### **Skill with Cookbook Pattern:**

```bash
mkdir -p .claude/skills/complex-skill/{prompts,tools}

# Main skill file
cat > .claude/skills/complex-skill/SKILL.md <<'EOF'
---
name: complex-skill
description: Multi-step complex workflow
trigger: manual
---

# Complex Skill

Follow these steps:
1. Execute instructions in prompts/step1.md
2. Execute instructions in prompts/step2.md
3. Run tools/validation.sh
EOF

# Supporting prompts
echo "# Step 1 Instructions..." > .claude/skills/complex-skill/prompts/step1.md
echo "# Step 2 Instructions..." > .claude/skills/complex-skill/prompts/step2.md

# Supporting tools
cat > .claude/skills/complex-skill/tools/validation.sh <<'EOF'
#!/bin/bash
echo "Running validation..."
EOF
chmod +x .claude/skills/complex-skill/tools/validation.sh
```

---

## **10. Debugging Skills**

### **Common Issues:**

**Problem: Claude doesn't use my auto-triggered skill**
- **Solution**: Make the `description` more specific and keyword-rich
- **Solution**: Verify the skill is actually loaded with `/skills`
- **Solution**: Try invoking manually first to test the skill logic

**Problem: Skill has errors**
- **Solution**: Check YAML syntax (use a YAML validator)
- **Solution**: Verify file paths are correct
- **Solution**: Check for typos in tool names in `allowed-tools`

**Problem: Multiple skills conflict**
- **Solution**: Check skill names for conflicts across scopes
- **Solution**: Rename one skill to make it unique
- **Solution**: Remove or disable conflicting skills

### **Debugging Commands:**

```bash
# List all available skills
/skills

# Try invoking manually to test
/my-skill

# Check settings file for issues
cat .claude/settings.json
```

---

## **11. Example Skills**

### **Simple Skill (Single File):**

```markdown
---
name: hello
description: Says hello to the user
trigger: manual
---

# Hello Skill

Greet the user warmly and ask how you can help them today.
```

### **Skill with Tool Permissions:**

```markdown
---
name: read-analysis
description: Analyzes code structure without making any modifications
trigger: auto
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Read-Only Code Analysis

You can read and analyze code, but you CANNOT modify anything.

Steps:
1. Use Glob to find relevant files
2. Use Read to examine their contents
3. Use Grep to search for patterns
4. Provide analysis and recommendations
```

### **Multi-File Skill with Cookbook:**

```
quality-check/
├── SKILL.md
├── prompts/
│   ├── lint-check.md
│   ├── type-check.md
│   └── test-check.md
└── tools/
    └── run-checks.sh

SKILL.md:
---
name: quality-check
description: Runs comprehensive quality checks on code
trigger: manual
allowed-tools:
  - Bash
  - Read
---

# Quality Check Skill

Execute these checks in order:

1. Linting: Follow prompts/lint-check.md
2. Type Checking: Follow prompts/type-check.md
3. Tests: Follow prompts/test-check.md

Use tools/run-checks.sh to execute each check.
```

---

## **12. Skills vs. Slash Commands vs. Subagents**

### **Use Skills When:**
- You need auto-triggering capability
- You want to package complex workflows
- You need tool access restrictions
- You're building reusable procedures

### **Use Slash Commands When:**
- Simple, one-off shortcuts
- Quick text substitutions
- Don't need auto-triggering
- Don't need multiple supporting files

### **Use Subagents When:**
- Need a completely separate AI instance
- Want different model or configuration
- Need isolation between tasks
- Building specialized AI personas

---

## **13. Advanced Patterns**

### **Pattern: Skill Chaining**

One skill can invoke another:

```markdown
---
name: full-deploy
description: Complete deployment with all checks
---

# Full Deployment

1. First run /quality-check
2. Then run /security-scan
3. Finally run /deploy-prod
```

### **Pattern: Conditional Execution**

```markdown
---
name: smart-commit
description: Intelligently commits code after running appropriate checks
---

# Smart Commit

1. Analyze changed files
2. If TypeScript files changed, run /type-check
3. If test files changed, run /test
4. If all checks pass, commit with appropriate message
```

### **Pattern: Dynamic Prompts**

```markdown
---
name: framework-helper
description: Provides framework-specific assistance
---

# Framework Helper

1. Detect the framework by reading package.json
2. Load the appropriate prompt from prompts/{framework}-guide.md
3. Follow that framework's specific patterns
```

---

## **14. Constraints and Limitations**

1. **Character/Token Limits**: Very large SKILL.md files may hit context limits
2. **No Parameters in YAML**: You can't parameterize frontmatter values dynamically
3. **File Path Resolution**: Paths in skills are relative to skill directory
4. **Execution Order**: When multiple auto-triggered skills match, Claude decides priority
5. **No Persistent State**: Skills don't maintain state between invocations

---

## **15. Integration with Other Features**

### **Skills + Hooks:**

Hooks can trigger skills:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": ["claude --prompt 'Run /code-review before writing'"]
      }
    ]
  }
}
```

### **Skills + MCP:**

Skills can use MCP tools if configured:

```yaml
allowed-tools:
  - github_create_issue
  - slack_send_message
```

### **Skills + Subagents:**

Skills can invoke subagents for specialized tasks.

---

**End of Official Skills Reference Documentation**
