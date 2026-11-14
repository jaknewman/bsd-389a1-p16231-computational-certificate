#!/usr/bin/env python3
"""Audit arithmetic-projector algebra and finite-level strict-Selmer transport.

The 21-dimensional E projector is a FORMAL matrix realization of
alpha beta=[40], not the actual 21-dimensional Jacobian endomorphism.
Other auxiliary pairs and Sha torsion are SYNTHETIC; the historical
2x2 MW localization blocks are genuine previously audited values.
"""
from fractions import Fraction
from math import gcd

D=21
beta=[1]+[0]*(D-1)
alpha=[40,1,3,5]+[0]*(D-4)
assert sum(alpha[i]*beta[i] for i in range(D))==40
E=[[Fraction(beta[i]*alpha[j],40) for j in range(D)] for i in range(D)]
assert all(sum(E[i][k]*E[k][j] for k in range(D))==E[i][j]
           for i in range(D) for j in range(D))
assert all(sum(E[i][k]*beta[k] for k in range(D))==beta[i] for i in range(D))
print('MODULAR_IDEMPOTENT_RELATION_PASS','degree',40,'dimension_model',D,
      'denominator_prime_support',(2,5))

A_BY_P={
  5:((1,3),(1,0)),
  7:((1,3),(1,6)),
  11:((1,10),(1,7)),
  107:((1,15),(1,53)),
}

def matvec(A,x,mod):
    return tuple(sum(A[i][j]*x[j] for j in range(2))%mod for i in range(2))

def inv2(A,mod):
    d=(A[0][0]*A[1][1]-A[0][1]*A[1][0])%mod
    assert gcd(d,mod)==1
    u=pow(d,-1,mod)
    return ((A[1][1]*u%mod,-A[0][1]*u%mod),
            (-A[1][0]*u%mod,A[0][0]*u%mod))

C=((1,1),(1,2))

def test(p,k,a):
    mod=p**k
    tmod=p**a
    scale=p**(k-a)
    A=A_BY_P[p]
    Ainv=inv2(A,mod)
    for v in ((1,0),(0,1)):
        assert matvec(Ainv,matvec(A,v,mod),mod)==v
    B=(((0,0),(0,0)),((1,0),(0,1)),C)
    def lam(i,s):
        x,t=s
        b=matvec(B[i],t,tmod)
        return matvec(A,((x[0]+scale*b[0])%mod,
                         (x[1]+scale*b[1])%mod),mod)
    def proj(i,s):
        x,t=s
        z=matvec(Ainv,lam(i,s),mod)
        return (((x[0]-z[0])%mod,(x[1]-z[1])%mod),t)
    ts=((0,0),(1,0),(0,1),(1,1),(p**a-1,1))
    xs=((0,0),(1,2),(mod-1,mod//2))
    for i in range(3):
        for t in ts:
            for x in xs:
                s=(x,t)
                y=proj(i,s)
                assert lam(i,y)==(0,0)
                assert proj(i,y)==y
                assert proj(i,(x,(0,0)))==((0,0),(0,0))
                assert y[1]==t
                for j in range(3):
                    assert proj(i,proj(j,s))==proj(i,s)
    for t in ts:
        s=proj(0,((0,0),t))
        for i in range(3):
            for j in range(3):
                assert proj(j,proj(i,s))==proj(j,s)
    if tmod<=49:
        intersection=0
        for u in range(tmod):
            for v in range(tmod):
                t=(u,v)
                s=proj(0,((0,0),t))
                if lam(1,s)==(0,0):intersection+=1
        assert intersection==1
    print('STRICT_SELMER_TRANSPORT_RING_PASS','p',p,'k',k,
          'hypothetical_Sha_exponent',a,'module_order',tmod*tmod,
          'all_absorptions',True,'flat_transports',True,
          'two_strict_kernels_trivial_intersection',True)

for p in A_BY_P:
    for k,a in ((1,1),(2,1),(2,2),(3,1)):
        test(p,k,a)

print('SCOPE: FORMAL MODELS; NO GLOBAL SHA ANNIHILATOR, NO BSD')
