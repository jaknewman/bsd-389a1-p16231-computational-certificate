#!/usr/bin/env python3
"""389a1: verify the precise I_n-adic valuation of a two-prime Kurihara residue.

An arithmetic verifier and conditional implication only. It cannot
compute modular symbols or authenticate a supplied Kurihara delta.
Sources: Kim Thm 1.8 + Castella-Sano Thm B + Cassels-Tate.

Input requires primes q1,q2, the genuine Frobenius traces a_q and the
correct period-normalized Kurihara residue mod I_(q1*q2).
Prime, residual and Manin hypotheses require separate authentication.
"""
from __future__ import annotations
import argparse


def valuation(x: int, p: int) -> int:
    if x == 0:
        return 10**12  # infinity sentinel for the exact integer zero
    x = abs(x)
    v = 0
    while x % p == 0:
        v += 1
        x //= p
    return v


def arithmetic_gate(p: int, q1: int, aq1: int, q2: int, aq2: int, delta: int) -> dict:
    if p < 5 or p == 389 or q1 == q2 or q1 in (p, 389) or q2 in (p, 389):
        raise ValueError("Require good p>=5 and distinct good auxiliary q")
    # The congruence check does not prove q are primes or a_q are genuine.
    k1 = min(valuation(q1 - 1, p), valuation(aq1 - q1 - 1, p))
    k2 = min(valuation(q2 - 1, p), valuation(aq2 - q2 - 1, p))
    k = min(k1, k2)
    if k < 1:
        raise ValueError("Auxiliary primes are not p-admissible")
    modulus = p ** k
    residue = delta % modulus
    if residue == 0:
        return dict(p=p, q1=q1, q2=q2, k=k, modulus=modulus,
                    residue=0, finite_witness=False,
                    status="ZERO_IN_QUOTIENT__NO_BOUND")
    e = valuation(residue, p)
    assert e < k
    even_bound = 2 * (e // 2)
    return dict(p=p, q1=q1, q2=q2, k=k, modulus=modulus,
                residue=residue, finite_witness=True, valuation=e,
                sha_order_upper_bound=p ** even_bound,
                sha_primary_zero=(even_bound == 0),
                status="CONDITIONAL_ON_AUTHENTIC_KURIHARA_AND_SOURCE_HYPOTHESES")


def self_test():
    # Earlier supplied normalized residues; the script does not recompute them.
    records = ((5, 41, -3, 61, -8, 4),
               (7, 113, 9, 673, 2, 2),
               (107, 369793, 2, 383917, -854, 34))
    for rec in records:
        ans = arithmetic_gate(*rec)
        assert ans["k"] == 1 and ans["sha_primary_zero"]
        print("PASS HISTORICAL_INPUT_ARITHMETIC", ans)
    # The auxiliary q and a_q below are genuine point-count arithmetic.
    # Delta=5 is SYNTHETIC and DOES NOT REPRESENT A COMPUTED KURIHARA NUMBER.
    ans = arithmetic_gate(5, 5351, -23, 10651, 2, 5)
    assert ans["k"] == 2 and ans["valuation"] == 1 and ans["sha_primary_zero"]
    print("PASS SYNTHETIC_E1_PARITY_BOOTSTRAP", ans)
    assert not arithmetic_gate(5, 5351, -23, 10651, 2, 0)["finite_witness"]
    for e in (2, 3, 4, 5):
        assert not arithmetic_gate(5, 5351, -23, 10651, 2, 5 ** e)["finite_witness"]
    print("PASS_PRECISION_FLOOR_CANNOT_IDENTIFY_HIGHER_E")
    print("SELF_TEST_PASS__NO_NEW_KURIHARA_COMPUTATION")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    for name in ("p", "q1", "aq1", "q2", "aq2", "delta"):
        ap.add_argument("--" + name, type=int)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    vals = [getattr(args, k) for k in ("p", "q1", "aq1", "q2", "aq2", "delta")]
    if any(v is None for v in vals):
        ap.error("Supply --p --q1 --aq1 --q2 --aq2 --delta or --self-test")
    print(arithmetic_gate(*vals))


if __name__ == "__main__":
    main()
