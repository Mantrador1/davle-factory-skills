---
name: davle-reference-edit-preservation
description: Preserve an existing DAVLE dial while making surgical image edits. Enforces locked-region prompts, minimal-delta generation, dependency-aware changes, and rejection of collateral redesign. Use whenever the user provides an existing dial and asks for limited changes.
---

# DAVLE Reference Edit Preservation

## Objective
Make the smallest visual delta necessary to satisfy the user's change request.

## Mandatory upstream
Run `davle-dial-structure-mapping` first.

## Edit contract
Before generation define:
- SOURCE: the exact input image to preserve,
- MUTABLE: only user-requested regions,
- LOCKED: everything else,
- DEPENDENT: minimum geometry that must change because of the edit.

## Minimal-delta principle
The target is not “same style.” The target is “same image except for named changes.”

Never:
- reinterpret the design language,
- improve unrelated typography,
- move complications,
- change textures,
- alter colors,
- add details,
- clean patina,
- change framing,
- change lighting,
- redraw icons,
unless requested.

## Prompt discipline
For image editing, use imperative clauses:
- “Edit the attached source image.”
- “Preserve all pixels/regions outside [mutable region] as closely as possible.”
- “Do not redesign or restyle the dial.”
- “Change only: …”
- “Keep identical: …”

Describe the mutable geometry precisely but do not re-describe the entire dial in a way that invites regeneration.

## Failure behavior
If the result changes any locked area materially:
- verdict = REJECT,
- do not rationalize the drift,
- regenerate from the original source image, not from the drifted result.

## Iteration rule
Always branch each correction from the last user-approved source, never from a failed derivative unless the user explicitly approves the derivative.

## Change budget
For surgical edits:
- expected changed area should be approximately limited to the mutable regions plus edge blending,
- any large global change is presumptive failure.

## Pixel-lock escalation
When exact preservation is required and image-processing tools are available, run `davle-surgical-compositing` after generation so locked regions are restored directly from the original source image rather than merely trusted to the generator.

## Output
Return:
- edit contract,
- mutable list,
- locked list,
- dependency list,
- exact minimal edit prompt,
- preservation verdict after generation.
