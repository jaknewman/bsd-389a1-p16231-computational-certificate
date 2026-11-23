#!/usr/bin/env python3
"""REAL Hecke distribution and 1-variable diagonal Kurihara rank-two identity.

All sums use the authenticated 390 integer plus modular-symbol vector,
not hypothetical coefficients. Full original terms are enumerated at p5
(q41,61) and p11 (q397,991). No Sage is needed.

This is an exact conductor-dependent Hecke/diagonal THEOREM TEST, not
uniform Sha finiteness or the complex BSD leading-coefficient identity.
"""
from math import comb
from time import monotonic

from bsd389_p11_Kurihara_Plucker_non_decomposability_gate import (
    logs, modular_symbol,
)

TESTS=((5,41,61,4),(11,397,991,1))
D=6

def point_count(q):
    total=1
    for x in range(q):
        z=(1+4*(x*x*x+x*x-2*x))%q
        total+=1 if z==0 else 2 if pow(z,(q-1)//2,q)==1 else 0
    return total

def one_prime(p,q,L):
    assert (q-1)%(2*p)==0
    out=[0]*(D+1)
    for a in range(1,(q-1)//2+1):
        s=(2*modular_symbol(a,q,p))%p
        for k in range(D+1):
            if int(L[a])>=k:
                out[k]=(out[k]+s*comb(int(L[a]),k))%p
    return out

def Euler_factor(p,new,old,L_old):
    e=int(L_old[new%old])
    a_new=new+1-point_count(new)
    E=[(a_new-2)%p]
    for k in range(1,D+1):
        E.append((-comb(e,k)-comb(p-e,k))%p)
    return e,E

def convolution(E,old,p):
    return [sum(E[j]*old[d-j] for j in range(d+1))%p
            for d in range(D+1)]

def complete_pair(p,q1,q2,expected):
    start=monotonic()
    _,L1=logs(q1,p)
    _,L2=logs(q2,p)
    old1=one_prime(p,q1,L1)
    old2=one_prime(p,q2,L2)
    M=[[0]*5 for _ in range(5)]
    col=[0]*(D+1)   # theta_n(T1,0)
    row=[0]*(D+1)   # theta_n(0,T2)
    diagonal={}
    diagonals=[(1,1),(1,2),(2,3)]
    for u,v in diagonals:diagonal[(u,v)]=0
    n=q1*q2
    for a in range(1,(n-1)//2+1):
        r1,r2=a%q1,a%q2
        if not r1 or not r2:continue
        e,f=int(L1[r1]),int(L2[r2])
        coeff=(2*modular_symbol(a,n,p))%p
        if not coeff:continue
        b1=[comb(e,k) if e>=k else 0 for k in range(D+1)]
        b2=[comb(f,k) if f>=k else 0 for k in range(D+1)]
        for i in range(D+1):
            col[i]=(col[i]+coeff*b1[i])%p
            row[i]=(row[i]+coeff*b2[i])%p
        for i in range(5):
            for j in range(5):
                M[i][j]=(M[i][j]+coeff*b1[i]*b2[j])%p
        for u,v in diagonals:
            z=(u*e+v*f)%p
            diagonal[(u,v)]=(diagonal[(u,v)]+coeff*comb(z,2))%p
    assert M[0][0]==M[1][0]==M[0][1]==M[2][0]==M[0][2]==0
    assert M[1][1]==expected
    for u,v in diagonals:
        assert diagonal[(u,v)]==(u*v*expected)%p
    e2,E2=Euler_factor(p,q1,q2,L2)
    e1,E1=Euler_factor(p,q2,q1,L1)
    assert convolution(E2,old2,p)==row
    assert convolution(E1,old1,p)==col
    assert old1[0]==old2[0]==0
    print('AUTHENTIC_HECKE_CONDUCTOR_NORM_BOTH_DIRECTIONS_PASS',
          p,q1,q2,'crosslogs',(e1,e2),
          'old_single_quadratic',(old1[2],old2[2]),
          'projected_degree_0_to_6',(col,row),flush=True)
    print('AUTHENTIC_DIAGONAL_QUADRATIC_EQUALS_KURIHARA_PASS',
          p,q1,q2,'delta',expected,'diagonal_choices',diagonal,
          'raw_M33',M[3][3],
          'elapsed_seconds',round(monotonic()-start,2),flush=True)
    return M

for p,q1,q2,expected in TESTS:
    complete_pair(p,q1,q2,expected)
print('ALL_REAL_ONE_VARIABLE_DIAGONAL_QUADRATIC_AND_HECKE_NORM_TESTS_PASS')
print('BOUNDARY_NO_UNIFORM_NONVANISHING_OR_GLOBAL_SHA_FINITENESS')
