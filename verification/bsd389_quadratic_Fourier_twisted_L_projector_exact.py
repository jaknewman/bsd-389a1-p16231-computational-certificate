#!/usr/bin/env python3
"""Exact Q(zeta_m) proof check: degree-two projector from ALL twisted values.

Finite group-ring algebra only. The actual E389a1 Manin input is from
user-run p5-depth25 result; no independent 28M-symbol re-enumeration.

SymPy required (available in Sage's Python environment).
"""
from math import comb
import sympy as s

x=s.symbols('x')
for m in (5,25):
    phi=s.cyclotomic_poly(m,x)
    aa=[(r*r+3*r+7)%11-5 for r in range(m)]
    F=sum(aa[r]*x**r for r in range(m))
    direct=sum(aa[r]*comb(r,2) for r in range(m))
    reduce=lambda z:s.rem(z,phi,x).expand()
    ft0=sum(aa)
    value=s.Rational((m-1)*(m-2),6)*ft0
    for t in range(1,m):
        z=x**(m-t)
        inv=s.invert(1-z,phi,x)
        weight=-(m-1)*inv/s.Integer(2)-z*inv*inv
        ft=reduce(F.subs(x,x**t))
        value+=reduce(ft*weight)
    assert reduce(value)==direct
    print('CYCLOTOMIC_EXACT_QUADRATIC_SPECTRAL_PROJECTOR_PASS',
          m,'direct',direct)
print('BOUNDARY_ALGEBRAIC_ONLY_NO_UNIFORM_KURIHARA_NONVANISHING')
