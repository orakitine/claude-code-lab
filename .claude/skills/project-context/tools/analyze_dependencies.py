#!/usr/bin/env python3
"""
Analyze Dependencies Tool

Extracts and analyzes project dependencies from package.json, requirements.txt,
or go.mod files.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional


def analyze_dependencies(project_path: str = ".", project_type: str = "auto") -> str:
    """
    Analyze project dependencies.

    Args:
        project_path: Path to the project root (default: current directory)
        project_type: Type of project ("nodejs", "python", "go", or "auto" for detection)

    Returns:
        JSON string with dependency analysis:
        {
            "runtime": [...],
            "dev": [...],
            "scripts": {...},
            "node_version": "...",
            "total_count": N
        }
    """
    project_root = Path(project_path).resolve()

    # Auto-detect project type if needed
    if project_type == "auto":
        project_type = _detect_type(project_root)

    result = {
        "type": project_type,
        "runtime": [],
        "dev": [],
        "scripts": {},
        "metadata": {},
        "total_count": 0
    }

    if project_type == "nodejs":
        _analyze_nodejs(project_root, result)
    elif project_type == "python":
        _analyze_python(project_root, result)
    elif project_type == "go":
        _analyze_go(project_root, result)

    return json.dumps(result, indent=2)


def _detect_type(project_root: Path) -> str:
    """Detect project type based on indicator files."""
    if (project_root / "package.json").exists():
        return "nodejs"
    if (project_root / "requirements.txt").exists() or (project_root / "pyproject.toml").exists():
        return "python"
    if (project_root / "go.mod").exists():
        return "go"
    return "unknown"


def _analyze_nodejs(project_root: Path, result: Dict) -> None:
    """Analyze Node.js dependencies from package.json."""
    package_json = project_root / "package.json"

    if not package_json.exists():
        return

    try:
        with open(package_json) as f:
            pkg = json.load(f)

        # Extract dependencies
        runtime_deps = pkg.get("dependencies", {})
        dev_deps = pkg.get("devDependencies", {})

        result["runtime"] = [
            {"name": name, "version": version}
            for name, version in runtime_deps.items()
        ]

        result["dev"] = [
            {"name": name, "version": version}
            for name, version in dev_deps.items()
        ]

        # Extract scripts
        result["scripts"] = pkg.get("scripts", {})

        # Extract metadata
        result["metadata"] = {
            "name": pkg.get("name", "unknown"),
            "version": pkg.get("version", "unknown"),
            "description": pkg.get("description", ""),
            "node_version": pkg.get("engines", {}).get("node", "not specified"),
            "package_manager": _detect_package_manager(project_root)
        }

        result["total_count"] = len(runtime_deps) + len(dev_deps)

    except (json.JSONDecodeError, IOError) as e:
        result["error"] = f"Failed to parse package.json: {str(e)}"


def _analyze_python(project_root: Path, result: Dict) -> None:
    """Analyze Python dependencies from requirements.txt or pyproject.toml."""
    requirements_file = project_root / "requirements.txt"

    if requirements_file.exists():
        try:
            with open(requirements_file) as f:
                lines = f.readlines()

            dependencies = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    # Parse dependency (handle version specifiers)
                    if "==" in line:
                        name, version = line.split("==", 1)
                    elif ">=" in line:
                        name = line.split(">=")[0]
                        version = f">={line.split('>=')[1]}"
                    else:
                        name = line
                        version = "any"

                    dependencies.append({"name": name.strip(), "version": version.strip()})

            result["runtime"] = dependencies
            result["total_count"] = len(dependencies)

        except IOError as e:
            result["error"] = f"Failed to read requirements.txt: {str(e)}"

    # Check for pyproject.toml
    pyproject_file = project_root / "pyproject.toml"
    if pyproject_file.exists():
        result["metadata"]["has_pyproject"] = True
        # Note: Full TOML parsing would require tomli/tomllib library
        # For now, just indicate presence


def _analyze_go(project_root: Path, result: Dict) -> None:
    """Analyze Go dependencies from go.mod."""
    go_mod = project_root / "go.mod"

    if not go_mod.exists():
        return

    try:
        with open(go_mod) as f:
            content = f.read()

        dependencies = []
        in_require = False

        for line in content.split("\n"):
            line = line.strip()

            if line.startswith("require ("):
                in_require = True
                continue
            elif line == ")":
                in_require = False
                continue

            if in_require or line.startswith("require "):
                # Parse dependency line
                line = line.replace("require ", "").strip()
                if line and not line.startswith("//"):
                    parts = line.split()
                    if len(parts) >= 2:
                        name = parts[0]
                        version = parts[1]
                        dependencies.append({"name": name, "version": version})

        result["runtime"] = dependencies
        result["total_count"] = len(dependencies)

    except IOError as e:
        result["error"] = f"Failed to read go.mod: {str(e)}"


def _detect_package_manager(project_root: Path) -> str:
    """Detect which package manager is used."""
    if (project_root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (project_root / "yarn.lock").exists():
        return "yarn"
    if (project_root / "package-lock.json").exists():
        return "npm"
    return "npm"  # default


if __name__ == "__main__":
    import sys

    # Get project path from command line or use current directory
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    project_type = sys.argv[2] if len(sys.argv) > 2 else "auto"

    # Run analysis
    output = analyze_dependencies(project_path, project_type)
    print(output)
