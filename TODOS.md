# TODOs

## P1: Submission Compliance Scan

**Depends on**: `/draft-review` skill + venue-aware rubric (landed)

Add a compliance scan that checks for:
- Double-blind leakage (author names, institution references, GitHub URLs in code, acknowledgments)
- Self-citation exposure (e.g., "In our prior work [Anonymous, 2024]" patterns that reveal identity)
- Missing required sections (limitations, ethics statement, broader impact — venue-dependent)
- Venue-procedural risks (page limit violations, wrong template, missing supplementary format)

This should be a separate skill or an optional flag on `/draft-review`, not a silent check baked into the review. Authors should opt in to compliance scanning.

**Why P1**: These are mechanical rejection causes that a reviewer simulator should catch. They are lower-value than substantive review but higher-certainty — a double-blind violation is a guaranteed desk reject at many venues.

## P2: Rebuttal-Aware Review Mode

Add an explicit opt-in mode that reads `rebuttal.*`, `response.*`, or prior review artifacts when the user wants a revision-cycle review rather than a first-pass manuscript review.

**Why P2**: These files are useful in later submission cycles, but reading them by default biases the initial reviewer simulation and contaminates the manuscript-only flow.
