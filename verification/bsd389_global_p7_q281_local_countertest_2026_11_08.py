#!/usr/bin/env python3
"""Exact finite-field Kummer counter-test for 389a1 at p=7.
Archived delta_(113*281)=0 is NOT recomputed without Sage/eclib.
"""
from math import isqrt
P=(-1,1); Q=(0,-1); p=7
def prime(n): return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def on(A,q):
    x,y=A
    return (y*y+y-x**3-x*x+2*x)%q==0
def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if (x-u)%q==0 and (y+v+1)%q==0:return None
    if (x-u)%q:
        z=pow((u-x)%q,-1,q)
        lam=(v-y)*z%q;nu=(y*u-v*x)*z%q
    else:
        d=(2*y+1)%q
        if not d:return None
        z=pow(d,-1,q)
        lam=(3*x*x+2*x-2)*z%q
        nu=(-x*x*x-2*x-y)*z%q
    X=(lam*lam-1-x-u)%q
    return X,(-lam*X-nu-1)%q
def mul(n,A,q):
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q);n>>=1
    return R
for q,expected,a_expected in [(113,105,9),(281,294,-12)]:
    assert prime(q) and q%p==1 and q!=389
    E=[None]+[(x,y) for x in range(q) for y in range(q) if on((x,y),q)]
    assert len(E)==expected and q+1-expected==a_expected
    assert (a_expected-(q+1))%p==0
    image={mul(p,R,q) for R in E}
    tors=[R for R in E if mul(p,R,q) is None]
    dim={7:1,49:2}[len(tors)]
    assert len(image)*len(tors)==len(E)
    print("P7_LOCAL_GROUP_EXACT_PASS",q,"a_q",a_expected,"group_order",expected,
          "torsion7",len(tors),"mod7_dim",dim)
    if q==113:
        assert dim==1
        a=mul(expected//7,P,q); b=mul(expected//7,Q,q)
        assert a is not None and b==mul(3,a,q)
        print("P7_113_Q_EQUALS_3P_IN_MOD7_PASS")
    if q==281:
        assert dim==2 and len(image)==6
        relations=[(a,b) for a in range(p) for b in range(p)
                   if add(mul(a,P,q),mul(b,Q,q),q) in image]
        assert relations==[(0,0)]
        print("P7_281_LOCAL_PQ_BASIS_PASS",relations)
        print("P7_281_FROBENIUS_IDENTITY_PASS")
print("ARCHIVED_DELTA_113_281_ZERO_NOT_RECOMPUTED")
print("NO_CLAIM_FOR_PAIRS_WITH_BOTH_NONIDENTITY_UNIPOTENT_FROBENII")
