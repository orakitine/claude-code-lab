# Implement Task Workflow (Generic)

Execute task implementation following specification with automated quality gates and systematic validation.

## Workflow

1. **Discover and Load Task**

   - Use task discovery pattern to find target task file
   - Tool: Glob to search TASK_DIR with user's identifier
   - Support all formats: full ID, short ID, keywords, category, "latest"
   - Example: User says "implement 006" → Find TASK-006 [toImplement] (feat): add-user-authentication-with-jwt.md

2. **Validate Task State**

   - Tool: Read task file and extract [state] from filename
   - Verify state is [toImplement] (expected for implement workflow)
   - IF: state is [toRefine] → Error "Task needs refinement first. Run refine workflow."
   - IF: state is [toImplement] → Proceed with implementation
   - IF: state is [toReview] or [done] → Warn "Already implemented"
   - Example: TASK-006 [toImplement] found → State valid, proceed

3. **Load and Parse Specification**

   - Tool: Read entire task specification file
   - Extract key information: Requirements (Must/Should/Could), Files to modify/create, Architecture changes, Integration points, Acceptance criteria, Testing strategy
   - Validate specification completeness (all sections present and filled)
   - Example: Loaded TASK-006 spec: JWT auth, 3 files to create, 2 to modify, 5 acceptance criteria

4. **Pre-Implementation Safety Checks**

   - IF: ENABLE_LINT → Tool: Bash to run lint command
   - IF: ENABLE_TYPECHECK → Tool: Bash to run typecheck command
   - IF: ENABLE_BUILD → Tool: Bash to run build command
   - IF: ENABLE_TESTS → Tool: Bash to run test command
   - Verify all checks pass before starting implementation
   - Example: Run `npm run lint && npm run typecheck && npm test` → All pass ✓

5. **Plan Implementation Phases**

   - Break implementation into logical phases based on complexity
   - LOW complexity: Single phase (straightforward implementation)
   - MEDIUM complexity: 2-3 phases (setup → core → integration)
   - HIGH complexity: 4+ phases (setup → foundation → features → integration → polish)
   - Identify dependencies between phases (must complete phase N before N+1)
   - Example: MEDIUM complexity → Phase 1: Setup auth infrastructure, Phase 2: Implement login/logout, Phase 3: Integrate with existing components

6. **Execute Implementation Phases**

   - For each phase in planned order:
     - Announce phase: "Phase X of Y: {phase description}"
     - Implement changes: Tool: Write for new files, Tool: Edit for modifications
     - Follow specification precisely: implement exactly what's specified, use patterns/conventions from codebase
     - Validate phase completion: run relevant subset of quality gates
     - Document progress: note any deviations or discoveries
   - Example: Phase 1 complete → Created auth middleware (auth.ts), Added JWT utilities (jwt-utils.ts), Updated types (auth-types.ts)

7. **Continuous Validation**

   - After each significant change or phase:
     - IF: ENABLE_TYPECHECK → Run type checking
     - Check for compilation errors, type mismatches
     - Fix issues before proceeding to next change
   - Example: After creating auth middleware → Run `npm run typecheck` → Fix 2 type errors → Proceed

8. **Integration and Testing**

   - After all phases complete:
     - Verify all Must Have requirements implemented
     - Check Should Have requirements (implement if time permits)
     - Test each acceptance criterion manually
     - Verify integration points work correctly
   - Example: Test JWT generation, token validation, login flow, logout flow, error scenarios → All acceptance criteria met ✓

9. **Final Quality Gates**

   - Run complete quality gate suite:
     - IF: ENABLE_LINT → Tool: Bash run `npm run lint` (or project equivalent)
     - IF: ENABLE_TYPECHECK → Tool: Bash run `npm run typecheck`
     - IF: ENABLE_BUILD → Tool: Bash run `npm run build`
     - IF: ENABLE_TESTS → Tool: Bash run `npm test`
   - ALL gates must pass before transitioning to review
   - IF: Any gate fails → Fix issues and re-run gates
   - Example: All quality gates pass → Implementation validated ✓

10. **Document Implementation**

    - Tool: Edit task file to add implementation notes
    - Document: Files created/modified, Key decisions made during implementation, Any deviations from original spec (and why), Known issues or technical debt, Testing completed
    - Add to Workflow State History section
    - Example: Add note "Implemented JWT auth with 7-day token expiry. Created 3 new files, modified 2 existing. All acceptance criteria met."

