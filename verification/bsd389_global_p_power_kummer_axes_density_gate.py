#!/usr/bin/env python3
"""Exact finite combinatorics of p^k-level MW Kummer axis Chebotarev sets.

External arithmetic theorems (Serre, Sah, Chebotarev) are not proved here.
Does not compute Kurihara derivatives or Sha.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def check(p,k):
    m=p**k
    gl_order=p**(4*(k-1))*(p*p-1)*(p*p-p)
    cent=m*m-m*m//p
    assert cent==p**(2*k-1)*(p-1)
    assert gl_order%cent==0
    cls=gl_order//cent
    assert cls==p**(2*k-2)*(p*p-1)
    # R² is the p^k-Kummer local quotient for P,Q; P a unit, Q zero.
    favorable=sum(gcd(a,p)==1 and b==0
                  for a,b in product(range(m),repeat=2))
    assert favorable==m-m//p
    fiber_weight=Fraction(favorable,m*m)
    density=Fraction(cls,gl_order)*fiber_weight
    assert density==Fraction(1,p**(3*k))
    print('GLOBAL_PPOWER_KUMMER_AXIS_DENSITY_PASS',
          'p',p,'k',k,'class_size',cls,'centralizer',cent,
          'unit_axis_patterns',favorable,'of',m*m,
          'density',str(density))


for p,k in [(3,1),(3,2),(5,1),(5,2),(7,2),(11,2),(11,3),(107,2)]:
    check(p,k)
print('BOUNDARY_PPOWER_AXIS_IS_NOT_KURIHARA_NONVANISHING')
