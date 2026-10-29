#!/usr/bin/env python3
"""Independent differential audit of the unmodified K107 native executable.

Compares native 390-vector AND contraction to Sage's own convergents and
modular symbols on deterministic, distributed short intervals. Not a full
recomputation of the 710 production chunks.
"""
import argparse, hashlib, math, random, re, subprocess
from pathlib import Path
from sage.all import QQ, EllipticCurve, GF, continued_fraction

P,Q1,Q2,N = 107,369793,383917,389
MOD=Q1*Q2
HALF=(MOD-1)//2

def reduce_q(x):
    x=QQ(x)
    a,b=int(x.numerator()),int(x.denominator())
    assert b % P
    return a*pow(b,-1,P)%P

def log_table(q):
    g=int(GF(q).multiplicative_generator())
    out=bytearray(q)
    k=1
    for i in range(q-1):
        out[k]=i%P
        k=k*g%q
    assert k==1
    return out,g

def edge_vector(a, weight):
    w=[0]*390
    w[389]=weight
    conv=[(int(v.numerator()),int(v.denominator())) for v in continued_fraction(QQ(a)/MOD).convergents()]
    assert conv[0]==(0,1) and conv[-1]==(a,MOD)
    for (u,v),(x,y) in zip(conv,conv[1:]):
        det=u*y-x*v
        assert abs(det)==1
        sign,c,d=(1,v,y) if det==1 else (-1,y,v)
        c%=N;d%=N
        idx=389 if c==0 else d*pow(c,-1,N)%N
        w[idx]=(w[idx]+sign*weight)%P
    return w

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--table',required=True)
    ap.add_argument('--native',required=True)
    ap.add_argument('--intervals',type=int,default=24)
    ap.add_argument('--width',type=int,default=13)
    args=ap.parse_args()
    raw=Path(args.table).read_bytes()
    nums=list(map(int,raw.split()))
    assert nums[:3]==[P,Q1,Q2] and len(nums)==393
    M=nums[3:]
    assert all(0<=z<P for z in M)
    e=EllipticCurve(QQ,[0,1,1,-2,0])
    symbol=e.modular_symbol(sign=1,implementation='sage',normalize='L_ratio')
    L1,g1=log_table(Q1); L2,g2=log_table(Q2)
    rng=random.Random(3891072026)
    first=[1,1000,2_000_000,100_000_000,100_000_001,11_400_000_001,HALF-args.width+1]
    starts=first+[rng.randrange(1,HALF-args.width+2) for _ in range(args.intervals)]
    starts=sorted(set(starts))
    for j,start in enumerate(starts,1):
        end=start+args.width-1
        proc=subprocess.run([args.native,'--table',args.table,'--start',str(start),'--end',str(end)],
                            check=True,capture_output=True,text=True)
        lines=proc.stdout.splitlines()
        assert len(lines)==2 and lines[0].startswith('K107_NATIVE_CHUNK ')
        assert 'contraction=' in lines[0]
        native=int(re.search(r'\bcontraction=(\d+)',lines[0]).group(1))
        Wnative=list(map(int,lines[1].split()[1:]))
        assert len(Wnative)==390
        W=[0]*390
        reference=0
        checked=0
        for a in range(start,end+1):
            if a%Q1==0 or a%Q2==0:continue
            wt=L1[a%Q1]*L2[a%Q2]%P
            if not wt:continue
            checked+=1
            piece=edge_vector(a,wt)
            W=[(x+y)%P for x,y in zip(W,piece)]
            reference=(reference+wt*reduce_q(symbol(QQ(a)/MOD)))%P
        assert W==Wnative, ('W390_MISMATCH',start,end)
        assert reference==native, ('SAGE_MISMATCH',start,end,reference,native)
        assert sum(x*y for x,y in zip(W,M))%P==reference
        print('K107_END_TO_END_INTERVAL_PASS',j,len(starts),start,end,'residue',reference,'weighted',checked,flush=True)
    print('K107_END_TO_END_DISTRIBUTED_AUDIT_PASS',len(starts),'width',args.width,flush=True)
    print('BOUNDARY: differential testing is not universal proof of C++ correctness',flush=True)
if __name__=='__main__':main()