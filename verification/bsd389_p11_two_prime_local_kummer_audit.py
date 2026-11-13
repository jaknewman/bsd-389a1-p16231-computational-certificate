#!/usr/bin/env python3
"""Pure-Python exact E389a1 p11 local Kummer + basis reconciliation.

NO Sage; NO Kurihara sum; NO new Sha conclusion. All assertions are exact.
"""
from math import gcd, isqrt
from fractions import Fraction as F
P=(-1,1); Q=(0,-1); p=11

def prime(n): return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def aq(q):
    assert prime(q) and q!=389
    s=0
    for x in range(q):
        d=(4*x*x*x+4*x*x-8*x+1)%q
        if d:
            t=pow(d,(q-1)//2,q)
            assert t in (1,q-1)
            s+=1 if t==1 else -1
    return -s

def oncurve(V,q):
    if V is None:return True
    x,y=V
    return (y*y+y-x*x*x-x*x+2*x)%q==0

def add(U,V,q):
    if U is None:return V
    if V is None:return U
    x,y=U; u,v=V
    if x==u and (y+v+1)%q==0:return None
    if x==u:lam=(3*x*x+2*x-2)*pow((2*y+1)%q,-1,q)%q
    else:lam=(v-y)*pow((u-x)%q,-1,q)%q
    nu=(y-lam*x)%q
    xx=(lam*lam-1-x-u)%q
    W=(xx,(-lam*xx-nu-1)%q)
    assert oncurve(W,q)
    return W

def mul(U,k,q):
    V=None
    while k:
        if k&1:V=add(V,U,q)
        U=add(U,U,q);k//=2
    return V

rows=[]
for q,ap,n,pp,qq,ratio,gi in (
    (397,24,374,(217,30),(217,366),10,22),
    (991,-53,1045,(68,61),(744,857),7,55),
):
    assert aq(q)==ap and q+1-ap==n and q%p==1 and ap%p==2
    assert n%p==0 and n%(p*p)!=0
    assert oncurve(P,q) and oncurve(Q,q)
    R,S=mul(P,n//p,q),mul(Q,n//p,q)
    assert (R,S)==(pp,qq) and R is not None
    assert mul(R,p,q) is None and mul(S,p,q) is None
    assert mul(R,ratio,q)==S
    assert mul(P,n,q) is None and mul(Q,n,q) is None
    assert gcd(q-1,ap-q-1)==gi
    rows.append([1,ratio])
    print('K11_LOCAL_KUMMER_PASS','q',q,'ap',ap,'E_Fq',n,'Pproj',R,
          'Qproj',S,'ratio',ratio,'I_q_gcd',gi)
assert rows==[[1,10],[1,7]]
det=(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])%p
assert det==8
print('K11_MW_TWO_LOCAL_UNIT_PASS','A',rows,'det',det)

# Rational MW normalization: P'=(0,0)=-Q, Q'=(1,0)=P-Q.
def add_r(U,V):
    x,y=U;u,v=V
    lam=(v-y)/(u-x) if x!=u else (3*x*x+2*x-2)/(2*y+1)
    nu=y-lam*x
    xx=lam*lam-1-x-u
    return xx,-lam*xx-nu-1
assert add_r((F(-1),F(1)),(F(0),F(0)))==(F(1),F(0))
B=((0,1),(-1,-1))
def prod(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%p
             for j in range(2)] for i in range(2)]
C=prod(rows,B)
assert C==[[1,2],[4,5]]
D=[[C[0][0],C[0][1]],[3*C[1][0]%p,3*C[1][1]%p]]
assert D==[[1,2],[1,4]] and 3*det%p==2
print('K11_FULL_LOCAL_NORMALIZATION_RECONCILIATION_PASS','change_B',B,
      'local_rescale',(1,3),'external_A',D,'external_det',2)
print('SCOPE_LOCAL_ONLY_NO_KURIHARA_SUM_NO_GLOBAL_BSD')
