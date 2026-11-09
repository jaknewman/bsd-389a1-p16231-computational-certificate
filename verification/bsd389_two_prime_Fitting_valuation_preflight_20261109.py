#!/usr/bin/env python3
"""E=389a1 two-prime Kurihara-integrality preflight (no Sage needed).

Inputs delta and its normalization MUST be independently verified.
Checks local conductor admissibility via exact finite-field point counts.
The Sha bound then uses published theorems of Kim / Castella--Sano
and Cassels--Tate. Does not recalculate any Kurihara sums.
"""
import argparse
import json
from math import isqrt

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def frobenius(q):
    assert prime(q) and q>2 and q!=389
    chi=[-1]*q
    chi[0]=0
    for y in range(1,q): chi[y*y%q]=1
    return -sum(chi[(1+4*(x*x*x+x*x-2*x))%q] for x in range(q))

def vp(n,p):
    if n==0:return 10**9
    n=abs(n);i=0
    while n%p==0:
        n//=p;i+=1
    return i

def audit(p,q1,q2,delta):
    assert p>=5 and prime(p) and p!=389
    assert q1!=q2 and all(prime(q) and q not in (2,p,389) for q in (q1,q2))
    cert=[]
    for q in (q1,q2):
        a=frobenius(q)
        count=q+1-a
        h=min(vp(q-1,p),vp(count,p))
        assert h>=1,(q,a,count,'NOT_KURIHARA_ADMISSIBLE')
        cert.append(dict(prime=q,trace=a,order=count,modulus_exponent=h))
    h=min(c['modulus_exponent'] for c in cert)
    assert 0<=delta<p**h
    out={'curve':'389a1','p':p,'auxiliary':cert,
         'integral_precision':h,'delta_assumed_independently_certified':delta}
    if delta==0:
        out.update(status='ZERO_AT_THIS_PRECISION',sha_conclusion='NONE')
    else:
        k=vp(delta,p)
        assert k<h
        out.update(status='NONZERO_AT_THIS_PRECISION',valuation=k,
                   sha_exponent_divides=p**(k//2),
                   sha_order_exponent_bound=2*(k//2),
                   sha_zero_if_valuation_0_or_1=(k<=1),
                   source='Kim Th 1.1 + Castella-Sano Th B + Cassels-Tate',
                   sha_conclusion='CONDITIONAL_ON_EXTERNAL_DELTA_AND_PUBLISHED_THEOREMS')
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--q1',type=int,required=True)
    parser.add_argument('--q2',type=int,required=True)
    parser.add_argument('--delta',type=int,required=True)
    args=parser.parse_args()
    print(json.dumps(audit(args.p,args.q1,args.q2,args.delta),indent=2,sort_keys=True))
