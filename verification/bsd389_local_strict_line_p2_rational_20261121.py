#!/usr/bin/env python3
"""Exact E389a1 local strict-Mordell--Weil line modulo p^2.

This computes lambda_p = log_p(Q)/log_p(P) mod p^2 from exact
rational elliptic point addition. The formal parameter t=-x/y
satisfies log_E(t)=t+O(t^3) at p>=5 (a1=0), and for
R=[#E(F_p)]P, t(R) is divisible by p. Thus exact t mod p^3
determines log_E(R)/p mod p^2. No global Selmer/Fitting
nonvanishing is deduced from these local computations.

This code does NOT compute or verify the published theta values.
"""
from fractions import Fraction as F
from math import gcd

N={5:9,7:13,11:16}
EXPECTED={5:(18,1,7),7:(16,46,9),11:(41,35,113)}

def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u and y+v==-1: return None
    if P==Q:
        lam=(3*x*x+2*x-2)/(2*y+1)
    else:
        lam=(v-y)/(u-x)
    xx=lam*lam-1-x-u
    yy=lam*(x-xx)-y-1
    assert yy*yy+yy==xx*xx*xx+xx*xx-2*xx
    return xx,yy

def mul(P,k):
    R=None
    while k:
        if k&1: R=add(R,P)
        P=add(P,P)
        k//=2
    return R

def mod_frac(q,m):
    assert gcd(q.denominator,m)==1
    return q.numerator*pow(q.denominator,-1,m)%m

def run():
    for p,npoints in N.items():
        readings=[]
        for pt in ((F(-1),F(1)),(F(0),F(-1))):
            R=mul(pt,npoints)
            assert R is not None
            x,y=R
            t=mod_frac(-x/y,p**3)
            assert t%p==0 and (t//p)%p!=0
            readings.append(t//p)
        lam=readings[1]*pow(readings[0],-1,p*p)%(p*p)
        assert (readings[0],readings[1],lam)==EXPECTED[p]
        print("BSD389_STRICT_LOCAL_LOG_LIFT_PASS",
              "p",p,"N",npoints,
              "tP_over_p_mod_p2",readings[0],
              "tQ_over_p_mod_p2",readings[1],
              "lambda_mod_p2",lam,"lambda_mod_p",lam%p)
    print("BSD389_STRICT_LOCAL_LINE_PASS")
    print("BOUNDARY: local MW line, no claim about global Fitting or Sha.")

if __name__=="__main__":
    run()
