---
name: davle-watch-hand-engineering
description: Engineer physically credible watch hands and analog pointer gauges for DAVLE dials, including hour/minute/seconds hierarchy, hand length and mass, skeleton/openworked construction, 1950s–1960s hand language, pivot placement, pointer-to-arc geometry, clearance, and edit-preservation. Use whenever a DAVLE task creates, edits, resizes, styles, or validates watch hands or gauge pointers.
---

# DAVLE Watch Hand Engineering

## Objective
Make every hand and analog pointer mechanically plausible, visually legible, period-coherent, and correctly related to the track or scale it reads.

This skill is narrower and stricter than the general horology skill. When hands or pointers are a critical part of the request, apply this skill before prompt engineering and again during QA.

Read:
- `references/hand-geometry.md`
- `references/1960s-hand-language.md`

## Non-negotiable hierarchy

### Central time hands
For a conventional central handset:
- the hour hand is shorter than the minute hand,
- the minute hand is longer and reaches the minute track or terminates just inside it,
- the seconds hand is normally the thinnest and may be the longest,
- the hour hand must NEVER visually project farther from the center than the minute hand,
- the hour hand must not sit “above” the minute hand in a way that makes it appear longer or dominant by reach.

If image generation produces a longer hour hand than minute hand, this is a HARD FAIL.

### Recommended proportional envelope
Measure from center pivot to tip using dial radius R:
- hour hand: approximately 0.52R–0.67R,
- minute hand: approximately 0.78R–0.91R,
- seconds hand: approximately 0.86R–0.96R when present.

These are design targets, not universal laws. The visual rule is mandatory: hour < minute, and the minute tip must read the minute track without touching the bezel.

## DAVLE minute-hand proportion rule

When the user does not specify a different minute-hand length, compute the minute-hand tip radius from the hour-hand tip radius and the usable inner-bezel radius:

`L_minute = L_hour + 0.5 × (R_inner_bezel - L_hour)`

Equivalent interpretation: the minute-hand tip sits exactly halfway between the hour-hand tip and the inner edge of the outer bezel.

This DAVLE rule overrides the broader generic proportional envelope for edit tasks unless the user explicitly requests another length. The minute hand must still remain visibly longer than the hour hand, simple in silhouette, and must not touch the bezel.

## Hand architecture

### Hour hand
- shorter,
- heavier/wider or more visually massive,
- clear tip,
- must point to hour-marker zone.

### Minute hand
- longer,
- usually slightly slimmer than the hour hand,
- tip aligned to minute track,
- may pass over complications and information if the concept requires it; do not shorten it merely to avoid overlapping data.

### Seconds hand
- thin, light, high-contrast,
- long enough to read the seconds/minute perimeter,
- counterweight optional.

## Skeleton/openworked hands
A skeleton hand is an OPEN METAL FRAME:
- perimeter rails define the hand,
- interior is an actual void revealing the dial underneath,
- no white, black, lume, cream, paint, translucent filler or decorative panel inside the open channel unless explicitly requested,
- frame must remain structurally plausible at the neck and tip,
- minute hand should keep an elongated open aperture; hour hand may use a wider, shorter aperture.

For a 1960s-inspired dense instrument dial, prefer narrow openworked baton/alpha/syringe hybrids with restrained taper, not futuristic blades.

## Center stack and layering
- hour and minute hands share the same central axis,
- both lie parallel to the dial,
- visual spacing between stacked hands must be even,
- hands must not touch each other, the dial, or an implied crystal,
- center hub/cannon pinion should appear capable of carrying the stack,
- the apparent z-order must not invert the length hierarchy.

## Pointer gauges and arc instruments

### Fixed pivot rule
A conventional gauge pointer is one rigid STRAIGHT needle rotating around one fixed pivot.

### Arc-center rule
The scale arc must be concentric with the pointer pivot:
- choose pivot P,
- choose radius r from P to the reading track,
- all scale ticks lie on the same circular arc centered on P,
- pointer centerline is radial from P,
- pointer tip crosses the scale approximately perpendicular to the tangent at the reading point.

