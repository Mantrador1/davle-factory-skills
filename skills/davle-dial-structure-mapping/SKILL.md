---
name: davle-dial-structure-mapping
description: Decompose a source or candidate DAVLE watch-face image into stable semantic regions, spatial relationships, normalized coordinates, and dependency links before editing or factory handoff. Use whenever an existing dial must be modified without unintended redesign or when exact layout preservation matters.
---

# DAVLE Dial Structure Mapping

## Objective
Turn a visual dial into an explicit semantic map before any edit. Prevent the model from treating the whole image as free-form redesign space.

## Required output
Create an internal map with:
- canvas and dial bounds,
- center point,
- outer bezel / minute-track bounds,
- primary time region,
- hour/minute/seconds hands and pivot,
- every subdial/gauge,
- every data cell,
- logo/brand region,
- icons/buttons,
- moon/weather imagery,
- decorative plates/screws/bridges,
- typography blocks,
- mutable regions,
- locked regions,
- dependencies.

Use normalized coordinates 0.0–1.0 whenever possible.

## Region classes
- LOCKED: must remain visually unchanged.
- MUTABLE: explicitly requested for change.
- DEPENDENT: may move only if required by a named geometric dependency.
- REGENERATABLE: can be redrawn because the user explicitly allows redesign.

Default is LOCKED.

## Relationship map
Record:
- alignment,
- symmetry,
- overlap,
- z-order,
- shared pivot,
- concentricity,
- tangency,
- equal sizing,
- spacing,
- color/material continuity.

## Edit rule
If user says “change only X” or “do not touch anything else”:
1. map all regions,
2. mark X as MUTABLE,
3. mark every other region LOCKED,
4. identify true DEPENDENT geometry,
5. reject any prompt that describes the entire dial as if redesign were allowed.

## Handoff
Return a compact structure packet:
- locked regions,
- mutable regions,
- dependent regions,
- geometric anchors,
- do-not-change list,
- exact edit scope.
