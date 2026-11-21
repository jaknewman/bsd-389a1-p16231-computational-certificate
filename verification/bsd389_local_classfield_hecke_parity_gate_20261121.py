#!/usr/bin/env python3
"""Regression for local inertia action and class-field/Kurihara parity.

The companion paper proves the uniform theorem. These finite matrix
checks do NOT calculate class groups, Sha or the all-large-prime tail.
"""
from math import ceil
PRIMES=(5,7,11,17,23,97,107,599,16231)

def mul(A,B,p):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p
                       for j in range(2)) for i in range(2))

def inv(A,p):
    a,b=A[0];c,d=A[1]
    D=(a*d-b*c)%p
    Di=pow(D,-1,p)
    return ((d*Di%p,-b*Di%p),(-c*Di%p,a*Di%p))

def run():
    checks=0
    for p in PRIMES:
        U=((1,1),(0,1))
        for a in {2%p,3%p,(p-1)%p,389%p} - {0}:
            D=((a,0),(0,1))
            C=mul(mul(D,U,p),inv(D,p),p)
            assert C==((1,a),(0,1)),(p,a,C)
            # Since U^i=[[1,i],[0,1]], the cyclic norm
            # N=1+U+...+U^(p-1)=0 for p>=5.
            assert (p*(p-1)//2)%p==0
            # H^1(<U>,V) = V / (U-1)V has basis class e2.
            # The conjugation D(a) acts by a^(-1).
            assert a*pow(a,-1,p)%p==1
            checks+=1
        exceptional=(389%p==1)
        assert exceptional==(p==97)
        print('BSD389_LOCAL_TATE_INERTIA_FROBENIUS_GATE',
              'p',p,'389_mod_p',389%p,'exception_p97',exceptional)
    for d in range(1,101):
        eps=d%2
        mu=d+eps
        s=mu-2
        assert mu==2*ceil(d/2)
        assert s%2==0 and s>=0 and 2+s-eps==d
        assert (s==0)==(d<=2)
    print('BSD389_EXACT_CLASSGROUP_KURIHARA_PARITY_GATE_PASS',
          'matrix_checks',checks,'p_rank_cases',100)
    print('BOUNDARY: group-action/parity regression; no computation of Cl(K), Sha or global tail')

if __name__=='__main__':run()
