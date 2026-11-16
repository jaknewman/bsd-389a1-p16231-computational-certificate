#!/usr/bin/env sage -python
"""Real Sage/eclib direct comparison of 389a1 p=107 modular symbols.

This is a NEW, not-yet-executed independent audit. It must be run in Sage 10.9
(or equivalent) and its results saved before claiming an eclib-normalized
signed analytic L-function coefficient.
"""
from sage.all import EllipticCurve, QQ, ZZ
from collections import Counter
import argparse, sys

ap=argparse.ArgumentParser()
ap.add_argument('--full',action='store_true',help='compare all 5671 plus pairs')
opts=ap.parse_args()
p=107
n=p*p
N=389
compact="222224232123221232321222312332210011221232131210022222211110222242322222111220000112210221101334422332132111111111323233121211220222323121333422232134222244424332233424333433333443223233222010022220010222332322344333334333424332233424442222431232224333121323222022112121332323111111111231233224433101122012211000022111222223242222011112222220012131232122110012233213222123232122321232422222"
assert len(compact)==390
V=[int(c)-2 for c in compact]
INV=[0]+[pow(a,-1,N) for a in range(1,N)]
def manin_sym(a):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a;s=V[N]
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
    return ZZ(s)

E=EllipticCurve(QQ,[0,1,1,-2,0])
assert E.conductor()==389
assert E.ap(p)==0
M=E.modular_symbol(sign=+1,implementation='eclib')
# Avoid hidden normalization assumptions: exact QQ evaluation, not mod-p conversion.
points=[a for a in range(1,(n-1)//2+1) if a%p]
if not opts.full:
    # Rational independent samples distributed through the full range.
    ids=sorted(set([0,1,2,3,4,5,10,20,50,100,500,1000,2000,3000,4000,5000,len(points)-1]))
    points=[points[i] for i in ids]
ratio=None; zeros=0
C=[0,0,0]; Cp=[0,0,0]; counts=Counter()
for i,a in enumerate(points):
    raw=manin_sym(a)
    measured=QQ(M(QQ(a)/n))
    if raw==0:
        assert measured==0,('zero discrepancy',a,raw,measured)
        zeros+=1
    else:
        r=measured/raw
        counts[str(r)]+=1
        if ratio is None: ratio=r
        assert r==ratio,('variable scale',a,ratio,r)
    k=(-(pow(a,p-1,n)-1)//p)%p
    if measured.denominator()%p==0:raise ArithmeticError(('nonintegral p symbol',a,measured))
    # independently accumulate the two conductor p² moments.
    for output, symbol in ((C,raw),(Cp,measured)):
        mm=int((symbol.numerator()%p)*pow(int(symbol.denominator()%p),-1,p)%p)
        output[0]=(output[0]+2*mm)%p
        output[1]=(output[1]+2*mm*k)%p
        output[2]=(output[2]+mm*k*(k-1))%p
    if i%1000==0:print('P107_ECLIB_PROGRESS',i,len(points),flush=True)
print('P107_ECLIB_MATCH_COUNT',len(points),'zeros',zeros,'ratio',ratio,'ratio_counts',dict(counts),flush=True)
print('P107_ECLIB_PARTIAL_MOMENTS',C,'eclib',Cp,flush=True)
if opts.full:
    assert len(points)==5671
    assert C==[0,0,86],C
    assert ratio is not None
    # Formula of the normalized plus modular symbol in Sage measure must
    # still be matched with _quotient_of_periods / real components = 2.
    print('P107_ECLIB_FULL_MOMENTS',Cp,'signed_candidate',(-Cp[2]*pow(2,-1,p))%p)
    if ratio==1:
        print('P107_EXACT_ECLIB_VECTOR_EQUALITY_PASS')
    else:
        print('P107_EXACT_ECLIB_VECTOR_SCALE',ratio,'CHECK_PERIOD_NORMALIZATION')
else:
    print('SCOPE: spot-only; rerun --full to certify all 5671 representatives.')
print('SCOPE: raw eclib plus symbols vs archived vector; signed main conjecture not executed.')
