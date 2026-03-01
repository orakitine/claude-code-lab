# Browser Automation Workflow Runner

## Purpose

Higher-order prompt that executes saved browser automation workflows from `.claude/commands/bowser/` with consistent setup, teardown, and reporting. Think of this as a function that takes a workflow as a parameter.

## Variables

WORKFLOW: ""                               # Workflow file name (without .md extension)
MODE: headless                             # Options: headed, headless
VISION: false                              # Enable vision mode for screenshots in context
PROMPT: ""                                 # Additional text to inject into the workflow

## Workflow

1. **Parse Arguments**
   - First argument → WORKFLOW name
   - Scan remaining arguments for keywords (case-insensitive):
   - IF: "headed" found → set MODE=headed
   - IF: "headless" found → set MODE=headless
   - IF: "vision" found → set VISION=true
   - Remaining text → set PROMPT
   - Example: `/bowser:hop-automate blog-summarizer https://example.com headed` → WORKFLOW=blog-summarizer, MODE=headed, PROMPT="https://example.com"

2. **Validate Workflow**
   - IF: no WORKFLOW specified → list available workflows from `.claude/commands/bowser/` and return
   - Check file exists: `.claude/commands/bowser/<WORKFLOW>.md`
   - IF: file not found → report error with available workflow names
   - Example: `/bowser:hop-automate` → "Available workflows: blog-summarizer, amazon-add-to-cart"
   - Tool: Glob `.claude/commands/bowser/*.md`

3. **Load Workflow**
   - Read the workflow file
   - IF: file has YAML frontmatter → extract defaults for MODE, VISION
   - Command-line arguments override frontmatter defaults
   - IF: PROMPT is set → inject it into the workflow content
   - Example: workflow file says `mode: headed` but args say "headless" → use headless
   - Tool: Read `.claude/commands/bowser/<WORKFLOW>.md`

4. **Execute Workflow**
   - Activate the `/playwright-browser` skill
   - IF: MODE is headed → set HEADED=true
   - IF: VISION is true → set VISION=true
   - Run the loaded workflow content with the playwright-browser skill
   - Create output directory: `./browser-automations/<WORKFLOW>_<timestamp>/`
   - Save any screenshots/artifacts to output directory
   - Tool: Bash (mkdir), then execute skill workflow

5. **Report Results**
   - Summarize: which workflow ran, mode used, outcome
   - Include: output directory path, screenshot list, any errors
   - Example:
     ```
     WORKFLOW COMPLETE
     Workflow: blog-summarizer
     Mode: headless
     Output: ./browser-automations/blog-summarizer_2026-03-01_19-30/
     Result: Successfully summarized 1 blog post
     ```
