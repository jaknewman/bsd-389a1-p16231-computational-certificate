#!/usr/bin/env python3
"""Exact arithmetic checks for the Kim–Pollack p=3 389a1 example and
Chebotarev class counting. Does NOT recompute Kurihara delta nonvanishing."""
from fractions import Fraction

def ap(prime):
    assert prime >= 3 and prime % 2
    value=0
    for x in range(prime):
        v=(4*x*x*x+4*x*x-8*x+1)%prime
        if v:
            value += 1 if pow(v,(prime-1)//2,prime)==1 else -1
    return -value

p,q1,q2=3,79,109
assert ap(p)==-2
assert ap(q1)==-13 and ap(q2)==2
assert q1 % p==q2 % p==1
assert (ap(q1)-(q1+1))%p == 0
assert (ap(q2)-(q2+1))%p == 0
print("P3_KIM_PUBLISHED_PAIR_ADMISSIBILITY_PASS",q1,q2,"ap",ap(q1),ap(q2))
print("P3_KIM_KURIHARA_NONVANISHING_EXTERNAL_SOURCE_NOT_RECOMPUTED")

for ell in [3,5,7,11,17,107,599,16231]:
    gl2=(ell*ell-1)*(ell*ell-ell)
    unipotent=ell*ell
    dens=Fraction(unipotent,gl2)
    assert dens==Fraction(ell,(ell-1)**2*(ell+1))
    print("CHEBOTAREV_DENSITY_FORMULA_PASS",ell,str(dens))

print("STOP: admissibility density does not establish nonvanishing or BSD.")
