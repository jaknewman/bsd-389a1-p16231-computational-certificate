#!/usr/bin/env python3
"""389a1 Kurihara sums using 390 precomputed Gamma_0(389) Manin edges.

Run with Sage-enabled `python`:
  python -u verification/kurihara_manin_390_fast.py --selftest
  python -u verification/kurihara_manin_390_fast.py --p 107 --limit 1000

This is an O(phi(n)*log n) *evaluation speedup*, NOT sublinear extraction.
The implementation deliberately aborts before a full p=107 run.
"""
import argparse, math, time
from sage.all import EllipticCurve, QQ, GF
from sage.libs.eclib.newforms import ECModularSymbol

N=389

def table_390(symbol,p):
    """Edge {gamma infinity -> gamma 0}, indexed by bottom row P1(F_N).

    For c !=0, representatives [[0,-1],[1,t]] with t=d/c,
    so edge 0 -> -1/t. For c=0, representative identity,
    so edge infinity -> 0.  Exact values (mod p).
    """
    def red(r):
        v=QQ(symbol(r)); a=int(v.numerator()); b=int(v.denominator())
        assert b%p, ('nonintegral',r,v)
        return a*pow(b,-1,p)%p
    m0=red(QQ(0))
    vals=[0]*N
    for t in range(N):
        vals[t]=(-m0 if t==0 else (red(QQ(-1)/t)-m0))%p
    infinity=m0
    return vals,infinity

def symbol_by_manin(a,n,p,tab):
    """Unimodular continued fraction path infinity -> a/n, 0<=a<n.

    Consecutive convergents have determinant +-1. A determinant +1
    matrix with columns (u,v) gives edge u -> v; with -1 reverse.
    """
    vals,infty=tab
    assert 0 <= a < n and math.gcd(a,n)==1
    # Pair of consecutive convergents, initialized with infinity.
    prev_num,prev_den=1,0
    last_num,last_den=0,1
    # Start with edge infinity -> 0 (det +1): indexed by (0,1).
    acc=infty
    x,y=a,n
    # CF of 0<a<n: first quotient 0, already accounted for infinity->0.
    q0,x,y=x//y,y,x%y
    assert q0==0
    while y:
        q,x,y=x//y,y,x%y
        new_num=q*last_num+prev_num
        new_den=q*last_den+prev_den
        # edge last -> new, determinant alternates +1,-1.
        det=last_num*new_den-new_num*last_den
        assert det in (-1,1)
        if det == 1:
            c,d=last_den,new_den
            sign=1
        else:
            c,d=new_den,last_den
            sign=-1
        c%=N; d%=N
        edge=infty if c==0 else vals[d*pow(c,-1,N)%N]
        acc=(acc+sign*edge)%p
        prev_num,prev_den=last_num,last_den
        last_num,last_den=new_num,new_den
    assert last_num==a and last_den==n, (a,n,last_num,last_den)
    return acc

def dlog(q,p):
    g=int(GF(q).multiplicative_generator()); tab=bytearray(q)
    x=1
    for k in range(q-1):
        tab[x]=k%p; x=x*g%q
    assert x==1
    return tab,g

def compute(symbol,tab,p,q1,q2,limit,full=False):
    n=q1*q2
    assert ((q1-1)//2)%p==0 and ((q2-1)//2)%p==0
    t1,g1=dlog(q1,p);t2,g2=dlog(q2,p)
    max_a=(n-1)//2; end=max_a if full else min(limit,max_a)
    print('MANIN390_CONFIG',{'p':p,'q1':q1,'q2':q2,'n':n,'limit':end,'primitive_roots':(g1,g2)},flush=True)
    total=0; nonzero=0; tic=time.monotonic()
    for a in range(1,end+1):
        r1=a%q1;r2=a%q2
        if not r1 or not r2:continue
        wt=t1[r1]*t2[r2]%p
        if not wt:continue
        v=symbol_by_manin(a,n,p,tab)
        total=(total+wt*v)%p;nonzero+=1
        if a%100000==0: print('MANIN390_PROGRESS',a,total,round(time.monotonic()-tic,2),flush=True)
    value=2*total%p if full else total
    print('MANIN390_COMPLETE' if full else 'MANIN390_PARTIAL_ONLY',p,q1,q2,value,'nonzero_weights',nonzero,'seconds',round(time.monotonic()-tic,3),flush=True)
    return value

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--selftest',action='store_true')
    ap.add_argument('--p',type=int,default=107)
    ap.add_argument('--q1',type=int,default=369793)
    ap.add_argument('--q2',type=int,default=383917)
    ap.add_argument('--limit',type=int,default=1000)
    args=ap.parse_args()
    E=EllipticCurve(QQ,[0,1,1,-2,0]);symbol=ECModularSymbol(E,sign=1)
    pset=[5,7,107] if args.selftest else [args.p]
    for p in pset:
        tab=table_390(symbol,p)
        for a,n in [(1,5),(1,7),(1,41),(1,673),(1,2501),(1,76049),(1,141969819181),(1234,76049),(987654,141969819181)]:
            if math.gcd(a,n)!=1: continue
            v=QQ(symbol(QQ(a)/n))
            assert int(v.denominator())%p
            direct=int(v.numerator())*pow(int(v.denominator()),-1,p)%p
            fast=symbol_by_manin(a,n,p,tab)
            assert direct==fast,('MANIN390_SYMBOL_MISMATCH',p,a,n,direct,fast)
        print('MANIN390_SYMBOL_SELFTEST_PASS',p,flush=True)
        if args.selftest:
            if p==5:
                value=compute(symbol,tab,5,41,61,0,True)
                assert value==4,('P5_MISMATCH',value)
                print('MANIN390_P5_PASS',value,flush=True)
            elif p==7:
                value=compute(symbol,tab,7,113,673,0,True)
                assert value==2,('P7_MISMATCH',value)
                print('MANIN390_P7_PASS',value,flush=True)
        else:
            # Prevent accidental multi-day job. Limit is always a pilot here.
            value=compute(symbol,tab,p,args.q1,args.q2,args.limit,False)
            if p==107 and args.q1==369793 and args.q2==383917 and args.limit==1000:
                assert value==53, ('P107_PARTIAL_MISMATCH',value)
                print('MANIN390_P107_1000_PASS',flush=True)
if __name__=='__main__':main()