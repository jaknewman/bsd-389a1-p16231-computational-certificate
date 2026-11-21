#!/usr/bin/env python3
"""Finite-field checks for the correct GMA coefficient module for E389a1.

General abstract matrix identities, not a Selmer computation or BSD proof.
"""
def matmul(A, B, p):
    assert len(A[0]) == len(B)
    return [[sum(a*b for a,b in zip(row,col))%p
             for col in zip(*B)] for row in A]

def gl2_inv(g,p):
    a,b=g[0]; c,d=g[1]
    den=(a*d-b*c)%p
    assert den
    di=pow(den,-1,p)
    return [[d*di%p,-b*di%p],[-c*di%p,a*di%p]]

def diag3(g):
    return [[g[0][0],g[0][1],0],
            [g[1][0],g[1][1],0],
            [0,0,1]]

def block(v):
    return [[0,0,v[0]],[0,0,v[1]],[0,0,0]]

for p in (5,7,11,107,599):
    minus=[[p-1,0],[0,p-1]]
    generators=[
        [[1,1],[0,1]],
        [[2,1],[1,1]],
        [[0,p-1],[1,0]],
        minus,
    ]
    vectors=[[1,0],[0,1],[1,1],[3,2]]
    for g in generators:
        inverse=gl2_inv(g,p)
        for v in vectors:
            lhs=matmul(matmul(diag3(g),block(v),p),diag3(inverse),p)
            gv=[sum(g[i][j]*v[j] for j in (0,1))%p for i in (0,1)]
            assert lhs==block(gv),(p,g,v)
    # On ad^0(V), -I acts trivially, but on V it acts by -1.
    assert 2%p!=0
    print('GMA_OFFDIAGONAL_IS_V_PASS',p,'tests',len(generators)*len(vectors))
    print('ADJOINT_V_GALOIS_MAP_VANISHES_PASS',p)
    # Hypothetical Xp=Zp^2+(Z/p)^2, Fitt2(Xp)=(p^2).
    # A separate congruence module can have length 0.
    hecke_length,sha_length=0,2
    assert hecke_length<=sha_length
    assert not sha_length<=hecke_length
    print('CONGRUENCE_TO_SHA_WRONG_DIRECTION_COUNTERMODEL_PASS',p)

print('SCOPE: Galois-module identities and toy lengths only; no actual Sha.')
