---
name: Project Context Analyzer
description: Analyzes project structure, dependencies, and patterns to generate comprehensive context documentation. Helps understand unfamiliar codebases quickly.
---

# Purpose

Analyze a project's structure, dependencies, framework, and patterns to generate a comprehensive context document. This helps with onboarding, understanding unfamiliar codebases, and providing context to other AI agents.

Follow the `Instructions`, execute the `Workflow`, based on the `Cookbook`.

## Variables

ENABLE_JAVASCRIPT: true
ENABLE_PYTHON: false
ENABLE_GO: false
OUTPUT_MODE: display  # "display" or "save"
OUTPUT_FILE: .project-context.md
SUPPORTED_PROJECT_TYPES: javascript, typescript

## Instructions

- Based on the project type detected, follow the `Cookbook` to determine which analysis workflow to use.
- Use the custom tools in `tools/` directory to perform specialized analysis.
- Output mode can be controlled by user request:
  - "analyze project" or "show me project context" → display mode
  - "generate project context and save" → save mode (creates .project-context.md)
- Provide comprehensive but concise analysis.
- Focus on what's most important for understanding the project quickly.

## Workflow

1. Understand the user's request to analyze the project.
2. Detect the project type using the `detect_framework` tool.
3. Follow the appropriate `Cookbook` based on project type.
4. Call analysis tools in sequence to gather information.
5. Aggregate results and generate formatted report.
6. Display or save based on user request.

## Cookbook

### JavaScript/TypeScript Projects

- IF: The project has a `package.json` file AND `ENABLE_JAVASCRIPT` is true.
- THEN: Read and execute: `.claude/skills/project-context/cookbook/javascript.md`
- EXAMPLES:
  - "analyze this project"
  - "generate project context"
  - "what is this project about"
  - "show me project context"
  - "generate project context and save it"

### Unknown Project Type

- IF: No specific project type detected.
- THEN: Perform basic analysis using available built-in tools (Glob, Read).
- Report what can be detected and suggest adding Python/Go support in the future.
