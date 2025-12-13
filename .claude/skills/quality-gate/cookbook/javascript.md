# JavaScript/TypeScript Quality Gate

Comprehensive quality checks for JavaScript and TypeScript projects. Non-destructive - reports issues only. Uses parallel agent execution for maximum speed.

## Variables

ENABLE_PARALLEL_EXECUTION: true       # Use swarm pattern for parallel checks (faster)
MAX_PARALLEL_AGENTS: 6                # Maximum agents to run simultaneously

## Workflow

1. **Detect Available Tools**
   - Tool: Read package.json to check available scripts and installed tools
   - Look for: lint, format:check, type-check, test, build scripts
   - Determine which checks can run based on available tooling
   - Example: {scripts: {lint: "eslint .", test: "vitest run", build: "vite build"}} → Can run lint, test, build checks

2. **Launch Parallel Quality Check Swarm**
   - IF: ENABLE_PARALLEL_EXECUTION is true → Launch all checks as parallel background agents
   - Tool: Task with run_in_background: true for each check
   - Agents to spawn (based on available tools):
     - Agent "Linter": IF lint script exists → Run `npm run lint`
     - Agent "Formatter": IF format:check exists → Run `npm run format:check` ELSE IF prettier installed → Run `npx prettier --check "src/**/*.{ts,tsx,js,jsx}"`
     - Agent "TypeChecker": IF type-check exists → Run `npm run type-check` ELSE IF tsconfig.json → Run `npx tsc --noEmit`
     - Agent "Tester": IF test script exists → Run `npm test`
     - Agent "Builder": IF build script exists → Run `npm run build`
     - Agent "Security": IF ENABLE_SECURITY_CHECK → Run `npm audit --production`
   - Each agent runs independently and returns results
   - Example: 6 agents launch simultaneously → All complete in ~15s (vs ~60s sequential)

3. **Collect Swarm Results**
   - Tool: TaskOutput for each agent to retrieve results
   - Wait for all agents to complete (block: true)
   - Parse each agent's output for errors, warnings, and status
   - Example: Linter agent returns "5 errors in src/utils.ts", Formatter returns "All files formatted correctly"

4. **Parse and Compile Results**
   - Process results from each agent:
     - Linting: Extract file paths, line numbers, error messages
     - Formatting: Extract files needing formatting
     - Type Check: Extract type errors with locations
     - Tests: Extract passed/failed counts, test names, execution time
     - Build: Extract build status, errors, bundle size, build time
     - Security: Extract vulnerabilities by severity, affected packages
   - Example: Parse "src/utils.ts:42:10 - 'foo' is assigned but never used" → {file: "src/utils.ts", line: 42, col: 10, error: "unused variable"}

5. **Generate Report**
   - Compile all parsed results into formatted report
   - Format: Phase sections (Static Analysis, Testing, Build, Security), overall status (PASS/FAIL/WARNINGS)
   - Include: Specific file:line locations, error messages, actionable fix commands
   - Show execution time comparison if parallel execution was used
   - Example report:
     ```
     QUALITY GATE REPORT
     Project: my-app | TypeScript
     Execution: Parallel (6 agents, 15.2s)

     STATIC ANALYSIS
       Linting: ✗ FAIL (5 issues)
         • src/utils.ts:42 - Unused variable 'foo'
         • src/App.tsx:45 - Missing dependency in useEffect
       Formatting: ✓ PASS
       Type Check: ✗ FAIL (3 errors)
         • src/types.ts:12 - Type 'string' not assignable to 'number'

     TESTING
       Tests: ✓ PASS (45 passed, 0 failed)
       Coverage: 78%

     BUILD: ✓ PASS
       Bundle size: 245 KB
       Build time: 3.2s

     SECURITY: ⚠ WARNINGS (2 critical vulns)
       • lodash@4.17.20 - Prototype Pollution

     OVERALL: ✗ FAILED

     RECOMMENDATIONS:
     • Run `npm run lint:fix` to auto-fix linting issues
     • Fix type errors in src/types.ts:12
     • Run `npm audit fix` to update vulnerable packages

     Performance: 75% faster than sequential execution (15s vs 60s)
     ```

## Failure Criteria

Gate FAILS if: Linting errors, type errors, tests fail, build fails
Gate shows WARNINGS if: Critical/high security vulnerabilities, formatting issues
