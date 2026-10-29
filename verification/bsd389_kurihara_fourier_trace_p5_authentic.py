#!/usr/bin/env python3
"""Exact Fourier/Artin--Schreier trace reconstruction of Kurihara delta_2501 (p=5).

Run inside SageMath 10.9 environment:
    python -u verification/bsd389_kurihara_fourier_trace_p5_authentic.py
or with an already exported table:
    python -u verification/bsd389_kurihara_fourier_trace_p5_authentic.py --table PATH

This is a genuine small-prime end-to-end regression using Neron-normalized
ECModularSymbol(389a1,sign=1) and the 390 Manin-edge presentation.
It is NOT a fast method for p=599: constructing one Fourier coefficient
naively still uses O(n) modular symbols; K=GF(5^60) is feasible while
GF(599^(10071454220)) is not.
"""
import argparse
import math
import time

from sage.all import GF, QQ, ZZ, EllipticCurve, matrix, vector, set_random_seed
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import table_390, symbol_by_manin

P, Q1, Q2 = 5, 41, 61
N = Q1 * Q2
D = 60


def logs_mod_p(q):
    divs = list(ZZ(q-1).prime_divisors())
    g = next(k for k in range(2,q)
             if all(pow(k,(q-1)//int(d),q)!=1 for d in divs))
    L=[0]*q
    a=1
    for j in range(q-1):
        L[a]=j%P
        a=a*g%q
    assert a==1
    return g,L


def manin_table(filename):
    if filename:
        with open(filename) as f:
            numbers=list(map(int,f.read().split()))
        assert len(numbers)==393
        assert numbers[:3]==[P,Q1,Q2]
        assert all(0<=a<P for a in numbers[3:])
        return numbers[3:389+3],numbers[-1]
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    symbol=ECModularSymbol(E,sign=1)
    return table_390(symbol,P)


def field_trace_p(element, p, count):
    total=element.parent()(0)
    x=element
    for _ in range(count):
        total+=x
        x=x**p
    return total


def relative_trace_k0(element, p, h):
    total=element.parent()(0)
    x=element
    pp=p**p
    for _ in range(h):
        total+=x
        x=x**pp
    return total


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--table',default=None)
    args=ap.parse_args()
    t=time.monotonic()
    F=GF(P)
    table=manin_table(args.table)
    assert len(table[0])==389
    g1,L1=logs_mod_p(Q1)
    g2,L2=logs_mod_p(Q2)
    assert (g1,g2)==(6,2)
    assert L1[P]==2 and L2[P]==2

    values=[0]*N
    for a in range(1,N):
        if math.gcd(a,N)==1:
            values[a]=int(symbol_by_manin(a,N,P,table))
    assert all(values[a]==values[-a%N] for a in range(N))
    delta=sum(values[a]*L1[a%Q1]*L2[a%Q2] for a in range(N))%P
    assert delta==4,('Kurihara direct normalization mismatch',delta)
    print('K5_AUTHENTIC_MANIN_DIRECT_DELTA_PASS',delta,'n',N,flush=True)

    K=GF(P**D,'z')
    set_random_seed(3892026)
    while True:
        z=K.random_element()**((P**D-1)//N)
        if z!=1 and z**(N//Q1)!=1 and z**(N//Q2)!=1:
            break
    assert z**N==1
    z1,z2=z**Q2,z**Q1
    A1=sum((K(L1[a])*z1**a for a in range(1,Q1)),K(0))
    A2=sum((K(L2[a])*z2**a for a in range(1,Q2)),K(0))
    c1,c2=L1[P],L2[P]
    assert A1**P-A1==K(c1)
    assert A2**P-A2==K(c2)
    lam=c2*pow(c1,-1,P)%P
    beta=A2-K(lam)*A1
    assert beta**P==beta
    beta0=next(b for b in range(P) if beta==K(b))
    print('K5_ARTIN_SCHREIER_FIELD_PASS','degree',D,'c',(c1,c2),
          'lambda',lam,'beta',beta0,flush=True)

    # beta is a choice-of-root gauge. Change primitive n-th root by t
    # with t = 1 mod q1 and ell_2(t) = -beta mod p.
    residue2=pow(g2,(-beta0)%P,Q2)
    tcrt=(1+Q1*(((residue2-1)*pow(Q1,-1,Q2))%Q2))%N
    assert tcrt%Q1==1 and tcrt%Q2==residue2 and math.gcd(tcrt,N)==1
    znew=z**tcrt
    assert znew**Q2==z1
    zz2=znew**Q1
    A2new=sum((K(L2[a])*zz2**a for a in range(1,Q2)),K(0))
    assert A2new==A2-K(beta0)==K(lam)*A1
    print('K5_BETA_NORMALIZATION_ROOT_CHANGE_PASS','root_exponent',tcrt,flush=True)

    seen=set()
    reps=[]
    for m in range(1,N):
        if math.gcd(m,N)!=1 or m in seen:
            continue
        x=m
        orbit=set()
        for _ in range(D):
            orbit.add(x)
            orbit.add((-x)%N)
            x=x*P%N
        assert x==m and len(orbit)==2*D,('sign orbit overlap',m,len(orbit))
        assert orbit.isdisjoint(seen)
        seen.update(orbit)
        reps.append(m)
    assert len(seen)==(Q1-1)*(Q2-1)
    assert len(reps)==20
    print('K5_SIGN_FROBENIUS_ORBITS_PASS',len(reps),flush=True)

    # A1 is an AS generator of degree P=5 over F_5.
    powers=[A1**i for i in range(P)]
    B=matrix(F,[list(a.vector()) for a in powers]).transpose()
    assert B.rank()==P
    inv1=pow(Q2,-1,Q1)
    inv2=pow(Q1,-1,Q2)
    h=D//P
    total=0
    for index,m in enumerate(reps):
        # True additive Fourier coefficient of S, using authentic Manin data.
        ratio=z**((-m)%N)
        running=K(1)
        shat=K(0)
        for aa in range(N):
            if values[aa]:
                shat+=K(values[aa])*running
            running*=ratio
        assert running==1
        b1=L1[m*inv1%Q1]
        b2=L2[m*inv2%Q2]
        what=(A1+K(b1))*(A2+K(b2))
        u2=lam
        u1=(beta0+b2+lam*b1)%P
        u0=b1*(beta0+b2)%P
        assert what==K(u0)+K(u1)*A1+K(u2)*A1**2

        H=relative_trace_k0(shat,P,h)
        assert H**(P**P)==H
        hc=B.solve_right(vector(F,list(H.vector())))
        assert H==sum((K(int(hc[j]))*powers[j] for j in range(P)),K(0))
        tr_value=int(field_trace_p(what*H,P,P))
        top_formula=-(u2*int(hc[P-3])+u1*int(hc[P-2])+u0*int(hc[P-1]))%P
        assert tr_value==top_formula,('trace coefficients',m,tr_value,top_formula)
        assert int((what*shat).trace())==tr_value
        total=(total+2*top_formula)%P
        if index in (0,len(reps)-1):
            print('K5_FOURIER_ORBIT_TRACE_PASS',index,m,'trace',tr_value,
                  'h_top',[int(hc[j]) for j in range(P-3,P)],flush=True)

    total=total*pow(N,-1,P)%P
    assert total==delta==4
    print('K5_AUTHENTIC_FOURIER_ARTIN_SCHREIER_DELTA_PASS',total,
          'classes',len(reps),'target_coefficients',3*len(reps),
          'seconds',round(time.monotonic()-t,3),flush=True)
    print('BOUNDARY: proves small-prime regression, NOT a sublinear p599 algorithm.',flush=True)


if __name__=='__main__':
    main()
