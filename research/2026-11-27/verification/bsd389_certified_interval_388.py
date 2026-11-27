#!/usr/bin/env python3
"""Rigorous interval enclosure for 388 level-389 plus modular symbols.

Uses mpmath interval arithmetic with outward rounded endpoints, not Sage.
Certifies unique nearest integer for all 388 independently constructed
Fourier/AGM modular symbols, conditional on standard modularity/period formulas.
"""
from __future__ import annotations
import argparse, hashlib, math, time
from fractions import Fraction
from pathlib import Path
from mpmath import iv

P=389
SHA='9bce8b66c37b7f257f5a6015c08806c2b80c36d1e47356677e3819fc171e8360'

def point_count_coefficients(M):
    sieve=bytearray(b'\x01')*(M+1)
    sieve[:2]=b'\x00\x00'
    spf=list(range(M+1))
    for i in range(2,math.isqrt(M)+1):
        if sieve[i]:
            for k in range(i*i,M+1,i):
                sieve[k]=0
                if spf[k]==k: spf[k]=i
    primes=[i for i in range(2,M+1) if sieve[i]]
    aps={}
    for p in primes:
        if p==P: aps[p]=1;continue
        s=0
        for x in range(p):
            d=(1+4*(x*x*x+x*x-2*x))%p
            if d: s+=(1 if pow(d,(p-1)//2,p)==1 else -1)
        aps[p]=-s
    a=[0]*(M+1);a[1]=1
    for n in range(2,M+1):
        p=spf[n];m=n//p
        a[n]=aps[p]*a[m]-(p*a[m//p] if m%p==0 and p!=P else 0)
    assert a[1:12]==[1,-2,-2,2,-3,4,-5,0,1,6,-4]
    return a

def f(t:Fraction):return 4*t**3+4*t**2-8*t+1

def certified_roots():
    roots=[]
    for lo,hi in [(Fraction(-3),Fraction(-1)),(Fraction(0),Fraction(1,3)),(Fraction(1,2),Fraction(2))]:
        fl=f(lo)
        assert fl*f(hi)<0
        for _ in range(140):
            mid=(lo+hi)/2
            fm=f(mid)
            if fl*fm>0: lo=mid;fl=fm
            else:hi=mid
        assert f(lo)*f(hi)<=0 and hi-lo < Fraction(1,10**38)
        # Exact dyadic rationals, outward rounded conversion via interval division.
        low=iv.mpf(lo.numerator)/iv.mpf(lo.denominator)
        high=iv.mpf(hi.numerator)/iv.mpf(hi.denominator)
        roots.append(iv.mpf([low.a,high.b]))
    return roots

def interval_period(roots):
    e3,e2,e1=roots
    q=iv.sqrt((e1-e2)/(e1-e3))
    a,b=iv.mpf(1),q
    for _ in range(12):
        a,b=(a+b)/2,iv.sqrt(a*b)
    # True AGM is bounded by the lower bound of b, upper bound of a.
    assert b.a < a.b
    omega_low=iv.pi/(a*iv.sqrt(e1-e3))
    omega_high=iv.pi/(b*iv.sqrt(e1-e3))
    return iv.mpf([omega_low.a,omega_high.b])

def symbol_from_table(a,n,tab):
    pn,pd,ln,ld=1,0,0,1
    x,y=n,a
    ans=tab[P]
    while y:
        q,r=divmod(x,y)
        nn,nd=q*ln+pn,q*ld+pd
        det=ln*nd-nn*ld
        assert abs(det)==1
        c,d=(ld,nd) if det==1 else (nd,ld)
        c%=P;d%=P
        i=P if c==0 else d*pow(c,-1,P)%P
        ans+=det*tab[i]
        pn,pd,ln,ld=ln,ld,nn,nd
        x,y=y,r
    assert (ln,ld)==(a,n)
    return ans

def certify(M=2500,dps=65):
    t=time.monotonic()
    iv.dps=dps
    dat=Path(__file__).with_name('manin_390.txt').read_bytes()
    assert hashlib.sha256(dat).hexdigest()==SHA
    tab=list(map(int,dat.split()))
    assert len(tab)==390
    a=point_count_coefficients(M)
    roots=certified_roots()
    period=interval_period(roots)
    q=iv.exp(-2*iv.pi/P)
    qr=q
    buckets=[iv.mpf(0) for _ in range(P)]
    for n in range(1,M+1):
        if a[n]:buckets[n%P]+=iv.mpf(a[n])*qr/n
        qr*=q
    # Real Fourier values are sums of coefficients grouped modulo 389.
    # cos(k 2*pi/389) = cos((389-k)*2*pi/389).
    cosines=[iv.cos(2*iv.pi*k/P) for k in range((P+1)//2)]
    values=[iv.mpf(0)]*((P+1)//2)
    for u in range(1,(P+1)//2):
        acc=iv.mpf(0)
        for r in range(P):
            k=(u*r)%P
            if k>P//2:k=P-k
            acc+=buckets[r]*cosines[k]
        values[u]=acc
    # Uniform tail: |a_n|<=d(n)*sqrt(n)<=2n.
    # The Fourier cusp difference has two phases, giving 4 q^{M+1}/(1-q).
    tail=4*q**(M+1)/(1-q)
    worstUpper=0.
    strict_margin=iv.mpf("5e-16")
    examples={}
    for u in range(1,P):
        d=pow(u,-1,P)
        A=values[min(u,P-u)]
        B=values[min(d,P-d)]
        raw=(A-B)/period
        # unknown Fourier tail of difference is enclosed by +-tail/period
        err=tail/period
        full=raw+iv.mpf([-err.b,err.b])
        expected=symbol_from_table(u,P,tab)
        assert full>iv.mpf(expected)-iv.mpf('0.5') and full<iv.mpf(expected)+iv.mpf('0.5'),(u,expected,full)
        assert full>iv.mpf(expected)-strict_margin and full<iv.mpf(expected)+strict_margin,(u,expected,full)
        maxerr=max(abs(float(full.a)-expected),abs(float(full.b)-expected))
        worstUpper=max(worstUpper,maxerr)
        if u in (5,7,13,89,194,388):examples[u]=[expected,str(full)]
    print('CERTIFIED_FOURIER_AGM_INDEPENDENT_NERON_SYMBOLS_PASS 388/388')
    print('METHOD outward-rounded mpmath.iv arithmetic and rational root isolation')
    print('MANIN_SHA256',SHA)
    print('FOURIER_LENGTH',M,'IV_DPS',dps)
    print('PERIOD_INTERVAL',period)
    print('FOURIER_TAIL_BOUND_INTERVAL',tail)
    print('ALL_388_STRICT_CERTIFIED_ERROR_LT_5e-16', True)
    print('WORST_ABS_DISTANCE_FLOAT_DIAGNOSTIC_ONLY',worstUpper)
    print('EXAMPLES',examples)
    print('WALL_TIME_SEC',round(time.monotonic()-t,2))
    print('BOUNDARY: verifies Fourier/period normalization, not global BSD')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--M',type=int,default=2500);parser.add_argument('--dps',type=int,default=65)
    opts=parser.parse_args();certify(opts.M,opts.dps)
