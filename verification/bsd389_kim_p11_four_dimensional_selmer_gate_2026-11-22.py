#!/usr/bin/env python3
"""Exact 4x4 augmentation-rank test motivated by Kim's 2026 anticyclotomic theorem.

Only toy 11-adic matrices and genuine elementary local p=11 signs are
checked. No actual Selmer action matrix or Gross-theta unit is supplied.
"""
from itertools import combinations, permutations
from math import gcd

P = 11

def rank_mod_p(M, p):
    A = [[x % p for x in row] for row in M]
    n, m = len(A), len(A[0]); r = 0
    for j in range(m):
        pivot = next((i for i in range(r, n) if A[i][j] % p), None)
        if pivot is None: continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][j], -1, p)
        A[r] = [x*inv%p for x in A[r]]
        for i in range(n):
            if i != r and A[i][j] % p:
                k = A[i][j]
                A[i] = [(x-k*y)%p for x,y in zip(A[i],A[r])]
        r += 1
        if r == n: break
    return r

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def det(M):
    n = len(M)
    return sum((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)) *
               __import__('math').prod(M[i][perm[i]] for i in range(n))
               for perm in permutations(range(n)))

def fitt2_at_zero(A):
    return gcd(*[abs(det([[A[i][j] for j in cols] for i in rows]))
                  for rows in combinations(range(4),2) for cols in combinations(range(4),2)])

def toy_matrix(e):
    v = P**e
    return [[0,-v,0,0], [0,0,0,0], [0,0,0,-v], [0,0,0,0]]

def demonstrate():
    for D, split389, split11 in [(-43,-1,+1),(-7,+1,+1)]:
        def chi(D, q):
            d = D % q
            return 0 if d == 0 else (1 if pow(d,(q-1)//2,q)==1 else -1)
        assert (chi(D,389),chi(D,11)) == (split389,split11)
        root_twist = -chi(D,389)
        assert (D==-43 and root_twist==1) or (D==-7 and root_twist==-1)
        print('EXACT_TWIST_SIGN_PASS',D,'chi_D(389)',split389,'chi_D(11)',split11,'root_twist',root_twist)
    for e in (0,1,2):
        N = toy_matrix(e)
        assert matmul(N,matmul(N,N)) == [[0]*4 for _ in range(4)]
        assert fitt2_at_zero(N) == P**(2*e)
        rank = rank_mod_p(N,P)
        assert rank == (2 if e==0 else 0)
        print('ABSTRACT_IWASAWA_RANK_GATE_PASS', 'e',e,'rank_mod11',rank,
              'dim_Sel_mod11',4-rank,'Fitt2_at_augmentation',P**(2*e))
    N=[[0,1,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]]
    assert rank_mod_p(N,P)==2 and fitt2_at_zero(N)==1
    assert matmul(N,matmul(N,matmul(N,N)))==[[0]*4 for _ in range(4)]
    print('ABSTRACT_JORDAN_3_PLUS_1_PASS')
    print('BOUNDARY: REAL_GROSS_THETA_AND_REAL_SELMER_GAMMA_MATRIX_NOT_COMPUTED')

if __name__ == '__main__': demonstrate()
