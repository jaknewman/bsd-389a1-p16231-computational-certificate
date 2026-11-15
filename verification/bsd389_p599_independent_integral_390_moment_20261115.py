#!/usr/bin/env python3
"""Independent real E389a1 p599 conductor-p² C2 from 390 integer Manin data.

The 390-element vector was independently reconstructed and archived in
research/bsd389-direct-global-sha-complex-Lstar-20261106:
  verification/bsd389_390_integral_manin_vector_20261113.json
It is not the frozen p599 Sage/eclib Manin table. This is an independent
finite-sum algorithm, not a substitute for proving modular normalization.
"""
import time
p=599;n=p*p;N=389
compact='222224232123221232321222312332210011221232131210022222211110222242322222111220000112210221101334422332132111111111323233121211220222323121333422232134222244424332233424333433333443223233222010022220010222332322344333334333424332233424442222431232224333121323222022112121332323111111111231233224433101122012211000022111222223242222011112222220012131232122110012233213222123232122321232422222'
assert len(compact)==390
V=[int(v)-2 for v in compact]
assert V[389]==0 and all(-2<=v<=2 for v in V)
INV=[0]+[pow(a,-1,N) for a in range(1,N)]
def sym(a,n):
    pn,pd,ln,ld=1,0,0,1;u,v=n,a;res=V[N]
    while v:
        k,u,v=u//v,v,u%v
        x,y=k*ln+pn,k*ld+pd
        det=ln*y-x*ld
        assert abs(det)==1
        c,d=(ld,y) if det==1 else (y,ld)
        c%=N;d%=N
        res+=det*V[d*INV[c]%N if c else N]
        pn,pd,ln,ld=ln,ld,x,y
    assert (ln,ld)==(a,n)
    return res
assert sym(7,389)==-1 and sym(5,389)==-2
C0=C1=C2=0;count=0
tic=time.monotonic()
for a in range(1,(n-1)//2+1):
    if a%p==0:continue
    s=sym(a,n)%p
    k=-((pow(a,p-1,n)-1)//p)%p
    assert (pow(a,p,n)*(1+p*k))%n==a%n
    C0=(C0+2*s)%p
    C1=(C1+2*s*k)%p
    C2=(C2+s*k*(k-1))%p
    count+=1
assert (count,C0,C1,C2)==(179101,0,0,543)
print('P599_GENUINE_390_INTEGER_MANIN_INDEPENDENT_PASS',
      'plus_pairs',count,'C0',C0,'C1',C1,'C2',C2,
      'seconds',round(time.monotonic()-tic,3),flush=True)
print('INPUT_PROVENANCE: prior research branch integer vector, NOT p599 frozen eclib table')
print('SCOPE: NO direct p^3 sum, no Sage p_primary_bound run, no new all-prime BSD')
