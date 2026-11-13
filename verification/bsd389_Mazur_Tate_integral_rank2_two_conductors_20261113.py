#!/usr/bin/env python3
"""Exact prime-independent rank-2 Mazur–Tate jets for E389a1 (no Sage).
Uses committed normalized 390 modular symbols. No global Sha/complex BSD claim.
"""
import json
from pathlib import Path
from math import comb, gcd, lcm
from itertools import combinations
N=389
HERE=Path(__file__).resolve().parent
V=json.loads((HERE/"bsd389_390_integral_manin_vector_20261113.json").read_text())["vector"]
assert len(V)==390
INV=[0]+[pow(x,-1,N) for x in range(1,N)]
def sym(a,n):
    pn,pd,ln,ld=1,0,0,1
    u,v=n,a;res=V[N]
    while v:
        k,u,v=u//v,v,u%v
        x,y=k*ln+pn,k*ld+pd
        det=ln*y-x*ld
        assert abs(det)==1
        c,d=(ld,y) if det==1 else (y,ld)
        c%=N;d%=N
        res+=det*V[d*INV[c]%N if c else N]
        pn,pd,ln,ld=ln,ld,x,y
    assert (ln,ld)==(a,n)
    return res
assert sym(7,389)==-1 and sym(5,389)==-2
def root(q):
    x=q-1;fac=[];d=2
    while d*d<=x:
        if x%d==0:
            fac.append(d)
            while x%d==0:x//=d
        d+=1
    if x>1:fac.append(x)
    return next(g for g in range(2,q) if all(pow(g,(q-1)//f,q)!=1 for f in fac))
def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def index(cols):
    d=0
    for abc in combinations(cols,3):d=gcd(d,abs(det3(*abc)))
    return d
def audit(q,r):
    n=q*r;m=q-1;k=r-1; g=root(q);h=root(r)
    iq={pow(g,i,q):i for i in range(m)}
    ir={pow(h,j,r):j for j in range(k)}
    mq={a:sym(a,q) for a in range(1,q)}
    mr={a:sym(a,r) for a in range(1,r)}
    ivr=pow(r,-1,q);ivq=pow(q,-1,r)
    raw=[0]*6;regular=[0]*6
    for a in range(1,n):
        if a%q==0 or a%r==0:continue
        i,j=iq[a%q],ir[a%r]
        w=[1,i,j,comb(i,2),i*j,comb(j,2)]
        v=sym(a,n)
        for t in range(6):raw[t]+=v*w[t]
        if a<n/2:
            v-=mq[(a*ivr)%q]+mr[(a*ivq)%r]
            assert v==sym(n-a,n)-mq[((n-a)*ivr)%q]-mr[((n-a)*ivq)%r]
            for t in range(6):regular[t]+=v*w[t]
    assert raw[0]==0 and raw[1]%m==0 and raw[2]%k==0
    vraw=[raw[3]-(raw[1]//m)*comb(m,2),raw[4],
          raw[5]-(raw[2]//k)*comb(k,2)]
    d=gcd(m,k)
    raw_order=lcm(m//gcd(m,vraw[0]),d//gcd(d,vraw[1]),k//gcd(k,vraw[2]))
    assert regular[0]==0
    assert regular[1]%(m//2)==0 and regular[2]%(k//2)==0
    c=(regular[1]//(m//2))%2
    assert c==(regular[2]//(k//2))%2
    a=(regular[1]-c*m//2)//m
    b=(regular[2]-c*k//2)//k
    vreg=[regular[3]-a*comb(m,2)-c*comb(m//2,2),
          regular[4]-c*(m//2)*(k//2),
          regular[5]-b*comb(k,2)-c*comb(k//2,2)]
    cols=[[m,0,0],[0,m,0],[0,k,0],[0,0,k],
          [m//2,k//2,0],[0,m//2,k//2],[-m*m//4,m*k//2,-k*k//4]]
    total=index(cols);after=index(cols+[vreg])
    assert total%after==0
    return {"n":n,"roots":[g,h],"raw_sums":raw,"raw_jet":vraw,
        "raw_jet_order":raw_order,"regularized_plus_sums":regular,
        "regularized_plus_jet":vreg,"lattice_order":total,
        "theta_quotient_lattice_index":after,"regularized_plus_jet_order":total//after}
if __name__=="__main__":
    first=audit(41,61);second=audit(113,673)
    assert first["raw_sums"]==[0,280,60,5360,244,950]
    assert first["raw_jet_order"]==30
    assert first["regularized_plus_sums"]==[0,-600,-1440,-9910,-46358,-33000]
    assert first["regularized_plus_jet_order"]==20
    assert second["raw_sums"]==[0,-448,-26208,-23408,-2604992,-9552816]
    assert second["raw_jet_order"]==7
    assert second["regularized_plus_sums"]==[0,-10752,415968,-6832,19186280,147637728]
    assert second["regularized_plus_jet_order"]==7
    for result in (first,second):
        print("BSD389_INTEGRAL_MAZUR_TATE_RANK2_PASS",json.dumps(result,sort_keys=True),flush=True)
    print("BOUNDARY_FINITE_LEVEL_GROUP_RING_NOT_GLOBAL_SHA_ANNULLATOR",flush=True)
