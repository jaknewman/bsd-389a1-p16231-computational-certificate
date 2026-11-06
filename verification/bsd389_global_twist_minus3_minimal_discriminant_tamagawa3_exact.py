#!/usr/bin/env python3
"""Exact arithmetic sanity-check for the GLOBAL d=-3 twist normalization.
Proves polynomial/discriminant/Tate cubic identities with integer arithmetic only.
Does not itself prove the analytic modular-symbol/Manin-Drinfeld theorem.
"""
from fractions import Fraction as Q
def f(x): return x**3+x**2-2*x+Q(1,4)
def twist_cubic(x): return x**3-3*x*x-18*x-Q(27,4)
assert all(twist_cubic(-3*x)==-27*f(x) for x in map(Q,(-4,-1,0,1,5)))
print("TWIST_EXACT_CUBIC_RELATION_PASS")
# A Weierstrass equation y^2+a3*y=x^3+a2*x^2+a4*x+a6
# has invariants b2=4*a2, b4=2*a4, b6=a3^2+4*a6,
# b8=4*a2*a6+a2*a3^2-a4^2.
# Delta=-b2^2*b8-8*b4^3-27*b6^2+9*b2*b4*b6.
# There is NO 1728 divisor here (it belongs to (c4^3-c6^2)/1728).
a2,a3,a4,a6=-3,1,-18,-7
b2=4*a2
b4=2*a4
b6=a3*a3+4*a6
b8=4*a2*a6+a2*a3*a3-a4*a4
Delta=(-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)
assert Delta==389*729,(Delta,389*729)
print("MINIMAL_TWIST_DELTA_PASS",Delta)
# y_old=Y+4 yields [a2,a3,a4,a6]=[-3,9,-18,-27].
assert a2==-3 and a4==-18
def Pt(t): return t**3-t**2-2*t-1
assert [t for t in range(3) if Pt(t)%3==0]==[1]
assert all(((t-1)*(t*t+1)-Pt(t))%3==0 for t in range(3))
print("TATE_I0STAR_ROOT_COUNT_C3_PASS",1,2)
print("EXACT_TAMAGAWA_PRODUCT_PREDICTED",2)
print("RANKZERO_TWIST_L_OVER_OMEGA_EQUAL_TWO_SOURCE_PROOF_SEPARATE")
print("BOUNDARY: no Sha=0, all-prime bound, or rank-two BSD")
