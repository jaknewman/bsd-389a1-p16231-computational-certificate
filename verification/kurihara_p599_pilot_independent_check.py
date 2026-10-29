#!/usr/bin/env python3
"""Differential test for the bounded p599 native kernel, using BSGS and an
independent CF implementation. Synthetic 390-table does NOT certify delta.

  python verification/kurihara_p599_pilot_independent_check.py --native /tmp/k599_pilot \
       --table /path/to/manin_table_p599.txt

The checker also works with an authentic p599 Sage-exported Manin table.
"""
import argparse
import math
import re
import subprocess
from pathlib import Path


def bsgs_setup(g, q):
    m=math.isqrt(q-1)+1
    table={}
    x=1
    for j in range(m):
        table.setdefault(x,j)
        x=x*g%q
    giant=pow(g,-m,q)
    def find(v):
        y=v
        for i in range(m+1):
            j=table.get(y)
            if j is not None:
                k=i*m+j
                if pow(g,k,q)==v:
                    return k%(q-1)
            y=y*giant%q
        raise ValueError('not a discrete logarithm')
    return find


def manin_edge_vector(a,n,p):
    # Convergents of a/n, initialized with infinity -> 0.
    w=[0]*390
    w[389]=1
    pn,pd=1,0
    ln,ld=0,1
    x,y=n,a
    while y:
        quot,x,y=x//y,y,x%y
        nn,nd=quot*ln+pn,quot*ld+pd
        det=ln*nd-nn*ld
        assert det in (-1,1)
        c,d=(ld,nd) if det==1 else (nd,ld)
        index=389 if c%389==0 else d*pow(c,-1,389)%389
        w[index]=(w[index]+det)%p
        pn,pd,ln,ld=ln,ld,nn,nd
    assert (ln,ld)==(a,n)
    return w


def check(native,table,interval):
    nums=list(map(int,table.read_text().split()))
    p,q1,q2=nums[:3]
    assert len(nums)==393 and p==599 and (q1,q2)==(6912461,13963889)
    n=q1*q2;M=nums[3:]
    start,end=interval
    out=subprocess.check_output([str(native),'--table',str(table),'--start',str(start),'--end',str(end)],text=True).splitlines()
    assert len(out)==2 and 'STATUS=PARTIAL_ONLY' in out[0]
    fields=dict(re.findall(r'(\w+)=(\S+)',out[0]))
    w_native=list(map(int,out[1].split()[1:]))
    assert len(w_native)==390
    g1,g2=int(fields['g1']),int(fields['g2'])
    log1=bsgs_setup(g1,q1);log2=bsgs_setup(g2,q2)
    w=[0]*390
    total=0
    for a in range(start,end+1):
        u=a%q1;v=a%q2
        if not u or not v:continue
        weight=(log1(u)%p)*(log2(v)%p)%p
        if not weight:continue
        ed=manin_edge_vector(a,n,p)
        row=sum(x*m for x,m in zip(ed,M))%p
        total=(total+weight*row)%p
        w=[(w_i+weight*e)%p for w_i,e in zip(w,ed)]
    assert w==w_native,(interval,'W390 mismatch')
    assert total==int(fields['contraction']),(interval,'contraction mismatch')
    print('K599_INDEPENDENT_PILOT_INTERVAL_PASS',start,end,'sum',total,'W390',len(w),flush=True)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--native',type=Path,required=True)
    ap.add_argument('--table',type=Path,required=True)
    a=ap.parse_args()
    for interval in [(1,30),(100000,100030),(6912450,6912480),
                     (13963880,13963900),(48262408622200,48262408622235)]:
        check(a.native,a.table,interval)
    print('K599_INDEPENDENT_CRT_BSGS_MANIN_PILOT_PASS 5 intervals',flush=True)
    print('BOUNDARY: finite partial intervals only, not full Kurihara delta.',flush=True)


if __name__=='__main__':
    main()
