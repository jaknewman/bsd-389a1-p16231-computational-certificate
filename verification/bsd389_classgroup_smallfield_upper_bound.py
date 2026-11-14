#!/usr/bin/env python3
"""Exact numeric sanity checks for the proved O(p²) Sha[p]-rank upper.

No class group, Selmer group or global BSD is computed here. Actual
mathematical proof uses class-field descent, Serre local different
bound, Minkowski and elementary ideal counting. See companion paper.
"""
from math import isqrt, log, sqrt

def isprime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def audit(p):
    assert isprime(p) and p>=5 and p not in (97,389)
    n=p*p-1
    if p>=41:a,b=2,3
    elif p>=7:a,b=3,3
    else:a,b=4,4
    # Every ideal class of the degree-n character field has a
    # representative of norm below (2sqrt389*p)**n.
    assert 2*sqrt(389)*p < p**a
    # H_{p^(an)}<p^b is proven for ALL eligible p by ln p
    # bounds; this finite sample merely tests the inequality.
    assert 1+a*n*log(p)<p**b
    # h(L)<p^(a*n+b*(n-1)); parity improves the Sha[p] bound.
    vp_upper=a*n+b*(n-1)-1
    dim_sha_upper=vp_upper-1
    dim_sha_upper-=dim_sha_upper%2
    expected=({5:8}.get(p,6 if p<41 else 5))*n-6
    assert dim_sha_upper==expected
    print("SMALL_FIELD_MINKOWSKI_SHA_P_RANK_UPPER_PASS",
          p,"field_degree",n,"vp_class_number_upper",vp_upper,
          "dim_Sha_p_upper",dim_sha_upper)

for p in (5,7,11,13,17,19,23,29,31,37,41,43,47,107,599,16231):
    audit(p)
print("STRONG_GAP: vp(h(L_p))<=2 WOULD FORCE Sha[p^infty]=0")
print("NO ACTUAL FIELD CLASS NUMBER OR ALL_LARGE_p_SHA_VANISHING PROVED")
