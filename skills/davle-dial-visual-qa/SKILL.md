---
name: davle-dial-visual-qa
description: Evaluate a generated DAVLE dial image against the approved commercial concept, dial-only constraints, readability, geometry, originality, and factory handoff requirements. Use after dial image generation or whenever a candidate dial needs acceptance, rejection, or targeted correction.
---

# DAVLE Dial Visual QA

## Objective
Decide whether a generated dial is commercially coherent, visually clean, faithful to the approved concept, and suitable for factory handoff.

## Inspect
- dial-only compliance,
- straight-on framing,
- circular geometry and symmetry,
- time readability,
- hierarchy,
- typography consistency,
- indices/hands geometry,
- spacing and alignment,
- complication placement,
- contrast,
- clutter,
- AI artifacts or malformed details,
- commercial visual hook,
- originality versus source references,
- feasibility as a watch-face visual source.

## Hard rejects
Reject if any of these are present:
- visible strap, wrist, lugs, crown, physical case, or lifestyle scene,
- severe perspective distortion,
- unreadable or nonsensical key text/time,
- broken circular geometry,
- obvious copied branding or competitor identity,
- major mismatch with the approved concept.

## Scoring
Score 1-5:
- dial-only compliance,
- readability,
- geometry,
- hierarchy,
- visual polish,
- commercial appeal,
- originality,
- factory usability.

Require all hard gates to pass and average score >=4.0 for ACCEPT.

## Output
Return:
- ACCEPT / REVISE / REJECT,
- scores,
- up to 5 highest-impact defects,
- precise correction instructions,
- whether regeneration is required.