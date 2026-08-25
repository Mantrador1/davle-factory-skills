# DAVLE Factory Skills

Canonical reusable skill library for DAVLE watch-face intelligence and production workflows.

## Canonical Market-to-Dial Stack

The current upstream intelligence/creative pipeline is:

1. `davle-watchface-market-research`
2. `davle-watchface-trend-analysis`
3. `davle-watchface-pattern-extraction`
4. `davle-watchface-portfolio-intelligence`
5. `davle-commercial-dial-synthesis`
6. `davle-watchface-opportunity-scoring`
7. `davle-dial-prompt-engineering`
8. image generation capability
9. `davle-dial-visual-qa`
10. standardized factory handoff

Post-release learning uses:

- `davle-watchface-feedback-learning`

Full autonomous orchestration uses:

- `davle-market-to-dial-orchestrator`

Each canonical skill lives in:

`skills/<skill-name>/SKILL.md`

The GitHub repository is the source of truth. Agents should read the latest relevant `SKILL.md` before execution rather than relying on remembered versions.

## Supporting Contracts

- `schemas/market-product-record.schema.json`
- `schemas/opportunity-score.schema.json`
- `schemas/portfolio-entry.schema.json`
- `schemas/release-feedback.schema.json`
- `schemas/factory-handoff.schema.json`

## Evaluation

Regression assets:

- `evals/market-to-dial-cases.json`
- `evals/market-to-dial-rubric.md`
- `evals/score_eval.py`
- `evals/validate_skill_library.py`

Skill changes should preserve hard gates and avoid material regression on the core evaluation set.

## Legacy Material

Older flat Markdown files under `skills/` such as `MARKET_INTEL_v1.md`, `LYSIEN_HERO_ART_v1.md`, `FACTORY_WORKFLOW_v1.md`, and related operational notes predate the canonical modular stack. Treat them as legacy/reference material unless a workflow explicitly calls them.

## Core Principle

Market evidence → trend signal → reusable patterns → original commercial synthesis → opportunity selection → dial-only generation → hard-gated visual QA → factory handoff → real-world feedback learning.
