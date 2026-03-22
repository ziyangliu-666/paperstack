# Paper Critique: {TITLE}

**Paper Card**: [papers/cards/{paper-id}.md](../../papers/cards/{paper-id}.md)
**Date**: {DATE}

---

## Claim-Evidence Alignment

{For each key claim from the paper card, evaluate how well the evidence supports it.}

| Claim | Evidence | Alignment | Assessment |
|---|---|---|---|
| {claim 1} | {evidence presented} | STRONG / PARTIAL / WEAK / MISSING | {explanation} |
| {claim 2} | {evidence} | {alignment} | {explanation} |

## Methodology Assessment

### Experimental Design
{Is the experimental setup appropriate for the claims being made? Are there confounds?}

### Baselines
{Are the baselines appropriate? Are any obvious baselines missing? Are comparisons fair (same compute budget, same data, same hyperparameter search)?}

**Missing baselines**: {list any baselines that should have been included}
**Fairness issues**: {any issues with how baselines were compared}

### Ablation Studies
{Do the ablations isolate the contribution of each component? Are there ablations that should have been run but weren't?}

## Novelty Assessment

**Rating**: GENUINELY NEW / INCREMENTAL / REPACKAGING

{What specifically is new? Is it a new problem formulation, a new method, a new application of an existing method, or primarily an engineering contribution? How does it differ from the most similar prior work?}

## Reproducibility Assessment

**Rating**: HIGH / MODERATE / LOW / UNREPRODUCIBLE

| Aspect | Available? | Notes |
|---|---|---|
| Code | YES / NO / PARTIAL | {details} |
| Data | YES / NO / PARTIAL | {details} |
| Hyperparameters | YES / NO / PARTIAL | {details} |
| Compute requirements | YES / NO / PARTIAL | {details} |
| Random seeds | YES / NO | {details} |
| Training details | YES / NO / PARTIAL | {details} |

## Baseline Fairness

{Are the comparisons in this paper fair? Specific concerns:}

- Are baselines given the same hyperparameter tuning budget?
- Are baselines run on the same hardware?
- Are baselines using the same data splits?
- Are any results cherry-picked (e.g., best run reported without variance)?

## Statistical Rigor

- **Sample sizes**: {adequate / inadequate / not reported}
- **Significance testing**: {present / absent / inappropriate}
- **Error bars / confidence intervals**: {present / absent}
- **Multiple comparisons correction**: {applied / not applied / not needed}
- **Variance across runs**: {reported / not reported}

## Hidden Assumptions

{What does the paper assume without explicitly defending? List each assumption and assess whether it's reasonable.}

1. **Assumption**: {what} — **Reasonable?** {yes/no/partially, because...}
2. **Assumption**: {what} — **Reasonable?** {assessment}

## External Validity

{Would these results hold outside the specific experimental setup? Consider:}

- Different datasets
- Different scales
- Different domains
- Real-world (non-benchmark) conditions
- Different computational budgets

## Strongest Criticism

{If you had to write one paragraph demolishing this paper, what would it say? Be specific and evidence-based, not dismissive.}

## Strongest Defense

{If you had to write one paragraph defending this paper against all criticism, what would it say? Steelman the contribution.}

## Verdict

**Overall**: STRONG / MODERATE / WEAK

**Justification**: {2-3 sentences explaining the verdict, grounded in the assessment above. Reference specific evidence.}

**Key strength**: {one sentence}
**Key weakness**: {one sentence}
