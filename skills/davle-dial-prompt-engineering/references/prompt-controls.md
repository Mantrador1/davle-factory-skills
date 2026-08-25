# DAVLE Dial Prompt Controls

Use these controls as reusable building blocks. Do not copy all blocks mechanically; include only what the approved concept requires.

## Prompt order
Prefer this sequence:
1. object and framing,
2. display mode and primary hierarchy,
3. geometry/layout,
4. typography/hands/indices,
5. complications and information density,
6. palette/material/texture,
7. lighting/render treatment,
8. implementation-oriented cleanliness,
9. negative constraints.

## Dial-only framing control
State explicitly:
- watch-face dial artwork only,
- isolated circular dial,
- straight-on orthographic front view,
- centered and perfectly level,
- no physical watch case or exterior hardware.

Repeat the most important negative constraint near the end when the generator tends to produce a whole watch.

## Geometry control
Describe relative structure instead of vague aesthetics:
- exact number of major zones,
- radial versus grid organization,
- primary time position,
- ring hierarchy,
- complication count and approximate clock positions,
- symmetric spacing where intended,
- consistent index lengths and angular intervals.

## Readability control
Specify:
- primary time must dominate at glance,
- high foreground/background contrast,
- secondary data visibly subordinate,
- no decorative element may cross essential time or numerals,
- avoid microtext that cannot be rendered cleanly.

## Typography control
Prefer typography classes and behavior over named proprietary fonts:
- condensed geometric sans,
- monospaced technical digits,
- restrained neo-grotesk,
- engineered stencil accents.

Request clean, correctly formed numerals and minimal nonessential text. Image generators frequently corrupt small text; design around that weakness.

## Analog control
When analog:
- specify hour/minute/seconds hand hierarchy,
- consistent center pivot,
- hand lengths relative to index rings,
- clean separation from complications,
- avoid excessive skeletonization that harms glance reading.

## Digital control
When digital:
- define digit block size and alignment,
- specify hour/minute relationship,
- keep seconds subordinate unless commercially central,
- use stable baseline/grid alignment.

## Hybrid control
When hybrid:
- explicitly state which representation owns primary time,
- prevent analog hands and digital time from competing equally unless intentionally designed as dual-primary.

## Material/texture control
Use restrained material language that can translate into a flat digital asset:
- subtle brushed metal impression,
- fine matte grain,
- controlled radial texture,
- shallow embossed/ring depth.

Avoid physical reflections, glass glare, case reflections, and product-photography cues.

## Negative constraints
Default forbidden elements:
- no watch case,
- no bezel hardware outside the dial graphic,
- no crown,
- no lugs,
- no buttons,
- no strap or bracelet,
- no wrist/hand/person,
- no lifestyle scene,
- no angled view,
- no perspective,
- no packaging,
- no competitor logo/branding,
- no malformed numerals,
- no random decorative microtext.

## Known failure patterns
### Whole-watch leakage
Symptom: case, crown, lugs, or strap appears.
Correction: move “isolated dial artwork only” to the first sentence and repeat explicit forbidden hardware at the end.

### AI microtext noise
Symptom: pseudo-labels and broken words.
Correction: remove nonessential text; replace labels with geometry/icons or leave intentionally blank implementation zones.

### Distorted numeral ring
Symptom: duplicated/missing/warped numerals or indices.
Correction: reduce numeral count, request uniform radial intervals, simplify ornamental layers, and prioritize geometry over texture.

### Hierarchy collapse
Symptom: every data element has equal visual weight.
Correction: explicitly rank primary, secondary, tertiary information and set secondary elements to smaller scale/lower contrast.

### Physical-product render
Symptom: reflections, glass, body depth, photographed watch appearance.
Correction: request flat implementation reference, orthographic graphic rendering, no glass and no external body.

## Regression logging
After a real generation, record only reusable observations:
- prompt control used,
- failure observed,
- correction applied,
- whether correction improved the result.

Do not generalize a single success into a permanent rule without repeated evidence.