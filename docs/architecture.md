# Architecture

## Core idea

paperstack chains research artifacts through 7 skills. Each skill reads prior artifacts and writes new ones to deterministic paths. Every skill enforces intellectual rigor through forcing questions — probing questions that demand specificity, challenge assumptions, and refuse vague answers.

## Artifact dependency graph

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

## Artifact chaining table

| Skill | Reads | Writes |
|---|---|---|
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

There are 18 forcing questions across the full workflow:
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

## References pattern

Long rubrics and detailed evaluation matrices live in `references/` subdirectories within each skill, not inline in the SKILL.md. This keeps SKILL.md files readable while making detailed guidance available when needed.

- `research-intake/references/intake-rubric.md` — question sharpness criteria
- `paper-read/references/multi-lens-rubric.md` — detailed per-lens reading guidance
- `paper-critic/references/critique-rubric.md` — evaluation matrix with scoring criteria

Skills reference these files with: "Read `references/<filename>` for the detailed rubric."

## Design principles

1. **Local-first**: No database, no web service, no frontend. Plain files and folders.
2. **Deterministic paths**: Every artifact has one canonical location. No ambiguity.
3. **Append, don't destroy**: Skills update existing artifacts safely. Prior work is preserved.
4. **Templates define structure**: Required sections are defined in `templates/`. Skills enforce them.
5. **Minimal but extensible**: 7 skills, not 70. Add more when you need them.
