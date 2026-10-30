#!/usr/bin/env python3
"""Cheap genuine p=107 supersingular conductor-p^2 leading-moment probe.

For E=389a1 and p=107, a_p=0.  Compute the tame-trivial plus-symbol
quadratic moment C2 using only p(p-1)/2 = 5671 rational cusp symbols,
not (p-1)*p^2 = 1,212,? level-p^3 terms, and do not rerun K107's
70,984,909,590 half-range positions.

The conditional exact Hecke/Frobenius derivation is the same as the one
in paper/bsd389_p599_hecke_frobenius_precise_lemma_2026-10-30.md,
with 2 real components. Here F0[2] mod p = C2/2 mod p.

The script checks rank, generators, Galois surjectivity and normalized
p-adic regulator independently in Sage. A printed "DERIVED" result is
not a successful invocation of p_primary_bound or direct level-p^3
summation. A zero C2 gives *no* assertion about Sha.

Run: python -u verification/bsd389_p107_supersingular_p2_shortcut.py
"""
import argparse
import hashlib
from pathlib import Path

from sage.all import EllipticCurve, QQ, ZZ, log

P = 107
N = P * P
EXPECTED_PAIRS = P * (P - 1) // 2


def residue(z):
    z = QQ(z)
    denominator = int(z.denominator())
    if denominator % P == 0:
        raise ValueError("NOT_P_INTEGRAL_SYMBOL: " + str(z))
    return (int(z.numerator()) * pow(denominator, -1, P)) % P


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", type=int, default=1000)
    parser.add_argument("--skip-regulator", action="store_true")
    args = parser.parse_args()

    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert E.conductor() == 389 and E.discriminant() == 389
    assert E.ap(P) == 0 and E.is_supersingular(P)
    assert E.Np(P) == P + 1
    components = ZZ(E.real_components())
    assert components == 2
    L = E.padic_lseries(P)
    symbol = L._modular_symbol
    assert residue(symbol(QQ(0))) == 0

    print("P107_SUPERSINGULAR_P2_START", flush=True)
    print("P107_CONFIG", "p", P, "modulus", N,
          "pairs", EXPECTED_PAIRS, "a_p", 0,
          "real_components", int(components), flush=True)

    C0 = C1 = C2 = 0
    buckets = [0] * P
    seen = 0
    for a in range(1, (N - 1)//2 + 1):
        if a % P == 0:
            continue
        symbol_value = residue(symbol(QQ(a)/N))
        fermat = pow(a, P - 1, N)
        assert fermat % P == 1
        j = (-((fermat - 1)//P)) % P
        assert (pow(a, P, N) * (1 + P*j)) % N == a
        # Weight j is invariant under a <-> -a for odd p.
        value2 = j*(j-1)//2
        C0 = (C0 + 2*symbol_value) % P
        C1 = (C1 + 2*symbol_value*j) % P
        C2 = (C2 + 2*symbol_value*value2) % P
        buckets[a%P] = (buckets[a%P] + symbol_value) % P
        buckets[-a%P] = (buckets[-a%P] + symbol_value) % P
        seen += 1
        if args.progress and seen % args.progress == 0:
            print("P107_P2_PROGRESS", seen, "/", EXPECTED_PAIRS,
                  flush=True)
    assert seen == EXPECTED_PAIRS
    assert all(v == 0 for v in buckets[1:]), (
        "HECKE_P2_FIBRE_MISMATCH", [(i, buckets[i]) for i in range(1,P) if buckets[i]]
    )
    print("P107_ALL_HECKE_P2_FIBRES_PASS", P-1, flush=True)
    assert C0 == C1 == 0, ("LOW_MOMENTS_NONZERO", C0, C1)
    print("P107_CYCLOTOMIC_P2_MOMENTS_PASS",
          "C0", C0, "C1", C1, "C2", C2, flush=True)

    # Hecke plus Teich lift identities: A3 = 0 mod p, B3/p = C2 mod p.
    # Sage 10.9 Frobenius projection, real_components=2:
    # F0[2] = [2*A3-(p-1)*B3/p] / [2*(p+1)^2] = C2/2 mod p.
    f0 = C2 * pow(2, -1, P) % P
    print("P107_ANALYTIC_QUADRATIC_F0_DERIVED_MODP", f0, flush=True)

    if args.skip_regulator:
        print("P107_REGULATOR_GATE_SKIPPED", flush=True)
        return
    assert E.rank(proof=True) == 2
    gens = E.gens(proof=True)
    assert len(gens) == 2 and E.gens_certain()
    assert E.torsion_order() == 1
    assert E.tamagawa_product() == 1
    surj = E.galois_representation().is_surjective(P)
    assert surj
    print("P107_RANK2_SURJECTIVITY_TAMAGAWA_PASS",
          "generators", gens, "surjective", surj, flush=True)

    reg = E.padic_regulator(P, prec=6)
    K = reg[0].parent()
    lg = log(K(1+P))
    norm = [reg[i]/lg**2 for i in range(2)]
    valuations = [x.valuation() for x in norm]
    print("P107_NORMALIZED_REGULATOR_VALUATIONS", valuations, flush=True)
    if valuations[0] == 0:
        residue0 = int(ZZ(norm[0].residue()))
        print("P107_NORMALIZED_REGULATOR_0_RESIDUE", residue0, flush=True)
    else:
        residue0 = None

    # Provable-bound applicability is CONDITIONAL on independently reviewed
    # exact Hecke/precision lemmas and Stein-Wuthrich/Kato theorem.
    if f0 != 0 and valuations[0] == 0:
        print("P107_STEIN_WUTHRICH_BOUND_ZERO_DERIVED",
              "analytic_val", 0, "regulator_val", 0, flush=True)
        print("P107_SHA_ZERO_CONDITIONAL_ON_PROVEN_HECCKE_AND_KATO_BRIDGE",
              flush=True)
    else:
        print("P107_FIRST_DIGIT_NOT_ENOUGH_FOR_SHA_BOUND",
              "analytic_f0", f0,
              "regulator_v0", valuations[0], flush=True)
        print("P107_USE_ARCHIVED_FULL_KURIHARA_DELTA_34_AND_KIM_THEOREM",
              flush=True)
    print("P107_SUPERSINGULAR_P2_FINISHED", flush=True)


if __name__ == "__main__":
    main()
