# Paper Card: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Metadata

| Field | Value |
|---|---|
| **Paper ID** | lewis-2020-rag |
| **Title** | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks |
| **Authors** | Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, Mike Lewis, Wen-tau Yih, Tim Rocktaschel, Sebastian Riedel, Douwe Kiela |
| **Year** | 2020 |
| **Venue** | NeurIPS 2020 |
| **URL** | https://arxiv.org/abs/2005.11401 |
| **Date read** | 2026-03-22 |

---

## One-Paragraph Summary

This paper introduces RAG, a model that combines a pre-trained seq2seq generator (BART) with a neural retriever (DPR) trained end-to-end. The key idea is that instead of storing all knowledge in model parameters (which is static and opaque), the model retrieves relevant documents at inference time and conditions generation on them. Two variants are proposed: RAG-Sequence (same documents for entire sequence) and RAG-Token (different documents per token). The model achieves state-of-the-art on open-domain QA benchmarks and generates more specific and factual text than pure parametric models. Crucially, this is one of the first papers to train the retriever and generator jointly in an end-to-end fashion.

## Problem

Knowledge-intensive NLP tasks (open-domain QA, fact verification, knowledge-grounded dialogue) require access to large amounts of world knowledge. Purely parametric models store knowledge implicitly in weights, which is opaque, hard to update, and limited by model size. The paper asks: can we build a model that explicitly retrieves relevant knowledge and uses it for generation, trained end-to-end?

## Approach

1. **Retriever**: Dense Passage Retriever (DPR) using BERT bi-encoder. Encodes query and documents into dense vectors, retrieves top-k via MIPS (Maximum Inner Product Search).
2. **Generator**: BART-large, conditioned on retrieved documents concatenated with the input.
3. **Two marginalization strategies**:
   - RAG-Sequence: Same set of retrieved docs for generating the entire output
   - RAG-Token: Can attend to different docs for each output token
4. **End-to-end training**: The retriever is trained through the generator's loss via marginalization over retrieved documents. DPR encoder is fine-tuned; FAISS index is periodically re-built.

## Key Claims

1. RAG achieves state-of-the-art on 3 open-domain QA datasets (Natural Questions, TriviaQA, WebQuestions) at time of publication.
2. RAG generates more specific and factual text than BART alone on MS-MARCO and Jeopardy question generation.
3. End-to-end training of retriever + generator outperforms pipeline approaches.
4. RAG-Token performs better on tasks requiring diverse knowledge; RAG-Sequence on tasks requiring coherent single-document reasoning.

## Evidence Map

| Claim | Evidence | Evidence type | Strength |
|---|---|---|---|
| Claim 1 | Tables 1-3: EM scores on NQ (44.5), TriviaQA (56.8), WQ (45.5) | Experiment on standard benchmarks | MODERATE — strong at publication time, now superseded |
| Claim 2 | Table 4: Jeopardy generation; human evaluation of factuality | Experiment + human eval | MODERATE — human eval is small-scale (52 questions) |
| Claim 3 | Ablation comparing fixed retriever vs. end-to-end trained | Ablation study | MODERATE — tested on limited settings |
| Claim 4 | Comparison of RAG-Sequence vs RAG-Token across tasks | Experiment | WEAK — differences are small and not significance-tested |

## Main Results

- NQ Exact Match: 44.5 (RAG-Token), vs. 36.4 (DPR baseline), 32.6 (REALM)
- TriviaQA: 56.8 (RAG-Token), vs. 57.9 (DPR reader — actually higher for DPR on this one)
- WebQuestions: 45.5 (RAG-Sequence)
- Jeopardy generation: higher factuality and specificity than BART in human evaluation

## Assumptions

- Wikipedia (Dec 2018 dump) is a sufficient knowledge source for the evaluated tasks
- DPR's bi-encoder retrieval is good enough as a retrieval backbone
- FAISS approximate search doesn't significantly degrade retrieval quality
- 5-10 retrieved passages are sufficient context for generation
- Factoid QA benchmarks are representative of "knowledge-intensive" tasks

## Limitations

