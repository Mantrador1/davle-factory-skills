# WORKFLOW: Reference → Prompt

> **Trigger.** The operator supplies a reference watch image (a photo to turn into a watch face),
> or asks for a new design "like" a reference. This is an **image-conditioned** task, not a
> blind text-to-image task — the previous pipeline treated it as the latter, which is why
> fidelity was lost.

> Produces the four-file unit from `templates/RENDER_PROMPT_TEMPLATE_v1.md`.

---

## Why this workflow exists

The old flow was: feedback → ChatGPT writes a short spec → Ideogram renders → done. The spec
never enumerated the reference exhaustively, so the renderer "averaged" toward a generic watch
and dropped the seconds hand, the textures, the arc. This workflow makes enumeration mechanical
and adds image conditioning where available.

---

## Process

<step name="ingest_reference">
Load the reference image. If multiple references, pick the primary and note which attributes
come from each. Record provenance in the evidence bundle.
</step>

<step name="enumerate_manifest">
Walk `reference/WATCH_ANATOMY_v1.md` Enumeration Checklist top-to-bottom. For EVERY row,
mark PRESENT/ABSENT and capture attributes. Produce `manifest.json`.
**Gate:** the manifest must explicitly account for all items in the Drop List (seconds hand,
sub-dial textures, top arc, marker radius, secondary scales, sub-dial frames, pinion, pushers).
Do not proceed with any Drop-List item left as "unknown".
</step>

<step name="assign_finishes">
For each PRESENT component, attach material/finish phrases from
`MATERIALS_FINISHES_LIGHTING_v1.md`. No component may be left finish-less (finish-less = flat).
Stack contrasting finishes deliberately.
</step>

<step name="assign_bands">
Assign every component a radial band from `FRAMING_LAYOUT_v1.md`. Set hand-tip radii.
Verify no functional element exceeds R≈0.90.
</step>

<step name="select_renderer">
Choose the model (see template's per-model hints). Default luxury → gemini-3-pro-image-hd or
gpt-image-1-high. Record choice + rationale in `model.txt`.
</step>

<step name="image_conditioning">
If the chosen renderer supports reference/image input or img2img, supply the reference image as
a conditioning input alongside the text prompt (strength tuned so layout/finishes transfer but
DAVLE branding/template overrides apply). If it does NOT (pure text-to-image), compensate by
making the enumerated prompt maximally explicit — the manifest already guarantees coverage.
State which path was used in `model.txt`.
</step>

<step name="assemble_prompt">
Fill `templates/RENDER_PROMPT_TEMPLATE_v1.md` sections 1–11 from the manifest+finishes+bands.
Assemble the negative from `NEGATIVE_PROMPTS_v1.md` (fidelity-first order). Emit `prompt.txt`
and `negative.txt`.
</step>

<step name="render_candidates">
Generate 3–4 candidates (vary seed, not prompt) so the QC loop has choices. Save all.
</step>

<step name="handoff_to_qc">
Pass candidates + manifest to `workflows/DESIGN_QC_LOOP_v1.md`. Do NOT present to the operator
before QC. Only QC-passing candidates reach the operator's Phase-2 selection.
</step>

---

## Evidence bundle (per order, versioned)

```
orders/<ORDER_NAME>_v<N>/
  reference/        # input image(s) + provenance
  manifest.json     # the Component Manifest
  prompt.txt        # positive
  negative.txt      # negative
  model.txt         # renderer, params, conditioning path
  candidates/       # rendered images
  qc/               # QC scorecards (see QC workflow)
  SELECTED.md       # operator's choice + change requests (Phase 2)
```

This directory is the reproducible unit. Commit it. A winning prompt becomes a reusable
preset; recurring presets graduate into named templates in `templates/`.
