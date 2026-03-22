# Multi-Lens Reading Rubric

Read every important paper through these 6 lenses. Each lens asks different questions and surfaces different insights. Rushing through any lens — especially the Skeptic lens — defeats the purpose.

---

## Author Lens

**Purpose**: Understand the paper on its own terms before critiquing it.

**Core question**: "If you wrote this paper, what would you most want the reader to understand? What would you be most worried they'd misinterpret?"

**Detailed questions**:
1. What is the paper's central contribution in one sentence? (Not the abstract — your own words.)
2. What problem were the authors actually trying to solve? (This may differ from the problem stated in the introduction.)
3. What were the key design decisions, and what alternatives did the authors consider?
4. What would the authors say is the strongest part of their work?
5. Where do the authors seem most uncertain or careful in their claims?

**Push until you hear**: A specific, jargon-free restatement that a smart non-expert could follow. The user should be able to explain the paper's contribution without using any of the paper's own phrasing.

**Red flags**:
- Restating the abstract. That's copying, not understanding.
- "The paper proposes a novel framework for X." That's a press release.
- Inability to distinguish what the paper claims from what it demonstrates.

**BAD**: "The paper introduces an interesting new approach to multi-hop question answering."
**GOOD**: "The paper's core move is to decompose multi-hop questions into sub-questions before retrieval, rather than retrieving for the full question at once. This trades one hard retrieval for N easier retrievals, at the cost of error propagation across decomposition steps."

---

## Reviewer Lens

**Purpose**: Evaluate the paper as a peer reviewer would.

**Core question**: "If this were a borderline submission — what's the one thing that would tip you to accept, and the one thing that would tip you to reject?"

**Detailed questions**:
1. Is the problem well-motivated? Does the paper convince you this problem matters?
2. Is the approach well-described? Could a graduate student implement it from the paper?
3. Are the experiments sufficient to support the claims?
4. Are the baselines appropriate and fairly compared?
5. Is the paper honest about its limitations?

**Push until you hear**: Specific technical claims or methodological choices, not "it's well-written" or "it's incremental."

**Red flags**:
- "I'd accept/reject based on the writing quality." Writing quality is not a contribution.
- "It's a solid paper." What does "solid" mean? Specify.
- Evaluating novelty without checking related work yourself.

**BAD**: "The paper is well-written and makes a solid contribution to the field."
**GOOD**: "Accept for the decomposition approach and the ablation showing that sub-question quality is the bottleneck. Reject concern: the comparison to ColBERT uses the 2020 checkpoint, not the 2022 v2 which closes much of the reported gap."

---

## Skeptic Lens

**Purpose**: Find the weakest link. This is the most important lens.

**Core question**: "What's the weakest link in the chain from assumptions to conclusions? If this paper is wrong, where does it break?"

**Detailed questions**:
1. What are the paper's unstated assumptions? (Every paper has them.)
2. For each key result, what alternative explanation could produce the same numbers?
3. Is the claimed improvement within the noise of the evaluation?
4. Are there confounds in the experimental setup?
5. What would a hostile reviewer say in the first paragraph of their review?

**Push until you hear**: A specific assumption, data issue, or logical step — not "it might not generalize."

**Red flags**:
- "The paper seems generally sound." What would make it unsound? Be specific.
- "The limitations section addresses my concerns." Limitations sections are marketing — authors list the weaknesses they can defend against.
- Accepting benchmark improvements at face value without checking statistical significance.

**BAD**: "The results look convincing, though there may be some generalization concerns."
**GOOD**: "Claim 3 rests on the assumption that Natural Questions is representative of real user queries. NQ questions are factoid lookups derived from Google search logs — they systematically underrepresent multi-constraint, comparative, and temporal queries. If the method's advantage comes from factoid decomposition, the 12% improvement in Table 2 might not hold on a more diverse question distribution."

---

## Reproducer Lens

**Purpose**: Assess whether this work could be replicated from the paper alone.

**Core question**: "List every piece of information you would need to reproduce Table 1 that is NOT in this paper."

**Detailed questions**:
1. Is the method described precisely enough to reimplement? Where is it ambiguous?
2. Are all hyperparameters specified? (Learning rate, batch size, optimizer, scheduler, etc.)
3. What compute budget would you need?
4. Is the data processing pipeline fully described?
5. Is code available? If so, does it match the paper's description?

**Push until you hear**: Specific missing details — not "it would be hard to reproduce" but "the learning rate schedule is not specified, the preprocessing for dataset X is not described, and the retrieval index construction details are in a footnote reference to code that doesn't exist."

**Red flags**:
- "Code is available on GitHub." Is it documented? Does it run? Does it match the paper?
- "The paper includes sufficient implementation details." Did you actually check, or are you assuming?
- Confusing "the method is described" with "the method is reproducible."

---

## Practitioner Lens

**Purpose**: Assess real-world applicability beyond benchmark numbers.

**Core question**: "If you needed to deploy this in production next week, what would break first?"

**Detailed questions**:
1. What is the inference latency? Is it reported? Is it acceptable for your use case?
2. What are the resource requirements (memory, compute, storage)?
3. How does it handle edge cases (empty inputs, adversarial inputs, out-of-domain data)?
4. What is the maintenance burden? Does it require periodic retraining or index updates?
5. How does it fail? Gracefully or catastrophically?

**Push until you hear**: Specific engineering concerns with quantified thresholds — not "it might be slow" but "the paper reports 350ms per query on A100; at production scale (10K QPS) this would require 50+ GPUs for retrieval alone."

**Red flags**:
- "This would be straightforward to deploy." What about data pipeline, monitoring, failure modes?
- Ignoring cost. A method that requires 8 A100s is not a solution for most teams.
- Assuming benchmark conditions match production conditions.

---

## Student Lens

**Purpose**: Identify prerequisites and learning path.

**Core question**: "What does this paper assume you know that a newcomer wouldn't?"

**Detailed questions**:
1. What prerequisite knowledge does this paper require?
2. What papers should you read before this one?
3. What jargon does this paper use without defining?
4. What is the simplest possible explanation of the core idea?
5. If you were teaching this paper, what would students struggle with most?

**Push until you hear**: Specific concepts, papers, or mathematical prerequisites — not "you need to know machine learning."

**Red flags**:
- "The paper is self-contained." Almost no paper is. What does it assume?
- Listing general fields ("NLP", "information retrieval") instead of specific concepts ("BM25 scoring", "dense passage embedding", "cross-encoder reranking").
