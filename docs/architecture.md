# Architecture

## Core idea

paperstack chains research artifacts through 11 skills. Each skill reads prior artifacts and writes new ones to deterministic paths. Every skill enforces intellectual rigor through forcing questions — probing questions that demand specificity, challenge assumptions, and refuse vague answers.

The skills split into three paths:
- **Idea development** (3 skills): idea stress-test → refinement → contribution framing
- **Research workflow** (7 skills): question framing → reading → critique → synthesis
- **Author self-review** (1 skill): manuscript → conference-style review → revision checklist

## Artifact dependency graph

### Idea development

```
.paperstack/ideas/{idea}.md    (from /idea-test)
    |
    v
.paperstack/briefs/{idea}.md   (from /idea-sharpen, iterative)
    |
    v
  [research pipeline + experiments]
    |
    v
.paperstack/frames/{paper}.md  (from /contribution-frame)
```

### Research workflow

```
research-brief.md  (from /research-intake)
    |
    v
literature-map.md  (from /literature-map)
    |
    v
reading-queue.md   (from /paper-triage)
    |
    |   paper-card.md        (from /paper-read, per paper)
    |       |
    |       v
    |   paper-critique.md    (from /paper-critic, per paper)
    |       |
    +-------+
    |
    v
comparison-matrix.md  (from /compare-papers)
    |
    v
synthesis.md  (from /synthesis)
```

### Author self-review (independent path)

```
current workspace
    |
    v
manuscript detection + whitelist scan
    |
    v
venue guidance lookup
    |   ├─ live success
    |   ├─ cache fallback (loud)
    |   └─ generic fallback (loud)
    |
    v
.paperstack/
    ├─ latest-review.md
    ├─ history/YYYYMMDD-HHMMSS-review.md
    └─ cache/venue-guidance/{venue-key}.md
```

## Artifact chaining table

| Skill | Reads | Writes |
|---|---|---|
| `/idea-test` | (nothing, or prior idea artifacts) | `.paperstack/ideas/{idea}.md` |
| `/idea-sharpen` | Prior idea assessment (optional) | `.paperstack/briefs/{idea}.md` |
| `/contribution-frame` | Experimental results (user-provided) | `.paperstack/frames/{paper}.md` |
| `/draft-review` | Workspace manuscript + support files | `.paperstack/latest-review.md`, `.paperstack/history/*` |
| `/research-intake` | (nothing) | `docs/research/current/research-brief.md` |
| `/literature-map` | `research-brief.md` | `docs/research/current/literature-map.md` |
| `/paper-triage` | `research-brief.md`, `literature-map.md` | `docs/research/current/reading-queue.md` |
| `/paper-read` | `research-brief.md` | `papers/cards/<paper-id>.md` |
| `/paper-critic` | `papers/cards/<paper-id>.md` | `papers/critiques/<paper-id>.md` |
| `/compare-papers` | `papers/cards/*.md`, `research-brief.md` | `docs/research/current/comparison-matrix.md` |
| `/synthesis` | All prior artifacts | `docs/research/current/synthesis.md` |

## Forcing questions philosophy

paperstack uses **forcing questions** — diagnostic questions that refuse to accept vague, hedged, or comfortable answers. This pattern is adapted from YC office hours diagnostic methodology.

Each forcing question has four components:
1. **The question itself** — direct, specific, often uncomfortable
2. **"Push until you hear:"** — what a good answer sounds like
3. **"Red flags:"** — patterns that indicate the answer isn't sharp enough
4. **BAD vs GOOD examples** — concrete contrast between soft exploration and rigorous diagnosis

**Why this matters for research**: The most common failure mode in literature review is confirmation bias — reading papers that confirm what you already believe, summarizing instead of critiquing, and hedging instead of taking positions. Forcing questions counter every one of these failure modes.

There are 33 forcing questions across all workflows:
- 5 in `/idea-test` (claim, baseline, significance, novelty, cheap test)
- 5 in `/idea-sharpen` (draft abstract, positioning, mock rebuttal, killer figure, experimental plan)
- 5 in `/contribution-frame` (elevator pitch, surprise test, fragility, competition, preemptive rejection)
- 4 in `/research-intake` (intellectual honesty about the question itself)
- 1 in `/literature-map` (challenging familiarity bias)
- 1 in `/paper-triage` (relevance vs. familiarity)
- 6 in `/paper-read` (one per analytical lens)
- 2 in `/paper-critic` (evidence scrutiny and honest concession)
- 1 in `/compare-papers` (dimension selection rigor)
- 3 in `/synthesis` (commitment to a position)

## Anti-sycophancy for academic context

In software reviews, sycophancy sounds like "that's an interesting approach." In academic reading, sycophancy sounds like "the paper makes a compelling argument" or "the results are promising." Both are meaningless without specifics.

paperstack's anti-sycophancy rules target two directions:
1. **Don't flatter the user** — "Being open-minded is great!" when they haven't examined their assumptions
2. **Don't defer to the paper** — "The authors present a novel method" when the novelty is incremental at best

The replacement for both: specificity. Name the claim. Cite the evidence. State your position. Say what would change your mind.

## Skill discovery

Each skill lives in its own directory at the repo root (e.g., `idea-test/SKILL.md`). When the repo is cloned to `~/.claude/skills/paperstack/`, the `setup` script creates symlinks so Claude Code can discover each skill:

```
~/.claude/skills/idea-test  →  paperstack/idea-test
~/.claude/skills/paper-read →  paperstack/paper-read
...
```

This follows the same pattern used by gstack: mono-repo at `~/.claude/skills/<name>/`, symlinks for each skill.

## References pattern

Long rubrics and detailed evaluation matrices live in `references/` subdirectories within each skill, not inline in the SKILL.md. This keeps SKILL.md files readable while making detailed guidance available when needed.

- `research-intake/references/intake-rubric.md` — question sharpness criteria
- `paper-read/references/multi-lens-rubric.md` — detailed per-lens reading guidance
- `paper-critic/references/critique-rubric.md` — evaluation matrix with scoring criteria
- `draft-review/references/review-rubric.md` — pre-submission review dimensions

Skills reference these files with: "Read `references/<filename>` for the detailed rubric."

## Design principles

1. **Local-first**: No database, no web service, no frontend. Plain files and folders.
2. **Deterministic paths**: Every artifact has one canonical location. No ambiguity.
3. **Append, don't destroy**: Skills update existing artifacts safely. Prior work is preserved.
4. **Templates define structure**: Required sections are defined in `templates/`. Skills enforce them.
5. **Minimal but extensible**: 11 skills, not 110. Add more when you need them.
6. **Independent paths coexist**: Idea development, research reading, and author self-review are separate artifact chains. They share critique dimensions but not output paths.
7. **Iterative by design**: `/idea-sharpen` can be re-run to progressively refine. `/draft-review` preserves history for comparison across revisions.
