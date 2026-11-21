#!/usr/bin/env python3
"""Exact rational elliptic-Wieferich and local MW primitivity regressions.

Tests E=389a1 at p=223,419 for the two full-rank MW generators, and
the rank-one curve E=37a1 at p=179. Uses ONLY Fraction arithmetic:
no floating point, Sage or reduction of an approximate p-adic log.
Does not compute Galois wild inertia, class groups or Sha.
"""
from fractions import Fraction as F
from math import gcd

def add(A,B,a2,a4):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and y+v==-1:return None
    lam=((3*x*x+2*a2*x+a4)/(2*y+1) if A==B
         else (v-y)/(u-x))
    xx=lam*lam-a2-x-u
    yy=lam*(x-xx)-y-1
    assert yy*yy+yy==xx**3+a2*xx**2+a4*xx
    return xx,yy

def multiply(P,n,a2,a4):
    R=None
    while n:
        if n&1:R=add(R,P,a2,a4)
        P=add(P,P,a2,a4)
        n//=2
    return R

def ap(p,a2,a4):
    result=0
    for x in range(p):
        disc=(1+4*(x**3+a2*x*x+a4*x))%p
        if disc:
            legendre=pow(disc,(p-1)//2,p)
            assert legendre in (1,p-1)
            result += 1 if legendre==1 else -1
    return -result

def tmod(P,p,card,a2,a4,power=2):
    R=multiply(P,card,a2,a4)
    assert R is not None
    x,y=R
    t=-x/y
    m=p**power
    assert gcd(t.denominator,m)==1
    val=t.numerator*pow(t.denominator,-1,m)%m
    assert val%p==0
    return val

def run():
    points=((F(-1),F(1)),(F(0),F(-1)))
    for p,expected_ap,expected_pair in (
        (223,-5,(0,94)),(419,-35,(0,100))):
        a=ap(p,1,-2)
        assert a==expected_ap
        n=p+1-a
        assert n%p
        result=tuple(tmod(P,p,n,1,-2)//p for P in points)
        assert result==expected_pair,(p,result,expected_pair)
        assert result[0]==0 and result[1]%p
        print("BSD389_ELLIPTIC_WIEFERICH_P_LOCAL_PASS",
              "p",p,"ap",a,"N",n,
              "P_t_over_p",result[0],"Q_t_over_p",result[1],
              "Q_repairs_primitive_localization",True,flush=True)
    p=179
    a=ap(p,0,-1)
    assert a==18
    n=p+1-a
    assert n==162 and n%p
    t=tmod((F(0),F(0)),p,n,0,-1,power=3)
    assert t==18*p*p
    print("E37A1_INDEPENDENT_RANK_ONE_WIEFERICH_PASS",
          "p",p,"ap",a,"N",n,"t_mod_p3",t,
          "t_valuation",2,flush=True)
    print("BSD389_WILD_INERTIA_HYPOTHESIS_AUDIT_LOCAL_EXAMPLES_PASS")
    print("BOUNDARY: local logs do not establish tame vs wild E[p] or Sha.")

if __name__=="__main__":run()
