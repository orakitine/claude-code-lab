# /bowser:hop-automate Command (Summary from Bowser)

## Purpose

Higher-order prompt (HOP) that runs saved browser automation workflows. Think of it like a function that takes another function as a parameter — the consistent pieces (setup, teardown, reporting) go in the HOP, and the specific workflow goes in the argument.

## Parameters

- WORKFLOW (required): automation file name (without .md extension)
- SKILL: playwright-bowser | claude-bowser (default: playwright-bowser)
- MODE: headed | headless (default: headed)
- VISION: true | false (default: false)
- PROMPT: custom text injected into the workflow

## 4-Phase Workflow

### Phase 1: Parse & Validate
- If no arguments: list available workflows
- Validate the specified workflow file exists in `.claude/commands/bowser/`

### Phase 2: Load Workflow
- Read workflow file's frontmatter for default settings
- Command-line arguments override frontmatter defaults

### Phase 3: Execute
- Call `/playwright-bowser` or `/claude-bowser` with resolved config
- Pass workflow content + PROMPT as the task

### Phase 4: Report
- Return which workflow ran, skill used, and results

## Key Pattern: Higher-Order Prompt

Keywords are detected case-insensitively from arguments:
- "playwright" / "chrome" → sets SKILL
- "headed" / "headless" → sets MODE
- "vision" → sets VISION
- Remaining text → becomes PROMPT
