# paperstack

A Claude Code skill repository that turns Claude into a rigorous academic research partner — and a brutally honest pre-submission reviewer.

paperstack does two things:

1. **Research workflows**: Study a topic through structured reading, adversarial critique, cross-paper comparison, and synthesis.
2. **Draft review**: Review your own paper before submission. Get conference-style feedback that exposes rejection risk — the kind of structured, uncomfortable, venue-aware critique that real reviewers deliver.

## Why this exists

Most AI paper tools produce summaries. Summaries are not understanding — and summaries won't save you from Reviewer 2.

Understanding requires you to state what you believe before reading, identify the weakest link in an argument, separate claims from evidence, and take a position you can defend. paperstack forces this discipline at every step.

Pre-submission review requires something harder: simulating the scrutiny of a hostile but fair reviewer who knows the field. paperstack's `/draft-review` does this by scanning your workspace, reading your full manuscript, and generating a conference-style review with verdict, major concerns, and a revision checklist.

| Without paperstack | With paperstack |
|---|---|
| "Summarize this paper" | Multi-lens reading through 6 analytical perspectives |
| Vague research questions | Forcing questions that demand precision and falsifiability |
| Cherry-picked papers | Systematic literature mapping with explicit triage criteria |
| Passive reading | Adversarial critique with claim-evidence alignment |
| "The paper is interesting" | Specific: WHAT is interesting, WHY, and what evidence supports it |
| Summary of summaries | Synthesis that identifies consensus, conflicts, and gaps |
| Submit and pray | Conference-style review before submission, with repair checklist |

## Skills

### Research Workflow

| Skill | What it does |
|---|---|
| `/research-intake` | Define a research question with precision. Forces honesty about priors, scope, and success criteria. |
| `/literature-map` | Map the research landscape — clusters, timelines, key papers, datasets, metrics, gaps. |
| `/paper-triage` | Prioritize papers for reading. Rank by relevance, not familiarity. |
| `/paper-read` | Deep-read a paper through 6 lenses: Author, Reviewer, Skeptic, Reproducer, Practitioner, Student. |
| `/paper-critic` | Adversarial critique — claim-evidence alignment, novelty, baseline fairness, reproducibility. |
| `/compare-papers` | Compare papers side-by-side on dimensions that matter for your question. |
| `/synthesis` | Synthesize findings into a coherent answer. No hedging. Take a position. |

### Pre-Submission Review

| Skill | What it does |
|---|---|
| `/draft-review` | Review your own paper before submission. Scans your workspace, generates a conference-style review with venue-aware critique, and outputs a prioritized revision checklist. |

## Workflows

### Research workflow

```
/research-intake     Define the question
        |
        v
/literature-map      Map the landscape
        |
        v
/paper-triage        Decide what to read
        |
        v
/paper-read          Deep-read each paper (repeat per paper)
        |
        v
/paper-critic        Critique each paper (repeat per paper)
        |
        v
/compare-papers      Compare across papers
        |
        v
/synthesis           Answer the question
```

You don't have to run every skill. Skip `/paper-triage` if you already know what to read. Skip `/literature-map` if you're reading a single paper. The sequence is a guide, not a cage.

### Author self-review workflow

```
/draft-review        Review your draft before submission
```

That's it. One command. `/draft-review` scans your workspace for the manuscript, asks for the target venue, and generates:

- A **conference-style review** with verdict, strengths, major/minor concerns, and reviewer questions
- A **revision checklist** with prioritized repair tasks (MUST-FIX / SHOULD-FIX / NICE-TO-HAVE)

Output goes to `.paperstack/` in your workspace — a stable `latest-review.md`, timestamped history, and venue-guidance cache files for repeat runs.

## Who this is for

- **Authors preparing to submit** a paper and wanting honest pre-submission feedback
- **PhD applicants** preparing research proposals
- **Graduate students** doing literature reviews
- **Engineers** reading papers to understand what to implement
- **Researchers** exploring a new area systematically
- **Builders** who need paper understanding, not paper collection

## Install

Clone this repository:

```bash
git clone <repo-url> ~/.claude/skills/paperstack
```

Add to your project's `CLAUDE.md` or `~/.claude/CLAUDE.md`:

```markdown
# paperstack

Available skills:
- `/draft-review` — review your own draft before submission
- `/research-intake` — define research question
- `/literature-map` — map research landscape
- `/paper-triage` — prioritize reading
- `/paper-read` — deep-read a paper
- `/paper-critic` — adversarial critique
- `/compare-papers` — cross-paper comparison
- `/synthesis` — synthesize findings
```

## Project structure

```
paperstack/
  .paperstack/                 # Draft review outputs (per workspace)
    latest-review.md           #   Latest review artifact
    history/                   #   Timestamped review history
    cache/venue-guidance/      #   Cached official venue guidance
  docs/
    architecture.md            # How artifact chaining works
    workflows.md               # Recommended sequences
    research/current/          # Active research artifacts
  papers/
    cards/                     # Paper cards (one per paper)
    critiques/                 # Paper critiques (one per paper)
    metadata/                  # Structured metadata
  templates/                   # Markdown templates for all artifacts
  scripts/                     # Optional Python helpers
  examples/
    sample-topic/              # Research workflow example
    draft-review/              # Draft review output example
  .claude/skills/paperstack/   # Skill definitions
```

## Design principles

1. **Evidence first** — Separate claims from interpretation. Record uncertainty. Never overstate.
2. **Multi-lens reading** — Every paper analyzed from 6 perspectives, not just summarized.
3. **Artifact chaining** — Each skill reads prior artifacts and writes new ones. Research builds on itself.
4. **Forcing questions** — 18 probing questions across the workflow that demand specificity and honesty.
5. **Anti-sycophancy** — "The paper is interesting" is banned. Say what, why, and with what evidence.
6. **Local-first** — No database, no web service, no frontend. Plain files in your workspace.
7. **Loud degradation** — If venue-specific guidance is unavailable, paperstack must say so explicitly and fall back to cache or generic review criteria.

## Helper scripts

Optional Python scripts (stdlib only, no dependencies):

```bash
python scripts/init_research.py "My Research Topic"     # Set up directory structure
python scripts/new_paper_card.py "Lewis" "2020" "RAG"   # Create a paper card
python scripts/validate_markdown.py papers/cards/*.md    # Check required sections
```
