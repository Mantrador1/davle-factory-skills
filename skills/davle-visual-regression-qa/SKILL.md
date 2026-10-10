---
name: davle-visual-regression-qa
description: Compare a generated DAVLE dial against its approved/source image and detect unintended layout, typography, color, texture, icon, or geometry drift outside allowed edit regions. Use after any surgical edit or iterative refinement.
---

# DAVLE Visual Regression QA

## Objective
Detect collateral changes before a generated edit is shown as acceptable.

## Required inputs
- source image,
- generated image,
- mutable region map from `davle-dial-structure-mapping`.

## Checks
Outside mutable/dependent regions compare:
- dial framing and scale,
- region positions,
- silhouettes,
- major edges,
- typography content and placement,
- colors,
- textures/patina,
- screws/plates,
- icons,
- logo,
- data values,
- subdial geometry.

## Quantitative option
When image-analysis tooling is available:
1. align source and candidate by dial circle / stable anchors,
2. mask mutable + dependent regions,
3. compare remaining area using structural similarity, edge-map difference and perceptual color difference,
4. visually inspect all flagged drift.

Do not rely on a single scalar metric; typography or geometry changes can be severe even when global similarity is high.

## Hard fails
REJECT if any locked region has:
- moved or resized module,
- changed text/value,
- altered icon,
- changed material/color family,
- added/removed screw or plate,
- changed bezel/minute track,
- changed moon/weather image,
- changed logo,
- changed framing,
unless explicitly allowed.

## Severity
- CRITICAL: layout or identity drift.
- MAJOR: visible locked-region restyle.
- MINOR: tiny texture/noise variation with no functional effect.

## Regeneration
Regenerate from the original approved source and narrow the edit prompt. Never “repair” drift by repeatedly editing a drifted image.

## Output
PASS / REVISE / REJECT with:
- changed locked regions,
- severity,
- allowed changes confirmed,
- exact next correction.
