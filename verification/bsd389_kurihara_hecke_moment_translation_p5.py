#!/usr/bin/env python3
"""Exact p5 Manin/eclib regression for Hecke marginal cancellation.

Uses the actual Neron-normalized modular symbol of 389a1. Validates
Hecke fibre identities, vanishing lower logarithmic moments, and
translation invariance of the mixed Kurihara coefficient.
A p5 test, not a p599 or Sha certificate.
"""
import math
from sage.all import QQ, ZZ, EllipticCurve
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin

P,Q1,Q2=5,41,61
N=Q1*Q2

def logs(q):
    factors=[int(x) for x in ZZ(q-1).prime_divisors()]
    g=next(a for a in range(2,q) if all(pow(a,(q-1)//d,q)!=1 for d in factors))
    x=1; out=[0]*q
    for i in range(q-1):
        out[x]=i%P
        x=x*g%q
    assert x==1
    return g,out

def main():
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    phi=ECModularSymbol(E,sign=1)
    tab=table_390(phi,P)
    assert (int(E.ap(Q1)),int(E.ap(Q2)))==(-3,-8)
    print('K5_HECKE_AQ_PASS',Q1,int(E.ap(Q1)),Q2,int(E.ap(Q2)),flush=True)
    S=[0]*N
    for a in range(1,N):
        if math.gcd(a,N)==1:
            S[a]=int(symbol_by_manin(a,N,P,tab))
    symbols1={b:int(symbol_by_manin(b,Q1,P,tab)) for b in range(1,Q1)}
    symbols2={b:int(symbol_by_manin(b,Q2,P,tab)) for b in range(1,Q2)}
    buckets1=[0]*Q1; buckets2=[0]*Q2
    for a in range(1,N):
        if math.gcd(a,N)==1:
            buckets1[a%Q1]=(buckets1[a%Q1]+S[a])%P
            buckets2[a%Q2]=(buckets2[a%Q2]+S[a])%P
    for q,other,symbols,buckets in [(Q1,Q2,symbols1,buckets1),(Q2,Q1,symbols2,buckets2)]:
        iq=pow(other,-1,q)
        ao=int(E.ap(other))
        for b in range(1,q):
            rhs=(ao*symbols[b]-symbols[b*other%q]-symbols[b*iq%q])%P
            assert buckets[b]==rhs,('Hecke fibre mismatch',q,other,b,buckets[b],rhs)
        print('K5_HECKE_ALL_FIBRES_PASS','modulus',q,'checked',q-1,flush=True)
    g1,L1=logs(Q1);g2,L2=logs(Q2)
    assert (g1,g2)==(6,2)
    moments=[0]*4
    for a in range(1,N):
        if not S[a]:continue
        u,v=L1[a%Q1],L2[a%Q2]
        for j,mult in enumerate((1,u,v,u*v)):
            moments[j]=(moments[j]+S[a]*mult)%P
    assert moments==[0,0,0,4],moments
    print('K5_HECKE_LOWER_LOG_MOMENTS_ZERO_PASS',moments[:3],flush=True)
    print('K5_KURIHARA_MIXED_MOMENT_PASS',moments[3],flush=True)
    for t in (2,7,17,599):
        assert math.gcd(t,N)==1
        value=sum(L1[a%Q1]*L2[a%Q2]*S[t*a%N] for a in range(1,N) if math.gcd(a,N)==1)%P
        assert value==4,(t,value)
        print('K5_HECKE_TRANSLATION_INVARIANCE_PASS','t',t,'delta',value,flush=True)
    print('BOUNDARY: exact p5 regression only; no p599 delta or Sha result',flush=True)

if __name__ == '__main__':
    main()
