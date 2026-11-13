#!/usr/bin/env python3
"""Exact 389a1 Mazur--Tate Euler norm and p-bicyclic mixed-jet audit.

Pure Python, no Sage. Imports the already committed complete integer
390-symbol cusp evaluator. Recomputes ALL 1,768 integer Euler
coefficient equalities and the 25/49 exact group-ring coefficients.

A published Selmer theorem (Bullach--Honnor 2026 Th. 1.4) is the
EXTERNAL cohomological input. This script does not compute Sha.
"""
import csv
import json
from math import comb
from pathlib import Path
from bsd389_Mazur_Tate_integral_rank2_two_conductors_20261113 import sym,root
OUT=Path(__file__).resolve().parent
def point_count(q):
    sq={t*t%q for t in range(q)}
    n=1
    for x in range(q):
        d=(1+4*(x*x*x+x*x-2*x))%q
        n+=(1 if d==0 else 2 if d in sq else 0)
    return q+1-n,n

def audit(q,r,p):
    assert q%p==r%p==1 and (q-1)%(p*p) and (r-1)%(p*p)
    n=q*r
    g,h=root(q),root(r)
    Q={a:sym(a,q) for a in range(1,q)}
    R={a:sym(a,r) for a in range(1,r)}
    assert sum(Q.values())==sum(R.values())==0
    lq={pow(g,i,q):i for i in range(q-1)}
    lr={pow(h,j,r):j for j in range(r-1)}
    Pq={a:0 for a in Q};Pr={a:0 for a in R}
    Rq={a:0 for a in Q};Rr={a:0 for a in R}
    C=[[0]*p for _ in range(p)]
    raw=[0]*6
    iq=pow(q,-1,r);ir=pow(r,-1,q)
    for a in range(1,n):
        if a%q==0 or a%r==0:continue
        v=sym(a,n)
        u,t=lq[a%q],lr[a%r]
        C[u%p][t%p]+=v
        for k,w in enumerate((1,u,t,comb(u,2),u*t,comb(t,2))):
            raw[k]+=v*w
        Pq[a%q]+=v;Pr[a%r]+=v
        reg=v-Q[(a*ir)%q]-R[(a*iq)%r]
        Rq[a%q]+=reg;Rr[a%r]+=reg
    assert raw[0]==0 and raw[1]%(q-1)==raw[2]%(r-1)==0
    jet=[raw[3]-(raw[1]//(q-1))*comb(q-1,2),
         raw[4],
         raw[5]-(raw[2]//(r-1))*comb(r-1,2)]
    pjet=[v%p for v in jet]
    assert pjet in ([0,4,0],[0,2,0])
    moments=[0]*6
    for a in range(p):
        for b in range(p):
            for k,w in enumerate((1,a,b,comb(a,2),a*b,comb(b,2))):
                moments[k]+=C[a][b]*w
    assert [z%p for z in moments]==[0,0,0,0,pjet[1],0]
    total=0
    for m,ell,pr,reg,base in ((q,r,Pq,Rq,Q),(r,q,Pr,Rr,R)):
        ap,ecount=point_count(ell)
        assert ecount%p==0 and (ell+1-ap)==ecount
        inv=pow(ell,-1,m)
        for a in range(1,m):
            assert pr[a]==ap*base[a]-base[(a*ell)%m]-base[(a*inv)%m]
            assert reg[a]==ap*base[a]-ell*base[(a*inv)%m]-base[(a*ell)%m]
            total+=2
        assert sum(pr.values())==sum(reg.values())==0
        print('INTEGER_EULER_FACTOR_NORM_ALL_COEFF_PASS',n,'to',m,
              'trace',ap,'#E',ecount,'comparisons',2*(m-1),flush=True)
    with (OUT/f'bsd389_MT_C{p}_C{p}_complete_integer_grid.csv').open('w',newline='') as f:
        wr=csv.writer(f)
        wr.writerow(('x_degree','y_degree','integer_coefficient'))
        wr.writerows((i,j,C[i][j]) for i in range(p) for j in range(p))
    print('BICYCLIC_PURE_MIXED_CLASS_PASS',n,'p',p,'jet',pjet,
          'grid_n',p*p,'group_degree',p*p,flush=True)
    return {'p':p,'n':n,'roots':(g,h),'raw_six_moments':raw,
            'p_bicyclic_jet':pjet,'integer_coefficients':C,
            'euler_norm_comparisons':total}

def main():
    a=audit(41,61,5);b=audit(113,673,7)
    assert a['integer_coefficients']==[
        [12,6,2,-38,18],[-38,2,6,12,18],
        [6,56,-20,-16,-26],[36,-44,-44,36,16],
        [-16,-20,56,6,-26]]
    assert b['integer_coefficients']==[
        [2,-56,-18,-12,80,40,-44],
        [16,114,80,-16,-112,-26,-72],
        [40,-10,-62,92,-62,-10,40],
        [-72,-26,-112,-16,80,114,16],
        [-44,40,80,-12,-18,-56,2],
        [30,46,90,-12,2,-114,-32],
        [-32,-114,2,-12,90,46,30]]
    assert a['euler_norm_comparisons']+b['euler_norm_comparisons']==1768
    print('ALL_EXACT_EULER_NORM_AND_BICYCLIC_MAZUR_TATE_PASS',flush=True)
    print('BOUNDARY: Bullach-Honnor 2026 Selmer theorem is external; '
          'NO integer Sha(Q) annihilator or complex BSD proof',flush=True)
if __name__=='__main__':main()
