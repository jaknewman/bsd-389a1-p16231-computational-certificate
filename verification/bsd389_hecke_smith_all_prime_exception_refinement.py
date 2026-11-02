#!/usr/bin/env python3
"""All-prime congruence refinement via the Smith invariants of true integer Hecke matrices.

At E=389a1, sign-plus level-389 integral modular-symbol lattice dimension 33.
USER-RUN BASELINE: T2-a2*I has Q-rank 32, a primitive 33-vector in its
right kernel, and one maximal minor with abs(det)=29000=2^3*5^3*29.
Mod5 rank is 29, mod7/mod107 rank32.

The exact GCD of ALL 32x32 minors of any stacked matrix is the PRODUCT
of its 32 nonzero Smith elementary divisors D. So the divisors of D
are the EXACT exceptional primes where this *fixed* Hecke system has
mod-p kernel dimension >1. This is strictly sharper than one arbitrary
maximal minor (=29000): D must divide 29000 and decreases on stacking
more operators. The script adds T3,T5,T7,... on the same *integral*
lattice, and checks the primitive rational E-eigenvector is killed by
each one. It computes exact D via PARI Smith invariants.

Critical scope: D bounds modular-symbol Hecke congruence exceptions
ONLY. D IS NOT a uniform Selmer/Sha Fitt2 bound and does not force
2-prime Kurihara mixed coefficient M11 nonzero.

Sage 10.9 invocation:
  python -u verification/bsd389_hecke_smith_all_prime_exception_refinement.py \
    --output ~/bsd389_hecke_smith_refinement.json \
    --max-operators 8

Read and check the user's original canonical source JSON, so there is
no dependence on guessed integral eigenvector coordinates.
"""

import argparse
from functools import reduce
from hashlib import sha256
import json
from operator import mul
from pathlib import Path

from sage.all import (
    EllipticCurve, GF, ModularSymbols, QQ, ZZ, identity_matrix,
    matrix, vector,
)

N = 389
D0_MINOR = 29000
BASELINE_SHA256 = "afccd10890e7c24f591f828576e78f901de7ba83b46fe17a7582567233297c64"
HEC_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
PROBES = (2, 5, 29, 7, 107)
EXPECTED_BASELINE = {5: 29, 7: 32, 107: 32}


def canonical_digested_json(path, expected):
    raw = path.read_bytes()
    obj = json.loads(raw)
    canon = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert raw == canon + b"\n", "BASELINE_IS_NOT_CANONICAL_JSON"
    found = sha256(canon).hexdigest()
    assert found == expected, ("BASELINE_DIGEST_MISMATCH", found, expected)
    return obj


