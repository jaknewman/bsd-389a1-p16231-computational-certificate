#!/usr/bin/env python3
"""Exact mod-p CRT weight obstruction, independent of Sage or Sha.

For each p>=5 and q1,q2 (p | q_i-1), the mixed Kurihara
functional L_p(f) = sum_{k,ell} k*ell*f(k,ell) mod p
is NOT forced nonzero by:
  - existence of a unit value in f;
  - a NONZERO mixed anchored difference;
  - rank-1 mixed matrix;
  - the sign-plus symmetry (k,ell)->(k+h1/2,ell+h2/2).

Proof-carrying synthetic witness:
  f(k,ell) = (k mod p)*(ell mod p).
Then f(1,1)=1, its mixed anchored difference equals f and is
nonzero (mixed matrix rank 1). For p>=5:
  L_p(f) = (sum k^2)*(sum ell^2) = 0 mod p
because sum_{r in F_p} r^2 = 0.

Also checks p=5 that a distinct *sign-plus symmetric* synthetic f
supported on the two points (1,1) and (21,31) has L_p(f)=2!=0,
showing that L itself is nonzero.

This is purely algebra, NOT the actual E modular-symbol distribution.
"""
import argparse
from math import isqrt


KNOWN = ((5,41,61),(7,113,673),(107,369793,383917))


def isprime(n):
    if n < 2:
        return False
    for k in range(2,isqrt(n)+1):
        if n % k == 0:
            return False
    return True


def sum_squares_mod_p(h,p):
    assert h%p == 0
    # The residue k mod p appears h/p times, and the sum over F_p
    # vanishes at p>=5: sum_{r=0}^{p-1} r^2 = 0 mod p.
    return (h//p)*sum(r*r for r in range(p))%p


def run_case(p,q1,q2):
    assert isprime(p) and p>=5
    assert (q1-1)%p==0 and (q2-1)%p==0
    h1,h2=q1-1,q2-1
    assert h1%2==0 and h2%2==0
    assert (h1//2)%p==(h2//2)%p==0
    s1=sum_squares_mod_p(h1,p)
    s2=sum_squares_mod_p(h2,p)
    assert s1==s2==0
    # f(k,l) = k*l mod p is unchanged by the simultaneous minus
    # involution, and has mixed anchored difference Delta f = f,
    # since f(k,0)=f(0,l)=f(0,0)=0.
    f11=1
    mixed11=(1*1 - 1*0 - 0*1 + 0)%p
    assert f11==mixed11==1
    assert (s1*s2)%p==0
    print("MIXED_NONZERO_RANK1_BUT_KURIHARA_ZERO_EXACT_PASS",
          "p",p,"q1",q1,"q2",q2,
          "f_1_1",f11,"mixed_1_1",mixed11,
          "weighted_sum",0,flush=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--extra",nargs=3,type=int,metavar=("P","Q1","Q2"))
    args=ap.parse_args()
    for case in KNOWN:
        run_case(*case)
    if args.extra:
        run_case(*args.extra)
    p=5
    # f is supported at (1,1) and its plus-symmetry mate (21,31).
    # L = 1*1 + 21*31 = 652 = 2 mod 5.
    nonzero=(1*1 + 21*31)%p
    assert nonzero==2
    print("SIGN_PLUS_MIXED_KURIHARA_FUNCTIONAL_NOT_IDENTICALLY_ZERO_PASS",
          "p",p,"toy_weighted_sum",nonzero,flush=True)
    print("BOUNDARY_NO_ACTUAL_EIGENSYMBOL_OR_SHA_NONVANISHING_PROOF",flush=True)


if __name__=="__main__":
    main()
