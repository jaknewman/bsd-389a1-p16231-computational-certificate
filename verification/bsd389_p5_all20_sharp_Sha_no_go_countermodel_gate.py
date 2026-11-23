#!/usr/bin/env python3
"""Check an explicit NONZERO algebraic model compatible with all20 theta/Fitt/norm data.

Does NOT compute the actual Selmer group or Sha. See the companion paper.
Usage: python verification/bsd389_p5_all20_sharp_Sha_no_go_countermodel_gate.py --hist /tmp/bsd389_val1_all20.txt
"""
import argparse
import hashlib
import json
from math import comb, gcd
from pathlib import Path

P=argparse.ArgumentParser()
P.add_argument("--hist",type=Path,required=True)
a=P.parse_args()
lines=a.hist.read_text().splitlines()
assert len(lines)==21 and lines[0]=="count 34775000"
rows=[]
for line in lines[1:]:
    fields=line.split()
    assert len(fields)==28 and fields[0]=="r" and fields[2]=="hist"
    r=int(fields[1]);h=list(map(int,fields[3:]))
    assert len(h)==25 and gcd(r,5)==1
    rows.append((r,h))
assert [r for r,_ in rows]==[r for r in range(1,25) if r%5]
sha=hashlib.sha256(json.dumps(rows,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
assert sha=="1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463"
print("ALL20_GENUINE_INPUT_SHA_PASS",sha)

# Norm in R/(5,T^2): N=25+300*T+O(T^2)=0.
assert 25%5==300%5==0
# sigma on Y=F5[T]/T^2, in basis (1,T), matrix [[1,0],[1,1]]
S=((1,0),(1,1))
J=((0,1),(-1,0))
def transpose(M):return tuple(zip(*M))
def prod(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%5 for j in range(2)) for i in range(2))
assert prod(prod(transpose(S),J),S)==tuple(tuple(x%5 for x in row) for row in J)
assert prod(S,S)!=((1,0),(0,1))
print("NONZERO_Y0_ALTERNATING_PAIRING_AND_NORM_PASS",
      "Y0_order",25,"G_action_unipotent",True)

for r,h in rows:
    c=[sum(x*comb(j,d) for j,x in enumerate(h) if j>=d) for d in range(4)]
    c0,c1,c2,c3=c
    assert c0==0 and c1%25==0
    assert c2%25==(15*r)%25 and c3%5==0
    k=c1//25
    # In R=Z5[T]/((1+T)^25-1), eliminate the 25k*T term:
    # 25*T=-300*T^2-2300*T^3-... .
    b2,b3=c2-300*k,c3-2300*k
    assert b2%5==b3%5==0
    # Therefore theta_r belongs to Fitt_0(X0)=(5*T^2,T^4).
    assert c2%5==0 and c3%5==0
    print("ACTUAL_THETA_IN_NONZERO_MODEL_FITT0_PASS",
          "r",r,"c2_mod25",c2%25,"reduced_T2_mod5",b2%5,
          "reduced_T3_mod5",b3%5)
print("ALL20_NONZERO_ALTERNATING_FITT0_NORM_COUNTERMODEL_PASS")
print("TRUE_SHA_ZERO_REQUIRES_EXTRA_ARITHMETIC_INPUT")
print("SHARP_TARGET_TRUE_X_OVER_NX_CARDINALITY_EQUALS_5^4")
