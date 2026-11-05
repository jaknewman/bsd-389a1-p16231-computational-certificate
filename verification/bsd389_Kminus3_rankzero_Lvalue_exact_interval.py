#!/usr/bin/env python3
"""Exact rational interval certificate 4.51 < L(E389a1^(-3),1) < 4.60.

Only Python standard library; uses the centered approximate functional
equation of an elliptic newform twisted by chi_-3, root number +1,
and fully rational rigorous upper/lower bounds.
"""
from fractions import Fraction as F

M = 64
N = 389 * 9
assert N == 3501
assert F(59169,1000)**2 < N < F(59170,1000)**2
alpha_lo = 2*F(223,71)/F(59170,1000)
alpha_hi = 2*F(22,7)/F(59169,1000)
assert 0 < alpha_lo < alpha_hi < F(1,8)

def factor(n):
    fac=[]; q=2
    while q*q<=n:
        if n%q==0:
            e=0
            while n%q==0:
                n//=q; e+=1
            fac.append((q,e))
        q+=1
    if n>1: fac.append((n,1))
    return fac

def trace_prime(p):
    if p==2:
        count=1+sum((y*y+y-x*x*x-x*x+2*x)%2==0
                    for x in range(2) for y in range(2))
        return 3-count
    s=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        if d:
            v=pow(d,(p-1)//2,p)
            assert v in (1,p-1)
            s+=1 if v==1 else -1
    return -s

traces={q:trace_prime(q) for q in range(2,M+1)
        if len(factor(q))==1 and factor(q)[0][1]==1}
assert trace_prime(389)==1
def chi_minus3(n):
    return 0 if n%3==0 else (1 if n%3==1 else -1)
assert chi_minus3(-389)==1

def a_n(n):
    out=1
    for q,e in factor(n):
        a0,a1=1,traces[q]
        for _ in range(2,e+1):
            a0,a1=a1,traces[q]*a1-q*a0
        out*=a1
    return out

def S(x,k):
    out=term=F(1)
    for n in range(1,k+1):
        term*=-x/n
        out+=term
    return out

lo=hi=F(0)
for n in range(1,M+1):
    c=F(2*a_n(n)*chi_minus3(n),n)
    xlo=alpha_lo*n/16
    xhi=alpha_hi*n/16
    assert 0<=xlo<=xhi<1
    elo=S(xhi,9)**16
    ehi=S(xlo,8)**16
    assert 0<elo<=ehi
    if c>=0:
        lo+=c*elo
        hi+=c*ehi
    else:
        lo+=c*ehi
        hi+=c*elo

# Deligne bound |a_n|<=d(n)*sqrt(n), d(n)<=2sqrt(n),
# implying |a_n|/n<=2. Tail of 2*sum a_n chi(n)e^(-alpha*n)/n.
beta=S(alpha_lo,8)
tail=4*S(alpha_lo*(M+1)/16,8)**16/(1-beta)
assert 0<beta<1 and tail>0
LOW=lo-tail
HIGH=hi+tail
assert LOW>F(451,100) and HIGH<F(46,10)
print("TWIST_MINUS3_CONDUCTOR",N)
print("E389_AP389_SPLIT_MULT_ROOT_PLUS_PASS")
print("TWIST_MINUS3_ROOT_PLUS_PASS")
print("RATIONAL_PARTIAL_LOWER",format(float(lo),".12f"))
print("RATIONAL_PARTIAL_UPPER",format(float(hi),".12f"))
print("RATIONAL_TAIL_UPPER",format(float(tail),".12f"))
print("L_E_MINUS3_1_STRICT_BOUNDS_PASS 4.51 < L < 4.60")
print("L_E_MINUS3_1_NONZERO_RIGOROUS_PASS")
print("BOUNDARY_AUXILIARY_RANKIN_VALUE_NOT_EXPLICITLY_CERTIFIED")
