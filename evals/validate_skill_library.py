#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = [
    "davle-watchface-market-research",
    "davle-watchface-trend-analysis",
    "davle-watchface-pattern-extraction",
    "davle-commercial-dial-synthesis",
    "davle-watchface-opportunity-scoring",
    "davle-watchface-portfolio-intelligence",
    "davle-dial-prompt-engineering",
    "davle-dial-visual-qa",
    "davle-watchface-feedback-learning",
    "davle-market-to-dial-orchestrator",
]


def validate_skill(skill_name):
    path = ROOT / "skills" / skill_name / "SKILL.md"
    errors = []
    if not path.exists():
        return [f"missing {path.relative_to(ROOT)}"]

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        errors.append(f"{skill_name}: SKILL.md exceeds 500 lines")

    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append(f"{skill_name}: missing YAML frontmatter")
        return errors

    frontmatter = match.group(1)
    keys = []
    values = {}
    for line in frontmatter.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{skill_name}: malformed frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        keys.append(key)
        values[key] = value

    if set(keys) != {"name", "description"}:
        errors.append(f"{skill_name}: frontmatter keys must be exactly name, description; got {keys}")
    if values.get("name") != skill_name:
        errors.append(f"{skill_name}: frontmatter name does not match directory")
    if not values.get("description"):
        errors.append(f"{skill_name}: description is empty")
    return errors


def validate_json_files():
    errors = []
    for folder in [ROOT / "schemas", ROOT / "evals"]:
        if not folder.exists():
            continue
        for path in folder.rglob("*.json"):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
    return errors


def validate_orchestrator_links():
    errors = []
    path = ROOT / "skills" / "davle-market-to-dial-orchestrator" / "SKILL.md"
    if not path.exists():
        return errors
    text = path.read_text(encoding="utf-8")
    pipeline_dependencies = [
        "davle-watchface-market-research",
        "davle-watchface-trend-analysis",
        "davle-watchface-pattern-extraction",
        "davle-watchface-portfolio-intelligence",
        "davle-commercial-dial-synthesis",
        "davle-watchface-opportunity-scoring",
        "davle-dial-prompt-engineering",
        "davle-dial-visual-qa",
    ]
    for name in pipeline_dependencies:
        if name not in text:
            errors.append(f"orchestrator does not reference {name}")
    if "schemas/factory-handoff.schema.json" not in text:
        errors.append("orchestrator does not reference factory handoff schema")
    return errors


def main():
    errors = []
    for skill in REQUIRED_SKILLS:
        errors.extend(validate_skill(skill))
    errors.extend(validate_json_files())
    errors.extend(validate_orchestrator_links())

    if errors:
        print("DAVLE_SKILL_LIBRARY_VALIDATION=FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("DAVLE_SKILL_LIBRARY_VALIDATION=PASS")
    print(f"skills={len(REQUIRED_SKILLS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
