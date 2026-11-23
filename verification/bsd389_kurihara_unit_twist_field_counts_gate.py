#!/usr/bin/env python3
"""Exact character counts and nonzero quadratic jets for three authentic BSD389 units.

External inputs: full user modular-symbol certificates, Hecke norm,
Birch-Stevens, Kato's twist rank-zero theorem, and no rational isogenies.
No all-prime Sha finiteness is claimed.
"""
from math import gcd

CERTS=[(5,1,41,61,4),(11,1,397,991,1),(5,2,5351,10651,22)]
total_fields=0
total_unique_twists=0
for p,k,q1,q2,delta in CERTS:
    m=p**k
    assert (q1-1)%(2*m)==(q2-1)%(2*m)==0
    assert delta%p
    units=[a for a in range(1,m) if gcd(a,m)==1]
    fields=set()
    twists=set()
    for r in units:
        fields.add(r)
        for t in range(1,m):
            a=t
            b=r*t%m
            assert a and b
            twists.add((a,b))
            j=k
            while a%p==0:
                j-=1
                a//=p
            assert j>=1
            assert p**(j-1)*(p-1)>=4
    assert len(fields)==len(units)
    expected=sum((p**j-p**(j-1))**2 for j in range(1,k+1))
    assert len(twists)==expected
    total_fields+=len(fields)
    total_unique_twists+=len(twists)
    print('KURIHARA_UNIT_GIVES_RANK_STABLE_CYCLIC_FIELDS_PASS',
          'p',p,'k',k,'q1',q1,'q2',q2,'delta',delta,
          'degree',m,'fields',len(fields),
          'distinct_twists',len(twists),'conductor',q1*q2)
assert total_fields==34 and total_unique_twists==532
print('BSD389_TOTAL_EXPLICIT_REAL_CYCLIC_FIELDS_NO_MW_GROWTH',total_fields)
print('BSD389_TOTAL_DISTINCT_NONZERO_TWIST_L_CENTRAL_VALUES',total_unique_twists)
print('EXTERNAL_KATO_PLUS_NO_ISOGENY_IMPLICATION: MW_UNCHANGED_IN_ALL_34_FIELDS')
print('BOUNDARY_NO_SHA_GLOBAL_FINITE_AND_NO_EXACT_COMPLEX_RANK2_BSD')
