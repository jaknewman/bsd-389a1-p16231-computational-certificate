#!/usr/bin/env python3
"""Exact algebraic rank-two Bockstein factorization/SNF and adelic toy countermodel.

Only checks algebraic models, NOT actual Selmer complex/Sha of E=389a1.
Published p-adic regulator first digits for 389a1 are checked only as mod-p units.
Requires sympy.
"""
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from math import prod
T=S.Symbol('T')

def order_tors(A):
    N=smith_normal_form(A,domain=ZZ)
    return prod(abs(int(N[i,i])) for i in range(min(N.shape)) if N[i,i]!=0)

def run(d1,d2,B):
    D=S.diag(d1,d2,0,0)
    M=S.Matrix([[1,2,3,7],[-1,4,5,2],[2,1,B[0][0],B[0][1]],
                [3,2,B[1][0],B[1][1]]])
    N=S.Matrix([[2,0,0,1],[0,1,2,0],[3,0,1,0],[0,4,1,2]])
    U=S.eye(4);U[0,2]=3;U[1,3]=-2;U[2,1]=5
    V=S.eye(4);V[2,0]=2;V[3,1]=-3;V[0,1]=4
    assert U.det()==V.det()==1
    A=U*(D+T*M+T*T*N)*V
    c2=int(S.Poly(A.det(method='berkowitz'),T).nth(2))
    f=order_tors(A.subs(T,0))
    detb=int(S.Matrix(B).det())
    assert f==abs(d1*d2) and c2==d1*d2*detb
    print('RANK2_EXACT_BOCKSTEIN_SNF_PASS',f,detb,c2)

for x in [(3,10,[[2,1],[1,4]]),(1,7,[[3,2],[4,5]]),
          (5,5,[[1,0],[0,1]]),(4,12,[[0,1],[2,0]]),
          (1,1,[[1,1],[1,1]])]:
    run(*x)
for p in (5,7,11,13,17,19,23,101):
    A=S.diag(T,T,T+p,T+p)
    assert order_tors(A.subs(T,0))==p*p
    assert S.Poly(A.det(),T).nth(2)==p*p
    assert S.Poly(A.det(),T).nth(4)==1
    print('ADELIC_PRIMITIVE_NO_INTEGER_GLUING_TOY_PASS',p)
published={5:1,7:6,11:4,13:9,17:4,19:3,23:17,
           29:9,31:1,37:28,41:20,43:40,47:25}
for p,a in published.items():
    assert a%p
    print('MST2006_PUBLISHED_389A_P_ADIC_MW_REGULATOR_UNIT_DIGIT',p,a)
print('BOUNDARY: NO actual full Selmer Bockstein nor global Sha annihilator inferred')
