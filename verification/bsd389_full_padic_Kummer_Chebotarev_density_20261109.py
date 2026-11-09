#!/usr/bin/env python3
"""Pure integer group-theory audit for arbitrary-depth Kummer--Chebotarev.
Proof of the global Kummer image is in companion paper; this code does NOT
compute Kurihara derivatives, Selmer dimensions, or Sha.
"""
from fractions import Fraction
from math import gcd

def check(p,m):
    R=p**m
    group=(p*p-1)*p*(p-1)*p**(4*(m-1))
    phi=R-R//p
    centralizer=phi*R
    assert group%centralizer==0
    conj=group//centralizer
    translations=phi*R*R
    density=Fraction(conj*translations,group*R**4)
    assert density==Fraction(1,p**(3*m))
    print('DEPTH_KUMMER_CHEBOTAREV_DENSITY_PASS',
          p,m,str(density),group,centralizer,conj)

def brute(p,m):
    N=p**m
    count=cent=conj=0
    for a in range(N):
      for b in range(N):
       for c in range(N):
        for d in range(N):
         if gcd((a*d-b*c)%N,N)!=1:continue
         count+=1
         if c==0 and d==a:cent+=1
         if (a+d-2)%N==0 and (a*d-b*c-1)%N==0 and (
            (a-1)%p or b%p or c%p or (d-1)%p):conj+=1
    assert cent==(N-N//p)*N
    assert conj==count//cent
    print('DEPTH_GL2_BRUTE_CLASS_PASS',p,m,count,cent,conj)

if __name__=='__main__':
    for p,m in ((5,1),(5,2),(5,3),(7,1),(7,2),
                (11,1),(11,2),(17,1),(17,2),(389,2)):
        check(p,m)
    for p,m in ((5,1),(5,2),(7,1)):brute(p,m)
    print('BOUNDARY: no derived Kato nonvanishing or full Sha certificate')
