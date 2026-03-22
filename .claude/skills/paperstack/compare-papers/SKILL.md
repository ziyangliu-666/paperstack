---
name: compare-papers
description: |
  Compare multiple papers side by side on dimensions that matter for your
  research question. Produces a comparison matrix with divergences and consensus.
  Use when: "compare these papers", "how do they differ?", "side by side".
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---

# Compare Papers

You are a systematic comparator. Your job is to put papers next to each other on the dimensions that matter and make the differences visible. A good comparison reveals what no single paper card can show: where the field agrees, where it diverges, and why.

---

## Phase 1: Read Prior Artifacts

1. Read the research brief for comparison context:
   ```bash
   cat docs/research/current/research-brief.md 2>/dev/null || echo "NO_BRIEF"
   ```

2. Find all paper cards:
   ```bash
   ls papers/cards/*.md 2>/dev/null
   ```

   **If fewer than 2 cards**: STOP. "Comparison requires at least 2 paper cards. Run `/paper-read` on more papers first."

3. Read ALL paper cards. Comparison requires full context on every paper.

4. Optionally read critiques for additional depth:
   ```bash
   ls papers/critiques/*.md 2>/dev/null
   ```

5. Check for existing comparison matrix:
   ```bash
   cat docs/research/current/comparison-matrix.md 2>/dev/null || echo "NO_EXISTING_MATRIX"
   ```
   If it exists, you're updating. Preserve prior analysis and add new papers.

---

## Phase 2: Dimension Selection

The default comparison dimensions are: problem framing, method family, key innovation, datasets, primary metric, strengths, weaknesses, compute cost, reproducibility, what to borrow, what to distrust.

But not all dimensions matter equally for every research question.

### Forcing Question: Dimension relevance

**Ask via AskUserQuestion**: "You have {N} paper cards. Papers can be compared on many dimensions. Which 5-7 dimensions matter most for YOUR research question — and why those, not others? Be specific. 'Methodology' is too vague. 'Whether the method works with less than 1000 training examples' is specific."

**Push until you hear**: Dimensions that connect directly to the research question from the brief. The user should be able to explain why each dimension would change their conclusions.

**Red flags**:
- Listing generic dimensions like "methodology" and "results." (These apply to any comparison. What's specific to YOUR question?)
- Including a dimension because it's standard, not because it matters. (If compute cost doesn't affect your conclusions, drop it.)
- Forgetting dimensions where papers DISAGREE. (Disagreement is the most valuable comparison axis.)

**BAD pushback**: "Those are great dimensions for comparison."
**GOOD pushback**: "You listed 'accuracy' as a comparison dimension. But the papers use different datasets and different metrics — so comparing their accuracy numbers directly is meaningless. The useful dimension here is: 'how do their evaluation approaches differ, and what does each approach fail to capture?' That's the comparison that would actually inform your research question."

---

## Phase 3: Build the Matrix

For each dimension and each paper:
1. Extract the relevant information from the paper card
2. Normalize the comparison (same scale, same framing)
3. Note where direct comparison is possible and where it's not (and why)

Pay special attention to:
- **Divergences**: Where papers disagree. Explain what causes the disagreement — different methods, different data, different definitions, or different claims.
- **Hidden agreements**: Where papers agree without citing each other. This suggests convergent evidence.
- **Incomparable axes**: Where papers can't be directly compared and why. This is valuable information about the field's fragmentation.

---

## Phase 4: Analyze Patterns

After building the matrix, synthesize higher-level observations:

1. **Methodology convergence**: Are methods converging toward a standard approach?
2. **Benchmark saturation**: Are results on shared benchmarks hitting a ceiling?
3. **Blind spots**: What do ALL papers ignore? (This is often more interesting than what they each get wrong individually.)
4. **Borrowing opportunities**: Which ideas from Paper A could improve Paper B?

---

## Phase 5: Write the Comparison Matrix

1. Read the template:
   ```bash
   cat templates/comparison-matrix.template.md
   ```

2. Write `docs/research/current/comparison-matrix.md` following the template.

3. The "Lessons for the Research Question" section is the most important. It should directly connect the comparison back to the brief.

---

## Anti-Sycophancy Rules

- "All papers make valuable contributions" — ranking is the job. Which paper contributes MOST to answering the research question?
- "The approaches are complementary" — sometimes they are. Sometimes one is strictly better. Say which.
- "Each paper has its strengths" — of course they do. But what are the RELATIVE strengths? If you had to pick one approach, which would you pick and why?

---

## Completion Status

- **DONE** — Comparison matrix written with divergences, consensus, and lessons for the research question.
- **DONE_WITH_CONCERNS** — Matrix written but some dimensions couldn't be compared fairly. Specify.
- **BLOCKED** — Fewer than 2 paper cards available.
