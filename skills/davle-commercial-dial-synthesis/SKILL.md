---
name: davle-commercial-dial-synthesis
description: Synthesize market research, trend findings, extracted patterns, and available DAVLE portfolio context into original commercially coherent dial candidates. Use when DAVLE needs concrete design theses that combine evidence-backed selling characteristics without copying a competitor, especially before opportunity scoring and image prompt creation.
---

# DAVLE Commercial Dial Synthesis

## Objective
Convert upstream evidence into a small set of coherent original DAVLE design theses suitable for commercial ranking.

## Workflow
1. Read the latest market, trend, pattern, and portfolio handoffs that are available.
2. Define the target buyer/use context for each candidate in one sentence.
3. Select only mutually compatible market patterns.
4. Create 2–3 meaningfully different candidates for autonomous “what should we build next?” tasks. If the user has already fixed a narrow direction, create one strong candidate instead.
5. Give every candidate one primary visual hook that survives at thumbnail size.
6. Set hierarchy: primary time first, supporting data second, decorative depth third unless evidence justifies another hierarchy.
7. Define display mode, layout, palette logic, typography class, information density, complications, customization strategy, and AOD direction.
8. Add distinctive DAVLE expression without copying recognizable competitor composition or branding.
9. State important popular patterns intentionally excluded and why.
10. Pass candidates to `davle-watchface-opportunity-scoring` before final prompt engineering when a commercial choice remains.

## Required thesis fields
For every candidate specify:
- target user,
- category/style,
- primary visual hook,
- information hierarchy,
- layout philosophy,
- color strategy,
- typography direction,
- complication strategy,
- premium level,
- differentiation,
- click/purchase logic,
- implementation risks.

## Internal viability gate
Reject a candidate before scoring if:
- primary readability is weak by design,
- its commercial hook depends on copying a competitor,
- it is merely a color variant of another candidate,
- it combines incompatible patterns without a coherent hierarchy,
- its essential visual effect cannot translate into a practical watch-face implementation.

## Rules
- Do not create a market-average collage.
- Do not treat every repeated feature as mandatory.
- Prefer coherent segment-specific concepts over one concept trying to satisfy everyone.
- Preserve evidence/inference/creative-decision boundaries.

## Output
Return candidate theses plus a concise handoff to opportunity scoring. After one candidate is selected, provide its final thesis to `davle-dial-prompt-engineering`.