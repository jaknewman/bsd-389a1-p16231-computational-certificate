#!/usr/bin/env python3
"""Check exact integral rank-two Bockstein determinant/SNF arithmetic.

This is an ALGEBRAIC model. It does not construct Selmer complexes,
Kurihara coefficients or a global Sha annihilator for E389a1.
"""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
T=s.Symbol('T')

def check(a):
 A=s.diag(T,T,T+a,T+a)
 f=s.expand(A.det())
 c2=int(f.coeff(T,2))
 assert f==T**4+2*a*T**3+a*a*T**2
 A0=A.subs(T,0)
 assert A0.rank()==2
 D=smith_normal_form(A0,domain=ZZ)
 order=s.prod(abs(int(D[i,i])) for i in range(D.rows) if D[i,i]!=0)
 assert c2==order==a*a
 U=s.eye(4);U[0,2]=1;U[1,3]=-2;U[2,3]=3
 V=s.eye(4);V[2,0]=1;V[3,1]=4
 B=U*A*V
 D2=smith_normal_form(B.subs(T,0),domain=ZZ)
 order2=s.prod(abs(int(D2[i,i])) for i in range(D2.rows) if D2[i,i]!=0)
 assert int(s.expand(B.det()).coeff(T,2))==order2==a*a
 print('RANK2_BOCKSTEIN_EXACT_SNF_PASS',a,'coefficient',c2,'torsion_order',order2)

for a in (1,2,3,5,6,25,125):check(a)
a=5;A=s.diag(2*T,T,T+a,T+a)
assert int(s.expand(A.det()).coeff(T,2))==50
assert 50%(a*a)==0
print('RANK2_BOCKSTEIN_EXTRA_FACTOR_PASS',50,'torsion_order',a*a)
A=s.diag(T,T,T,T)
assert s.expand(A.det())==T**4 and A.subs(T,0).rank()==0
print('PRIMITIVE_HIGHER_CORANK_ALTERNATIVE_PASS')
print('LIMIT_NOT_A_PRESENTATION_OF_SHA_389A1')
