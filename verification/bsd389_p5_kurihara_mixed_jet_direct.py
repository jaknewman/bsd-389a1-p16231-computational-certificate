#!/usr/bin/env python3
"""Independent small p=5 Mazur–Tate mixed-jet audit for E=389a1.

An intentionally tiny **real arithmetic** follow-up to the all-prime
m_E^+(7/389)=-1 certificate, which alone does NOT control Sha.

Uses q1=41, q2=61, p=5, primitive roots (6,2), n=2501.
Computes 1200 independent eclib sign-plus modular symbols
at cusps a/n (not a/389) and fills the 1200 negatives via
m^+(-r)=m^+(r). Validates 24 samples against Sage's *independent*
modular-symbol implementation; 2400 CRT unit positions are audited.

Exact checks:
  * CRT / roots / +/- involution / distinct sources.
  * Direct double Kurihara weighted sum = coefficient [TU] Theta(1+T,1+U).
  * Anchored mixed-difference formula.
  * Unweighted/one-direction first jets separately reported (no guess).
  * Change-of-primitive-roots transforms delta by p-adic unit.
  * Rank of mixed-difference matrix over F_5 as a new structural probe.
  * Existing reported p5 delta=4, but no claim of a *new* witness
    before this program is genuinely user-executed.

This proves NOTHING for untested primes and does not imply all-prime
Sha finiteness, full BSD, or m2(p)=0 for arbitrary p.

Run:
 python -u verification/bsd389_p5_kurihara_mixed_jet_direct.py
"""
from sage.all import EllipticCurve, QQ, GF, matrix
import math

P, Q1, Q2 = 5, 41, 61
N = Q1 * Q2
G1, G2 = 6, 2
H1, H2 = Q1-1, Q2-1
EXPECTED_DELTA = 4


def primitive_powers(g, q):
    powers = [pow(g, k, q) for k in range(q-1)]
    assert len(set(powers)) == q-1 and powers[0] == 1
    return powers


def crt_unit(x, y):
    a = x + Q1 * (((y-x)*pow(Q1, -1, Q2)) % Q2)
    assert 1 <= a < N and a % Q1 == x and a % Q2 == y
    assert math.gcd(a, N) == 1
    return a


def mod_rational(frac):
    r = QQ(frac)
    den = int(r.denominator())
    assert den % P, ("NON_P_INTEGRAL_SYMBOL", r)
    return int(r.numerator()) * pow(den, -1, P) % P


def ff_rank(rows, p):
    # Independent hand-coded Gaussian elimination over F_p.
    a = [[v % p for v in row] for row in rows]
    nrows, ncols = len(a), len(a[0])
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, nrows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [v*inv % p for v in a[rank]]
        for i in range(rank+1, nrows):
            x = a[i][col]
            if x:
                a[i] = [(a[i][j]-x*a[rank][j])%p
                        for j in range(ncols)]
        rank += 1
        if rank == nrows:
            break
    return rank


def main():
    assert (P,Q1,Q2,N,G1,G2) == (5,41,61,2501,6,2)
    assert H1 % P == H2 % P == 0
    assert (H1//2) % P == (H2//2) % P == 0
    xs = primitive_powers(G1,Q1)
    ys = primitive_powers(G2,Q2)
    E = EllipticCurve(QQ,[0,1,1,-2,0])
    assert int(E.conductor()) == 389
    m_eclib = E.modular_symbol(sign=+1,implementation="eclib")
    m_sage = E.modular_symbol(sign=+1,implementation="sage",normalize="L_ratio")

    f = [[None for _ in range(H2)] for _ in range(H1)]
    independent_eclib = 0
    sage_comparisons = 0
    # 24 comparisons spaced deterministically across the first 1200
    sample_indices = set(range(0,1200,50))
    for k in range(H1):
        for ell in range(H2):
            if f[k][ell] is not None:
                continue
            a = crt_unit(xs[k],ys[ell])
            value = mod_rational(m_eclib(QQ(a)/N))
            neg_k = (k+H1//2)%H1
            neg_ell = (ell+H2//2)%H2
            assert crt_unit(xs[neg_k],ys[neg_ell]) == N-a
            f[k][ell] = value
            assert f[neg_k][neg_ell] is None
            f[neg_k][neg_ell] = value
            if independent_eclib in sample_indices:
                actual = mod_rational(m_sage(QQ(a)/N))
                assert actual == value, ("SAGE_ECLIB_MISMATCH",a,value,actual)
                sage_comparisons += 1
            independent_eclib += 1
            if independent_eclib % 200 == 0:
                print("P5_MIXED_JET_PROGRESS", independent_eclib,
                      "/",H1*H2//2,flush=True)
    assert independent_eclib == 1200 and sage_comparisons == 24
    assert all(v is not None for row in f for v in row)
    print("P5_ALL_2400_CRT_UNITS_SYMMETRIC_COMPLETE_PASS",
          "eclib_evaluations", independent_eclib,
          "direct_independent_sage_samples", sage_comparisons,flush=True)

    # The four lowest moments are exactly the coefficients of
    # 1,T,U,TU in Theta_{n}(1+T,1+U) over F_p.
    m00 = m10 = m01 = m11 = 0
    for k in range(H1):
        for ell in range(H2):
            v = f[k][ell]
            m00 += v
            m10 += k*v
            m01 += ell*v
            m11 += k*ell*v
    m00,m10,m01,m11 = [v%P for v in (m00,m10,m01,m11)]
    print("P5_THETA_LOWEST_MOMENTS", "M00",m00,
          "M10",m10,"M01",m01,"M11",m11,flush=True)

    # Mixed anchor differences: all functions u(k)+v(ell) cancel.
    f00 = f[0][0]
    diffs = [[(f[k][ell]-f[k][0]-f[0][ell]+f00)%P
              for ell in range(H2)] for k in range(H1)]
    assert all(v == 0 for v in diffs[0])
    assert all(row[0] == 0 for row in diffs)
    mixed = sum(k*ell*diffs[k][ell]
                for k in range(H1) for ell in range(H2))%P
    assert mixed == m11, ("MIXED_DIFFERENCE_IDENTITY_FAIL",mixed,m11)
    mixed_rank = ff_rank(diffs,P)
    nonzero_diffs = sum(v != 0 for row in diffs for v in row)
    print("P5_MIXED_ANCHORED_JET_PASS","direct",m11,
          "difference",mixed,"matrix_rank",mixed_rank,
          "nonzero_mixed_entries",nonzero_diffs,flush=True)

    # New generators are g1^3 and g2^11.
    # Their log-coordinate factors relative to the originals are
    # 3^{-1} mod 40 and 11^{-1} mod 60.
    assert math.gcd(3,H1)==math.gcd(11,H2)==1
    translated = sum(
        k*ell*f[(3*k)%H1][(11*ell)%H2]
        for k in range(H1) for ell in range(H2))%P
    scale = (pow(3,-1,H1)*pow(11,-1,H2))%P
    assert translated == (scale*m11)%P
    print("P5_PRIMITIVE_ROOT_CHANGE_UNIT_SCALING_PASS",
          "old",m11,"new",translated,"factor",scale,flush=True)

    assert m11 == EXPECTED_DELTA, ("HISTORICAL_DELTA_MISMATCH",
                                   m11,EXPECTED_DELTA)
    print("P5_INDEPENDENT_DIRECT_KURIHARA_DELTA_MATCH_PASS",
          "p",P,"n",N,"delta_mod_p",m11,flush=True)
    print("BOUNDARY_P5_ONLY_NO_UNIFORM_TWO_PRIME_NONVANISHING",
          flush=True)


if __name__=="__main__":
    main()
