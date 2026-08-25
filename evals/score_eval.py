#!/usr/bin/env python3
import argparse
import json
import sys

WEIGHTS = {
    "research_evidence": 15,
    "fact_inference_separation": 10,
    "trend_reasoning": 10,
    "pattern_quality": 10,
    "commercial_thesis": 15,
    "opportunity_logic": 10,
    "originality": 10,
    "prompt_quality": 5,
    "visual_qa": 10,
    "factory_handoff": 5,
}


def evaluate(payload):
    scores = payload.get("scores", {})
    hard_gates = payload.get("hard_gates", {})

    missing = [key for key in WEIGHTS if key not in scores]
    if missing:
        raise ValueError("Missing scores: " + ", ".join(missing))

    for key in WEIGHTS:
        value = scores[key]
        if not isinstance(value, (int, float)):
            raise ValueError(f"Score {key} must be numeric")
        if not 0 <= value <= 5:
            raise ValueError(f"Score {key} must be between 0 and 5")

    weighted = sum((scores[key] / 5.0) * weight for key, weight in WEIGHTS.items())
    failed_gates = [key for key, value in hard_gates.items() if value is not True]

    if failed_gates or weighted < 80:
        verdict = "FAIL"
    elif weighted >= 90:
        verdict = "STRONG_PASS"
    else:
        verdict = "PASS"

    return {
        "weighted_score": round(weighted, 2),
        "verdict": verdict,
        "failed_hard_gates": failed_gates,
        "weights": WEIGHTS,
    }


def main():
    parser = argparse.ArgumentParser(description="Score a DAVLE market-to-dial evaluation result.")
    parser.add_argument("input", help="Path to JSON evaluation result, or - for stdin")
    args = parser.parse_args()

    if args.input == "-":
        payload = json.load(sys.stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as handle:
            payload = json.load(handle)

    print(json.dumps(evaluate(payload), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
