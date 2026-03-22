# Workflows

## The full sequence

```
/research-intake  →  /literature-map  →  /paper-triage  →  /paper-read  →  /paper-critic  →  /compare-papers  →  /synthesis
```

This is the intended order. Each skill builds on prior artifacts. But the sequence is a guide, not a cage — skip steps when they don't apply.

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
