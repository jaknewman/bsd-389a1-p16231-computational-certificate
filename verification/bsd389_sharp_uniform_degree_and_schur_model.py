#!/usr/bin/env python3
"""Proof-sanity finite-field model for the sharp uniform Kurihara-degree target.

The theorem mu_p=dim Sel(E[p]) comes from Kim under hypotheses;
this program verifies only algebra behind the Schur-complement argument.
The extra Selmer/Sha directions are SYNTHETIC: not actual Sha(389a1).
"""

def mul(A,B,p):
    assert len(A[0])==len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p
             for j in range(len(B[0]))] for i in range(len(A))]

def sub(A,B,p):
    return [[(A[i][j]-B[i][j])%p for j in range(len(A[0]))]
            for i in range(len(A))]

def inv2(A,p):
    d=(A[0][0]*A[1][1]-A[0][1]*A[1][0])%p
    assert d!=0
    v=pow(d,-1,p)
    return [[(v*A[1][1])%p,(-v*A[0][1])%p],
            [(-v*A[1][0])%p,(v*A[0][0])%p]]

def identity(d): return [[1 if i==j else 0 for j in range(d)] for i in range(d)]

def det_nonzero(A,p):
    A=[[v%p for v in row] for row in A]
    n=len(A); assert all(len(row)==n for row in A)
    d=1
    for j in range(n):
        z=next((i for i in range(j,n) if A[i][j]), None)
        if z is None:return 0
        if z!=j:
            A[j],A[z]=A[z],A[j]
            d=-d
        t=A[j][j]
        d=d*t%p
        inv=pow(t,-1,p)
        for i in range(j+1,n):
            f=A[i][j]*inv%p
            A[i]=[(A[i][k]-f*A[j][k])%p for k in range(n)]
    return d%p

PAIRS={
    5: [[1,3],[1,0]],
    7: [[1,3],[1,6]],
    11:[[1,10],[1,7]],
    107:[[1,15],[1,53]]
}
for p,A in PAIRS.items():
    AI=inv2(A,p)
    for s in (0,1,2):
        d=2*s; r=2+d
        B=[[(i+2*j+3)%p for j in range(d)] for i in range(2)]
        C=[[(3*i+j+2)%p for j in range(2)] for i in range(d)]
        D=mul(mul(C,AI,p),B,p) if d else []
        for i in range(d):D[i][i]=(D[i][i]+1)%p
        S=sub(D,mul(mul(C,AI,p),B,p),p) if d else []
        assert S==identity(d)
        M=[(A[i]+B[i]) for i in range(2)]+[(C[i]+D[i]) for i in range(d)]
        assert det_nonzero(M,p)==det_nonzero(A,p)
        # Strict-lift basis: w_j = old generator j minus MW correction A^{-1}B_j.
        for j in range(d):
            mw=[-sum(AI[i][k]*B[k][j] for k in range(2))%p for i in range(2)]
            v=mw+[1 if k==j else 0 for k in range(d)]
            out=[sum(M[i][k]*v[k] for k in range(r))%p for i in range(r)]
            assert out == [0,0]+[1 if i==j else 0 for i in range(d)]
        # Alternating perfect form on a *hypothetical finite* Sha[p] quotient.
        J=[[0]*d for _ in range(d)]
        for j in range(s): J[2*j][2*j+1]=1;J[2*j+1][2*j]=-1%p
        if d:assert det_nonzero(J,p)==1
        print('SHARP_BARRIER_SYNTHETIC_MODEL_PASS',
              'p',p,'extra_symplectic_pairs',s,'mu',r,
              'localization_det',det_nonzero(M,p),
              'strict_kernel_dim',d,'Schur_identity',True)
print('WARNING: FINITE-FIELD MODELS, NOT AN ELLIPTIC SHA COMPUTATION')
print('THEOREM TARGET: mu<=3 FOR ALL LARGE GOOD p WOULD FORCE mu=2 BY PARITY')
