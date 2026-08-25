---
name: davle-watchface-trend-analysis
description: Analyze fresh DAVLE watch-face market research to identify current and emerging visual, functional, pricing, and positioning trends. Use after a market scan or when DAVLE needs to know where paid Wear OS watch-face demand appears to be moving.
---

# DAVLE Watch Face Trend Analysis

## Objective
Convert current market evidence into directional trends without confusing frequency with momentum.

## Workflow
1. Read the latest market-research handoff.
2. Cluster products by style, layout, information density, palette, typography, complication strategy, AOD behavior, and positioning.
3. Separate:
   - dominant/current patterns,
   - emerging patterns,
   - mature/saturated patterns,
   - declining or weakly supported patterns.
4. Look for change signals: recent releases, recent updates, repeated newer design choices, review language, developer repetition, and store-positioning shifts.
5. Assign confidence: high / medium / low, based on evidence breadth and recency.

## Rules
- A common pattern is not automatically a growing trend.
- Do not declare a trend from one developer or one product family.
- State when evidence cannot establish direction over time.
- Preserve counterexamples.

## Output
Return:
- 5-10 strongest current trends,
- 3-5 emerging signals,
- saturated/overused patterns to avoid blindly copying,
- confidence for each finding,
- handoff to `davle-watchface-pattern-extraction`.