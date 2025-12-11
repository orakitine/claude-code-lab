#!/usr/bin/env python3
"""
Doc Vault Index Manager
Helps update README.md index when docs are added.
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def update_readme(name: str, description: str, date_str: str = None):
    """
    Update README.md with new doc entry.

    Args:
        name: Doc name (e.g., "tanstack-query-options")
        description: One-sentence description
        date_str: Date string (YYYY-MM-DD), defaults to today
    """
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # Find README.md
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent
    readme_path = skill_dir / "README.md"

    if not readme_path.exists():
        print(f"Error: README.md not found at {readme_path}", file=sys.stderr)
        return False

    # Read current README
    content = readme_path.read_text()

    # Parse library name from doc name (e.g., "tanstack-query-options" → "TanStack Query")
    library = infer_library_name(name)

    # Create entry
    entry = f"- **{name}** ({date_str}) - {description}"

    # Find the "## Cached Documents" section
    if "*No documents cached yet" in content:
        # First doc!
        new_section = f"""## Cached Documents

### {library}
{entry}

---

**Total:** 1 document
**Last updated:** {date_str}"""
        content = content.replace(
            "## Cached Documents\n\n*No documents cached yet. Add your first doc to get started!*\n\n---\n\n**Total:** 0 documents\n**Last updated:** Never",
            new_section
        )
    else:
        # Add to existing section
        # Try to find the library section
        library_header = f"### {library}"
        if library_header in content:
            # Add to existing library section
            # Find the line after the library header
            lines = content.split('\n')
            new_lines = []
            found_library = False
            inserted = False

            for i, line in enumerate(lines):
                new_lines.append(line)
                if line == library_header and not inserted:
                    found_library = True
                elif found_library and line.startswith('- **') and not inserted:
                    # Insert before this line (alphabetically)
                    if name < line.split('**')[1]:
                        new_lines.insert(-1, entry)
                        inserted = True
                elif found_library and (line.startswith('###') or line == '---') and not inserted:
                    # Insert before next section or separator
                    new_lines.insert(-1, entry)
                    inserted = True

            if not inserted and found_library:
                # Add to end of library section
                for i in range(len(new_lines) - 1, -1, -1):
                    if new_lines[i].startswith('- **'):
                        new_lines.insert(i + 1, entry)
                        break

            content = '\n'.join(new_lines)
        else:
            # Create new library section
            # Find where to insert (before "---")
            separator_pos = content.find('\n---\n\n**Total:**')
            if separator_pos > 0:
                new_section = f"\n### {library}\n{entry}\n"
                content = content[:separator_pos] + new_section + content[separator_pos:]

        # Update count and date
        # Count total docs
        doc_count = content.count('- **')
        content = content.replace(
            '**Total:** 0 document',
            f'**Total:** {doc_count} document{"s" if doc_count != 1 else ""}'
        )
        # Update the number if it exists
        import re
        content = re.sub(
            r'\*\*Total:\*\* \d+ documents?',
            f'**Total:** {doc_count} document{"s" if doc_count != 1 else ""}',
            content
        )
        content = re.sub(
            r'\*\*Last updated:\*\* [\d-]+',
            f'**Last updated:** {date_str}',
            content
        )
        content = content.replace('**Last updated:** Never', f'**Last updated:** {date_str}')

    # Write updated README
    readme_path.write_text(content)
    print(f"✓ Updated README.md: added {name}", file=sys.stderr)
    return True


def infer_library_name(doc_name: str) -> str:
    """Infer library display name from doc name."""
    # Common mappings
    mappings = {
        'tanstack': 'TanStack Query',
        'prisma': 'Prisma',
        'react': 'React',
        'nextjs': 'Next.js',
        'next': 'Next.js',
        'zod': 'Zod',
        'trpc': 'tRPC',
        'drizzle': 'Drizzle',
        'typescript': 'TypeScript',
        'vite': 'Vite',
        'vitest': 'Vitest',
    }

    # Check prefixes
    name_lower = doc_name.lower()
    for key, display in mappings.items():
        if name_lower.startswith(key):
            return display

    # Default: capitalize first part before hyphen
    parts = doc_name.split('-')
    return parts[0].capitalize()


def list_docs():
    """List all cached docs."""
    script_dir = Path(__file__).parent
    cache_dir = script_dir.parent / "cache"

    if not cache_dir.exists():
        print("No docs cached yet.", file=sys.stderr)
        return

    docs = sorted(cache_dir.glob("*.md"))
    if not docs:
        print("No docs cached yet.", file=sys.stderr)
        return

    print(f"Found {len(docs)} cached document(s):", file=sys.stderr)
    for doc in docs:
        print(f"  • {doc.name}", file=sys.stderr)


def main():
    """CLI interface."""
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  manage_index.py update <name> <description> [date]", file=sys.stderr)
        print("  manage_index.py list", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_docs()
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: update requires <name> <description>", file=sys.stderr)
            sys.exit(1)
        name = sys.argv[2]
        description = sys.argv[3]
        date_str = sys.argv[4] if len(sys.argv) > 4 else None
        success = update_readme(name, description, date_str)
        sys.exit(0 if success else 1)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
