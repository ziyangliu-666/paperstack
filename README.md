# paperstack

A Claude Code skill repository that turns Claude into a rigorous academic research partner — from first idea to final submission.

paperstack covers the full research lifecycle:

1. **Idea development**: Stress-test, sharpen, and frame your research ideas before committing months of work.
2. **Research workflows**: Study a topic through structured reading, adversarial critique, cross-paper comparison, and synthesis.
3. **Draft review**: Review your own paper before submission. Get conference-style feedback that exposes rejection risk.

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
| "Is my idea any good?" | Stress-test with 5 forcing questions before committing months of work |

## Skills

### Idea Development

| Skill | What it does |
|---|---|
| `/idea-test` | Stress-test an idea before you commit. 5 forcing questions on novelty, significance, baselines, and feasibility. Verdict: PURSUE / REFINE / PIVOT / ABANDON. |
| `/idea-sharpen` | Sharpen a rough idea into a precise contribution. Forces draft abstract, positioning against 3 specific papers, mock rebuttal, killer figure, and experimental plan. |
| `/contribution-frame` | Frame results into a publishable contribution. Forces articulation of insights over methods, tests structural fragility, preempts rejection. |

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

### Full lifecycle (idea through submission)

```
/idea-test           Is the idea worth pursuing?
        |
        v
/idea-sharpen        Sharpen into a precise claim (repeat until sharp)
        |
        v
/research-intake     Define the reading question
        |
        v
/literature-map      Map the landscape
        |
        v
/paper-read          Deep-read each paper
        |
        v
/paper-critic        Critique each paper
        |
        v
/synthesis           Synthesize findings
        |
        v
  [run experiments]
        |
        v
/contribution-frame  Frame results into a paper
        |
        v
  [write the draft]
        |
        v
/draft-review        Review before submission
```

You don't have to run every skill. Enter at any point. The sequence is a guide, not a cage.

### Quick idea validation

```
/idea-test
```

One command to stress-test an idea before committing. Get a verdict (PURSUE / REFINE / PIVOT / ABANDON), risk map, and a "next 48 hours" plan.

### Author self-review

```
/draft-review
```

`/draft-review` scans your workspace for the manuscript, asks for the target venue, and generates a **conference-style review** with a **revision checklist**. Output goes to `.paperstack/`.

## Who this is for

- **Researchers with a new idea** who want honest validation before committing months
- **Authors preparing to submit** who want brutally honest pre-submission feedback
- **PhD students** doing literature reviews or developing thesis proposals
- **Engineers** reading papers to understand what to implement
- **Anyone stuck between results and paper** who can't articulate the contribution

## Install

### Option A: One-liner (paste into Claude Code)

Open Claude Code and paste this:

> Install paperstack: run **`git clone https://github.com/ziyangliu-666/paperstack.git ~/.claude/skills/paperstack`** then add a "paperstack" section to CLAUDE.md that lists the available skills: /idea-test, /idea-sharpen, /contribution-frame, /draft-review, /research-intake, /literature-map, /paper-triage, /paper-read, /paper-critic, /compare-papers, /synthesis.

Claude does the rest.

### Option B: Manual install

```bash
git clone https://github.com/ziyangliu-666/paperstack.git ~/.claude/skills/paperstack
```

Add to your `CLAUDE.md` (project or `~/.claude/CLAUDE.md`):

```markdown
## paperstack
Available skills: /idea-test, /idea-sharpen, /contribution-frame, /draft-review,
/research-intake, /literature-map, /paper-triage, /paper-read, /paper-critic,
/compare-papers, /synthesis.
```

### Add to a repo (so collaborators get it)

```bash
cp -Rf ~/.claude/skills/paperstack .claude/skills/paperstack
rm -rf .claude/skills/paperstack/.git
```

Commit `.claude/skills/paperstack/` to your repo. `git clone` just works for everyone.

## Project structure

```
paperstack/
  .paperstack/                 # All paperstack outputs (per workspace)
    ideas/                     #   Idea assessments from /idea-test
    briefs/                    #   Idea briefs from /idea-sharpen
    frames/                    #   Contribution frames from /contribution-frame
    latest-review.md           #   Latest draft review
    history/                   #   Timestamped review history
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
    idea-test/                 # Idea assessment example
  .claude/skills/paperstack/   # Skill definitions
```

## Design principles

1. **Evidence first** — Separate claims from interpretation. Record uncertainty. Never overstate.
2. **Multi-lens reading** — Every paper analyzed from 6 perspectives, not just summarized.
3. **Artifact chaining** — Each skill reads prior artifacts and writes new ones. Research builds on itself.
4. **Forcing questions** — 33 probing questions across all workflows that demand specificity and honesty.
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