11. **Transition State**

    - Tool: Rename file from [toImplement] to [toReview]
    - Old: TASK-006 [toImplement] (feat): add-user-authentication-with-jwt.md
    - New: TASK-006 [toReview] (feat): add-user-authentication-with-jwt.md
    - Example: mv "./tasks/TASK-006 [toImplement] (feat): add-user-authentication-with-jwt.md" "./tasks/TASK-006 [toReview] (feat): add-user-authentication-with-jwt.md"

12. **Generate Implementation Summary**

    - Compile comprehensive summary: Files created (count and list), Files modified (count and list), Quality gate results (all passing), Implementation time estimate, Complexity assessment (was it LOW/MEDIUM/HIGH as estimated?), Next steps (review workflow)
    - Example: "✓ TASK-006 implemented successfully. Created 3 files, modified 2 files. All quality gates passing. State: [toReview]. Next: Run review workflow for comprehensive validation."

## Quality Gates

Automated checks ensure code quality:

### Linting
- IF: ENABLE_LINT is true → Run linting
- Tool: Bash execute project lint command
- Common commands: `npm run lint`, `yarn lint`, `pnpm lint`, `ruff check .` (Python), `golangci-lint run` (Go)
- Ensure zero linting errors before proceeding
- Example: `npm run lint` → 0 errors ✓

### Type Checking
- IF: ENABLE_TYPECHECK is true → Run type checking
- Tool: Bash execute type check command
- Common commands: `npm run typecheck`, `tsc --noEmit`, `mypy .` (Python)
- Ensure zero type errors before proceeding
- Example: `npm run typecheck` → 0 errors ✓

### Build Verification
- IF: ENABLE_BUILD is true → Run build
- Tool: Bash execute build command
- Common commands: `npm run build`, `yarn build`, `python -m build`
- Ensure build completes without errors
- Example: `npm run build` → Build successful (142 KB bundle) ✓

### Test Execution
- IF: ENABLE_TESTS is true → Run test suite
- Tool: Bash execute test command
- Common commands: `npm test`, `yarn test`, `pytest`, `go test ./...`
- Ensure all tests pass, no regressions
- Example: `npm test` → 45 passing, 0 failing ✓

## Error Handling

Handle common implementation issues:

**Quality gate failures**
- Display which gate failed and error details
- Suggest fixes based on error type (linting → run fix command, type errors → add types, test failures → fix logic)
- Allow retry after fixes
- Example: "Linting failed: 3 errors in auth.ts. Run `npm run lint:fix` to auto-fix. Then retry implement workflow."

**Specification ambiguities discovered**
- Note ambiguity encountered
- Make reasonable assumption and document it
- Flag for review workflow to validate assumption
- Example: "Spec unclear on token storage location. Assumed localStorage for browser, flagged for review."

**Integration conflicts**
- If changes conflict with existing code
- Analyze conflict and suggest resolution
- Document conflict resolution in implementation notes
- Example: "Existing auth pattern conflicts with JWT approach. Refactored to support both session and JWT modes."

**Missing dependencies**
- If implementation requires libraries not in spec
- Document additional dependency
- Add to package.json or requirements.txt
- Note in implementation summary
- Example: "Added jsonwebtoken library (not in original spec) for JWT handling."

## Implementation Patterns

Follow project conventions:

**Code Organization**
- Match existing directory structure
- Follow naming conventions in codebase
- Use consistent file organization patterns
- Example: Auth utilities in `/lib/auth/`, types in `/types/auth.ts`

**Error Handling**
- Use project's error handling patterns
- Implement try-catch where appropriate
- Provide meaningful error messages
- Log errors consistently
- Example: Use existing ErrorBoundary pattern for React components

**Testing**
- Write tests matching project's testing patterns
- Follow existing test file naming (*.test.ts, *.spec.ts, test_*.py)
- Use project's testing utilities and helpers
- Aim for reasonable coverage of new code
- Example: Create auth.test.ts using existing test utilities

**Documentation**
- Add code comments for complex logic
- Use JSDoc/docstrings for public APIs
- Update README if user-facing changes
- Document configuration changes
- Example: Add JSDoc comments to JWT utility functions
