# paperstack

A Claude Code skill repository that turns Claude into a rigorous academic research partner.

paperstack helps you study a research topic through a structured sequence — from question framing through literature mapping, deep reading, adversarial critique, cross-paper comparison, and final synthesis. Every step enforces intellectual honesty through forcing questions that challenge vague thinking, unstated assumptions, and confirmation bias.

## Why this exists

Most AI paper tools produce summaries. Summaries are not understanding.

Understanding requires you to state what you believe before reading, identify the weakest link in an argument, separate claims from evidence, and take a position you can defend. paperstack forces this discipline at every step.

| Without paperstack | With paperstack |
|---|---|
| "Summarize this paper" | Multi-lens reading through 6 analytical perspectives |
| Vague research questions | Forcing questions that demand precision and falsifiability |
| Cherry-picked papers | Systematic literature mapping with explicit triage criteria |
| Passive reading | Adversarial critique with claim-evidence alignment |
| "The paper is interesting" | Specific: WHAT is interesting, WHY, and what evidence supports it |
| Summary of summaries | Synthesis that identifies consensus, conflicts, and gaps |

## Skills

| Skill | What it does |
|---|---|
| `/research-intake` | Define a research question with precision. Forces honesty about priors, scope, and success criteria. |
| `/literature-map` | Map the research landscape — clusters, timelines, key papers, datasets, metrics, gaps. |
| `/paper-triage` | Prioritize papers for reading. Rank by relevance, not familiarity. |
| `/paper-read` | Deep-read a paper through 6 lenses: Author, Reviewer, Skeptic, Reproducer, Practitioner, Student. |
| `/paper-critic` | Adversarial critique — claim-evidence alignment, novelty, baseline fairness, reproducibility. |
| `/compare-papers` | Compare papers side-by-side on dimensions that matter for your question. |
| `/synthesis` | Synthesize findings into a coherent answer. No hedging. Take a position. |

## Workflow

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

## Who this is for

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
  docs/
    architecture.md          # How artifact chaining works
    workflows.md             # Recommended sequences
    research/current/        # Active research artifacts
  papers/
    cards/                   # Paper cards (one per paper)
    critiques/               # Paper critiques (one per paper)
    metadata/                # Structured metadata
  templates/                 # Markdown templates for all artifacts
  scripts/                   # Optional Python helpers
  examples/sample-topic/     # Worked example
  .claude/skills/paperstack/ # Skill definitions
```

## Design principles

1. **Evidence first** — Separate claims from interpretation. Record uncertainty. Never overstate.
2. **Multi-lens reading** — Every paper analyzed from 6 perspectives, not just summarized.
3. **Artifact chaining** — Each skill reads prior artifacts and writes new ones. Research builds on itself.
4. **Forcing questions** — 18 probing questions across the workflow that demand specificity and honesty.
5. **Anti-sycophancy** — "The paper is interesting" is banned. Say what, why, and with what evidence.

## Helper scripts

Optional Python scripts (stdlib only, no dependencies):

```bash
python scripts/init_research.py "My Research Topic"     # Set up directory structure
python scripts/new_paper_card.py "Lewis" "2020" "RAG"   # Create a paper card
python scripts/validate_markdown.py papers/cards/*.md    # Check required sections
```
