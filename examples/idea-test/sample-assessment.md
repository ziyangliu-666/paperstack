# Idea Assessment: Curriculum-Aware Knowledge Distillation

**Date**: 2026-03-15
**Verdict**: REFINE

---

## The Idea

Use curriculum learning principles to schedule which layers of a teacher model transfer knowledge to a student during distillation. Instead of distilling all layers simultaneously, start with shallow layers (which capture syntax/low-level features) and progressively add deeper layers (which capture semantics/reasoning). The hypothesis is that students learn more effectively when the knowledge transfer follows the same shallow-to-deep progression that the teacher itself learned during pretraining.

## Falsifiable Claim

"I claim that scheduling layer-wise knowledge distillation from shallow-to-deep during student training produces a student model that matches the teacher's downstream task performance with 40% fewer training steps, because shallow features are prerequisite for learning deep features, and simultaneous transfer creates conflicting optimization objectives."

## Risk Map

| Dimension | Rating | Evidence |
|---|---|---|
| Novelty | MEDIUM | Layer-wise distillation exists (PKD, Sunetal 2019). The scheduling idea adds something, but the delta from progressive training is incremental. Must clearly differentiate from curriculum distillation (Haghani et al., 2021). |
| Significance | MEDIUM | 40% fewer training steps is meaningful if real, but contribution framing relies on efficiency, which is a crowded space. Needs an insight beyond "it's faster." |
| Baseline threat | HIGH | Standard KD with the same total compute might achieve comparable results. The naive baseline "distill all layers with linearly increasing weight" is very close to this idea and hasn't been checked. |
| Feasibility | LOW | Can test on BERT-to-TinyBERT in a weekend. Clear experimental setup. |
| Clarity | LOW | The claim is well-stated with a specific mechanism (conflicting gradients from simultaneous transfer). |

## Closest Prior Work

**Paper**: Sun et al., 2019 — "Patient Knowledge Distillation for BERT Model Compression"
**Your delta**: PKD distills from all layers simultaneously with equal weight. Your idea schedules the layer order, starting from shallow layers. PKD treats layers as independent; your idea treats them as having a prerequisite structure.
**Reviewer concern**: "This is PKD with a learning rate schedule on the layer losses. How is this fundamentally different from curriculum learning applied to the loss weights?"

## Simplest Baseline

**Baseline**: Standard PKD (all-layer simultaneous distillation) with the same total training steps.
**Why your idea must beat it**: If scheduling doesn't help over simultaneous transfer, the core claim about conflicting gradients is wrong. This is the make-or-break comparison.

## Significance Statement

If this works, we learn that knowledge distillation has an implicit curriculum — that the ORDER of knowledge transfer matters, not just the amount. This would mean current distillation methods are leaving efficiency on the table by ignoring feature dependencies. Practitioners building compressed models (mobile deployment, edge inference) would get smaller students faster.

## One-Week Test

**Experiment**: Distill BERT-base to a 4-layer student on MNLI.
- Condition A: Standard PKD (all layers, simultaneous)
- Condition B: Scheduled (layers 1-3 first 30% of training, add layers 4-6 at 30%, add layers 7-12 at 60%)
- Compare validation accuracy curves at 50K, 100K, 150K steps.

**Pass criterion**: Condition B reaches Condition A's final accuracy at least 30% faster (in steps).
**Fail criterion**: Conditions A and B have indistinguishable learning curves. If scheduling doesn't matter, the core mechanism claim is dead.
**Resources needed**: 1 GPU, 2-3 days, HuggingFace transformers + existing MNLI data.

## Verdict

**REFINE**

The idea has a testable core mechanism (conflicting gradients from simultaneous transfer) and a cheap validation experiment. However, the novelty risk from PKD and curriculum distillation literature is real — the user needs to clearly articulate why scheduling by layer is fundamentally different from existing curriculum approaches to distillation, which schedule by DATA difficulty. The baseline threat (PKD + adjusted loss weights achieving the same result) needs to be addressed before committing further.

## Next 48 Hours

1. Read Haghani et al., 2021 (curriculum distillation) and PKD carefully. Map the exact technical delta.
2. Run the one-week test (BERT→4-layer on MNLI) with the two conditions.
3. If the learning curves differ meaningfully, run `/idea-sharpen` to refine the positioning and draft abstract.
