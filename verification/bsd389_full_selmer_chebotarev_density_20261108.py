#!/usr/bin/env python3
"""Exact GL2(Fp) density checks for full-Selmer Chebotarev sampling.
Does NOT compute the actual p-Selmer, Kurihara numbers, or BSD.
"""
from fractions import Fraction

def check(p, d):
    unip = 0
    nontrivial = 0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for z in range(p):
                    if (a*z-b*c) % p == 1 and (a+z) % p == 2:
                        unip += 1
                        if (a,b,c,z) != (1,0,0,1):
                            nontrivial += 1
    assert unip == p*p
    assert nontrivial == p*p-1
    gl2 = (p*p-1)*p*(p-1)
    translations = p**d*(p-1)
    density = Fraction(nontrivial*translations, gl2*p**(2*d))
    assert density == Fraction(1,p**(d+1))
    print('SELMER_CHEBOTAREV_DENSITY_PASS',p,d,str(density))

for p in (3,5,7,11,17):
    for d in (2,3,4):
        check(p,d)
print('LIMIT: does not determine dim Sel_p or prove Sha[p]=0')
