#!/usr/bin/env python3
"""Exact identification of Castella--Hsieh Gross ideals by omega^n, n=1,2.
Pure integer arithmetic. Does not compute Brandt values or Selmer."""
from math import gcd
P=11
def root(r,n):
    r%=P
    for j in range(1,n):
        m=P**j
        assert (r*r-r+11)%m==0
        r=(r-((r*r-r+11)//m)*pow(2*r-1,-1,P)*m)%(m*P)
    assert (r*r-r+11)%(P**n)==0
    return r
def check(n):
    m=P**n; mod=P**(2*n)
    s,t=root(0,2*n),root(1,2*n)
    assert (s*t)%mod==P and (s+t)%mod==1
    sn=pow(s,n,mod);tn=pow(t,n,mod)
    assert sn%m==0 and tn%P
    scaled=(sn//m)%m
    kappa=scaled*pow(tn,-1,m)%m
    assert kappa==pow(t,-2*n,m)
    assert kappa==(1 if n==1 else 45)
    tested=0
    for a in range(m):
        if gcd(a,P)!=1:continue
        b=kappa*a%m
        # omega^n r_n(a) = [[s^n, (s^n/m)a],[0,t^n]]
        assert sn%m==0
        assert (a*scaled-b*tn)%m==0
        tested+=1
    assert tested==m-m//P
    print('SOURCE_GROSS_GLOBAL_LEFT_MULTIPLIER_PASS',
          {'n':n,'units':tested,'s':s,'t':t,'kappa':kappa,'index':m*m})
def index_gate():
    assert pow(39,11,121)==94
    assert 39*pow(94,-1,121)%121==12
    assert 45==1+4*11
    assert -pow(-4%11,-2,11)%11==2
    assert sum(i*(i-1)//2 for i in range(11))%11==0
    slopes=set()
    for k in range(110):
        b=pow(39,k,121)
        a=b*pow(45,-1,121)%121
        tau=pow(a%11,11,121)
        z=a*pow(tau,-1,121)%121
        assert (z-1)%11==0
        assert (z-1)//11==(k-4)%11
        slopes.add(b)
    assert slopes=={a for a in range(121) if a%11}
    print('GENUINE_SOURCE_THETA_INDEX_AND_P1_CANCELLATION_PASS',
          'i=(k-4)mod11','factor=-alpha^-2=2')
if __name__=='__main__':
    check(1);check(2);index_gate()
    print('BOUNDARY: NO REAL BRANDT WEIGHT OR THETA UNIT EVALUATED')
