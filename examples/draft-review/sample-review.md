---
generated: 2026-03-20T14:32:07+08:00
venue: NeurIPS 2026 main track
venue_guidance_source: https://neurips.cc/Conferences/2026/CallForPapers
venue_guidance_status: live
venue_guidance_cached_at: 2026-03-20T14:31:12+08:00
manuscript: ./main.tex
files_read:
  - ./main.tex
  - ./intro.tex
  - ./method.tex
  - ./experiments.tex
  - ./related.tex
  - ./appendix.tex
  - ./references.bib
files_missing:
  - ./supplement.tex
reduced_context: true
---

# Draft Review: Adaptive Gradient Compression for Federated Learning with Heterogeneous Clients

**Target venue**: NeurIPS 2026 main track
**Manuscript**: ./main.tex
**Review date**: 2026-03-20

> ⚠️ **Reduced context**: `supplement.tex` was referenced by the manuscript but not found. The review may miss supplementary experiments or proofs.

---

## Paper Summary

This paper proposes Adaptive Gradient Compression (AGC), a method for reducing communication costs in federated learning by dynamically adjusting the compression ratio per client based on local gradient statistics. The key insight is that clients with more heterogeneous data distributions benefit from lower compression (higher fidelity gradients), while clients with data closer to the global distribution can tolerate aggressive compression without sacrificing convergence. The method introduces a lightweight proxy for data heterogeneity based on the cosine similarity between local and global gradient directions, computed without sharing raw data.

The authors evaluate AGC on three standard FL benchmarks (CIFAR-10, CIFAR-100, FEMNIST) with heterogeneous partitions. The main results show a 2.3x communication reduction compared to uniform top-k compression at matched final accuracy, and 1.4x improvement over the closest adaptive baseline (DGC). The paper also provides a convergence analysis under standard assumptions, showing that AGC preserves the O(1/√T) rate of SGD.

---

## Strengths

- **S1**: The heterogeneity proxy (cosine similarity of gradient directions) is simple, privacy-preserving, and requires no additional communication. This is a genuine design insight, not just an engineering trick. (Section 3.2)
- **S2**: The convergence proof (Theorem 1) properly accounts for client-dependent compression ratios, which most prior analyses do not. The assumptions are standard and clearly stated. (Section 4, Appendix A)
- **S3**: The experimental setup includes a realistic heterogeneity sweep (α ∈ {0.1, 0.5, 1.0} for Dirichlet partition), which is more thorough than many FL papers that test only extreme heterogeneity. (Section 5.1)
- **S4**: Communication cost is measured in actual transmitted bytes, not just number of selected gradients, which avoids the common trap of ignoring encoding overhead. (Table 2)

---

## Major Concerns

### MC-1: Missing comparison with FedPAQ and DRIVE

**What**: The baselines include Top-K, Random-K, DGC, and FedAvg with quantization, but omit FedPAQ (Reisizadeh et al., 2020) and DRIVE (Vargaftik et al., 2021), both of which are adaptive communication methods designed for heterogeneous FL.
**Where**: Section 5.1, Table 1
**Why it matters**: A NeurIPS reviewer familiar with FL communication efficiency will immediately ask "where is FedPAQ?" FedPAQ specifically addresses heterogeneity-aware quantization, which is the same problem this paper targets. Without this comparison, the 1.4x improvement over DGC is unconvincing — FedPAQ may already achieve similar gains.
**Suggested fix**: Add FedPAQ and DRIVE as baselines on at least CIFAR-10/100. If they perform similarly to AGC, the paper needs to articulate the orthogonal advantage (e.g., AGC works with sparsification while FedPAQ addresses quantization).

### MC-2: Convergence analysis assumes bounded gradient dissimilarity, but experiments use extreme heterogeneity

**What**: Theorem 1 requires Assumption 3 (bounded gradient dissimilarity: ‖∇fᵢ - ∇f‖² ≤ δ²), but the experiments with α=0.1 Dirichlet partition create distributions where this bound is likely very large. The paper does not empirically verify or discuss the tightness of δ in practice.
**Where**: Section 4, Assumption 3; Section 5.2
**Why it matters**: A theory-minded reviewer will flag the disconnect between the convergence guarantee and the experimental regime. If δ is large enough, the convergence bound becomes vacuous, and the theory provides no real guarantee for the settings where AGC is most interesting.
**Suggested fix**: Add an empirical measurement of the gradient dissimilarity δ across the experimental settings. Discuss whether the convergence bound is meaningful for α=0.1, or acknowledge that the theoretical guarantee is most relevant for moderate heterogeneity.

