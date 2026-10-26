#!/usr/bin/env python3
"""Independent exact-integer/rational audit of source Manin export.

Checks all 390 cusp-divisor identities (2012 terms), 389+1
projective keys, all determinant-one Gamma0(N) relation matrices,
exact oriented continued-fraction cusps and source-derived exceptional
Shapiro paths 38 and 67. No Sage, eclib, C++ or V19 state.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import hashlib
import json

N,P=389,16231
P2=P*P
P3=P2*P
TOTAL=P*(P-1)
SHA="9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/"historical/originals/bsd389_tame_relation_export_p16231.json"

def mul(x,y):
    return (x[0]*y[0]+x[1]*y[2],x[0]*y[1]+x[1]*y[3],
            x[2]*y[0]+x[3]*y[2],x[2]*y[1]+x[3]*y[3])

def det(x):return x[0]*x[3]-x[1]*x[2]
def inv(x):
    assert det(x)==1
    return (x[3],-x[1],-x[2],x[0])

def cusp(a,b):return "INFINITY" if b==0 else Fraction(a,b)

def divisor(x):
    c=Counter()
    c[cusp(x[0],x[2])]+=1
    c[cusp(x[1],x[3])]-=1
    return Counter({k:v for k,v in c.items() if v})

def pkey(x,n):
    c,d=x[2]%n,x[3]%n
    return (c*pow(d,-1,n))%n if d else n

def shapiro_index(x):
    assert x[2]%N==0
    d=x[3]%P
    return x[2]*pow(N*d,-1,P)%P if d else P

def representative(j,rinf):
    return (1,0,N*j,1) if j<P else rinf

def fragments(x):
    r,s=x,P2
    h2,h1=0,1
    k2,k1=1,0
    out=[]
    while s:
        q,rr=divmod(r,s)
        h,k=q*h1+h2,q*k1+k2
        out.append((h,k))
        h2,h1=h1,h
        k2,k1=k1,k
        r,s=s,rr
    assert out and out[-1][0]*P2==out[-1][1]*x
    matrices=[(1,out[0][0],0,out[0][1])]
    for j in range(len(out)-1):
        sign=-1 if j%2==0 else 1
        matrices.append((sign*out[j][0],out[j+1][0],
                         sign*out[j][1],out[j+1][1]))
    return matrices

def audit_cusps(data):
    reps=data["reps"]
    assert len(reps)==390 and len(data["generators"])==67
    counts={"generators":0,"nongenerators":0,"terms":0}
    observed_generators=set()
    keys=set()
    for i,row in enumerate(reps):
        mat=tuple(row["matrix"])
        assert det(mat)==1
        key=pkey(mat,N)
        assert key not in keys
        keys.add(key)
        assert data["key_to_rep"][str(key)]==i
        if row["generator"]>=0:
            counts["generators"]+=1
            observed_generators.add(row["generator"])
        else:counts["nongenerators"]+=1
        discrepancy=Counter(divisor(mat))
        for t in row["relations"]:
            A=tuple(t["A"])
            assert det(A)==1 and A[2]%N==0
            assert t["coeff"] in (-1,1)
            assert reps[t["r"]]["generator"]>=0
            translated=mul(inv(A),tuple(reps[t["r"]]["matrix"]))
            for point,v in divisor(translated).items():
                discrepancy[point]-=t["coeff"]*v
            counts["terms"]+=1
        assert all(x==0 for x in discrepancy.values()),("cusp mismatch",i,discrepancy)
    assert len(keys)==390 and keys==set(range(N+1))
    assert observed_generators==set(range(67))
    assert counts=={"generators":67,"nongenerators":323,"terms":2012}
    print("EXACT_MANIN_390_CUSP_DIVISOR_IDENTITIES_PASS",flush=True)
    print("EXACT_MANIN_2012_TERMS_DET_ONE_PASS",flush=True)
    return keys

def audit_pair(id,data,keymap,rinf):
    a,b=1+id//P,id%P
    x=a+P*b
    frags=fragments(x)
    cusp_diff=Counter()
    tally={"gen":0,"rel":0,"e0":0,"e1":0}
    for f in frags:
        assert det(f)==1
        for point,n in divisor(f).items():cusp_diff[point]+=n
        R=data["reps"][keymap[pkey(f,N)]]
        H=mul(f,inv(tuple(R["matrix"])))
        assert H[2]%N==0
        j0=shapiro_index(H)
        h=mul(H,inv(representative(j0,rinf)))
        assert det(h)==1 and h[2]%(N*P)==0
        if j0==P:tally["e0"]+=1
        if R["generator"]>=0:tally["gen"]+=1
        else:
            tally["rel"]+=1
            for t in R["relations"]:
                X=mul(representative(j0,rinf),inv(tuple(t["A"])))
                assert X[2]%N==0
                j1=shapiro_index(X)
                inner=mul(X,inv(representative(j1,rinf)))
                assert det(inner)==1 and inner[2]%(N*P)==0
                if j1==P:tally["e1"]+=1
    wanted=Counter({"INFINITY":1,Fraction(x,P2):-1})
    wanted=Counter({k:v for k,v in wanted.items() if v})
    assert all(cusp_diff[k]==wanted[k] for k in cusp_diff|wanted)
    print("EXACT_EXCEPTIONAL_PAIR_TRANSPORT_PASS",id,tally,flush=True)
    return tally

def main():
    payload=FILE.read_bytes()
    assert hashlib.sha256(payload).hexdigest()==SHA
    data=json.loads(payload)
    assert (data["N"],data["p"])==(N,P)
    audit_cusps(data)
    rinf=tuple(data["rinf"])
    assert det(rinf)==1 and rinf[2]%N==0 and rinf[3]%P==0
    keymap={pkey(tuple(r["matrix"]),N):i for i,r in enumerate(data["reps"])}
    result={id:audit_pair(id,data,keymap,rinf) for id in
            (0,38,67,P+3,TOTAL//2,TOTAL-1)}
    assert result[38]["e1"]==1
    assert result[67]["e0"]==1 and result[67]["e1"]==66
    print("EXACT_SHAPIRO_E0_E1_BRANCHES_PASS",flush=True)
    print("EXACT_C01_MANIN_SHAPIRO_ORIENTATION_AUDIT_PASS",flush=True)
    print("BOUNDARY: independent exact algebra, not a Sage n3 numerical oracle",flush=True)

if __name__=="__main__":
    main()
