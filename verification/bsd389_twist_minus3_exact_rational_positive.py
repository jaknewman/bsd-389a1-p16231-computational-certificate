#!/usr/bin/env python3
"""Pure rational proof: 9/2 < L(389a1 quadratic twist by -3,1) < 23/5.
No Sage, sympy, mpmath, arbitrary precision decimal or floating-point arithmetic.
Uses 100 Hecke coefficients, Taylor rational intervals, Hasse tail.
The standard conductor/root sign gates are N=3501 and w=+1.
"""
from fractions import Fraction as F
PBOUND=100
TAYLOR=70
CLOW=F(53,500)
CHIGH=F(107,1000)

def primes(n):
    a=[True]*(n+1)
    a[0]=a[1]=False
    for i in range(2,int(n**0.5)+1):
        if a[i]:
            for j in range(i*i,n+1,i):a[j]=False
    return [i for i in range(2,n+1) if a[i]]

def a_prime(p):
    if p==2:
        count=1+sum((y*y+y-x*x*x-x*x+2*x)%2==0
                    for x in range(2) for y in range(2))
        return 3-count
    t=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        z=pow(d,(p-1)//2,p)
        t+=(0 if z==0 else (1 if z==1 else -1))
    return -t

def hecke_coefficients(M):
    ap={p:a_prime(p) for p in primes(M)}
    assert tuple(ap[p] for p in (2,3,5,7,11,13))==(-2,-2,-3,-5,-4,-3)
    an=[0]*(M+1)
    an[1]=1
    for n in range(2,M+1):
        q=n
        prod=1
        for p in ap:
            if p*p>q:break
            if q%p:continue
            k=0
            while q%p==0:
                q//=p
                k+=1
            pre,cur=1,ap[p]
            for j in range(2,k+1):
                pre,cur=cur,ap[p]*cur-p*pre
            prod*=cur
        if q>1:prod*=ap[q]
        an[n]=prod
    return an

def exp_interval(x):
    # Lagrange remainder e^-xi*x^(K+1)/(K+1)! <= x^(K+1)/(K+1)!
    term=F(1)
    val=F(1)
    for k in range(1,TAYLOR+1):
        term=-term*x/k
        val+=term
    err=abs(term*x)/(TAYLOR+1)
    return val-err,val+err

def main():
    # Classical Archimedes bounds 223/71 < pi < 22/7.
    assert F(591,10)**2<3501<F(592,10)**2
    assert (2*F(223,71)/F(592,10))>CLOW
    assert (2*F(22,7)/F(591,10))<CHIGH
    assert (-389)%3==1  # chi_{-3}(-389)=+1, so w(E^-3)=+1
    an=hecke_coefficients(PBOUND)
    slo,shi=F(0),F(0)
    nonzero=0
    for n in range(1,PBOUND+1):
        chi=0 if n%3==0 else (1 if n%3==1 else -1)
        v=chi*an[n]
        if not v:continue
        nonzero+=1
        lo,_=exp_interval(CHIGH*n)
        _,hi=exp_interval(CLOW*n)
        assert 0<lo<hi<1
        z=F(v,n)
        if z>0:
            slo+=z*lo
            shi+=z*hi
        else:
            slo+=z*hi
            shi+=z*lo
    # Hasse bound: |a_n|<=d(n)*sqrt(n)<=2*n;
    # e^(-c)<1/(1+c)<10/11, hence tail <=44*(10/11)^101.
    tail=44*F(10,11)**(PBOUND+1)
    low=2*slo-tail
    high=2*shi+tail
    assert tail<F(1,300)
    assert low>F(9,2) and high<F(23,5)
    print("BSD389_TWIST_MINUS3_EXACT_RATIONAL_POSITIVITY_PASS")
    print("TWIST_MINUS3_N_CONDUCTOR",3501,"ROOT_NUMBER",1)
    print("TWIST_MINUS3_DIRICHLET_TERMS",PBOUND,"NONZERO",nonzero)
    print("TWIST_MINUS3_RATIONAL_TAIL_BOUND_LESSTHAN_1_OVER_300",True)
    print("TWIST_MINUS3_L1_GREATER_THAN","9/2")
    print("TWIST_MINUS3_L1_LESS_THAN","23/5")
    print("TWIST_MINUS3_L1_RATIONAL_INTERVAL_DIAGNOSTIC",float(low),float(high))
    print("TWIST_MINUS3_L1_POSITIVE_UNCONDITIONAL_GIVEN_STANDARD_MODULARITY_PASS")
    print("BOUNDARY: proves twist central positivity, not ring-class Rankin central positivity.")

if __name__=="__main__":main()
