#!/usr/bin/env python3
"""Exact p=5 algebraic obstruction to inferring two-prime Kurihara nonvanishing.

Construct a synthetic 40x60 F5 distribution with ALL favorable *structural*
properties seen for real E=389a1 q=(41,61):
  - simultaneous sign-plus symmetry (k,l)->(k+20,l+30),
  - an F5-unit sampled value f(1,1)=4,
  - all five Hecke-forced degree<=2 pure/marginal jets ZERO,
  - MAXIMAL rank 39 of the anchored mixed-difference matrix,
BUT the actual weighted mixed coefficient M11 = sum k*l*f(k,l) is ZERO.

Construction: choose deterministic, sign-symmetric g1,g2, set
     f = (1-shift_k)^3 g1 + (1-shift_l)^3 g2 mod 5.
The third difference in one variable annihilates ALL
degree<=2 polynomial test weights in that variable, including k*l.
The other variable supplies a generic mixed matrix, of maximal rank.

This counterexample is NOT the genuine E eigensymbol, and is NOT a
counterexample to BSD, a Hecke eigenrelation at higher levels,
or Kim's theorem. It disproves only an inference from these
*marginal-jet/rank/symmetry/unit* properties alone.
"""
from hashlib import sha256

P, H1, H2 = 5, 40, 60


def symmetric_seed(seed):
    out = [[0] * H2 for _ in range(H1)]
    for k in range(H1 // 2):
        for l in range(H2):
            v = sha256(f"{seed}:{k}:{l}".encode("utf-8")).digest()[0] % P
            out[k][l] = v
            out[k + H1 // 2][(l + H2 // 2) % H2] = v
    return out


def difference3_k(g, k, l):
    return (g[k][l] - 3 * g[(k-1) % H1][l]
            + 3 * g[(k-2) % H1][l] - g[(k-3) % H1][l]) % P


def difference3_l(g, k, l):
    return (g[k][l] - 3 * g[k][(l-1) % H2]
            + 3 * g[k][(l-2) % H2] - g[k][(l-3) % H2]) % P


def gaussian_rank_modp(matrix):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for j in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][j] % P), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][j], -1, P)
        a[rank] = [v * inverse % P for v in a[rank]]
        for i in range(rank+1, rows):
            coefficient = a[i][j]
            if coefficient:
                a[i] = [(a[i][c] - coefficient*a[rank][c]) % P
                        for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def main():
    g1, g2 = symmetric_seed("A0"), symmetric_seed("B0")
    f = [[(difference3_k(g1, k, l) + difference3_l(g2, k, l)) % P
          for l in range(H2)] for k in range(H1)]
    for k in range(H1):
        for l in range(H2):
            assert f[k][l] == f[(k+H1//2) % H1][(l+H2//2) % H2]
    assert f[1][1] == 4
    print("P5_TOY_SIGN_PLUS_AND_UNIT_SAMPLE_PASS",
          "f_1_1", f[1][1], "entries", H1*H2, flush=True)

    zero_jets = [
        sum(f[k][l] for k in range(H1) for l in range(H2)) % P,
        sum(k*f[k][l] for k in range(H1) for l in range(H2)) % P,
        sum((k*(k-1)//2)*f[k][l]
            for k in range(H1) for l in range(H2)) % P,
        sum(l*f[k][l] for k in range(H1) for l in range(H2)) % P,
        sum((l*(l-1)//2)*f[k][l]
            for k in range(H1) for l in range(H2)) % P,
    ]
    assert zero_jets == [0]*5
    print("P5_TOY_ALL_FIVE_HECKE_MARGINAL_JETS_ZERO_PASS",
          "M00_M10_M20_M01_M02", zero_jets, flush=True)

    anchored = [[(f[k][l]-f[k][0]-f[0][l]+f[0][0]) % P
                 for l in range(H2)] for k in range(H1)]
    assert all(v == 0 for v in anchored[0])
    assert all(row[0] == 0 for row in anchored)
    rank = gaussian_rank_modp(anchored)
    assert rank == H1-1 == 39
    print("P5_TOY_MIXED_ANCHORED_MATRIX_MAXIMAL_RANK_PASS",
          "rank", rank, "max", H1-1, flush=True)

    m11 = sum(k*l*f[k][l] for k in range(H1)
              for l in range(H2)) % P
    from_anchored = sum(k*l*anchored[k][l] for k in range(H1)
                        for l in range(H2)) % P
    assert m11 == from_anchored == 0
    print("P5_TOY_FULL_RANK_AND_ALL_PURE_JETS_YET_M11_ZERO_PASS",
          "actual_M11", m11,
          "direct_mixed_contraction", from_anchored,
          "unit_sample", f[1][1], flush=True)
    print("BOUNDARY_SYNTHETIC_FUNCTION_NOT_REAL_EIGENSYMBOL_OR_SHA",
          flush=True)


if __name__ == "__main__":
    main()
