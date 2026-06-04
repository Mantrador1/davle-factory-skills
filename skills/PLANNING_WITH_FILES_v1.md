# PLANNING WITH FILES — Durable Task State

> This file previously contained only "404: Not Found" while SSOT_KEEPER listed it as an
> integration — a broken dependency. It is now defined.

## Purpose
The factory runs in ephemeral contexts. Plans, decisions, and progress must live in files,
not in a session's memory, so any fresh context (or a different agent) can resume exactly.

## Core rule
Every order has a directory; the directory IS the plan. No task state lives only in chat.

## Order directory (mirrors REFERENCE_TO_PROMPT evidence bundle)
```
orders/<ORDER_NAME>_v<N>/
  PLAN.md          # objective, chosen doctrine (LUX/COCKPIT), constraints, 2–3 tasks
  STATE.md         # living status: current step, last action, next action, blockers
  manifest.json    # Component Manifest
  prompt.txt / negative.txt / model.txt
  candidates/  qc/  SELECTED.md
```

## PLAN.md shape
```
# ORDER <name> v<N>
Doctrine: DAVLE-LUX | DAVLE-COCKPIT
Reference: <path or "brief">
Objective: <one line>
Constraints: <size, must-have complications, text>
Tasks:
  1. <task>  — done-when: <measurable>
  2. <task>  — done-when: <measurable>
```

## STATE.md shape (update after every step)
```
Step: <enumerate|finish|band|render|qc|review>
Last: <what just happened + result>
Next: <single next action>
Blockers: <none | description>
QC: <best score so far / cycles used>
```

## Rules
- Update STATE.md after every step; it is the resume point.
- Keep PLAN.md to 2–3 tasks (context-size discipline).
- One commit per meaningful step; the order dir is the audit trail.
- On resume, read STATE.md first, then continue from `Next`.

## Integrations
- SSOT_KEEPER: order dirs are the evidence trail.
- LYSIEN_HERO_ART v2: PLAN.md records the chosen doctrine + manifest.
- DESIGN_QC_LOOP: QC scorecards live in `qc/`, summarized in STATE.md.
