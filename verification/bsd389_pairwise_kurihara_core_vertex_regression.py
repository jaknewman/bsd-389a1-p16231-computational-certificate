#!/usr/bin/env python3
"""Pure Python E389a1 actual Kurihara-versus-MW test at 8 auxiliary pairs.

Uses copied genuine integral 390-Manin vector from authenticated research
branch. Checks finite-field points, q-local Kummer determinants, full
weighted modular symbols by plus-symmetry. No Sage, no new all-p BSD.
"""
import json
from pathlib import Path
from math import isqrt

N=389
V=json.loads((Path(__file__).parent/"bsd389_390_integral_manin_vector_20261113.json").read_text())["vector"]
assert len(V)==390
INV=[0]+[pow(x,-1,N) for x in range(1,N)]

def modular_symbol(a,n):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a
    acc=V[N]
    while v:
        k,u,v=u//v,v,u%v
        x,y=k*ln+pn,k*ld+pd
        d=ln*y-x*ld
        assert abs(d)==1
        c,t=(ld,y) if d==1 else (y,ld)
        c%=N;t%=N
        acc+=d*V[t*INV[c]%N if c else N]
        pn,pd,ln,ld=ln,ld,x,y
    assert (ln,ld)==(a,n)
    return acc

assert (modular_symbol(7,389),modular_symbol(5,389))==(-1,-2)

def prime(n):return n>=2 and all(n%k for k in range(2,isqrt(n)+1))

def ap(q):
    assert prime(q) and q!=389
    val=0
    for x in range(q):
        d=(4*x*x*x+4*x*x-8*x+1)%q
        if d:
            t=pow(d,(q-1)//2,q)
            assert t in (1,q-1)
            val+=(1 if t==1 else -1)
    return -val

def plus(U,W,q):
    if U is None:return W
    if W is None:return U
    x,y=U;u,v=W
    if x==u and (y+v+1)%q==0:return None
    if x==u:
        slope=(3*x*x+2*x-2)*pow((2*y+1)%q,-1,q)%q
    else:
        slope=(v-y)*pow((u-x)%q,-1,q)%q
    b=(y-slope*x)%q
    nx=(slope*slope-1-x-u)%q
    return(nx,(-slope*nx-b-1)%q)

def times(U,n,q):
    out=None
    while n:
        if n&1:out=plus(out,U,q)
        U=plus(U,U,q);n//=2
    return out

def row(p,q,aq):
    order=q+1-aq
    assert order%p==0 and order%(p*p)!=0
    P=times((-1,1),order//p,q)
    Q=times((0,-1),order//p,q)
    T=P if P is not None else Q
    assert T is not None
    table={times(T,k,q):k for k in range(p)}
    assert len(table)==p
    return table[P],table[Q]

def dlog(q,p):
    m=q-1;f=[];d=2
    while d*d<=m:
        if m%d==0:
            f.append(d)
            while m%d==0:m//=d
        d+=1
    if m>1:f.append(m)
    g=next(g for g in range(2,q) if all(pow(g,(q-1)//factor,q)!=1 for factor in f))
    arr=[0]*q;v=1
    for k in range(q-1):
        arr[v]=k%p;v=v*g%q
    assert v==1
    return g,arr

def delta(p,q,r):
    g1,L1=dlog(q,p);g2,L2=dlog(r,p)
    total=0;n=q*r
    for a in range(1,(n+1)//2):
        if a%q and a%r:
            w=L1[a%q]*L2[a%r]%p
            if w:total=(total+w*modular_symbol(a,n))%p
    return (2*total)%p,(g1,g2)

CASES=[
  (5,41,61,2,4),
  (5,41,131,1,1),
  (5,41,211,1,2),
  (5,41,1321,0,0),
  (7,113,673,3,2),
  (7,113,1429,1,1),
  (7,113,2423,1,6),
  (7,113,7589,0,0),
]
for p,q,r,d_expected,v_expected in CASES:
    aq,ar=ap(q),ap(r)
    assert q%p==r%p==1 and aq%p==ar%p==2
    R,S=row(p,q,aq),row(p,r,ar)
    det=(R[0]*S[1]-R[1]*S[0])%p
    value,roots=delta(p,q,r)
    assert (det,value)==(d_expected,v_expected)
    assert (det!=0)==(value!=0)
    print("TRUE_E389A1_PAIRWISE_KURIHARA_REGRESSION_PASS",p,q,r,
          "MWdet",det,"Kurihara",value,"roots",roots,flush=True)
print("SCOPE_EIGHT_ACTUAL_FINITE_TESTS_NOT_UNIFORM_SHA_PROOF")
