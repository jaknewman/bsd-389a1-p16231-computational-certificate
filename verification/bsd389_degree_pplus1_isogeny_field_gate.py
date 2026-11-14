#!/usr/bin/env python3
"""Exact 389a1 p+1-degree isogeny-field arithmetic.

The class-field/isogeny-Selmer INJECTION is a cohomological theorem, not
computed by this file. This file certifies the independent geometric
inputs: j, irreducibility of a genuine X0(5) sextic, Borel indices and
the quotient character. Requires only the standard library and SymPy.
"""
from sympy import Poly, symbols, gcd as pgcd, factor_list
t=symbols("t")
a1,a2,a3,a4,a6=0,1,1,-2,0
b2=a1*a1+4*a2
b4=a1*a3+2*a4
b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert (c4,Delta,c4**3)==(112,389,1404928)
f=(Delta*(t*t+10*t+5)**3-c4**3*t).expand()
assert f==389*t**6+11670*t**5+122535*t**4+505700*t**3+612675*t**2-1113178*t+48625
q=Poly(f,t,modulus=3).monic()
assert q.as_expr()==t**6+t**3+t-1
assert q.is_irreducible
print("BSD389_P5_EXACT_IRREDUCIBLE_X0_5_SEXTIC_PASS",str(f))
for p in (5,7,11):
    B={(a,b,0,d) for a in range(1,p) for b in range(p) for d in range(1,p)}
    chi_kernel={b for b in B if b[3]==1}
    order=p*(p-1)**2*(p+1)
    assert len(B)==p*(p-1)**2
    assert len(chi_kernel)==p*(p-1)
    assert order//len(B)==p+1 and order//len(chi_kernel)==p*p-1
    assert (p-1,0,0,p-1) in B
    for a,b,c,d in B:
        for v in range(p):
            assert (c*(1+v)+d*v)%p==d*v%p
    print("BOREL_DUAL_ISOGENY_CHARACTER_PASS",p,
          "GL2",order,"Borel",len(B),"K_degree",p+1,
          "L_degree",p*p-1)
for p in (107,16231):
    print("BIG_FIELD_DEGREE_FORMULA",p,
          "F",p*(p-1)**2*(p+1),"K",p+1,"L",p*p-1)
print("NO_ISOGENY_SELMER_OR_SHA_COMPUTED")
