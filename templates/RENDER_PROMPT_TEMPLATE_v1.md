# RENDER PROMPT TEMPLATE — Assembly Spec

> **Purpose.** The single, structured artifact the design brain fills to produce a render
> prompt. It forces every component, finish, and framing rule to be named, so nothing is
> dropped. This is the artifact that was previously invisible (it lived only in transient
> `render_prompt.txt` on the server). It is now versioned IP.

> Inputs it consumes: the **Component Manifest** (from `reference/WATCH_ANATOMY_v1.md`),
> phrases from `MATERIALS_FINISHES_LIGHTING_v1.md`, bands from `FRAMING_LAYOUT_v1.md`,
> blocks from `NEGATIVE_PROMPTS_v1.md`.

---

## Structure of a render prompt (ordered — order matters to most models)

1. **Subject + medium** (1 line) — what it is, shot how.
2. **Case & bezel** — material, finish, bezel texture, crown, pushers.
3. **Dial base** — color, finish/texture.
4. **Chapter ring & scales** — every printed/engraved ring, with color.
5. **Hour markers** — type, count, finish, radius.
6. **Hands** — EACH hand listed (hour, minute, central seconds + tail, sub-dial hands), pinion.
7. **Sub-dials / modules / apertures** — each with texture, frame ring, contents, position.
8. **Branding & text** — exact, minimal.
9. **Composition** — the framing block from `FRAMING_LAYOUT_v1.md`.
10. **Lighting & optics** — the single-key studio block.
11. **Quality boosters** — macro/PBR tail.
12. **Negative prompt** — assembled blocks (separate field if the model supports it).

---

## Fill-in template (luxury photoreal)

```
[1] Ultra-detailed macro product photograph of a luxury <case_shape> chronograph watch face,
straight-on top-down view.

[2] CASE: <metal+finish> case with polished bevels; <bezel_texture> bezel; <crown_style>
crown at 3 o'clock; <N> chronograph pushers flanking the crown.

[3] DIAL: <dial_color> dial, <dial_finish/texture>.

[4] SCALES: <scale_1 e.g. gilt tachymeter 500→60> and a fine minute/seconds track on the
chapter ring (<direction>); <scale_2 if any> in <color>.

[5] MARKERS: exactly twelve <marker_type> hour markers, <marker_finish>, applied with
diamond-cut facets, centered at ~76% of the dial radius with a clear gap to the crystal,
evenly spaced at 30° intervals.

[6] HANDS: <hour_style> hour hand (tip ~58% radius); <minute_style> minute hand reaching the
minute track (~85%, not touching the crystal); a thin central seconds hand with a
counterweight tail and a <accent> lacquered tip (~88%); all pivoting from a single clean
polished central pinion. <sub-dial hands enumerated>.

[7] SUB-DIALS/MODULES: <subdial_1: position, concentric guilloché/snailed texture, polished
frame ring, soft inner shadow, its scale/numerals, its hand>; <subdial_2 ...>;
<module: recessed round LCD under polished ring, amber 7-seg digits, faint glass reflection,
contents>; <aperture/arc: curved power-reserve arc at 12 with a tapered needle>.

[8] TEXT: "<BRAND>" under 12 in <weight>; "<sub-line>" — crisp, correctly spelled, no other text.

[9] COMPOSITION: perfectly centered, fully visible, zero tilt, even ~7% margin, watch ~85% of
frame; every element on true concentric circles. (full block from FRAMING_LAYOUT_v1.md)

[10] LIGHT/OPTICS: single large soft key light upper-left, dark studio reflections in the
polished metal, ambient occlusion in all recesses; domed sapphire crystal with faint
anti-reflective blue sheen and slight rim refraction.

[11] QUALITY: macro product photography, physically based rendering, tack-sharp focus on the
dial, high microcontrast, 8k surface detail, no motion blur.

NEGATIVE: <Blocks 1,2,3,4,5,6 from NEGATIVE_PROMPTS_v1.md, fidelity-first order>
```

---

## Fill-in template (neon-minimal — separate doctrine)

```
[1] Clean flat vector-style Wear OS watch face, top-down, high contrast on pure black.
[2/3] No case; full-bleed circular dial, pure #000000 background.
[5] Twelve minimal tick/baton markers in <accent neon>, centered at ~80% radius.
[6] One bold oversized time display (digital HH:MM occupying ~35–45% of screen) OR
two crisp flat hands; thin accent seconds optional.
[7] ≤ 3 complication zones, flat, single accent color, no texture.
[9] Perfectly centered, all elements fully inside the circle, even margin.
[11] crisp anti-aliased vector, flat design, maximum legibility, sunlight-readable.
NEGATIVE: <Blocks 1,2,4,5 — skip texture/lighting; flat is intended>
```

---

## Rendering hints per model (this environment)

When the renderer is selected by the brain, tune the assembly:

- **gemini-3-pro-image-hd / gpt-image-1-high** — strong at coherent photoreal product shots
  and at *following long enumerated instructions*. No separate negative field → fold negatives
  as positive constraints ("with all twelve markers fully inside the dial, a visible central
  seconds hand, ..."). Best default for luxury hero.
- **flux-2-pro / imagen-4-ultra** — excellent material/lighting realism; keep the prompt dense
  on finishes; respond well to the macro/PBR tail.
- **ideogram-v3-quality** — best when dial text must be exact; weaker on guilloché micro-texture
  → lean harder on the finish vocabulary and accept a QC pass for texture.

Record which model + exact prompt produced each candidate in the evidence bundle
(see `workflows/DESIGN_QC_LOOP_v1.md`), so winners are reproducible.

---

## Output contract

The brain emits, per order:
- `manifest.json` (the Component Manifest)
- `prompt.txt` (the filled positive prompt)
- `negative.txt` (assembled negative blocks)
- `model.txt` (chosen renderer + params)

These four files + the resulting image are the reviewable, versioned unit of work.
