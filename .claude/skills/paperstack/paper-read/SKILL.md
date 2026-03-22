---
name: paper-read
description: |
  Deep-read a single paper through 6 analytical lenses: Author, Reviewer,
  Skeptic, Reproducer, Practitioner, Student. Produces a structured paper card.
  Use when: "read this paper", "analyze this paper", "paper card for X".
disable-model-invocation: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
  - WebSearch
---

# Paper Read

You are a rigorous reader, not a summarizer. Summaries are what you get when you read passively. Understanding is what you get when you read through multiple lenses, challenge claims against evidence, and identify what the paper doesn't say.

**This is the core skill of paperstack.** The 6-lens reading process is what separates "I read the abstract" from "I understood the paper."

---

## Phase 1: Context and Paper Selection

1. Read the research brief for context (optional but recommended):
   ```bash
   cat docs/research/current/research-brief.md 2>/dev/null || echo "NO_BRIEF (proceeding without research context)"
   ```

2. Ask the user which paper to read via AskUserQuestion:
   > "Which paper do you want to read? Provide one of:
   > - A URL (arXiv, Semantic Scholar, conference page)
   > - A citation (Author et al., Year)
   > - A file path to a PDF
   > - A title to search for"

3. Determine the paper ID (slug): `{first-author-lastname}-{year}-{shortitle}`
   Example: `lewis-2020-rag`, `vaswani-2017-attention`

4. Check if a card already exists:
   ```bash
   ls papers/cards/*.md 2>/dev/null | grep "{paper-id}" || echo "NO_EXISTING_CARD"
   ```
   If a card exists, ask whether to update or re-read from scratch.

5. Obtain the paper text. If given a URL, use WebSearch or WebFetch to access the paper. If given a PDF path, read it.

---

## Phase 2: First Pass — Comprehension

Before the lens analysis, establish baseline comprehension:

1. Identify: title, authors, year, venue, abstract
2. Read the introduction and conclusion
3. Scan figures and tables
4. Read section headings to understand structure

Output a 2-3 sentence summary of what the paper claims to do. This is provisional — it will be refined through the lens analysis.

---

## Phase 3: Multi-Lens Analysis

Read `references/multi-lens-rubric.md` for the detailed per-lens rubric.

Work through each lens systematically. For each lens, ask ONE forcing question via AskUserQuestion. The questions below are the core forcing questions — the rubric file contains additional detailed questions for each lens.

### Lens 1: Author

**Ask via AskUserQuestion**: "Restate this paper's central contribution in one sentence — your own words, not the abstract. If you can't do this clearly, that tells us something important about the paper's clarity or your understanding of it."

**Push until you hear**: A specific, jargon-free restatement that a smart non-expert could follow. The user should distinguish between what the paper CLAIMS and what it DEMONSTRATES.

**BAD**: "The paper proposes a novel framework for multi-hop question answering."
**GOOD**: "The paper's key move is decomposing complex questions into simpler sub-questions before retrieval, showing this improves answer accuracy by 12% on HotpotQA — but only for factoid-style questions, not open-ended ones."

### Lens 2: Reviewer

**Ask via AskUserQuestion**: "If this paper were a borderline submission to the top venue in its field — name one specific thing that tips you to accept, and one that tips you to reject."

**Push until you hear**: Specific technical claims or methodological choices. Not "well-written" or "interesting."

**BAD**: "Accept because it's a solid contribution. Reject because it's somewhat incremental."
**GOOD**: "Accept for the ablation in Table 4 that isolates the decomposition quality as the bottleneck — that's actionable and novel. Reject because the comparison to ColBERT uses the 2020 checkpoint, not v2 which likely closes the gap."

### Lens 3: Skeptic

**Ask via AskUserQuestion**: "What's the weakest link in the chain from this paper's assumptions to its conclusions? If this paper turns out to be wrong, where does it break?"

**Push until you hear**: A specific assumption, data issue, or logical step. Not "it might not generalize."

**BAD**: "The results look solid, though generalization is always a concern."
**GOOD**: "The entire evaluation rests on Natural Questions, which consists of factoid lookups from Google search logs. If the method's advantage comes specifically from factoid decomposition, the 12% gain could vanish on questions requiring multi-constraint reasoning — and the paper tests nothing outside factoid QA."

### Lens 4: Reproducer

**Ask via AskUserQuestion**: "If you had to reproduce the key result in Table 1, list every piece of information you would need that is NOT in this paper."

**Push until you hear**: Specific missing details — learning rate schedule, preprocessing pipeline, index construction, hardware specs, random seeds. Not "it would be hard."

**BAD**: "The paper provides sufficient implementation details."
**GOOD**: "Missing: (1) learning rate warmup schedule, (2) how the Wikipedia passages are chunked (overlapping? fixed 100 tokens?), (3) exact FAISS index type and parameters, (4) whether results are the best run or averaged, (5) total training time and hardware."

### Lens 5: Practitioner

**Ask via AskUserQuestion**: "If someone deployed this system in production next week, what would break first?"

**Push until you hear**: Specific engineering concerns with concrete reasoning. Not "it might be slow."

**BAD**: "There might be scalability concerns."
**GOOD**: "The retriever re-encodes all queries at inference time using a DPR model. At 100 QPS, that's 100 forward passes/second through BERT-base — feasible on GPU but latency-sensitive. The bigger issue: the paper assumes a static Wikipedia index, but production systems need index updates. Rebuilding the FAISS index on updated documents is not addressed."

### Lens 6: Student

**Ask via AskUserQuestion**: "What's one thing this paper assumes you already know that a newcomer to this area wouldn't?"

**Push until you hear**: Specific concepts, papers, or mathematical prerequisites. Not "you need to know machine learning."

**BAD**: "You need background in NLP."
**GOOD**: "The paper assumes you understand dense passage retrieval (DPR) and why it differs from sparse retrieval (BM25). Without reading Karpukhin et al. 2020 first, the design choices in Section 3 won't make sense — particularly why they use a bi-encoder instead of a cross-encoder."

---

## Phase 4: Write the Paper Card

1. Read the template:
   ```bash
   cat templates/paper-card.template.md
   ```

2. Write `papers/cards/{paper-id}.md` following the template.

3. Ensure every section is populated. Mark any section you're uncertain about with a confidence note.

4. The Evidence Map is critical: for each claim, link it to specific evidence (table, figure, proof) and rate the evidence strength.

---

## Phase 5: Update Research Artifacts

1. If a reading queue exists, update the paper's status to DONE:
   ```bash
   grep -l "{paper-id}" docs/research/current/reading-queue.md 2>/dev/null
   ```

2. If this paper connects to previously read papers, note the connection in both cards' "Connections" sections.

---

## Anti-Sycophancy Rules

These rules apply to how you analyze the paper, not just how you talk to the user:

- "The paper presents a novel approach" — what specifically is novel? Is it actually novel or is it a known technique in a new domain?
- "The experiments are comprehensive" — are they? Name a missing experiment.
- "The results demonstrate clear improvements" — over what baselines? By how much? Is it statistically significant? Is the improvement meaningful or is it within noise?
- "This is a well-motivated problem" — who has this problem? What's at stake? Is the paper solving a real problem or a benchmark game?

---

## Completion Status

- **DONE** — Paper card written with all sections and all 6 lens notes.
- **DONE_WITH_CONCERNS** — Card written but some lenses are thin. List which ones and why.
- **NEEDS_CONTEXT** — Could not access the paper text. State what's needed.
