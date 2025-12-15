---
description: "Execute implementation following established patterns and quality gates"
args: ["spec-file-name"]
allowed_tools: ["Read", "Edit", "MultiEdit", "Write", "Bash", "Glob", "TodoWrite"]
---

# COMPREHENSIVE IMPLEMENTATION WORKFLOW

Target implementation: $ARGUMENTS

STEP 1: TASK DISCOVERY & VALIDATION

@.claude/patterns/task-discovery.md

**Expected State**: `toImplement`
@.claude/patterns/state-validation.md

**Pre-implementation validation**:
- Load and parse spec content
- Check spec has all required sections completed
- Verify acceptance criteria are testable
- Ensure technical requirements are clear
- **Confirm readiness**: Spec must be complete before implementation

STEP 2: ENVIRONMENT & SAFETY CHECKS
1. **Git status validation**:
   - Ensure working directory is clean (no uncommitted changes)
   - Confirm on appropriate branch for this work
   - Suggest creating feature branch if needed

2. **Project health check**:
   - Run `npm run lint` to ensure starting point is clean
   - Run build/typecheck to verify current state
   - Check all tests pass before making changes

3. **Create implementation backup**:
   - Document current state of files that will be modified
   - Create git stash if there are any uncommitted changes

STEP 3: IMPLEMENTATION STRATEGY & PLANNING
1. **Analyze spec complexity**:
   - Categorize as LOW/MEDIUM/HIGH complexity
   - Identify implementation phases (e.g., setup → core → testing → integration)
   - Determine file dependencies and modification order

2. **Review architecture patterns**:
   - Check `/docs` for relevant architectural decisions
   - Review existing similar implementations in codebase
   - Identify reusable patterns and utilities

3. **Plan implementation approach**:
   - Break down into logical phases
   - Identify potential challenges early
   - Plan testing strategy for each phase

STEP 4: SYSTEMATIC IMPLEMENTATION EXECUTION
1. **Phase-by-phase implementation**:
   - Implement one logical unit at a time
   - Test each phase before moving to next
   - Follow established project conventions:
     * Next.js 15 App Router structure
     * TypeScript strict typing
     * Shadcn/ui vs custom component patterns
     * Constants structure in `/lib/constants/`
     * Modal management and cookie consent integration

2. **Continuous validation**:
   - Run TypeScript compilation after each major change
   - Execute relevant tests frequently
   - Validate browser functionality for UI changes
   - Check performance impact for complex changes

3. **Error handling & resilience**:
   - Implement proper error boundaries
   - Add loading states for async operations
   - Follow accessibility best practices
   - Ensure graceful degradation

STEP 5: COMPREHENSIVE TESTING & VALIDATION
1. **Automated testing**:
   - Run full test suite: `npm test`
   - Execute linting: `npm run lint`
   - Perform type checking: `npm run typecheck`
   - Run build process: `npm run build`

2. **Manual testing**:
   - Test all acceptance criteria from spec
   - Verify integration with existing features
   - Check responsive design (mobile/desktop)
   - Validate accessibility compliance

3. **Performance validation**:
   - Check bundle size impact
   - Verify loading performance
   - Test under various network conditions

STEP 6: DOCUMENTATION & STATE TRANSITION
1. **Code documentation**:
   - Document complex business logic
   - Add JSDoc comments for public APIs
   - Update type definitions if needed
   - Follow established documentation patterns

2. **Update project documentation**:
   - Update README if new features added
   - Add to architecture docs if significant changes
   - Document any new environment variables or setup

3. **Execute state transition**: Rename file from `[toImplement]` to `[toReview]`
   - Example: `BROOKLY-006 [toImplement] (design): theme.md` → `BROOKLY-006 [toReview] (design): theme.md`
   - Indicates implementation is complete and ready for review

4. **Implementation summary**:
   - List all files created/modified
   - Summarize key changes made
   - Document any deviations from original task
   - Provide testing instructions for validation
   - **Confirm next step**: Task is now ready for `/review-task`

ENHANCED IMPLEMENTATION FEATURES:
- **Intelligent Spec Discovery**: Same fuzzy matching as refine-task
- **Phase-based Implementation**: Logical breakdowns instead of all-at-once
- **Continuous Validation**: Testing at each phase, not just at end
- **Safety Features**: Git checks, backups, rollback capabilities
- **Automated Quality Gates**: Lint, typecheck, build, test validation
- **Comprehensive Documentation**: Clear standards and expectations

@.claude/shared/constants.md

EXAMPLE USAGE SCENARIOS:
- `/implement-task BROOKLY-006` (finds BROOKLY-006 [toImplement])
- `/implement-task 6` (short ID lookup)
- `/implement-task design theme` (keywords)
- `/implement-task latest` (most recent [toImplement] task)