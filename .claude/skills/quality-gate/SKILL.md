---
name: Quality Gate Skill
description: Comprehensive code quality verification workflow that checks linting, formatting, type safety, tests, and build before committing code. Non-destructive - only reports issues without making changes.
---

# Purpose

Run a comprehensive Quality Gate check on the current project to verify code quality before committing. This includes static analysis, testing, build verification, and security checks.

Follow the `Instructions`, execute the `Workflow`, based on the `Cookbook`.

## Variables

ENABLE_JAVASCRIPT: true
ENABLE_PYTHON: true
ENABLE_SECURITY_CHECK: true
SUPPORTED_PROJECT_TYPES: javascript, typescript, python

## Instructions

- Based on the project type detected, follow the `Cookbook` to determine which workflow to use.
- **Non-destructive:** This skill ONLY reports issues. It does NOT auto-fix anything.
- **Continue on failure:** If one phase fails, continue to other phases to get complete picture.
- **Informative:** Provide specific file paths and line numbers when possible.
- **Actionable:** Suggest specific commands to fix issues.

## Workflow

1. Understand the user's request to run quality checks.
2. Detect the project type by checking for indicator files (package.json, requirements.txt, etc.).
3. Follow the `Cookbook` to determine which quality check workflow to execute.
4. Execute all phases of the quality check.
5. Generate a comprehensive report with results and recommendations.

## Cookbook

### JavaScript/TypeScript Projects

- IF: The project has a `package.json` file AND `ENABLE_JAVASCRIPT` is true.
- THEN: Read and execute: `.claude/skills/quality-gate/cookbook/javascript.md`
- EXAMPLES:
  - "run quality gate"
  - "quality check"
  - "check quality before commit"
  - "run all checks"

### Python Projects

- IF: The project has `requirements.txt` or `pyproject.toml` AND `ENABLE_PYTHON` is true.
- THEN: Read and execute: `.claude/skills/quality-gate/cookbook/python.md`
- EXAMPLES:
  - "run quality gate"
  - "quality check"
  - "verify code quality"

### Generic Projects

- IF: No specific project type detected.
- THEN: Run basic checks available in the project and report.
- EXAMPLES:
  - "run quality gate"
  - "check what we can"
