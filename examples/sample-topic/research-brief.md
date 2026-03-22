# Research Brief: Evaluation Methods for Retrieval-Augmented Generation

**Date**: 2026-03-22
**Status**: COMPLETE

---

## Research Question

How should retrieval-augmented generation (RAG) systems be evaluated, and what do current evaluation methods fail to capture?

Specifically: Which evaluation approaches (automatic metrics, human evaluation, benchmark suites) best predict real-world RAG system quality, and what systematic blind spots exist in the most widely used evaluation frameworks?

## Motivation

RAG systems are being deployed across enterprises for question answering, document search, and knowledge-grounded conversation. Teams are making deployment decisions based on benchmark scores (e.g., accuracy on Natural Questions, MMLU) that may not reflect real-world performance. If the evaluation methods are flawed, deployment decisions based on them are unreliable.

This matters for: (1) practitioners choosing between RAG architectures, (2) researchers proposing new RAG methods, (3) anyone interpreting published RAG benchmark results.

## Prior Beliefs

- I believe most RAG benchmarks over-index on factoid question answering and under-test complex reasoning, multi-step retrieval, and robustness to noisy documents.
- I suspect that retrieval quality and generation quality are evaluated independently in most frameworks, but their interaction effects (good retrieval + bad generation, bad retrieval + good generation) are poorly understood.
- I believe human evaluation of RAG systems is more informative but rarely done well — small sample sizes, unclear annotation guidelines, low inter-annotator agreement.
- I expect that faithfulness metrics (does the answer match the retrieved context?) are the most important but least standardized dimension.

## Scope

### In scope
- Automatic evaluation metrics for RAG (ROUGE, BERTScore, faithfulness metrics, citation accuracy)
- Human evaluation protocols for RAG
- Benchmark suites (KILT, BEIR, RAGAS, RGB, ARES)
- Evaluation of retrieval quality, generation quality, and their interaction
- Faithfulness and grounding evaluation
- Papers from 2020-present (RAG era)

### Out of scope
- Evaluation of non-RAG language models (pure LLM benchmarks)
- Evaluation of retrieval systems without generation (pure IR)
- Training methodologies for RAG (how to build RAG, not how to evaluate it)
- Commercial RAG platforms and their proprietary evaluation tools

### Non-goals
- Proposing a new evaluation metric (this is a literature review, not a research contribution)
- Comprehensive coverage of every RAG paper (focus on evaluation methodology papers)

## Success Criteria

I will consider this research complete when I can:
1. Identify the 3-5 most commonly used RAG evaluation approaches and their known failure modes
2. Articulate which evaluation dimensions (faithfulness, relevance, completeness, etc.) are well-covered and which are neglected
3. Make a specific recommendation for how a practitioner should evaluate a RAG system, with justification
4. Identify 2-3 promising evaluation approaches that are underutilized

## Key Terms

| Term | Definition | Notes |
|---|---|---|
| RAG | Retrieval-Augmented Generation — a system that retrieves documents and uses them to condition a language model's output | Introduced by Lewis et al. 2020, now used broadly |
| Faithfulness | Whether the generated answer is supported by the retrieved documents | Also called "grounding" or "attribution" — terminology varies |
| Relevance | Whether the retrieved documents are relevant to the query | Distinct from answer relevance |
| RAGAS | Retrieval Augmented Generation Assessment framework | Automatic metric framework by Es et al. 2023 |
| Attribution | Whether claims in the generated text can be traced to specific source documents | Related to faithfulness but emphasizes citation |

## Keywords and Search Strategy

- Primary keywords: RAG evaluation, retrieval-augmented generation benchmark, faithfulness evaluation, grounding metrics
- Secondary keywords: RAGAS, ARES, KILT benchmark, attribution evaluation, hallucination detection RAG
- Sources: Semantic Scholar, Google Scholar, arXiv (cs.CL, cs.IR)
- Time range: 2020-present
- Exclusion criteria: Non-English papers, papers about RAG training without evaluation focus

## Likely Subtopics

1. Automatic metrics for RAG (token-level, semantic, faithfulness-specific)
2. Benchmark suites and datasets for RAG evaluation
3. Human evaluation protocols
4. Faithfulness and attribution evaluation
5. Retrieval quality metrics vs. end-to-end metrics
6. Robustness and stress testing for RAG

## Dissenting Framings

- A **systems engineer** would frame this as "which metrics correlate with user satisfaction in production?" rather than "which metrics are theoretically sound."
- A **benchmark designer** would ask "what tasks should a RAG benchmark include?" rather than "how well do existing benchmarks work?"
- A **ML researcher** focused on hallucination might argue that faithfulness is the ONLY evaluation dimension that matters for RAG, since retrieval is a solved-enough problem.
- A **practitioner** might argue that benchmark evaluation is irrelevant — only A/B testing in production matters.
