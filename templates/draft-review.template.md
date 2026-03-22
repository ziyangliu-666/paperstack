---
generated: {TIMESTAMP}
venue: {VENUE}
venue_guidance_source: {SOURCE_URL_OR_FALLBACK}
venue_guidance_status: {live | cached | generic-fallback}
venue_guidance_cached_at: {ISO_8601_OR_NULL}
manuscript: {MAIN_MANUSCRIPT_PATH}
files_read:
  - {FILE_1}
  - {FILE_2}
files_missing:
  - {MISSING_FILE_1}
reduced_context: {true|false}
---

# Draft Review: {TITLE}

**Target venue**: {VENUE}
**Manuscript**: {MAIN_MANUSCRIPT_PATH}
**Review date**: {DATE}

{If venue guidance was degraded, show warning here:}
{> ⚠️ **Venue guidance**: {FALLBACK_MESSAGE}}

---

## Paper Summary

{2-3 paragraph summary demonstrating understanding of the paper. Write as a reviewer would in a conference review form — show the authors you read the paper carefully before critiquing it.}

---

## Strengths

{Bulleted list of specific strengths. Each must reference a concrete aspect — a result, technique, analysis, or framing. No generic praise.}

- **S1**: {specific strength with reference to section/figure/table}
- **S2**: {specific strength}
- **S3**: {specific strength}

---

## Major Concerns

{Issues that would individually justify rejection or major revision if unaddressed.}

### MC-1: {Title of concern}

**What**: {Precise statement of the concern}
**Where**: {Section, claim, table, or figure reference}
**Why it matters**: {Why a reviewer would flag this as a rejection reason}
**Suggested fix**: {Concrete path to resolution}

### MC-2: {Title}

**What**: {concern}
**Where**: {location}
**Why it matters**: {reasoning}
**Suggested fix**: {resolution}

---

## Minor Concerns

- **mn-1**: {specific minor concern with location reference}
- **mn-2**: {concern}
- **mn-3**: {concern}

---

## Questions for Authors

{Questions a reviewer would ask in the review form. The paper should preemptively answer these.}

1. {question with reference to specific section or claim}
2. {question}
3. {question}

---

## Missing References

{Papers that a knowledgeable reviewer would expect to see cited. For each, explain why it is relevant.}

- {Author et al., Year} — {why this reference is expected}
- {Author et al., Year} — {relevance}

---

## Verdict

**Overall recommendation**: {STRONG ACCEPT | WEAK ACCEPT | BORDERLINE | WEAK REJECT | STRONG REJECT}

**Confidence**: {HIGH | MEDIUM | LOW}

**Summary judgment**: {2-3 sentences synthesizing the verdict. Reference specific strengths and concerns. The judgment must follow logically from the review above — do not soften a critical review with a generous verdict.}

---

## Revision Checklist

### MUST-FIX — Blocks acceptance

- [ ] `[MF-1]` {Specific actionable task} ← MC-1
- [ ] `[MF-2]` {Task} ← MC-2

### SHOULD-FIX — Significantly strengthens paper

- [ ] `[SF-1]` {Task} ← mn-{N} or Question {N}
- [ ] `[SF-2]` {Task}

### NICE-TO-HAVE — Polish

- [ ] `[NH-1]` {Task}
- [ ] `[NH-2]` {Task}
