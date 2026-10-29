#!/usr/bin/env python3
"""Independent full-sum audit at p=5 and bounded two-prime search at p=7.
Run: python -u verification/kurihara_small_pair_audit.py --bound 600 --max-pairs 20
Requires SageMath Python. All conclusions conditional on matching normalization.
"""
import argparse
from itertools import combinations
from sage.all import EllipticCurve, QQ, ZZ, prime_range, GF
from sage.libs.eclib.newforms import ECModularSymbol

def dlog_table(q,p):
    g=int(GF(q).multiplicative_generator())
    out=bytearray(q) if p <256 else [0]*q
    a=1
    for k in range(q-1):
        out[a]=k%p
        a=a*g%q
    assert a==1 and pow(g,(q-1)//p,q)!=1
    return out,g

def kurihara(symbol,p,q1,q2, cache, half=True):
    n=q1*q2
    t1,g1=cache[q1]; t2,g2=cache[q2]
    # E=389a1 has positive discriminant; this code uses eclib scale 1.
    assert ((q1-1)//2)%p==0 and ((q2-1)//2)%p==0
    total=0
    end=(n-1)//2 if half else n-1
    for a in range(1,end+1):
        r1,r2=a%q1,a%q2
        if r1==0 or r2==0:continue
        weight=t1[r1]*t2[r2]%p
        if not weight:continue
        v=QQ(symbol(QQ(a)/n))
        denominator=int(v.denominator())
        if denominator%p==0:raise ValueError(('bad-denominator',p,q1,q2,a,v))
        z=int(v.numerator())*pow(denominator,-1,p)%p
        total=(total+weight*z)%p
    return (2*total if half else total)%p

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bound',type=int,default=600)
    ap.add_argument('--max-pairs',type=int,default=20)
    ap.add_argument('--max-level',type=int,default=250000)
    args=ap.parse_args()
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    symbol=ECModularSymbol(E,sign=1)
    # Independent direct full residue enumeration, deliberately no a->n-a pairing.
    cache5={q:dlog_table(q,5) for q in (41,61)}
    v=kurihara(symbol,5,41,61,cache5,half=False)
    print('P5_DIRECT_FULL_AUDIT',v,'MATCH_EXPECTED_4',v==4,flush=True)
    if v!=4:raise AssertionError('Mismatch: do not use p5 certificate')
    p=7
    qs=[int(q) for q in prime_range(3,args.bound+1) if (q-1)%p==0 and q!=389 and int(E.ap(q)-q-1)%p==0]
    print('P7_ADMISSIBLE',qs,flush=True)
    cache={q:dlog_table(q,p) for q in qs}
    attempted=0
    for q1,q2 in combinations(qs,2):
        n=q1*q2
        if n>args.max_level:continue
        attempted+=1
        value=kurihara(symbol,p,q1,q2,cache,half=True)
        print('P7_COMPLETE',q1,q2,n,value,flush=True)
        if value:
            # Independent direct enumeration to check reduction by half.
            direct=kurihara(symbol,p,q1,q2,cache,half=False)
            print('P7_NONZERO_WITNESS',q1,q2,'DELTA',value,'DIRECT',direct,'AGREES',direct==value,flush=True)
            if direct!=value:raise AssertionError('full vs half mismatch')
            return
        if attempted>=args.max_pairs:break
    print('P7_NO_WITNESS_IN_TESTED_PAIRS',attempted,flush=True)
if __name__=='__main__':main()