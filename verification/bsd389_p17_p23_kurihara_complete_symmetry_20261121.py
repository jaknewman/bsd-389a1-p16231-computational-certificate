#!/usr/bin/env python3
"""Complete two-prime Kurihara certificates for E389a1, p=17 and p=23.

Runs on Python 3 standard library. Reuses the frozen 390-entry integral
Manin vector and finite group law from the separately archived
bsd389_p11_three_kurihara_independent_standard_python_20261121.py.
That vector was formerly checked with genuine Sage/eclib samples,
but is NOT independently re-derived by the present program.

Uses a -> n-a plus-symbol symmetry; because q_i == 1 mod 2p,
both auxiliary discrete logarithms mod p are invariant under -1.
Hence 2 times the exact half-sum equals the full Kurihara number.

Output is authentic arithmetic evidence for specific prime components,
not a proof of global Sha finiteness or the complete BSD formula.
"""
import argparse
from hashlib import sha256
from pathlib import Path
from runpy import run_path

script = Path(__file__).with_name(
    "bsd389_p11_three_kurihara_independent_standard_python_20261121.py"
)
m = run_path(str(script), run_name="BSD389_IMPORT")
assert len(m["V"]) == 390
assert sha256(bytes(v+2 for v in m["V"])).hexdigest() == (
    "31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee"
)

# p, q1, q2, a_q1, a_q2, #E(F_p), expected rows Q/P, expected delta
DATA = {
    17: (1667, 5237, 19, 87, 24, 6, 12, 4),
    23: (1289, 3727, 25, 94, 28, 5, 12, 17),
}

def local_row(q, p, ap_expected):
    a = m["ap"](q)
    assert a == ap_expected
    N = q + 1 - a
    assert q % p == 1 and a % p == 2 and N % p == 0 and N % (p*p)
    P = m["mul"]((-1 % q, 1), N//p, q)
    Q = m["mul"]((0, -1 % q), N//p, q)
    assert P is not None and m["mul"](P, p, q) is None
    ratio = next((j for j in range(p) if m["mul"](P, j, q) == Q), None)
    assert ratio is not None
    return N, ratio

def verify(p):
    q1, q2, a1, a2, Np, expected1, expected2, delta = DATA[p]
    assert p+1-m["ap"](p) == Np and Np % p
    N1, row1 = local_row(q1, p, a1)
    N2, row2 = local_row(q2, p, a2)
    assert (row1, row2) == (expected1, expected2)
    assert (row2-row1) % p != 0
    assert (q1-1)//2 % p == (q2-1)//2 % p == 0
    g1, log1 = m["dlog"](q1, p)
    g2, log2 = m["dlog"](q2, p)
    n = q1*q2
    moments = [0, 0, 0, 0]
    checked = 0
    samples = (1, 2, 3, 7, 23, 199, 1000, 10007, 50001)
    for a in range(1, n//2 + 1):
        b, c = a % q1, a % q2
        if b == 0 or c == 0:
            continue
        v = m["manin"](a, n, p)
        u, w = log1[b], log2[c]
        moments[0] = (moments[0] + v) % p
        moments[1] = (moments[1] + u*v) % p
        moments[2] = (moments[2] + w*v) % p
        moments[3] = (moments[3] + u*w*v) % p
        if a in samples:
            assert m["manin"](n-a, n, p) == v
            assert log1[(-a) % q1] == u and log2[(-a) % q2] == w
        checked += 1
    assert 2*checked == (q1-1)*(q2-1)
    moments = [2*x % p for x in moments]
    assert moments == [0, 0, 0, delta], (p, moments)
    print(
        "BSD389_KURIHARA_NEW_PRIME_PASS", "p", p,
        "q", (q1, q2), "a_q", (a1, a2),
        "E_Fq", (N1, N2), "local_rows", (row1, row2),
        "det", (row2-row1) % p, "roots", (g1, g2),
        "half_units", checked, "all_units", 2*checked,
        "moments_mod_p", moments, flush=True
    )
    return moments

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, choices=tuple(DATA))
    args = parser.parse_args()
    for p in ((args.p,) if args.p else tuple(DATA)):
        verify(p)
    print("BOUNDARY: p-specific Kurihara arithmetic, not a uniform Sha bound.")
