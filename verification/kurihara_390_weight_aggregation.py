#!/usr/bin/env python3
"""Exact 390-coordinate Manin weight aggregation for the 389a1 Kurihara sum.

Requires Sage's Python and the existing kurihara_manin_390_fast.py in the same directory.
This is a correctness prototype, NOT a sublinear algorithm. For p=107 it
refuses full enumeration. Weight buckets contain the signed occurrences of
unimodular CF edges, each weighted by both auxiliary discrete logarithms.
"""
import argparse, json, math, time, hashlib
from sage.all import EllipticCurve, QQ
from sage.libs.eclib.newforms import ECModularSymbol
from kurihara_manin_390_fast import N, table_390, symbol_by_manin, dlog

def edges(a,n):
    """Yield signed P1(F_389) indices for path infinity -> a/n.

    Index 389 is cusp c=0; 0..388 denotes t=d/c mod 389.
    Algebra exactly mirrors symbol_by_manin in the verified pilot.
    """
    assert 0 < a < n and math.gcd(a,n)==1
    yield N,1  # infinity -> 0
    prev_num,prev_den=1,0
    last_num,last_den=0,1
    x,y=a,n
    q0,x,y=x//y,y,x%y
    assert q0==0
    while y:
        q,x,y=x//y,y,x%y
        new_num=q*last_num+prev_num
        new_den=q*last_den+prev_den
        det=last_num*new_den-new_num*last_den
        assert det in (-1,1)
        if det==1: c,d=last_den,new_den; sg=1
        else: c,d=new_den,last_den; sg=-1
        c%=N; d%=N
        yield (N if c==0 else d*pow(c,-1,N)%N),sg
        prev_num,prev_den=last_num,last_den
        last_num,last_den=new_num,new_den
    assert (last_num,last_den)==(a,n)

def vec_390(tab):
    vals,inf=tab
    assert len(vals)==N
    return [*vals,inf]

def aggregate(p,q1,q2,limit=None,full=False,check_every=0):
    n=q1*q2
    assert q1!=q2 and math.gcd(q1,q2)==1
    assert (q1-1)%(2*p)==0 and (q2-1)%(2*p)==0, 'half-symmetry condition missing'
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    sym=ECModularSymbol(E,sign=1)
    tab=table_390(sym,p)
    M=vec_390(tab)
    l1,g1=dlog(q1,p); l2,g2=dlog(q2,p)
    bound=(n-1)//2
    if full:
        assert p in (5,7), 'Full enumeration restricted to small benchmarks.'
        end=bound
    else:
        assert limit is not None and 1<=limit<=1000000
        end=min(limit,bound)
    W=[0]*(N+1); covered=0; nonzero_weights=0; total_edges=0
    t0=time.monotonic()
    for a in range(1,end+1):
        i=a%q1;j=a%q2
        if not i or not j:continue
        covered+=1
        wt=l1[i]*l2[j]%p
        if not wt:continue
        nonzero_weights+=1
        for idx,sg in edges(a,n):
            W[idx]=(W[idx]+sg*wt)%p
            total_edges+=1
        if check_every and a%check_every==0:
            print('AGGREGATION_PROGRESS',a,flush=True)
    partial=sum(x*y for x,y in zip(M,W))%p
    if full:
        W=[2*w%p for w in W]
        contracted=sum(x*y for x,y in zip(M,W))%p
    else:
        contracted=partial
    # Compare to existing evaluator on exactly the same terms (not independent algebra).
    # This is cheap at these benchmark sizes, and catches edge-index or sign mismatches.
    old_sum=0
    for a in range(1,end+1):
        i=a%q1;j=a%q2
        if i==0 or j==0:continue
        wt=l1[i]*l2[j]%p
        if wt: old_sum=(old_sum+wt*symbol_by_manin(a,n,p,tab))%p
    if full:old_sum=2*old_sum%p
    assert contracted==old_sum,(contracted,old_sum)
    expected={(5,41,61):4,(7,113,673):2,(107,369793,383917):53}
    if (p,q1,q2) in expected and (full or end==1000):
        assert contracted==expected[(p,q1,q2)],'reference mismatch'
    report={'kind':'COMPLETE' if full else 'PARTIAL_ONLY',
        'p':p,'q1':q1,'q2':q2,'n':n,'processed_through_a':end,
        'representatives_full':bound,'covered_units':covered,
        'nonzero_weights':nonzero_weights,'signed_edge_occurrences':total_edges,
        'nonzero_buckets':sum(w!=0 for w in W),'contraction':contracted,
        'direct_manin_reference':old_sum,'primitive_roots':[g1,g2],
        'W_sha256':hashlib.sha256(bytes(W)).hexdigest(),
        'seconds':round(time.monotonic()-t0,3)}
    print('KURIHARA_390_WEIGHT_'+report['kind'],json.dumps(report,sort_keys=True),flush=True)
    return report,W

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--selftest',action='store_true')
    ap.add_argument('--p',type=int,default=107)
    ap.add_argument('--q1',type=int,default=369793)
    ap.add_argument('--q2',type=int,default=383917)
    ap.add_argument('--limit',type=int,default=1000)
    ap.add_argument('--out',help='optional JSON file for the resulting weight vector')
    a=ap.parse_args()
    if a.selftest:
        for p,q1,q2,full in [(5,41,61,True),(7,113,673,True),(107,369793,383917,False)]:
            result,w=aggregate(p,q1,q2,1000,full)
            print('KURIHARA_390_SELFTEST_PASS',p,result['contraction'],flush=True)
    else:
        result,w=aggregate(a.p,a.q1,a.q2,a.limit,False)
        if a.out:
            with open(a.out,'w') as f:json.dump({'report':result,'W':w},f,indent=2)