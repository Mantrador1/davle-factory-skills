---
name: davle-dial-prompt-engineering
description: Convert an approved DAVLE commercial dial concept into a precise image-generation prompt that produces only the watch-face dial artwork. Use immediately before image generation for DAVLE concepts, especially when strict dial-only framing and layout fidelity are required.
---

# DAVLE Dial Prompt Engineering

## Objective
Produce a generation prompt that preserves the commercial design thesis while enforcing a clean, front-facing dial-only image.

## Mandatory framing
Always specify:
- dial only,
- straight-on / orthographic front view,
- centered circular composition,
- no watch case,
- no bezel hardware unless it is part of the graphic dial itself,
- no crown,
- no lugs,
- no strap,
- no wrist or hand,
- no lifestyle scene,
- no product box,
- no perspective tilt,
- no reflective glass obscuring information.

## Workflow
1. Translate the approved architecture into explicit visual instructions.
2. Describe hierarchy before decoration.
3. Specify geometry, zones, relative placement, typography class, hands/indices when applicable, palette, texture, lighting, and information density.
4. Include negative constraints against forbidden whole-watch elements.
5. Avoid vague words such as 'cool', 'premium', or 'futuristic' unless followed by concrete visual meaning.
6. Do not reference competitor brand names as a shortcut for style.

## Output
Return one production prompt in English, optimized for image generation, plus a short negative-constraints line if the generator benefits from it.

## Quality gate
Reject and rewrite the prompt if:
- it could plausibly generate a complete physical watch,
- the main time hierarchy is ambiguous,
- key layout relationships are unspecified,
- it relies on another brand's identity rather than explicit design language.