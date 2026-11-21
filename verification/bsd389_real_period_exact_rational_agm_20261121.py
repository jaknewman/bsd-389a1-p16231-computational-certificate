#!/usr/bin/env python3
"""A rigorous rational enclosure of the BSD real period for E389a1.

No floating-point calls, Sage, elliptic L-values, Sha assumptions, or BSD
conjectural input. Roots of x^3+x^2-2x+1/4 are isolated by rational
bisection. pi by a rational alternating Machin arctan series. AGM
sqrt steps are outward-rounded by exact integer isqrt. The output
therefore is a proof-carrying enclosure of the geometric period.
"""
from fractions import Fraction as F
from math import isqrt

SCALE=10**88

class Iv:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=self.lo if hi is None else F(hi)
        assert self.lo <= self.hi
    def __add__(self,other):
        other=asiv(other)
        return Iv(self.lo+other.lo,self.hi+other.hi)
    def __sub__(self,other):
        other=asiv(other)
        return Iv(self.lo-other.hi,self.hi-other.lo)
    def __mul__(self,other):
        other=asiv(other)
        p=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Iv(min(p),max(p))
    def __truediv__(self,other):
        other=asiv(other)
        assert other.lo*other.hi>0
        return self * Iv(1/other.hi,1/other.lo)
    def sqrt(self):
        assert self.lo>=0
        def down(x):
            n=x.numerator*SCALE*SCALE//x.denominator
            k=isqrt(n)
            assert F(k*k,SCALE*SCALE)<=x<F((k+1)*(k+1),SCALE*SCALE)
            return F(k,SCALE),F(k+1,SCALE)
        l,_=down(self.lo)
        _,h=down(self.hi)
        return Iv(l,h)
    def width(self):return self.hi-self.lo

def asiv(x):return x if isinstance(x,Iv) else Iv(x)

def cubic(x):return x*x*x+x*x-2*x+F(1,4)

def root_interval(a,b,rounds=340):
    a,b=F(a),F(b)
    sa=cubic(a)
    assert sa*cubic(b)<0
    for _ in range(rounds):
        mid=(a+b)/2
        sm=cubic(mid)
        if sm==0:return Iv(mid)
        if sm*sa>0:a=mid;sa=sm
        else:b=mid
    assert cubic(a)*cubic(b)<0
    return Iv(a,b)

def atan_bound(k,N):
    # An even-numbered alternating partial sum is a rigorous lower bound.
    assert N%2==0 and k>1
    val=sum((F(1, (2*j+1)*k**(2*j+1)) if j%2==0 else
             -F(1,(2*j+1)*k**(2*j+1))) for j in range(N))
    next_term=F(1,(2*N+1)*k**(2*N+1))
    return Iv(val,val+next_term)

def decimal_bounds(v,digits=55):
    scale=10**digits
    l=v.lo.numerator*scale//v.lo.denominator
    h=-(-v.hi.numerator*scale//v.hi.denominator)
    def fmt(n):
        s=str(abs(n)).zfill(digits+1)
        return ('-' if n<0 else '')+s[:-digits]+'.'+s[-digits:]
    return fmt(l),fmt(h)

def main():
    e3=root_interval(-3,-1)
    e2=root_interval(0,F(1,2))
    e1=root_interval(F(1,2),2)
    assert e3.hi<e2.lo<e2.hi<e1.lo
    # Cubic is y_adj^2=(x-e1)(x-e2)(x-e3).
    Delta=e1-e3
    k2=(e2-e3)/Delta
    complementary=(e1-e2)/Delta
    assert 0<k2.lo and k2.hi<1
    assert 0<complementary.lo and complementary.hi<1
    assert (k2+complementary).lo<=1<=(k2+complementary).hi
    # AGM(1, sqrt(1-k^2)) and K(k)=pi/(2AGM).
    b=complementary.sqrt()
    a=Iv(1)
    for _ in range(12):
        a,b=(a+b)/2, (a*b).sqrt()
    assert b.lo<a.hi
    agm=Iv(b.lo,a.hi)
    pi=atan_bound(5,80)*16-atan_bound(239,30)*4
    # With two real components, period = 4*K(k)/sqrt(e1-e3)
    # = 2*pi/(sqrt(Delta)*AGM).
    period=pi*2/(Delta.sqrt()*agm)
    lower,upper=decimal_bounds(period,55)
    assert period.width()<F(1,10**65)
    print('BSD389_RATIONAL_CUBIC_ROOT_ISOLATION_PASS',340,'steps_per_root')
    print('BSD389_RATIONAL_MACHIN_PI_ENCLOSURE_PASS',80,30)
    print('BSD389_RATIONAL_AGM_ENCLOSURE_PASS',12,'iterations')
    print('BSD389_REAL_PERIOD_LOWER_55_DIGITS',lower)
    print('BSD389_REAL_PERIOD_UPPER_55_DIGITS',upper)
    assert F(lower)<=period.lo<=period.hi<=F(upper)
    # Analytic bound taken as a conservative widening of the previous
    # authentic user's certified Sage Arb interval for L''(E,1)/2.
    L=Iv(F('0.7593165002884267'),F('0.7593165002884269'))
    ratio=L/period  # THIS IS THE REGULATOR REQUIRED IF #Sha=1.
    rlo,rhi=decimal_bounds(ratio,30)
    print('BSD389_FORCED_REGULATOR_IF_SHA1_LOWER_30_DIGITS',rlo)
    print('BSD389_FORCED_REGULATOR_IF_SHA1_UPPER_30_DIGITS',rhi)
    assert ratio.lo<F('0.15246017794314375162432475704945582')<ratio.hi
    print('BSD389_ARCHIMEDEAN_PERIOD_CERTIFIED_PASS')
    print('BOUNDARY: the forced regulator enclosure uses prior Arb Lstar bound; '
          'the independent canonical height determinant is not enclosed here, '
          'and numeric proximity cannot prove complex BSD or Sha finiteness.')

if __name__=='__main__':main()
