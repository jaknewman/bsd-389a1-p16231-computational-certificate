#!/usr/bin/env python3
"""Fixed chi9 on Pic(O_53) for E389a1: exact Frobenius regularity.

For rational split prime p=a²-ab+b², pi=a+b*omega,
r=pi/bar(pi)=pi²/p modulo 53; chi9(pfrak)!=1 iff r^6!=1.
Pic(O_53)=C18 and chi9 has order nine: Chebotarev density 4/9.

All arithmetic exact in F_53[omega], omega²+omega+1=0.
Finite census illustrates the proved density; does NOT prove
nonzero theta second jets, bounded global Sha or full BSD.
"""
from math import isqrt
Q=53

def mul(x,y):
    a,b=x;c,d=y
    return ((a*c-b*d)%Q,(a*d+b*c-b*d)%Q)

def power(x,n):
    z=(1,0)
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z

def rep(p):
    assert p>3 and p%3==1
    for b in range(1,isqrt(4*p//3)+2):
        D=4*p-3*b*b
        if D<0:break
        s=isqrt(D)
        if s*s==D and (b+s)%2==0:
            a=(b+s)//2
            assert a*a-a*b+b*b==p
            return a,b
    raise ArithmeticError(('NO_EISENSTEIN_REPRESENTATION',p))

def regular(p):
    a,b=rep(p)
    z=a%Q,b%Q
    pinv=pow(p,-1,Q)
    rr=tuple(t*pinv%Q for t in mul(z,z))
    assert power(rr,54)==(1,0)
    yes=power(rr,6)!=(1,0)
    # Choice of sixth root of unity for pi does not affect r^6.
    for u in ((1,0),(Q-1,0),(0,1),(0,Q-1),
              (Q-1,Q-1),(1,1)):
        x=mul(z,u)
        test=tuple(t*pinv%Q for t in mul(x,x))
        assert (power(test,6)!=(1,0))==yes
    conjugate=(a-b)%Q,(-b)%Q
    cc=tuple(t*pinv%Q for t in mul(conjugate,conjugate))
    assert (power(cc,6)!=(1,0))==yes
    return yes,(a,b),rr

def primes(n):
    s=bytearray(b'\x01')*(n+1);s[0]=s[1]=0
    for p in range(2,isqrt(n)+1):
        if s[p]:s[p*p::p]=bytes(len(s[p*p::p]))
    return [p for p in range(2,n+1) if s[p]]

def main():
    sample=(7,13,19,31,37,43,61,73,97,109,223,1297,1579,2383,4423)
    for p in sample:
        yes,ab,r=regular(p)
        assert yes
        print('BSD389_CHI9_EXACT_FROBENIUS_PASS',
              'p',p,'pi',ab,'r_mod53',r,'regular',yes)
    for bound in (10000,50000,100000,200000):
        pp=primes(bound)
        eligible=sum(regular(p)[0] for p in pp if p%3==1)
        split=sum(p%3==1 for p in pp)
        print('BSD389_CHI9_CHEBOTAREV_CENSUS_PASS',
              'bound',bound,'all_primes',len(pp),
              'split_primes',split,
              'fixed_chi9_regular_primes',eligible,
              'theoretical_natural_density','4/9')
    print('BSD389_FIXED_CHI9_CHEBOTAREV_REGULARITY_PASS')
    print('BOUNDARY: no Gross-period rerun, theta T² nonvanishing, global Sha or BSD proof')

if __name__=='__main__':main()
