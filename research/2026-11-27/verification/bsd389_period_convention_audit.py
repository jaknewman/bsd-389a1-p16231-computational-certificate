#!/usr/bin/env python3
"""BSD389a1 normalization bridge: primitive real period versus BSD period.

Validates all reported raw p^2 coefficients from the unmodified CSV and
computes their two unit-normalized variants. It does NOT independently
recompute all 297 modular-symbol sums or prove a global Selmer assertion.
"""
import csv, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSV = ROOT.parent / 'data' / 'ordinary_p2_5_to_1999.csv'
EXPECTED = 'cd0cfbb3f9c216433eb95966c0896f0ab64eabfa38f17480e93e98f15090afe9'
assert hashlib.sha256(CSV.read_bytes()).hexdigest() == EXPECTED
rows = list(csv.DictReader(CSV.open(newline='')))
assert len(rows) == 297
assert len({int(r['p']) for r in rows}) == 297
checks = {5: 4, 7: 5, 11: 9, 13: 3, 17: 13, 89: 39}
for r in rows:
    p, ap, c = int(r['p']), int(r['ap']), int(r['c2'])
    assert p >= 5 and p != 389 and ap % p and c % p
    assert int(r['c0']) == int(r['c1']) == 0
    primitive = c * pow(ap, -2, p) % p
    bsd_real_period = primitive * pow(2, -1, p) % p
    assert primitive != 0 and bsd_real_period != 0
    if p in checks:
        assert bsd_real_period == checks[p]
        print('PERIOD_CONVENTION_CHECK_PASS', p, c, primitive, bsd_real_period)

# Neron primitive real period Omega+ = 2.490212...,
# full BSD real period = 2 Omega+, since E(R) has two components.
assert 321*pow(2,-1,389) % 389 == 355
print('P389_LEADING_COEFF_PRIMITIVE_AND_BSD', 321, 355)
print('ALL_REPORTED_ORDINARY_COEFFS_REMAIN_UNITS',len(rows))
print('INDEPENDENT_SAGEMATH_DOCUMENTATION_389A_P5_T2_MOD5',checks[5])
print('BOUNDARY: CSV consistency and normalization, NOT a rerun of all 297 sums')
