#!/usr/bin/env python3
"""Prove [5+3omega] generates Pic(O_(16231^2)), via split CRT group."""
P=16231
M=P*P
r0,r1=49689135,213756225
h=P*(P-1)//3
assert h==87809710
assert (r0*r0+r0+1)%M==0 and (r1*r1+r1+1)%M==0
assert (r0*r1)%M==1 and (r0+r1+1)%M==0
w=((5+3*r0)*pow(5+3*r1,-1,M))%M
assert w==138112843 and w%P==3264
assert pow(w,3*h,M)==1
# For a cyclic ring-class group of order h, w has full quotient order
# iff w^(3h/q) !=1 mod p^2 for every prime divisor q of h.
for q in (2,5,541,P):
    assert h%q==0
    z3=pow(w,3*(h//q),M)
    assert z3!=1
    print("NORM19_FULL_RINGCLASS_ORDER_PRIME_DIVISOR_PASS",q,z3,flush=True)
assert pow(w,h,M) in (1,r0,r1)
print("NORM19_FULL_RINGCLASS_GENERATOR_PASS",h,flush=True)
# Teich(w) = w^p and w = Teich(w)*(1+p)^s mod p^2.
teich=pow(w,P,M)
unit=w*pow(teich,-1,M)%M
s=(-5415)%P
assert unit==pow(1+P,s,M)
assert pow(teich,P-1,M)==1
assert pow(unit,P,M)==1
print("NORM19_TEICH_COMPONENT_MOD_P2",teich,flush=True)
print("NORM19_PRINCIPAL_UNIT_U_EXPONENT_PASS",s,flush=True)
print("NORM19_FULL_RINGCLASS_CYCLIC_COORDINATES_PASS",5410,P,h,flush=True)
print("BOUNDARY_NO_QUATERNIONIC_19_NEIGHBOR_TRANSITION_PRODUCED",flush=True)
print("BOUNDARY_THETA_GLOBAL_C2_NOT_COMPUTED",flush=True)
