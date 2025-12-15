---
description: "Create detailed task specifications with codebase analysis"
args: ["description"]
allowed_tools: ["Read", "LS", "Glob", "Write", "TodoWrite"]
---

# CODEBASE-AWARE TASK SPECIFICATION GENERATOR

Task to analyze: $ARGUMENTS

STEP 1: TASK ID GENERATION

1. **Determine conventional commit category** based on description:
   - "new feature", "add", "create" → **feat**
   - "improve", "enhance", "optimize" → **enhance**
   - "design", "styling", "colors", "UI", "theme" → **design**
   - "fix", "bug", "error", "issue" → **fix**
   - "lint", "format", "code quality", "refactor" → **refactor**
   - "test", "testing" → **test**
   - "docs", "documentation", "content" → **docs**
   - "location", "service area" → **feat** (location features)
   - "service", "cleaning" → **feat** (service features)
   - Default fallback → **chore**

2. **Scan `/tasks` folder** for all existing BROOKLY-### files
3. **Auto-increment sequentially**: Find highest BROOKLY number and increment by 1
   - Example: If BROOKLY-005 exists, create BROOKLY-006
   - Format: `BROOKLY-###` (3-digit zero-padded)

4. **Generate filename with [toRefine] state**: `BROOKLY-### [toRefine] (category): task-name-slug.md`
   - Example: `BROOKLY-006 [toRefine] (feat): add-booking-modal.md`
   - [toRefine] indicates task needs requirements clarification before implementation

STEP 2: CODEBASE ANALYSIS
Before creating specification, analyze the existing codebase:

1. **Identify relevant existing files** based on the task:
   - Home page tasks → examine `src/app/page.tsx`
   - Component tasks → check `src/components/`
   - Service tasks → review `src/lib/constants/services.ts`
   - Styling tasks → look at existing CSS/Tailwind usage

2. **Read and understand current implementation**:
   - What components already exist?
   - What's the current structure and functionality?
   - What patterns are being used?
   - What might need modification vs. replacement?

3. **Reference project documentation**:
   - Check `/docs` for relevant architectural decisions
   - Review CLAUDE.md for established patterns
   - Understand existing systems (modals, analytics, etc.)

STEP 3: INTELLIGENT SPECIFICATION CREATION
Based on the analysis above, create this specification:

# Task Specification: [TASK-TITLE-FROM-USER-INPUT]

## Current State Analysis

### Existing Implementation

- **Current files involved**: [List actual files found during analysis]
- **Current functionality**: [Describe what exists now based on file reads]
- **Current structure**: [Explain existing architecture from codebase]
- **Existing patterns used**: [Reference actual patterns found in code]

### Gap Analysis

- **What works well**: [Identify good existing elements from analysis]
- **What needs improvement**: [Specific issues found in current code]
- **What's missing**: [Functionality gaps identified]

## Overview

- **Task ID**: BROOKLY-### (category) (auto-generated from steps above)
- **Priority**: [HIGH/MEDIUM/LOW based on business impact assessment]
- **Estimated Complexity**: [LOW/MEDIUM/HIGH based on codebase analysis]
- **Dependencies**: [List actual files and systems found during analysis]

## Description

[Detailed explanation combining user input with current state analysis findings]

## User Story

As a [website visitor/business owner/developer - determine from context], I want [extract core functionality from user input] so that [determine benefit based on business context].

## Technical Requirements

### Must Have

- [Core requirements based on existing code analysis and user needs]

### Should Have

- [Enhancements that build on existing patterns found in codebase]

### Could Have

- [Advanced features that extend current implementation without breaking it]

## Implementation Approach

### Files to Modify

- [List ACTUAL existing files that need changes - from codebase analysis]

### Files to Create

- [New files needed, following existing patterns discovered]

### Architecture Changes

- [Specific changes based on current structure analysis]

### Integration Points

- [How this connects to ACTUAL existing systems found during analysis]

## Acceptance Criteria

- [ ] [Testable criteria based on current implementation analysis]
- [ ] [Criteria that respect existing functionality discovered]
- [ ] [Performance criteria if applicable]
- [ ] [Accessibility criteria if UI changes]

## Migration Strategy

- [How to transition from current state to desired state without breaking existing features]
- [What existing functionality to preserve based on analysis]

## Potential Challenges

- [Challenges specific to existing codebase found during analysis]
- [Integration issues with current systems discovered]

## Testing Strategy

- [Testing approach for modified existing components]
- [Verification that existing functionality still works]
- [New feature testing requirements]

## References

- [Link to ACTUAL /docs files that are relevant to this task]
- [Reference ACTUAL existing code files analyzed]

@.claude/shared/constants.md

**EXECUTION STEPS:**

1. Generate task ID using sequential BROOKLY-### numbering and category detection above
2. Create specification following this template
3. **AUTOMATICALLY SAVE** the task file to `/tasks/BROOKLY-### [toRefine] (category): task-name-slug.md`
4. Confirm file was created successfully
5. Remind user to run `/refine-task` to clarify requirements before implementation

**FILENAME EXAMPLES:**

- `/tasks/BROOKLY-006 [toRefine] (feat): add-booking-modal.md`
- `/tasks/BROOKLY-007 [toRefine] (design): update-color-scheme.md`
- `/tasks/BROOKLY-008 [toRefine] (fix): repair-navigation-bug.md`
