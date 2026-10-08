---
name: davle-horology-dial-engineering
description: Apply real horological display logic, hand geometry, retrograde and gauge mechanics, vintage-period design language, dial typography, and edit-preservation discipline to DAVLE watch-face concepts and corrections. Use whenever a DAVLE dial contains analog hands, pointer gauges, retrograde arcs, vintage/mechanical cues, or requires physically credible watchmaking-inspired geometry.
---

# DAVLE Horology Dial Engineering

## Objective
Prevent visually attractive but mechanically incoherent watch-face designs. Translate watchmaking and analog-instrument principles into implementation-ready dial geometry before prompt generation or image editing.

Read:
- `references/horology-geometry.md`
- `references/vintage-1960s-instrument-language.md`

## Trigger conditions
Run this skill when any request includes one or more of:
- hour/minute/seconds hands,
- skeleton, dauphine, syringe, baton, sword, alpha, leaf or pointer hands,
- analog battery/power/goal/health gauges,
- retrograde or partial-arc scales,
- vintage, 1950s, 1960s, tool-watch, chronograph, dashboard or instrument styling,
- requests to resize, shorten, lengthen, hollow or restyle hands,
- corrections where the user says a hand, pointer, scale or gauge “does not make sense”.

## Core geometry rules

### 1. A moving hand has one fixed pivot
A watch or gauge hand is a rigid straight indicator rotating about one fixed axis. Do not draw a moving hand as a curved element that follows an arc.

### 2. A pointer scale must be centered on its pivot
For a rotating pointer over a partial scale, the scale arc is concentric with the pivot. The pointer sweeps radially from the pivot, and its tip meets the scale approximately perpendicular to the tangent of the arc.

If an existing arc is not concentric with the intended pivot, change the pivot, change the arc, or use a non-pointer fill/progress treatment. Do not fake the relationship.

### 3. Retrograde logic
A retrograde indication uses a straight hand that sweeps across a limited arc around a fixed pivot and returns to zero at the end of its cycle. The moving element is the hand, not a curved hand-shaped decoration.

### 4. Hand-length hierarchy
- hour hand: shortest; reaches the hour-marker field,
- minute hand: longer; tip reaches the minute track or just inside it,
- central seconds/chronograph-style hand: usually longest and thinnest; tip reaches the seconds/minute track.
Do not let a minute hand terminate far short of its track unless intentionally stylized. Do not let it visually collide with or enter the bezel.

### 5. Hand distinction
Hour and minute hands must be distinguishable by length and/or mass. Seconds and auxiliary pointers should be visually lighter than the primary handset unless the function intentionally needs emphasis.

### 6. Skeleton/openworked hands
Skeleton hands use an open central body bounded by a metal frame. If the user requests an empty interior, keep the aperture genuinely open: no white/lume fill, no dark filler, no decorative panel inside it. The frame alone carries the silhouette.

### 7. Alignment and clearance
- hands share the intended center/pivot,
- hands remain parallel to the dial plane,
- visual stacking is coherent,
- no accidental touching/collision,
- tips line up with the track they indicate,
- center cap/hub should look structurally capable of carrying the hands.

## Gauge and arc logic

### Moving-pointer gauge
Use when direction/trend/position matters.
Required:
- fixed pivot,
- straight pointer,
- concentric scale arc,
- clearly identifiable tip,
- start/end values in a logical direction,
- color thresholds anchored to scale zones.

### Fill-only gauge
Use when a progress percentage is the main message and no mechanical pointer is required.
Required:
- background track,
- active fill from the defined zero end,
- explicit low/high warning zones only where meaningful,
- no decorative pointer that implies a mechanical reading.

### Hybrid pointer + color zones
Allowed only when both pointer position and thresholds add distinct information. The pointer remains the primary reading device; color bands are secondary.

## Color-zone discipline
Color must encode state, not decorate randomly.
Examples:
- red at low battery or danger,
- green near goal completion,
- neutral/cream/white for normal range.
If the user defines a custom orientation, map 0 and 100 explicitly before generation.

## Vintage 1950s–1960s design grammar
Use period cues as a coherent system, not as generic “old-looking” distress:
- matte or lightly brushed metal, painted lacquer, cream/ivory print, black instrument fields,
- restrained polished/chromed or gilt metal,
- one purposeful accent such as red for central seconds or warning pointer,
- printed scales with crisp hierarchy,
- recessed registers or stepped dial zones for depth,
- compact, legible, condensed or monoline typography inspired by technical/draftsman printing,
- restrained patina; wear is optional and should never substitute for period accuracy,
- avoid neon, holographic materials, sci-fi paneling and exaggerated cyberpunk geometry unless explicitly requested.

## Typography rules
- one coherent type family or tightly related family,
- strong numeral legibility at watch scale,
- labels smaller than values,
- condensed forms where horizontal space is constrained,
- preserve open counters and adequate spacing,
- vintage styling must not make critical numbers ambiguous.

## Dial hierarchy
A dial must remain legible at a glance:
1. primary time,
2. primary instrument/gauge readings,
3. secondary data,
4. decorative texture/material cues.

Mechanical-looking components must have an apparent functional reason. Do not add bezels, screws, arcs, scales or needles that imply functions they do not serve.

## Edit-preservation mode
When the user asks to change only specific elements:
1. List the exact mutable regions internally.
2. Treat all unlisted regions as locked.
3. Modify only the named hands/gauges/text/icons/material zones.
4. Preserve framing, typography, textures, colors, layout and all other elements unless the requested correction requires a geometric dependency.
5. If a dependency forces another change, state it before generation.

## Pre-generation horology gate
Before writing an image prompt, verify:
- every hand has a plausible pivot,
- every pointer scale is concentric with its pivot,
- minute/hour/seconds lengths match their tracks,
- skeleton apertures are truly open when requested,
- no pointer is curved to “follow” a scale,
- scale direction and zero/full positions are explicit,
- color zones have meaning,
- 1960s/vintage cues are period-coherent,
- no unrequested redesign is introduced.

## QA hard failures
Return REVISE if any of these occur:
- pointer arc and pivot are geometrically incompatible,
- curved moving pointer used for a rotating gauge,
- minute hand touches or visually enters the bezel,
- skeleton hand contains unintended fill,
- scale labels cannot be mapped to pointer movement,
- pointer obscures its own reading point,
- accidental hand collision or implausible center hub,
- “vintage” result becomes sci-fi/cyberpunk without request,
- edit changes locked areas.

## Sources and evidence basis
Authoritative/reference sources used to build this skill include:
- Fondation Haute Horlogerie encyclopedia: dial, hand, display, retrograde, power reserve.
- American Watchmakers-Clockmakers Institute material on hands/dials and CW21 hand alignment.
- Horological Society of New York educational material and recommended watchmaking references.
- NASA/DOT human-factors guidance on analog moving-pointer displays.
- TAG Heuer historical archives on 1960s Carrera/Autavia instrument legibility.
- Period dial-typography research and watch-design references.

## Output
For a horology-sensitive task provide downstream:
- geometry verdict,
- hand/pointer specification,
- scale/pivot specification,
- period-style constraints,
- locked vs mutable edit regions,
- exact corrective prompt clauses,
- QA checks that must pass.
