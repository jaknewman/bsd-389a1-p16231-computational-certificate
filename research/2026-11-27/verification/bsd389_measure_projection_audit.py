#!/usr/bin/env python3
"""Exact finite level p^2 tame-trivial cyclotomic projection for E389a1.

Compares raw modular-symbol coefficients with the *full* Mazur--Tate
unit-root-stabilized measure at level p^2, modulo p. The p-adic unit root
is reduced modulo p, so alpha == a_p mod p for ordinary good p; alpha=1
for split multiplicative p=389.

Does NOT by itself prove that this normalization agrees with an arithmetic
main conjecture or that Sha has been computed.
"""
import argparse
from math import comb
from pathlib import Path
from bsd389_standalone_p2_audit import load_table, modular_symbol

N=389

def ap(p):
    points=1
    for x in range(p):
        discr=(1+4*(x*x*x+x*x-2*x))%p
        if discr==0:
            points+=1
        elif pow(discr,(p-1)//2,p)==1:
            points+=2
    return p+1-points

def coeffs(p,tab,degree=4):
    n=p*p
    a_p=1 if p==389 else ap(p)
    assert a_p%p!=0,(p,'nonordinary')
    unitroot=a_p%p
    alpha_inv=pow(unitroot,-1,p)
    base=[0]*p
    for r in range(1,p):base[r]=modular_symbol(r,p,tab)
    raw=[0]*(degree+1)
    correction=[0]*(degree+1)
    for a in range(1,n):
        r=a%p
        if not r:continue
        j=(-((pow(a,p-1,n)-1)//p))%p
        v=modular_symbol(a,n,tab)
        for k in range(degree+1):
            c=comb(j,k) if j>=k else 0
            raw[k]=(raw[k]+v*c)%p
            correction[k]=(correction[k]+base[r]*c)%p
    normalized=[(pow(alpha_inv,2,p)*raw[k]-pow(alpha_inv,3,p)*correction[k])%p for k in range(degree+1)]
    expected=[(pow(alpha_inv,2,p)*x)%p for x in raw]
    print('P',p,'AP',a_p,'ALPHA_MODP',unitroot,'RAW',raw,'CORRECTION',correction,
          'MEASURE',normalized,'SIMPLE_UNIT_SCALED',expected,'MATCH',normalized==expected,flush=True)
    assert normalized==expected
    assert all(x==0 for x in correction[:min(degree+1,p-1)])
    return raw,correction,normalized

if __name__=='__main__':
    z=argparse.ArgumentParser()
    z.add_argument('--primes',type=int,nargs='+',default=[5,7,11,13,17,89,389])
    opts=z.parse_args()
    tab=load_table(Path(__file__).with_name('manin_390.txt'))
    for p in opts.primes:
        assert p>=5
        if p==389:
            raw,corr,measure=coeffs(p,tab,3)
            assert raw==[0,0,0,321]
        else:
            raw,corr,measure=coeffs(p,tab,2)
            assert raw[0]==raw[1]==0 and measure[2]!=0
    print('MEASURE_TAME_TRIVIAL_LEVEL_P2_NORMALIZATION_PASS',flush=True)
