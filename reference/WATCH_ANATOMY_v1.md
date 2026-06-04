# WATCH ANATOMY — Component Taxonomy for Render Prompts

> **Purpose.** This is the controlled vocabulary the design brain MUST use when it
> reads a reference watch and writes a render prompt. Every render prompt enumerates
> each component that is present in the reference. **Components that are not named are
> the components that get dropped by the renderer.** The missing seconds hand, the
> missing top arc, the out-of-frame hour markers — all of them are absent because the
> prompt never named them. This file makes "naming everything" mechanical.

> Read together with: `MATERIALS_FINISHES_LIGHTING_v1.md` (how each part looks),
> `FRAMING_LAYOUT_v1.md` (where each part sits), `NEGATIVE_PROMPTS_v1.md` (defects to forbid).

---

## How to use this file

1. Put the reference image in front of you.
2. Walk the **Enumeration Checklist** below top-to-bottom. For every row, decide:
   PRESENT / ABSENT. If PRESENT, capture its attributes (count, position, color,
   finish, length).
3. Every PRESENT component becomes an explicit clause in the render prompt. No
   component is "implied". If it is on the dial, it is in the prompt.
4. A component that is PRESENT in the reference but you do not name in the prompt is
   a **fidelity bug**. Treat it like a dropped requirement.

---

## Enumeration Checklist (walk every row)

### A. Case & external structure
- **Case shape** — round / cushion / tonneau / square. Default round (454×454 Wear OS).
- **Case material & finish** — see materials file (e.g. brushed rose-gold, polished steel).
- **Bezel** — type and texture:
  - `coin-edge` / `fluted` / `knurled` (the fine vertical teeth around the rim)
  - `smooth polished`
  - `tachymeter bezel` (engraved scale on the bezel itself)
  - `diver unidirectional` (minute track + pip at 12)
