#!/usr/bin/env python3
"""BSD 389a1: exact local Kummer determinants calibrated against ARCHIVED deltas.
Does NOT recompute modular symbols or establish any delta=unit*det theorem.
"""
from math import isqrt
P=(-1,1);Q=(0,-1)
def prime(q):return q>=2 and all(q%d for d in range(2,isqrt(q)+1))
def ap(q):
    acc=0
    for x in range(q):
        a=(4*x*x*x+4*x*x-8*x+1)%q
        if a:acc+=1 if pow(a,(q-1)//2,q)==1 else -1
    return -acc
def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x%q==u%q and (y+v+1)%q==0:return None
    if (u-x)%q:
        inv=pow((u-x)%q,-1,q)
        lam=(v-y)*inv%q; nu=(y*u-v*x)*inv%q
    else:
        d=(2*y+1)%q
        if not d:return None
        inv=pow(d,-1,q)
        lam=(3*x*x+2*x-2)*inv%q
        nu=(-x*x*x-2*x-y)*inv%q
    z=(lam*lam-1-x-u)%q
    return z,(-lam*z-nu-1)%q
def mul(n,A,q):
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q)
        n//=2
    return R
def ratio(p,q):
    assert prime(q) and q not in (p,389) and q%p==1
    a=ap(q);o=q+1-a
    assert a%p==2 and o%p==0 and o%(p*p)!=0
    U=mul(o//p,P,q);V=mul(o//p,Q,q)
    assert U is not None and mul(p,U,q) is None
    assert mul(o,P,q) is None and mul(o,Q,q) is None
    t=next((j for j in range(p) if mul(j,U,q)==V),None)
    assert t is not None
    return a,o,t
for p,q1,q2,archived in [(5,41,61,4),(7,113,673,2)]:
    a1,o1,r1=ratio(p,q1);a2,o2,r2=ratio(p,q2)
    det=(r2-r1)%p
    assert det
    print("LOCAL_DETERMINANT_PASS",p,q1,q2,"ap",(a1,a2),"orders",(o1,o2),"rows",((1,r1),(1,r2)),"det",det)
    print("ARCHIVED_KURIHARA_NOT_RECOMPUTED",p,"delta",archived,"delta_over_det",archived*pow(det,-1,p)%p)
print("BOUNDARY: no global unit comparison; no all-prime Sha result.")
