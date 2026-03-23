# Workflows

## Full lifecycle

```
/idea-test  →  /idea-sharpen  →  /research-intake  →  /literature-map  →  /paper-read  →  /paper-critic  →  /synthesis  →  [experiments]  →  /contribution-frame  →  [writing]  →  /draft-review
```

This is the ideal path. Enter at any point. Each skill is independently usable.

## The research sequence

```
/research-intake  →  /literature-map  →  /paper-triage  →  /paper-read  →  /paper-critic  →  /compare-papers  →  /synthesis
```

The reading pipeline. Each skill builds on prior artifacts. Skip steps when they don't apply.

## Idea development

```
/idea-test  →  /idea-sharpen (repeat)  →  /research-intake  →  [...reading...]  →  /contribution-frame
```

Run `/idea-test` when you have a research idea and want to know if it's worth pursuing. Follow with `/idea-sharpen` to refine the idea into a precise claim, draft abstract, and experimental plan. After experiments, use `/contribution-frame` to frame results into a publishable contribution.

**`/idea-test` output**: `.paperstack/ideas/` — risk map, verdict (PURSUE/REFINE/PIVOT/ABANDON), next 48 hours plan.

**`/idea-sharpen` output**: `.paperstack/briefs/` — 1-sentence claim, draft abstract, positioning triangle, mock rebuttal, killer figure, experimental plan. Re-run to sharpen further.

**`/contribution-frame` output**: `.paperstack/frames/` — contribution statement, story arc, fragility analysis, competition test, recommended paper structure.

## Author self-review

```
/draft-review
```

Run `/draft-review` when you have a manuscript draft and want to simulate what reviewers will say before you submit. The skill:

1. Scans your workspace for the manuscript and support files
2. Asks for the target venue and looks up official reviewer guidance
3. Generates a conference-style review (verdict, strengths, major/minor concerns, reviewer questions)
4. Produces a revision checklist mapping each concern to a repair task

**Output**: `.paperstack/latest-review.md` (plus timestamped history in `.paperstack/history/`)

**When to run**: Before any submission. Also useful mid-writing to check whether the current draft's contribution framing and evidence are clear enough.

**Does NOT require**: Any prior paperstack research artifacts. Works on a standalone manuscript workspace.

**Re-running**: Each run generates a new timestamped review and updates the `latest-review.md` pointer. Prior reviews are preserved in history — compare them to track whether your revisions are addressing the concerns.

---

## When to use each skill

### Starting a new research topic
Run `/research-intake` first. Always. Even if you think you know the question, the forcing questions will sharpen it.

### Mapping the landscape
Run `/literature-map` after you have a research brief. This is especially valuable when you're new to an area and don't know what papers exist.

**Skip if**: You already know the key papers and just need to read them deeply.

### Deciding what to read
Run `/paper-triage` to prioritize your reading queue. Most useful when the literature map surfaced more papers than you can read.

**Skip if**: You have 3 or fewer papers, or you already know the reading order.

### Reading a paper
Run `/paper-read` for each paper you want to understand deeply. This is the core of paperstack — 6 analytical lenses that force you past surface-level comprehension.

**Run multiple times**: Once per paper. Each creates a separate card in `papers/cards/`.

### Critiquing a paper
Run `/paper-critic` after reading a paper to evaluate its claims adversarially. The critique builds on the paper card — you need to read before you can critique.

**Skip if**: The paper is background reading and its specific claims don't matter for your question.

### Comparing papers
Run `/compare-papers` once you have at least 2 paper cards. Most valuable with 3-5 papers that address similar questions with different approaches.

### Synthesizing findings
Run `/synthesis` last. It reads ALL prior artifacts and produces the final answer to your research question. The forcing questions here demand you take a position — no "more research is needed" hedging.

### Reviewing your own draft
Run `/draft-review` when your manuscript draft is in the workspace. No prior paperstack artifacts are needed — this skill operates directly on your manuscript files.

### Testing a research idea
Run `/idea-test` when you have a new idea and want honest validation. No prior artifacts needed. Get a verdict and risk map in one session.

### Sharpening an idea
Run `/idea-sharpen` to turn a rough idea into a precise claim. Can run iteratively — each pass reads the prior brief and pushes further. Most useful after `/idea-test` gives a REFINE verdict.

### Framing results as a contribution
Run `/contribution-frame` after you have experimental results but before writing the paper. Forces you to articulate the insight, not just the method.

## Common workflows

### Quick paper understanding (single paper)
```
/paper-read  →  /paper-critic
```
Skip the full pipeline. Just read and critique one paper.

### Literature review for a thesis chapter
```
/research-intake  →  /literature-map  →  /paper-triage  →  /paper-read (x5-10)  →  /compare-papers  →  /synthesis
```
Full pipeline. The synthesis output can serve as a first draft for the related work section.

### Engineer evaluating a technique
```
/research-intake  →  /paper-read  →  /paper-critic
```
Focus on the Practitioner and Reproducer lenses. Skip the broad literature mapping.

### Pre-submission check
```
/draft-review
```
Review your own draft before submitting. Run once, address the MUST-FIX items, then run again to verify the concerns are resolved.

### Idea to paper (full path)
```
/idea-test  →  /idea-sharpen  →  /research-intake  →  /paper-read (x3-5)  →  /paper-critic  →  [experiments]  →  /contribution-frame  →  [writing]  →  /draft-review
```
The complete lifecycle. Start with idea validation, read the relevant literature, run experiments, frame the contribution, write, review.

### Quick idea check
```
/idea-test
```
Stress-test an idea in one session. Get a verdict and "next 48 hours" plan.

### Adding papers to an ongoing research topic
If you already have a research brief and literature map:
1. Run `/paper-read` for the new paper
2. Optionally run `/paper-critic`
3. Re-run `/compare-papers` to update the comparison matrix
4. Re-run `/synthesis` to update findings

The skills will read existing artifacts and incorporate the new paper.

## Tips

- **State your priors honestly in `/research-intake`**. The forcing questions exist because unstated assumptions are the biggest threat to good research. The question "what do you already believe?" is not a formality.
- **Don't skip the Skeptic lens in `/paper-read`**. It's the most valuable lens and the one most people rush through.
- **Run `/paper-critic` on papers you agree with**. It's easy to critique papers you dislike. Critiquing papers you like is where intellectual honesty lives.
- **The synthesis forcing question "no hedging" is serious**. After reading N papers, you have an opinion. State it. You can qualify it, but the qualification must be specific.
- **Run `/draft-review` before you think the draft is ready**. The review is most useful when there's still time to make structural changes, not when you're polishing prose the night before the deadline.
- **Run `/idea-test` before you commit**. The cheapest experiment is the one you don't run because the idea wasn't worth pursuing.
- **Re-run `/idea-sharpen`**. The first pass produces a draft. The second pass is where real sharpening happens. Third pass is for perfectionists.
- **Don't skip `/contribution-frame`**. The #1 rejection reason at top venues is "contribution is unclear." This skill exists to prevent that.
