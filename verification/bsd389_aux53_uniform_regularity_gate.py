#!/usr/bin/env python3
"""BSD 389a1: exact 53-adic Frobenius depth at a variable split prime.

Standard-library-only arithmetic. Computes the exact integer
  m_p = v_53((pi / conjugate(pi))**54 - 1)
with pi=A+B*w, w^2+w+1=0, norm(pi)=p and p != 53.
The first 53-power ring-class character of order 53**n that detects
Frob_pi has n=m_p (conductor 53**(m_p+1)).

This is a local regularity certificate, NOT a theta-order or Sha certificate.
For primality of large input p, independent proof is required.
"""
from __future__ import annotations
import argparse
from math import isqrt
Q = 53

def norm(a: int, b: int) -> int:
    return a*a - a*b + b*b

def mul(x: tuple[int,int], y: tuple[int,int], modulus: int) -> tuple[int,int]:
    a,b=x; c,d=y
    return ( (a*c-b*d)%modulus, (a*d+b*c-b*d)%modulus )

def exponentiate(x: tuple[int,int], n: int, modulus: int) -> tuple[int,int]:
    ans=(1,0)
    while n:
        if n&1: ans=mul(ans,x,modulus)
        x=mul(x,x,modulus)
        n >>= 1
    return ans

def is_prime_trial(n: int) -> bool:
    """Only used for the small built-in examples."""
    if n<2: return False
    for k in range(2,isqrt(n)+1):
        if n%k==0: return False
    return True

def split_frobenius_depth(a: int, b: int, max_depth: int=16):
    p=norm(a,b)
    if p<=3 or p%3!=1 or p%Q==0:
        raise ValueError('Norm must be a split rational prime p!=53, p>3.')
    for m in range(1,max_depth+1):
        modulus=Q**(m+1)
        # pi/conjugate(pi) = pi**2 / Norm(pi), all q-adic units
        pi=(a%modulus,b%modulus)
        pi2=mul(pi,pi,modulus)
        inv=pow(p,-1,modulus)
        u=tuple((t*inv)%modulus for t in pi2)
        residue=exponentiate(u,Q+1,modulus)
        if residue != (1,0):
            # Since the residue is 1 mod q**m (but not q**(m+1)),
            # the tangent mod q is nonzero and has trace zero.
            assert (residue[0]-1)%Q**m==0 and residue[1]%Q**m==0
            tangent=((residue[0]-1)//Q**m %Q, residue[1]//Q**m %Q)
            assert tangent != (0,0)
            assert (2*tangent[0]-tangent[1])%Q==0
            return p,m,residue,tangent
    raise ArithmeticError(f'Not detected through 53-adic precision {max_depth+1}; raise --max-depth')

def ap_elliptic(p: int) -> int:
    # E: y^2+y=x^3+x^2-2x
    s=0
    for x in range(p):
        delta=(1+4*(x*x*x+x*x-2*x))%p
        if delta:
            s += 1 if pow(delta,(p-1)//2,p)==1 else -1
    return -s

def audit_example(p,a,b,m_expected,ap_expected=None):
    assert norm(a,b)==p and is_prime_trial(p)
    n,m,residue,tangent=split_frobenius_depth(a,b)
    assert m==m_expected
    # Six unit multiples and conjugation must give the same depth.
    ua, ub = a, b
    for _ in range(3):
        assert split_frobenius_depth(ua,ub)[1]==m
        assert split_frobenius_depth(-ua,-ub)[1]==m
        ua,ub = -ub,ua-ub  # multiply by w
    assert (ua,ub)==(a,b)
    assert split_frobenius_depth(a-b,-b)[1]==m
    if ap_expected is not None:
        assert ap_elliptic(p)==ap_expected
    print(f'PASS p={p} pi=({a},{b}) m53={m} '
          f'chi_order=53^{m} first_regular_conductor=53^{m+1} '
          f'normalized_tangent_mod53={tangent} '
          f'v54_mod_53pow{m+1}={residue}'
          + (f' ap={ap_expected}' if ap_expected is not None else ''))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a',type=int)
    parser.add_argument('--b',type=int)
    parser.add_argument('--max-depth',type=int,default=16)
    args=parser.parse_args()
    if (args.a is None)!=(args.b is None):
        parser.error('Use both --a and --b, or neither for built-in examples')
    if args.a is not None:
        p,m,r,t=split_frobenius_depth(args.a,args.b,args.max_depth)
        print(f'INPUT p={p} pi=({args.a},{args.b}) m53={m} '
              f'first_detecting_order=53^{m} conductor=53^{m+1} '
              f'residue={r} tangent_mod53={t}')
    else:
        audit_example(7,3,1,1)
        audit_example(1297,39,7,2,-38)
        audit_example(1579,42,5,2,-44)
        audit_example(1801,49,24,2,-27)
        # Explicit counterexample to v53(A*B*(A-B)) as a depth formula:
        assert (39*7*(39-7))%53 == 44
        print('PASS COUNTEREXAMPLE naive_m=v53(A*B*(A-B)) is 0 at p=1297, actual_m=2')