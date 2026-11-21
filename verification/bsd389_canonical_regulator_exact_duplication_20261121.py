#!/usr/bin/env python3
"""Fully rational interval certificate for Neron--Tate regulator of E389a1.

Uses the doubled Neron--Tate height pairing <P,P>=lim h(x(2^nP))/4^n.
Height limits use the exact x-coordinate duplication map; an explicit
Bezout identity with resultant 389 bounds the height error uniformly.
Rational logarithm intervals are computed via an atanh series after
binary range reduction. Zero floating point, no BSD or Sha assumptions.
"""
from fractions import Fraction as F
from math import gcd
from time import monotonic
import argparse

class Iv:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=self.lo if hi is None else F(hi)
        assert self.lo<=self.hi
    def __add__(self,v):
        v=iv(v)
        return Iv(self.lo+v.lo,self.hi+v.hi)
    def __sub__(self,v):
        v=iv(v)
        return Iv(self.lo-v.hi,self.hi-v.lo)
    def __mul__(self,v):
        v=iv(v)
        w=[u*z for u in (self.lo,self.hi) for z in (v.lo,v.hi)]
        return Iv(min(w),max(w))
    def __truediv__(self,v):
        v=iv(v)
        assert v.lo*v.hi>0
        return self*Iv(1/v.hi,1/v.lo)
    def square(self):
        if self.lo<=0<=self.hi:return Iv(0,max(self.lo**2,self.hi**2))
        return Iv(min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))

def iv(x):return x if isinstance(x,Iv) else Iv(x)

A=lambda x,z:x**4+4*x*x*z*z-2*x*z**3+3*z**4
B=lambda x,z:4*x**3*z+4*x*x*z*z-8*x*z**3+z**4

def verify_bezout():
    # The reversed Bezout and ordinary identities are polynomials, not
    # just pointwise numerical checks. They are certified by exact rational
    # polynomial arithmetic at startup via all 8 coefficients.
    def mul(U,V):
        z=[0]*(len(U)+len(V)-1)
        for i,a in enumerate(U):
            for j,b in enumerate(V):z[i+j]+=a*b
        return z
    # polynomials in X, setting Z=1
    a=[3,-2,4,0,1]; b=[1,-8,4,4,0]
    uz=[144,-32,-48];vz=[-43,40,-4,12]
    urev=[389,188,-520,66]; vrev=[-47,-212,108,-198]
    # Z^7 identity is 389 (constant polynomial).
    yz=mul(uz,a);bz=mul(vz,b)
    yz += [0]*(max(len(yz),len(bz))-len(yz))
    bz += [0]*(max(len(yz),len(bz))-len(bz))
    assert [x+y for x,y in zip(yz,bz)]==[389]+[0]*7
    # X^7 identity, coefficient arrays in Z at X=1
    arev=list(reversed(a));brev=list(reversed(b))
    yy=mul(urev,arev);by=mul(vrev,brev)
    yy += [0]*(max(len(yy),len(by))-len(yy))
    by += [0]*(max(len(yy),len(by))-len(by))
    assert [x+y for x,y in zip(yy,by)]==[389]+[0]*7
    assert sum(map(abs,uz+vz))==323
    assert sum(map(abs,urev+vrev))==1728
    return 1728

def dupl(x,z):
    xx,zz=A(x,z),B(x,z)
    gg=gcd(xx,zz)
    assert gg>0 and 389%gg==0,(gg,)
    xx//=gg;zz//=gg
    assert zz!=0
    if zz<0:xx,zz=-xx,-zz
    assert gcd(xx,zz)==1
    return xx,zz

def log_atanh_x(x,terms=83):
    assert 1<=x<=F(2)
    t=(x-1)/(x+1)
    assert 0<=t<=F(1,3)
    accum=F(0)
    power=t
    for j in range(terms):
        accum+=2*power/F(2*j+1)
        power*=t*t
    upper=accum+2*power/(F(2*terms+1)*(1-t*t))
    return Iv(accum,upper)

def log_integer(n,bits=125):
    assert n>=1
    k=n.bit_length()-1
    if k>=bits:
        q=n>>(k-bits)
        xl=F(q,2**bits);xh=F(q+1,2**bits)
    else:
        xl=F(n,2**k);xh=xl
    ln2=log_atanh_x(F(2))
    return ln2*k+Iv(log_atanh_x(xl).lo,log_atanh_x(xh).hi)

def out(v,digits=12):
    scale=10**digits
    lo=v.lo.numerator*scale//v.lo.denominator
    hi=-(-v.hi.numerator*scale//v.hi.denominator)
    def fmt(z):
        s=str(abs(z)).zfill(digits+1)
        return ('-' if z<0 else '')+s[:-digits]+'.'+s[-digits:]
    return fmt(lo),fmt(hi)

def point_height(x,n,C):
    xx,zz=x,1
    for j in range(n):xx,zz=dupl(xx,zz)
    M=max(abs(xx),abs(zz))
    h=log_integer(M)/(4**n)
    error=log_integer(C).hi/(3*4**n)
    interval=h+Iv(-error,error)
    print('BSD389_HEIGHT_DUPLICATION_PASS','x',x,'n',n,
          'max_coordinate_bits',M.bit_length(),
          'enclosure_12_digits',out(interval,12),flush=True)
    return interval

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--doublings',type=int,default=10)
    args=ap.parse_args();n=args.doublings
    assert 2<=n<=11
    C=verify_bezout()
    print('BSD389_DUPLICATION_BEZOUT_IDENTITIES_EXACT_PASS',
          'resultant',389,'height_constant',C,flush=True)
    t=monotonic()
    # P=(-1,1), Q=(0,-1), P+Q=(4,8).
    assert 8*8+8==4**3+4**2-2*4
    hp=point_height(-1,n,C)
    hq=point_height(0,n,C)
    hpq=point_height(4,n,C)
    pairing=(hpq-hp-hq)/2
    reg=hp*hq-pairing.square()
    assert reg.lo>0
    print('BSD389_RATIONAL_NERON_TATE_REG_LOWER_12_DIGITS',out(reg,12)[0])
    print('BSD389_RATIONAL_NERON_TATE_REG_UPPER_12_DIGITS',out(reg,12)[1])
    assert reg.lo<F('0.15246017794314375162432475704945582')<reg.hi
    print('BSD389_CANONICAL_REGULATOR_RATIONAL_INTERVAL_PASS',
          'seconds',round(monotonic()-t,3))
    print('BOUNDARY: 4^-n height-limit enclosure is rigorous but not exact BSD; '
          'rank and saturation basis taken from previous user-certified arithmetic.')

if __name__=='__main__':main()
