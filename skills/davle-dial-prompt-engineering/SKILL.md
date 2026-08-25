---
name: davle-dial-prompt-engineering
description: Convert an approved DAVLE commercial dial concept into a precise image-generation prompt that produces only the watch-face dial artwork. Use immediately before image generation for DAVLE concepts, especially when strict dial-only framing, hierarchy, geometry, readability, and reproducible prompt controls are required.
---

# DAVLE Dial Prompt Engineering

## Objective
Produce a generation prompt that preserves the approved commercial thesis while maximizing dial-only compliance, clean geometry, hierarchy, and usefulness as a factory visual reference.

Read `references/prompt-controls.md` when building or correcting a production prompt.

## Mandatory framing
Always specify:
- dial artwork only,
- straight-on orthographic front view,
- centered circular composition,
- no watch case,
- no crown, lugs, buttons, strap, bracelet, wrist, hand, lifestyle scene, packaging, or perspective tilt,
- no reflective glass obscuring information.

## Workflow
1. Start from the approved commercial thesis, not from a competitor image or brand name.
2. Describe object/framing first, then information hierarchy, then geometry, then styling.
3. Define which element owns primary time readability.
4. Specify layout zones, relative positions, spacing logic, typography class, hands/indices where applicable, complication count, palette, texture, and information density.
5. Design around image-generator weaknesses: minimize unnecessary microtext, avoid fragile ornament, and demand clean numerals/indices.
6. Add explicit negative constraints against whole-watch leakage and malformed geometry.
7. Keep physical-product rendering cues out of the prompt unless explicitly required.
8. After a failed generation, change only the controls related to the observed defect before regenerating.

## Output
Return one production prompt in English plus concise negative constraints when useful.

## Regression discipline
Record reusable prompt learnings only after real generations. Separate:
- observed failure,
- control changed,
- observed result.

Do not declare one successful wording a universal rule from a single sample.

## Quality gate
Reject and rewrite the prompt if:
- it could plausibly generate a complete physical watch,
- the main time hierarchy is ambiguous,
- key layout relationships are unspecified,
- it relies on another brand's identity,
- it requests excessive microtext or geometry too fragile for reliable generation.