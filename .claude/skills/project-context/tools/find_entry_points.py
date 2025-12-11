#!/usr/bin/env python3
"""
Find Entry Points Tool

Locates main entry point files for the application based on project type
and framework.
"""

import json
from pathlib import Path
from typing import List, Dict


def find_entry_points(project_path: str = ".", framework: str = "auto") -> str:
    """
    Find application entry points.

    Args:
        project_path: Path to the project root (default: current directory)
        framework: Framework type ("react-vite", "nextjs", "express", etc. or "auto")

    Returns:
        JSON string with entry points:
        {
            "main": [...],
            "server": [...],
            "tests": [...],
            "framework_specific": [...]
        }
    """
    project_root = Path(project_path).resolve()

    result = {
        "main": [],
        "server": [],
        "tests": [],
        "framework_specific": []
    }

    # Read package.json if it exists (for Node.js projects)
    package_json_main = None
    package_json = project_root / "package.json"
    if package_json.exists():
        try:
            import json as json_lib
            with open(package_json) as f:
                pkg = json_lib.load(f)
                package_json_main = pkg.get("main")
        except:
            pass

    # Find entry points based on framework
    if framework in {"react-vite", "vue-vite", "svelte"}:
        _find_vite_entry_points(project_root, result)
    elif framework == "nextjs":
        _find_nextjs_entry_points(project_root, result)
    elif framework in {"express", "fastify", "nestjs"}:
        _find_backend_entry_points(project_root, result)
    elif framework == "django":
        _find_django_entry_points(project_root, result)
    elif framework == "flask" or framework == "fastapi":
        _find_python_web_entry_points(project_root, result)
    else:
        # Generic search
        _find_generic_entry_points(project_root, result, package_json_main)

    # Find test entry points
    _find_test_entry_points(project_root, result)

    return json.dumps(result, indent=2)


def _find_vite_entry_points(project_root: Path, result: Dict) -> None:
    """Find entry points for Vite-based projects."""
    # Common Vite entry points
    candidates = [
        "src/main.ts",
        "src/main.tsx",
        "src/main.js",
        "src/main.jsx",
        "index.html"  # Vite always uses index.html
    ]

    for candidate in candidates:
        file_path = project_root / candidate
        if file_path.exists():
            result["main"].append(candidate)

    # Find App component
    app_candidates = [
        "src/App.tsx",
        "src/App.ts",
        "src/App.jsx",
        "src/App.js"
    ]

    for candidate in app_candidates:
        file_path = project_root / candidate
        if file_path.exists():
            result["framework_specific"].append(candidate)


def _find_nextjs_entry_points(project_root: Path, result: Dict) -> None:
    """Find entry points for Next.js projects."""
    # App Router
    if (project_root / "app").exists():
        result["framework_specific"].append("app/ (App Router)")
        if (project_root / "app" / "layout.tsx").exists():
            result["framework_specific"].append("app/layout.tsx")
        if (project_root / "app" / "page.tsx").exists():
            result["framework_specific"].append("app/page.tsx")

    # Pages Router
    if (project_root / "pages").exists():
        result["framework_specific"].append("pages/ (Pages Router)")
        if (project_root / "pages" / "_app.tsx").exists():
            result["framework_specific"].append("pages/_app.tsx")
        if (project_root / "pages" / "index.tsx").exists():
            result["framework_specific"].append("pages/index.tsx")

    # API routes
    if (project_root / "pages" / "api").exists():
        result["server"].append("pages/api/")


def _find_backend_entry_points(project_root: Path, result: Dict) -> None:
    """Find entry points for backend frameworks."""
    candidates = [
        "src/index.ts",
        "src/index.js",
        "src/server.ts",
        "src/server.js",
        "src/app.ts",
        "src/app.js",
        "src/main.ts",
        "src/main.js",
        "index.ts",
        "index.js",
        "server.ts",
        "server.js",
        "app.ts",
        "app.js"
    ]

    for candidate in candidates:
        file_path = project_root / candidate
        if file_path.exists():
            result["server"].append(candidate)


def _find_django_entry_points(project_root: Path, result: Dict) -> None:
    """Find entry points for Django projects."""
    if (project_root / "manage.py").exists():
        result["main"].append("manage.py")

    # Find settings.py
    for settings_file in project_root.rglob("settings.py"):
        if "site-packages" not in str(settings_file):
            result["framework_specific"].append(str(settings_file.relative_to(project_root)))
            break


def _find_python_web_entry_points(project_root: Path, result: Dict) -> None:
    """Find entry points for Flask/FastAPI projects."""
    candidates = [
        "app.py",
        "main.py",
        "server.py",
        "src/app.py",
        "src/main.py"
    ]

    for candidate in candidates:
        file_path = project_root / candidate
        if file_path.exists():
            result["main"].append(candidate)


def _find_generic_entry_points(project_root: Path, result: Dict, package_json_main: str = None) -> None:
    """Find entry points generically."""
    # Use package.json main if available
    if package_json_main:
        main_path = project_root / package_json_main
        if main_path.exists():
            result["main"].append(package_json_main)
            return

    # Common entry point names
    candidates = [
        "src/index.ts",
        "src/index.js",
        "src/main.ts",
        "src/main.js",
        "index.ts",
        "index.js",
        "main.ts",
        "main.js",
        "main.py",
        "app.py",
        "manage.py",
        "main.go"
    ]

    for candidate in candidates:
        file_path = project_root / candidate
        if file_path.exists():
            result["main"].append(candidate)


def _find_test_entry_points(project_root: Path, result: Dict) -> None:
    """Find test configuration files."""
    test_configs = [
        "vitest.config.ts",
        "jest.config.js",
        "jest.config.ts",
        "pytest.ini",
        "setup.cfg",
        "test/setup.ts",
        "src/test/setup.ts"
    ]

    for config in test_configs:
        file_path = project_root / config
        if file_path.exists():
            result["tests"].append(config)


if __name__ == "__main__":
    import sys

    # Get project path from command line or use current directory
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    framework = sys.argv[2] if len(sys.argv) > 2 else "auto"

    # Run analysis
    output = find_entry_points(project_path, framework)
    print(output)
