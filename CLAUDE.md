# paperstack

## Available skills

- `/draft-review` — Pre-submission reviewer simulation with venue-aware critique and revision checklist
- `/research-intake` — Define a research question with forcing questions that demand precision
- `/literature-map` — Map the research landscape around a defined question
- `/paper-triage` — Prioritize papers for reading by relevance, not familiarity
- `/paper-read` — Deep-read a paper through 6 analytical lenses
- `/paper-critic` — Adversarial critique with claim-evidence alignment
- `/compare-papers` — Compare papers side-by-side on research-relevant dimensions
- `/synthesis` — Synthesize findings into a position you can defend

## Project structure

```
.paperstack/                   Draft review outputs and venue cache
docs/research/current/         Research artifacts for the active topic
papers/cards/                  Paper cards (one per paper, slug: author-year-shortitle)
papers/critiques/              Paper critiques (one per paper)
papers/metadata/               Structured metadata files
templates/                     Templates defining required sections
scripts/                       Python helpers (stdlib only)
examples/                      Worked examples
```

## Conventions

**Paper IDs**: Slugified as `author-year-shortitle`. Example: `lewis-2020-rag`, `vaswani-2017-attention`. Use lowercase, hyphens only. First author's last name.

**Artifact paths**: Research-level artifacts go in `docs/research/current/`. Paper-specific artifacts go in `papers/cards/` and `papers/critiques/`. Draft review artifacts go in `.paperstack/`.

**Draft review outputs**: `/draft-review` writes to `.paperstack/` in the workspace root. `latest-review.md` is always the most recent review. Timestamped versions are preserved in `.paperstack/history/`. Venue guidance cache files live in `.paperstack/cache/venue-guidance/`. These are real user-facing artifacts plus tool-managed cache, not disposable scratch space.

**Artifact continuity**: Skills append or update existing artifacts. They NEVER destroy prior work. If a research brief already exists, the skill should read it first and ask the user whether to update or start fresh.

**Required prior artifacts**: Each skill declares what it reads. If a required artifact is missing, STOP and tell the user which skill to run first:
- `/draft-review` requires a manuscript in the workspace (detects automatically)
- `/literature-map` requires `research-brief.md`
- `/paper-triage` requires `research-brief.md` + `literature-map.md`
- `/paper-critic` requires the paper's card in `papers/cards/`
- `/compare-papers` requires at least 2 paper cards
- `/synthesis` requires `research-brief.md` (warns if fewer than 3 paper cards)

## Anti-sycophancy mandate

This applies to ALL paperstack skills. Never use vague praise about papers or research.

**Banned phrases:**
- "This is an interesting paper" — say WHAT is interesting and WHY with evidence
- "The authors make a compelling argument" — name WHICH argument and WHAT evidence supports it
- "The methodology seems reasonable" — specify WHICH aspects and WHAT would make it unreasonable
- "The results are promising" — name WHICH results, what they prove, and what they don't
- "There are some limitations" — name them specifically, assess how they threaten the claims

**Always do:**
- Take a position on every claim. State your position AND what evidence would change it.
- Name the specific weakness, not the category.
- Challenge the strongest version of the argument, not a strawman.
- When uncertain, say "I am uncertain because X" — not "this is complex."

## Templates

Templates in `templates/` define required sections for each artifact type. Skills should ensure all required sections are populated. The `scripts/validate_markdown.py` helper can check this.
