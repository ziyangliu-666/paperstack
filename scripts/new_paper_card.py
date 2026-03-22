#!/usr/bin/env python3
"""Create a new paper card from template.

Generates a slugified paper ID and creates the card file.

Usage:
    python scripts/new_paper_card.py "Lewis" "2020" "Retrieval-Augmented Generation"
    python scripts/new_paper_card.py "Vaswani" "2017" "Attention Is All You Need"
"""

import os
import re
import sys
from datetime import date


def slugify(text: str) -> str:
    """Convert text to a short filesystem-safe slug."""
    text = text.lower().strip()
    # Take first few meaningful words
    words = re.sub(r"[^\w\s]", "", text).split()
    # Keep up to 3 words, skip common words
    skip = {"a", "an", "the", "is", "are", "of", "for", "in", "on", "to", "and", "with", "all", "you"}
    meaningful = [w for w in words if w not in skip][:3]
    return "-".join(meaningful) if meaningful else "-".join(words[:2])


def main():
    if len(sys.argv) < 4:
        print("Usage: python scripts/new_paper_card.py AUTHOR YEAR TITLE")
        print('Example: python scripts/new_paper_card.py "Lewis" "2020" "Retrieval-Augmented Generation"')
        sys.exit(1)

    author = sys.argv[1].lower().strip()
    year = sys.argv[2].strip()
    title = sys.argv[3]
    short_title = slugify(title)

    paper_id = f"{author}-{year}-{short_title}"
    today = date.today().isoformat()

    # Find repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    # Ensure directories exist
    cards_dir = os.path.join(repo_root, "papers", "cards")
    os.makedirs(cards_dir, exist_ok=True)

    card_path = os.path.join(cards_dir, f"{paper_id}.md")

    if os.path.exists(card_path):
        print(f"Card already exists: papers/cards/{paper_id}.md")
        sys.exit(1)

    # Read template
    template_path = os.path.join(repo_root, "templates", "paper-card.template.md")
    if not os.path.exists(template_path):
        print(f"Template not found: {template_path}")
        sys.exit(1)

    with open(template_path, "r") as f:
        content = f.read()

    # Fill placeholders
    content = content.replace("{TITLE}", title)
    content = content.replace("{author-year-shortitle}", paper_id)
    content = content.replace("{full title}", title)
    content = content.replace("{author list}", f"{sys.argv[1]} et al.")
    content = content.replace("{year}", year)
    content = content.replace("{date}", today)

    with open(card_path, "w") as f:
        f.write(content)

    print(f"Created papers/cards/{paper_id}.md")
    print(f"Next step: run /paper-read to fill in the card.")


if __name__ == "__main__":
    main()
