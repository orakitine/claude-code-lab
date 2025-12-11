#!/usr/bin/env python3
"""
Detect Framework Tool

Detects the project type, framework, and language by analyzing indicator files
and configurations.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional


def detect_framework(project_path: str = ".") -> str:
    """
    Detect the project framework and type.

    Args:
        project_path: Path to the project root (default: current directory)

    Returns:
        JSON string with detection results:
        {
            "type": "nodejs" | "python" | "go" | "unknown",
            "framework": "react-vite" | "nextjs" | "django" | etc,
            "language": "typescript" | "javascript" | "python" | "go",
            "confidence": "high" | "medium" | "low"
        }
    """
    result = {
        "type": "unknown",
        "framework": "unknown",
        "language": "unknown",
        "confidence": "low"
    }

    project_root = Path(project_path).resolve()

    # Check for Node.js/JavaScript/TypeScript
    if _check_nodejs(project_root, result):
        return json.dumps(result, indent=2)

    # Check for Python
    if _check_python(project_root, result):
        return json.dumps(result, indent=2)

    # Check for Go
    if _check_go(project_root, result):
        return json.dumps(result, indent=2)

    return json.dumps(result, indent=2)


def _check_nodejs(project_root: Path, result: Dict) -> bool:
    """Check if project is Node.js based."""
    package_json = project_root / "package.json"

    if not package_json.exists():
        return False

    result["type"] = "nodejs"

    # Read package.json
    try:
        with open(package_json) as f:
            pkg = json.load(f)

        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

        # Check for TypeScript
        if "typescript" in deps or (project_root / "tsconfig.json").exists():
            result["language"] = "typescript"
        else:
            result["language"] = "javascript"

        # Detect framework
        # Next.js
        if "next" in deps or (project_root / "next.config.js").exists() or (project_root / "next.config.mjs").exists():
            result["framework"] = "nextjs"
            result["confidence"] = "high"
            return True

        # React with Vite
        if "react" in deps and "vite" in deps:
            result["framework"] = "react-vite"
            result["confidence"] = "high"
            return True

        # React (generic)
        if "react" in deps:
            result["framework"] = "react"
            result["confidence"] = "medium"
            return True

        # Vue
        if "vue" in deps:
            if "vite" in deps:
                result["framework"] = "vue-vite"
            else:
                result["framework"] = "vue"
            result["confidence"] = "high"
            return True

        # Svelte
        if "svelte" in deps:
            result["framework"] = "svelte"
            result["confidence"] = "high"
            return True

        # Express
        if "express" in deps:
            result["framework"] = "express"
            result["confidence"] = "high"
            return True

        # Nest.js
        if "@nestjs/core" in deps:
            result["framework"] = "nestjs"
            result["confidence"] = "high"
            return True

        # Fastify
        if "fastify" in deps:
            result["framework"] = "fastify"
            result["confidence"] = "high"
            return True

        # Vanilla/Generic Node.js
        result["framework"] = "nodejs"
        result["confidence"] = "medium"
        return True

    except (json.JSONDecodeError, IOError):
        result["framework"] = "nodejs"
        result["confidence"] = "low"
        return True


def _check_python(project_root: Path, result: Dict) -> bool:
    """Check if project is Python based."""
    has_requirements = (project_root / "requirements.txt").exists()
    has_pyproject = (project_root / "pyproject.toml").exists()
    has_setup_py = (project_root / "setup.py").exists()

    if not (has_requirements or has_pyproject or has_setup_py):
        return False

    result["type"] = "python"
    result["language"] = "python"

    # Try to detect framework
    # Check for Django
    if has_requirements:
        try:
            with open(project_root / "requirements.txt") as f:
                content = f.read().lower()
                if "django" in content:
                    result["framework"] = "django"
                    result["confidence"] = "high"
                    return True
                if "flask" in content:
                    result["framework"] = "flask"
                    result["confidence"] = "high"
                    return True
                if "fastapi" in content:
                    result["framework"] = "fastapi"
                    result["confidence"] = "high"
                    return True
        except IOError:
            pass

    # Check for Django by structure
    if (project_root / "manage.py").exists():
        result["framework"] = "django"
        result["confidence"] = "high"
        return True

    # Generic Python project
    result["framework"] = "python"
    result["confidence"] = "medium"
    return True


def _check_go(project_root: Path, result: Dict) -> bool:
    """Check if project is Go based."""
    go_mod = project_root / "go.mod"

    if not go_mod.exists():
        return False

    result["type"] = "go"
    result["language"] = "go"
    result["framework"] = "go"
    result["confidence"] = "high"

    return True


if __name__ == "__main__":
    import sys

    # Get project path from command line or use current directory
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."

    # Run detection
    output = detect_framework(project_path)
    print(output)
