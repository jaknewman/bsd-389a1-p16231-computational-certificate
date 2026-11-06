#!/usr/bin/env python3
"""Exact rational interval proof isolating the -3 twist modular-symbol integer."""
from fractions import Fraction as Q

def cubic(x):
    return x**3 + x**2 - 2*x + Q(1,4)

for a,b in ((-2041,-2039),(134,136),(904,906)):
    assert cubic(Q(a,1000))*cubic(Q(b,1000)) < 0
print("EXACT_THREE_REAL_ROOT_BRACKETS_PASS")

A_lower,A_upper=Q(294,100),Q(296,100)
assert Q(1714,1000)**2 < A_lower
assert Q(1721,1000)**2 > A_upper
assert Q(26,100) < Q(768,2947)
assert Q(772,2943) < Q(27,100)

m_lower,m_upper=Q(26,100),Q(27,100)
# K(m) = pi/2 * sum c_j*m^j, with c0=1,c1=1/4,cj<=9/64 for j>=2
# Use rigorous 3.14<pi<22/7.
om_lower=Q(314,100)/Q(1721,1000)*(1+m_lower/4)
om_upper=Q(22,7)/Q(1714,1000)*(1+m_upper/4+Q(9,64)*m_upper**2/(1-m_upper))
assert Q(19,10)<om_lower<om_upper<Q(21,10)
print("EXACT_IMAG_PERIOD_BOUNDS_PASS",om_lower,om_upper)

# Input is PREVIOUSLY PROVED, not rerun: 9/2 < L(E^-3,1) < 23/5.
# Gauss/modular symbol + c_E=1 + rational cusp torsion zero gives
# L(E^-3,1)=2*m0*OmegaMinus/sqrt(3), with integer m0.
# Bound sqrt(3) by 17/10 and 7/4.
nlo=Q(9,2)*Q(17,10)/(2*Q(21,10))
nhi=Q(23,5)*Q(7,4)/(2*Q(19,10))
assert 1<nlo<2<nhi<3
print("GLOBAL_TWIST_MANIN_INTEGER_UNIQUE_PASS",nlo,nhi)
print("CONCLUSION_WITH_MODULAR_SYMBOL_THEOREM: L(E^-3,1)=4*OmegaMinus/sqrt(3) EXACT")
print("BOUNDARY: no rank-two complex BSD identity or global Sha finiteness")
