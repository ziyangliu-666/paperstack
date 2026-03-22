#!/usr/bin/env python3
"""Initialize a new research topic.

Creates the directory structure and copies templates into place.

Usage:
    python scripts/init_research.py "My Research Topic"
"""

import os
import re
import shutil
import sys
from datetime import date


def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/init_research.py \"My Research Topic\"")
        sys.exit(1)

    topic = sys.argv[1]
    today = date.today().isoformat()

    # Find the repo root (where this script lives is scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    # Create directories
    dirs = [
        "docs/research/current",
        "papers/cards",
        "papers/critiques",
        "papers/metadata",
    ]
    for d in dirs:
        path = os.path.join(repo_root, d)
        os.makedirs(path, exist_ok=True)
        print(f"  Created {d}/")

    # Copy templates into research/current/ with placeholders filled
    template_dir = os.path.join(repo_root, "templates")
    current_dir = os.path.join(repo_root, "docs", "research", "current")

    template_map = {
        "research-brief.template.md": "research-brief.md",
        "literature-map.template.md": "literature-map.md",
        "reading-queue.template.md": "reading-queue.md",
        "comparison-matrix.template.md": "comparison-matrix.md",
        "synthesis.template.md": "synthesis.md",
    }

    for template_name, output_name in template_map.items():
        src = os.path.join(template_dir, template_name)
        dst = os.path.join(current_dir, output_name)

        if os.path.exists(dst):
            print(f"  Skipped {output_name} (already exists)")
            continue

        if not os.path.exists(src):
            print(f"  Warning: template {template_name} not found")
            continue

        with open(src, "r") as f:
            content = f.read()

        # Fill basic placeholders
        content = content.replace("{TOPIC}", topic)
        content = content.replace("{DATE}", today)

        with open(dst, "w") as f:
            f.write(content)

        print(f"  Created {output_name}")

    print(f"\nResearch topic '{topic}' initialized.")
    print(f"Next step: run /research-intake to define your research question.")


if __name__ == "__main__":
    main()
