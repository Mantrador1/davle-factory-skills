# NEGATIVE PROMPTS — Defect Suppression Library

> **Purpose.** Positive prompts say what to draw; negative prompts forbid the specific ways
> renderers fail. Every defect the operator reported has a matching negative clause here.
> The brain assembles the negative prompt by pulling the relevant blocks for the chosen template.

> Renderer note: Ideogram/SD-family accept a dedicated negative field. For models without a
> negative field (some GPT-image / Gemini-image endpoints), fold these as positive
> *constraints* ("...with NO missing hands, ALL twelve markers fully inside the dial, ...").
> Either way, the content below is the checklist.

---

## Block 1 — Missing-component defects (fidelity)

Maps to: "λείπει ο δείκτης δευτερολέπτων", "λείπει το τόξο", "στοιχεία λείπουν εντελώς".

```
missing seconds hand, missing central hand, missing hands, only one hand,
missing sub-dial hands, empty sub-dials, missing power-reserve arc, missing scales,
missing tachymeter ring, missing markers, fewer than twelve hour markers,
missing crown, missing pushers, blank dial, omitted complications, simplified dial,
dropped details, incomplete watch
```

**Better still:** restate the must-haves positively in the main prompt
(`exactly twelve hour markers; a thin central seconds hand WITH a counterweight tail;
two sub-dials each WITH its own hand; a curved power-reserve arc at 12`). Negatives alone
do not guarantee inclusion — pairing is what works.

---

## Block 2 — Framing / cropping defects

Maps to: "οι δείκτες των ωρών είναι εκτός πλαισίου".

```
hour markers touching the edge, markers cut off by the frame, indices outside the dial,
dial cropped, watch cut off, case clipped by frame, off-center dial, tilted dial,
hands extending beyond the dial, elements bleeding off canvas, zoomed-in crop,
asymmetric placement, dial not fully visible
```

Positive partner clause: `the entire watch face perfectly centered and fully visible,
all twelve markers sitting on a radius well inside the crystal edge, generous even margin
around the case` (see `FRAMING_LAYOUT_v1.md`).

---

## Block 3 — Texture / flatness defects

Maps to: "λείπουν οι υφές μέσα στα εσωτερικά καντράν".

```
flat sub-dials, plastic look, matte featureless surfaces, no texture, untextured metal,
painted-on details, sticker look, toy watch, printed flat dial, cartoonish,
uniform single finish, no specular highlights, no reflections, dull metal, CGI plastic
```

Positive partner: pull the guilloché/finish-stacking clauses from `MATERIALS_FINISHES_LIGHTING_v1.md`.

---

## Block 4 — Geometry / "sloppy cuts" defects

Maps to: "τα εσωτερικά καντράν έχουν τσαπατσούλικα κοψίματα".

```
sloppy sub-dial edges, ragged circle, uneven sub-dial frame, broken ring, wobbly circles,
melted edges, smeared center, blobby pinion, misaligned hands, hands not on center axis,
crooked markers, uneven marker spacing, warped chapter ring, non-circular dial, lopsided bezel,
double rings, overlapping duplicated scales
```

Positive partner: `perfectly circular concentric rings, crisp clean polished sub-dial frames,
all hands pivoting from a single clean central pinion, evenly spaced markers at exact 30° intervals`.

---

## Block 5 — AI-artifact / text defects

```
gibberish text, misspelled brand, random letters, distorted numbers, duplicated numerals,
extra crowns, extra pushers, three hands fused, watermark, signature, logo overlay, frame,
border, caption, UI chrome, jpeg artifacts, banding, noise, oversharpened halos,
deformed, asymmetrical case, lens flare clutter, extra sub-dials, phantom complications
```

Note on text: it is safer to keep dial text minimal and explicitly specified than to let the
model invent numerals. If exact scale numbers are not legible in the reference, instruct
`fine tick marks without numerals` rather than risk gibberish.

---

## Block 6 — Lighting defects

```
multiple conflicting light sources, harsh flat lighting, blown-out highlights,
crushed blacks with no detail, flat ambient with no specular, unrealistic reflections,
reflection of a photographer, HDR halos, overexposed dial
```

---

## Block 7 — Wear-OS deliverable defects (when rendering the final asset, not the hero)

```
drop shadow under watch, floating watch, background scenery, wrist, arm, hand model,
strap, lugs dominating frame, perspective tilt, 3/4 angle (when a flat top-down face is required)
```

---

## Assembly rule

The brain selects blocks by template:
- **Photoreal-luxury hero:** Blocks 1,2,3,4,5,6 (skip 7 — hero may keep studio context).
- **Final 454×454 deliverable:** Blocks 1,2,4,5 + Block 7 (flat, no scenery, top-down).
- **Neon-minimal:** Blocks 1,2,4,5 (skip 3 texture/6 studio — flat is intended there).

Always order the negative prompt: fidelity (1) → framing (2) → geometry (4) → artifacts (5)
→ texture/lighting (3,6) → deliverable (7). Highest-impact defects first.
