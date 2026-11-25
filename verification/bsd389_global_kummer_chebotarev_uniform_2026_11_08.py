#!/usr/bin/env python3
"""Exact rank-two Kummer auxiliary-point separation, not Kurihara nonvanishing."""
from math import isqrt
from fractions import Fraction
P=(-1,1);Q=(0,-1)

def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def oncurve(X,q):
    x,y=X
    return (y*y+y-x**3-x*x+2*x)%q==0

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if (x-u)%q==0 and (y+v+1)%q==0:return None
    if (x-u)%q:
        den=(u-x)%q
        lam=(v-y)*pow(den,-1,q)%q
        nu=(y*u-v*x)*pow(den,-1,q)%q
    else:
        den=(2*y+1)%q
        if not den:return None
        lam=(3*x*x+2*x-2)*pow(den,-1,q)%q
        nu=(-x**3-2*x-y)*pow(den,-1,q)%q
    z=(lam*lam-1-x-u)%q
    w=(-lam*z-nu-1)%q
    return z,w

def mul(n,A,q):
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q)
        n//=2
    return R

def ap(q):
    s=0
    for x in range(q):
        d=(1+4*(x**3+x*x-2*x))%q
        if d:s+=1 if pow(d,(q-1)//2,q)==1 else -1
    return -s

examples={5:{"P":61,"Q":251},7:{"P":8597,"Q":2423}}
for p, case in examples.items():
    for name,q in case.items():
        assert isprime(q) and q not in [p,389] and q%p==1
        assert oncurve(P,q) and oncurve(Q,q)
        a=ap(q);n=q+1-a
        assert a%p==2 and n%p==0 and n%(p*p)!=0
        x=mul(n//p,P,q);y=mul(n//p,Q,q)
        assert mul(n,P,q) is None and mul(n,Q,q) is None
        assert ((x is not None) and (y is None)) if name=="P" else ((x is None) and (y is not None))
        print("KUMMER_SEPARATION_PASS",p,q,a,n,x,y,name)

for p,q in [(5,61),(5,251)]:
    points=[None]+[(x,y) for x in range(q) for y in range(q) if oncurve((x,y),q)]
    assert len(points)==q+1-ap(q)
    image={mul(p,T,q) for T in points}
    assert (((P[0]%q,P[1]%q) in image) == (q==251))
    assert (((Q[0]%q,Q[1]%q) in image) == (q==61))
    print("BRUTE_FORCE_P_DIVISIBILITY_PASS",p,q,len(points))

for p in (3,5,7):
    n=0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a*d-b*c)%p==1 and (a+d)%p==2 and (a,b,c,d)!=(1,0,0,1):n+=1
    assert n==p*p-1
    G=(p*p-1)*(p*p-p)
    assert Fraction(n*p*p*(p-1),G*p**4)==Fraction(1,p**3)
    print("UNIPOTENT_DENSITY_PASS",p,n,str(Fraction(1,p**3)))
print("BOUNDARY: does not evaluate Kurihara deltas or establish Sha vanishing.")
