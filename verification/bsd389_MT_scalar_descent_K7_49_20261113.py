#!/usr/bin/env python3
"""Rigorous exact 7-adic scalar-ideal calculation from actual K7 Mazur-Tate theta.

Uses the previously committed full 390-symbol generator and exact K7
49-coefficient builder.  Sha(K7) deduction additionally invokes the
published Bullach--Honnor Thm 1.4 and the prior Sha(Q)[7inf]=0 certificate.
Does NOT compute a Selmer group directly or prove rank-two complex BSD.
Requires sympy only for independent cyclotomic resultants.
"""
from collections import Counter
from sympy import Symbol,Poly,resultant
from bsd389_MT_Euler_norm_bicyclic_20261113 import audit

P=7;K=12
C=audit(113,673,P)['integer_coefficients']
n=49;mod=P**K

def norm_of_character(a,b):
    Z=Symbol('Z')
    d=[sum(C[i][j] for i in range(P) for j in range(P)
           if (a*i+b*j)%P==t) for t in range(P)]
    return int(resultant(Poly(sum(d[t]*Z**t for t in range(P)),Z),
                         Poly(sum(Z**t for t in range(P)),Z),Z))

norms=[norm_of_character(a,b) for a,b in
       ([(1,t) for t in range(P)]+[(0,1)])]
assert all(x for x in norms)
def v(x):
    if not x:return K
    s=0
    while x%P==0:x//=P;s+=1
    return s
assert sorted(map(v,norms))==[2]*6+[4]*2
assert sum(map(v,norms))==20
print('P7_ALL_CHARACTER_RESULTANTS_NONZERO_PASS',norms,flush=True)

A=[[C[(i//P-j//P)%P][(i%P-j%P)%P]%mod if j<n else 1
    for j in range(n+1)] for i in range(n)]
Orig=[row[:] for row in A]
V=[[int(i==j) for j in range(n+1)] for i in range(n+1)]
rhs=[49]+[0]*(n-1)
vals=[]

for i in range(n):
    e,r,c=min((v(A[r][j]),r,j) for r in range(i,n)
              for j in range(i,n+1))
    assert e<K
    if r!=i:
        A[i],A[r]=A[r],A[i]
        rhs[i],rhs[r]=rhs[r],rhs[i]
    if c!=i:
        for row in A:row[i],row[c]=row[c],row[i]
        for row in V:row[i],row[c]=row[c],row[i]
    assert v(A[i][i])==e
    u=pow(A[i][i]//P**e,-1,mod//P**e)
    for j in range(i+1,n+1):
        a=A[i][j]
        assert a%P**e==0
        t=(a//P**e)*u%(mod//P**e)
        if t:
            for row in A[i:]:row[j]=(row[j]-t*row[i])%mod
            for row in V:row[j]=(row[j]-t*row[i])%mod
    for j in range(i+1,n):
        a=A[j][i]
        assert a%P**e==0
        t=(a//P**e)*u%(mod//P**e)
        if t:
            for z in range(i,n+1):A[j][z]=(A[j][z]-t*A[i][z])%mod
            rhs[j]=(rhs[j]-t*rhs[i])%mod
    assert all(A[i][j]==0 for j in range(i+1,n+1))
    assert all(A[j][i]==0 for j in range(i+1,n))
    vals.append(e)

assert Counter(vals)=={0:36,1:6,2:7}
assert sum(vals)==20
z=[0]*(n+1)
for i,e in enumerate(vals):
    assert rhs[i]%P**e==0
    z[i]=(rhs[i]//P**e)*pow(A[i][i]//P**e,-1,mod//P**e)%(mod//P**e)
x=[sum(V[i][j]*z[j] for j in range(n+1))%mod for i in range(n+1)]
assert all((sum(Orig[i][j]*x[j] for j in range(n+1))-
            (49 if i==0 else 0))%mod==0 for i in range(n))
assert x[-1]==1
# Independent direct multiplication in group ring using actual theta C
for i in range(P):
    for j in range(P):
        actual=(sum(C[a][b]*x[((i-a)%P)*P+((j-b)%P)]
                    for a in range(P) for b in range(P))+x[-1])%mod
        assert actual==(49 if i==j==0 else 0)
print('P7_EXACT_DVR_SMITH_PASS',dict(sorted(Counter(vals).items())),flush=True)
print('P7_DIRECT_GROUPRING_BEZOUT_PASS','precision',K,
      'modulus',mod,'coefficient_count',len(x),'norm_coefficient',x[-1],
      flush=True)
print('THEOREM_SCALAR_CONTRACTION','(theta,N)capZ7=49 Z7',flush=True)
print('ARITHMETIC_COROLLARY_WITH_BULLACH_HONNOR_AND_SHA_Q_7_ZERO',
      '49 Sha(E/K7)[7inf]=0',flush=True)
print('BOUNDARY_NO_Sha(K7)_TRIVIALITY_NO_UNIFORM_SHA(Q)_NO_COMPLEX_BSD',flush=True)
