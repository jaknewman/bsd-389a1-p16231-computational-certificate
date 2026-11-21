#!/usr/bin/env python3
"""E389a1: rigorous fast Neron--Tate regulator from Tate's archimedean series.

Uses ONLY integers/Fractions and outward rounding on a fixed 10^100 grid.
No floating point, Sage, heuristic error bound, Sha or BSD hypothesis.

Translated minimal equation: y^2+y=X^3-8X^2+19X-12, X=x+3>0
for EVERY real point on E. Its Tate z is 1-38 t^2+94 t^3-15 t^4.
All three integral input points have nonsingular reduction at 389,
the only bad prime (type I_1). In Cremona's canonical height
normalization their finite local height contributions vanish.
Thus twice the usual canonical height is
 H(R)=log(X(R))+sum_{j>=0}4^(-j-1)*log(z(2^jR)).
Global 1/50<z<64 yields a tail bound log(64)/(3*4^N).
"""
from fractions import Fraction as F
S=10**100
LOG_TERMS=95

class Iv:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None,raw=False):
        if raw:
            self.lo,self.hi=lo,lo if hi is None else hi
        else:
            a,b=F(lo), F(lo if hi is None else hi)
            self.lo=(a.numerator*S)//a.denominator
            self.hi=-((-b.numerator*S)//b.denominator)
        assert self.lo<=self.hi
    def __add__(self,other):
        y=toiv(other);return Iv(self.lo+y.lo,self.hi+y.hi,raw=True)
    __radd__=__add__
    def __neg__(self):return Iv(-self.hi,-self.lo,raw=True)
    def __sub__(self,other):return self + (-toiv(other))
    def __rsub__(self,other):return toiv(other)-self
    def __mul__(self,other):
        y=toiv(other)
        p=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        low=min(p)//S;high=-(-max(p)//S)
        return Iv(low,high,raw=True)
    __rmul__=__mul__
    def __truediv__(self,other):
        y=toiv(other)
        assert 0<y.lo<=y.hi,('nonpositive denominator',y)
        inv=Iv((S*S)//y.hi,-(-(S*S)//y.lo),raw=True)
        return self*inv
    def __repr__(self):
        return f'Iv([{F(self.lo,S)}, {F(self.hi,S)}])'
    def absupper(self):return max(abs(self.lo),abs(self.hi))

def toiv(x):return x if isinstance(x,Iv) else Iv(x)

def atan_log_two():
    u=Iv(F(1,3))
    return twice_atanh(u)

def twice_atanh(u):
    assert 0<=u.lo<=u.hi<S//2
    t2=u*u
    acc=Iv(0);term=u
    for i in range(LOG_TERMS):
        acc += (2*term)/(2*i+1)
        term=term*t2
    tail=(2*term)/(2*LOG_TERMS+1)/(1-t2)
    return Iv(acc.lo,acc.hi+tail.hi,raw=True)

LOG2=atan_log_two()

def pow2(k):return F(2**k) if k>=0 else F(1,2**(-k))

def logiv(v):
    v=toiv(v)
    assert v.lo>0
    val=F(v.lo,S)
    k=val.numerator.bit_length()-val.denominator.bit_length()
    while val<pow2(k):k-=1
    while val>=pow2(k+1):k+=1
    m=v/Iv(pow2(k))
    assert m.lo>=S and m.hi<3*S
    u=(m-1)/(m+1)
    r=twice_atanh(u)
    return r+k*LOG2

def curve_f(x):return x*x*x+x*x-2*x+F(1,4)

def certify_global_z_bound():
    # Real x lies in [e3,e2] U [e1,infinity), where e_i are
    # the three real roots of curve_f. Establish safe rational
    # enclosures by exact endpoint signs and derivative analysis.
    assert curve_f(F(-41,20))<0<curve_f(F(-2))
    assert curve_f(F(13,100))>0>curve_f(F(7,50))
    assert curve_f(F(9,10))<0<curve_f(F(91,100))
    # Thus t=1/(x+3) lies in (0,10/39) U (50/157,20/19).
    z=lambda t:1-38*t*t+94*t**3-15*t**4
    v=lambda t:38-141*t+30*t*t
    assert v(F(10,39))>0
    assert v(F(50,157))<0
    assert 30*F(20,19)<141  # v decreases for t<141/60.
    # z'=-2t*v(t): decreasing on first interval; increasing on second.
    assert z(F(10,39))>F(1,50)
    assert z(F(50,157))>F(1,50)
    assert z(F(20,19))<64
    print('BSD389_GLOBAL_TATE_Z_MONOTONICITY_PASS',
          'unbounded_t_max','10/39','bounded_t_range','50/157,20/19',
          'z_range','(1/50,64)',flush=True)

def double_X(x):
    xx=x*x
    num=xx*xx-38*xx+94*x-15
    den=4*xx*x-32*xx+76*x-47
    assert den.lo>0,('Tate doubled denominator must be positive',x,den)
    nxt=num/den
    assert nxt.lo>S*F(19,20),('valid real x+3 bound',nxt)
    return nxt

def tate_z(X):
    t=Iv(1)/X;t2=t*t
    z=1-38*t2+94*t2*t-15*t2*t2
    assert F(1,50)*S<z.lo<=z.hi<64*S,('z outside global bound',z)
    return z

def height(original_x,N=35):
    X=Iv(original_x+3)
    total=logiv(X)
    for j in range(N):
        z=tate_z(X)
        total += logiv(z)/(4**(j+1))
        if j+1<N:X=double_X(X)
    # Upper bound on log(64)/(3*4^N), outward-rounded.
    error=-(-(6*LOG2.hi)//(3*4**N))
    H=Iv(total.lo-error,total.hi+error,raw=True)
    print('BSD389_TATE_LOCAL_HEIGHT_ENCLOSURE_PASS',
          'x',original_x,'terms',N,'absolute_tail_bound',
          rounded(Iv(error,raw=True),25)[1],
          'height_interval',rounded(H,24),flush=True)
    return H

def square(v):
    assert v.lo>=0
    return v*v

def rounded(v,digits):
    # Endpoints outward-rounded to multiples of 10^-digits.
    sc=10**digits
    lo=(v.lo*sc)//S
    hi=-(-v.hi*sc//S)
    def form(n):
        sig='-' if n<0 else ''
        s=str(abs(n)).zfill(digits+1)
        return sig+s[:-digits]+'.'+s[-digits:]
    return form(lo),form(hi)

def regulator(N=35):
    certify_global_z_bound()
    # Check each y coordinate mod 389 nonsingular: 2*y+1 !=0.
    assert all((2*y+1)%389 for y in (1,-1,8))
    P=height(-1,N)
    Q=height(0,N)
    PQ=height(4,N)
    cross=(PQ-P-Q)/2
    assert cross.lo>0
    R=P*Q-square(cross)
    assert R.lo>0
    print('BSD389_TATE_RANK2_REGULATOR_LOWER_20',rounded(R,20)[0])
    print('BSD389_TATE_RANK2_REGULATOR_UPPER_20',rounded(R,20)[1])
    print('BSD389_TATE_RANK2_REGULATOR_CERTIFICATE_PASS')
    return R

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--terms',type=int,default=35)
    args=ap.parse_args()
    assert 20<=args.terms<=35
    regulator(args.terms)