### MC-3: No evaluation on a large-scale or realistic FL task

**What**: All experiments are on CIFAR-10, CIFAR-100, and FEMNIST with 100 simulated clients. There is no experiment on a larger-scale task (e.g., StackOverflow, Reddit, or a production-scale vision task) or with more clients.
**Where**: Section 5
**Why it matters**: NeurIPS 2026 FL papers are expected to demonstrate scalability beyond toy benchmarks. A reviewer will question whether the cosine similarity proxy remains cheap and effective with 1000+ clients and production model sizes (e.g., ViT-Base, not ResNet-18).
**Suggested fix**: Add one experiment with a larger model and/or more clients. At minimum, discuss computational overhead of the proxy at scale with concrete numbers.

---

## Minor Concerns

- **mn-1**: The abstract says "up to 3x communication reduction" but Table 2 shows the maximum is 2.7x (FEMNIST, α=0.1). The "3x" should be corrected or contextualized. (Abstract, line 4)
- **mn-2**: Figure 3 (convergence curves) uses log scale for communication cost but linear scale for accuracy, making the improvement look larger than it is visually. Consider matching axes or adding a linear-scale version. (Figure 3)
- **mn-3**: The related work section does not discuss concurrent work on adaptive compression (e.g., Eden, Vargaftik et al., 2023), which appeared on arXiv before the likely submission deadline.
- **mn-4**: Algorithm 1 uses "ComputeProxy()" without specifying the computational cost. A reviewer may wonder if this adds non-trivial overhead per round.

---

## Questions for Authors

1. How does AGC perform when combined with secure aggregation? The cosine similarity proxy requires comparing local and global gradient directions — does this leak information about local gradients? (Section 3.2)
2. What happens when a client's data distribution shifts over time? Is the proxy recalculated each round, and if so, does the adaptation lag hurt convergence? (Section 3.3)
3. The convergence proof assumes full client participation per round. How does partial participation (standard in cross-device FL) affect the theoretical guarantees? (Theorem 1)

---

## Missing References

- Reisizadeh et al., 2020 (FedPAQ) — directly addresses heterogeneity-aware quantization in FL; omission is conspicuous.
- Vargaftik et al., 2021 (DRIVE) — adaptive sketching for distributed learning with theoretical guarantees.
- Haddadpour et al., 2021 — convergence analysis for compressed FL with heterogeneous data; provides relevant comparison for Theorem 1.
- Jhunjhunwala et al., 2021 (FedLin) — linear speedup under heterogeneity with communication compression.

---

## Verdict

**Overall recommendation**: WEAK REJECT

**Confidence**: HIGH

**Summary judgment**: The core idea — adapting compression ratios per client based on a privacy-preserving heterogeneity proxy — is sound and the convergence analysis is non-trivial. However, the missing baselines (MC-1) are a significant gap that undermines the empirical contribution, and the lack of any evaluation beyond small-scale benchmarks (MC-3) is below the bar for NeurIPS 2026. With the baseline and scale concerns addressed, this could become a solid paper. In its current form, it is not ready.

---

## Revision Checklist

### MUST-FIX — Blocks acceptance

- [ ] `[MF-1]` Add FedPAQ and DRIVE as baselines on CIFAR-10 and CIFAR-100; update Table 1 and discussion ← MC-1
- [ ] `[MF-2]` Empirically measure gradient dissimilarity δ across experimental settings; discuss whether Theorem 1's bound is vacuous at α=0.1 ← MC-2
- [ ] `[MF-3]` Add one experiment at larger scale (≥500 clients or ViT-Base model) or provide concrete computational overhead analysis of the proxy at scale ← MC-3

### SHOULD-FIX — Significantly strengthens paper

- [ ] `[SF-1]` Correct abstract claim from "3x" to match actual maximum (2.7x) ← mn-1
- [ ] `[SF-2]` Add missing references: FedPAQ, DRIVE, Haddadpour et al., Jhunjhunwala et al. ← Missing References
- [ ] `[SF-3]` Address secure aggregation compatibility in Section 3 or Discussion ← Question 1
- [ ] `[SF-4]` Discuss partial participation in the convergence analysis or as a stated limitation ← Question 3

### NICE-TO-HAVE — Polish

- [ ] `[NH-1]` Add linear-scale version of Figure 3 or use consistent axes ← mn-2
- [ ] `[NH-2]` Add computational cost annotation to Algorithm 1's ComputeProxy() call ← mn-4
- [ ] `[NH-3]` Cite concurrent work on adaptive compression (Eden) ← mn-3
