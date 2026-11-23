#!/usr/bin/env python3
"""Exact finite-field prerequisites for the all20 nonzero Sha[5] theorem.

Computes #E(Fq) by quadratic-character sum, separately enumerates affine
points and checks 5-torsion by the elliptic-curve group law; compares rational
MW images. The global implication uses Poitou-Tate, tame inertia and Kummer,
proved in the companion paper; this script does NOT compute true Selmer/Sha.
"""
import argparse, hashlib, json
from math import gcd, comb

def add(P,Q,p):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u and (y+v+1)%p==0: return None
    if x==u:
        den=(2*y+1)%p
        assert den
        w=pow(den,-1,p)
        lam=((3*x*x+2*x-2)*w)%p
        nu=((-x**3-2*x-y)*w)%p
    else:
        w=pow((u-x)%p,-1,p)
        lam=((v-y)*w)%p
        nu=((y*u-v*x)*w)%p
    X=(lam*lam-1-x-u)%p
    Y=(-lam*X-nu-1)%p
    assert (Y*Y+Y-X**3-X**2+2*X)%p==0
    return X,Y

def neg(P,p):
    return None if P is None else (P[0],(-P[1]-1)%p)

def mul(P,n,p):
    assert n>=0
    Z=None
    while n:
        if n&1: Z=add(Z,P,p)
        P=add(P,P,p)
        n>>=1
    return Z

def count_legendre(p):
    s=0
    for x in range(p):
        disc=(1+4*(x*x*x+x*x-2*x))%p
        s+=0 if not disc else (1 if pow(disc,(p-1)//2,p)==1 else -1)
    return p+1+s

def point_and_torsion_count(p):
    ys={}
    for y in range(p): ys.setdefault((y*y+y)%p,[]).append(y)
    n=1; t=1
    for x in range(p):
        for y in ys.get((x*x*x+x*x-2*x)%p,[]):
            n+=1
            if mul((x,y),5,p) is None: t+=1
    return n,t

p=5
for q,n,tor in [(5351,5375,5),(13001,13075,25)]:
    assert count_legendre(q)==n
    count,t=point_and_torsion_count(q)
    assert count==n and t==tor
    print("LOCAL_TWO_INDEPENDENT_COUNTS_PASS",q,"point_count",n,
          "E_Fq_5torsion_count",t,"finite_singular_dim",1 if t==5 else 2,flush=True)

P=lambda q:(q-1,1)
Q=lambda q:(0,q-1)
for q,n in [(5351,5375),(13001,13075)]:
    assert mul(P(q),n,q) is None and mul(Q(q),n,q) is None

# At q1 the 5-Sylow is Z/125; its quotient modulo 5 is detected by
# multiplication by 43*25: Q=-P in the one-dimensional quotient.
U=mul(P(5351),43*25,5351)
V=mul(Q(5351),43*25,5351)
assert U is not None and add(U,V,5351) is None

# At q2 the 5-Sylow is F5^2; projection by the 5-prime-to factor 523
# shows Q=2P, with P nonzero. Thus image(MW/5) at q2 has rank exactly 1.
A=mul(P(13001),523,13001)
B=mul(Q(13001),523,13001)
assert A is not None and add(mul(A,2,13001),neg(B,13001),13001) is None
print("LOCAL_MW_13001_CODIM_ONE_PASS","E_Fq_mod5_dimension",2,
      "rational_MW_local_image_dimension",1,"Q_equals_2P",True)
print("LOCAL_MW_BOTH_PRIMES_RANK2_PASS","q5351_Q_equals_minus_P",True,
      "q13001_Q_equals_2P",True,"minor_mod5",3)

ap=argparse.ArgumentParser()
ap.add_argument("--hist",required=True)
args=ap.parse_args()
L=open(args.hist,encoding="utf8").read().splitlines()
assert L[0].strip()=="count 34775000" and len(L)==21
rows=[]
for line in L[1:]:
    s=line.split()
    assert s[0]=="r" and s[2]=="hist"
    r=int(s[1]); h=[int(x) for x in s[3:]]
    assert len(h)==25 and gcd(r,5)==1
    rows.append((r,h))
    c=[sum(x*comb(i,d) for i,x in enumerate(h) if i>=d) for d in range(4)]
    assert c[0]==0 and c[1]%25==0 and c[2]%25==(15*r)%25 and c[3]%5==0
assert [r for r,h in rows]==[r for r in range(1,25) if r%5]
sha=hashlib.sha256(json.dumps(rows,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
assert sha=="1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463"
print("ALL20_ACTUAL_THETA_SHA_AND_ORDER_THREE_PASS",sha)
print("POITOU_TATE_MATH_THEOREM",
      "base_Sel5_dim_2","relaxed_at_13001_dim_3",
      "G_invariant_Sel5_K_dim_3","new_Sha_K_5_class_nonzero")
print("IF_PRIOR_BH_AND_MW_RANK_STABILITY_ACCEPTED",
      "all20_Sha5_K_order_at_least_25",
      "r_mod5_1_2_at_most_5^20",
      "r_mod5_3_4_at_most_5^32")
print("BOUNDARY_SCRIPT_CHECKS_LOCAL_ARITHMETIC_NOT_GLOBAL_SELmer")
