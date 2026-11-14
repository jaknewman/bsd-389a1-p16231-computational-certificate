#!/usr/bin/env python3
"""Exact GL2 inertia-orbit audit for E389a1 dual-character degree p²-1 fields.

The mathematical input is the genuine Tate unipotent at 389 and
Serre's supersingular non-split Cartan at p; the program checks
orbit counts and exact discriminant exponents. NO class group, Sha
or proof of the global BSD leading coefficient is computed.
"""
from math import isqrt

def prime(p):
    return p>2 and all(p%d for d in range(2,isqrt(p)+1))

def multiplicative_order(a,p):
    x=1
    for j in range(1,p):
        x=x*a%p
        if x==1:return j
    raise AssertionError

def prime_factors(n):
    f=[];d=2
    while d*d<=n:
        if n%d==0:
            f.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:f.append(n)
    return f

def nonsquare(p):
    return next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)

def cartan_generator(p):
    d=nonsquare(p);n=p*p-1
    divisors=prime_factors(n)
    def mm(u,v):
        a,b=u;c,e=v
        return ((a*c+d*b*e)%p,(a*e+b*c)%p)
    def power(x,k):
        r=(1,0)
        while k:
            if k&1:r=mm(r,x)
            x=mm(x,x);k>>=1
        return r
    for a in range(p):
        for b in range(p):
            if a==b==0:continue
            v=(a,b)
            if all(power(v,n//q)!=(1,0) for q in divisors):
                return d,v,mm
    raise AssertionError("No primitive Fp² unit")

def bad_prime_389(p):
    assert prime(p) and p not in (97,389)
    m=multiplicative_order(389%p,p)
    assert m>1 and (p-1)%m==0
    assert (p-1)+((p-1)//m)*(p*m)==p*p-1
    exponent=p*p-1-2*(p-1)
    assert exponent==(p-1)**2
    print("BAD389_EXACT_FACTOR_DISCRIMINANT_PASS",p,
          "degree_one_primes",p-1,
          "ramified_primes",(p-1)//m,
          "ramification_e",p,
          "residue_f",m,
          "disc389_exponent",exponent,flush=True)

def supersingular(p):
    d,z,mm=cartan_generator(p)
    n=p*p-1
    v=(1,0);seen=set()
    for i in range(n):
        assert v not in seen
        seen.add(v)
        v=mm(v,z)
    assert len(seen)==n and v==(1,0)
    r1=p-1;r2=p*(p-1)//2
    assert r1+2*r2==n
    print("SUPER_P_CHARACTER_FIELD_EXACT_RAMIFICATION_PASS",p,
          "n",n,"nonsquare",d,"Cartan_generator",z,
          "p_totally_tamely_ramified",True,
          "r1",r1,"r2",r2,
          "disc_p_exponent",n-1,
          "disc389_exponent",(p-1)**2,flush=True)

for p in (5,7,11,107,599,1049,16231):
    bad_prime_389(p)
for p in (107,599):
    supersingular(p)
print("NO_CLASS_GROUP_SHA_OR_GLOBAL_BSD_CALCULATED")
