#!/usr/bin/env python3
"""Constructive mathematical counterexample to naive uniform Selmer determinants.

This program illustrates and witnesses an EXACT general algebraic lemma
proved in paper/bsd389_uniform_global_integral_det_vs_profinite_counterexample_2026-11-01.md:

R = product_p Z_p, b=(p)_p,
X = R^2 (+) (R/b R)^2,
Fitt_2(X) = (b^2), and its p-component is (p^2) at EVERY prime.

For an arbitrary nonzero user-specified integer C, the code constructs
a prime q dividing abs(C)+1, so q does not divide C. Therefore C is a
q-adic unit, while the local Fitt_2 is q^2 Z_q: C does NOT lie in it.
This disproves any claim that a profinite nonzero determinant alone
supplies a uniform *diagonal integer* C.

This abstract module is not asserted to be an actual elliptic Selmer group.
"""
import argparse
from math import gcd


def smallest_prime_factor(n):
    assert n >= 2
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def all_2x2_minors_4x2(p):
    """Relation matrix 4x2 for Z_p^2 (+) (Z_p/p)^2."""
    rows = [(0, 0), (0, 0), (p, 0), (0, p)]
    minors = [a[0] * b[1] - a[1] * b[0]
              for i, a in enumerate(rows)
              for b in rows[i+1:]]
    answer = 0
    for determinant in minors:
        answer = gcd(answer, determinant)
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--integer", type=int, default=729,
                        help="candidate diagonal integer, must be nonzero")
    args = parser.parse_args()
    C = args.integer
    if C == 0:
        parser.error("--integer must be nonzero")
    q = smallest_prime_factor(abs(C) + 1)
    assert (abs(C) + 1) % q == 0
    assert gcd(q, C) == 1
    assert C % q != 0
    assert all_2x2_minors_4x2(q) == q*q
    print("FINITE_LOCAL_FITTING_MINORS_PASS",
          "prime", q, "fitt2_generator", q*q, flush=True)
    print("CONSTRUCTIVE_NO_FIXED_DIAGONAL_INTEGER_PASS",
          "candidate_C", C, "counterexample_prime", q,
          "q_divides_C_plus_one", True,
          "q_divides_C", False, flush=True)
    print("MATHEMATICAL_GLOBAL_PROFINITE_COUNTEREXAMPLE",
          "R=product_p(Zp)", "b=(p)_p",
          "Fitt2=(b^2)", "components=(p^2) for ALL p", flush=True)
    print("BOUNDARY_NOT_A_REAL_SHA_MODULE_AND_NOT_AN_ALL_PRIME_SHA_PROOF", flush=True)


if __name__ == "__main__":
    main()
