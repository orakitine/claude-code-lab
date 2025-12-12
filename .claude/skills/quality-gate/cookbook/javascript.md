# JavaScript/TypeScript Quality Gate

Comprehensive quality checks for JavaScript and TypeScript projects. Non-destructive - reports issues only.

## Workflow

1. **Detect Available Tools**
   - Tool: Read package.json to check available scripts and installed tools
   - Look for: lint, format:check, type-check, test, build scripts
   - Example: {scripts: {lint: "eslint .", test: "vitest run", build: "vite build"}}

2. **Run Linting**
   - IF: package.json has "lint" script → Run `npm run lint`
   - Record: All linting errors with file paths and line numbers
   - Example: src/utils.ts:42:10 - 'foo' is assigned but never used

3. **Run Format Check**
   - IF: "format:check" or "prettier:check" script exists → Run that script
   - ELSE IF: Prettier installed → Run `npx prettier --check "src/**/*.{ts,tsx,js,jsx}"`
   - Record: All formatting issues with file paths
   - Example: src/App.tsx needs formatting

4. **Run Type Check**
   - IF: "type-check" script exists → Run `npm run type-check`
   - ELSE IF: tsconfig.json exists → Run `npx tsc --noEmit`
   - Record: All type errors with file paths and line numbers
   - Example: src/components/Button.tsx:12:5 - Type 'string' not assignable to 'number'

5. **Run Tests**
   - IF: "test" script exists → Run `npm test` or `npm run test`
   - Record: passed count, failed count, failed test names, error messages, execution time
   - IMPORTANT: Continue to next phases even if tests fail
   - Example: 45 passed, 2 failed - "should handle edge case" failed with [error]

6. **Run Build**
   - IF: "build" script exists → Run `npm run build`
   - Record: build success/failure, errors, bundle size (if shown), build time
   - Optional: Clean up build artifacts after checking
   - Example: Build failed - Cannot find module 'missing-import'

7. **Security Audit**
   - IF: ENABLE_SECURITY_CHECK is true → Run `npm audit --production`
   - Record: vulnerabilities by severity (critical/high/moderate/low), affected packages, recommended fixes
   - NOTE: Only report, do NOT run `npm audit fix`
   - Example: 2 critical, 5 high, 10 moderate vulnerabilities found

8. **Generate Report**
   - Compile all results into formatted report
   - Format: Phase sections (Static Analysis, Testing, Build, Security), overall status (PASS/FAIL/WARNINGS)
   - Include: Specific file:line locations, error messages, actionable fix commands
   - Example report:
     ```
     QUALITY GATE REPORT
     Project: my-app | TypeScript

     STATIC ANALYSIS
       Linting: ✗ FAIL (5 issues)
       Formatting: ✓ PASS
       Type Check: ✗ FAIL (3 errors)

     TESTING
       Tests: ✓ PASS (45 passed)
       Coverage: 78%

     BUILD: ✓ PASS
     SECURITY: ⚠ WARNINGS (2 critical vulns)

     OVERALL: ✗ FAILED

     ISSUES:
     • src/utils.ts:42 - Unused variable
     • src/types.ts:12 - Type mismatch

     RECOMMENDATIONS:
     • Run `npm run lint:fix`
     • Fix type errors in src/types.ts
     • Run `npm audit fix`
     ```

## Failure Criteria

Gate FAILS if: Linting errors, type errors, tests fail, build fails
Gate shows WARNINGS if: Critical/high security vulnerabilities, formatting issues
