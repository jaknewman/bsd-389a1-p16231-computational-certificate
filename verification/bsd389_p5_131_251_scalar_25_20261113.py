#!/usr/bin/env python3
"""New p=5 Mazur–Tate 32881 scalar contraction on 389a1, Sage-free exact check.

Recomputes all 25 theta coefficients from the certified 390 integral Manin
symbols, six nontrivial character norms, exact INTEGRAL Smith normal form.
Requires sympy and the prior same-directory 390-symbol helper and JSON.

Arithmetic Sha(K) conclusions require Bullach–Honnor 2026 Theorem 1.4,
not provided by this numeric program. Full Bezout coefficients mod 5^12
and two-prime cross-audit are in the 13 Nov 2026 conversation ZIP.
"""
from collections import Counter
from math import gcd
from sympy import ZZ,Matrix,Poly,Symbol,resultant
from sympy.matrices.normalforms import smith_normal_form
from bsd389_Mazur_Tate_integral_rank2_two_conductors_20261113 import sym,root

p=5;q=131;r=251;n=q*r
def trace(ell):
    sq={y*y%ell for y in range(ell)}
    count=1
    for x in range(ell):
        t=(1+4*(x*x*x+x*x-2*x))%ell
        count+=1 if t==0 else 2 if t in sq else 0
    return ell+1-count,count
assert trace(q)==(2,130) and trace(r)==(22,230)
g,h=root(q),root(r)
assert (g,h)==(2,6)
u={pow(g,i,q):i%p for i in range(q-1)}
v={pow(h,j,r):j%p for j in range(r-1)}
C=[[0]*p for _ in range(p)]
for a in range(1,n):
    if a%q and a%r:C[u[a%q]][v[a%r]]+=sym(a,n)
assert C==[[-100,-2,-228,-86,-58],[54,-2,186,-116,24],
          [54,24,-116,186,-2],[-100,-58,-86,-228,-2],
          [104,30,246,246,30]]
print('BSD389_NEW_P5_COMPLETE_THETA_25_INTEGERS_PASS',flush=True)

six=[sum(C[i][j]*f(i,j) for i in range(p) for j in range(p)) for f in
     (lambda i,j:1,lambda i,j:i,lambda i,j:j,
      lambda i,j:i*(i-1)//2,lambda i,j:i*j,lambda i,j:j*(j-1)//2)]
assert six==[0,1640,-30,2660,3556,-40] and [x%p for x in six]==[0,0,0,0,1,0]
print('BSD389_NEW_P5_THETA_MIXED_XY_UNIT_PASS',six,flush=True)

z=Symbol('z');phi=Poly(sum(z**i for i in range(p)),z)
valuations=[]
for a,b in [(1,t) for t in range(p)]+[(0,1)]:
    w=[sum(C[i][j] for i in range(p) for j in range(p)
           if (a*i+b*j)%p==k) for k in range(p)]
    assert len(set(w))>1
    norm=int(resultant(Poly(sum(w[i]*z**i for i in range(p)),z),phi,z))
    assert norm
    d=abs(norm);vp=0
    while d%p==0:d//=p;vp+=1
    valuations.append(vp)
    print('BSD389_NEW_P5_CHARACTER_NORM_NONZERO_PASS',a,b,norm,vp,flush=True)
assert sorted(valuations)==[2,2,2,2,4,4]

N=p*p
A=Matrix([[C[(i//p-j//p)%p][(i%p-j%p)%p] if j<N else 1
           for j in range(N+1)] for i in range(N)])
smith=smith_normal_form(A,domain=ZZ)
def ordp(x):
    x=abs(int(x));i=0
    while x%p==0 and x:x//=p;i+=1
    return i
hist=Counter(ordp(smith[i,i]) for i in range(N))
assert hist=={0:16,1:2,2:7}
print('BSD389_NEW_P5_EXACT_INTEGRAL_SMITH_PASS',dict(hist),flush=True)
print('BSD389_NEW_P5_SCALAR_IDEAL_CONTRACTION_PASS','25 Z_5',flush=True)
print('BOUNDARY: SHA RESULTS REQUIRE BH THEOREM; NOT GLOBAL BSD',flush=True)
