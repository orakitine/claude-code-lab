# Python Quality Gate Cookbook

This cookbook defines the quality gate workflow for Python projects.

## Phase 1: Static Analysis 🔍

### Run Linting

- IF: `ruff` is installed (check with `which ruff` or `pip show ruff`)
- THEN: Run `ruff check .`
- ELSE IF: `pylint` is installed
- THEN: Run `pylint src/` or `pylint *.py`
- ELSE IF: `flake8` is installed
- THEN: Run `flake8 .`
- RECORD: All linting errors with file paths and line numbers

### Run Format Check

- IF: `ruff` is installed and configured for formatting
- THEN: Run `ruff format --check .`
- ELSE IF: `black` is installed
- THEN: Run `black --check .`
- RECORD: All formatting issues

### Run Type Check

- IF: `mypy` is installed AND `mypy.ini` or `setup.cfg` exists
- THEN: Run `mypy .`
- RECORD: All type errors with file paths and line numbers

## Phase 2: Testing 🧪

### Run Tests

- IF: `pytest` is installed
- THEN: Run `pytest -v`
- ELSE IF: `unittest` tests exist
- THEN: Run `python -m unittest discover`
- RECORD:
  - Number of tests passed
  - Number of tests failed
  - Failed test names and error messages
  - Test execution time

### Check Coverage

- IF: `pytest-cov` is installed
- THEN: Run `pytest --cov --cov-report=term`
- RECORD: Coverage percentage if available

**Important:** If tests fail, continue to next phases but mark overall as FAILED.

## Phase 3: Build Verification 🏗️

### Check Import Errors

- TRY: Import main modules to check for import errors
- IF: `setup.py` or `pyproject.toml` exists
- THEN: Run `python -m py_compile *.py` to check syntax
- RECORD: Any import or syntax errors

### Check Package Build (if applicable)

- IF: `pyproject.toml` or `setup.py` exists
- THEN: Try `python -m build` (if build package installed)
- RECORD: Build success or failure

## Phase 4: Security & Dependencies 🔒

### Security Audit

- IF: `pip-audit` is installed AND `ENABLE_SECURITY_CHECK` is true
- THEN: Run `pip-audit`
- ELSE IF: `safety` is installed
- THEN: Run `safety check`
- RECORD:
  - Number of vulnerabilities by severity
  - Affected packages
  - Recommended fixes

### Check for Outdated Dependencies (Optional)

- Run `pip list --outdated` (informational only)
- RECORD: Significantly outdated packages

## Phase 5: Generate Report 📊

Create a comprehensive report in this format:

```
🚦 QUALITY GATE REPORT
═══════════════════════════════════════

📋 PROJECT: [project name]
📁 DIRECTORY: [current directory]
🕐 TIMESTAMP: [current time]
🐍 DETECTED: Python

PHASE 1: STATIC ANALYSIS
  ├─ Linting:        [✓ PASS | ✗ FAIL] ([X] issues)
  ├─ Formatting:     [✓ PASS | ✗ FAIL] ([X] files need formatting)
  └─ Type Checking:  [✓ PASS | ✗ FAIL] ([X] errors)

PHASE 2: TESTING
  ├─ Test Suite:     [✓ PASS | ✗ FAIL] ([X] passed, [Y] failed)
  ├─ Duration:       [X.XX]s
  └─ Coverage:       [XX%] (if available)

PHASE 3: BUILD
  └─ Import Check:   [✓ PASS | ✗ FAIL]

PHASE 4: SECURITY
  ├─ Audit:          [✓ PASS | ⚠ WARNINGS]
  └─ Vulnerabilities: [X critical, Y high, Z moderate, W low]

═══════════════════════════════════════
OVERALL STATUS: [✓ PASSED | ✗ FAILED | ⚠ WARNINGS]
═══════════════════════════════════════

[If any failures:]

❌ ISSUES FOUND:

Linting Issues:
  • file.py:42:10 - [error message]

Type Errors:
  • module.py:12:5 - [error message]

Failed Tests:
  • Test: "test_edge_case" - [error message]

Security Vulnerabilities:
  • package-name: [severity] - [description]

[End issues section]

💡 RECOMMENDATIONS:

[Provide specific commands to fix issues, such as:]
  • Run `ruff check --fix .` or `black .` to format code
  • Fix linting issues in [specific files]
  • Fix type errors in [specific files]
  • Review failing tests: [test names]
  • Update vulnerable packages: [specific commands]

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
- Import/syntax errors found

The quality gate shows WARNINGS if:
- High or critical security vulnerabilities found
- Formatting issues found (can be auto-fixed)

## Notes

- This workflow is **non-destructive** - it only reports issues
- Continue all phases even if early phases fail
- Provide actionable next steps in recommendations
- Be specific about file locations and error messages
- Some tools may not be installed - handle gracefully and skip those checks
