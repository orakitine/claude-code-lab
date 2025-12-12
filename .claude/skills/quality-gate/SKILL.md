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

## Variables

ENABLE_JAVASCRIPT: true           # Enable JavaScript/TypeScript quality checks
ENABLE_PYTHON: true                # Enable Python quality checks
ENABLE_SECURITY_CHECK: true        # Enable security vulnerability scanning
SUPPORTED_PROJECT_TYPES: javascript, typescript, python  # Currently supported project types

## Workflow

1. **Parse User Request**
   - Identify quality check intent
   - User triggers: "run quality gate", "quality check", "check quality before commit", "verify code quality"
   - Example: "run quality gate" → Intent: comprehensive quality checks

2. **Detect Project Type**
   - Check for indicator files: package.json (JS/TS), requirements.txt/pyproject.toml (Python)
   - Determines which cookbook workflow to use
   - Example: package.json found → JavaScript/TypeScript project

3. **Route to Cookbook**
   - Based on detected type and ENABLE flags
   - JavaScript/TypeScript: IF package.json AND ENABLE_JAVASCRIPT → javascript.md
   - Python: IF requirements.txt/pyproject.toml AND ENABLE_PYTHON → python.md
   - Generic: IF no match → Run basic checks available in project
   - Example: TypeScript project + ENABLE_JAVASCRIPT=true → Route to cookbook/javascript.md

4. **Execute Quality Checks**
   - Run all check phases defined in cookbook (linting, formatting, type checking, tests, build)
   - IMPORTANT: Non-destructive - only report issues, never auto-fix
   - Continue on failure - run all phases even if some fail (get complete picture)
   - Example: Run lint → Run format check → Run type check → Run tests → Run build

5. **Generate Report**
   - Compile results from all phases
   - Include: specific file paths, line numbers when possible, error messages, actionable fix commands
   - Format: Clear sections per phase (✓ passed, ✗ failed), summary at end
   - Example: "Linting: ✗ 5 errors in src/utils.ts:23, src/App.tsx:45 - Run 'npm run lint:fix'"

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
