#!/usr/bin/env python3
"""Proof-grade rational interval for L(E^(-43),1) with E=389a1.

No floating point in proof; no external packages. Exact point counts, Hecke
recurrences, alternating Taylor bounds for exp, classical rational bounds
3.14159 < pi < 3.14160, and elementary exponential tail estimates.
"""
from fractions import Fraction as F
from math import isqrt


M=1500
N=389*43**2
assert 848**2 < N < 849**2
c_lo=F(2*314159,100000*849)
c_hi=F(2*314160,100000*848)
assert c_hi*M < 16

def compute_coefficients(M):
    spf=list(range(M+1))
    for p in range(2,isqrt(M)+1):
        if spf[p]==p:
            for i in range(p*p,M+1,p):
                if spf[i]==i:spf[i]=p

    def ap(p):
        if p==2:
            return p+1-(1+sum((y*y+y-x*x*x-x*x+2*x)%p==0 for x in range(p) for y in range(p)))
        total=0
        for x in range(p):
            rhs=(x*x*x+x*x-2*x)%p
            discr=(1+4*rhs)%p
            if discr:
                total+=1 if pow(discr,(p-1)//2,p)==1 else -1
        return -total
    traces={p:ap(p) for p in range(2,M+1) if spf[p]==p}
    # Quadratic reciprocity: chi_{-43}(n)=(n/43), since -43 is
    # a negative fundamental discriminant and 43 is prime.
    def character_prime(p):
        r=p%43
        return 0 if r==0 else (1 if pow(r,21,43)==1 else -1)
    assert traces[2]==-2 and traces[11]==-4 and traces[389]==1
    assert character_prime(11)==1 and character_prime(389)==-1 and character_prime(-389)==1
    a=[0]*(M+1);a[1]=1
    chi=[0]*(M+1);chi[1]=1
    for n in range(2,M+1):
        p=spf[n];q=n;e=0
        while q%p==0:
            q//=p;e+=1
        if e==1: factor=traces[p]
        elif p==389:factor=traces[p]**e
        else:
            previous_previous,previous=1,traces[p]
            for _ in range(2,e+1):
                previous_previous,previous=previous,traces[p]*previous-p*previous_previous
            factor=previous
        a[n]=a[q]*factor
        chi[n]=chi[q]*character_prime(p)**e
    return a,chi

def exponential_interval(n):
    # x=c*n; x/16 <1.  For 0<=y<=1:
    # 1-y+y^2/2-y^3/6 <= exp(-y) <= 1-y+y^2/2-y^3/6+y^4/24
    y_hi=c_hi*n/16
    y_lo=c_lo*n/16
    def P3(y):return 1-y+y*y/2-y*y*y/6
    def P4(y):return P3(y)+y**4/24
    lower=P3(y_hi)**16
    upper=P4(y_lo)**16
    assert 0 < lower <= upper <=1
    return lower,upper

if __name__=='__main__':
    a,chi=compute_coefficients(M)
    lower=F(0)
    upper=F(0)
    for n in range(1,M+1):
        lo,hi=exponential_interval(n)
        factor=F(2*a[n]*chi[n],n)
        if factor>=0:
            lower+=factor*lo
            upper+=factor*hi
        else:
            lower+=factor*hi
            upper+=factor*lo
    # |a_n| <= d(n)*sqrt(n) <= 2n, chi bounded by 1:
    # |tail| <= 4*exp[-c(M+1)]/(1-exp[-c])
    # exp[-t] <= (1+t/16)^(-16), 1-exp[-c]>=c/(1+c)
    tail=4*(1+c_lo)/c_lo/(1+c_lo*(M+1)/16)**16
    complete_lo=lower-tail
    complete_hi=upper+tail
    def dec(v):return f"{float(v):.15f}"
    print('N_TWIST',N,'M',M,'AP2',-2,'AP11',-4,'AP389',1)
    print('PI_AND_SQRT_RATIONAL_BOUNDS_PASS',c_lo,c_hi)
    print('PARTIAL_L_INTERVAL',dec(lower),dec(upper))
    print('EXPLICIT_TAIL_BOUND',dec(tail))
    print('COMPLETE_L_INTERVAL',dec(complete_lo),dec(complete_hi))
    assert F(10) < complete_lo < complete_hi < F(11)
    print('TWIST_MINUS43_L_INTERVAL_10_TO_11_RATIONAL_CERTIFICATE_PASS')
    print('SCOPE: under modular functional equation and root number +1; no BSD proof')
