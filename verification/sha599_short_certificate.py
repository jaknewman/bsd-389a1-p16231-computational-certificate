#!/usr/bin/env python3
"""Bounded-memory p=599 finite moment and conditional analytic-bridge audit.

Requires authentic Manin table pinned by SHA256. Does NOT evaluate all
units at level p^3 or execute Sage p_primary_bound(599). The derived
analytic residue depends on the documented Hecke and precision lemmas.
See verification/README_sha599.md for the proof obligation and status.
"""
import argparse
import hashlib
import math
from pathlib import Path
import time

P = 599
N = P * P
LEVEL = 389
EXPECTED_HASH = "fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8"
EXPECTED_HEADER = [599, 6912461, 13963889]
EXPECTED_C = (0, 0, 543)
EXPECTED_PAIRS = 179101
EXPECTED_EDGES = 1924081
EXPECTED_CHECKSUM = 779927018
MOD_CHECKSUM = 1000000007


def assert_lift_identities(prime):
    """Weights of j and all j+p*t lifts, congruence mod p^2."""
    assert prime >= 5 and all(prime % q for q in range(2, math.isqrt(prime)+1))
    assert sum(j*(j-1)//2 for j in range(prime)) % prime == 0
    for j in range(prime):
        lhs = sum((j+t*prime)*(j+t*prime-1)//2 for t in range(prime))
        rhs = prime * (j*(j-1)//2)
        assert (lhs-rhs) % (prime*prime) == 0


def parse_table(path):
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == EXPECTED_HASH, f"Manin table SHA256 mismatch: {digest}"
    seq = list(map(int, raw.split()))
    assert len(seq) == 393, f"Expected 393 integers; found {len(seq)}"
    assert seq[:3] == EXPECTED_HEADER
    vals = seq[3:]
    assert len(vals) == 390 and all(0 <= v < P for v in vals)
    return vals, digest


def raw_modular_symbol(a, n, M, inverses):
    """Signed full-convergent rational path; independent of optimized kernel."""
    pn, pd, ln, ld = 1, 0, 0, 1
    x, y = n, a
    value = M[389]
    sign = -1
    edges = 0
    while y:
        q, r = divmod(x, y)
        x, y = y, r
        nn, nd = q*ln+pn, q*ld+pd
        if sign == 1:
            c, d = ld % LEVEL, nd % LEVEL
        else:
            c, d = nd % LEVEL, ld % LEVEL
        idx = 389 if c == 0 else (d*inverses[c]) % LEVEL
        value = (value + sign*M[idx]) % P
        pn, pd, ln, ld = ln, ld, nn, nd
        sign = -sign
        edges += 1
    assert x == 1 and ln == a and ld == n
    return value, edges


def compute_level_p2(table, progress):
    M, digest = parse_table(table)
    print("MANIN_TABLE_SHA256", digest, flush=True)
    inv = [0]*LEVEL
    for c in range(1, LEVEL):
        inv[c] = pow(c, -1, LEVEL)
    bucket = [0]*P
    C0 = C1 = C2 = 0
    edgecount = checksum = pairs = 0
    tic = time.monotonic()
    for a in range(1, (N-1)//2+1):
        if a % P == 0:
            continue
        t = pow(a, P-1, N)
        assert t % P == 1
        k = (-((t-1)//P)) % P
        assert (pow(a, P, N)*(1+P*k)) % N == a
        v, edges = raw_modular_symbol(a, N, M, inv)
        edgecount += edges
        bucket[a % P] = (bucket[a % P]+v) % P
        bucket[-a % P] = (bucket[-a % P]+v) % P
        C0 = (C0+2*v) % P
        C1 = (C1+2*v*k) % P
        C2 = (C2+v*k*(k-1)) % P
        checksum = (checksum + a*v + k*k) % MOD_CHECKSUM
        pairs += 1
        if progress and pairs % progress == 0:
            print("P599_FINITE_PROGRESS", pairs, "/", EXPECTED_PAIRS,
                  "sec", round(time.monotonic()-tic, 2), flush=True)
    assert pairs == EXPECTED_PAIRS, pairs
    assert edgecount == EXPECTED_EDGES, edgecount
    assert checksum == EXPECTED_CHECKSUM, checksum
    assert (C0, C1, C2) == EXPECTED_C, (C0, C1, C2)
    assert all(b == 0 for b in bucket[1:]), "Hecke fibres failed"
    print("P599_LEVEL_P2_INDEPENDENT_PASS", "C0", C0, "C1", C1,
          "C2", C2, "pairs", pairs, "edges", edgecount,
          "checksum", checksum, flush=True)
    return C2


def arithmetic_sage_gate(f0):
    from sage.all import EllipticCurve, QQ, ZZ, log
    from sage.libs.eclib.newforms import ECModularSymbol
    E = EllipticCurve(QQ, [0, 1, 1, -2, 0])
    p = ZZ(P)
    assert E.conductor() == 389 and E.discriminant() == 389
    assert E.ap(p) == 0 and E.is_supersingular(p)
    assert E.real_components() == 2
    assert E.rank(proof=True) == 2
    G = E.gens(proof=True)
    assert len(G) == 2 and E.gens_certain()
    assert E.torsion_order() == 1
    assert list(E.tamagawa_numbers()) == [1]
    assert E.galois_representation().is_surjective(p)
    M = E.modular_symbol(sign=1, implementation='eclib')
    Nsym = ECModularSymbol(E, sign=1)
    assert M._scaling == 1
    for d in (5, 41, 599):
        assert M(QQ(1)/d) == Nsym(QQ(1)/d)
    reg = E.padic_regulator(p, prec=6)
    K = reg[0].parent()
    lg = log(K(1+p))
    normalized = [reg[i]/lg**2 for i in range(2)]
    assert normalized[0].valuation() == 0
    assert normalized[1].valuation() >= 1
    b = int(ZZ(normalized[0].residue()))
    assert b == 571 and f0 == b
    print("SAGE_ARITHMETIC_GATES_PASS", "rank", 2,
          "generators", str(G), "surjective", True,
          "regulator_0_modp", b,
          "regulator_1_val", normalized[1].valuation(), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--table", type=Path, required=True)
    parser.add_argument("--sage", action="store_true")
    parser.add_argument("--progress", type=int, default=25000)
    args = parser.parse_args()
    print("SHA599_SHORT_CERTIFICATE_START", flush=True)
    for q in (5, 7, 11, P):
        assert_lift_identities(q)
    print("LIFT_WEIGHT_IDENTITIES_PASS", flush=True)
    c2 = compute_level_p2(args.table, args.progress)
    # Derived from Hecke A3 == 0 (mod p), lifts B3/p == C2 (mod p),
    # and Frobenius. This does not itself compute level-p^3 symbols.
    f0 = (-(P-1)*c2*pow(2*(P+1)**2, -1, P)) % P
    f1 = 0
    assert f0 == 571 and (2*f0-c2) % P == 0
    print("ANALYTIC_FROBENIUS_DERIVED", "F0_modp", f0,
          "F1_modp", f1, "kind", "HECKE_PLUS_PRECISION_LEMMA", flush=True)
    print("PRECISION_NOTE", "alpha-adic O(alpha^-1): G_error in Zp,",
          "H_error in p^-1 Zp; Frobenius projection kills mod p", flush=True)
    if args.sage:
        arithmetic_sage_gate(f0)
    else:
        print("SAGE_ARITHMETIC_GATES_NOT_RUN", flush=True)
    print("KATO_THEOREM_APPLICATION",
          "Stein-Wuthrich Algorithm 11.1; mathematical review required", flush=True)
    print("BOUNDARY",
          "Not a direct p_primary_bound computation; Hecke/projection and",
          "theorem applicability require independent mathematical audit", flush=True)
    print("SHA599_SHORT_CERTIFICATE_FINISHED", flush=True)


if __name__ == "__main__":
    main()
