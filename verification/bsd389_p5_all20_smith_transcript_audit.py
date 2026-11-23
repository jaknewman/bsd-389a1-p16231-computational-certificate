#!/usr/bin/env python3
"""Audit the 20 reported Smith lines, without asserting arithmetic provenance.

Usage:
  python verification/bsd389_p5_all20_smith_transcript_audit.py --log /path/to/log.txt

The *conditional* strengthened size bound uses the exact norm-quotient
snake-lemma in paper/bsd389_p5_all20_norm_quotient_sharp_Sha_bound_2026-11-23.md.
"""
import argparse
import ast
import re
from collections import Counter

P = argparse.ArgumentParser()
P.add_argument("--log", required=True)
args = P.parse_args()
s = open(args.log, encoding="utf-8").read()
prefix = "TRUE_NORM_AND_THETA_24x24_SMITH_CERTIFICATE_PASS "
pattern = re.compile(
    r"^" + re.escape(prefix)
    + r"r (\d+) v5_resultant (\d+) nonunit_invariants (\[[^\]]*\]) "
    + r"true_Sha5_exponent_divides (\d+) "
    + r"true_Sha5_cardinality_at_most 5\^(\d+)\s*$", re.M)
rows = pattern.findall(s)
rs = {r for r in range(1, 25) if r % 5}
assert len(rows) == len(rs) == 20, f"expected 20 rows, got {len(rows)}"
seen = set()
classes = Counter()
for r0, a0, factors0, exponent0, old0 in rows:
    r, a, exponent, old = map(int, (r0, a0, exponent0, old0))
    assert r in rs and r not in seen, (r, seen)
    seen.add(r)
    factors = ast.literal_eval(factors0)
    expected = ([25] * 4) if r % 5 in (1, 2) else [5, 5, 25, 25, 125, 125]
    expected_a = 8 if r % 5 in (1, 2) else 12
    expected_e = 25 if r % 5 in (1, 2) else 125
    assert factors == expected, (r, factors)
    assert a == expected_a and exponent == expected_e, (r, a, exponent)
    assert old == 3*a, (r, old)
    classes[(a, exponent)] += 1
    print("TRANSCRIPT_ROW_CONSISTENT", r,
          "ring_length", a,
          "conditional_sha_exponent_divides", exponent,
          "conditional_sha_cardinality_at_most", f"5^{3*a-4}")
assert seen == rs
assert classes == Counter({(8,25): 10, (12,125): 10})
assert "ALL20_TRUE_SHA_FINITE_EXPONENT_ORDER_BOUND_PREMISES_PASS" in s
print("ALL20_TRANSCRIPT_INTERNAL_CONSISTENCY_PASS")
print("CAUTION_NOT_AN_ARITHMETIC_OR_SMITH_RECOMPUTATION")
print("CONDITIONAL_ON_GENUINE_THETA_FITT0_AND_THREE_GENERATORS")
