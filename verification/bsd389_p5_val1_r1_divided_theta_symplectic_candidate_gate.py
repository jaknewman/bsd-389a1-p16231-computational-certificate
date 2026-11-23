#!/usr/bin/env python3
"""Explicit *candidate* (not actual Sha!) at r=1: (Z/25)^2 with C25 symplectic action.

Runs on original 20 coefficient histograms and checks their frozen SHA256.
Uses exact group ring factorization theta_1=T^2 H(T). The finite module
Y_model=Z_5[C25]/(N,H) is then (Z/25)^2, with
sigma=[[1,10],[1,11]] in basis (1,T), determinant1 and order25.
This matches the known Sha-like alternating and invariant requirements,
but does NOT identify Y_model with true Sha(E/K_1)[5-infinity].
"""
import argparse, hashlib, json
from math import comb

p=argparse.ArgumentParser()
p.add_argument("--hist",required=True)
a=p.parse_args()
lines=open(a.hist,encoding="utf8").read().splitlines()
assert len(lines)==21 and lines[0].strip()=="count 34775000"
rows=[]
for line in lines[1:]:
    s=line.split()
    assert s[0]=="r" and s[2]=="hist"
    rows.append((int(s[1]),[int(x) for x in s[3:]]))
assert [r for r,_ in rows]==[r for r in range(1,25) if r%5]
digest=hashlib.sha256(json.dumps(rows,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
assert digest=="1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463"
h=rows[0][1]
assert h==[-424,9536,-424,3388,5172,-8022,-2658,-1240,-9294,-1588,-1580,-1512,9782,3208,3208,9782,-1512,-1580,-1588,-9294,-1240,-2658,-8022,5172,3388]
c=[sum(h[j]*comb(j,d) for j in range(d,25)) for d in range(26)]
assert c[0]==0 and c[1]%25==0
k=c[1]//25
H=[c[j+2]-k*comb(25,j+2) for j in range(24)]
assert [t%25 for t in H[:4]]==[15,0,11,14]

# Seek rank-two quotient B=(Z/25)[T]/(T^2-a-bT).
# Because reduction of H mod5 has initial T^2, a and b are multiples of5.
inv=pow(H[2],-1,25)
aa=(-H[0]*inv)%25
bb=(-(H[1]+H[3]*aa)*inv)%25
assert (aa,bb)==(10,10)

def dot(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%25
             for j in range(2)] for i in range(2)]

I=[[1,0],[0,1]]
T=[[0,aa],[1,bb]]
S=[[1,aa],[1,bb+1]]
assert dot(T,T)==[[(aa*I[i][j]+bb*T[i][j])%25 for j in range(2)] for i in range(2)]

# Since T^4=0 and N=(25+300*T+2300*T^2+12650*T^3+53130*T^4+...),
# all N terms vanish in the 25-torsion rank-two quotient.
assert dot(dot(T,T),dot(T,T))==[[0,0],[0,0]]
N=[[0,0],[0,0]]
P=I
for _ in range(25):
    N=[[(N[i][j]+P[i][j])%25 for j in range(2)] for i in range(2)]
    P=dot(P,S)
assert N==[[0,0],[0,0]] and P==I

# Evaluate H(T) *exactly* in B (25-torsion, T^4=0).
powers=[I,T,dot(T,T),dot(dot(T,T),T)]
HM=[[sum(H[k]*powers[k][i][j] for k in range(4))%25
    for j in range(2)] for i in range(2)]
assert HM==[[0,0],[0,0]]

# H and N vanish in B, giving a surjection Y_model -> B.
# Independent all20 Smith calculation establishes |Y_model|=25^2,
# so this surjection is an isomorphism.
assert (S[0][0]*S[1][1]-S[0][1]*S[1][0])%25==1
V=I
for j in range(1,26):
    V=dot(V,S)
    if j==5: assert V==[[1,0],[5,1]]
    if j==25: assert V==I
# Perfect alternating pairing x^t J y /25 is preserved iff det(S)=1.
J=[[0,1],[-1,0]]
ST=[[S[j][i] for j in range(2)] for i in range(2)]
assert dot(dot(ST,J),S)==[[v%25 for v in row] for row in J]
# On Y[5]=5B, sigma has mod5 Jordan block length 2: 1 invariant dimension.
assert [[x%5 for x in row] for row in S]==[[1,0],[1,1]]
print("R1_TRUE_HIST_SHA_PASS",digest)
print("R1_EXACT_DIVIDED_THETA_JETS_MOD25_PASS", [x%25 for x in H[:4]])
print("R1_CANDIDATE_GALOIS_SYMPLECTIC_MATRIX_PASS",
      "sigma",S,"order",25,"det_mod25",1,
      "Y_model_ab_group","(Z/25)^2",
      "Y_model_5torsion_G_invariants_dim",1)
print("MODEL_NOT_A_PROOF_OF_ACTUAL_SHA_STRUCTURE")
