# Critique Evaluation Rubric

Use this rubric to systematically evaluate a paper's claims, methodology, and contribution. Score each dimension, then synthesize into an overall verdict.

---

## Dimension 1: Claim-Evidence Alignment

### Claim types (identify which type each claim is):
- **Empirical**: "Our method achieves X% accuracy" — requires experimental evidence
- **Theoretical**: "Our algorithm has O(n log n) complexity" — requires formal proof
- **Comparative**: "Our approach outperforms X" — requires head-to-head comparison under fair conditions
- **Causal**: "X causes Y" — requires controlled experiments or strong causal framework
- **Generalization**: "This works for all Z" — requires diverse evaluation or theoretical argument
- **Novelty**: "This is the first to..." — requires thorough related work survey

### Evidence quality hierarchy:
1. **Strongest**: Multiple datasets, multiple metrics, significance tests, ablations, reproducible code
2. **Strong**: Single comprehensive evaluation with ablations and error analysis
3. **Moderate**: Standard benchmark evaluation with baselines
4. **Weak**: Limited evaluation, few baselines, no statistical analysis
5. **Weakest**: Anecdotal examples, cherry-picked cases, no quantitative evaluation

### Alignment rating:

| Rating | Criteria |
|---|---|
| STRONG | Claim is directly supported by controlled experiments with appropriate statistical tests |
| MODERATE | Claim is supported by experiments, but with caveats (limited datasets, no significance tests, confounds) |
| WEAK | Claim is stated but evidence is indirect, anecdotal, or cherry-picked |
| MISSING | Claim has no supporting evidence in the paper |

### Red flags for claim-evidence mismatch:
- Claim uses "significantly" but no significance test is reported
- Claim is about general capability but evaluation is on one narrow benchmark
- Claim is causal but study design is observational
- Claim says "state-of-the-art" but comparison set is incomplete
- Abstract claims don't match what the experiments actually measured

**Method**: Take each claim from the paper card's "Key Claims" section. Identify its type. Find the specific table, figure, or proof that supports it. Evaluate whether the evidence type is appropriate for the claim type. If you can't find evidence, the alignment is MISSING.

## Dimension 2: Novelty Realism

| Rating | Criteria |
|---|---|
| GENUINELY NEW | New problem formulation, method, or theoretical insight that didn't exist before |
| INCREMENTAL | Meaningful improvement on existing work — new component, better training, clever combination |
| APPLICATION | Applies existing methods to a new domain or dataset |
| REPACKAGING | Previously known ideas presented as novel (check the related work and citations carefully) |

**Common traps**: "Novel" in the abstract doesn't mean novel in reality. Check if the "new" method is a known technique applied to a different problem, or a minor variant of existing work.

**Novelty misconceptions to avoid** (from Michael Black):
- Confusing novelty with complexity — simple changes can be highly novel
- Equating novelty with difficulty — elegant solutions shouldn't be undervalued
- "Obvious in hindsight" fallacy — judge ideas before knowing they work, not after
- Limiting novelty to technical innovation — datasets, applications, and methodological connections count

## Dimension 3: Baseline Fairness

Checklist:
- [ ] Are the strongest known baselines included? (Check papers published up to 6 months before submission)
- [ ] Are baselines given the same hyperparameter tuning budget?
- [ ] Are baselines run on the same hardware and data splits?
- [ ] Are baselines using official implementations or reimplementations? (Reimplementations often underperform)
- [ ] Is the comparison to concurrent work acknowledged if relevant?
- [ ] Are results averaged over multiple runs with variance reported?

**Red flags**:
- Comparing to a baseline's "out of the box" performance while tuning your own method
- Using an old version of a baseline when a newer, better version exists
- Comparing on a metric where your method has a structural advantage

## Dimension 4: Dataset Quality

| Aspect | Questions to ask |
|---|---|
| Representativeness | Does the dataset represent the real-world distribution the paper claims to address? |
| Size | Is the dataset large enough for the conclusions drawn? |
| Contamination | Could there be train/test overlap? Data leakage? |
| Bias | What biases does the dataset encode? Does the paper acknowledge them? |
| Staleness | Is the dataset current enough? (Especially for language/web data) |

## Dimension 5: Metric Adequacy

- Does the metric actually measure what the paper claims to optimize?
- Are there known failure modes of this metric? (E.g., BLEU for open-ended generation)
- Is a single metric sufficient, or should multiple metrics be reported?
- Do the metrics capture what a real user would care about?

## Dimension 6: Ablation Sufficiency

A good ablation study isolates the contribution of each component:
- [ ] Each claimed contribution has a corresponding ablation
- [ ] Ablations remove one thing at a time, not multiple
- [ ] The "base" model in ablations is clearly defined
- [ ] Ablation results are statistically meaningful, not within noise

## Dimension 7: Statistical Rigor

| Aspect | Acceptable | Concerning |
|---|---|---|
| Runs | 3+ with mean and std | Single run |
| Significance | p < 0.05 or CI reported | No significance test |
| Effect size | Reported and meaningful | Only p-value |
| Comparisons | Corrected for multiple comparisons | Uncorrected |

## Dimension 8: Reproducibility

Score based on what is available:
- Code: publicly available, documented, runnable
- Data: publicly available or clearly described
- Hyperparameters: fully specified
- Compute: hardware and time requirements stated
- Random seeds: specified for reproducibility

## Dimension 9: Hidden Assumptions

Every paper rests on assumptions it doesn't defend. Common ones:
- The benchmark is representative of real use
- The training distribution matches the deployment distribution
- The metric captures what users care about
- The compute budget is accessible to the intended audience
- The method scales to production requirements

## Dimension 10: External Validity

Would results hold under:
- Different datasets from different domains?
- Different scales (10x larger, 10x smaller)?
- Different languages or cultural contexts?
- Real-world conditions (noisy data, adversarial inputs, shifting distributions)?
- Different computational budgets?

## Dimension 11: Writing and Presentation

This is NOT about prose quality. Evaluate:
- Are claims stated precisely, or are they vague?
- Are limitations presented honestly, or buried?
- Is the related work fair to competitors?
- Are figures informative or decorative?
- Does the paper oversell its contribution?

---

## Synthesizing the Verdict

| Verdict | Criteria |
|---|---|
| STRONG | Most claims are well-supported. Methodology is sound. Contribution is clear and meaningful. Limitations are honest. |
| MODERATE | Key claims are supported, but with notable caveats. Some methodological concerns. Contribution is real but may be overstated. |
| WEAK | Major claims lack support. Significant methodological issues. Contribution is unclear or overstated. |

The verdict should follow from the dimension scores, not from gut feeling. If you rate a paper MODERATE but have 5 WEAK dimensions, something is wrong — recalibrate.