def smith_nonzero_invariants(A, desired_rank):
    # Sage's elementary_divisors() is documented to be substantially
    # faster than smith_form() with unimodular transformation matrices.
    invariants = [abs(ZZ(s)) for s in A.elementary_divisors() if s]
    assert len(invariants) == desired_rank, (
        "WRONG_INTEGRAL_SMITH_RANK", len(invariants), desired_rank
    )
    product = reduce(mul, invariants, ZZ(1))
    assert product > 0
    return invariants, ZZ(product)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--baseline", type=Path, default=Path.home() /
        "bsd389_integral_hecke_eigenline_minor.json"
    )
    parser.add_argument(
        "--output", type=Path, default=Path.home() /
        "bsd389_hecke_smith_refinement.json"
    )
    parser.add_argument("--max-operators", type=int, default=8)
    args = parser.parse_args()
    assert 1 <= args.max_operators <= len(HEC_PRIMES)

    original = canonical_digested_json(args.baseline, BASELINE_SHA256)
    assert original["curve"] == "389a1"
    assert original["level"] == N and original["sign"] == 1
    assert original["ambient_dim"] == 33
    assert original["rational_rank"] == 32
    assert original["maximal_minor_det"] in ("29000", "-29000")
    assert original["uniform_integer_C"] == "29000"
    assert original["hecke_primes_and_ap"] == [[2, -2]]
    v = vector(ZZ, original["primitive_integer_eigenvector"])
    assert len(v) == 33
    from math import gcd
    assert any(x != 0 for x in v)
    assert reduce(gcd, (abs(int(x)) for x in v), 0) == 1
    print("HECKE_SMITH_BASELINE_CANONICAL_SHA256_PASS", BASELINE_SHA256,
          flush=True)

    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert ZZ(E.conductor()) == N
    M = ModularSymbols(N, 2, sign=+1, base_ring=QQ)
    d = int(M.dimension())
    assert d == 33 and int(M.integral_structure().rank()) == d
    A2 = matrix(ZZ, M.integral_hecke_matrix(2))
    A2 -= ZZ(E.ap(2)) * identity_matrix(ZZ, d)
    assert A2.nrows() == A2.ncols() == d
    assert A2 * v == vector(ZZ, d)
    assert int(A2.rank()) == d - 1

    rows = [int(i) for i in original["maximal_minor_rows"]]
    cols = [int(j) for j in original["maximal_minor_columns"]]
    assert len(rows) == len(cols) == d - 1
    assert len(set(rows)) == len(set(cols)) == d - 1
    reconstructed_minor = ZZ(
        A2.matrix_from_rows_and_columns(rows, cols).det()
    )
    assert abs(reconstructed_minor) == D0_MINOR
    print("HECKE_SMITH_BASELINE_T2_MINOR_29000_RECONSTRUCTED_PASS",
          "det", reconstructed_minor, "rank_Q", d-1, flush=True)

    for p, expected in EXPECTED_BASELINE.items():
        rank = int(A2.change_ring(GF(p)).rank())
        assert rank == expected, ("BASELINE_MODP_RANK_MISMATCH", p, rank, expected)
    print("HECKE_SMITH_BASELINE_MOD5_7_107_RANKS_PASS",
          "rank_p5", 29, "rank_p7", 32, "rank_p107", 32, flush=True)

    stacked = matrix(ZZ, 0, d)
    steps = []
    previous = ZZ(D0_MINOR)
    for ell in HEC_PRIMES[:args.max_operators]:
        if ell == 2:
            A = A2
        else:
            A = matrix(ZZ, M.integral_hecke_matrix(ell))
            assert A.nrows() == A.ncols() == d
            A -= ZZ(E.ap(ell)) * identity_matrix(ZZ, d)
        assert A*v == vector(ZZ, d), (
            "HECKE_EIGENVECTOR_NOT_COMMON", ell
        )
        stacked = stacked.stack(A)

        invariants, D = smith_nonzero_invariants(stacked, d-1)
        assert D0_MINOR % D == 0, (
            "SMITH_GCD_NOT_DIVIDING_KNOWN_29000_MINOR", ell, D
        )
        assert previous % D == 0, (
            "GCD_OF_MAXIMAL_MINORS_INCREASED_ON_STACKING", ell,
            previous, D
        )
        assert sum(x != 1 for x in invariants) <= d-1
        ranks = {}
        for p in PROBES:
            rank = int(stacked.change_ring(GF(p)).rank())
            predicted_rank = sum((s % p != 0) for s in invariants)
            assert rank == predicted_rank, (
                "SNF_VS_INDEPENDENT_MODP_RANK_MISMATCH",
                ell, p, predicted_rank, rank
            )
            assert (rank == d-1) == (D % p != 0)
            ranks[str(p)] = {
                "rank": rank,
                "kernel_dim": d-rank,
                "p_divides_smith_gcd": D % p == 0,
            }
        factors = [[int(p), int(e)] for p, e in ZZ(D).factor()]
        # Since D|29000, its possible prime factors are *exactly*
        # contained in {2,5,29}; hence these 5 probes cover all
        # possible exceptional primes for the selected stack.
        assert all(p in (2,5,29) for p,e in factors)
        assert all(e >= 1 for p,e in factors)
        print("HECKE_SMITH_STACK_CERTIFICATE",
              "ell", ell, "ap", E.ap(ell),
              "operators", len(steps)+1,
              "rows", int(stacked.nrows()),
              "exact_gcd_maximal_minors", D,
              "factorization", str(D.factor()),
              "rank_p2", ranks["2"]["rank"],
              "rank_p5", ranks["5"]["rank"],
              "rank_p29", ranks["29"]["rank"],
              flush=True)
        steps.append({
            "hecke_prime": int(ell), "a_ell": int(E.ap(ell)),
            "stacked_rows": int(stacked.nrows()),
            "exact_nonzero_smith_invariants": [int(s) for s in invariants],
            "gcd_all_maximal_minors": str(D),
            "factorization": factors,
            "probes": ranks,
        })
        previous = D
        if D == 1:
            print("HECKE_SMITH_ALL_PRIMES_EIGENLINE_RIGIDITY_PASS",
                  "first_n_operators", len(steps), flush=True)
            break

    final_D = ZZ(steps[-1]["gcd_all_maximal_minors"])
    out = {
        "curve": "389a1",
        "level": N,
        "sign": 1,
        "ambient_integral_lattice_dim": d,
        "baseline_sha256": BASELINE_SHA256,
        "baseline_minor_abs": D0_MINOR,
        "primitive_integer_kernel_vector": [int(x) for x in v],
        "steps": steps,
        "final_exact_gcd_of_all_rank32_minors": str(final_D),
        "final_exact_exceptional_primes_for_selected_stack":
            [int(p) for p, e in ZZ(final_D).factor()],
        "scope": (
            "The EXACT exceptional primes for one-dimensional kernel of "
            "this fixed STACK of INTEGRAL Hecke matrices, not all mod-p "
            "modular symbols and NOT Sha, Fitt2 or strong BSD."
        )
    }
    encoded = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(encoded + b"\n")
    digest = sha256(encoded).hexdigest()
    print("HECKE_SMITH_FINAL_INTEGER", final_D, flush=True)
    print("HECKE_SMITH_FINAL_EXACT_EXCEPTIONAL_PRIMES",
          out["final_exact_exceptional_primes_for_selected_stack"], flush=True)
    print("HECKE_SMITH_CANONICAL_JSON_SHA256", digest, flush=True)
    print("HECKE_SMITH_REPORT", args.output, flush=True)
    print("BOUNDARY_CONGRUENCE_EIGENLINE_ONLY_NOT_SHA_OR_BSD", flush=True)


if __name__ == "__main__":
    main()
