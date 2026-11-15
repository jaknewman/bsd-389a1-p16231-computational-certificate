#!/usr/bin/env python3
"""E389a1: Galois unipotent + uniform Selmer Kummer row density audit.

This is a finite GL2(Fp) combinatorics verification; the simultaneous
Kummer image V^r for independent H1(Q,V) classes is proved by Sah,
irreducibility, Schur and semisimplicity in the companion note.
This program does NOT compute Sha or a Kato derivative.
"""
from fractions import Fraction
from itertools import product

def audit(p,r):
    unips=sum(1 for a,b,c,d in product(range(p),repeat=4)
              if (a+d)%p==2 and (a*d-b*c)%p==1
              and (a,b,c,d)!=(1,0,0,1))
    assert unips==p*p-1
    gl=p*(p-1)**2*(p+1)
    assert Fraction(unips,gl)==Fraction(1,p*(p-1))
    isolated=sum(1 for v in product(range(p),repeat=r)
                 if all(x==0 for x in v[:-1]) and v[-1]!=0)
    assert isolated==p-1
    density=Fraction(unips,gl)*Fraction(isolated,p**r)
    assert density==Fraction(1,p**(r+1))
    print('SEL_UNIPOTENT_KUMMER_SEPARATION_PASS',
          p,r,'unipotents',unips,'density',density)

for p in (5,7,11):
    for r in (2,3,4):
        audit(p,r)
print('LIMIT: finite-group combinatorics only; no new Sha vanishing')
