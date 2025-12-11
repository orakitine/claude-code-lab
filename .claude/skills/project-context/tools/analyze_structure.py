#!/usr/bin/env python3
"""
Analyze Structure Tool

Maps the project directory structure and categorizes files/directories
by their purpose.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Set


# Directories to ignore
IGNORE_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", "out", "__pycache__",
    ".pytest_cache", "venv", "env", ".venv", "vendor", "target", "coverage",
    ".nyc_output", ".cache", "tmp", "temp"
}

# File patterns to ignore
IGNORE_FILES = {
    ".DS_Store", "Thumbs.db", "*.pyc", "*.pyo", "*.log"
}


def analyze_structure(project_path: str = ".", max_depth: int = 4) -> str:
    """
    Analyze project directory structure.

    Args:
        project_path: Path to the project root (default: current directory)
        max_depth: Maximum depth to traverse (default: 4)

    Returns:
        JSON string with structure analysis:
        {
            "source": {...},
            "tests": {...},
            "config": [...],
            "docs": [...],
            "assets": [...],
            "other": [...]
        }
    """
    project_root = Path(project_path).resolve()

    result = {
        "source": {},
        "tests": {},
        "config": [],
        "docs": [],
        "assets": [],
        "build_output": [],
        "other": []
    }

    _walk_directory(project_root, project_root, result, current_depth=0, max_depth=max_depth)

    return json.dumps(result, indent=2)


def _walk_directory(
    current_path: Path,
    project_root: Path,
    result: Dict,
    current_depth: int,
    max_depth: int
) -> None:
    """Recursively walk directory and categorize contents."""
    if current_depth > max_depth:
        return

    try:
        for item in sorted(current_path.iterdir()):
            # Skip ignored directories
            if item.is_dir() and item.name in IGNORE_DIRS:
                if item.name in {"dist", "build", ".next", "out"}:
                    result["build_output"].append(str(item.relative_to(project_root)))
                continue

            # Get relative path
            rel_path = str(item.relative_to(project_root))

            if item.is_dir():
                _categorize_directory(item, rel_path, result, project_root, current_depth, max_depth)
            elif item.is_file():
                _categorize_file(item, rel_path, result)

    except PermissionError:
        pass  # Skip directories we can't read


def _categorize_directory(
    dir_path: Path,
    rel_path: str,
    result: Dict,
    project_root: Path,
    current_depth: int,
    max_depth: int
) -> None:
    """Categorize a directory by its purpose."""
    dir_name = dir_path.name.lower()

    # Source directories
    if dir_name in {"src", "lib", "app", "pages", "components", "api", "routes", "views", "models", "controllers", "services"}:
        if "source" not in result:
            result["source"] = {}
        result["source"][rel_path] = _get_directory_summary(dir_path)
        # Continue walking source directories
        _walk_directory(dir_path, project_root, result, current_depth + 1, max_depth)

    # Test directories
    elif dir_name in {"test", "tests", "__tests__", "spec", "specs"} or dir_name.endswith(".test") or dir_name.endswith(".spec"):
        if "tests" not in result:
            result["tests"] = {}
        result["tests"][rel_path] = _get_directory_summary(dir_path)

    # Documentation
    elif dir_name in {"docs", "doc", "documentation", "examples"}:
        result["docs"].append(rel_path)

    # Assets
    elif dir_name in {"public", "static", "assets", "images", "media"}:
        result["assets"].append(rel_path)

    else:
        # Check if it contains source files
        has_source = _contains_source_files(dir_path)
        if has_source:
            if "source" not in result:
                result["source"] = {}
            result["source"][rel_path] = _get_directory_summary(dir_path)
            _walk_directory(dir_path, project_root, result, current_depth + 1, max_depth)
        else:
            result["other"].append(rel_path)


def _categorize_file(file_path: Path, rel_path: str, result: Dict) -> None:
    """Categorize a file by its purpose."""
    file_name = file_path.name.lower()

    # Config files
    if _is_config_file(file_name):
        result["config"].append(rel_path)

    # Documentation
    elif file_name in {"readme.md", "contributing.md", "changelog.md", "license", "license.md"}:
        result["docs"].append(rel_path)


def _is_config_file(filename: str) -> bool:
    """Check if a file is a configuration file."""
    config_patterns = [
        ".json", ".yaml", ".yml", ".toml", ".ini", ".env", ".config",
        "tsconfig", "vite.config", "next.config", "webpack.config",
        "babel.config", "jest.config", "vitest.config", "eslint",
        "prettier", ".gitignore", ".dockerignore", "dockerfile"
    ]
    filename_lower = filename.lower()
    return any(pattern in filename_lower for pattern in config_patterns)


def _get_directory_summary(dir_path: Path) -> Dict:
    """Get a summary of files in a directory."""
    try:
        files = [f.name for f in dir_path.iterdir() if f.is_file() and not f.name.startswith(".")]
        subdirs = [d.name for d in dir_path.iterdir() if d.is_dir() and d.name not in IGNORE_DIRS]

        return {
            "file_count": len(files),
            "subdir_count": len(subdirs),
            "subdirs": subdirs[:10]  # Limit to first 10
        }
    except PermissionError:
        return {"file_count": 0, "subdir_count": 0, "subdirs": []}


def _contains_source_files(dir_path: Path) -> bool:
    """Check if directory contains source code files."""
    source_extensions = {".ts", ".tsx", ".js", ".jsx", ".py", ".go", ".rs", ".java", ".cpp", ".c", ".h"}

    try:
        for item in dir_path.iterdir():
            if item.is_file() and item.suffix in source_extensions:
                return True
    except PermissionError:
        pass

    return False


if __name__ == "__main__":
    import sys

    # Get project path from command line or use current directory
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 4

    # Run analysis
    output = analyze_structure(project_path, max_depth)
    print(output)
