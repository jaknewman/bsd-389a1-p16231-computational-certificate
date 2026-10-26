#!/usr/bin/env python3
"""Small-prime exact n2/n3 finite-level regression of the C01/Sage bridge.

E=389a1, p=5 and 7. Independently evaluate full ordinary measures at n2
and n3, C01 scalar from M0/M1, and compare with Sage n3 series when
precision permits. No p=16231 global data are read.
THIS SCRIPT IS NEW / HAS NOT BEEN EXECUTED.
"""
from sage.all import EllipticCurve, QQ, ZZ

def modrat(x,p,k):
    x=QQ(x)
    d=int(x.denominator())
    if d%p==0: raise ArithmeticError("p-denominator in modular symbol")
    modulus=p**k
    return int(x.numerator())*pow(d,-1,modulus)%modulus

def finite_coefficient(f,p,alpha,n):
    modulus=p*p
    pn=p**n
    inv=pow(alpha,-1,modulus)
    ans=0
    for a in range(1,p):
        omega=pow(a,p**(n-1),pn)
        for j in range(2,p**(n-1)):
            x=omega*pow(1+p,j,pn)%pn
            top=modrat(f(QQ(x)/pn),p,2)
            bot=modrat(f(QQ(x)/(pn//p)),p,2)
            mu=pow(inv,n,modulus)*(top-inv*bot)%modulus
            ans=(ans+(j*(j-1)//2)*mu)%modulus
    return ans*pow(2,-1,modulus)%modulus

def scalar_J(f,p,alpha):
    p2,p3=p*p,p*p*p
    inv=pow(alpha,-1,p)
    J=0
    for a in range(1,p):
        omega=pow(a,p*p,p3)
        inv_a=pow(a,-1,p)
        fermat=((pow(a,p-1,p2)-1)//p)%p
        for b in range(p):
            x=a+p*b
            u=(b*inv_a-fermat)%p
            lift=omega*pow(1+p,u,p3)%p3
            assert (lift-x)%p2==0
            kappa=((lift-x)//p2)%p
            weight=((2*u-1)*inv_a)%p
            M0=(-modrat(f(QQ(x)/p2),p,1)
                +inv*modrat(f(QQ(x)/p),p,1))%p
            linear=0
            for c in range(p):
                linear=(linear+c*modrat(f(QQ(x+p2*c)/p3),p,1))%p
            M1=-inv*linear%p
            J=(J-weight*(M1-kappa*M0))%p
    return J

def check(p):
    E=EllipticCurve("389a1")
    assert E.is_good(p) and E.is_ordinary(p)
    L=E.padic_lseries(ZZ(p),implementation="eclib")
    assert E.real_components()==2
    assert L._quotient_of_periods_to_twist(1)==1
    alpha=int(L.alpha(prec=8).lift())%(p*p)
    assert (alpha*alpha-int(E.ap(p))*alpha+p)%(p*p)==0
    f=L.modular_symbol
    A2=finite_coefficient(f,p,alpha,2)
    A3=finite_coefficient(f,p,alpha,3)
    J=scalar_J(f,p,alpha)
    delta=(A3-A2)%(p*p)
    predicted=p*J*pow(4*alpha*alpha,-1,p*p)%(p*p)
    print("BRIDGE_SMALL_PRIME_DATA",p,"alpha",alpha,"A2n2",A2,
          "A2n3",A3,"J",J,"delta",delta,"expected",predicted,flush=True)
    assert delta==predicted,(p,delta,predicted)
    print("BRIDGE_SMALL_PRIME_N2_N3_CORRECTION_PASS",p,flush=True)
    bounds=L._prec_bounds(3,3)
    if bounds[2]>=2:
        sageA3=L.series(n=3,prec=3)[2]
        actual=int(ZZ(sageA3.lift())%(p*p))
        assert actual==A3,(p,actual,A3)
        print("BRIDGE_SMALL_PRIME_N3_EQUALS_SAGE_SERIES_PASS",p,flush=True)
    else:
        print("BRIDGE_SMALL_PRIME_N3_SERIES_PRECISION_INSUFFICIENT",p,flush=True)

if __name__=="__main__":
    check(5)
    check(7)
    print("BRIDGE_SMALL_PRIMES_5_7_DIRECT_ORACLE_PASS",flush=True)
    print("BOUNDARY: small-prime test, not p16231 direct n3 execution.",flush=True)
