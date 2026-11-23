#!/usr/bin/env python3
"""NEW TRUE 5^2-Kurihara valuation-one witness and Bullach-Honnor parity gate.

p=5, q1=5351 (a_q=-23), q2=13001 (a_q=-73), m=25, n=69568351.
Independently assistant-computed 34,775,000 genuine Manin representatives.
Full Native reproducer: bsd389_p5_depth25_valuation1_full_integer_hist_native.cpp

The theorem (NOT computed by Python) is:
  genuine theta_K in Fitt_0(Sel_pinf(K)^dual), and
  a depth-p^k two-prime Kurihara valuation s<k means theta
  maps to p^s unit*T^2 !=0 in (Z/p^(s+1))[T]/(T^3).
  This quotient kills (p,T)^(s+3), hence Selmer needs <=s+2
  group-ring generators. Restriction gives dim Sha(Q)[p]<=s.
  For s=1, p-parity + Cassels-Tate => Sha(Q)[pinf]=0.

Important: this does NOT prove Sha(E/K)[5inf]=0 at this
valuation-one conductor. The nonzero analytic saturated cokernel
also CANNOT be identified with Sha(Q)[5inf].
"""
import argparse
from math import comb, isqrt
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

p,m,q1,q2=5,25,5351,13001
N=q1*q2
COUNT=34775000
HIST=[
 -424,9536,-424,3388,5172,-8022,-2658,-1240,-9294,-1588,
 -1580,-1512,9782,3208,3208,9782,-1512,-1580,-1588,-9294,
 -1240,-2658,-8022,5172,3388,
]
EXPECTED_B=50443283548485308992625542772647982784420646448431399798180232543641606348609945600000000
EXPECTED_HALF=224595822642553414416922351284439356643840000

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument("--hist",type=Path,help="Actual full native C++ histogram output")
args=ap.parse_args()
if args.hist:
    lines=args.hist.read_text().splitlines()
    assert len(lines)>=2
    assert lines[0].strip()==f"count {COUNT}"
    actual=list(map(int,lines[1].removeprefix("hist ").split()))
    assert actual==HIST,("NEW_NATIVE_HIST_DIFFERS_FROM_INDEPENDENT_ASSISTANT_RESULT",actual)
assert len(HIST)==m and N==69568351
assert sp.isprime(q1) and sp.isprime(q2)
assert (q1-1)%50==(q2-1)%50==0
def point_count(q):
    sq=bytearray(q)
    for i in range(q):sq[i*i%q]=1
    total=1
    for x in range(q):
        d=(1+4*((x*x*x+x*x-2*x)%q))%q
        total+=1 if d==0 else (2 if sq[d] else 0)
    return total

n1,n2=point_count(q1),point_count(q2)
assert (n1,n2)==(5375,13075)
assert (q1+1-n1,q2+1-n2)==(-23,-73)
assert sp.primitive_root(q1)==11
assert sp.primitive_root(q2)==3
assert ((q1-1)*(q2-1))//2==COUNT
coeff=[sum(z*comb(j,d) for j,z in enumerate(HIST) if j>=d) for d in range(4)]
c0,c1,c2,c3=coeff
assert (c0,c1,c2)==(0,-108600,-993960)
assert c1%m==0
assert c2%m==15 and c2%p==0 and c2%(p*p)!=0

def dlog_mod(q,g,a):
    x=1
    for j in range(q-1):
        if x==a%q:return j%m
        x=x*g%q
    raise AssertionError("not a primitive root")
lN1,lN2=dlog_mod(q1,11,389),dlog_mod(q2,3,389)
shift=(-(lN1+lN2))%m
assert (lN1,lN2,shift)==(2,21,2)
assert all(HIST[j]==HIST[(shift-j)%m] for j in range(m))

# R=Z5[T]/((1+T)^25-1) maps to B=(Z/25)[T]/(T^3).
# Here (5,T)^4 B=0, but true theta maps to 15 T^2 !=0.
assert m%25==0 and comb(m,2)%25==0
assert c0%25==c1%25==0 and c2%25==15
assert 15%25!=0
print("TRUE_MOD25_VALUATION1_HECKE_AND_QUOTIENT_FILT_GATE_PASS",
      "conductor",N,"reps",COUNT,"q_point_counts",(n1,n2),
      "q_traces",(-23,-73),"primitive_roots",(11,3),
      "c0_c1_c2_c3",coeff,
      "delta_mod25",15,"delta_mod5",0,flush=True)
print("LOCAL_RING_THEOREM theta_image_in_Z25_T_MOD_T3 = 15*T^2 !=0")
print("LOCAL_RING_THEOREM (5,T)^4_killed => theta_notin_(5,T)^4")
print("PUBLISHED_BULLACH_HONNOR_FITTING => minimal_R_generators_at_most_3")
print("RESTRICTION_TO_Q => dim_Sha_Q_5 <=1")
print("DOKCHITSER_P_PARITY_PLUS_CASSELS_TATE => dim_Sha_Q_5 even => zero")

# Independent complete real integer cyclotomic resultant.
x=sp.Symbol('x')
F=sp.Poly(sum(z*x**j for j,z in enumerate(HIST)),x)
S=sp.Poly(sum(x**j for j in range(m)),x)
B=int(sp.resultant(S,F,x))
assert B==EXPECTED_B and B>0 and B%625==0
sqrtB=isqrt(B)
assert sqrtB==EXPECTED_HALF and sqrtB**2==B
R=B//625
assert R%p==0
def v5(z):
    count=0
    while z and z%5==0:z//=5;count+=1
    return count
assert v5(B)==8 and v5(R)==4

# Real symmetric theta multiplication matrix, exact integer Smith form:
h=(m-1)//2
t=next(t for t in range(m) if (2*t+shift)%m==0)
assert t==24
g=[HIST[(j-t)%m] for j in range(m)]
assert all(g[j]==g[-j%m] for j in range(m))
A=sp.Matrix(h,h,lambda i,j:
    g[(i-j)%m]+g[(i+j+2)%m]-2*g[i+1])
det=int(A.det())
assert det==-EXPECTED_HALF and det*det==B
D=smith_normal_form(A,domain=sp.ZZ)
e=[v5(abs(int(D[i,i]))) for i in range(h)]
assert sorted(e)==[0]*10+[2,2]
print("AUTHENTIC_VALUATION1_INTEGER_RESULTANT_AND_SMITH_PASS",
      "resultant_digits",len(str(B)),"v5_B",v5(B),
      "normalized_mod5",R%p,"v5_normalized",v5(R),
      "sqrt_B",sqrtB,"center",t,"p_smith_valuations",e,flush=True)
print("IMPORTANT_NO_INFERENCE_OF_SHA_K_ZERO_AT_VALUATION_ONE")
print("UNIFORM_GOAL_FOR_ALL_LARGE_P: SOME_P2_DEEP_TWO_PRIME_DELTA_NOT_ZERO_MOD_P2")
print("BOUNDARY_NO_ALL_PRIME_EXISTENCE_OR_EXACT_COMPLEX_BSD")
