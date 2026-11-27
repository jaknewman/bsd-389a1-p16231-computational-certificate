#!/usr/bin/env python3
"""Independent integer Mazur--Tate layer and exact U_389 check for 389a1.

Reads integer Manin table (index t in F_389, then infinity). Does not use
numerical L-values or Sha. All sums are exact integers then reduced mod 389.
"""
import math, hashlib, json
from math import comb
from pathlib import Path
P=389
N=P*P
v=list(map(int,Path(__file__).with_name('manin_390.txt').read_text().split()))
assert len(v)==390 and v[389]==0
inv=[0]*P
for i in range(1,P):inv[i]=pow(i,-1,P)

def ms(a,n):
    assert 0<a<n and math.gcd(a,n)==1
    pn,pd,ln,ld=1,0,0,1
    total=v[P]
    x,y=n,a
    while y:
        q,r=divmod(x,y)
        nn,nd=q*ln+pn,q*ld+pd
        det=ln*nd-nn*ld
        assert abs(det)==1
        if det==1:c,d=ld,nd
        else:c,d=nd,ld
        c%=P;d%=P
        total+=det*v[P if c==0 else d*inv[c]%P]
        pn,pd,ln,ld=ln,ld,nn,nd
        x,y=y,r
    assert ln==a and ld==n
    return total

assert ms(7,P)==-1 and ms(5,P)==-2
coefs=[0]*6
cyclotomic=[0]*P
U=[0]*P
symcheck=0
num=0
for a in range(1,N):
    if a%P==0:continue
    num+=1
    m=ms(a,N)
    t=pow(a,P-1,N)
    assert t%P==1
    j=(-(t-1)//P)%P
    cyclotomic[j]+=m
    U[a%P]+=m
    for k in range(6):coefs[k]+=m*comb(j,k)
    if a <N//2:
        assert ms(N-a,N)==m
        symcheck+=1
coefs=[x%P for x in coefs]
assert coefs == [0,0,0,321,102,102],coefs
assert all(U[a]==ms(a,P) for a in range(1,P))
assert num==P*(P-1)
digest=hashlib.sha256(json.dumps([x%P for x in cyclotomic],separators=(',',':')).encode()).hexdigest()
print('EXACT_LEVEL_P2',N,'UNITS',num,'SYM_CHECKS',symcheck)
print('U389_ALL_388_EXACT_PASS')
print('NERON_ANCHOR_PASS',ms(7,P),ms(5,P))
print('TAYLOR_COEFFICIENTS_MOD389',coefs)
print('CYCLOTOMIC_GROUP_RING_SHA256',digest)
print('FIRST_NONZERO_ORDER_MOD389',next(i for i,c in enumerate(coefs) if c))
