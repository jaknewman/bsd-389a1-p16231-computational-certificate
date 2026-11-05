#!/usr/bin/env python3
"""Exact rational-interval L(E389a1 quadratic twist by -3, 1)>4.51.
Python stdlib only. Assumes standard modularity/functional equation, Deligne
coefficient bound and conductor 3501 of the quadratic twist.
"""
from fractions import Fraction as F

M=64
N=389*9
assert F(59169,1000)**2 < N < F(59170,1000)**2
# Archimedes: 223/71 < pi < 22/7
alo=2*F(223,71)/F(59170,1000)
ahi=2*F(22,7)/F(59169,1000)
assert F(0)<alo<ahi<F(1,8)

def trace(p):
    # E: y^2+y=x^3+x^2-2x.
    if p==2:
        points=1+sum((y*y+y-x*x*x-x*x+2*x)%2==0 for x in range(2) for y in range(2))
        return 3-points
    s=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        if d:
            z=pow(d,(p-1)//2,p)
            assert z in (1,p-1)
            s+=(1 if z==1 else -1)
    return -s

def factors(n):
    ans=[]
    q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0:
                n//=q;e+=1
            ans.append((q,e))
        q+=1
    if n>1:ans.append((n,1))
    return ans

primes={q:trace(q) for q in range(2,M+1) if factors(q)==[(q,1)]}
assert trace(389)==1  # split multiplicative at 389; w(E)=+1

def chi(n):
    return 0 if n%3==0 else (1 if n%3==1 else -1)
assert chi(-389)==1 # twist sign remains +1
def coeff(n):
    z=1
    for q,e in factors(n):
        a0,a1=1,primes[q]
        for _ in range(2,e+1):
            a0,a1=a1,primes[q]*a1-q*a0
        z*=a1
    return z
def Taylor(x,k):
    s=t=F(1)
    for j in range(1,k+1):
        t=-t*x/j;s+=t
    return s

# 0<x<1: Taylor_9(x)<=exp(-x)<=Taylor_8(x).
# Apply to x=alpha*n/16 and raise to the 16th power.
lo=hi=F(0)
for n in range(1,M+1):
    c=F(2*coeff(n)*chi(n),n)
    xhi=ahi*n/16
    xlo=alo*n/16
    assert 0<=xlo<=xhi<1
    el=Taylor(xhi,9)**16
    eu=Taylor(xlo,8)**16
    assert 0<el<=eu
    if c>=0:lo+=c*el;hi+=c*eu
    else:lo+=c*eu;hi+=c*el

# |a_n|<=d(n)*sqrt(n)<=2*n; thus tail <=
# 4*exp(-alpha*(M+1))/(1-exp(-alpha)), bounded rationally.
exp_a_upper=Taylor(alo,8)
tail=4*Taylor(alo*(M+1)/16,8)**16/(1-exp_a_upper)
assert exp_a_upper<1
LOW,HIGH=lo-tail,hi+tail
assert LOW>F(451,100) and HIGH<F(46,10)
print("E389A1_ROOT_PLUS_AND_TWIST_MINUS3_ROOT_PLUS_PASS")
print("TWIST_CONDUCTOR",N)
print("RATIONAL_PARTIAL_INTERVAL",format(float(lo),".12f"),format(float(hi),".12f"))
print("RATIONAL_TAIL_UPPER",format(float(tail),".12f"))
print("L_E_MINUS3_1_RATIONAL_INTERVAL_PASS 4.51 < L < 4.60")
print("L_E_MINUS3_1_PROVABLY_NONZERO_PASS")
print("BOUNDARY_L_E_OVER_K_CHI_AND_THETA_ORDER2_NOT_PROVED")
print("BOUNDARY_SHA_P16231_NOT_PROVED")
