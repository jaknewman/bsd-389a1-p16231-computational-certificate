# Sage 10.9 preflight for Stein's published rank-two Heegner derivative witness
# Stein, Heegner Points on Rank Two Elliptic Curves (2009), Theorem 2.7
# and Table 3.2: E=389a1, D=-7, q=p=3, ell=5, c=41.
#
# CRITICAL: arithmetic preflight ONLY. This code DOES NOT compute the
# quaternionic Heegner derivative z_(c,sigma,ell), nor prove it nonzero.
# Paper: https://wstein.org/misc/sagedays18_papers/stein-heegner_points_on_rank_two_elliptic_curves.pdf

from sage.all import *

E = EllipticCurve('389a1')
D, p, ell, c = ZZ(-7), ZZ(3), ZZ(5), ZZ(41)
assert E.conductor() == 389
assert E.ainvs() == (0, 1, 1, -2, 0)
print("HEEGNER_CURVE_AND_CONDUCTOR_PASS", flush=True)

assert D.is_fundamental_discriminant()
assert kronecker(D, ZZ(389)) == 1
assert kronecker(D, c) == -1
assert kronecker(D, ell) == -1
print("HEEGNER_SPLIT_389_INERT_C41_ELL5_PASS", flush=True)

a_c = E.ap(c)
assert a_c == -3
assert a_c % p == 0 and (c+1) % p == 0
print("HEEGNER_KOLYVAGIN_C41_ADMISSIBLE_PASS", a_c, flush=True)

Nell = E.change_ring(GF(ell)).cardinality()
assert Nell == 9 and Nell % p == 0
print("HEEGNER_LOCAL_ELL5_GROUP_ORDER_PASS", Nell, flush=True)

print("HEEGNER_P3_ARITHMETIC_PREFLIGHT_PASS", flush=True)
print("BOUNDARY_STEIN_TABLE_NONVANISHING_NOT_RECOMPUTED", flush=True)
print("BOUNDARY_SHA3_NOT_INDEPENDENTLY_CERTIFIED_BY_THIS_SCRIPT", flush=True)
