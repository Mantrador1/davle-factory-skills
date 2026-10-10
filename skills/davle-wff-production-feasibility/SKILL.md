---
name: davle-wff-production-feasibility
description: Check whether a DAVLE visual concept is practical for modern Wear OS Watch Face Format production, including complications, AOD, animations, memory, customization, data sources, and battery constraints. Use before factory handoff or whenever a visual concept adds dynamic smartwatch behavior.
---

# DAVLE WFF Production Feasibility

## Objective
Keep visual concepts buildable, performant, and compatible with modern Wear OS Watch Face Format.

## Authoritative basis
Prefer current official Google/Android WFF documentation, XSD/specification, validator, memory evaluator, optimizer, and Wear OS samples.

## Checkpoints

### Data/complications
- distinguish fixed built-in data from editable complication slots,
- avoid hardcoded labels that become wrong when a complication is reassigned,
- confirm the desired provider/data type exists,
- keep complication count and layout practical.

### AOD
- define a distinct ambient/AOD state,
- reduce lit pixels and motion,
- remove seconds/animation unless explicitly supported and justified,
- preserve primary time legibility,
- consider burn-in protection.

### Animation
- prefer short event-triggered loops or static fallback over continuous video,
- require a static thumbnail/fallback,
- keep frame count, dimensions and memory under control,
- avoid animation where a simple expression/transform can do the same work.

### Memory/performance
- treat large bitmaps, many frames, duplicated assets and unnecessary high-resolution layers as risks,
- use official WFF validation/memory tooling in the factory pipeline where possible.

### Customization
- plan color themes, complication slots and shortcuts as structured options rather than baking every variation into unique raster assets.

## Visual-to-factory handoff
For every dynamic element specify:
- visual appearance,
- data source,
- update behavior,
- active/AOD behavior,
- fallback state,
- interaction/shortcut if any.

## Verdicts
- BUILDABLE
- BUILDABLE_WITH_CHANGES
- NOT_RECOMMENDED

Never approve a beautiful concept that requires unsupported or battery-hostile behavior without flagging it.
