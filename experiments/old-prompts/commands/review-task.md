---
description: "Perform comprehensive code reviews with automated quality gates"
args: ["spec-file-name"]
allowed_tools: ["Read", "Edit", "Bash", "Glob", "TodoWrite"]
---

# COMPREHENSIVE CODE REVIEW & APPROVAL WORKFLOW

Target review: $ARGUMENTS

STEP 1: TASK DISCOVERY & VALIDATION

@.claude/patterns/task-discovery.md

**Expected State**: `toReview`
@.claude/patterns/state-validation.md

**Identify implementation scope**:
- Extract list of files that should have been modified
- Review implementation approach from spec
- Identify acceptance criteria for validation
- Note any special testing or performance requirements

STEP 2: AUTOMATED VALIDATION & TESTING
1. **Pre-review validation**:
   - Run `npm run lint` - ensure code style compliance
   - Run `npm run typecheck` - verify TypeScript correctness
   - Run `npm run build` - confirm buildable without errors
   - Run `npm test` - validate all tests pass
   - **HALT review if any automated checks fail**

2. **Git status verification**:
   - Confirm all implementation changes are committed
   - Check for any uncommitted or unstaged changes
   - Validate branch status and recent commits
   - Ensure clean working directory

3. **Performance baseline check**:
   - Check bundle size impact (if applicable)
   - Verify no significant performance regression
   - Test loading speed for UI changes
   - Validate memory usage for complex features

STEP 3: SPECIFICATION COMPLIANCE REVIEW
1. **Requirements verification**:
   - Load original spec and compare with implementation
   - **Systematically check each acceptance criterion**:
     * Mark ✅ for fully implemented criteria
     * Mark ⚠️ for partially implemented criteria  
     * Mark ❌ for missing/incorrect implementation
   - Verify all "Must Have" requirements are implemented
   - Check if "Should Have" features were included

2. **User story validation**:
   - Test the user workflow described in spec
   - Verify the "As a [user], I want [goal] so that [benefit]" story works
   - Check edge cases and error scenarios
   - Validate accessibility compliance

3. **Technical requirements check**:
   - Confirm architecture matches spec decisions
   - Verify integration points work correctly
   - Check error handling implementation
   - Validate security considerations addressed

STEP 4: CODE QUALITY ASSESSMENT
1. **TypeScript & code standards**:
   - Verify strict TypeScript typing throughout
   - Check proper interface definitions
   - Validate error handling patterns
   - Confirm no `any` types or unsafe operations

2. **Architecture compliance**:
   - **Next.js patterns**: Proper App Router usage, server/client components
   - **Component organization**: Follows established `/components` structure  
   - **Constants usage**: Leverages `/lib/constants` appropriately
   - **Utility functions**: Uses existing utilities vs. reinventing

3. **Integration review**:
   - **Modal system**: Proper priority-based modal usage if applicable
   - **Cookie consent**: GDPR compliance maintained if data collected
   - **Analytics tracking**: Events properly implemented if user actions tracked
   - **Responsive design**: Mobile/desktop compatibility verified

STEP 5: MANUAL TESTING & VALIDATION
1. **Functional testing**:
   - Test all primary user workflows
   - Verify error states and edge cases
   - Check loading states and async operations
   - Validate form submissions and data handling

2. **Cross-browser & device testing**:
   - Test on desktop (Chrome, Firefox, Safari)
   - Test on mobile devices (iOS Safari, Android Chrome)
   - Verify responsive breakpoints work correctly
   - Check accessibility with screen readers

3. **Performance testing**:
   - Check page load times
   - Verify smooth animations and interactions
   - Test under slow network conditions
   - Validate bundle size impact

STEP 6: DOCUMENTATION & SECURITY REVIEW
1. **Documentation standards**:
   - Verify complex logic is documented with comments
   - Check JSDoc comments for public APIs
   - Confirm README updated if needed
   - Validate type definitions are complete

2. **Security assessment**:
   - Check for exposed sensitive data
   - Verify input validation and sanitization
   - Confirm no security vulnerabilities introduced
   - Validate HTTPS and security headers

3. **Maintenance considerations**:
   - Code is readable and maintainable
   - Patterns are consistent with existing codebase
   - Dependencies are justified and secure
   - Future extensibility considered

STEP 7: REVIEW DECISION & STATE TRANSITION
1. **Compile review results**:
   - Summarize all findings with specific examples
   - Categorize issues by severity (Critical/Major/Minor/Suggestion)
   - Provide actionable feedback for any problems found
   - Document positive aspects and good implementations

2. **Make review decision**:
   - **✅ APPROVED**: All criteria met, ready for production
     * Execute state transition: `[toReview]` → `[done]`
     * Update task file with approval timestamp and reviewer notes
   - **🔄 NEEDS REVISION**: Minor issues require fixes
     * Keep in `[toReview]` state, document specific changes needed
     * Set up for re-review after fixes applied
   - **❌ REQUIRES CHANGES**: Major issues, back to implementation
     * Transition back to `[toImplement]` state for re-implementation
     * Document all critical issues that must be addressed

3. **Generate comprehensive review report**:
   - Summary of review scope and methodology
   - Detailed findings with file locations and line numbers
   - Checklist of all acceptance criteria with status
   - Performance and security assessment results
   - Next steps and timeline for any required changes

@.claude/shared/constants.md

ENHANCED REVIEW FEATURES:
- **Intelligent Task Discovery**: Same fuzzy matching as other commands
- **Automated Quality Gates**: Full test/lint/build validation before review
- **Systematic Compliance Check**: Each acceptance criterion individually validated
- **Multi-dimensional Assessment**: Code, performance, security, documentation
- **Professional Review Report**: Detailed findings with actionable feedback
- **State-aware Workflow**: Proper transitions based on review outcomes

EXAMPLE USAGE SCENARIOS:
- `/review-task BROOKLY-006` (finds BROOKLY-006 [toReview])
- `/review-task 6` (short ID lookup)
- `/review-task design theme` (keywords)
- `/review-task latest` (most recent [toReview] task)