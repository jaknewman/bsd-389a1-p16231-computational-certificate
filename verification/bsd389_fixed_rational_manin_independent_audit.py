#!/usr/bin/env python3
"""Independently audit the immutable 389-cusp rational modular-symbol JSON.

This script needs only the Python standard library. It DOES NOT call
Sage, eclib, or Sha or use the original exporter's gcd/Bezout code.

Authenticates the user-reported SHA256, checks exactly 389 fractions,
reconstructs common denominator, integer vector, content gcd, exact
integer Bezout witness, and all plus-symbol evenness relations
a <-> -a mod 389. Prints the two witness cusp indices and coefficients.

Usage:
  python -u verification/bsd389_fixed_rational_manin_independent_audit.py \
    --input ~/bsd389_fixed_rational_manin_content.json
"""

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, lcm
from pathlib import Path


N = 389
EXPECTED_SHA = (
    "9719d0863045ef63fe3519b23da0c4bb74303ee3d84cb9791f95e2a29d456dd4"
)


def content_gcd(values):
    current = 0
    for value in values:
        current = gcd(current, abs(value))
    return current


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--input", type=Path,
        default=Path.home() / "bsd389_fixed_rational_manin_content.json",
    )
    ap.add_argument("--expected-sha", default=EXPECTED_SHA)
    args = ap.parse_args()

    raw = args.input.read_bytes()
    obj = json.loads(raw)
    canon = json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    digest = hashlib.sha256(canon).hexdigest()
    assert raw == canon + b"\n", "NOT_CANONICAL_ONE_LINE_JSON"
    assert digest == args.expected_sha, (
        "CANONICAL_JSON_SHA256_MISMATCH", digest, args.expected_sha
    )
    assert obj["curve"] == "389a1"
    assert obj["model"] == [0, 1, 1, -2, 0]
    assert obj["conductor"] == N
    assert obj["sign"] == 1
    assert obj["cusp_denominator"] == N
    assert obj["indices"] == "a=0..388"
    assert obj["count"] == N
    values = [Fraction(x) for x in obj["raw_rational"]]
    assert len(values) == N
    assert sum(x != 0 for x in values) == obj["nonzero"] == 228

    D = 1
    for x in values:
        D = lcm(D, x.denominator)
    assert D == obj["denominator_lcm"] == 1
    integers = [int(D * x) for x in values]
    assert all(Fraction(z, D) == x for z, x in zip(integers, values))
    g = content_gcd(integers)
    assert g == obj["scaled_content_gcd"] == 1
    primitive = [z // g for z in integers]
    assert primitive == obj["primitive_vector"]
    assert content_gcd(primitive) == 1

    # The original modular symbol has sign +1; it is invariant under
    # the involution a -> -a modulo 389. Check independently from JSON.
    # This audits the captured plus-symbol property, not a Selmer theorem.
    for a in range(N):
        assert values[a] == values[(-a) % N], (
            "PLUS_EVENNESS_FAIL", a, values[a], values[(-a) % N]
        )

    pairs = obj["bezout_identity_sparse"]
    assert isinstance(pairs, list)
    assert len(pairs) == 2, ("EXPECTED_TWO_TERM_WITNESS", len(pairs))
    seen = set()
    summation = 0
    for row in pairs:
        assert isinstance(row, list) and len(row) == 2
        idx, coeff = row
        assert type(idx) is int and type(coeff) is int
        assert 0 <= idx < N and idx not in seen and coeff != 0
        seen.add(idx)
        summation += coeff * integers[idx]
    assert summation == g == 1, ("BEZOUT_IDENTITY_INVALID", summation)

    print("FIXED_M389_INDEPENDENT_CANONICAL_JSON_SHA256_PASS", digest, flush=True)
    print("FIXED_M389_INDEPENDENT_389_FRACTIONS_PASS", len(values), flush=True)
    print("FIXED_M389_INDEPENDENT_NONZERO_COUNT_PASS", obj["nonzero"], flush=True)
    print("FIXED_M389_INDEPENDENT_DENOMINATOR_CONTENT_PASS",
          "D", D, "g", g, flush=True)
    print("FIXED_M389_INDEPENDENT_PLUS_EVENNESS_PASS",
          "comparisons", N, flush=True)
    for idx, coeff in pairs:
        print(
            "FIXED_M389_INDEPENDENT_BEZOUT_TERM",
            "a", idx, "symbol", integers[idx], "coefficient", coeff,
            flush=True
        )
    print("FIXED_M389_INDEPENDENT_BEZOUT_SUM_PASS", summation, flush=True)
    print("FIXED_M389_ALL_PRIMES_NONZERO_FIXED_SYMBOL_VECTOR_PASS", flush=True)
    print("BOUNDARY_NO_TWO_PRIME_KURIHARA_OR_SHA_FITTING_IMPLICATION", flush=True)


if __name__ == "__main__":
    main()
