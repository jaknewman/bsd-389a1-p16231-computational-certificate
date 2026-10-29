#!/usr/bin/env python3
"""Exact rational proof that L'(389a1 quadratic twist by -7, 1) > 0.

No Sage, PARI, mpmath or floating-point computation is used for certificates.
The twist has conductor 389*7**2=19061 and root number -1 (coprime twist).

For w=-1 the completed Mellin integral yields
    L'(E^(-7),1) = 2 sum_{n>=1} a_n(E)*chi_{-7}(n)*E1(c*n)/n,
    c=2*pi/sqrt(19061), E1(t)=integral_t^infty exp(-u)/u du.

Archimedean rational interval: pi via Machin arctangent, sqrt via isqrt,
log via rapidly convergent atanh, Euler gamma from H_N-log(N)-1/(2*N),
E1(t)= -gamma - log(t) - sum_{k>=1} (-t)^k/(k*k!),
with alternating remainder. Tail: |a_n|<=2*n and E1(t)<=exp(-t)/t,
exp(-c)<=1/(1+c).

Run: python -u bsd389_twist_minus7_exact_rank1.py
"""
from fractions import Fraction as F
from math import isqrt, factorial

N=19061
D=-7
M=150
TAYLOR=60
LOG_TERMS=35
GAMMA_HARMONIC=256

def atan_bounds(d, count=16):
    x=F(1,d)
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1)) for k in range(count))
    r=x**(2*count+1)/F(2*count+1)
    return (s, s+r) if count%2==0 else (s-r,s)

def pi_bounds():
    a,b=atan_bounds(5)
    c,d=atan_bounds(239)
    return 16*a-4*d,16*b-4*c

def log_bounds(x, terms=LOG_TERMS):
    assert x>0
    y=x
    k=0
    while y<1:
        y*=2; k-=1
    while y>=2:
        y/=2; k+=1
    assert 1<=y<2
    def log_atanh(v):
        z=(v-1)/(v+1)
        part=sum(2*z**(2*j+1)/F(2*j+1) for j in range(terms))
        err=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return part,part+err
    lo,hi=log_atanh(y)
    l2,h2=log_atanh(F(2))
    if k>=0:
        return lo+k*l2,hi+k*h2
    return lo+k*h2,hi+k*l2

def gamma_bounds():
    h=sum(F(1,n) for n in range(1,GAMMA_HARMONIC+1))
    loglo,loghi=log_bounds(F(GAMMA_HARMONIC))
    lower=h-loghi-F(1,2*GAMMA_HARMONIC)
    upper=h-loglo-F(1,2*GAMMA_HARMONIC)+F(1,12*GAMMA_HARMONIC**2)
    return lower,upper

def chi_neg7(n):
    if n%7==0: return 0
    return 1 if n%7 in (1,2,4) else -1

def prime_list(n):
    sieve=[True]*(n+1);sieve[0]=sieve[1]=False
    for i in range(2,isqrt(n)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]]

