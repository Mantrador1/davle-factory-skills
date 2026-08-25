---
name: davle-watchface-market-research
description: Research the current commercial Wear OS watch-face market and identify evidence-backed successful paid watch faces, pricing, rankings, reviews, visual styles, and recurring buyer signals. Use when DAVLE needs fresh market evidence, top-paid references, competitor scans, a current market snapshot, or standardized product records before concept creation.
---

# DAVLE Watch Face Market Research

## Objective
Produce a fresh, evidence-backed market snapshot for paid/successful Wear OS watch faces. Do not reuse stale embedded conclusions when current research is possible.

Use `schemas/market-product-record.schema.json` as the canonical product-record contract when the repository is available.

## Workflow
1. Search current Google Play and reputable secondary sources for paid/successful Wear OS watch faces.
2. Build a comparison set of at least 20 relevant products when enough credible evidence exists.
3. For every product capture, when available: name, developer, price, rating, review volume, install/download signal, ranking/visibility, update recency, display mode, style cluster, visual hook, visible complications, customization/AOD claims, color/typography direction, buyer praise/complaints, and source/date.
4. Separate OBSERVED FACT from INFERENCE.
5. Mark unavailable or unverifiable metrics as data gaps instead of guessing.
6. Prefer recent evidence and record the research date.
7. Use consistent fields across products so downstream scoring compares like with like.

## Evidence rules
- Never call something a bestseller solely because it looks popular.
- Never present review count, rating, or install bands as actual paid sales.
- Distinguish paid ranking, popularity, rating, install signal, and inferred commercial strength.
- Treat screenshots/store copy as positioning evidence, not proof of conversion.
- Preserve source links or source identifiers.
- Give each product evidence confidence: HIGH / MEDIUM / LOW.

## Minimum evidence behavior
Target 20+ credible current references. If fewer than 10 are available, explicitly label the market snapshot LIMITED and lower confidence rather than expanding with weak evidence.

## Output
Return:
- standardized product records,
- strongest current commercial clusters,
- notable outliers,
- repeated buyer-facing promises,
- recurring complaints,
- data gaps and confidence limits,
- concise handoff to `davle-watchface-trend-analysis`.

## Guardrail
This skill discovers evidence. It does not choose the final DAVLE concept and does not convert proxies into invented sales figures.