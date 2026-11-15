#!/usr/bin/env python3
"""389a1: proof-level, pure-integer/rational interval for L''(E,1)/2.

No Sage, floating-point, mpmath, NumPy or mathematical black-box numerics.
Uses exact Legendre point counts, Hecke recurrences, Machin's pi identity,
integer sqrt bounds, alternating Taylor exp/log inequalities, signed
rectangular interval quadrature, and explicit infinite tail bounds.

Assumptions from established modularity / rank-zero theorem:
 E is modular of conductor 389, functional sign +1, and rank >=2.
These imply L(E,1)=L'(E,1)=0 exactly.
Our interval gives strict L''(E,1)/2 > 0, proving analytic rank 2.
Does not prove strong BSD's exact leading-term identity or Sha finiteness.
"""
from fractions import Fraction as F
from math import factorial, isqrt

N, B, T, H = 389, 100, 60, 1000
M = 10**25

# Long Weierstrass invariants for [a1,a2,a3,a4,a6]=[0,1,1,-2,0].
# The global minimal discriminant is +389 (NOT -389).
b2,b4,b6,b8 = 4,-4,1,-3
Delta = -b2*b2*b8 - 8*b4**3 -27*b6*b6 + 9*b2*b4*b6
assert Delta == 389
# At 389 the model has multiplicative reduction (v_389(Delta)=1).
# Direct point enumeration of its singular reduction gives a_389=+1,
# i.e. split multiplicative reduction; hence global root number is +1.
qbad=389
sumchi=0
for x in range(qbad):
    d=(4*x*x*x+4*x*x-8*x+1)%qbad
    if d:
        cc=pow(d,(qbad-1)//2,qbad)
        assert cc in (1,qbad-1)
        sumchi += (1 if cc==1 else -1)
assert -sumchi == +1


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -(-x.numerator // x.denominator)


def cdiv(a,b):
    return -((-a)//b)


def isprime(n):
    return n >= 2 and all(n % k for k in range(2,isqrt(n)+1))


def a_prime(p):
    assert isprime(p) and p != N
    if p == 2:
        # Same discriminant test works using the 0/1 characteristic-2 point count,
        # but explicitly enumerate y to avoid treating 2 as an odd prime.
        count = 1
        for x in range(2):
            for y in range(2):
                if (y*y+y-(x*x*x+x*x-2*x)) % 2 == 0:
                    count += 1
        return p+1-count
    total=0
    for x in range(p):
        delta=(4*x*x*x+4*x*x-8*x+1)%p
        if delta:
            chi=pow(delta,(p-1)//2,p)
            assert chi in (1,p-1)
            total += 1 if chi==1 else -1
    return -total


def hecke_coeffs():
    ap={p:a_prime(p) for p in range(2,B+1) if isprime(p)}
    out=[0]*(B+1)
    out[1]=1
    for n in range(2,B+1):
        rem=n; prod=1
        for p in ap:
            if p*p>rem:
                break
            if rem % p != 0:
                continue
            pp=1
            b0,b1=1,ap[p]
            while rem%p==0:
                rem//=p
                pp+=1
                if pp>=3:
                    b0,b1=b1,ap[p]*b1-p*b0
            # pp = k+1. b1 equals a_{p^k}
            prod*=b1
        if rem>1:
            prod*=ap[rem]
        out[n]=prod
    assert out[1:9]==[1,-2,-2,2,-3,4,-5,0]
    return out


def atan_partial_inverse(q,terms):
    return sum(((-1)**k * F(1,(2*k+1)*q**(2*k+1)) for k in range(terms)),F(0))

# Machin: pi = 16 atan(1/5) - 4 atan(1/239), with alternating rational bounds
pi_lo=16*atan_partial_inverse(5,18)-4*atan_partial_inverse(239,19)
pi_hi=16*atan_partial_inverse(5,19)-4*atan_partial_inverse(239,18)
assert F(314159,100000)<pi_lo<pi_hi<F(314160,100000)
R=10**16
root_floor=isqrt(N*R*R)
sqrt_lo=F(root_floor,R)
sqrt_hi=F(root_floor+1,R)
assert sqrt_lo**2<=N<=sqrt_hi**2
c_lo=2*pi_lo/sqrt_hi
c_hi=2*pi_hi/sqrt_lo
assert F(3,10)<c_lo<c_hi<F(1,3)


def exp_neg_bounds(xlo,xhi):
    # For x>=0, sum_0^odd (-x)^k/k! < e^{-x} < sum_0^even (-x)^k/k!
    assert 0<=xlo<=xhi<F(1,2)
    def partial(x,terms):
        v=F(1); term=F(1)
        for k in range(1,terms+1):
            term *= -x/k
            v += term
        return v
    return partial(xhi,25),partial(xlo,26)

initial_lo,initial_hi=exp_neg_bounds(c_lo,c_hi)
step_lo,step_hi=exp_neg_bounds(c_lo/H,c_hi/H)
y_lo=floor(M*initial_lo)
y_hi=ceil(M*initial_hi)
step_l=floor(M*step_lo)
step_u=ceil(M*step_hi)
assert 0 < y_lo <= y_hi < M and 0 < step_l <= step_u < M

A=hecke_coeffs()
positive=[0]+[max(A[n],0) for n in range(1,B+1)]
negative=[0]+[max(-A[n],0) for n in range(1,B+1)]


def poly_fixed(y,arr,upper):
    """Directed rounding for Σ arr[n]*(y/M)^n, stored as M times value."""
    s=0
    if upper:
        for n in range(B,0,-1):
            s=cdiv(s*y,M)+arr[n]*M
        return cdiv(s*y,M)
    for n in range(B,0,-1):
        s=(s*y)//M+arr[n]*M
    return (s*y)//M


def log_increment(d):
    """lower S6 / upper S5 for log(1+1/d), directed to M grid."""
    assert d>=H
    low=high=0
    dpow=1
    for k in range(1,7):
        dpow*=d
        den=k*dpow
        fl=M//den
        ce=cdiv(M,den)
        if k%2:
            low+=fl
            high+=ce
        else:
            low-=ce
            if k<=4:
                high-=fl
    return low,high

lsum=usum=0
loglo=loghi=0
for j in range((T-1)*H):
    dl,du=log_increment(H+j)
    next_loglo=loglo+dl
    next_loghi=loghi+du
    next_ylo=(y_lo*step_l)//M
    next_yhi=cdiv(y_hi*step_u,M)
    assert 0<next_ylo<=next_yhi and 0<=loglo<=loghi<=next_loghi

    p_low=poly_fixed(next_ylo,positive,False)
    n_low=poly_fixed(next_ylo,negative,False)
    p_high=poly_fixed(y_hi,positive,True)
    n_high=poly_fixed(y_hi,negative,True)
    assert p_low>=0 and n_low>=0 and p_high>=0 and n_high>=0
    # On [t_j,t_j+h], log(t)^2 rises and e^(-c*n*t) falls.
    # Positive coefficients contribute min at (t_{j+1},t_j), max
    # at (t_j,t_{j+1}); negative coefficients reverse inequalities.
    ell=p_low*loglo**2-n_high*next_loghi**2
    uu=p_high*next_loghi**2-n_low*loglo**2
    scale=M*M
    lsum+=ell//scale
    usum+=cdiv(uu,scale)
    loglo,loghi=next_loglo,next_loghi
    y_lo,y_hi=next_ylo,next_yhi

I_core_lo=F(lsum,H*M)
I_core_hi=F(usum,H*M)

# For all n: |a_n|<=d(n)*sqrt(n)<=2n (Deligne + elementary divisor bound).
# For t>=1, (log t)^2<=(t-1)^2, hence
#  |sum_{n>B} a_n int_1^∞ e^(-c*n*t) log^2 t dt|
# <=4/c^3 * sum_{n>B} e^(-c*n)/n^2
# <=(4/(3/10)^3) * (3/4)^(B+1) / ((B+1)^2*(1-3/4)).
# Because c>3/10 and e^(-c)<3/4 (Taylor: exp(3/10)>4/3).
r=F(3,4)
c0=F(3,10)
assert 1+c0+c0*c0/2+c0**3/6 > F(4,3)
tail_n=4/c0**3 * r**(B+1)/((B+1)**2*(1-r))

# For t>=T, |sum_{n>=1} a_n e^(-c*n*t)| <=2*z/(1-z)^2,
# z=e^(-c*t) <=(3/4)^T. Bound log^2 t <=t^2 and integrate.
tail_t=2*r**T/(1-r**T)**2*(F(T*T)/c0+2*F(T)/c0**2+2/c0**3)

I_lo=I_core_lo-tail_n-tail_t
I_hi=I_core_hi+tail_n+tail_t
assert I_lo > 0
halfL_lo=c_lo*I_lo
halfL_hi=c_hi*I_hi
assert halfL_lo < halfL_hi

def decimals(x,places=12,direction='floor'):
    v=10**places
    a=floor(x*v) if direction=='floor' else ceil(x*v)
    return ('-' if a<0 else '') + str(abs(a)//v) + '.' + str(abs(a)%v).zfill(places)

print('BSD389_ANALYTIC_RANK2_CERTIFICATE_BEGIN')
print('MINIMAL_DISCRIMINANT_PLUS_389_AND_ROOT_NUMBER_PLUS_ONE_PASS')
print('MODULAR_CURVE',N,'HECKE_COEFFICIENTS',B,'GRID_T',T,'GRID_H',H,'FIXED_POINT_SCALE_DIGITS',len(str(M))-1)
print('FIRST_20_A_N',A[1:21])
print('PI_MACHIN_BOUNDS_DECIMAL',decimals(pi_lo,12),decimals(pi_hi,12))
print('ALPHA_BOUNDS_DECIMAL',decimals(c_lo,12),decimals(c_hi,12))
print('RATIONAL_SIGNED_RECTANGLE_I_BOUNDS',decimals(I_core_lo,12),decimals(I_core_hi,12))
print('N_TAIL_UPPER',float(tail_n),'T_TAIL_UPPER',float(tail_t))
print('CERTIFIED_L_DOUBLE_PRIME_OVER_TWO_OUTWARD_INTERVAL',decimals(halfL_lo,10),decimals(halfL_hi,10,'ceil'))
assert F(75,100)<halfL_lo<halfL_hi<F(77,100)
print('BSD389_L_DOUBLE_PRIME_POSITIVE_CERTIFIED_PASS')
print('BSD389_ANALYTIC_RANK_EXACT_TWO_CONDITIONAL_ONLY_ON_ESTABLISHED_MODULARITY_ROOT_SIGN_AND_RANK_ZERO_THEOREM')
print('NO_EXACT_STRONG_BSD_LEADING_TERM_OR_GLOBAL_SHA_CLAIM')