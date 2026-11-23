#!/usr/bin/env python3
"""Exact all20 divided-theta Fitting model -- NOT a computation of true Sha.

Let R=Z_5[C25], T=sigma-1, N=sum_g g. Genuine theta=F_r(sigma)
has c0=0 and c1 divisible by25. In R it factors theta=T^2 H.
For the explicit *candidate* X=R/(T)^2 (+) Y with Y=R/(N,H),
Fitt0(X)=(theta), norm kills Y, rank quotient is 2, and
#Y=5^(v5(Res(theta,N))-4). This is an algebraic model satisfying
more than the known Fitting containment, NOT proof that true X=the model.

Run: python verification/bsd389_p5_all20_theta_divided_T2_candidate_Sha_smith_gate.py --hist /tmp/bsd389_val1_all20.txt
"""
import argparse
import hashlib
import json
from math import comb, gcd
from pathlib import Path

def smith_valuations_mod_p(data,p=5,precision=8):
    a=[list(row) for row in data]
    n=len(a)
    mod=p**precision
    a=[[z%mod for z in row] for row in a]
    def val(z):
        if not z%mod:return precision
        v=0
        while not z%p:v+=1;z//=p
        return v
    vals=[]
    for k in range(n):
        v,i,j=min((val(a[i][j]),i,j) for i in range(k,n) for j in range(k,n))
        assert v<precision, ("matrix not proven finite at precision",precision,k)
        a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        pp=p**v; m=mod//pp
        inv=pow((a[k][k]//pp)%m,-1,m)
        for i in range(k+1,n):
            assert a[i][k]%pp==0
            f=(a[i][k]//pp*inv)%m
            for j in range(k,n):a[i][j]=(a[i][j]-f*a[k][j])%mod
            assert a[i][k]==0
        for j in range(k+1,n):
            assert a[k][j]%pp==0
            f=(a[k][j]//pp*inv)%m
            for i in range(k,n):a[i][j]=(a[i][j]-f*a[i][k])%mod
            assert a[k][j]==0
        vals.append(v)
    return sorted(vals)

def multiplication_matrix25quotient(coeff):
    assert len(coeff)==25
    return [[coeff[(i-j)%25]-coeff[(24-j)%25] for j in range(24)]
            for i in range(24)]

def divided_theta(r,hist):
    assert len(hist)==25 and sum(hist)==0
    c=[sum(x*comb(j,d) for j,x in enumerate(hist) if j>=d)
       for d in range(26)]
    assert c[0]==0 and c[1]%25==0
    k=c[1]//25
    h_t=[c[j+2]-k*comb(25,j+2) for j in range(24)]
    # Exact identity in Z[T], not a numerical division:
    # F(1+T) - T^2 H(T) = k*((1+T)^25 - 1).
    lhs=[c[j]-(h_t[j-2] if 2<=j<=25 else 0)
         for j in range(26)]
    rhs=[k*comb(25,j) if j else 0 for j in range(26)]
    assert lhs==rhs
    # H(T) -> H(X-1) (coefficient at X^24 is 0)
    h_x=[sum(h_t[j]*comb(j,i)*(-1)**(j-i)
             for j in range(i,24)) for i in range(24)]+[0]
    smith_theta=smith_valuations_mod_p(multiplication_matrix25quotient(hist))
    smith_h=smith_valuations_mod_p(multiplication_matrix25quotient(h_x))
    a=sum(smith_theta)
    assert a in (8,12) and sum(smith_h)==a-4
    assert a==(8 if r%5 in (1,2) else 12)
    # Norm(T) on Z5[X]/(N) is N(1)=25, so Norm(T^2) has v5=4.
    assert sum(smith_theta)-sum(smith_h)==4
    print("EXACT_T2_DIVISIBILITY_IN_REAL_GROUP_RING_PASS","r",r,
          "theta_resultant_v5",a,"divided_theta_resultant_v5",sum(smith_h),
          "candidate_Y_elementary_divisors",
          [5**v for v in smith_h if v],flush=True)
    return a,smith_h

p=argparse.ArgumentParser()
p.add_argument("--hist",type=Path,required=True)
args=p.parse_args()
lines=args.hist.read_text(encoding="utf-8").splitlines()
assert lines[0].strip()=="count 34775000" and len(lines)==21
rows=[]
for line in lines[1:]:
    s=line.split()
    assert s[0]=="r" and s[2]=="hist"
    r=int(s[1]);hist=list(map(int,s[3:]))
    assert 1<=r<=24 and gcd(r,5)==1 and len(hist)==25
    rows.append((r,hist))
assert [r for r,_ in rows]==[r for r in range(1,25) if r%5]
digest=hashlib.sha256(json.dumps(rows,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
assert digest=="1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463"
print("GENUINE_ALL20_HISTOGRAM_SHA_PASS",digest,flush=True)
groups={4:0,8:0}
for r,hist in rows:
    a,sm=divided_theta(r,hist)
    groups[a-4]+=1
assert groups=={4:10,8:10}
print("ALL20_EXACT_DIVIDED_THETA_FINITE_CANDIDATE_PASS",groups)
print("RELATIVE_BSD_5ADIC_SHA_ORDER_PREDICTION_IF_BSD_BOTH_FIELDS",
      "r_mod5_1_2: 5^4","r_mod5_3_4: 5^8")
print("NO_PROOF_TRUE_SHA_EQUALS_CANDIDATE_Y_OR_BSD")
