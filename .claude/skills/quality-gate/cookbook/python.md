# Python Quality Gate

Comprehensive quality checks for Python projects. Non-destructive - reports issues only.

## Workflow

1. **Detect Available Tools**
   - Check which linting/formatting/testing tools are installed
   - Tools to check: ruff, pylint, flake8 (linting), black (formatting), mypy (type checking), pytest, unittest
   - Example: ruff and pytest installed, mypy not installed

2. **Run Linting**
   - IF: ruff installed → Run `ruff check .`
   - ELSE IF: pylint installed → Run `pylint src/` or `pylint *.py`
   - ELSE IF: flake8 installed → Run `flake8 .`
   - Record: All linting errors with file paths and line numbers
   - Example: src/utils.py:42:10 - F841 local variable 'foo' is assigned but never used

3. **Run Format Check**
   - IF: ruff installed with format config → Run `ruff format --check .`
   - ELSE IF: black installed → Run `black --check .`
   - Record: All formatting issues with file paths
   - Example: src/app.py would be reformatted

4. **Run Type Check**
   - IF: mypy installed AND (mypy.ini or setup.cfg exists) → Run `mypy .`
   - Record: All type errors with file paths and line numbers
   - Example: src/models.py:12:5 - Incompatible return value type

5. **Run Tests**
   - IF: pytest installed → Run `pytest -v`
   - ELSE IF: unittest tests exist → Run `python -m unittest discover`
   - Record: passed count, failed count, failed test names, error messages, execution time
   - IMPORTANT: Continue to next phases even if tests fail
   - Example: 32 passed, 1 failed - test_edge_case failed with AssertionError

6. **Check Imports/Syntax**
   - Try importing main modules to check for import errors
   - IF: setup.py or pyproject.toml exists → Run `python -m py_compile *.py`
   - Record: Any import or syntax errors
   - Example: ImportError: cannot import name 'MissingModule' from 'package'

7. **Security Audit**
   - IF: pip-audit installed AND ENABLE_SECURITY_CHECK → Run `pip-audit`
   - ELSE IF: safety installed → Run `safety check`
   - Record: vulnerabilities by severity, affected packages, recommended fixes
   - Example: 1 critical, 3 high vulnerabilities in dependencies

8. **Generate Report**
   - Compile all results into formatted report
   - Format: Phase sections (Static Analysis, Testing, Build, Security), overall status (PASS/FAIL/WARNINGS)
   - Include: Specific file:line locations, error messages, actionable fix commands
   - Example report:
     ```
     QUALITY GATE REPORT
     Project: my-python-app | Python

     STATIC ANALYSIS
       Linting: ✗ FAIL (8 issues)
       Formatting: ✓ PASS
       Type Check: ✗ FAIL (2 errors)

     TESTING
       Tests: ✓ PASS (32 passed)
       Coverage: 85%

     BUILD
       Import Check: ✓ PASS

     SECURITY: ⚠ WARNINGS (1 critical vuln)

     OVERALL: ✗ FAILED

     ISSUES:
     • src/utils.py:42 - Unused variable
     • src/models.py:12 - Type mismatch

     RECOMMENDATIONS:
     • Run `ruff check --fix .`
     • Run `black .` to format code
     • Fix type errors in src/models.py
     • Update vulnerable package: requests<2.32
     ```

## Failure Criteria

Gate FAILS if: Linting errors, type errors, tests fail, import/syntax errors
Gate shows WARNINGS if: Critical/high security vulnerabilities, formatting issues
Note: Some tools may not be installed - skip those checks gracefully
