#!/usr/bin/env python3
"""Sage/eclib rank-two Kurihara p7 Hecke and wild-quotient dual test.

Pairs (113,281) and (113,673) are independently known to yield
delta=0 and delta=2 mod 7. Check BOTH cases with authentic
Neron-normalized symbols, exact Hecke fibres, and all four
first-order wild quotient coefficients.

Runtime: scans 31,753 + 76,049 rational arguments, not p599's giant n.
No claim of Sha[599] or of a faster tame-norm computation.
"""
import math
from sage.all import EllipticCurve, QQ, ZZ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin

P,Q1 = 7,113
Q2_EXPECTED = ((281,0),(673,2))

def dlogs(q):
    factors=[int(v) for v in ZZ(q-1).prime_divisors()]
    gen=next(g for g in range(2,q)
             if all(pow(g,(q-1)//d,q)!=1 for d in factors))
    L=[0]*q
    x=1
    for k in range(q-1):
        L[x]=k%P
        x=x*gen%q
    assert x==1
    return gen,L

def direct_modular_symbol(phi,a,n):
    v=QQ(phi(QQ(a)/n))
    assert int(v.denominator())%P
    return int(v.numerator())*pow(int(v.denominator()),-1,P)%P

def run_pair(E, phi, tab, q2, expected):
    q1=Q1
    n=q1*q2
    a1=int(E.ap(q1))
    a2=int(E.ap(q2))
    assert q1%P==q2%P==1 and a1%P==a2%P==2
    print("K7_HEC_AUXILIARY_PASS",q1,q2,"a_q",a1,a2,flush=True)

    symbols=[0]*n
    bucket1=[0]*q1
    bucket2=[0]*q2
    for a in range(1,n):
        if a%q1==0 or a%q2==0:
            continue
        z=int(symbol_by_manin(a,n,P,tab))
        symbols[a]=z
        bucket1[a%q1]=(bucket1[a%q1]+z)%P
        bucket2[a%q2]=(bucket2[a%q2]+z)%P
    for a in (1,2,3,17,47):
        if math.gcd(a,n)==1:
            assert symbols[a]==direct_modular_symbol(phi,a,n),(a,q2)
    assert all(symbols[a]==symbols[n-a] for a in range(1,n))
    print("K7_MANIN_ECLIB_SAMPLE_AND_PARITY_PASS",n,flush=True)

    for modulus,other,bucket,ap_other in (
        (q1,q2,bucket1,a2),
        (q2,q1,bucket2,a1)):
        s=[0]*modulus
        for b in range(1,modulus):
            s[b]=int(symbol_by_manin(b,modulus,P,tab))
        inv=pow(other,-1,modulus)
        for b in range(1,modulus):
            rhs=(ap_other*s[b]-s[b*other%modulus]
                 -s[b*inv%modulus])%P
            assert bucket[b]==rhs,("Hecke fibre mismatch",q2,modulus,b)
            laplacian=(2*s[b]-s[b*other%modulus]
                       -s[b*inv%modulus])%P
            assert bucket[b]==laplacian,("modp Laplacian mismatch",q2,modulus,b)
        print("K7_HEC_ALL_FIBRES_LAPLACIAN_PASS",
              "q2",q2,"modulus",modulus,"checked",modulus-1,flush=True)

    g1,L1=dlogs(q1)
    g2,L2=dlogs(q2)
    theta=[0]*4
    T=[[0]*P for _ in range(P)]
    for a in range(1,n):
        z=symbols[a]
        if z==0:continue
        u,v=L1[a%q1],L2[a%q2]
        T[u][v]=(T[u][v]+z)%P
        theta[0]=(theta[0]+z)%P
        theta[1]=(theta[1]+u*z)%P
        theta[2]=(theta[2]+v*z)%P
        theta[3]=(theta[3]+u*v*z)%P
    reduced=[
        sum(T[u][v]*factor(u,v) for u in range(P)
            for v in range(P))%P
        for factor in (lambda u,v:1,lambda u,v:u,
                       lambda u,v:v,lambda u,v:u*v)
    ]
    assert reduced==theta
    assert theta==[0,0,0,expected],("Kurihara moments",q2,theta,expected)
    print("K7_LOWER_MOMENTS_AND_WILD_DERIVATIVE_PASS",
          "q2",q2,"moments",theta,"classes",P*P,
          "roots",g1,g2,flush=True)

    for t in (2,7,17,599):
        assert math.gcd(t,n)==1
        translation=sum(
            L1[a%q1]*L2[a%q2]*symbols[(t*a)%n]
            for a in range(1,n)
            if a%q1 and a%q2
        )%P
        assert translation==expected,("translate",q2,t,translation)
        print("K7_TRANSLATION_PASS","q2",q2,"t",t,
              "delta",translation,flush=True)
    print("K7_KURIHARA_DIRECT_AND_HEC_PASS",
          "q2",q2,"delta",theta[3],flush=True)

def main():
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    phi=ECModularSymbol(E,sign=1)
    tab=table_390(phi,P)
    for q2,expected in Q2_EXPECTED:
        run_pair(E,phi,tab,q2,expected)
    print("K7_DUAL_ZERO_AND_NONZERO_HECKE_REGRESSION_PASS",
          "delta_113x281",0,"delta_113x673",2,flush=True)
    print("BOUNDARY: authentic finite p7 tests only; no p599 delta or Sha certificate.",flush=True)

if __name__=="__main__":
    main()
