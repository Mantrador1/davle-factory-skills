---
name: davle-market-to-dial-orchestrator
description: Orchestrate the complete DAVLE market-to-dial workflow from fresh market research through trend analysis, pattern extraction, commercial synthesis, image prompt creation, dial generation, and visual QA. Use when the user asks DAVLE to discover what is selling and produce the strongest dial-only concept end to end.
---

# DAVLE Market-to-Dial Orchestrator

## Objective
Run the full modular workflow while keeping each specialist skill responsible for its own decision layer.

## Sequence
1. Run `davle-watchface-market-research`.
2. Pass its evidence-backed handoff to `davle-watchface-trend-analysis`.
3. Pass trend findings to `davle-watchface-pattern-extraction`.
4. Pass the pattern matrix to `davle-commercial-dial-synthesis`.
5. Pass the approved concept to `davle-dial-prompt-engineering`.
6. Generate the dial image using the available image-generation capability.
7. Run `davle-dial-visual-qa` on the generated image.
8. If QA returns REVISE and a concrete correction is feasible, regenerate once using the correction instructions and re-run QA.

## Rules
- Do not skip fresh research when the task depends on what is selling now.
- Do not let downstream skills overwrite upstream evidence silently.
- Keep observed facts, inference, and creative synthesis distinct.
- Produce only dial-only imagery unless the user explicitly requests otherwise.
- Optimize for a commercially coherent original concept, not a collage of competitor features.

## Final response
Provide:
- concise market findings,
- key patterns,
- chosen commercial thesis,
- exact generation prompt,
- generated dial image,
- QA verdict,
- task progress.

Avoid exposing unnecessary internal orchestration details unless requested.