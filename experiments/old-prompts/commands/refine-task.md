---
description: "Conduct systematic requirements interviews for task specifications"
args: ["spec-file-name"]
allowed_tools: ["Read", "Edit", "Glob", "TodoWrite"]
---

# INTELLIGENT SPEC FILE REFINEMENT PROCESS

Target task file: $ARGUMENTS

STEP 1: TASK DISCOVERY & VALIDATION

@.claude/patterns/task-discovery.md

**Expected State**: `toRefine`
@.claude/patterns/state-validation.md

STEP 2: COMPREHENSIVE SPEC ANALYSIS

1. **Load and parse** the confirmed spec file
2. **Analyze completeness** across all sections:
   - Missing or vague requirements
   - Unclear acceptance criteria
   - Ambiguous technical specifications
   - Missing integration details
   - Insufficient testing approach
   - Vague user experience goals

3. **Categorize gaps** by implementation impact and effort to resolve

STEP 3: INTELLIGENT INTERVIEW PROCESS

1. **Present analysis summary** with prioritized question categories
2. **Conduct systematic interview** following this flow:
   - Ask ONE question at a time
   - Explain WHY each question is critical
   - Show progress indicator (Question X of Y)
   - Allow user to skip/defer non-critical questions
   - Update spec file after each answer
   - Validate answers make sense in context

3. **Track interview progress** and allow resumption if interrupted

QUESTION CATEGORIES (by priority):

1. **Critical Implementation Blockers** - Missing info that prevents coding
2. **User Experience & Business Goals** - What success looks like
3. **Technical Integration** - How this connects to existing systems
4. **Design & Visual Requirements** - Specific aesthetic needs
5. **Performance & Constraints** - Technical limitations
6. **Testing & Validation** - How to verify it works

STEP 4: COMPLETION & STATE TRANSITION

1. **Review all updates** made to spec file
2. **Validate consistency** across all sections
3. **Confirm readiness** for implementation
4. **Execute state transition**: Rename file from `[toRefine]` to `[toImplement]`
   - Example: `BROOKLY-006 [toRefine] (design): theme.md` → `BROOKLY-006 [toImplement] (design): theme.md`
5. **Generate summary** of all changes made
6. **Confirm next step**: Task is now ready for `/implement-task`

ENHANCED USER EXPERIENCE FEATURES:

- **Fuzzy File Matching**: `/refine-task 6` finds BROOKLY-006
- **Interactive Selection**: Multiple matches show numbered list
- **Progress Tracking**: Visual progress through interview
- **Skip Options**: Allow deferring non-critical questions
- **Auto-Backup**: Original file preserved before changes
- **Change Summary**: Clear list of all modifications made

@.claude/shared/constants.md

EXAMPLE USAGE SCENARIOS:

- `/refine-task BROOKLY-006` (finds BROOKLY-006 [toRefine])
- `/refine-task 6` (short ID lookup)
- `/refine-task design theme` (keywords)
- `/refine-task (design)` (category filter)
- `/refine-task latest` (most recent [toRefine] task)
