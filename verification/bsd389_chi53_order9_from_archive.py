#!/usr/bin/env python3
"""389a1 / K=Q(sqrt(-3)): recover the *order-nine* Gross-period witness.

Reads EXISTING files from previous quaternionic stages; does not recompute
Brandt ideals, Hecke matrices, embeddings or L-values.

The 18 states are indexed by successive powers of the same ideal class
(l_19).  Character: chi_9(l_19)=zeta_9 (or its inverse).
This is deliberately NOT the order-18 character.

Usage in Sage environment:
    python -u verification/bsd389_chi53_order9_from_archive.py
Optional: --orbit /path/to/bsd389_chi53_stage14_orbit19.json

Strict logical scope: verifies the archived finite Gross-orbit polynomial
and its nonvanishing.  The identification with an adelic toric period
depends on optimality / transport / Jacquet-Langlands conventions established
in separate stage-22/23/29/30 inputs.  Does not establish ord_T Theta=2
or p-primary Sha=0.
"""
import argparse
import hashlib
import json
from pathlib import Path
from sage.all import ZZ, QQ, PolynomialRing, cyclotomic_polynomial

BRANDT_EIGENVECTOR = [
    0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,
    2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0
]
EXPECTED_VALUES = [
    0,0,-1,0,0,-1,-1,2,2,-1,-1,2,2,-1,-1,0,0,-1
]

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--orbit", type=Path,
        default=Path.home()/"bsd389_chi53_stage14_orbit19.json")
    parser.add_argument("--output", type=Path,
        default=Path.home()/"bsd389_chi53_order9_period_from_archive.json")
    args = parser.parse_args()
    if not args.orbit.is_file():
        raise FileNotFoundError(
            f"Stage 14 file not found: {args.orbit}. "
            "Use --orbit with the archived stage14 JSON."
        )

    raw = args.orbit.read_bytes()
    orbit = json.loads(raw)
    assert orbit["status"] == "ORBIT_18_PASS", orbit.get("status")
    steps = orbit["steps"]
    assert len(steps) == 18
    assert len(BRANDT_EIGENVECTOR) == 33
    states = []
    for k, row in enumerate(steps):
        assert int(row["k"]) == k
        idx = int(row["index"])
        assert 0 <= idx < 33
        state = (idx, tuple(map(int, row["coefficients"])))
        states.append(state)
    assert len(set(states)) == 18
    for k, row in enumerate(steps):
        next_state = (
            int(row["next_index"]),
            tuple(map(int, row["next_coefficients"]))
        )
        assert next_state == states[(k + 1) % 18], (
            "ORBIT_CYCLE_MISMATCH", k, next_state, states[(k+1)%18]
        )

    coeffs = [int(BRANDT_EIGENVECTOR[idx]) for idx, _ in states]
    assert coeffs == list(map(int, orbit["values"]))
    assert coeffs == EXPECTED_VALUES
    print("CHI53_ARCHIVED_ORBIT_18_ORDERED_VALUES_PASS", coeffs, flush=True)

    R = PolynomialRing(QQ, "X")
    X = R.gen()
    F = sum(QQ(a) * X**j for j, a in enumerate(coeffs))
    phi9 = R(cyclotomic_polynomial(9))
    phi3 = R(cyclotomic_polynomial(3))
    remainder9 = F % phi9
    norm9 = ZZ(phi9.resultant(F))
    assert remainder9 == -3*X**5 - 3*X**4 + 3*X**3 - 3*X
    assert norm9 == 729
    assert F % phi3 == 0

    # Stronger exact result in Z[zeta_9]:
    # F(zeta_9) = -3*zeta_9*u, with u an explicit unit.
    u = X**4 + X**3 - X**2 + 1
    u_inverse = X**4 - X**3 - 1
    assert (u*u_inverse) % phi9 == 1
    assert remainder9 == (-3*X*u) % phi9

    # Tiny independent finite-field witness of F(zeta_9) != 0.
    # The residue 4 modulo 19 has multiplicative order 9.
    assert pow(4,9,19) == 1
    assert pow(4,3,19) != 1
    residue19 = sum(a*pow(4,j,19) for j,a in enumerate(coeffs)) % 19
    assert residue19 == 7

    print("CHI53_ORDER9_CYCLOTOMIC_REMAINDER", remainder9, flush=True)
    print("CHI53_ORDER9_CYCLOTOMIC_NORM", norm9, flush=True)
    print("CHI53_ORDER9_EXPLICIT_UNIT", u, flush=True)
    print("CHI53_ORDER9_EXPLICIT_UNIT_INVERSE", u_inverse, flush=True)
    print("CHI53_ORDER9_THREE_TIMES_UNIT_PASS", flush=True)
    print("CHI53_ORDER9_P_ADIC_UNIT_FOR_ALL_PRIMES_EXCEPT_3_PASS",flush=True)
    print("CHI53_ORDER9_MOD19_RESIDUE", residue19, flush=True)
    print("CHI53_ORDER3_PERIOD_ZERO_PASS", flush=True)
    print("CHI53_ORDER9_FORMAL_GROSS_PERIOD_NONZERO_PASS", flush=True)

    # Existing finite-input evidence, WITHOUT rerunning older calculations.
    p22 = Path.home()/"bsd389_chi53_stage22_adelic_right_ideals.json"
    p30 = Path.home()/"bsd389_chi53_stage30_hecke_sturm.json"
    evidence = {}
    if p22.exists():
        j22 = read_json(p22)
        assert j22["status"] == "RIGHT_IDEAL_TRANSPORT_PASS"
        assert len(j22["steps"]) == 18
        for k, rec in enumerate(j22["steps"]):
            assert int(rec["k"]) == k
            assert int(rec["source"]) == states[k][0]
            assert int(rec["destination"]) == states[(k+1)%18][0]
            assert rec["right_ideal_identity"] is True
            assert rec["embedding_identity"] is True
            assert rec["inverse_right_ideal_identity"] is True
        evidence["stage22"] = "ARCHIVED_IDENTITIES_PASS"
        print("CHI53_ARCHIVED_STAGE22_TRANSPORTS_CONSISTENT_PASS",flush=True)
    else:
        evidence["stage22"] = "JSON_NOT_PRESENT"
        print("CHI53_ARCHIVED_STAGE22_JSON_NOT_PRESENT",flush=True)

    if p30.exists():
        j30 = read_json(p30)
        assert j30["curve"] == "389a1"
        assert list(map(int,j30["brandt_vector"])) == BRANDT_EIGENVECTOR
        assert int(j30["right_column_nullity"]) == 1
        assert int(j30["sturm_bound"]) == 65
        assert j30["status"] == "STAGE30_HECkE_STURM_AND_MULTIPLICITY_ONE_PASS"
        evidence["stage30"] = "ARCHIVED_HECKE_EIGENLINE_PASS"
        print("CHI53_ARCHIVED_STAGE30_HECkE_EIGENLINE_CONSISTENT_PASS",flush=True)
    else:
        evidence["stage30"] = "JSON_NOT_PRESENT"
        print("CHI53_ARCHIVED_STAGE30_JSON_NOT_PRESENT",flush=True)

    report = {
        "status": "CHI53_ORDER9_FORMAL_GROSS_PERIOD_NONZERO_PASS",
        "curve": "389a1",
        "K": "Q(sqrt(-3))",
        "ring_class_conductor": 53,
        "ring_class_group_order": 18,
        "character_order": 9,
        "character_generator": "chi(l_19)=zeta_9",
        "orbit_source": str(args.orbit),
        "orbit_sha256": hashlib.sha256(raw).hexdigest(),
        "ordered_values": coeffs,
        "F_mod_Phi9": str(remainder9),
        "cyclotomic_norm": int(norm9),
        "explicit_unit": str(u),
        "explicit_unit_inverse": str(u_inverse),
        "p_adic_unit_for_all_rational_primes_except": [3],
        "residue_mod_19_at_4": int(residue19),
        "archived_evidence": evidence,
        "boundary": (
            "Finite algebraic orbit result. Global toric-period/Waldspurger "
            "application requires separately identified optimal Gross points "
            "and valid automorphic test-vector conventions; does not prove "
            "ord_T(Theta)=2, nonzero generalized Kato class, or Sha vanishing."
        )
    }
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",
                           encoding="utf-8")
    print("CHI53_ORDER9_REPORT", args.output, flush=True)
    print("BOUNDARY: theta(T) order=2 is NOT certified by this script",flush=True)

if __name__ == "__main__":
    main()
