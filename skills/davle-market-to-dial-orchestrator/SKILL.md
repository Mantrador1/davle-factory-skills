---
name: davle-market-to-dial-orchestrator
description: Orchestrate the complete DAVLE market-to-dial workflow from fresh market research through trend analysis, pattern extraction, portfolio context, commercial candidate synthesis, opportunity scoring, prompt creation, dial-only image generation, visual QA, and standardized factory handoff. Use when the user asks DAVLE to discover what is selling and produce the strongest dial-only concept end to end.
---

# DAVLE Market-to-Dial Orchestrator

## Objective
Run the complete modular workflow while preserving evidence boundaries and letting each specialist skill own its decision layer.

## Sequence
1. Run `davle-watchface-market-research` when the decision depends on the current market.
2. Pass the evidence packet to `davle-watchface-trend-analysis`.
3. Pass trend findings to `davle-watchface-pattern-extraction`.
4. Run `davle-watchface-portfolio-intelligence` when a reliable DAVLE portfolio registry/context is available.
5. Pass market, trend, pattern, and portfolio context to `davle-commercial-dial-synthesis`.
6. Generate 2–3 meaningful candidate theses for open-ended tasks, or one candidate for a narrow user-specified direction.
7. Run `davle-watchface-opportunity-scoring` on competing candidates. Select one PRODUCE candidate; do not force production when every candidate is HOLD/DO_NOT_PRODUCE.
8. If the winner has HIGH cannibalization risk, modify or replace it and rescore before generation.
9. Pass the approved thesis to `davle-dial-prompt-engineering`.
10. Generate only the dial image using the available image-generation capability.
11. Run `davle-dial-visual-qa`.
12. If QA returns REVISE and the defect is concretely correctable, regenerate using targeted correction instructions and re-run QA. Stop rather than falsely ACCEPT if a critical defect remains.
13. Build the final handoff using `schemas/factory-handoff.schema.json` when available.

## Evidence rules
- Keep OBSERVED FACT, INFERENCE, and CREATIVE DECISION distinct.
- Never convert ranking, reviews, ratings, install bands, or visibility proxies into invented sales numbers.
- Do not let downstream skills silently overwrite upstream evidence.

## Design rules
- Produce dial-only imagery unless explicitly requested otherwise.
- Optimize for coherent commercial value, not a collage of competitor features.
- Preserve originality; use market patterns, not competitor identity.
- Prefer one strong production thesis over multiple unresolved directions.

## Final handoff
Provide:
- market rationale and evidence confidence,
- trend signal and winning patterns,
- selected commercial thesis,
- opportunity score/risk summary when used,
- exact generation prompt,
- final dial image reference,
- concise visual implementation notes,
- QA verdict and defects,
- factory-ready package consistent with the handoff schema.

## Failure behavior
If evidence is too weak, all candidates fail commercial scoring, or the final image fails critical QA, say so explicitly. Do not manufacture certainty or accept a weak asset merely to complete the sequence.