### Acknowledged by authors
- Retrieval is limited to Wikipedia; doesn't generalize to arbitrary knowledge sources
- Index staleness: the FAISS index must be periodically rebuilt, which is expensive
- Computational cost of retrieval at training time

### Not acknowledged
- All evaluation is on English factoid QA — no complex reasoning, no multi-hop
- The human evaluation for Jeopardy generation is very small (52 questions, 3 annotators)
- RAG-Token vs RAG-Sequence differences are not significance-tested
- No evaluation of faithfulness — does the model actually USE the retrieved documents, or does it sometimes ignore them?
- No analysis of failure cases: when does retrieval fail and how does the generator handle bad retrievals?

---

## Reading Lenses

### Author Lens
The authors want you to understand that RAG represents a new paradigm: instead of cramming knowledge into parameters, let the model look things up. The end-to-end training is the key technical contribution — the retriever learns what to retrieve based on what helps generation. They'd be worried about readers dismissing this as "just combining DPR and BART" without appreciating the marginalization math that makes joint training possible.

### Reviewer Lens
**Decision**: ACCEPT (for 2020)
**Key issues**:
1. Strong results on standard benchmarks with a clean, well-motivated approach
2. Concern: all benchmarks are factoid QA. The claim of "knowledge-intensive NLP tasks" is broader than what's tested
3. The RAG-Sequence vs RAG-Token comparison needs significance testing — the differences look within noise on most tasks

### Skeptic Lens
The weakest link is the evaluation scope. The paper claims to address "knowledge-intensive NLP tasks" but evaluates exclusively on factoid QA and trivia generation. These are the EASIEST knowledge-intensive tasks — short answers, single-fact lookups, Wikipedia as gold source. The architecture might completely fail on multi-hop reasoning, numerical reasoning, or tasks requiring synthesis across documents. The 2020 benchmarks don't test any of this.

### Reproducer Lens
**Missing information**:
- Exact FAISS index type and parameters (IVF? PQ? How many clusters?)
- FAISS index rebuild frequency during training
- Learning rate schedule for DPR fine-tuning within RAG training
- Exact Wikipedia preprocessing (how are passages chunked? Overlap?)
- How many GPUs and how long for training
- Whether reported numbers are best-run or averaged

### Practitioner Lens
Deploying RAG circa 2020 means: (1) maintaining a FAISS index over Wikipedia-scale documents, which requires significant memory and periodic rebuilding, (2) the bi-encoder retriever adds ~50ms latency per query, (3) no clear strategy for handling retrieval failures — if the top-k docs are irrelevant, the model may hallucinate confidently, (4) the model has no mechanism for saying "I don't know" or indicating when retrieved evidence is insufficient.

### Student Lens
**Prerequisites**:
- Dense Passage Retrieval (Karpukhin et al. 2020) — the retrieval backbone
- BART (Lewis et al. 2020) — the generation backbone
- FAISS (Johnson et al. 2019) — approximate nearest neighbor search
- Maximum Inner Product Search (MIPS)
- Marginalization over latent variables — the math in Section 3 requires understanding of how to train models with discrete latent variables

---

## Connections

- Foundational paper for the entire RAG field. Every subsequent RAG paper cites this.
- Builds directly on DPR (Karpukhin et al. 2020) and BART.
- Led to RETRO (Borgeaud et al. 2022), Atlas (Izacard et al. 2022), and the modern RAG ecosystem.
- The lack of faithfulness evaluation in this paper is a gap that later work (RAGAS, ARES) tries to fill.

## Open Questions

1. How does RAG handle retrieval failures gracefully? (Not addressed in the paper.)
2. Does end-to-end training actually improve retrieval quality, or does it just teach the generator to work around bad retrievals?
3. How does performance change with different knowledge sources beyond Wikipedia?

## Confidence Rating

**Rating**: HIGH
**Reason**: This is a well-known, highly-cited paper with clear writing and reproducible (if dated) experiments. My understanding of the core contribution and limitations is solid. The main uncertainty is around the end-to-end training dynamics, which the paper doesn't analyze deeply.
