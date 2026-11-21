#!/usr/bin/env python3
"""Finite-level GMA coefficient gate for E=389a1.

Checks cyclotomic congruences and upper-right conjugation using Frobenius
companion matrices. Does not establish global automorphy, local Selmer
compatibility or BSD.
"""
from hashlib import sha256

PRIMES=(5,7,11,107,599,16231)
FROBENIUS=(2,3,5,7,11,13,17,19,23,29,31,37)
KNOWN_AP={2:-2,3:-2,5:-3,7:-5,11:-4}

def ap(ell):
    n=sum((y*y+y-x*x*x-x*x+2*x)%ell==0
          for x in range(ell) for y in range(ell))
    return ell-n

def mul(A,B,m):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%m
            for j in range(len(B[0]))] for i in range(len(A))]

def off(v):return [[0,0,v[0]],[0,0,v[1]],[0,0,0]]

def check(p,n,ell,a):
    m=p**n
    k=(p-1)*p**(n-1)
    assert pow(ell,k,m)==1
    A=[[0,-ell],[1,a]]
    d=pow(ell,k,m)
    R=[[0,-ell,0],[1,a,0],[0,0,d]]
    invell=pow(ell,-1,m)
    Ainv=[[a*invell,ell*invell],[-invell,0]]
    Rinv=[[Ainv[0][0],Ainv[0][1],0],
          [Ainv[1][0],Ainv[1][1],0],
          [0,0,pow(d,-1,m)]]
    assert mul(R,Rinv,m)==[[1,0,0],[0,1,0],[0,0,1]]
    for v in ((1,0),(0,1),(1,2)):
        result=mul(mul(R,off(v),m),Rinv,m)
        Av=((A[0][0]*v[0]+A[0][1]*v[1])%m,
            (A[1][0]*v[0]+A[1][1]*v[1])%m)
        assert result==off(Av)
    return 3

def main():
    aps={ell:ap(ell) for ell in FROBENIUS}
    for ell,a in KNOWN_AP.items(): assert aps[ell]==a
    print("BSD389_ELLIPTIC_FROBENIUS_TRACES_PASS",aps)
    total=0
    digest=sha256()
    for p in PRIMES:
        for n in (1,2,3,4):
            m=p**n
            k=(p-1)*p**(n-1)
            assert pow(1+p,k,m)==1
            assert pow(1+p,k,m*p)==(1-m)%(m*p)
            if n>1:
                previous=(p-1)*p**(n-2)
                assert pow(1+p,previous,m)==(1-p**(n-1))%m
            count=0
            for ell,a in aps.items():
                if ell==p:continue
                count+=check(p,n,ell,a)
                digest.update(f"{p},{n},{ell},{a},{k};".encode())
            total+=count
            print("BSD389_REGULARIZED_GMA_LEVEL_PASS",
                  "p",p,"n",n,"k",k,"frobenius_vectors",count)
    print("BSD389_REGULARIZED_GMA_TOWER_PASS",
          "frobenius_vector_checks",total,
          "sha256",digest.hexdigest())
    print("BOUNDARY: finite-level coefficient congruences only; "
          "no fixed compatible p-adic automorphic tower, Selmer comparison "
          "or uniform bound on Sha.")
if __name__=="__main__":main()
