# Research Question Sharpness Rubric

## What makes a good research question

A research question is sharp when:
1. **Falsifiable**: You can describe specific evidence that would answer it
2. **Scoped**: You can say what's in and what's out
3. **Motivated**: You can explain why the answer matters to someone specific
4. **Novel (to you)**: You can't already answer it from what you know

## Common failure modes

### Too broad
- BAD: "How does retrieval-augmented generation work?"
- GOOD: "Does adding a reranking step to RAG pipelines improve factual accuracy on multi-hop questions, and at what latency cost?"
- **Why it matters**: Broad questions produce surveys, not understanding. You'll read 50 papers and learn nothing actionable.

### Too narrow (for a literature review)
- BAD: "What is the exact F1 score of DPR on Natural Questions with the Dec 2023 Wikipedia dump?"
- GOOD: "How sensitive are dense retrieval methods to the freshness of the document corpus?"
- **Why it matters**: If the answer is a single number in a single paper, you don't need a literature review.

### Solution-first framing
- BAD: "How should I use vector databases for my search system?"
- GOOD: "What retrieval approaches achieve the best relevance-latency tradeoff for domain-specific search at 10M+ document scale?"
- **Why it matters**: Starting with a solution closes off alternatives. Start with the problem.

### Confirmation-seeking
- BAD: "Why is method X better than method Y?" (assumes X is better)
- GOOD: "Under what conditions does method X outperform method Y, and vice versa?"
- **Why it matters**: Confirmation-seeking questions produce biased literature reviews. You'll unconsciously filter for supporting evidence.

## Sharpness checklist

Before accepting a research question, verify:

- [ ] Can you describe what a satisfying answer looks like?
- [ ] Can you name at least one person or group who would frame this differently?
- [ ] Have you stated what you already believe about the answer?
- [ ] Is the scope narrow enough to complete with 5-15 papers?
- [ ] Is the question about a problem, not a solution?
- [ ] Could you be wrong about your initial beliefs? (If not, why research?)
