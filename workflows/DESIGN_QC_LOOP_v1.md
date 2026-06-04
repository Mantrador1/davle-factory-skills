# WORKFLOW: Design QC Loop (closed-loop, reference-compared)

> **Trigger.** Candidates exist from `REFERENCE_TO_PROMPT_v1.md` and must be checked before the
> operator ever sees them. This is the missing closed loop: the old pipeline rendered once and
> shipped defects straight to PENDING_OPERATOR_REVIEW.

> **Core idea.** Render → compare against the Component Manifest field-by-field → score →
> if fail, re-prompt with the *specific deltas* → re-render → repeat until pass or budget hit.
> The renderer is the design team; **this loop is the art director that rejects sloppy work.**

---

## The scorecard (score every candidate)

Score each axis 0–2 (0 = fail, 1 = weak, 2 = good). A candidate **passes** only if:
total ≥ 18/24 AND no single axis = 0 AND all Drop-List items = 2.

| # | Axis | 0 (fail) | 2 (good) |
|---|---|---|---|
| 1 | **Component coverage** | a manifest item is missing | every manifest item present |
| 2 | **Seconds hand** | absent | present, thin, with tail + tip |
| 3 | **Sub-dial texture** | flat/plastic | clear guilloché/snailed, framed ring |
| 4 | **Top arc / apertures** | missing | present and legible |
| 5 | **Marker framing** | markers off-edge / out of frame | all 12 inside R3, even 30° spacing |
| 6 | **Geometry cleanliness** | sloppy cuts, smeared center | crisp circles, clean pinion |
| 7 | **Finish contrast / realism** | uniform flat finish | stacked polished/brushed, real specular |
| 8 | **Text correctness** | gibberish/misspelled | exact, crisp, only intended text |
| 9 | **Composition** | tilted/cropped/off-center | centered, full, even margin |
| 10 | **Lighting** | flat or blown/crushed | single coherent key, AO in recesses |
| 11 | **Fidelity to reference** | generic, "averaged" | recognizably the reference's design |
| 12 | **No AI artifacts** | extra crowns/hands/warps | clean |

Record the scorecard as `qc/cand_<id>.md` with the numeric grid + a one-line note per failing axis.

---

## The loop

<step name="score_all">
Score each candidate on the 12 axes. Pick the highest total as the working candidate.
</step>

<step name="decide">
- **Pass** (≥18, no zeros, Drop-List all 2): promote to operator review. Stop.
- **Fail:** continue to re-prompt. Do NOT show the operator a failing candidate.
- **Budget:** max 4 re-prompt cycles per order. If still failing, escalate to operator with the
  scorecard and the best-so-far, stating exactly which axes won't converge and the suspected cause
  (e.g. "renderer cannot hold guilloché at this size → recommend gpt-image-1-high / upscale pass").
</step>

<step name="reprompt_with_deltas">
For each failing axis, append a **targeted corrective clause**, do not rewrite the whole prompt:
- coverage/seconds/arc fail → restate the missing item positively AND add its negative
  ("a thin central seconds hand WITH counterweight tail is REQUIRED; negative: missing seconds hand")
- texture fail → inject stronger guilloché phrasing from MATERIALS file
- marker-frame fail → re-pin radius ("markers at 76% radius, large gap to crystal") + Block 2 negative
- geometry fail → "perfectly circular concentric rings, single clean central pinion" + Block 4 negative
- text fail → reduce text / specify exactly / "no other text, correctly spelled"
Re-render (same model, new seed). Re-score. Increment cycle counter.
</step>

<step name="record">
Append each cycle's prompt-delta + new scorecard to `qc/`. The trail shows how the win was
reached — this is how the factory *learns* which deltas fix which renderer's weaknesses.
</step>

---

## Operator review handoff (Phase 2)

Only passing candidates are presented. Present 2–3 with their scores, e.g.:

```
Candidate A — 22/24. Strong guilloché, exact text. Minor: seconds tip a touch short.
Candidate B — 20/24. Cleaner composition, slightly flatter sub-dials.
```

Operator selects + requests changes → write `SELECTED.md` → if changes are dial-design changes,
re-enter REFERENCE_TO_PROMPT with the deltas; if approved as-is, hand to the app-build phase.

---

## Learning feedback (raise the tier over time)

When a delta reliably fixes a defect for a given renderer, promote it:
- recurring positive clause → add to the relevant `reference/` file
- recurring defect → add/strengthen a `NEGATIVE_PROMPTS_v1.md` block
- a fully-winning prompt for a style → save as a named preset/template

The factory's quality is a ratchet: every QC cycle either ships a pass or teaches the library
a new defense. That is how we climb to and hold tier 20.
