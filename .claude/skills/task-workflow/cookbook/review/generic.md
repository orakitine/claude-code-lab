# Review Task Workflow (Generic)

Perform comprehensive code review with automated validation, specification compliance, and quality assessment.

## Workflow

1. **Discover and Load Task**

   - Use task discovery pattern to find target task file
   - Tool: Glob to search TASK_DIR with user's identifier
   - Support all formats: full ID, short ID, keywords, category, "latest"
   - Example: User says "review 006" → Find TASK-006 [toReview] (feat): add-user-authentication-with-jwt.md

2. **Validate Task State**

   - Tool: Read task file and extract [state] from filename
   - Verify state is [toReview] (expected for review workflow)
   - IF: state is [toRefine] or [toImplement] → Error "Task not yet implemented. Complete implement workflow first."
   - IF: state is [toReview] → Proceed with review
   - IF: state is [done] → Warn "Already reviewed and approved"
   - Example: TASK-006 [toReview] found → State valid, proceed

3. **Load Specification and Implementation**

   - Tool: Read task specification file
   - Extract: Requirements, Acceptance criteria, Files to modify/create list, Testing strategy, Implementation notes (if any)
   - Identify scope of review: which files to examine, what to validate
   - Example: TASK-006 requires 3 new files, 2 modified files, 5 acceptance criteria to verify

4. **Run Automated Quality Gates**

   - Execute all enabled quality gates (must pass before manual review)
   - IF: ENABLE_LINT → Tool: Bash run linting
   - IF: ENABLE_TYPECHECK → Tool: Bash run type checking
   - IF: ENABLE_BUILD → Tool: Bash run build
   - IF: ENABLE_TESTS → Tool: Bash run tests
   - IF: Any gate fails → HALT review, return to implement workflow for fixes
   - Example: Run all gates → lint ✓, typecheck ✓, build ✓, tests (45 passing) ✓

5. **Verify Specification Compliance**

   - Systematically check each acceptance criterion
   - For each criterion:
     - Tool: Read relevant implementation files
     - Verify criterion is fully met
     - Mark: ✅ Fully implemented, ⚠️ Partially implemented, ❌ Not implemented/incorrect
     - Document evidence (file:line references)
   - Example: Criterion "JWT tokens expire after 7 days" → Check jwt-utils.ts:42 → ✅ Verified (expiresIn: '7d')

6. **Code Quality Assessment**

   - Review implementation files for quality
   - Check: Code organization (logical structure, proper modules), Naming conventions (clear, consistent names), Error handling (try-catch, validation, meaningful errors), Type safety (proper types, no `any`), Documentation (comments on complex logic, public API docs)
   - Rate each aspect: Excellent, Good, Needs Improvement, Poor
   - Example: Code organization: Good, Naming: Excellent, Error handling: Needs Improvement (missing validation in login route)

7. **Architecture and Pattern Review**

   - Verify implementation follows project architecture
   - Check: Proper separation of concerns, Consistent with existing patterns, Appropriate abstraction levels, No unnecessary complexity, Maintainability considerations
   - Flag architectural issues or deviations
   - Example: Auth middleware properly separates concerns ✓, Follows existing middleware pattern ✓, Could extract token validation to separate util (minor suggestion)

8. **Security Review**

   - IF: Implementation involves authentication, data handling, or external inputs
   - Check for: Input validation and sanitization, SQL injection vulnerabilities, XSS vulnerabilities, CSRF protection, Secure password/token storage, Proper authentication/authorization, Data exposure risks
   - Example: ✓ Passwords hashed with bcrypt, ✓ JWT tokens properly signed, ⚠️ No rate limiting on login endpoint (suggest adding)

9. **Performance Assessment**

   - Evaluate performance impact
   - Check for: Unnecessary re-renders or re-computations, Inefficient algorithms or queries, Memory leaks, Proper caching, Bundle size impact
   - Rate impact: Positive, Neutral, Minor Negative, Major Negative
   - Example: Performance impact: Neutral. JWT validation adds ~5ms per request (acceptable). Bundle size +12KB (reasonable).

10. **Testing Validation**

    - Verify testing completeness
    - Check: All critical paths have tests, Edge cases covered, Error scenarios tested, Integration points tested
    - Run tests and verify: All tests pass, Coverage meets project standards, Tests are meaningful (not just for coverage)
    - Example: Tests cover login, logout, token validation, expiry. Missing: concurrent login test. Coverage: 87% (good).

11. **Documentation Review**

    - Verify documentation completeness
    - Check: Complex logic has code comments, Public APIs have JSDoc/docstrings, README updated if needed, Configuration changes documented
    - Example: ✓ JWT utils documented, ✓ Auth middleware commented, ❌ Missing README update for new auth flow (needs addition)

