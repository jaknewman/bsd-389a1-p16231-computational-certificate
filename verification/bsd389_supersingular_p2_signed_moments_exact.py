#!/usr/bin/env python3
"""389a1: exact supersingular p^2 cyclotomic moments from one integral Manin vector.

Self-contained pure Python. Input is a previously archived, independently
verified 390-entry *integer* level-389 plus modular-symbol edge vector.
The p=599 original Sage/eclib data are a distinct source of corroboration.

This program computes a NONCONJECTURAL finite theta moment. The implication
to Sha[p^infty]=0 uses published signed-main-conjecture and finite-submodule
theorems and the source-matched Pollack-plus normalization, audited in the
associated paper. No uniform-in-p nonvanishing is asserted.

Usage:
 python verification/bsd389_supersingular_p2_signed_moments_exact.py --p 1049
 python verification/bsd389_supersingular_p2_signed_moments_exact.py --p 2957
 python verification/bsd389_supersingular_p2_signed_moments_exact.py --p 6661
 python verification/bsd389_supersingular_p2_signed_moments_exact.py --p 8263
"""
import argparse
import hashlib
import json
from math import isqrt

N=389
COMPACT="222224232123221232321222312332210011221232131210022222211110222242322222111220000112210221101334422332132111111111323233121211220222323121333422232134222244424332233424333433333443223233222010022220010222332322344333334333424332233424442222431232224333121323222022112121332323111111111231233224433101122012211000022111222223242222011112222220012131232122110012233213222123232122321232422222"
assert len(COMPACT)==390
V=tuple(int(z)-2 for z in COMPACT)
assert V[-1]==0 and all(-2<=v<=2 for v in V)
INV=[0]+[pow(j,-1,N) for j in range(1,N)]
EXPECTED={599:(543,28),1049:(202,948),2957:(410,2752),
          6661:(2995,1833),8263:(4734,5896)}

def is_prime(p):
    return p>2 and p%2 and all(p%k for k in range(3,isqrt(p)+1,2))

def a_p(p):
    # Discriminant in y: 1+4(x^3+x^2-2x).
    s=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        if not d:continue
        s+=1 if pow(d,(p-1)//2,p)==1 else -1
    return -s

def symbol_mod_p(a,den,p):
    assert 0<a<den and a%p
    pn,pd,ln,ld=1,0,0,1
    u,v=den,a
    res=V[N]
    while v:
        q,r=divmod(u,v)
        u,v=v,r
        nn=q*ln+pn;nd=q*ld+pd
        det=ln*nd-nn*ld
        assert det in (-1,1)
        c,d=(ld,nd) if det==1 else (nd,ld)
        c%=N;d%=N
        res+=det*V[(d*INV[c])%N if c else N]
        pn,pd,ln,ld=ln,ld,nn,nd
    assert (ln,ld)==(a,den)
    return res%p

def coefficients(p, limit=0):
    assert is_prime(p) and p>3 and a_p(p)==0, 'require genuine supersingular p'
    n=p*p;end=(n-1)//2
    if limit:
        if limit<1:raise ValueError('limit must be positive')
        end=min(end,limit)
    inv=[0]*p
    inv[1]=1
    for r in range(2,p):
        inv[r]=(p-(p//r)*inv[p%r]%p)%p
    h=[0]*p
    for r in range(1,p):
        teich=pow(r,p,n)
        assert teich%p==r
        h[r]=(teich-r)//p
    for a in (1,2,3,13,p+1,p+13,(n-1)//2):
        r=a%p
        if not r:continue
        j=(((a-r)//p-h[r])*inv[r])%p
        old=(-((pow(a,p-1,n)-1)//p))%p
        assert j==old,('Fermat_quotient_inconsistent',p,a,j,old)
    moments=[0,0,0]
    count=0
    for a in range(1,end+1):
        r=a%p
        if r==0:continue
        t=(a-r)//p
        j=((t-h[r])*inv[r])%p
        v=symbol_mod_p(a,n,p)
        moments[0]=(moments[0]+2*v)%p
        moments[1]=(moments[1]+2*v*j)%p
        moments[2]=(moments[2]+v*j*(j-1))%p
        count+=1
    complete=end==(n-1)//2
    if complete:
        assert count==p*(p-1)//2
        assert moments[0]==moments[1]==0
        c2=motions= moments[2]
        signed=-(c2*pow(2,-1,p))%p
        assert (p not in EXPECTED) or EXPECTED[p]==(c2,signed)
        return dict(p=p,ap=0,count=count,complete=True,
                    C0=0,C1=0,C2=c2,
                    Pollack_scalar_signed_coefficient_modp=signed,
                    unit=bool(signed),
                    input_manin390_sha256=hashlib.sha256(
                        bytes((v+2 for v in V))).hexdigest(),
                    theorem_scope='signed analytic coefficient gate; Sha implication uses the published theorems with checked local hypotheses')
    return dict(p=p,ap=0,count=count,complete=False,
                partial_moments_modp=moments,
                warning='PARTIAL_ONLY_NO_SHA_OR_SIGNED_L_COEFFICIENT_CONCLUSION')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--p',type=int,required=True)
    ap.add_argument('--limit',type=int,default=0,
                    help='0 means exhaustive; positive value is pilot only')
    args=ap.parse_args()
    print(json.dumps(coefficients(args.p,args.limit),sort_keys=True,indent=2))
if __name__=='__main__':main()
