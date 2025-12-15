# Claude Code Skills: Style Guide & Standards

**Purpose**: Standardized format for creating and editing Claude Code skills. Ensures consistency across AI (Claude), skill authors, and team developers.

**Audience**: Claude AI, skill creators, development teams

**Status**: Living Standard

**Last Updated**: 2025-12-12

---

## Table of Contents

1. [Core Principles](#core-principles)
2. [File Structure Standards](#file-structure-standards)
3. [Formatting Rules](#formatting-rules)
4. [Content Standards](#content-standards)
5. [Quick Reference](#quick-reference)
6. [Examples](#examples)

---

## Core Principles

### Single Source of Truth

**Rule**: Every piece of information exists in exactly ONE place.

- ✅ Workflow contains all procedural steps
- ✅ Variables contain all configuration
- ✅ Inline examples show behavior
- ❌ No Quick Reference sections (duplicates Workflow)
- ❌ No separate Examples sections (use inline)
- ❌ No Notes sections (use inline comments)

**Why**: When you edit information, you edit it once. No synchronization needed.

### Lean = No Duplication

**Rule**: Lean means zero duplication, NOT minimal lines.

A 50-line cookbook with clear examples is leaner than a 20-line cookbook requiring external documentation.

**Optimize for**:
- Clarity (self-documenting workflows)
- Maintainability (single edit points)
- Completeness (all information present)

**Don't optimize for**:
- Line count minimization
- Token reduction at clarity's expense

### Readability for Humans and AI

**Rule**: Skills must be readable by Claude AI AND human developers.

- ✅ **Bold step names** (minimal token cost, huge scan-ability)
- ✅ Inline examples (show expected behavior immediately)
- ✅ Consistent formatting (reduce cognitive load)
- ✅ Clear structure (easy to navigate)

**Balance**: Small token costs for large UX wins are acceptable.

---

## File Structure Standards

### Required SKILL.md Structure

```markdown
---
name: Skill Name
description: One-line description of what this skill does
trigger: manual|auto|both
allowed-tools:
  - ToolName1
  - ToolName2
---

# Purpose

[Single paragraph: what this skill does, when to use it]

## Variables

VARIABLE_NAME: default_value                  # Inline comment explaining purpose
ANOTHER_VAR: value                            # Options: value1, value2, value3

## Workflow

1. **Step Name**
   - Action to perform
   - IF: <condition> → THEN <action>
   - Example: "user input" → Expected behavior
   - Tool: Tool name with parameters

## Cookbook

### Scenario Name

- IF: Condition that triggers this cookbook
- THEN: Read and execute `.claude/skills/skill-name/cookbook/file-name.md`
- EXAMPLES:
  - "example user request 1"
  - "example user request 2"
```

**Required Sections** (in order):
1. YAML frontmatter
2. Purpose
3. Variables (if any configuration needed)
4. Workflow
5. Cookbook (if multiple scenarios exist)

**Optional Sections** (if non-duplicative):
- **Setup/Tips**: After Purpose, before Variables - for configuration guidance, prerequisites, or setup instructions that don't belong in Workflow
- **Prerequisites**: Before Variables - for required dependencies or environment setup

**Forbidden Sections**:
- ❌ Quick Reference (duplicates Workflow)
- ❌ Examples (separate from Workflow - use inline)
- ❌ Notes (use inline comments on Variables)
- ❌ Instructions (merge into Workflow)
- ❌ Success Criteria (implied by Workflow completion)
- ❌ Decorative emojis (functional icons acceptable in limited cases)

### Required Cookbook File Structure

```markdown
# Cookbook Title

[Brief purpose statement: 1-2 sentences]

## Variables

COOKBOOK_VAR: value                           # Only if cookbook needs unique config

## Workflow

1. **Step Name**
   - Detailed action
   - Example: "input" → output
   - Tool: Specific tool with flags

## Failure Criteria

Gate FAILS if: condition1, condition2
Gate shows WARNINGS if: condition3

(Optional - only for validation workflows)
```

**Required Sections** (in order):
1. Title and purpose
2. Variables (if cookbook-specific config needed)
3. Workflow

**Optional Sections**:
- Failure Criteria (only for quality gates, validation)

**Forbidden Sections**:
- ❌ Quick Reference
- ❌ Examples (separate from Workflow)
- ❌ Notes

---

## Formatting Rules

### 1. Frontmatter (YAML)

**ALWAYS EXPLICIT** - Never rely on defaults.

```yaml
---
name: Full Skill Name                         # Human-readable name
description: Brief description of purpose     # One line max
trigger: manual|auto|both                     # REQUIRED
allowed-tools:                                # REQUIRED (even if all tools)
  - Read
  - Bash
  - Glob
---
```

**Trigger values**:
- `manual`: Only via slash command (destructive ops, explicit workflows)
- `auto`: AI decides when relevant (helper skills, context awareness)
- `both`: Either method (analysis tools useful both ways)

**Allowed-tools**:
- Explicit list of permitted tools
- Security restriction enforced by skill system
- Omitting Write makes skill non-destructive

**Why explicit**: Documents intent, forces security awareness, prevents assumption errors.

### 2. Purpose Section

**Format**:
```markdown
# Purpose

Single paragraph explaining what this skill does and when to use it.
```

**Rules**:
- One paragraph maximum
- State what the skill does
- State when to use it
- No examples (save for Workflow)

### 3. Variables Section

**Format**:
```markdown
## Variables

VARIABLE_NAME: default_value                  # Inline comment explaining purpose
FLAG_OPTION: true                             # Boolean flag description
PATH_VAR: .claude/skills/name/cache           # File path description
MODE_VAR: display                             # Options: display, save, export
```

**Rules**:
- One variable per line
- SCREAMING_SNAKE_CASE names
- Inline comment on SAME line (after two spaces and #)
- Comments explain purpose or list options
- Only include configurable values (no internal constants)

**Variable types**:
- ✅ Configurable behavior (OUTPUT_MODE: display|save)
- ✅ Feature flags (ENABLE_JAVASCRIPT: true)
- ✅ Paths and locations (CACHE_DIR: path)
- ✅ Model selection (DEFAULT_MODEL: opus)
- ❌ Constants that never change
- ❌ Internal implementation details

### 4. Workflow Section

**Format**:
```markdown
## Workflow

1. **Step Name**
   - Action to perform
   - Conditional: IF <condition> → THEN <action>
   - Example: "user input" → Expected behavior
   - Tool: Tool name with specific parameters
```

**Rules**:
- **Bold step names** (use `**Step Name**`)
- Numbered list (1, 2, 3...)
- Each step has sub-bullets with details
- EVERY step has at least one inline example
- Conditionals use: `IF: <condition> → THEN <action>`
- Tool usage shows specific parameters/flags

**Step anatomy**:
1. **Bold name**: What is happening (action-oriented)
2. Action details: How to accomplish it
3. Conditionals: IF/THEN logic when applicable
4. Example: Concrete input → output demonstration
5. Tool reference: Which tool, what parameters

**Conditional format**:
```markdown
- IF: package.json exists AND ENABLE_JAVASCRIPT → Run npm checks
- ELSE IF: requirements.txt exists AND ENABLE_PYTHON → Run Python checks
- Example: package.json found → Route to cookbook/javascript.md
```

### 5. Cookbook Section

**Format**:
```markdown
## Cookbook

### Scenario Name

- IF: Condition that triggers this cookbook
- THEN: Read and execute `.claude/skills/skill-name/cookbook/file-name.md`
- EXAMPLES:
  - "example user request 1"
  - "example user request 2"
```

**Rules**:
- H3 heading for each scenario (`### Name`)
- IF/THEN/EXAMPLES structure
- IF: Condition (when to use this cookbook)
- THEN: Exact file path to cookbook
- EXAMPLES: 2-4 example user requests

---

## Content Standards

### What to Include

**✅ Always include**:
- Inline examples in EVERY workflow step
- Specific tool parameters (flags, options)
- Conditional logic (IF/THEN/ELSE)
- Expected input/output format
- Pattern reference lists (for analysis skills)
- Example reports (for skills that generate reports)

**✅ Include when relevant**:
- Variables section (only if configuration needed)
- Cookbook section (only if multiple scenarios exist)
- Failure Criteria (only for validation workflows)
- Cookbook-specific variables (in cookbook files)

### What to Exclude

**❌ Never include**:
- Quick Reference sections (duplicates Workflow)
- Separate Examples sections (use inline examples)
- Notes sections (use inline comments on Variables)
- Instructions sections (merge into Workflow)
- Success Criteria (implied by Workflow completion)
- Decorative emojis (unless specifically requested)
- Verbose explanations (be concise)

**✅ Can include** (if providing unique value):
- Setup/Tips section (after Purpose, non-duplicative configuration guidance)
- Prerequisites section (before Variables, dependency requirements)

### Inline Example Standards

**Every workflow step MUST have an example showing**:
- What triggers this step (for conditional steps)
- What the input looks like
- What the output should be
- Edge cases (when applicable)

**Good example**:
```markdown
1. **Detect Trigger**
   - Check for: "docs", "documentation", "api reference"
   - Do NOT trigger on topic names alone
   - Example: "check the Stripe docs" → TRIGGERED ✓
   - Example: "how does Stripe work?" → NOT TRIGGERED ✗
```

**Bad example**:
```markdown
1. **Detect Trigger**
   - Check for documentation keywords
```

**Why good example works**:
- Shows exact keywords to match
- Shows negative case (what NOT to trigger on)
- Clear input → output format

### Placeholder Consistency

**Standard**: Use `<angle>` brackets for all placeholders.

**✅ Correct**:
```markdown
- Format: `claude --model <model> -p "<task>"`
- Read file: `<file_path>`
- Output: `<result>`
```

**❌ Incorrect**:
```markdown
- Format: `claude --model [model] -p "{task}"`  # Inconsistent brackets
```

**Why**: Consistent placeholders reduce cognitive load, make patterns recognizable.

---

## Quick Reference

### Creating New Skills Checklist

When creating a new skill from scratch:

1. **Define purpose**:
   - [ ] What task does this skill perform?
   - [ ] When should it activate (manual/auto/both)?
   - [ ] Is it destructive (needs Write) or read-only?

2. **Write frontmatter**:
   - [ ] Name and description
   - [ ] Explicit trigger value
   - [ ] Explicit allowed-tools list

3. **Write Purpose paragraph**:
   - [ ] One paragraph max
   - [ ] States what and when

4. **Identify Variables** (if needed):
   - [ ] Only configurable values
   - [ ] Inline comments on same line
   - [ ] SCREAMING_SNAKE_CASE names

5. **Design Workflow**:
   - [ ] Bold step names
   - [ ] Inline example in EVERY step
   - [ ] Conditionals use IF/THEN format
   - [ ] Tool references show parameters

6. **Create Cookbooks** (if needed):
   - [ ] Separate file per scenario
   - [ ] IF/THEN/EXAMPLES structure in SKILL.md
   - [ ] Same formatting rules as SKILL.md

7. **Remove duplication**:
   - [ ] No Quick Reference
   - [ ] No separate Examples section
   - [ ] No Notes section

### Editing Existing Skills Checklist

When modifying an existing skill:

1. **Read entire skill first**
2. **Identify issues**:
   - [ ] Duplication (Quick Ref, Examples, Notes)
   - [ ] Missing frontmatter fields
   - [ ] Missing inline examples
   - [ ] Inconsistent placeholders
   - [ ] Vague workflow steps

3. **Fix structure**:
   - [ ] Consolidate into Workflow with inline examples
   - [ ] Move notes into inline comments on Variables
   - [ ] Remove forbidden sections
   - [ ] Verify frontmatter is explicit

4. **Verify completeness**:
   - [ ] No information loss
   - [ ] All technical details preserved
   - [ ] Examples show expected behavior

### Code Review Checklist

When reviewing a skill (human or AI):

**Structure**:
- [ ] Frontmatter has explicit trigger and allowed-tools
- [ ] Purpose paragraph is clear and concise (1 paragraph)
- [ ] Variables section present (if configuration needed)
- [ ] Variables have inline comments
- [ ] Workflow section present
- [ ] Cookbook section present (if multiple scenarios)

**Formatting**:
- [ ] Bold step names (`**Step Name**`)
- [ ] Consistent placeholders (`<angle>` brackets)
- [ ] Proper IF/THEN/EXAMPLES structure in Cookbook
- [ ] Inline comments on same line as Variables

**Content**:
- [ ] Every Workflow step has inline examples
- [ ] Tool references show specific parameters/flags
- [ ] Conditionals are clear (IF/THEN)
- [ ] No Quick Reference section
- [ ] No separate Examples section
- [ ] No Notes section (merged into Variables)
- [ ] No duplication between sections
- [ ] No duplication between SKILL.md and cookbooks

**Completeness**:
- [ ] All technical details preserved
- [ ] Pattern reference lists included (for analysis skills)
- [ ] Example reports included (for reporting skills)
- [ ] Cookbook-specific variables documented (in cookbooks)

---

## Decision Trees

### When to Create Skill vs. Cookbook

**Create separate skill when**:
- Completely different purpose
- No shared workflow logic
- Independent triggers
- Different tool requirements
- Example: doc-vault vs. quality-gate

**Create cookbook (within skill) when**:
- Variations of same core task
- Shared setup, different execution
- Same tools, different workflows
- Branching logic based on context
- Example: fork-terminal with different CLI tools

### When to Use Cookbooks

**Use cookbook pattern when**:
- ✅ Multiple distinct scenarios exist
- ✅ Branching logic would clutter SKILL.md
- ✅ Different workflows for different contexts
- ✅ Each branch needs different variables

**Benefits**:
- Claude only reads relevant branch (efficiency)
- Smaller file sizes (better context management)
- Single responsibility per cookbook
- Easier to maintain (isolated changes)

**Cookbook types**:

1. **Command Execution** (concise):
   - Exact commands with flags
   - Parameter passing details
   - Typical size: 30-50 lines
   - Example: fork-terminal cookbooks

2. **Analysis Guides** (comprehensive):
   - Pattern recognition workflows
   - Domain knowledge reference lists
   - Technology detection heuristics
   - Typical size: 60-100 lines
   - Example: project-context cookbooks

### When to Use Failure Criteria Section

**Include Failure Criteria when**:
- ✅ Quality gates (linting, testing, build)
- ✅ Validation workflows
- ✅ Clear pass/fail states needed
- ✅ Multiple failure conditions exist

**Omit Failure Criteria when**:
- ❌ General-purpose skills
- ❌ Success implied by completion
- ❌ No clear failure states

### Trigger Selection

**Use `trigger: manual` when**:
- Destructive operations (commit, push, delete)
- Explicit user workflows (quality-gate)
- Commands with side effects
- User should control execution

**Use `trigger: auto` when**:
- Helper skills that enhance responses (doc-vault)
- Context awareness (consult docs when mentioned)
- Non-intrusive improvements
- Safe to run automatically

**Use `trigger: both` when**:
- Useful via slash command AND automatically
- Example: project-context
  - Manual: `/project-context` for explicit analysis
  - Auto: Claude suggests when context would help

---

## Examples

### Example 1: Good SKILL.md Structure

```markdown
---
name: Quality Gate Skill
description: Comprehensive code quality verification workflow that checks linting, formatting, type safety, tests, and build before committing code. Non-destructive - only reports issues without making changes.
trigger: manual
allowed-tools:
  - Bash
  - Read
  - Glob
---

# Purpose

Run comprehensive Quality Gate checks to verify code quality before committing. Non-destructive analysis only - reports issues without auto-fixing. Includes linting, formatting, type safety, tests, build verification, and security checks.

**Tip**: For parallel execution, add `ENABLE_PARALLEL_EXECUTION: true` to your project's Variables.

## Variables

ENABLE_JAVASCRIPT: true           # Enable JavaScript/TypeScript quality checks
ENABLE_PYTHON: true               # Enable Python quality checks
ENABLE_SECURITY_CHECK: true       # Enable security vulnerability scanning

## Workflow

1. **Detect Project Type**
   - Check for indicator files
   - JavaScript/TypeScript: package.json
   - Python: requirements.txt or pyproject.toml
   - Example: package.json found → JavaScript/TypeScript project

2. **Route to Cookbook**
   - IF: package.json exists AND ENABLE_JAVASCRIPT → cookbook/javascript.md
   - ELSE IF: requirements.txt exists AND ENABLE_PYTHON → cookbook/python.md
   - Example: TypeScript project + ENABLE_JAVASCRIPT=true → Route to javascript.md

3. **Execute Quality Checks**
   - Run all check phases defined in cookbook
   - IMPORTANT: Non-destructive - only report issues, never auto-fix
   - Continue on failure - run all phases even if some fail
   - Example: Run lint → format check → type check → tests → build

4. **Generate Report**
   - Compile results from all phases
   - Include: file paths, line numbers, error messages, fix commands
   - Format: Clear sections per phase (✓ passed, ✗ failed), summary at end
   - Example: "Linting: ✗ 5 errors in src/utils.ts:23 - Run 'npm run lint:fix'"

## Cookbook

### JavaScript/TypeScript Projects

- IF: The project has a `package.json` file AND `ENABLE_JAVASCRIPT` is true.
- THEN: Read and execute: `.claude/skills/quality-gate/cookbook/javascript.md`
- EXAMPLES:
  - "run quality gate"
  - "quality check"
  - "check quality before commit"

### Python Projects

- IF: The project has `requirements.txt` or `pyproject.toml` AND `ENABLE_PYTHON` is true.
- THEN: Read and execute: `.claude/skills/quality-gate/cookbook/python.md`
- EXAMPLES:
  - "run quality gate"
  - "verify code quality"
```

**Why this is good**:
- ✅ Explicit frontmatter (trigger, allowed-tools)
- ✅ Clear Purpose paragraph
- ✅ Optional Tip section (non-duplicative setup guidance)
- ✅ Variables with inline comments
- ✅ Workflow with inline examples in every step
- ✅ IF/THEN conditionals clear
- ✅ Cookbook section with IF/THEN/EXAMPLES
- ✅ No duplication
- ✅ No forbidden sections

### Example 2: Good Cookbook Structure

```markdown
# Fork Terminal: Claude Code

Run claude code command in new terminal session.

## Variables

DEFAULT_MODEL: opus       # Default model if not specified
HEAVY_MODEL: opus         # Model for "heavy" tasks
BASE_MODEL: sonnet        # Base/standard model
FAST_MODEL: haiku         # Model for "fast" tasks

## Workflow

1. **Detect Model Request**
   - Check for keywords: "heavy", "fast", "haiku", "sonnet", "opus"
   - Example: "fork terminal use fast claude code" → haiku
   - Example: "fork terminal claude code" → opus (default)

2. **Map to Model**
   - IF: "heavy" requested → Use HEAVY_MODEL (opus)
   - IF: "fast" requested → Use FAST_MODEL (haiku)
   - IF: specific model mentioned → Use that model
   - ELSE: Use DEFAULT_MODEL (opus)

3. **Construct Command**
   - Format: `claude --model <model> -p "<task>" --dangerously-skip-permissions`
   - Always include `--dangerously-skip-permissions` flag
   - Example: `claude --model haiku -p "fix linting errors" --dangerously-skip-permissions`

4. **Execute Fork**
   - Tool: Bash with `.claude/skills/fork-terminal/tools/fork_terminal.sh`
   - Command: `bash .claude/skills/fork-terminal/tools/fork_terminal.sh -c "<command>"`
   - Example: Launches new terminal with claude code running
```

**Why this is good**:
- ✅ Brief purpose statement
- ✅ Cookbook-specific variables
- ✅ Workflow with inline examples
- ✅ Specific tool flags documented
- ✅ IF/THEN conditionals clear
- ✅ Example shows exact format

### Example 3: Bad Structure (Anti-Pattern)

```markdown
---
name: My Skill
description: Does stuff
---

# Purpose

This skill does various things with files and code.

## Quick Reference

- Trigger: auto
- Tools: Read, Bash
- Run with: /my-skill

## Variables

DEBUG_MODE: true

## Workflow

1. **Process Files**
   - Read the files
   - Do some processing

2. **Generate Output**
   - Create output

## Examples

- "process my files"
- "analyze code"

## Notes

- Remember to check the debug mode
- Files are processed in order
```

**Why this is bad**:
- ❌ No trigger in frontmatter (should be explicit)
- ❌ No allowed-tools in frontmatter
- ❌ Vague Purpose paragraph ("various things")
- ❌ Quick Reference section (duplicates info)
- ❌ No inline comments on Variables
- ❌ No inline examples in Workflow steps
- ❌ Vague workflow steps ("Do some processing")
- ❌ Separate Examples section (should be inline)
- ❌ Notes section (should be inline comments)

**How to fix**:
1. Add explicit frontmatter fields
2. Remove Quick Reference section
3. Add inline comments to Variables
4. Add inline examples to every Workflow step
5. Make Workflow steps specific with tool references
6. Remove separate Examples section
7. Move Notes into inline comments on Variables

---

## Pattern Rationale

### Why Single Source of Truth?

**Problem**: Multiple sections describing same information = maintenance burden
- Edit Workflow → must edit Quick Reference
- Edit Variables → must edit Notes
- Edit Examples → must edit inline examples
- 4 places to keep synchronized

**Solution**: One canonical location per piece of information
- Workflow contains all procedures (with inline examples)
- Variables contain all configuration (with inline comments)
- Edit once, done

**Result**: Easier maintenance, no sync errors, clearer structure

### Why Inline Examples?

**Problem**: Separate Examples section divorces examples from context
- See example "analyze code" in Examples section
- Search through Workflow to understand what step it relates to
- Context switching overhead

**Solution**: Example immediately follows the step it demonstrates
- Step description
- Inline example showing that exact step
- No context switching needed

**Result**: Self-documenting workflows, faster comprehension

### Why Explicit Frontmatter?

**Problem**: Defaults can change, assumptions fail
- Assume trigger is manual, but default changes to auto
- Assume all tools allowed, but restriction added
- No documentation of intent

**Solution**: Always explicit, even if current default
- `trigger: manual` explicitly documents intention
- `allowed-tools: [Read, Bash]` shows security restriction
- Reader sees design decisions

**Result**: Self-documenting security posture, clear intent

### Why Bold Step Names?

**Problem**: Dense text walls hard to scan
- 50-line workflow with no visual hierarchy
- Can't quickly find step 3
- Can't see structure at a glance

**Solution**: Bold step names create visual hierarchy
- `**Step Name**` = ~1 token cost
- Massive scan-ability improvement
- Human readers appreciate structure

**Result**: Better UX for minimal cost

---

## Appendix: Common Patterns

### Pattern: Feature Flags

```markdown
## Variables

ENABLE_JAVASCRIPT: true           # Enable JavaScript/TypeScript checks
ENABLE_PYTHON: true               # Enable Python checks
ENABLE_SECURITY: false            # Enable security vulnerability scanning
```

**Use when**: Skill supports multiple optional features

### Pattern: Mode Selection

```markdown
## Variables

OUTPUT_MODE: display              # Options: display, save, both
```

**Use when**: Skill has multiple output strategies

### Pattern: Path Configuration

```markdown
## Variables

CACHE_DIR: .claude/skills/doc-vault/cache              # Where cached docs are stored
INDEX_FILE: .claude/skills/doc-vault/README.md         # Lightweight registry
```

**Use when**: Skill needs configurable file paths

### Pattern: Conditional Routing

```markdown
2. **Route to Handler**
   - IF: package.json exists → cookbook/javascript.md
   - ELSE IF: requirements.txt exists → cookbook/python.md
   - ELSE: Report unsupported project type
   - Example: package.json found → Route to javascript.md
```

**Use when**: Different handlers based on conditions

### Pattern: Tool with Flags

```markdown
3. **Execute Command**
   - Tool: Bash
   - Format: `claude --model <model> -p "<task>" --dangerously-skip-permissions`
   - Always include `--dangerously-skip-permissions` flag
   - Example: `claude --model haiku -p "fix tests" --dangerously-skip-permissions`
```

**Use when**: Specific tool flags must be documented

### Pattern: Pattern Reference Lists

```markdown
5. **Detect Patterns**
   - Frontend: Component frameworks (React/Vue/Svelte), state (Redux/Zustand/Context)
   - Backend: API type (REST/GraphQL/tRPC), server (Express/Fastify)
   - Testing: Framework (Vitest/Jest), E2E (Playwright/Cypress)
   - Example: React + Vitest + Playwright → Modern frontend stack
```

**Use when**: Skill needs domain knowledge condensed for pattern recognition

### Pattern: Example Report

```markdown
8. **Generate Report**
   - Compile all results into formatted report
   - Example report:
     ```
     QUALITY GATE REPORT
     Project: my-app | TypeScript

     STATIC ANALYSIS
       Linting: ✗ FAIL (5 issues)
       Formatting: ✓ PASS
       Type Check: ✗ FAIL (3 errors)

     OVERALL: ✗ FAILED
     ```
```

**Use when**: Skill generates structured output, format must be specified

---

**End of Style Guide**

Next step: Use these standards when creating or editing skills. For assistance, consider building a meta skill that enforces these patterns automatically.
