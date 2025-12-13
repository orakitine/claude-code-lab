# Python Project Analysis

Comprehensive analysis workflow for Python projects. Uses parallel agent execution for faster analysis.

## Variables

ENABLE_PARALLEL_EXECUTION: true       # Use parallel agent swarm for faster analysis
MAX_PARALLEL_AGENTS: 3                # Maximum agents to run simultaneously

## Workflow

1. **Detect Framework**
   - Tool: Run `tools/detect_framework.py` on project root
   - Checks for: Django, Flask, FastAPI, generic Python
   - Indicators: requirements.txt/pyproject.toml, framework-specific files (manage.py for Django), common packages, structure patterns
   - Example: manage.py found + django in requirements → {type: "python", framework: "django", language: "python"}

2. **Launch Parallel Analysis Swarm**
   - IF: ENABLE_PARALLEL_EXECUTION is true → Launch all analysis tasks as parallel background agents
   - Tool: Task with run_in_background: true for each analysis task
   - Agents to spawn:
     - Agent "DependencyAnalyzer": Run `tools/analyze_dependencies.py` on project root
     - Agent "StructureMapper": Run `tools/analyze_structure.py` on project root
     - Agent "EntryPointFinder": Run `tools/find_entry_points.py` with detected framework
   - Each agent runs independently and returns analysis results
   - Example: 3 agents launch simultaneously → All complete in ~4s (vs ~9s sequential)

3. **Collect Swarm Results**
   - Tool: TaskOutput for each agent to retrieve results
   - Wait for all agents to complete (block: true)
   - Parse each agent's output:
     - DependencyAnalyzer: {runtime: [...], dev: [...], categories: {...}}
     - StructureMapper: {source: {...}, tests: {...}, config: [...], docs: [...]}
     - EntryPointFinder: ["manage.py", "myproject/settings.py", "myproject/wsgi.py"]
   - Example: All agents complete → Combined data ready for pattern detection

4. **Detect Patterns**
   - Analyze collected structure and dependencies to identify architecture patterns
   - Web: Django MTV (Model-Template-View), Flask Blueprint-based, FastAPI Router-based
   - Testing: pytest (most common), unittest, tox, coverage tools (coverage.py, pytest-cov)
   - Database: Django ORM/SQLAlchemy (ORM), psycopg2/pymongo (direct), alembic/Django migrations
   - API: REST (Flask-RESTful/DRF), GraphQL (Graphene), gRPC
   - Code quality: Linting (pylint/flake8/ruff), formatting (black/autopep8), type checking (mypy/pyright)
   - Async: asyncio, FastAPI (async by default), Django async views
   - Example: Django + DRF + PostgreSQL + Celery → REST API with background tasks

5. **Generate Report**
   - Tool: Run `tools/generate_report.py` with all collected data
   - Report sections: project overview, tech stack, directory structure, entry points, key dependencies, dev setup, detected patterns, dev workflow
   - Output mode: IF user requested "save" → Write to OUTPUT_FILE, ELSE → Display in chat
   - Show execution time comparison if parallel execution was used
   - Include Python-specific sections: virtual env setup, package vs application structure
   - Example report shows: "Analysis completed in 6s (29% faster than sequential 9s execution)"

## Tool Sequence Example

```
detect_framework(".")
  → {type: "python", framework: "django", language: "python"}

PARALLEL SWARM:
├─ analyze_dependencies(".")      → {runtime: [...], dev: [...]}
├─ analyze_structure(".")         → {source: {...}, tests: {...}, config: {...}}
└─ find_entry_points(".", "django")  → ["manage.py", "settings.py", "wsgi.py"]

collect_results()
  → {dependencies: {...}, structure: {...}, entry_points: [...]}

detect_patterns({...all_data...})
  → {web: "Django MTV", api: "DRF", database: "PostgreSQL + ORM"}

generate_report({...all_data...}, "display")
  → [formatted markdown report with performance metrics]
```
