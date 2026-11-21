#!/usr/bin/env python3
"""Complete 389a1 p11 Kurihara audit at 397, 991, 1321 (plain Python).

Runs all phi(q1*q2) units in each of THREE pairs; not a pilot.
The exact 390-coordinate Manin vector is copied from the archived
Sage/eclib cross-check script (SHA-256 pinned below). Independently
verifies finite-field traces, local Mordell--Weil rows,
4 full moments, and half/full agreement.
This does NOT call Sage/eclib: 397x991 was independently verified
by user-run Sage on Nov 14; 2 additional pairs need a fresh Sage audit.
"""
from hashlib import sha256
from math import gcd, isqrt
N=389
P=11
COMPACT=(
    '222224232123221232321222312332210011221232131210022222211110'
    '222242322222111220000112210221101334422332132111111111323233'
    '121211220222323121333422232134222244424332233424333433333443'
    '223233222010022220010222332322344333334333424332233424442222'
    '431232224333121323222022112121332323111111111231233224433101'
    '122012211000022111222223242222011112222220012131232122110012'
    '233213222123232122321232422222'
)
assert len(COMPACT)==390
assert sha256(bytes(int(c) for c in COMPACT)).hexdigest() == '31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee'
V=tuple(int(c)-2 for c in COMPACT)
assert sum(V)==0 and gcd(*V)==1
INV=(0,)+tuple(pow(a,-1,N) for a in range(1,N))
EXPECTED={397:(24,374,10),991:(-53,1045,7),1321:(2,1320,2)}
PAIRS=((397,991,1,8),(397,1321,9,3),(991,1321,10,6))

def isprime(q):
    return q>=2 and all(q%j for j in range(2,isqrt(q)+1))

def ap(q):
    s=0
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        if d:
            z=pow(d,(q-1)//2,q)
            assert z in (1,q-1)
            s+=(1 if z==1 else -1)
    return -s

def primitive_root(q):
    factors=[r for r in range(2,q) if (q-1)%r==0 and isprime(r)]
    return next(g for g in range(2,q) if all(pow(g,(q-1)//r,q)!=1 for r in factors))

def dlog(q,p):
    g=primitive_root(q)
    L=[0]*q
    a=1
    for k in range(q-1):
        L[a]=k%p;a=a*g%q
    assert a==1
    return g,L

def manin(a,n,p):
    # Continued-fraction Manin edge evaluation; source vector pinned.
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a
    s=V[N]
    while v:
        k,u,v=u//v,v,u%v
        x,y=k*ln+pn,k*ld+pd
        det=ln*y-x*ld
        assert abs(det)==1
        c,d=(ld,y) if det==1 else (y,ld)
        c%=N;d%=N
        s+=det*V[d*INV[c]%N if c else N]
        pn,pd,ln,ld=ln,ld,x,y
    assert (ln,ld)==(a,n)
    return s%p

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:return None
    if A==B:lam=(3*x*x+2*x-2)*pow(2*y+1,-1,q)%q
    else:lam=(v-y)*pow((u-x)%q,-1,q)%q
    xx=(lam*lam-1-x-u)%q
    yy=(lam*(x-xx)-y-1)%q
    assert (yy*yy+yy-xx**3-xx**2+2*xx)%q==0
    return (xx,yy)

def mul(A,n,q):
    R=None
    while n:
        if n&1:R=add(R,A,q)
        A=add(A,A,q);n>>=1
    return R

def local_row(q):
    a,n,r=EXPECTED[q]
    assert isprime(q) and q%P==1 and ap(q)==a and q+1-a==n
    assert n%P==0 and (n//P)%P!=0
    B=mul((-1%q,1),n//P,q)
    C=mul((0,-1%q),n//P,q)
    assert B is not None and mul(B,P,q) is None
    rr=next(i for i in range(P) if mul(B,i,q)==C)
    assert rr==r,(q,rr,r)
    print('K11_LOCAL_ROW_PASS',q,'N',n,'row',(1,rr))

def full_pair(q1,q2,expected,det):
    g1,L1=dlog(q1,P);g2,L2=dlog(q2,P)
    n=q1*q2
    low=[0]*4;count=0;half=0
    for a in range(1,n):
        x,y=a%q1,a%q2
        if x==0 or y==0:continue
        v=manin(a,n,P);u,w=L1[x],L2[y]
        low[0]=(low[0]+v)%P
        low[1]=(low[1]+u*v)%P
        low[2]=(low[2]+w*v)%P
        low[3]=(low[3]+u*w*v)%P
        if a<=n//2:half=(half+u*w*v)%P
        if a in (1,2,3,7,23):assert manin(n-a,n,P)==v
        count+=1
    assert count==(q1-1)*(q2-1)
    assert low==[0,0,0,expected],(q1,q2,low)
    assert low[3]==2*half%P
    assert det==(EXPECTED[q2][2]-EXPECTED[q1][2])%P
    print('K11_FULL_KURIHARA_THREE_PAIR_PASS',q1,q2,
          'units',count,'moments',low,'half',half,'roots',(g1,g2),'local_det',det)

def run():
    assert manin(7,389,11)==10   # original exact m_E^+(7/389)=-1
    for q in EXPECTED:local_row(q)
    for q1,q2,value,det in PAIRS:full_pair(q1,q2,value,det)
    print('K11_FULL_THREE_PAIR_ALL_PASS')
    print('BOUNDARY: independent pure-Python Manin evaluation using pinned frozen vector; '
          'not an independent Sage/eclib construction of that vector, not a uniform all-p BSD proof')
if __name__=='__main__':run()
