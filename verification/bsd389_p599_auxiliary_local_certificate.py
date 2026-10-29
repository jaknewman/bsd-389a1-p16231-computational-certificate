#!/usr/bin/env python3
"""Exact independent auxiliary-prime and local MW certificate for 389a1 at p=599.

Curve: y^2+y = x^3+x^2-2*x.  In field F_q set Y=y+1/2:
Y^2=x^3+x^2-2*x+1/4.  All arithmetic below is integer modular
arithmetic. No Sage, eclib, probabilistic primality or symbolic oracle.

Usage:
  python -u bsd389_p599_auxiliary_local_certificate.py
  python -u bsd389_p599_auxiliary_local_certificate.py --search --limit 20000000

The default recomputes exact #E(F_q) for both selected primes by exhaustive
quadratic-residue counts and proves their local reduction matrix is invertible.
This does NOT compute Kurihara delta, the p-Selmer group, or Sha[p].
"""
import argparse
from math import isqrt

P = 599
Q1 = 6912461
Q2 = 13963889
EXPECTED = ((Q1, 1799, 6910663, (1, 536)),
            (Q2, -4191, 13968081, (1, 412)))

# Elliptic-curve group law on y'^2=x^3+x^2-2*x+1/4 over F_q.
# None denotes the identity. At x=0,1, original y=0 corresponds to Y=1/2.
def ec_add(A, B, q):
    if A is None:
        return B
    if B is None:
        return A
    x, y = A
    u, v = B
    if x == u:
        if (y + v) % q == 0:
            return None
        lam = (3*x*x + 2*x - 2) * pow(2*y, -1, q) % q
    else:
        lam = (v-y) * pow(u-x, -1, q) % q
    xx = (lam*lam - 1 - x - u) % q
    yy = (lam*(x-xx) - y) % q
    return (xx, yy)

def ec_mul(n, A, q):
    assert n >= 0
    B = None
    while n:
        if n & 1:
            B = ec_add(B, A, q)
        n >>= 1
        if n:
            A = ec_add(A, A, q)
    return B

def rational_generators_mod_q(q):
    half = (q + 1) // 2
    return (0, half), (1, half)

def prime_list_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, isqrt(n)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00'*(((n-i*i)//i)+1)
    return [k for k in range(2, n+1) if sieve[k]]

def exact_prime(q, trial_primes):
    if q < 2:
        return False
    for d in trial_primes:
        if d*d > q:
            return True
        if q % d == 0:
            return q == d
    return True  # every trial prime up to sqrt(q) has been checked

