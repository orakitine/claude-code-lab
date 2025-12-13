# Python Quality Gate

Comprehensive quality checks for Python projects. Non-destructive - reports issues only. Uses parallel agent execution for maximum speed.

## Variables

ENABLE_PARALLEL_EXECUTION: true       # Use swarm pattern for parallel checks (faster)
MAX_PARALLEL_AGENTS: 6                # Maximum agents to run simultaneously

## Workflow

1. **Detect Available Tools**
   - Check which linting/formatting/testing tools are installed
   - Tools to check: ruff, pylint, flake8 (linting), black (formatting), mypy (type checking), pytest, unittest
   - Determine which checks can run based on available tooling
   - Example: ruff and pytest installed, mypy not installed → Can run linting, format, test checks (skip type check)

2. **Launch Parallel Quality Check Swarm**
   - IF: ENABLE_PARALLEL_EXECUTION is true → Launch all checks as parallel background agents
   - Tool: Task with run_in_background: true for each check
   - Agents to spawn (based on available tools):
     - Agent "Linter": IF ruff installed → Run `ruff check .` ELSE IF pylint → Run `pylint src/` ELSE IF flake8 → Run `flake8 .`
     - Agent "Formatter": IF ruff with format → Run `ruff format --check .` ELSE IF black → Run `black --check .`
     - Agent "TypeChecker": IF mypy installed AND config exists → Run `mypy .`
     - Agent "Tester": IF pytest installed → Run `pytest -v` ELSE IF unittest → Run `python -m unittest discover`
     - Agent "ImportChecker": IF setup.py or pyproject.toml → Run `python -m py_compile *.py`
     - Agent "Security": IF pip-audit installed AND ENABLE_SECURITY_CHECK → Run `pip-audit` ELSE IF safety → Run `safety check`
   - Each agent runs independently and returns results
   - Example: 6 agents launch simultaneously → All complete in ~12s (vs ~50s sequential)

3. **Collect Swarm Results**
   - Tool: TaskOutput for each agent to retrieve results
   - Wait for all agents to complete (block: true)
   - Parse each agent's output for errors, warnings, and status
   - Example: Linter agent returns "8 errors in src/utils.py", TypeChecker returns "2 type errors found"

4. **Parse and Compile Results**
   - Process results from each agent:
     - Linting: Extract file paths, line numbers, error codes, messages
     - Formatting: Extract files needing reformatting
     - Type Check: Extract type errors with locations
     - Tests: Extract passed/failed counts, test names, execution time
     - Import Check: Extract import errors and syntax issues
     - Security: Extract vulnerabilities by severity, affected packages
   - Example: Parse "src/utils.py:42:10 - F841 local variable 'foo' is assigned but never used" → {file: "src/utils.py", line: 42, col: 10, code: "F841", error: "unused variable"}

5. **Generate Report**
   - Compile all parsed results into formatted report
   - Format: Phase sections (Static Analysis, Testing, Build, Security), overall status (PASS/FAIL/WARNINGS)
   - Include: Specific file:line locations, error messages, actionable fix commands
   - Show execution time comparison if parallel execution was used
   - Handle missing tools gracefully (note: "mypy not installed - skipped type check")
   - Example report:
     ```
     QUALITY GATE REPORT
     Project: my-python-app | Python
     Execution: Parallel (5 agents, 12.4s)

     STATIC ANALYSIS
       Linting: ✗ FAIL (8 issues)
         • src/utils.py:42 - F841 Unused variable 'foo'
         • src/app.py:15 - E501 Line too long
       Formatting: ✓ PASS
       Type Check: ✗ FAIL (2 errors)
         • src/models.py:12 - Incompatible return value type

     TESTING
       Tests: ✓ PASS (32 passed, 0 failed)
       Coverage: 85%

     BUILD
       Import Check: ✓ PASS

     SECURITY: ⚠ WARNINGS (1 critical vuln)
       • requests@2.25.1 - CVE-2023-xxxxx

     OVERALL: ✗ FAILED

     ISSUES:
     • src/utils.py:42 - Unused variable
     • src/models.py:12 - Type mismatch

     RECOMMENDATIONS:
     • Run `ruff check --fix .` to auto-fix linting issues
     • Run `black .` to format code
     • Fix type errors in src/models.py
     • Update vulnerable package: requests>=2.32

     Performance: 76% faster than sequential execution (12s vs 50s)
     ```

## Failure Criteria

Gate FAILS if: Linting errors, type errors, tests fail, import/syntax errors
Gate shows WARNINGS if: Critical/high security vulnerabilities, formatting issues
Note: Some tools may not be installed - skip those checks gracefully
