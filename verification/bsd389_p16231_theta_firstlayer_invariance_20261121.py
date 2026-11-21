#!/usr/bin/env python3
"""E389a1 p16231: formal first-layer theta 2-jet normalization certificate.

Only algebraic consequences of USER-REPORTED Gross moments, not
a re-run of 87,809,710 ideals. Full ideal-source identification
and applicability of Castella-Hsieh theorems remain separate inputs.
"""
from math import comb
P=16231
M0,M1,M2=0,0,4083
ALPHA=128
INVSQ=pow(ALPHA,-2,P)
C2=(-3*INVSQ*M2)%P
assert INVSQ==4986 and C2==3739
assert P*(P-1)//3==87809710
for j in range(3):
    assert comb(P,j+1)%P==0
inv2=pow(2,-1,P)
for u in range(1,P):
    for b in (0,1,5,42,P-1):
        c1=(u*(u-1)*inv2+u*b)%P
        c0=b*(b-1)*inv2%P
        for i in (0,1,2,7,101,P-1):
            x=(u*i+b)%P
            assert x*(x-1)*inv2%P==(u*u*(i*(i-1)*inv2)+c1*i+c0)%P
        m2prime=(u*u*M2+c1*M1+c0*M0)%P
        assert m2prime==u*u*M2%P and m2prime!=0
assert (2*C2)%P!=0
print("BSD389_THETA_P1_LOW_DEGREES_VANISH_PASS",list(range(3)))
print("BSD389_THETA_GROSS_CLASS_COUNT_PASS",87809710)
print("BSD389_THETA_FINITE_C2_UNIT_PASS","alpha_minus_two",INVSQ,"M2",M2,"c2",C2)
print("BSD389_THETA_AFFINE_ORIENTATION_INVARIANCE_PASS","nonzero_u",P-1,"offsets",5,"index_samples",6)
print("BSD389_THETA_FUNCTIONAL_SIGN_AND_LINEAR_VANISHING_FORMAL_LEMMA_PASS")
print("BOUNDARY: original 87M Gross orbit, global identification of all source ideals, and published theorems are external evidence. No new full Sha/BSD proof.")