12. **Compile Review Report**

    - Create comprehensive review summary
    - Sections: Overall assessment, Automated quality gates results, Specification compliance (criterion by criterion), Code quality findings, Security assessment, Performance evaluation, Testing validation, Issues found (categorized by severity)
    - Example: "Overall: APPROVED with minor suggestions. 5/5 acceptance criteria met. Code quality: Good. 1 minor security suggestion (rate limiting). 1 documentation gap (README)."

13. **Make Review Decision**

    - Based on findings, decide outcome
    - IF: All acceptance criteria met AND no critical/major issues → APPROVED
    - IF: Minor issues found → APPROVED with suggestions (proceed to done)
    - IF: Major issues found → NEEDS REVISION (keep in toReview, document changes needed)
    - IF: Critical issues found → REQUIRES RE-IMPLEMENTATION (back to toImplement)
    - Example: APPROVED with suggestions → Minor items can be addressed in future tasks

14. **Transition State (if approved)**

    - Tool: Rename file from [toReview] to [done]
    - Old: TASK-006 [toReview] (feat): add-user-authentication-with-jwt.md
    - New: TASK-006 [done] (feat): add-user-authentication-with-jwt.md
    - Tool: Edit file to add review notes and completion timestamp
    - Example: mv to [done], add "Reviewed 2025-12-13. Approved with minor suggestions. See review notes for improvement opportunities."

15. **Generate Review Report**

    - Provide detailed review findings
    - Include: Summary of decision, All checked items with status, Issues found with severity and suggestions, Performance metrics, Security findings, Testing assessment, Next steps (if any)
    - Example: "✓ TASK-006 APPROVED. All criteria met. Minor suggestions: add rate limiting, update README. State: [done]. No blockers, task complete."

## Review Decision Criteria

Clear guidelines for review outcomes:

### APPROVED ✅
- All Must Have acceptance criteria fully met
- No critical or major security issues
- Code quality meets project standards
- Tests pass and coverage adequate
- No blocking architectural problems
- Minor issues acceptable (document as suggestions)
- **Action**: Transition to [done], task complete

### APPROVED with Suggestions ✅⚠️
- All acceptance criteria met
- Minor improvements identified but not blocking
- Code works correctly but could be enhanced
- Small documentation gaps
- **Action**: Transition to [done], create follow-up tasks for suggestions if desired

### NEEDS REVISION 🔄
- Most criteria met but 1-2 gaps remain
- Major issues that need fixing
- Code quality below standards in key areas
- Missing important tests
- **Action**: Keep in [toReview], document required changes, re-review after fixes

### REQUIRES RE-IMPLEMENTATION ❌
- Critical acceptance criteria not met
- Fundamental architectural problems
- Major security vulnerabilities
- Implementation doesn't match specification
- **Action**: Transition back to [toImplement], document issues, re-implement

## Issue Severity Levels

Categorize findings appropriately:

**Critical (Blocks approval)**
- Security vulnerabilities
- Specification requirements not met
- Broken functionality
- Data loss risks
- Example: "Critical: Passwords stored in plain text"

**Major (Should fix before approval)**
- Significant code quality issues
- Missing important tests
- Performance problems
- Accessibility violations
- Example: "Major: No error handling in auth middleware"

**Minor (Fix if time permits)**
- Code style inconsistencies
- Missing optional features
- Small optimization opportunities
- Documentation gaps
- Example: "Minor: Could add more descriptive variable names"

**Suggestion (Future improvement)**
- Refactoring opportunities
- Enhancement ideas
- Alternative approaches
- Nice-to-have features
- Example: "Suggestion: Consider adding social login in future"

## Review Checklist

Systematic checklist for comprehensive review:

### Functionality ✓
- [ ] All Must Have requirements implemented
- [ ] Should Have requirements implemented (or documented why not)
- [ ] Features work as specified
- [ ] Edge cases handled
- [ ] Error scenarios handled gracefully

### Code Quality ✓
- [ ] Code is readable and maintainable
- [ ] Naming conventions followed
- [ ] No code duplication
- [ ] Proper separation of concerns
- [ ] Comments on complex logic

### Testing ✓
- [ ] All tests pass
- [ ] Critical paths tested
- [ ] Edge cases tested
- [ ] Integration points tested
- [ ] Coverage meets standards

### Security ✓
- [ ] Input validation implemented
- [ ] Authentication/authorization correct
- [ ] No sensitive data exposed
- [ ] Secure defaults used
- [ ] Vulnerabilities addressed

### Performance ✓
- [ ] No obvious performance issues
- [ ] Efficient algorithms used
- [ ] Caching implemented where appropriate
- [ ] Bundle size acceptable
- [ ] Memory usage reasonable

### Documentation ✓
- [ ] Complex logic documented
- [ ] Public APIs documented
- [ ] README updated if needed
- [ ] Configuration documented
- [ ] Migration notes if applicable

### Architecture ✓
- [ ] Follows project patterns
- [ ] Proper abstraction levels
- [ ] Integration done correctly
- [ ] Extensibility considered
- [ ] No unnecessary complexity