- **Crown** — position (typically 3 o'clock), shape (onion / fluted cylinder / cabochon), material.
- **Pushers** — chronograph pushers flanking the crown (2 o'clock & 4 o'clock). Count them.
- **Lugs / case flank** — visible at edges; usually cropped on a watch face but note if visible.

### B. Dial base
- **Dial color & finish** — matte black / sunray blue / lacquered / fumé (gradient). See materials.
- **Dial texture** — flat / sunray brushed / vertical brushed / opaline / fumé gradient.
- **Inner bezel ring / rehaut** — the slanted ring between dial and crystal; often carries text or a minute track.

### C. Chapter ring & scales (the printed/engraved rings)
These are the dense outer rings. They are frequently the richest, most-dropped detail.
- **Minute / seconds track** — the fine tick ring at the outer dial. Note tick density
  (e.g. 60 minute ticks + 5 longer 5-minute ticks).
- **Tachymeter scale** — descending numerals (e.g. 500…60) used to compute speed.
- **Telemeter / pulsometer / decimal scale** — secondary printed arcs (often concentric, in a second color).
- **Direction of scales** — clockwise / counter-clockwise, and start value. Capture exact-ish numbers if legible.
- **Scale color(s)** — printed scales are often in a contrasting tint (gilt, white, red 5-min markers).

### D. Hour markers (the "indices")
This is where "markers out of frame" happens — markers must be pinned to the chapter ring radius.
- **Marker type** — applied faceted batons / printed lines / Arabic numerals / Roman / dot markers / mixed.
- **Marker count & layout** — 12 markers; note if 3/6/9/12 are special (numerals or double).
- **Marker finish** — polished applied metal, lume-filled, painted.
- **Marker radial position** — markers sit on a defined radius **inside** the chapter ring,
  never touching the crystal edge. (See `FRAMING_LAYOUT_v1.md` safe-area.)

### E. Hands (count EVERY hand — this is where the seconds hand disappears)
List each hand as its own clause with {style, length, color, tip, counterweight}:
- **Hour hand** — shorter, broad. Style: dauphine / baton / syringe / sword / breguet / skeleton.
- **Minute hand** — longer, reaches the minute track.
- **Central seconds hand** — thin, full-length, often with a colored tip and a tail
  (counterweight) past the center. **ALWAYS state it explicitly if present. It is the #1 dropped element.**
- **Sub-dial hands** — each active sub-dial has its own small hand(s). Count them.
- **Hand stack & pinion** — central hands share a polished central pinion (hub); name it so the
  renderer keeps a clean center instead of a smeared blob.
- **Lume** — which hands/markers glow; lume color (ice-blue / green / cream).

### F. Sub-dials / registers (the small inner dials)
For a chronograph, these are usually 2–3 recessed circles. Each one is a full mini-dial:
- **Count & position** — e.g. two sub-dials at 6 and 9, or three at 3/6/9.
- **Sub-dial texture** — **concentric guilloché / snailed (azurage) / circular-brushed.**
  Flat sub-dials read as cheap/AI. Name the texture explicitly (see materials).
- **Sub-dial function ring** — its own tiny numerals/ticks (e.g. 60/20/40 for a counter, 12-hour totalizer).
- **Sub-dial hand(s)** — see hands above.
- **Sub-dial framing** — polished metal ring around each sub-dial. The "sloppy cuts" defect
  is a sub-dial drawn without a clean circular frame — always specify the metal ring + crisp edge.
- **Sub-dial overlap** — note if a sub-dial overlaps the chapter ring or another module.

### G. Digital / module zones (hybrid faces)
- **LCD / OLED window** — shape (round / rectangular), bezel around it, glass reflection.
- **Segment style** — 7-segment / dot-matrix / crisp anti-aliased digits; color (amber / green / white).
- **Module contents** — time, date, weather glyphs, battery, steps. Name each glyph present.
- **Module integration** — recessed under its own metal ring, casting a soft inner shadow.

### H. Apertures & arcs (small but signature — frequently dropped)
- **Top arc / power-reserve arc** — the curved gauge near 12 o'clock. If present, name it
  ("curved power-reserve arc at 12 with a tapered needle"). This is the "τόξο" that went missing.
- **Date window** — rectangular/round aperture; framed; note position.
- **Day / month / moonphase aperture** — note shape and contents.
- **Open-heart aperture** — a cutout exposing the movement/balance wheel.

### I. Branding & text
- **Brand wordmark** — name, font weight, position (under 12).
- **Model / line text** — secondary line.
- **Sub-text** — "Automatic", "Chronometer", depth rating, etc. Keep legible, do not invent gibberish.

### J. Crystal & global optics
- **Crystal** — sapphire dome; note edge distortion at the rim.
- **AR coating reflection** — faint blue/violet sheen.
- **Global lighting** — single soft key light + environment reflections (see lighting file).

---

## Output contract (what the brain produces from this checklist)

For every reference, the brain emits a **Component Manifest** before writing prose:

```json
{
  "case":        {"shape":"round","finish":"brushed rose gold","bezel":"coin-edge fluted"},
  "crown":       {"pos":"3","style":"fluted cylinder"},
  "pushers":     2,
  "dial":        {"color":"matte black","texture":"flat with fine grain"},
  "chapter_ring":{"scales":["tachymeter 500-60 gilt","minute track"],"direction":"cw"},
  "markers":     {"type":"applied faceted baton","count":12,"finish":"polished gilt","radius":"on chapter ring inner edge"},
  "hands":       {"hour":"dauphine gilt","minute":"dauphine gilt","seconds":"thin central gilt with tail","pinion":"polished"},
  "subdials":    [{"pos":"9","texture":"concentric guilloché","ring":"polished gilt","hand":1,"scale":"60/20/40"},
                  {"pos":"6","texture":"snailed","ring":"polished gilt","hand":1,"scale":"12h totalizer"}],
  "modules":     [{"type":"round LCD","pos":"3-4","color":"amber 7-seg","contents":["time","weather glyph"]}],
  "apertures":   [{"type":"power-reserve arc","pos":"12"}],
  "text":        ["BRAND under 12","sub-line"],
  "optics":      {"crystal":"domed sapphire","ar":"faint blue"}
}
```

**The manifest is the contract.** The QC loop (`workflows/DESIGN_QC_LOOP_v1.md`) checks the
render against this manifest field-by-field. Anything in the manifest that is missing from
the render is a fail, not a stylistic preference.

---

## The Drop List (components that vanish most often — guard these explicitly)

1. **Central seconds hand** — always name it, with tip color + tail.
2. **Sub-dial textures** — concentric/snailed guilloché; never "flat".
3. **Top arc / power-reserve gauge** — small, curved, easy to omit.
4. **Applied marker facets & their radius** — markers must sit inside the chapter ring.
5. **Printed secondary scales** (tachymeter/telemeter) — the dense outer numerals.
6. **Sub-dial polished frame rings** — prevents "sloppy cuts".
7. **Central pinion / hand hub** — prevents a smeared center.
8. **Pusher count** — two pushers, not zero, not one.

Every one of these maps to a defect seen in production. Naming them is the fix.
