#!/usr/bin/env python3
"""Full p=11 Kurihara (397,991) via Sage/eclib and genuine 390-Manin symbols.

Run on Sage 10.9 Ubuntu, from repo root:
  python -u verification/bsd389_p11_kurihara_full_two_prime_sage_gate.py \
    2>&1 | tee ~/bsd389_p11_kurihara_full_gate.log

Intentionally NOT a claimed completed run. This computes all 392040 units,
including lower moments and independent half-sum agreement. Unlike a purely
archived δ, this re-evaluates every original modular-symbol argument.
"""
import math
import time
from sage.all import EllipticCurve, QQ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin, dlog
P,Q1,Q2=11,397,991
N=Q1*Q2

def direct(phi,a,n):
    v=QQ(phi(QQ(a)/n)); den=int(v.denominator())
    assert den%P
    return int(v.numerator())*pow(den,-1,P)%P

def main():
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    assert int(E.conductor())==389
    assert int(E.ap(Q1))==24 and int(E.ap(Q2))==-53
    assert int(E.ap(P))==-4
    assert math.gcd(Q1-1,int(E.ap(Q1))-Q1-1)==22
    assert math.gcd(Q2-1,int(E.ap(Q2))-Q2-1)==55
    assert (Q1-1)%P==(Q2-1)%P==0
    print('K11_ADMISSIBILITY_AND_I_N_MOD11_PASS','n',N,flush=True)
    phi=ECModularSymbol(E,sign=1)
    tab=table_390(phi,P)
    for a,n in ((1,41),(3,389),(1,N),(2,N),(17,N),(7919,N),
                (123457,N),(N-1,N)):
        if math.gcd(a,n)!=1:continue
        fast=int(symbol_by_manin(a,n,P,tab))
        assert fast==direct(phi,a,n),('Manin eclib mismatch',a,n)
    print('K11_DIRECT_ECLIB_MANIN390_SAMPLES_PASS',flush=True)
    L1,g1=dlog(Q1,P);L2,g2=dlog(Q2,P)
    theta=[0,0,0,0];h=0;cnt=hc=0
    start=time.monotonic()
    for a in range(1,N):
        r1,r2=a%Q1,a%Q2
        if r1==0 or r2==0:continue
        v=int(symbol_by_manin(a,N,P,tab));u=L1[r1];w=L2[r2]
        cnt+=1
        theta[0]=(theta[0]+v)%P
        theta[1]=(theta[1]+u*v)%P
        theta[2]=(theta[2]+w*v)%P
        theta[3]=(theta[3]+u*w*v)%P
        if a<=(N-1)//2:
            h=(h+u*w*v)%P;hc+=1
        if a%100000==1:
            print('K11_PROGRESS',a,'sum',theta[3],
                  'seconds',round(time.monotonic()-start,2),flush=True)
    assert (cnt,hc)==(392040,196020)
    assert theta[3]==2*h%P,('half_full_mismatch',theta,h)
    print('K11_HALF_FULL_EXACT_AGREEMENT_PASS',theta[3],h,
          'primitive_roots',g1,g2,flush=True)
    assert theta[:3]==[0,0,0],('unexpected_low_order_moments',theta)
    print('K11_LOWER_MOMENTS_ZERO_PASS',theta[:3],flush=True)
    if theta[3]==0:
        print('K11_DELTA_ZERO_RECHECK_EXTERNAL_NONVANISHING_CLAIM',flush=True)
        raise AssertionError('Kurihara coefficient 0; no unit certificate')
    print('K11_GENUINE_TWO_PRIME_KURIHARA_UNIT_PASS',theta[3],flush=True)
    print('K11_CONSEQUENCE_KIM_1_8_1_10_IF_RESIDUAL_MANIN_TAMAGAWA_GATES',flush=True)
    print('BOUNDARY_ONE_P_ONLY_NOT_GLOBAL_SHA_OR_COMPLEX_BSD',flush=True)

if __name__=='__main__':
    main()
