#!/usr/bin/env python3
"""Exact invariants of rank-zero curve 226802e1, counter-test to arXiv:1703.02215.

Inputs NOT recomputed here: Cremona exact analytic rank-zero modular-symbol
value (analytic Sha order 289) and the published Skinner-Urban theorem.
"""
from math import gcd
a1,a2,a3,a4,a6 = 1,1,0,-4433709274,-120882223686060
N,p=226802,17
b2=a1*a1+4*a2
b4=2*a4+a1*a3
b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
c4=b2*b2-24*b4
c6=-b2**3+36*b2*b4-216*b6
assert N==2*151*751
assert delta==-2**6*151*751**9
assert gcd(c4,N)==1
assert delta%p
A,B=-27*c4,-54*c6
assert 4*A**3+27*B**2==-2**8*3**12*delta
assert (4*A**3+27*B**2)%p
count=1+sum((y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6)%p==0 for x in range(p) for y in range(p))
assert count==24 and p+1-count==-6
print('EXACT_DISCRIMINANT_PASS',delta)
print('SEMISTABLE_CONDUCTOR_FACTORS_PASS',N,'gcd(c4,N)',gcd(c4,N))
print('GOOD_ORDINARY_17_PASS',count,'a17',-6)
print('SHORT_MODEL_DISCRIMINANT_UNIT_17_PASS')
print('EXTERNAL_EXACT_MODULAR_SYMBOL_ANALYTIC_SHA_289_REQUIRED')
print('EXTERNAL_SKINNER_URBAN_3_6_11_REQUIRED')
print('BOUNDARY: does not compute original BSD389 Sha or prove its finiteness')
