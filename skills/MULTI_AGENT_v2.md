---
name: MULTI_AGENT
description: Orchestration of the DAVLE render pipeline across the design brain (prompt author), the renderer (image model), and the QC art-director loop. Use for any watch-face generation or REMAKE request.
version: 2
supersedes: MULTI_AGENT_v1.md
---

# Multi-Agent Coordination v2 (design-brain → renderer → QC)

> v1 described a one-shot text-to-image handoff and was the structural reason fidelity was
> lost: the prompt author never enumerated the reference, and nothing checked the result.
> v2 wires in the render-brain IP and the closed-loop QC art-director.

## Agent roles
- **Claude Code** — orchestrator: runs the workflows, manages evidence/state, deploys, builds.
- **Design brain** (ChatGPT/OpenAI on server, or Claude here) — authors the Component Manifest
  and the render prompt. **MUST be primed with the render-brain IP** (see Priming below).
- **Renderer** (Ideogram on server; gemini-3-pro-image-hd / gpt-image-1-high / flux-2-pro here)
  — generates candidate images.
- **QC art-director** — scores candidates vs the manifest, re-prompts on failure, gates output.

## Priming the design brain (THIS is the wiring that was missing)
Before the design brain writes anything, concatenate into its system/context:
1. `reference/WATCH_ANATOMY_v1.md`
2. `reference/MATERIALS_FINISHES_LIGHTING_v1.md`
3. `reference/FRAMING_LAYOUT_v1.md`
4. `reference/NEGATIVE_PROMPTS_v1.md`
5. `templates/RENDER_PROMPT_TEMPLATE_v1.md`
On the server this is done by `brain_bridge` (see `deploy/INTEGRATION.md`). A brain that is not
primed with these files reproduces the old failures.

## Handoff pattern (v2)
1. Operator → Claude: reference image + brief (or "REMAKE with <delta>").
2. Claude → `workflows/REFERENCE_TO_PROMPT_v1.md`: enumerate → Component Manifest.
3. Design brain (primed) → fills `templates/RENDER_PROMPT_TEMPLATE` → prompt.txt + negative.txt + model.txt.
4. Renderer → 3–4 candidates (vary seed). Use image-conditioning if the model supports it.
5. Claude → `workflows/DESIGN_QC_LOOP_v1.md`: score 12 axes / 24; re-prompt failing deltas; ≤4 cycles.
6. **Only passing candidates** → operator (Phase 2 selection + change requests).
7. On approval → Phase 3 app build reads the approved image + manifest + prompt as source of truth.

## Doctrine selection (per order)
Claude sets `Doctrine: DAVLE-LUX | DAVLE-COCKPIT` in PLAN.md. LUX uses full materials/lighting;
COCKPIT uses MARKET_INTEL flat-neon rules. The two never mix on one order.

## Shared evidence (versioned — see PLANNING_WITH_FILES + REFERENCE_TO_PROMPT)
```
orders/<ORDER>_v<N>/
  reference/ manifest.json prompt.txt negative.txt model.txt
  candidates/ qc/ SELECTED.md PLAN.md STATE.md
```

## Error handling
- Renderer timeout 5 min; retry 3× exponential backoff.
- QC budget 4 cycles; on non-convergence escalate to operator with scorecard + best-so-far + cause.
- Fallback: previous passing version in the order's prior `_v<N-1>`.
