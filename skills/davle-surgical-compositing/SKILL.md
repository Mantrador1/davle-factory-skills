---
name: davle-surgical-compositing
description: Enforce pixel-level preservation for DAVLE source-image edits by compositing only approved mutable regions from a generated candidate back onto the original source image. Use for surgical edits where the user explicitly says not to change anything else.
---

# DAVLE Surgical Compositing

## Objective
Convert “do not change anything else” from a prompt preference into a deterministic image-processing rule.

## When to use
Use after image generation/editing when:
- an existing approved dial is the source,
- only specific hands, icons, gauges, labels, or local regions may change,
- all other pixels/layout must remain identical.

## Core method
1. Start from the original approved source image.
2. Generate/edit the requested change.
3. Build a binary/soft mask for MUTABLE + required DEPENDENT regions.
4. Composite:
   - candidate pixels inside the mask,
   - original source pixels everywhere outside the mask.
5. Feather mask edges minimally only where needed to avoid seams.
6. Run visual regression QA.

## Mask semantics
- black = preserve original source exactly,
- white = accept candidate pixels,
- grey = feather/blend edge only.

## Region construction
Prefer the smallest geometrically valid mask:
- hand edit: narrow polygon/capsule around old + new hand sweep and center hub,
- icon edit: button/icon bounding region only,
- text edit: exact text cell,
- gauge edit: gauge region and only its true dependencies.

Do not use large circular/global masks for local edits.

## Preservation guarantee
After final compositing, every pixel outside the non-black mask comes from the original source. Therefore collateral redesign outside the approved region is structurally impossible.

## Limitations
If the requested replacement requires reconstructing background that was hidden by the original element, local inpainting may still be needed inside the mutable mask. This does not justify changing pixels outside the mask.

## Retry rule
Always composite against the original approved source, never a drifted derivative.

## Tool
Use `tools/locked_region_composite.py` when a Python/Pillow runtime is available.

## QA
PASS only if:
- the requested change is correct,
- no forbidden pixels changed,
- seams are not visible,
- typography/layout outside the mask is identical,
- the candidate remains factory-usable.
