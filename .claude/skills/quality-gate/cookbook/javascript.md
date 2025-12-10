# JavaScript/TypeScript Quality Gate Cookbook

This cookbook defines the quality gate workflow for JavaScript and TypeScript projects.

## Phase 1: Static Analysis 🔍

### Detect Available Scripts

First, read `package.json` to see which scripts are available.

### Run Linting

- IF: `package.json` has a `lint` script
- THEN: Run `npm run lint`
- RECORD: All linting errors with file paths and line numbers

### Run Format Check

- IF: `package.json` has a `format:check` or `prettier:check` script
- THEN: Run the format check script
- ELSE IF: Prettier is installed
- THEN: Run `npx prettier --check "src/**/*.{ts,tsx,js,jsx}"`
- RECORD: All formatting issues

### Run Type Check

- IF: `package.json` has a `type-check` script
- THEN: Run `npm run type-check`
- ELSE IF: `tsconfig.json` exists
- THEN: Run `npx tsc --noEmit`
- RECORD: All type errors with file paths and line numbers

## Phase 2: Testing 🧪

### Run Tests

- IF: `package.json` has a `test` script
- THEN: Run `npm test` or `npm run test`
- RECORD:
  - Number of tests passed
  - Number of tests failed
  - Failed test names and error messages
  - Test execution time

### Check Coverage

- IF: `package.json` has a `test:coverage` or `coverage` script
- THEN: Run the coverage script
- RECORD: Coverage percentage if available
- NOTE: Coverage is informational, not a failure criteria

**Important:** If tests fail, continue to next phases but mark overall as FAILED.

## Phase 3: Build Verification 🏗️

### Run Build

- IF: `package.json` has a `build` script
- THEN: Run `npm run build`
- RECORD:
  - Build success or failure
  - Build errors if any
  - Bundle size if displayed
  - Build time

**Important:** Clean up build artifacts after checking (optional).

## Phase 4: Security & Dependencies 🔒

### Security Audit

- IF: `ENABLE_SECURITY_CHECK` is true
- THEN: Run `npm audit --production`
- RECORD:
  - Number of vulnerabilities by severity (critical, high, moderate, low)
  - Affected packages
  - Recommended fixes

**Note:** Only report, do NOT run `npm audit fix`.

### Check for Outdated Dependencies (Optional)

- Run `npm outdated` (informational only)
- RECORD: Significantly outdated packages (major versions behind)

## Phase 5: Generate Report 📊

Create a comprehensive report in this format:

```
🚦 QUALITY GATE REPORT
═══════════════════════════════════════

📋 PROJECT: [project name from package.json]
📁 DIRECTORY: [current directory]
🕐 TIMESTAMP: [current time]
🔧 DETECTED: JavaScript/TypeScript (Node.js)

PHASE 1: STATIC ANALYSIS
  ├─ Linting:        [✓ PASS | ✗ FAIL] ([X] issues)
  ├─ Formatting:     [✓ PASS | ✗ FAIL] ([X] files need formatting)
  └─ Type Checking:  [✓ PASS | ✗ FAIL] ([X] errors)

PHASE 2: TESTING
  ├─ Test Suite:     [✓ PASS | ✗ FAIL] ([X] passed, [Y] failed)
  ├─ Duration:       [X.XX]s
  └─ Coverage:       [XX%] (if available)

PHASE 3: BUILD
  ├─ Build Status:   [✓ PASS | ✗ FAIL]
  └─ Bundle Size:    [XXX KB] (if available)

PHASE 4: SECURITY
  ├─ Audit:          [✓ PASS | ⚠ WARNINGS]
  └─ Vulnerabilities: [X critical, Y high, Z moderate, W low]

═══════════════════════════════════════
OVERALL STATUS: [✓ PASSED | ✗ FAILED | ⚠ WARNINGS]
═══════════════════════════════════════

[If any failures:]

❌ ISSUES FOUND:

Linting Issues:
  • file.ts:42:10 - [error message]
  • file.ts:55:3 - [error message]

Type Errors:
  • component.tsx:12:5 - [error message]

Failed Tests:
  • Test: "should handle edge case" - [error message]

Security Vulnerabilities:
  • package-name: [severity] - [description]

[End issues section]

💡 RECOMMENDATIONS:

[Provide specific commands to fix issues, such as:]
  • Run `npm run lint:fix` to auto-fix linting issues
  • Run `npm run format` to format code
  • Fix type errors in [specific files]
  • Review failing tests: [test names]
  • Run `npm audit fix` to fix [X] vulnerabilities (review changes carefully)

═══════════════════════════════════════
```

## Success Criteria

- ✓ All phases attempted (even if some fail)
- ✓ Clear, formatted report generated
- ✓ Specific issues identified with file:line locations
- ✓ Actionable recommendations provided
- ✓ Overall PASS/FAIL status determined

## Failure Criteria

The quality gate FAILS if any of these conditions are met:
- Linting errors found
- Type checking errors found
- Tests fail
- Build fails

The quality gate shows WARNINGS if:
- High or critical security vulnerabilities found
- Formatting issues found (can be auto-fixed)

## Notes

- This workflow is **non-destructive** - it only reports issues
- Continue all phases even if early phases fail
- Provide actionable next steps in recommendations
- Be specific about file locations and error messages
