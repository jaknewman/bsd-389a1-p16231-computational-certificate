#!/usr/bin/env python3
"""Fast, exact Stage14 -> Stage30-vector -> toric polynomial -> norm 729 audit.

Requires only the existing local Stage14 oriented orbit JSON and Python stdlib.
Does NOT recompute Hecke eigenvector, Stage22 transitions, or theta derivatives.
Run:
  python -u verification/chi53_stage14_to_order9_toric_norm729_bridge.py
"""
from pathlib import Path
from math import gcd
import json
import hashlib

STAGE14 = Path.home() / "bsd389_chi53_stage14_orbit19.json"
# Frozen 33-dimensional Brandt Hecke vector from the historical Stage30 proof.
V = (0, 0, 0, 1, -1, 1, -1, -1, 1, -1, -1,
     -1, 0, 0, 1, -1, -1, 0, 0, 2, 2, 1, 0,
     0, 0, 1, 1, -2, 1, -2, -2, 2, 0)
EXPECTED_CLASSES = (1, 2, 9, 23, 22, 11, 4, 19, 31,
                    16, 15, 31, 19, 11, 4, 23, 22, 10)
EXPECTED_VALUES = (0, 0, -1, 0, 0, -1, -1, 2, 2,
                   -1, -1, 2, 2, -1, -1, 0, 0, -1)
PHI9 = (1, 0, 0, 1, 0, 0, 1)

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def poly_mod(a, b):
    a = trim(a)
    degree = len(b) - 1
    while len(a) > degree:
        offset = len(a) - len(b)
        top = a[-1]
        for j, bj in enumerate(b):
            a[offset+j] -= top * bj
        a = trim(a)
    return a

def det_bareiss(rows):
    a = [list(row) for row in rows]
    n = len(a)
    sign = 1
    old = 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((i for i in range(k+1,n) if a[i][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        x = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                y = a[i][j]*x - a[i][k]*a[k][j]
                assert y % old == 0
                a[i][j] = y // old
        for i in range(k+1,n):
            a[i][k] = 0
        old = x
    return sign*a[-1][-1]

def main():
    raw = STAGE14.read_bytes()
    data = json.loads(raw)
    assert data["status"] == "ORBIT_18_PASS"
    steps = data["steps"]
    assert len(steps) == 18
    assert len(V) == 33
    labels = tuple(int(row["index"]) for row in steps)
    assert labels == EXPECTED_CLASSES, ("CLASS_ORBIT_MISMATCH", labels)
    oriented = [(int(row["index"]), tuple(map(int,row["coefficients"])))
                for row in steps]
    assert len(oriented) == len(set(oriented)) == 18
    print("CHI53_STAGE14_JSON_SHA256", hashlib.sha256(raw).hexdigest(), flush=True)
    print("CHI53_STAGE14_18_ORIENTED_ORBIT_PASS", flush=True)
    coeffs = tuple(V[j] for j in labels)
    assert coeffs == EXPECTED_VALUES
    print("CHI53_STAGE14_STAGE30_VECTOR_TO_STAGE23_COEFFICIENTS_PASS", list(coeffs), flush=True)

    # The 18 coefficients represent P(X)=sum c_j X^j.
    # Their order-nine character value lives in Z[X]/Phi9.
    reduced = poly_mod(coeffs, PHI9)
    assert reduced == [0,-3,0,3,-3,-3], reduced
    assert sum(coeffs)==0
    print("CHI53_ORDER9_POLYNOMIAL_REDUCTION_PASS", reduced, flush=True)

    cols = [poly_mod([0]*j + list(coeffs), PHI9) for j in range(6)]
    mat = [[col[i] if i < len(col) else 0 for col in cols]
           for i in range(6)]
    norm = det_bareiss(mat)
    assert norm == 729 == 3**6
    print("CHI53_STAGE14_TO_TORIC_NORM729_PASS", norm, flush=True)
    print("BOUNDARY_ORBIT_RELATIONS_AND_HEECKE_EIGENVECTOR_NOT_INDEPENDENTLY_REPROVED", flush=True)
    print("BOUNDARY_PRO_P_ANTICYCLOTOMIC_THETA_SECOND_DERIVATIVE_NOT_COMPUTED", flush=True)
    print("BOUNDARY_SHA_P16231_NOT_PROVED_BY_THIS_TEST", flush=True)

if __name__ == "__main__":
    main()
