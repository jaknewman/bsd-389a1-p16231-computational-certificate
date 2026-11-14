#!/usr/bin/env python3
"""E389a1: exact rational p-local Kummer witnesses for unramified class fields.

Under full modp GL2, good non-anomalous p>=5, p!=97,389, mathematical
Kummer/Sah/Nakayama theory implies p^(2n) divides h(Q(E[p^n])) for all n.
The script ONLY checks actual arithmetic local points, not class groups.
"""
from fractions import Fraction as F
from math import isqrt, gcd

P=(F(-1),F(1)); Q=(F(0),F(-1))
def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def neg(U):return None if U is None else (U[0],-U[1]-1)
def add(U,V):
    if U is None:return V
    if V is None:return U
    x,y=U;u,v=V
    if x==u and y+v+1==0:return None
    slope=(v-y)/(u-x) if x!=u else (3*x*x+2*x-2)/(2*y+1)
    nu=y-slope*x
    X=slope*slope-1-x-u
    Y=-slope*X-nu-1
    assert Y*Y+Y==X**3+X*X-2*X
    return X,Y
def mul(U,k):
    if k<0:return mul(neg(U),-k)
    R=None
    while k:
        if k&1:R=add(R,U)
        U=add(U,U);k//=2
    return R
def count(q):
    assert prime(q) and q>=5 and q!=389
    N=1
    for x in range(q):
        d=(4*x*x*x+4*x*x-8*x+1)%q
        if d==0:N+=1
        elif pow(d,(q-1)//2,q)==1:N+=2
    return N
def formal_t_nR(R,n,p,k):
    S=mul(R,n)
    if S is None:return 0
    x,y=S;t=-x/y
    assert gcd(t.denominator,p)==1 and t.numerator%p==0
    return t.numerator*pow(t.denominator,-1,p**k)%(p**k)

# Each (a,b) primitive mod p and p-adically divisible at level 1;
# n2 coefficients, if given, similarly primitive and p²-locally divisible.
WITNESSES=[
    (5,(-2,1),(-4,-3)),
    (7,(-2,1),(-4,-5)),
    (11,(-3,1),None),
    (13,(-1,2),None),
    (17,(-1,1),None),
    (19,(-1,2),None),
    (23,(-3,-1),None),
]
for p,(a,b),level2 in WITNESSES:
    n=count(p)
    assert n%p!=0 and p not in (97,389)
    x=(formal_t_nR(P,n,p,2)//p)*pow(n,-1,p)%p
    y=(formal_t_nR(Q,n,p,2)//p)*pow(n,-1,p)%p
    assert (a*x+b*y)%p==0 and (a%p,b%p)!=(0,0)
    R=add(mul(P,a),mul(Q,b))
    assert R is not None and formal_t_nR(R,n,p,2)==0
    print("BSD389_UNRAMIFIED_KUMMER_LEVEL1_EXACT_LOCAL_PASS",
          "p",p,"N",n,"logP/p",x,"logQ/p",y,
          "primitive_R",f"{a}P+{b}Q","R",R,flush=True)
    if level2 is not None:
        a2,b2=level2
        assert (a2%p,b2%p)!=(0,0)
        R2=add(mul(P,a2),mul(Q,b2))
        assert R2 is not None and formal_t_nR(R2,n,p,3)==0
        xp=formal_t_nR(P,n,p,3)//p
        yp=formal_t_nR(Q,n,p,3)//p
        # Since a1=0, log(t) differs from t only at order t^3,
        # so t([n]R)/p agrees with the linearized form mod p².
        assert (a2*xp+b2*yp)%(p*p)==0
        print("BSD389_UNRAMIFIED_KUMMER_LEVEL2_EXACT_LOCAL_PASS",
              "p",p,"N",n,"primitive_R",f"{a2}P+{b2}Q",
              "R",R2,"t([N]R) mod p³",0,flush=True)
from fractions import Fraction
for ell in (5,7,11,107,16231):
    d=Fraction(ell**2,(ell-1)**2*(ell+1))
    print("SERRE_FIXED_TRACE_CHEBOTAREV_DENSITY_UPPER_BOUND",ell,str(d))
print("SCOPE: LOCAL WITNESSES ONLY; CLASSNUMBER DIVISIBILITY IS THEOREM, NOT RECOMPUTED")
print("NOT PROVED: UNIFORM CLASSNUMBER UPPER BOUND, Sha GLOBAL FINITENESS, OR BSD")
