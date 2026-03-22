# Draft Review Rubric

This rubric adapts the paper-critic's 11 evaluation dimensions for author-side draft review. The key difference: you are reviewing a work-in-progress, not a published paper. The goal is to expose rejection risk, not to grade a finished product.

---

## Core Review Dimensions

These dimensions are shared with the paper-critic skill but evaluated through a pre-submission lens.

### 1. Contribution Framing

| Rating | Criteria |
|---|---|
| CLEAR | The contribution is stated precisely. A reviewer can identify in 30 seconds what is new and why it matters. |
| FUZZY | The contribution is present but buried, vague, or conflated with background. A reviewer will struggle to extract the claim. |
| MISSING | No clear contribution statement. The paper reads as a report, not a research contribution. |

**What to look for in a draft**:
- Does the abstract state the contribution in one sentence?
- Does the introduction end with a numbered or bulleted list of contributions?
- Is each contribution falsifiable — could a reviewer disagree?
- Does the contribution match what the experiments actually measure?

### 2. Claim-Evidence Alignment

Same as paper-critic Dimension 1. For each claim in the draft:
- Identify the type: empirical, theoretical, comparative, causal, generalization, novelty.
- Find the specific evidence (table, figure, proof).
- Rate: STRONG / MODERATE / WEAK / MISSING.

**Draft-specific concern**: Authors often write claims before finishing experiments. Flag claims that appear to lack supporting evidence *in the current draft*, even if the author intends to add it.

### 3. Novelty Positioning

Same as paper-critic Dimension 2, but with extra scrutiny for:
- Does the related work section fairly represent the closest prior work?
- Is the delta from the closest prior work clearly stated?
- Would a reviewer who knows the field agree that this is novel?
- Is the novelty claim proportional to the actual technical contribution?

### 4. Baseline Adequacy

Same as paper-critic Dimension 3. Key questions for drafts:
- Are the baselines published within the last 2 years (or the strongest known)?
- Are baselines from official implementations, not weaker reimplementations?
- Is the comparison fair (same compute, data, tuning budget)?
- Are any obvious baselines missing that a reviewer will immediately ask about?

### 5. Experimental Design

Combined from paper-critic Dimensions 4-6 (methodology, dataset quality, metric adequacy, ablation sufficiency):
- Is the experimental setup appropriate for the claims?
- Are the datasets representative?
- Do the metrics measure what the paper claims to optimize?
- Are ablations sufficient to isolate each contribution?

### 6. Statistical Rigor

Same as paper-critic Dimension 7:
- Multiple runs with mean and std?
- Significance tests where claims involve comparisons?
- Effect sizes, not just p-values?

### 7. Reproducibility

Same as paper-critic Dimension 8. For drafts, also check:
- Are implementation details sufficient for a reviewer to assess feasibility?
- Are compute requirements stated (a reviewer may question scalability)?

### 8. Clarity and Presentation

Adapted from paper-critic Dimension 11 for submission context:
- Is the paper within page limits for the target venue?
- Are figures legible and informative?
- Is notation consistent?
- Are key terms defined before use?
- Is the writing precise or vague?
- Are limitations presented honestly or hidden?

---

## Venue-Aware Adjustments

When venue guidance is available, adjust the review along these axes:

| Axis | What to check |
|---|---|
| Scope fit | Does the paper match the venue's stated topics and tracks? |
| Evaluation expectations | Does the venue expect user studies, ablations, theoretical proofs? |
| Novelty bar | ML venues vs. application venues have different novelty standards. |
| Page limits | Is the paper within the venue's formatting constraints? |
| Double-blind compliance | Are author identities hidden if required? |
| Ethics / broader impact | Does the venue require these sections? |

---

## Review Verdict Scale

Use the same scale a real conference reviewer would use:

| Verdict | Meaning |
|---|---|
| STRONG ACCEPT | Clearly above the acceptance threshold. Well-executed, novel, well-written. |
| WEAK ACCEPT | Above the threshold with minor concerns. Would benefit from revision but is publishable. |
| BORDERLINE | Could go either way. Has merit but also has significant concerns. |
| WEAK REJECT | Below the threshold. Has some merit but concerns outweigh contributions. |
| STRONG REJECT | Clearly below the threshold. Fundamental issues with claims, evidence, or contribution. |

**Important**: Most drafts should land at BORDERLINE or below — that is the point. If the draft gets a STRONG ACCEPT from this tool, either it is genuinely excellent or the review was too soft.

---

## Mapping Review to Revision Checklist

Every major concern identified in the review MUST map to at least one revision task:

| Review finding type | Revision task type |
|---|---|
| Missing evidence | Add experiment / analysis |
| Weak baseline | Add or strengthen baseline comparison |
| Unclear contribution | Rewrite contribution statement |
| Missing related work | Add missing citations and comparisons |
| Statistical concern | Add significance tests / error bars / multiple runs |
| Clarity issue | Rewrite specific section |
| Scope / venue mismatch | Reframe or redirect to better venue |

Each revision task must be:
- **Specific**: "Add comparison to Method X on Dataset Y" not "improve baselines"
- **Actionable**: The author can start working on it immediately
- **Prioritized**: MUST-FIX (blocks acceptance) vs. SHOULD-FIX (strengthens paper) vs. NICE-TO-HAVE (polish)
