# Python Project Analysis

Comprehensive analysis workflow for Python projects.

## Workflow

1. **Detect Framework**
   - Tool: Run `tools/detect_framework.py` on project root
   - Checks for: Django, Flask, FastAPI, generic Python
   - Indicators: requirements.txt/pyproject.toml, framework-specific files (manage.py for Django), common packages, structure patterns
   - Example: manage.py found + django in requirements → {type: "python", framework: "django", language: "python"}

2. **Analyze Dependencies**
   - Tool: Run `tools/analyze_dependencies.py` on project root
   - Reads requirements.txt or pyproject.toml: runtime deps, version constraints, dev deps (if separated)
   - Record: Key packages and purposes, version specs, notable packages
   - Common categories: Web frameworks (Django/Flask/FastAPI), testing (pytest/unittest), linting (black/ruff/pylint), data science (numpy/pandas), database (SQLAlchemy/psycopg2/pymongo)
   - Example: {runtime: ["django==4.2", "djangorestframework", "psycopg2-binary"], dev: ["pytest", "black"]}

3. **Map Directory Structure**
   - Tool: Run `tools/analyze_structure.py` on project root
   - Categorizes directories: source (src/, app/, main package), tests (test/, *_test.py), config (setup.py, pyproject.toml), docs, data, scripts
   - Django: manage.py, multiple app dirs, settings.py/urls.py/wsgi.py
   - Flask: app.py/application.py, templates/, static/, flatter structure
   - FastAPI: main.py, routers/, models/
   - Package: setup.py/pyproject.toml, src/ or package_name/, tests/
   - Ignore: __pycache__/, *.pyc, .pytest_cache/, venv/, env/, dist/, build/, *.egg-info/, .git/
   - Example: {source: {manage.py, apps: ["users", "api"]}, tests: {test/}, config: ["settings.py"]}

4. **Find Entry Points**
   - Tool: Run `tools/find_entry_points.py` with detected framework
   - Django: manage.py, settings.py, urls.py, wsgi.py/asgi.py
   - Flask: app.py/main.py, wsgi.py
   - FastAPI: main.py (creates app = FastAPI())
   - CLI tools: __main__.py, entry points in setup.py/pyproject.toml
   - Example: ["manage.py", "myproject/settings.py", "myproject/wsgi.py"]

5. **Detect Patterns**
   - Analyze structure and dependencies to identify architecture patterns
   - Web: Django MTV (Model-Template-View), Flask Blueprint-based, FastAPI Router-based
   - Testing: pytest (most common), unittest, tox, coverage tools (coverage.py, pytest-cov)
   - Database: Django ORM/SQLAlchemy (ORM), psycopg2/pymongo (direct), alembic/Django migrations
   - API: REST (Flask-RESTful/DRF), GraphQL (Graphene), gRPC
   - Code quality: Linting (pylint/flake8/ruff), formatting (black/autopep8), type checking (mypy/pyright)
   - Async: asyncio, FastAPI (async by default), Django async views
   - Example: Django + DRF + PostgreSQL + Celery → REST API with background tasks

6. **Generate Report**
   - Tool: Run `tools/generate_report.py` with all collected data
   - Report sections: project overview, tech stack, directory structure, entry points, key dependencies, dev setup, detected patterns, dev workflow
   - Output mode: IF user requested "save" → Write to .project-context.md, ELSE → Display in chat
   - Example: Complete markdown report with Python-specific sections (virtual env, package vs app)

## Tool Sequence Example

```
detect_framework(".")
  → {type: "python", framework: "django", language: "python"}

analyze_dependencies(".")
  → {runtime: [...], dev: [...]}

analyze_structure(".")
  → {source: {...}, tests: {...}, config: {...}}

find_entry_points(".", "django")
  → ["manage.py", "settings.py", "wsgi.py"]

generate_report({...all_data...}, "display")
  → [formatted markdown report]
```
