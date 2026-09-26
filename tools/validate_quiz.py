#!/usr/bin/env python
"""Validate a Learn2Think module's quiz_items.json against the Style Guide rules.

Usage:  python tools/validate_quiz.py content/core/M2
Prints PASS/FAIL lines and exits with code 1 if any errors are found.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

TYPES = {"SCN", "SPOT", "ASK", "SORT", "RANK", "EST", "FIX", "AUDIT"}
WRITTEN = {"FIX", "ASK", "EST"}
CHOICE = {"SCN", "SPOT", "ASK"}
LIMITS = {"stem": 60, "option": 25, "feedback": 40}

# Stage depth ranges for concept checks: (floor, ceiling)
DEPTH = {
    **{m: (1, 3) for m in ["M1", "M2", "M3", "M4", "M5", "M6"]},
    **{m: (2, 4) for m in ["M7", "M8"]},
    **{m: (3, 4) for m in ["M9", "M10"]},
}
SPECIALIST_DEPTH = (2, 4)


def words(text):
    return len(str(text or "").split())


def main(folder):
    folder = Path(folder)
    module = folder.name
    errors, warnings = [], []

    path = folder / "quiz_items.json"
    try:
        items = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL  cannot read {path}: {exc}")
        return 1
    if not isinstance(items, list):
        print("FAIL  quiz_items.json must be a JSON array")
        return 1

    floor, ceiling = DEPTH.get(module, SPECIALIST_DEPTH)
    ids = set()
    blocks = defaultdict(list)
    audit_count = 0

    for it in items:
        iid = it.get("id", "<missing id>")
        if iid in ids:
            errors.append(f"{iid}: duplicate id")
        ids.add(iid)

        for field in ("id", "type", "depth", "context", "stem"):
            if field not in it:
                errors.append(f"{iid}: missing '{field}'")

        typ = it.get("type")
        if typ not in TYPES:
            errors.append(f"{iid}: unknown type {typ}")
        if typ == "AUDIT":
            audit_count += 1
            if not it.get("planted_flaws"):
                errors.append(f"{iid}: AUDIT item needs planted_flaws")
        if it.get("context") not in ("IN", "GLOBAL"):
            errors.append(f"{iid}: context must be IN or GLOBAL")
        if not it.get("confidence_prompt", False):
            warnings.append(f"{iid}: confidence_prompt not true")

        if words(it.get("stem")) > LIMITS["stem"] and not it.get("exhibit"):
            warnings.append(f"{iid}: stem is {words(it.get('stem'))} words (>60)")

        opts = it.get("options")
        if typ in CHOICE and opts:
            if sum(1 for o in opts if o.get("correct")) != 1:
                errors.append(f"{iid}: needs exactly one correct option")
            for o in opts:
                if words(o.get("text")) > LIMITS["option"]:
                    warnings.append(f"{iid}/{o.get('id')}: option >25 words")
                if words(o.get("feedback")) > LIMITS["feedback"]:
                    warnings.append(f"{iid}/{o.get('id')}: feedback >40 words")
                if not o.get("feedback"):
                    errors.append(f"{iid}/{o.get('id')}: option missing feedback")
                if not o.get("correct") and not re.fullmatch(r"E\d{2,}", str(o.get("error_tag", ""))):
                    errors.append(f"{iid}/{o.get('id')}: wrong option missing error_tag")
                text = str(o.get("text", "")).lower()
                if "all of the above" in text or "none of the above" in text:
                    errors.append(f"{iid}: uses all/none of the above")
        if typ in {"FIX", "AUDIT"} and not it.get("criteria"):
            errors.append(f"{iid}: {typ} needs criteria")

        match = re.match(rf"^({re.escape(module)}-C\d+)-Q\d+$", iid)
        if match:
            blocks[match.group(1)].append(it)

    for block, block_items in sorted(blocks.items()):
        block_items.sort(key=lambda x: x["id"])
        depths = [x.get("depth", 0) for x in block_items]
        if not 3 <= len(block_items) <= 5:
            errors.append(f"{block}: {len(block_items)} items (need 3-5)")
        if depths and depths[0] != floor:
            warnings.append(f"{block}: first item depth {depths[0]} (stage floor is {floor})")
        if any(b < a for a, b in zip(depths, depths[1:])):
            errors.append(f"{block}: depth decreases {depths}")
        if depths and max(depths) < ceiling:
            errors.append(f"{block}: never reaches ceiling D{ceiling} {depths}")
        if not any(x.get("type") in WRITTEN and x.get("depth", 0) >= 2 for x in block_items):
            errors.append(f"{block}: no FIX/ASK/EST item at D2+")

    if audit_count == 0:
        errors.append(f"{module}: no AUDIT item in module")
    if not any(i.startswith(f"{module}-MC-") for i in ids):
        errors.append(f"{module}: no mastery check items ({module}-MC-Qnn)")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    print(f"\n{module}: {len(items)} items, {len(blocks)} concept blocks, "
          f"{len(errors)} errors, {len(warnings)} warnings -> {'PASS' if not errors else 'FAIL'}")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