def exact_point_count(q):
    """Compute a_q exactly in O(q) with no external elliptic algorithms.

    #E(F_q) = q + 1 + sum_x Legendre(4x^3+4x^2-8x+1).
    The cubic is traversed via successive forward differences 0,32,24.
    """
    residues = bytearray(q)
    for y in range(1, (q-1)//2 + 1):
        residues[(y*y) % q] = 1
    f, diff1, diff2 = 1, 0, 32 % q
    character_sum = 0
    for _ in range(q):
        if f:
            character_sum += 1 if residues[f] else -1
        f += diff1
        if f >= q:
            f -= q
        diff1 += diff2
        if diff1 >= q:
            diff1 -= q
        diff2 += 24
        if diff2 >= q:
            diff2 -= q
    return -character_sum, q + 1 + character_sum

def local_row(q, order, p=P):
    assert order % p == 0 and (order // p) % p != 0
    P0, Q0 = rational_generators_mod_q(q)
    R = ec_mul(order//p, P0, q)
    S = ec_mul(order//p, Q0, q)
    assert ec_mul(p, R, q) is None and ec_mul(p, S, q) is None
    if R is None:
        assert S is not None
        return (0, 1)
    curr = None
    for i in range(p):
        if curr == S:
            return (1, i)
        curr = ec_add(curr, R, q)
    raise AssertionError('p-torsion at q is not cyclic; bad auxiliary q')

def verify():
    ap_p, card_p = exact_point_count(P)
    assert ap_p == 0 and card_p == P + 1
    print('P599_SUPERSINGULAR_EXACT_POINTCOUNT_PASS', 'a_599',ap_p, 'cardinality',card_p, flush=True)
    trials = prime_list_upto(isqrt(Q2) + 1)
    rows = []
    for q, want_ap, want_order, want_row in EXPECTED:
        assert exact_prime(q, trials), f'not prime: {q}'
        assert q % P == 1
        a_q, order = exact_point_count(q)
        assert (a_q,order)==(want_ap,want_order),(q,a_q,order)
        assert (a_q - (q + 1)) % P == 0
        assert order // P % P != 0
        print('P599_EXACT_POINT_COUNT_PASS',q,'a_q',a_q,
              'cardinality',order,'cofactor',order//P,flush=True)
        row=local_row(q,order)
        assert row==want_row,(q,row,want_row)
        rows.append(row)
        print('P599_LOCAL_COORDINATE_ROW_PASS',q,list(row),flush=True)
    determinant=(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])%P
    assert determinant==475
    print('P599_LOCAL_MORDELL_WEIL_DETERMINANT_NONZERO_PASS',determinant,flush=True)
    q1,q2=Q1,Q2
    phi=(q1-1)*(q2-1)
    print('P599_AUXILIARY_N',q1*q2,flush=True)
    print('P599_AUXILIARY_PHI_N',phi,flush=True)
    print('P599_AUXILIARY_SYMMETRY_REPS',phi//2,flush=True)
    print('P599_MW_MOD_P_TO_TWO_LOCAL_GROUPS_ISOMORPHISM_PASS',flush=True)
    print('BOUNDARY: no Kurihara nonzero witness; Selmer and Sha[599^infinity] NOT certified.',flush=True)

def search(limit, hits):
    assert 2000 <= limit <= 10**10
    assert 1 <= hits <= 50
    primes = prime_list_upto(isqrt(limit)+1)
    candidates=[]
    examined=0
    for q in range(P+1,limit+1,P):
        if not exact_prime(q,primes):
            continue
        examined+=1
        P0,Q0 = rational_generators_mod_q(q)
        bound=isqrt(4*q)
        k_min=(-bound - 2 + P-1)//P
        k_max=(bound - 2)//P
        for k in range(k_min,k_max+1):
            ap=2+k*P
            order=q+1-ap
            # Fast necessary filter. Both P0 and Q0 must have order dividing
            # the exact cardinality. It is NOT a proof that q is admissible.
            if ec_mul(order,P0,q) is not None:
                continue
            if ec_mul(order,Q0,q) is not None:
                continue
            aq_exact,n_exact=exact_point_count(q)
            if (aq_exact,n_exact)!=(ap,order):
                print('P599_FALSE_CANDIDATE_REJECTED',q,'candidate_ap',ap,'actual_ap',aq_exact,flush=True)
                continue
            if (order//P)%P==0:
                print('P599_LOCAL_CYCLICITY_UNCERTAIN',q,flush=True)
                continue
            row=local_row(q,order)
            candidates.append((q,ap,row))
            print('P599_DISCOVERED_EXACT_PRIME',q,'a_q',ap,'N',order,'row',list(row),flush=True)
            for r, _, other_row in candidates[:-1]:
                det=(other_row[0]*row[1]-other_row[1]*row[0])%P
                if det:
                    print('P599_INDEPENDENT_LOCAL_PAIR',r,q,'det',det,flush=True)
                    print('BOUNDARY: pair does not imply Kurihara nonvanishing.',flush=True)
                    return
            if len(candidates)>=hits:
                print('P599_SEARCH_HIT_LIMIT_REACHED',len(candidates),flush=True)
                return
        if examined % 1000==0:
            print('P599_SEARCH_PROGRESS',q,'primes_checked',examined,'hits',len(candidates),flush=True)
    print('P599_SEARCH_EXHAUSTED',limit,'primes_checked',examined,
          'hits',len(candidates),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--search',action='store_true')
    parser.add_argument('--limit',type=int,default=20000000)
    parser.add_argument('--hits',type=int,default=2)
    args=parser.parse_args()
    if args.search:
        search(args.limit,args.hits)
    else:
        verify()