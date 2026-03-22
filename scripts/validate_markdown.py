#!/usr/bin/env python3
"""Validate that markdown files have required headings.

Checks whether generated artifacts contain the required sections
defined by their template type. Also warns about placeholder text
and empty sections.

Usage:
    python scripts/validate_markdown.py papers/cards/lewis-2020-rag.md
    python scripts/validate_markdown.py docs/research/current/*.md
    python scripts/validate_markdown.py --all
"""

import os
import re
import sys


# Required headings per artifact type (matched by filename pattern)
REQUIRED_HEADINGS = {
    "draft-review": [
        "Paper Summary",
        "Strengths",
        "Major Concerns",
        "Minor Concerns",
        "Questions for Authors",
        "Missing References",
        "Verdict",
        "Revision Checklist",
    ],
    "research-brief": [
        "Research Question",
        "Motivation",
        "Prior Beliefs",
        "Scope",
        "Success Criteria",
        "Key Terms",
        "Keywords and Search Strategy",
        "Dissenting Framings",
    ],
    "literature-map": [
        "Overview",
        "Research Clusters",
        "Timeline of Key Developments",
        "Key Datasets",
        "Key Metrics and Benchmarks",
        "Gaps in the Literature",
    ],
    "reading-queue": [
        "Queue Summary",
        "P0",
        "P1",
    ],
    "paper-card": [
        "Metadata",
        "One-Paragraph Summary",
        "Problem",
        "Approach",
        "Key Claims",
        "Evidence Map",
        "Author Lens",
        "Reviewer Lens",
        "Skeptic Lens",
        "Reproducer Lens",
        "Practitioner Lens",
        "Student Lens",
        "Open Questions",
        "Confidence Rating",
    ],
    "paper-critique": [
        "Claim-Evidence Alignment",
        "Methodology Assessment",
        "Novelty Assessment",
        "Reproducibility Assessment",
        "Hidden Assumptions",
        "Strongest Criticism",
        "Strongest Defense",
        "Verdict",
    ],
    "comparison-matrix": [
        "Papers Compared",
        "Comparison Matrix",
        "Key Divergences",
        "Consensus Points",
    ],
    "synthesis": [
        "Answer to the Research Question",
        "Evidence Summary",
        "What Is Actually Known",
        "What Is Still Unclear",
        "Where Papers Conflict",
        "Confidence Assessment",
    ],
}

# Patterns that suggest unfilled template placeholders
PLACEHOLDER_PATTERNS = [
    r"\{[A-Z_]+\}",          # {TOPIC}, {DATE}, etc.
    r"\{[a-z][^}]*\}",       # {description}, {paper}, etc.
]


def detect_type(filepath: str) -> str:
    """Detect artifact type from filename."""
    basename = os.path.basename(filepath).lower()
    if "draft-review" in basename or "sample-review" in basename or "/draft-review/" in filepath:
        return "draft-review"
    elif "research-brief" in basename:
        return "research-brief"
    elif "literature-map" in basename:
        return "literature-map"
    elif "reading-queue" in basename:
        return "reading-queue"
    elif "comparison-matrix" in basename:
        return "comparison-matrix"
    elif "synthesis" in basename:
        return "synthesis"
    elif "critique" in basename or filepath.startswith("papers/critiques/") or "/critiques/" in filepath:
        return "paper-critique"
    elif "paper-card" in basename or filepath.startswith("papers/cards/") or "/cards/" in filepath:
        return "paper-card"
    return ""


def extract_headings(content: str) -> list[str]:
    """Extract markdown headings from content."""
    headings = []
    for line in content.split("\n"):
        match = re.match(r"^#{1,4}\s+(.+)", line)
        if match:
            headings.append(match.group(1).strip())
    return headings


def find_empty_sections(content: str) -> list[str]:
    """Find sections with no content between headings.

    A section with only sub-headings (e.g., ## Scope followed by ### In scope)
    is NOT considered empty — the sub-headings contain the content.
    """
    lines = content.split("\n")
    empty_sections = []
    current_heading = None
    current_level = 0
    has_content = False

    for line in lines:
        match = re.match(r"^(#{1,4})\s+(.+)", line)
        if match:
            level = len(match.group(1))
            heading_text = match.group(2).strip()
            if current_heading and not has_content:
                # A deeper heading counts as content for the parent
                if level <= current_level:
                    empty_sections.append(current_heading)
            current_heading = heading_text
            current_level = level
            has_content = False
        elif line.strip() and not line.startswith("---"):
            has_content = True

    if current_heading and not has_content:
        empty_sections.append(current_heading)

    return empty_sections


def find_placeholders(content: str) -> list[tuple[int, str]]:
    """Find unfilled placeholder patterns with line numbers."""
    results = []
    for i, line in enumerate(content.split("\n"), 1):
        for pattern in PLACEHOLDER_PATTERNS:
            matches = re.findall(pattern, line)
            for match in matches:
                results.append((i, match))
    return results


def validate_file(filepath: str) -> list[str]:
    """Validate a single file. Returns list of issues."""
    issues = []

    if not os.path.exists(filepath):
        return [f"File not found: {filepath}"]

    with open(filepath, "r") as f:
        content = f.read()

    if not content.strip():
        return [f"File is empty: {filepath}"]

    artifact_type = detect_type(filepath)
    if not artifact_type:
        issues.append(f"Could not detect artifact type for: {filepath}")
        return issues

    is_template = "/templates/" in filepath.replace("\\", "/")

    # Check required headings
    headings = extract_headings(content)
    required = REQUIRED_HEADINGS.get(artifact_type, [])
    for req in required:
        if not any(req.lower() in h.lower() for h in headings):
            issues.append(f"Missing required heading: '{req}'")

    # Check for empty sections
    empty = find_empty_sections(content)
    for section in empty:
        issues.append(f"Empty section: '{section}'")

    # Check for placeholders
    if not is_template:
        placeholders = find_placeholders(content)
        for line_num, placeholder in placeholders:
            issues.append(f"Unfilled placeholder on line {line_num}: {placeholder}")

    return issues


def find_all_artifacts(repo_root: str) -> list[str]:
    """Find all markdown artifacts in the repo."""
    files = []
    for dirpath in ["docs/research/current", "papers/cards", "papers/critiques"]:
        full_path = os.path.join(repo_root, dirpath)
        if os.path.isdir(full_path):
            for f in os.listdir(full_path):
                if f.endswith(".md") and f != ".gitkeep":
                    files.append(os.path.join(full_path, f))
    return sorted(files)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_markdown.py FILE [FILE ...]")
        print("       python scripts/validate_markdown.py --all")
        sys.exit(1)

    # Find repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    if sys.argv[1] == "--all":
        files = find_all_artifacts(repo_root)
        if not files:
            print("No artifacts found to validate.")
            sys.exit(0)
    else:
        files = sys.argv[1:]

    total_issues = 0
    for filepath in files:
        # Resolve relative to repo root if needed
        if not os.path.isabs(filepath):
            filepath = os.path.join(repo_root, filepath)

        issues = validate_file(filepath)
        rel_path = os.path.relpath(filepath, repo_root)

        if issues:
            print(f"\n{rel_path}: {len(issues)} issue(s)")
            for issue in issues:
                print(f"  - {issue}")
            total_issues += len(issues)
        else:
            print(f"{rel_path}: OK")

    if total_issues:
        print(f"\nTotal: {total_issues} issue(s) found.")
        sys.exit(1)
    else:
        print(f"\nAll {len(files)} file(s) passed validation.")


if __name__ == "__main__":
    main()
