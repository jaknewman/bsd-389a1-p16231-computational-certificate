#!/usr/bin/env python3
"""389a1: certify the remaining analytic gate for Kim's supersingular branch.

K = Q(sqrt(-4279)), p=107.  This script does NOT compute Heegner points,
does NOT prove Sha[p^infinity] finite, and does NOT certify any ordinary-prime
application.  The branch for 107 permits the bad prime 389 ramified in K.

Usage:
  python -u verification/bsd389_kim107_twist4279_gate.py
  python -u verification/bsd389_kim107_twist4279_gate.py --multiplier 3

Output CERTIFIED_ANALYTIC_RANK_ONE_PASS only if sign=-1 and the documented
Sage L-series first-derivative error bound excludes zero.
"""
import argparse
from math import isqrt
from sage.all import EllipticCurve, ZZ, kronecker_symbol

D = ZZ(-4279)
P = ZZ(107)
N = ZZ(389)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--multiplier", type=int, default=2,
                    help="number of multiples of ceil(sqrt(conductor)) (default 2)")
    ap.add_argument("--bits", type=int, default=128,
                    help="Sage real precision for derivative (default 128)")
    a = ap.parse_args()
    assert 1 <= a.multiplier <= 10
    assert 64 <= a.bits <= 512
    E = EllipticCurve("389a1")
    assert E.conductor() == N
    assert D % 4 == 1
    assert abs(D) == N * 11
    assert N.is_prime() and ZZ(11).is_prime()
    assert [int(kronecker_symbol(D, p)) for p in (2, 107, 16231, 389)] == [1, 1, 1, 0]
    assert E.ap(P) == 0  # 107 supersingular, from previous certificate
    print("KIM107_LOCAL_K_GATES_PASS",
          "D", D, "p_split", 107,
          "bad_389_ramified", True,
          "2_split", True, flush=True)
    ET = E.quadratic_twist(D)
    n = ZZ(ET.conductor())
    w = ZZ(ET.root_number())
    print("KIM107_TWIST_CONDUCTOR", n, flush=True)
    print("KIM107_TWIST_ROOT_NUMBER", w, flush=True)
    if w != -1:
        print("KIM107_SIGN_MINUS_GATE_FAIL",
              "Do not use derivative-at-one in an even-sign case.", flush=True)
        return
    print("KIM107_SIGN_MINUS_PASS", flush=True)
    k = a.multiplier * (isqrt(int(n)) + 1)
    print("KIM107_DERIVATIVE_INTERVAL_START", "terms", k,
          "precision_bits", a.bits, flush=True)
    value, error = ET.lseries().deriv_at1(k=k, prec=a.bits)
    print("KIM107_DERIVATIVE_APPROX", value, flush=True)
    print("KIM107_DERIVATIVE_ERROR_BOUND", error, flush=True)
    lo = value - error
    hi = value + error
    print("KIM107_DERIVATIVE_INTERVAL_APPROX", lo, hi, flush=True)
    if lo > 0 or hi < 0:
        print("KIM107_TWIST_DERIVATIVE_NONZERO_CERTIFIED_PASS", flush=True)
        print("KIM107_TWIST_ANALYTIC_RANK_ONE_PASS", flush=True)
        print("KIM107_SUPERSINGULAR_K_ANALYTIC_GATE_PASS", flush=True)
    else:
        print("KIM107_TWIST_DERIVATIVE_INTERVAL_INCONCLUSIVE",
              "try --multiplier 3 or 4", flush=True)
    print("BOUNDARY: analytic hypothesis only; Kim's theorem also needs",
          "derived Heegner point congruences to conclude Sha finiteness.", flush=True)

if __name__ == "__main__":
    main()