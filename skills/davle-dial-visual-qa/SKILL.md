---
name: davle-dial-visual-qa
description: Evaluate a generated DAVLE dial image against the approved commercial concept using hard gates for dial-only framing, geometry, readability, text/numeral integrity, originality, thumbnail impact, and factory-reference suitability. Use after dial image generation or whenever a candidate dial needs acceptance, rejection, or targeted regeneration instructions.
---

# DAVLE Dial Visual QA

## Objective
Decide whether a generated dial is commercially coherent, visually clean, faithful to the approved concept, original, and suitable for factory handoff.

Read `references/qa-gates.md` before evaluating a production candidate.

## Evaluation order
1. Check hard gates before aesthetic scoring.
2. Compare the image against the approved commercial thesis.
3. Test primary readability and thumbnail-scale commercial impact.
4. Inspect geometry, typography/numerals, indices/hands, spacing, complications, contrast, and AI artifacts.
5. Classify defects as CRITICAL / MAJOR / MINOR.
6. Score only after hard-gate inspection.

## Hard rejects
A candidate cannot be ACCEPTED when any of these are present:
- visible strap, wrist, lugs, crown, buttons, physical case, or lifestyle/product scene,
- severe perspective distortion,
- unreadable or materially ambiguous primary time,
- broken circular/radial geometry,
- malformed critical numerals or duplicated essential markers,
- obvious copied branding or recognizable competitor identity,
- major mismatch with the approved concept.

## Scoring
Score 1–5:
- dial-only compliance,
- front-facing geometry,
- primary readability,
- hierarchy,
- numeral/text integrity,
- visual polish,
- commercial thumbnail impact,
- originality,
- factory usability.

Require all hard gates to pass and average score >=4.0 for ACCEPT.

## Verdicts
- ACCEPT: all hard gates pass and no unresolved major defect remains.
- REVISE: concept is viable but one or more correctable major defects remain.
- REJECT: core concept or generation is unsuitable, derivative, or structurally broken.

## Regeneration behavior
For REVISE, return targeted correction instructions that state:
- observed defect,
- what must be preserved,
- exact correction,
- what must not recur.

Do not regenerate merely for subjective preference if the candidate already passes the approved commercial thesis and quality gates.

## Output
Return:
- ACCEPT / REVISE / REJECT,
- hard-gate PASS/FAIL table,
- numeric scores,
- highest-impact defects with severity,
- precise correction instructions,
- whether regeneration is required,
- factory-reference suitability verdict.