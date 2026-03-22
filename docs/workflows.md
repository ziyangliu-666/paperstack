# Workflows

## The full research sequence

```
/research-intake  →  /literature-map  →  /paper-triage  →  /paper-read  →  /paper-critic  →  /compare-papers  →  /synthesis
```

This is the intended order. Each skill builds on prior artifacts. But the sequence is a guide, not a cage — skip steps when they don't apply.

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
