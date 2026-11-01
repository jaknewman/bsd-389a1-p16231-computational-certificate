#!/usr/bin/env python3
"""Construct a p-INDEPENDENT exact modular-symbol vector for E=389a1.

Compute m^+(a/389), a=0,...,388, both from independently implemented
Sage and eclib algorithms in the SAME Neron-period normalization.
Compute the exact common denominator and the content (gcd) of the
integer-scaled vector, then SHA256-hash a canonical JSON transcript.

This is an actual rational arithmetic input independent of Sha and p.
It does NOT calculate a derived rank-two Euler system, does NOT imply
any bound on Selmer Fitt2, and is not the entire modular-symbol module.

Usage in Sage v10.9:
python -u verification/bsd389_fixed_rational_manin_content.py \
  --output ~/bsd389_fixed_rational_manin_content.json
"""
import argparse
import hashlib
import json
from math import gcd
from pathlib import Path

from sage.all import EllipticCurve, QQ, ZZ, lcm

N = 389


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path,
                    default=Path.home() /
                    "bsd389_fixed_rational_manin_content.json")
    ap.add_argument("--progress", type=int, default=100)
    args = ap.parse_args()

    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    assert ZZ(E.conductor()) == N and ZZ(E.discriminant()) == N
    assert E.real_components() == 2

    # eclib is independently normalized by its period convention.
    sage = E.modular_symbol(sign=+1, implementation="sage",
                            normalize="L_ratio")
    eclib = E.modular_symbol(sign=+1, implementation="eclib")
    values = []
    for a in range(N):
        cusp = QQ(a)/N
        left = QQ(sage(cusp))
        right = QQ(eclib(cusp))
        assert left == right, (
            "MODSYM_SAGE_ECLIB_CONVENTION_MISMATCH", a, left, right)
        values.append(left)
        if args.progress and (a+1) % args.progress == 0:
            print("FIXED_M389_PROGRESS", a+1, "/", N, flush=True)

    assert len(values) == N
    assert any(v for v in values)
    D = 1
    for val in values:
        D = lcm(D, ZZ(val.denominator()))
    integral = [ZZ(D * val) for val in values]
    g = 0
    for v in integral:
        g = gcd(g, abs(int(v)))
    assert g > 0
    # These 389 rational symbols, AND ONLY THESE, span the integer
    # content proven here; no theorem links it to Sha Fitt2.
    reduced = [int(x)//g for x in integral]
    assert gcd_of_vector(reduced) == 1
    bez_g, bez_coefs = bezout_vector([int(v) for v in integral])
    assert bez_g == g
    assert sum(z * int(v) for z,v in zip(bez_coefs,integral)) == g
    sparse_bezout = [[i,z] for i,z in enumerate(bez_coefs) if z]
    obj = {
        "curve": "389a1",
        "model": [0, 1, 1, -2, 0],
        "conductor": N,
        "sign": 1,
        "normalization": "Neron period / L_ratio, independently checked eclib",
        "cusp_denominator": N,
        "indices": "a=0..388",
        "count": len(values),
        "nonzero": sum(bool(v) for v in values),
        "denominator_lcm": int(D),
        "scaled_content_gcd": g,
        "bezout_identity_sparse": sparse_bezout,
        "primitive_vector": reduced,
        "raw_rational": [str(v) for v in values],
        "boundary": (
            "This is a fixed exact finite modular-symbol vector. "
            "Its unit content for primes excluding divisors of gD "
            "does not imply any Selmer Fitt2 or Sha-primary bound."
        )
    }
    canon = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    digest = hashlib.sha256(canon.encode("utf-8")).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(canon + "\n", encoding="utf-8")

    print("FIXED_M389_EXACT_ALL_SAGE_ECLIB_MATCH_PASS", len(values), flush=True)
    print("FIXED_M389_NONZERO_SYMBOLS", obj["nonzero"], flush=True)
    print("FIXED_M389_RATIONAL_DENOMINATOR_LCM", D, flush=True)
    print("FIXED_M389_INTEGRAL_SCALED_CONTENT", g, flush=True)
    print("FIXED_M389_PRIMITIVE_VECTOR_CONTENT_PASS", 1, flush=True)
    print("FIXED_M389_EXACT_BEZOUT_WITNESS_PASS",
          "gcd", g, "nonzero_coefficients", len(sparse_bezout), flush=True)
    print("FIXED_M389_EXACT_CANONICAL_JSON_SHA256", digest, flush=True)
    print("FIXED_M389_REPORT", args.output, flush=True)
    print("BOUNDARY_FIXED_MODULAR_SYMBOL_DATA_NOT_UNIFORM_SHA_FITTING_COMPARISON",
          flush=True)


def bezout_vector(values):
    """Construct an EXACT Z-linear combination of integer symbols equal to gcd."""
    d = 0
    coeffs = [0] * len(values)
    for i, v in enumerate(values):
        old_r, r = d, v
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
        if old_r < 0:
            old_r, old_s, old_t = -old_r, -old_s, -old_t
        coeffs = [old_s * z for z in coeffs]
        coeffs[i] += old_t
        d = old_r
    return d, coeffs


def gcd_of_vector(values):
    d = 0
    for v in values:
        d = gcd(d, abs(v))
    return d


if __name__ == "__main__":
    main()
