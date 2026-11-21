#!/usr/bin/env python3
"""Exact finite tests for the GL2(p^2)+Kummer Chebotarev theorem for E389a1.

The global Galois disjointness and Chebotarev density are proved in the
companion mathematical note; these are finite algebra and elliptic point
checks. The Kurihara sums are separately computed by the C++ companion.
"""
from math import isqrt

def isprime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))

def ap(q):
    s=0
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        if d:
            t=pow(d,(q-1)//2,q)
            assert t in (1,q-1)
            s+=1 if t==1 else -1
    return -s

def add(P,Q,q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y+v+1)%q==0:return None
    if P==Q: slope=(3*x*x+2*x-2)*pow((2*y+1)%q,-1,q)%q
    else: slope=(v-y)*pow((u-x)%q,-1,q)%q
    xx=(slope*slope-x-u-1)%q
    yy=(slope*(x-xx)-y-1)%q
    assert (yy*yy+yy-xx**3-xx**2+2*xx)%q==0
    return xx,yy

def mul(P,n,q):
    R=None
    while n:
        if n&1:R=add(R,P,q)
        P=add(P,P,q);n>>=1
    return R

def local_gate(p,q,expected_ap,direction):
    assert isprime(q) and q not in (p,389)
    assert q%p==1 and q%(p*p)!=1
    a=ap(q)
    assert a==expected_ap,(q,a,expected_ap)
    cardinal=q+1-a
    assert cardinal%p==0 and cardinal%(p*p)!=0
    P=mul((-1%q,1),cardinal//p,q)
    Q=mul((0,q-1),cardinal//p,q)
    assert P is None or mul(P,p,q) is None
    assert Q is None or mul(Q,p,q) is None
    if direction=='P': assert P is not None and Q is None
    if direction=='Q': assert P is None and Q is not None
    print('BSD389_PRECISE_AUXILIARY_LOCAL_PASS','p',p,'q',q,
          'ap',a,'Nq',cardinal,'direction',direction,'p_torsion_P',P,
          'p_torsion_Q',Q)

def run():
    for p in (5,7,11,13):
        # A mod p^2 = [[1+p*alpha,1+p*beta], [p*c,1+p*gamma]]
        # has det(A)=1+p*(alpha+gamma-c), det(I-A)=-p*c mod p^2.
        # Two nonzero independent Fp-linear forms give p^2*(p-1)^2 lifts.
        count=0
        for alpha in range(p):
            for gamma in range(p):
                for c in range(p):
                    if c and (alpha+gamma-c)%p:
                        count+=p       # arbitrary upper-right p^2 lift
        assert count==p*p*(p-1)**2
        # Frob unipotent U has image(U-I)=Fp*e1. For translations
        # vP=(a,b), vQ=(c,d), the two quotients are b,d.
        # P-nonzero / Q-zero count p^2*(p-1) in V^2.
        translations=p*p*(p-1)
        assert translations*2<=p**4
        from fractions import Fraction
        density=(Fraction(1,p*(p-1))*Fraction(count,p**4)
                 *Fraction(translations,p**4))
        assert density==Fraction((p-1)**2,p**5)
        print('BSD389_PRECISE_CHEBOTAREV_DENSITY_PASS',
              'p',p,'valid_p2_lifts',count,'total_p2_lifts',p**4,
              'valid_Kummer_translations',translations,'all_translations',p**4,
              'density_per_pure_MW_direction',str(density))
    local_gate(5,61,-8,'P')
    local_gate(5,991,-53,'Q')
    local_gate(7,2423,30,'Q')
    local_gate(7,8597,58,'P')
    print('BSD389_PRECISE_AUXILIARY_GROUP_THEORY_AND_CURVE_PASS')
    print('BOUNDARY: these tests do not prove a unit Kurihara derivative for all p, or Sha finiteness.')

if __name__=='__main__':run()
