# Horology Geometry Reference

## Fixed-pivot principle
A conventional watch or gauge hand rotates about a fixed arbor. Therefore its path is angular, not translational, and the reading scale for that hand must be arranged around the same center.

For a partial-arc indicator:
- define pivot P,
- define scale radius R,
- all tick marks lie on an arc centered on P,
- pointer is a straight segment from P toward the active tick,
- pointer tip radius should terminate at or just inside the tick ring,
- pointer is radial; the local arc tangent is perpendicular to the pointer.

This is the key correction for DAVLE retrograde/goal/battery pointer concepts.

## Retrograde
A retrograde display uses a hand sweeping over a limited scale and then returning to zero. It still obeys fixed-pivot radial geometry.

## Primary handset proportions
Use relative targets rather than absolute pixels:
- hour hand tip: usually within the hour-marker field,
- minute hand tip: at the minute track or slightly inside,
- seconds hand tip: at the seconds/minute track.
In information-dense smartwatch concepts, openworked/skeleton hands are useful because they preserve visibility of underlying information.

## Skeleton hand construction
A believable skeleton hand has:
- metal perimeter/frame,
- open void through the body,
- structurally plausible neck near the hub,
- pointed or defined reading tip,
- no arbitrary solid insert unless intentionally lumed.

For 1960s-style tool-watch language, prefer restrained tapered/open baton, alpha, or lightly pointed forms over futuristic blades.

## Hand stack
From dial upward, conceptually:
1. hour,
2. minute,
3. seconds / auxiliary.
Keep visual clearance between layers and a coherent center cap.

## Analog gauge mapping
Before rendering, explicitly map:
- zero angle,
- full-scale angle,
- direction of increase,
- pointer value,
- threshold color zones.

Example:
GOAL 0→100 over 130° clockwise:
- red warning/starting block near 0,
- neutral cream/white intermediate blocks,
- two green blocks at the 100 end,
- one straight red pointer on the same pivot as the scale arc.

## Human-factors rules
- a moving pointer over a fixed scale is excellent for at-a-glance qualitative state,
- pointer tip must be unambiguous,
- pointer should not obscure the scale value being read,
- combine analog state with digital precision only when both add value.

## Source notes
- FHH: Hand, Dial, Display, Retrograde encyclopedia entries.
- AWCI: hand/dial matching; CW21 alignment and division guidance.
- NASA/DOT human-factors: moving-pointer/fixed-scale display guidance.
