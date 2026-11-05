#!/usr/bin/env python3
"""Verify exact arithmetic inputs for the Chida-Hsieh sign/projection bridge.
This does not replace proving that the actual Gross normalization matches.
"""
from sage.all import EllipticCurve, ZZ
E=EllipticCurve("389a1")
p=ZZ(16231)
assert E.conductor()==389
assert E.ap(p)==128 and E.ap(p)%p!=0
assert E.root_number()==1 and E.root_number(p)==1
assert ZZ(389)%3==2 and p%3==1
assert pow(128,-2,int(p))==4986
assert (-3*4986*4083)%int(p)==3739
assert E.torsion_order()==1
print("BSD389_P16231_ORDINARY_AND_ROOT_SIGN_PASS")
print("BSD389_K_MINUS3_389_INERT_P_SPLIT_PASS")
print("BSD389_NPLUS_ONE_POSITIVE_THETA_INVOLUTION_SIGN_PASS")
print("BSD389_P2_THETA_FINITE_C2_MODP",3739)
print("BOUNDARY_REQUIRE_CHIDA_HSIEH_THETA_NORMALIZATION_IDENTIFICATION")
print("BOUNDARY_ANALYTIC_CONSTANT_ZERO_AND_THEOREM_B_HYPOTHESES_REQUIRE_ARGUMENT")
