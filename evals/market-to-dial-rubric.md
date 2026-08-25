# DAVLE Market-to-Dial Evaluation Rubric

Use this rubric for regression testing skill changes against `evals/market-to-dial-cases.json`.

## Hard gates
Any failed hard gate forces FAIL regardless of weighted score:
- evidence_honesty: no invented sales, rankings, reviews, sources, or certainty,
- originality: no recognizable competitor copy/branding,
- dial_only: final concept obeys dial-only unless the test explicitly requests otherwise,
- user_scope: respects explicit user constraints,
- no_critical_geometry_failure: no severe malformed dial geometry in an accepted final image.

## Weighted dimensions
Score 0–5.

### research_evidence — 15%
0: unsupported claims. 3: useful current evidence with visible gaps. 5: strong, current, diverse evidence with source traceability and explicit limitations.

### fact_inference_separation — 10%
0: guesses presented as facts. 3: mostly separated. 5: observed facts, inference, and creative decisions are consistently distinct.

### trend_reasoning — 10%
0: calls isolated examples trends. 3: reasonable multi-product trend assessment. 5: distinguishes momentum, persistence, saturation, and uncertainty using multiple signals.

### pattern_quality — 10%
0: superficial feature list. 3: repeated visual/functional/commercial patterns. 5: patterns are independent, recurring, evidence-backed, and commercially interpretable.

### commercial_thesis — 15%
0: generic aesthetic statement. 3: coherent target/layout/hook strategy. 5: sharply differentiated, implementable thesis with clear purchase logic tied to evidence.

### opportunity_logic — 10%
0: arbitrary choice. 3: compares alternatives. 5: disciplined scoring, saturation awareness, risks, confidence, and a justified production choice.

### originality — 10%
0: derivative/clone-like. 3: distinct synthesis. 5: clearly original while preserving validated abstract market patterns.

### prompt_quality — 5%
0: vague generator request. 3: usable structured prompt. 5: precise hierarchy, geometry, styling, negative constraints, and dial-only enforcement.

### visual_qa — 10%
0: accepts obvious defects. 3: catches major issues. 5: rigorous hard gates, targeted corrections, and honest ACCEPT/REVISE/REJECT judgment.

### factory_handoff — 5%
0: narrative only. 3: usable concept package. 5: consistent handoff containing rationale, thesis, exact prompt, image reference, visual spec, and QA verdict.

## Verdict thresholds
- STRONG_PASS: >=90 and all hard gates pass.
- PASS: >=80 and all hard gates pass.
- FAIL: <80 or any hard gate fails.

## Regression rule
Do not merge a skill change that materially reduces the aggregate score or introduces a new hard-gate failure on a previously passing core case unless the tradeoff is explicitly accepted and documented.