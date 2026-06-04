# FRAMING & LAYOUT — Composition and Radial Safe-Area

> **Purpose.** "Οι δείκτες των ωρών είναι εκτός πλαισίου" and "τσαπατσούλικα κοψίματα" are
> composition failures: the renderer placed elements with no awareness of where the dial edge
> and the safe radius are. This file defines a fixed radial coordinate system so every
> component lands inside its band, on a real circle, fully visible.

> Canvas reference: Wear OS active face = **454×454 px, circular**. Hero renders may be larger
> (1024–2048 square) but use the same normalized radii.

---

## The normalized radial system

Treat the dial as concentric bands, radius normalized 0.0 (center) → 1.0 (crystal edge).
Place every component in its band. State the band in the prompt.

| Band | Radius | What lives here |
|---|---|---|
| **R0 — Pinion** | 0.00–0.05 | central hand hub, clean polished pivot |
| **R1 — Inner field** | 0.05–0.35 | brand text, open-heart, central area, hand bodies |
| **R2 — Sub-dial belt** | 0.30–0.62 | sub-dials, LCD module, apertures, power-reserve arc |
| **R3 — Marker ring** | 0.70–0.82 | applied hour markers / indices sit centered here |
| **R4 — Chapter/scale ring** | 0.82–0.92 | minute track, tachymeter, printed scales |
| **R5 — Rehaut / inner bezel** | 0.92–0.96 | slanted inner ring, optional text |
| **R6 — Bezel** | 0.96–1.00 | coin-edge / fluted / tachymeter bezel |
| **SAFE EDGE** | > 0.96 | **nothing functional here.** Crystal + bezel only. |

**Hard rule:** hour markers center on **R3 (~0.76)**. They must never reach > 0.90.
The "markers out of frame" defect is markers drawn at R≈1.0. Pin them to R3 explicitly:
`twelve applied markers centered at ~76% of the dial radius, with clear space between the
markers and the crystal edge`.

---

## Hand-length rules (so hands don't overshoot the frame)

| Hand | Tip reaches |
|---|---|
| Hour | R3 inner edge (~0.55–0.62) |
| Minute | R4 minute track (~0.85) |
| Central seconds | R4/R5 (~0.88), tail counterweight to ~0.15 past center |
| Sub-dial hands | ~80% of that sub-dial's own radius |

State minute hand reaches the minute track but **does not touch the crystal**.

---

## Sub-dial placement (clean, non-overlapping, framed)

- Sub-dials live in **R2**. Center each on a clock position, not floating arbitrarily.
- Common, balanced layouts:
  - **2 registers:** 9 o'clock + 3 o'clock (horizontal), OR 6 + 12. Keep them symmetric.
  - **3 registers:** 3 / 6 / 9 (tri-compax), evenly spaced.
- Each sub-dial diameter ≈ 0.28–0.34 of dial diameter. Do not let two sub-dials touch.
- **Each sub-dial gets a crisp polished frame ring + soft inner shadow** (kills sloppy cuts).
- If a module (LCD) replaces a sub-dial, it occupies the same R2 slot and is described as
  recessed under its own ring.

---

## Symmetry & balance

- The dial is **radially balanced**: a sub-dial at 9 wants visual weight at 3 (sub-dial,
  module, or date window). Avoid one heavy side.
- Markers at exact **30° intervals**. State "evenly spaced at 30° intervals".
- Brand text on the vertical center line (under 12); sub-text balanced under it or above 6.

---

## Crop & margin (the literal frame)

For the **hero / static design image** (what the operator reviews):
```
the entire watch perfectly centered, fully visible, shot straight-on (top-down, zero tilt),
even margin of ~6–8% of canvas on all sides between the bezel and the image edge,
dark seamless studio background, watch occupying ~85% of the frame.
```

For the **final 454×454 Wear OS asset**:
```
flat top-down dial only, circular composition filling the round screen edge-to-edge,
no case sides, no background, no shadow, designed to be masked into a circle,
all markers and the minute track fully inside the visible circle.
```

---

## Composition prompt block (paste-ready)

```
COMPOSITION: perfectly centered, straight-on top-down view, zero perspective tilt,
the complete watch face fully visible with even margin to all edges. Radial layout:
pinion at center; sub-dials/module/arc in the R2 belt (30–62% radius); twelve hour
markers centered at ~76% radius with clear gap to the crystal; minute + tachymeter
scales at 82–92%; bezel at the rim. Hour hand tip ~58%, minute hand to the minute
track ~85% (not touching crystal), thin central seconds to ~88% with a counterweight tail.
Markers evenly spaced at exact 30° intervals. Every element on a true concentric circle.
```

---

## Why this fixes the reported defects

| Reported defect | Layout rule that prevents it |
|---|---|
| Markers out of frame | markers pinned to R3 (~76%), explicit gap to edge |
| Sloppy sub-dial cuts | R2 placement + mandatory polished frame ring + inner shadow |
| Hands overshoot | per-hand tip radius table |
| Off-center / tilted | "straight-on top-down, zero tilt, perfectly centered" |
| Crowded one side | radial balance rule + symmetric register layouts |
| Dial cropped | 6–8% even margin, watch ≤85% of frame |
