#!/usr/bin/env python3
"""Exact cyclotomic resultant 0-or-1 detector for p^k deep rank-two theta.

Tests genuine general finite *algebra* for integral c0,c1 divisible p^k
and c2 equal to authenticated example residues 4,1,22, vs nonunit controls.
Does not re-enumerate the genuine Manin sum or prove global Sha finiteness.
Requires sympy (installed in Sage's Python environment).
"""
import sympy as sp

x=sp.Symbol('x')
for p,k,unit in ((5,1,4),(11,1,1),(5,2,22)):
    m=p**k
    T=x-1
    S=sp.Poly(sum(x**a for a in range(m)),x)
    for c2 in (unit,p,0):
        F=sp.Poly(2*m+3*m*T+c2*T**2+2*T**3+4*T**4,x)
        B=sp.resultant(S,F,x)
        assert B%m**2==0
        R=B//m**2
        expected=pow(c2,m-1,p)
        assert R%p==expected
        assert expected in (0,1)
        print('EXACT_CYCLOTOMIC_RESULTANT_BOOLEAN_PASS',
              'p',p,'k',k,'c2',c2,
              'resultant_digits',len(str(abs(B))),
              'normalized_modp',R%p,'expected',expected)
print('RESULTANT_THEOREM_SCOPE: true theta quadratic jet comes from Hecke')
print('BOUNDARY: NOT A PRIME-INDEPENDENT SHA ANNIHILATOR')