A pointer cannot “follow” an arc by bending. A pivot placed too close to the arc will produce shallow tangency and is mechanically/visually wrong.

### How to fix a pointer that is too tangent to the arc
1. Move the pivot farther inward/away from the scale.
2. Increase pointer length accordingly.
3. Keep the pointer straight.
4. Re-center the scale arc on the new pivot if needed.
5. If the pivot must be visually hidden, place its root under an overlapping dial plate or bridge while preserving a believable concealed axis.

### Hidden-pivot rule
It is acceptable for the pointer root/pivot to disappear beneath a metal plate when the visible geometry implies a plausible concealed arbor. The visible needle must emerge from that region as a straight radial pointer.

### GOAL/retrograde use
For a 0–100 partial GOAL scale:
- one fixed pivot,
- one straight vintage red pointer,
- pointer length sufficient to reach all ticks,
- red low zone at the 0 end,
- neutral/ivory active field through the scale,
- green completion blocks at the 100 end,
- pointer sweeps from 0 to 100 while staying radial at every reading.

## 1960s hand vocabulary
Use mid-century instrument-watch language:
- matchstick,
- baton,
- syringe,
- alpha,
- dauphine,
- sword,
- restrained openworked/skeleton derivatives.

For DAVLE vintage instrument faces:
- aged steel, nickel, rhodium or warm metal frames,
- blackened or cream dial below,
- restrained red seconds/auxiliary pointer,
- little or no lume when the user asks for open skeleton hands,
- crisp mechanical geometry and modest taper.

Avoid:
- cyberpunk blade shapes,
- oversized sci-fi cutouts,
- fantasy spear points,
- random asymmetrical holes,
- broad white inserts when an open skeleton interior is required.

## Edit-preservation mode
When correcting hands/pointers in an existing dial:
- lock every non-hand/non-pointer pixel conceptually,
- do not move complications, labels, icons, colors, textures, screws, brand marks, scales, moon phase, bezels or typography unless mechanically required,
- preserve the existing hand angles unless the user asks for time correction,
- only adjust length, silhouette, openwork, pivot, pointer scale relationship or other named properties.

## Pre-generation hand gate
Verify all before generation:
- hour hand visibly shorter than minute hand,
- minute hand reaches minute-track region without bezel collision,
- skeleton interiors truly empty,
- seconds hand remains the lightest,
- each gauge pointer has one fixed pivot,
- pointer and scale share the same center,
- pointer crosses the scale radially,
- any hidden pivot is mechanically plausible,
- no unrelated dial element is changed.

## QA hard failures
REVISE immediately if:
- hour hand is equal to or longer than minute hand,
- minute hand is obviously too short to read its track,
- minute hand touches/enters the bezel,
- skeleton aperture contains fill,
- hand frames are malformed/asymmetric without design intent,
- gauge pointer is curved,
- pointer pivot is so close to the arc that the needle runs tangent to the scale,
- pointer cannot geometrically sweep the full scale,
- pivot/scale centers do not match,
- correction changes locked unrelated elements.

## Evidence basis
- Fondation Haute Horlogerie: hand as a lightweight moving metal indicator over a dial/scale; standard hand forms include baton, dauphine, feuille, sword, Breguet and skeleton.
- American Watchmakers-Clockmakers Institute: minute hand alignment to the 12 marker when the hour hand is centered; all hands parallel with even spacing and no contact.
- TAG Heuer historical Carrera material: 1960s emphasis on legibility, clean scale placement and restrained applied hands/markers.
- General analog-instrument geometry: a rotating pointer reads a concentric scale radially from a fixed center.

## Output
Return:
- hand family/style,
- hour-hand length/mass,
- minute-hand length/mass,
- seconds-hand treatment,
- skeleton/openwork specification,
- center-stack specification,
- gauge pointer pivot and scale-center specification,
- locked elements,
- hard QA checks.
