---
name: davle-watchface-opportunity-scoring
description: Score and rank DAVLE watch-face concept opportunities using explicit commercial criteria, evidence confidence, momentum, saturation, differentiation, utility, screenshot impact, and implementation fit. Use when multiple styles or concepts compete for production, when the strongest market opportunity must be selected, or when a design thesis needs an evidence-based commercial score before image generation.
---

# DAVLE Watch Face Opportunity Scoring

## Objective
Rank candidate watch-face opportunities without disguising subjective judgment as certainty. Use the market evidence and trend/pattern handoffs as inputs.

## Preconditions
- Require a current market evidence packet when the question depends on what is selling now.
- Require at least one explicit candidate concept or category direction.
- Mark missing evidence instead of filling gaps with invented values.

## Score dimensions
Score each dimension from 0 to 5, then apply the weight:

| Dimension | Weight |
|---|---:|
| Market evidence strength | 20 |
| Trend momentum | 15 |
| Demand breadth | 10 |
| Saturation headroom | 10 |
| Screenshot / thumbnail impact | 10 |
| Practical utility | 10 |
| Premium perception | 8 |
| Differentiation potential | 10 |
| Factory implementability | 7 |

Weighted total = 0–100.

## Evidence confidence
Assign confidence:
- HIGH: multiple independent current signals support the candidate.
- MEDIUM: useful evidence exists but contains material gaps.
- LOW: candidate depends mainly on inference or sparse data.

Do not multiply the score by a fabricated precision factor. Report confidence separately.

## Saturation rule
A popular category is not automatically attractive. Give high saturation-headroom scores only when demand appears strong and there is credible whitespace for a differentiated DAVLE concept.

## Kill conditions
Flag a candidate as DO NOT PRODUCE when any of the following is dominant:
- no credible demand signal,
- extreme clone risk,
- differentiation depends on competitor identity,
- poor glance readability is intrinsic to the concept,
- severe implementation mismatch,
- commercial hook exists only in a lifestyle mockup and not in the dial itself.

## Decision procedure
1. Score every candidate against the same dimensions.
2. Cite the evidence or inference behind every dimension scored 4 or 5.
3. State the strongest weakness for every candidate.
4. Rank candidates by weighted score, then use confidence and kill conditions as tie-breakers.
5. Select one production candidate unless the user requests multiple.
6. Pass the winning candidate and score rationale to prompt engineering.

## Output
Return:
- candidate ranking,
- 0–100 score,
- confidence level,
- strongest supporting evidence,
- strongest commercial risk,
- PRODUCE / HOLD / DO NOT PRODUCE,
- concise handoff to the next skill.

## Guardrail
Treat the score as a disciplined decision aid, not a prediction of actual sales or revenue.