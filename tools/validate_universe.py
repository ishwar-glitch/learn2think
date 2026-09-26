#!/usr/bin/env python
"""Validate Company Universe profiles (structure) and recompute the key arithmetic.

Usage:  python tools/validate_universe.py content/universe
Prints PASS/FAIL lines and exits with code 1 if any check fails.
"""
import re
import sys
from pathlib import Path

REQUIRED = ["## Story", "## Business model", "## Canon facts", "## Org chart", "## Strengths and weaknesses", "## Used by"]
fails = 0


def check(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + (" " + detail if detail else ""))
    if not ok:
        fails += 1


def close(a, b, tol):
    return abs(a - b) <= tol


def profile_checks(path):
    t = path.read_text(encoding="utf-8")
    pid = path.stem
    check(pid + " header", t.startswith("# " + pid + " "))
    check(pid + " sections", all(s in t for s in REQUIRED))
    facts = re.findall(r"^\d+\. ", t.split("## Canon facts")[1].split("## Org chart")[0], re.M)
    check(pid + " canon facts 8-12", 8 <= len(facts) <= 12, "(%d)" % len(facts))
    rows = [r for r in t.split("## Org chart")[1].split("## Strengths")[0].splitlines() if r.startswith("| ") and "---" not in r and "Name" not in r]
    check(pid + " characters 5-6", 5 <= len(rows) <= 6, "(%d)" % len(rows))
    check(pid + " context", ("**Context:** IN" in t) == pid.startswith("U-IN"))
    check(pid + " name status", "[VERIFY]" in t)


def arithmetic():
    # U-IN-1
    orders = 154000 * 365
    check("U-IN-1 stores", 60 + 30 + 20 + 30 == 140 and 140 * 1100 == 154000)
    check("U-IN-1 GMV crore", close(orders * 420 / 1e7, 2361, 1), "(%.1f)" % (orders * 420 / 1e7))
    check("U-IN-1 revenue crore", close(orders * 80 / 1e7, 450, 1), "(%.1f)" % (orders * 80 / 1e7))
    check("U-IN-1 cost per order", 38 + 12 + 14 + 6 + 5 + 7 == 82 and 80 - 82 == -2)
    check("U-IN-1 burn crore", close(orders * 2 / 1e7 + 133, 144, 0.5), "(%.1f)" % (orders * 2 / 1e7 + 133))
    check("U-IN-1 riders", 140 * 70 == 9800)
    # U-IN-2
    check("U-IN-2 book", 2000 + 1200 == 3200)
    check("U-IN-2 disbursals", 250 + 130 == 380 and close(250e7 / 125000, 20000, 1) and close(130e7 / 800000, 1625, 1))
    check("U-IN-2 funnel", 200000 * 0.62 == 124000 and close(124000 * 0.24, 29760, 1) and close(21625 / 29760, 0.73, 0.01) and 20000 + 1625 == 21625)
    check("U-IN-2 P&L", 3200 * 0.24 == 768 and close(3200 * 0.105, 336, 0.1) and close(768 - 336, 432, 0.1) and 432 - 144 - 190 == 98 and 3200 * 0.045 == 144)
    # U-IN-3
    check("U-IN-3 revenue", 310000 * 14000 / 1e7 == 434.0 and 310000 / 6.2e6 == 0.05)
    check("U-IN-3 costs", 32 + 38 + 14 + 10 + 6 == 100 and close(434 * .32, 139, .2) and close(434 * .38, 165, .2) and close(434 * .06, 26, .2))
    # U-IN-4
    check("U-IN-4 channels", 94.5 + 52.5 + 63 == 210 and close(94.5 / 210, .45, 1e-9) and close(52.5 / 210, .25, 1e-9))
    check("U-IN-4 orders lakh", close(94.5e7 / 690 / 1e5, 13.7, .05), "(%.2f)" % (94.5e7 / 690 / 1e5))
    check("U-IN-4 mix", 55 + 25 + 20 == 100)
    # U-GL-1
    check("U-GL-1 ARR", close(148e6 / 9800, 15100, 5) and close(148e6 / 310000, 477, 1) and close(477 / 12, 39.8, .1))
    # U-GL-2
    check("U-GL-2 ARR", 900000 + 900000 == 1800000 and close(900000 * 12.99 * 12 / 1e6, 140, .5) and close(900000 * 79.99 / 1e6, 72, .1) and close(140.3 + 72.0, 212, .5))
    check("U-GL-2 discount joiners", close(1.6e6 * .38, 608000, 1))
    # U-GL-3
    check("U-GL-3 GMV", close(620000 * 118 / 1e6, 73.2, .1) and close(620000 * 118 * 12 / 1e6, 878, .5) and close(878 * .22, 193, .3))
    check("U-GL-3 pros and mix", close(620000 / 46000, 13.5, .05) and 38 + 17 + 15 + 14 + 10 + 6 == 100)
    # U-GL-4
    check("U-GL-4 revenue", 8.0e6 * 80 == 640e6)
    check("U-GL-4 P&L", close(640 * .38, 243.2, .01) and close(8.0 * 14.6, 116.8, .01) and close(640 * .12, 76.8, .01) and close(640 * .05, 32, .01) and close(243.2 - 116.8 - 76.8 - 32, 17.6, .01) and close(17.6 / 640, .0275, 1e-6))


for p in sorted(Path(sys.argv[1]).glob("U-*.md")):
    profile_checks(p)
check("8 profiles", len(list(Path(sys.argv[1]).glob("U-*.md"))) == 8)
arithmetic()
print("\n%d failure(s)" % fails)
sys.exit(1 if fails else 0)
