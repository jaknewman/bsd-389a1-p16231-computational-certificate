#!/usr/bin/env python3
"""E389a1: exact p-local Mordell--Weil primitivity test and strict Selmer witness.

For p in {5,7,11,107,599,16231}, compute N_p*[P,Q] mod p^2
on the integral short Weierstrass model Y^2=X^3-3024X+46224,
X=36x+12 and Y=216y+108. The change of variables has unit
scaling at all tested p. Compute the original formal parameter
t=-x/y, whose relation to short-model t'=-X/Y near infinity is
t = 6*t' (mod p^2).

An exact, independent rational-arithmetic audit is done at p=5,7,11.
No Sage or external packages required.

Results concern ONLY local MW primitivity, not a proof of a global
Fitting bound, an Euler-system nonvanishing theorem, or BSD.
"""
from fractions import Fraction
from math import gcd

PRIMES = (5,7,11,107,599,16231)
APS = {5:-3,7:-5,11:-4,107:0,599:0,16231:128}
GEN = ((-1,1),(0,-1))
EXPECTED = {5:(3,1),7:(2,4),11:(8,2),
            107:(13,42),599:(119,121),16231:(8987,7760)}
A = -3024
B = 46224

def ap_legendre(p):
    s = 0
    for x in range(p):
        d = (1+4*(x*x*x+x*x-2*x)) % p
        if d:
            u = pow(d,(p-1)//2,p)
            assert u in (1,p-1)
            s += 1 if u==1 else -1
    return -s

def on_curve(J,m):
    X,Y,Z = J
    return (Y*Y-X*X*X-A*X*pow(Z,4,m)-B*pow(Z,6,m))%m==0

def dbl(J,m):
    X,Y,Z = J
    yy = Y*Y % m
    s = 4*X*yy % m
    t = (3*X*X+A*pow(Z,4,m))%m
    x = (t*t-2*s)%m
    y = (t*(s-x)-8*yy*yy)%m
    z = 2*Y*Z%m
    ans = (x,y,z)
    assert on_curve(ans,m)
    return ans

def near_infinity_plus_finite(near,finite,m,p):
    # The generic Jacobian addition formula is incomplete when either
    # input reduces to infinity modulo p. Use the invariant vector
    # field for the elliptic formal group, exact modulo p^2.
    X,Y,Z=near
    assert Z%p==0 and X%p and Y%p
    XX,YY,ZZ=finite
    assert ZZ%p
    zi=pow(ZZ,-1,m)
    x=XX*zi*zi%m
    y=YY*zi*zi*zi%m
    t=-X*Z*pow(Y,-1,m)%m
    assert t%p==0
    out=((x+2*y*t)%m,(y+(3*x*x+A)*t)%m,1)
    assert on_curve(out,m)
    return out

def add(J,K,m,p):
    X1,Y1,Z1 = J
    X2,Y2,Z2 = K
    if Z1%p==0 and Z2%p==0:
        raise AssertionError("ladder invariant violated: both points infinity mod p")
    if Z1%p==0:return near_infinity_plus_finite(J,K,m,p)
    if Z2%p==0:return near_infinity_plus_finite(K,J,m,p)
    z1sq = Z1*Z1 % m
    z2sq = Z2*Z2 % m
    u1 = X1*z2sq % m
    u2 = X2*z1sq % m
    s1 = Y1*z2sq*Z2 % m
    s2 = Y2*z1sq*Z1 % m
    h = (u2-u1)%m
    r = (s2-s1)%m
    # The Montgomery ladder always adds points differing by
    # the fixed non-infinity point P or Q modulo p.
    assert h%p or r%p, ("indeterminate addition", p,J,K)
    hh = h*h%m
    hhh = hh*h%m
    x = (r*r-hhh-2*u1*hh)%m
    y = (r*(u1*hh-x)-s1*hhh)%m
    z = h*Z1*Z2%m
    ans = (x,y,z)
    assert on_curve(ans,m)
    assert any(v%p for v in ans), ("nonprimitive Jacobian",p,J,K)
    return ans

def ladder(J,n,m,p):
    r0=(1,1,0)
    r1=J
    assert on_curve(r1,m)
    for bit in bin(n)[2:]:
        if bit=="0":
            r1=add(r0,r1,m,p)
            r0=dbl(r0,m)
        else:
            r0=add(r0,r1,m,p)
            r1=dbl(r1,m)
        assert any(v%p for v in r0)
        assert any(v%p for v in r1)
    return r0

def rational_add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and y+v==-1:return None
    if P==Q:
        slope = (3*x*x+2*x-2)/(2*y+1)
    else:
        slope = (v-y)/(u-x)
    xx=slope*slope-1-x-u
    yy=-slope*(xx-x)-y-1
    return (xx,yy)

def rational_multiple(P,n):
    r=None
    while n:
        if n&1:r=rational_add(r,P)
        P=rational_add(P,P)
        n//=2
    return r

def fraction_mod(q,m):
    assert gcd(q.denominator,m)==1
    return q.numerator*pow(q.denominator,-1,m)%m

def run():
    count=0
    assert -16*(4*A**3+27*B**2)==389*6**12
    for p in PRIMES:
        a=ap_legendre(p)
        assert a==APS[p], (p,a)
        npoints=p+1-a
        assert npoints%p!=0 and p!=389
        t_values=[]
        for x,y in GEN:
            assert y*y+y==x*x*x+x*x-2*x
            m=p*p
            X=(36*x+12)%m
            Y=(216*y+108)%m
            J=ladder((X,Y,1),npoints,m,p)
            xj,yj,zj=J
            assert zj%p==0 and xj%p and yj%p
            # t_old = 6*t_short + O(t_short^3), hence exact mod p^2
            t=(-6*xj*zj*pow(yj,-1,m))%m
            assert t%p==0
            t_values.append(t//p)
            if p in (5,7,11):
                R=rational_multiple((Fraction(x),Fraction(y)),npoints)
                assert R is not None and R[1] !=0
                original_t = fraction_mod(-R[0]/R[1],m)
                assert original_t==t, (p,x,y,t,original_t)
            count+=1
        assert tuple(t_values)==EXPECTED[p], (p,t_values)
        assert t_values[0]%p
        coeff=t_values[1]*pow(t_values[0],-1,p)%p
        print("BSD389_P_LOCAL_MW_PRIMITIVE_PASS",
              "p",p,"a_p",a,"N_p",npoints,
              "P_t_over_p",t_values[0],"Q_t_over_p",t_values[1],
              "Q_over_P_mod_p",coeff)
    # p=19 forces an intermediate infinity branch in the ladder.
    # Regression prevents false projective arithmetic at bad charts.
    p=19
    npoints=15
    m=p*p
    regression=[]
    for x,y in GEN:
        J=ladder(((36*x+12)%m,(216*y+108)%m,1),npoints,m,p)
        xx,yy,zz=J
        assert zz%p==0 and xx%p and yy%p
        regression.append(((-6*xx*zz*pow(yy,-1,m))%m)//p)
    assert tuple(regression)==(16,8),regression
    print("BSD389_FORMAL_INFINITY_ADDITION_BRANCH_PASS",tuple(regression))
    print("BSD389_P_STRICT_RANK_ONE_LOCAL_GATE_PASS",
          "primes",len(PRIMES),"point_checks",count,
          "independent_rational_checks",6)
    print("BOUNDARY: strict-Selmer splitting follows algebraically "
          "from rank-two MW and local primitivity; Sha finiteness and "
          "a nonzero Fitt_1 bound NOT established.")

if __name__ == "__main__":
    run()