def prime_a(p):
    if p==2:
        count=1+sum((y*y+y-x*x*x-x*x+2*x)%p==0 for x in range(p) for y in range(p))
        return p+1-count
    acc=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        z=pow(d,(p-1)//2,p)
        acc+=(0 if z==0 else (1 if z==1 else -1))
    return -acc

def elliptic_coefficients(m):
    primes=prime_list(m)
    ap={p:prime_a(p) for p in primes}
    assert [ap[p] for p in [2,3,5,7,11,13]] == [-2,-2,-3,-5,-4,-3]
    a=[0]*(m+1);a[1]=1
    for n in range(2,m+1):
        x=n;prod=1
        for p in primes:
            if p*p>x:break
            if x%p:continue
            e=0
            while x%p==0:x//=p;e+=1
            prev,cur=1,ap[p]
            for j in range(2,e+1):prev,cur=cur,ap[p]*cur-p*prev
            prod*=cur
        if x>1:prod*=ap[x]
        a[n]=prod
    return a

def e1_bounds(t,glo,ghi):
    assert t>0 and t<10 and TAYLOR>t
    lnlo,lnhi=log_bounds(t)
    term=F(1);s=F(0)
    for k in range(1,TAYLOR+1):
        term=term*(-t)/k
        s+=term/k
    # Eventually alternating; all k>=TAYLOR are in the decreasing regime.
    rem=t**(TAYLOR+1)/(F(TAYLOR+1)*factorial(TAYLOR+1))
    return -ghi-lnhi-s-rem,-glo-lnlo-s+rem

def dec_down(x, scale=10**11):
    # Exact integer arithmetic; rounds downward.
    z=x.numerator*scale//x.denominator
    return f"{z//scale}.{z%scale:011d}"

def dec_up(x, scale=10**11):
    # Exact integer arithmetic; rounds upward.
    z=(x.numerator*scale+x.denominator-1)//x.denominator
    return f"{z//scale}.{z%scale:011d}"

def main():
    assert N==389*49 and D==-7
    # 2 splits, 107 and 389 split for D=-7 (Kronecker from Euler criterion).
    assert D%8==1
    assert pow(D%107,53,107)==1
    assert pow(D%389,194,389)==1
    # The twisted root number is w(E)*chi_D(-389) = -1.
    assert chi_neg7(-389)==-1
    pl,ph=pi_bounds()
    rootfloor=isqrt(N*10**24)
    sl=F(rootfloor,10**12);sh=F(rootfloor+1,10**12)
    assert sl*sl<=N<sh*sh
    cl=2*pl/sh;ch=2*ph/sl
    assert cl<ch
    c0=F(455100201381,10**13) # 0.0455100201381
    assert c0>0
    delta=max(c0-cl,ch-c0)
    glo,ghi=gamma_bounds()
    a=elliptic_coefficients(M)
    total_lo=F(0);total_hi=F(0)
    totalabs=F(0)
    for n in range(1,M+1):
        chi=chi_neg7(n)
        if not chi:continue
        lo,hi=e1_bounds(n*c0,glo,ghi)
        coeff=F(2*a[n]*chi,n)
        if coeff>=0:total_lo+=coeff*lo;total_hi+=coeff*hi
        else:total_lo+=coeff*hi;total_hi+=coeff*lo
        totalabs+=abs(coeff)
    # |d E1(cn)/dc|=e^(-cn)/c <= 1/cl
    err_c=totalabs*delta/min(cl,c0)
    # q >= exp(-cl); |a_n|<=2n follows from Deligne + d(n)<=2sqrt(n).
    q=1/(1+cl)
    tail=4*q**(M+1)/(cl*(M+1)*(1-q))
    lower=total_lo-err_c-tail
    upper=total_hi+err_c+tail
    assert F(4)<lower<upper<F(5),('FAIL',str(float(lower)),str(float(upper)))
    print('BSD389_TWIST_MINUS7_CONDUCTOR',N,flush=True)
    print('BSD389_TWIST_MINUS7_ROOT_NUMBER_MINUS_ONE_PASS',flush=True)
    print('BSD389_TWIST_MINUS7_LOCAL_2_107_389_SPLIT_PASS',flush=True)
    print('BSD389_TWIST_MINUS7_COEFFICIENTS',M,flush=True)
    print('BSD389_TWIST_MINUS7_DERIVATIVE_LOWER',dec_down(lower),flush=True)
    print('BSD389_TWIST_MINUS7_DERIVATIVE_UPPER',dec_up(upper),flush=True)
    print('BSD389_TWIST_MINUS7_POSITIVE_EXACT_RATIONAL_CERTIFIED_PASS',flush=True)
    print('BSD389_TWIST_MINUS7_ANALYTIC_RANK_ONE_PASS',flush=True)
    print('BOUNDARY: Kim-2026 supersingular section 1.5.2 requires a ramified',
          'conductor prime when Nminus=1. 389 splits here, so this is NOT',
          'a direct certificate of Kim theorem applicability for p=107.',flush=True)

if __name__=='__main__':main()