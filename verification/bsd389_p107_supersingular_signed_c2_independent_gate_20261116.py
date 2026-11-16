#!/usr/bin/env python3
"""Exact p=107 conductor-p^2 cyclotomic moments of E=389a1.

Uses the separately archived signed integral 390-vector and independent
discrete-log reconstruction. NOT a proof of signed main-conjecture comparison.
"""
from math import isqrt
N, p = 389, 107
n = p*p
compact = "222224232123221232321222312332210011221232131210022222211110222242322222111220000112210221101334422332132111111111323233121211220222323121333422232134222244424332233424333433333443223233222010022220010222332322344333334333424332233424442222431232224333121323222022112121332323111111111231233224433101122012211000022111222223242222011112222220012131232122110012233213222123232122321232422222"
assert len(compact)==390
V = [int(c)-2 for c in compact]
INV = [0]+[pow(a,-1,N) for a in range(1,N)]
def symbol(a):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a; s=V[N]
    while v:
        k,u,v=u//v,v,u%v
        x,y=k*ln+pn,k*ld+pd
        d=ln*y-x*ld
        assert abs(d)==1
        c,e=(ld,y) if d==1 else (y,ld)
        c%=N;e%=N
        s+=d*V[e*INV[c]%N if c else N]
        pn,pd,ln,ld=ln,ld,x,y
    assert (ln,ld)==(a,n)
    return s
gamma_to_j={pow(1+p,j,n):j for j in range(p)}
assert len(gamma_to_j)==p
C0=C1=C2=checks=0
for a in range(1,(n-1)//2+1):
    if a%p==0:continue
    s=symbol(a)%p
    assert s==symbol(n-a)%p
    k=(-(pow(a,p-1,n)-1)//p)%p
    # F(a) = (a/omega(a)) with Teichmueller omega(a) = a^p (mod p^2).
    omega=pow(a,p,n)
    ratio=a*pow(omega,-1,n)%n
    j=gamma_to_j[ratio]
    assert j==k,(a,j,k)
    C0=(C0+2*s)%p
    C1=(C1+2*s*j)%p
    C2=(C2+s*j*(j-1))%p
    checks+=1
assert (checks,C0,C1,C2)==(5671,0,0,86),(checks,C0,C1,C2)
signed_minus=(-C2*pow(2,-1,p))%p
assert signed_minus==64
print('P107_SUPERSINGULAR_C2_SYMMETRY_AND_LOG_PASS',
      'pairs',checks,'C0',C0,'C1',C1,'C2',C2,
      'candidate_signed_minus',signed_minus)
print('STATUS: arithmetic finite-sum PASS only; true L_p^- coefficient requires')
print('        independent comparison of Pollack/Kobayashi normalizations')
print('        and integral error bound; no all-prime annihilator asserted')
