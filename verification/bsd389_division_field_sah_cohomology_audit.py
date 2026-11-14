#!/usr/bin/env python3
"""Exact H1(GL2(Fp),standard Fp^2) by 3-generator cocycle relators.

All GL2 matrices (p=5,7,11) and all edges in their right Cayley graphs
are enumerated. 1-cocycle constraints are linear in the six generator
values. Expected Z1=2, B1=2, H1=0; higher H2 is proved by Sah, NOT here.
No arithmetic division-field class group, isogeny Selmer or Sha is computed.
"""
from collections import deque

def mm(A,B,p):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)

def rank_add(v,p,basis):
    v=[x%p for x in v]
    for i,row in sorted(basis.items()):
        if v[i]:
            k=v[i]
            v=[(v[j]-k*row[j])%p for j in range(6)]
    for i,x in enumerate(v):
        if x:
            inv=pow(x,-1,p)
            basis[i]=[(z*inv)%p for z in v]
            return
def root(p):
    fs=[];n=p-1;d=2
    while d*d<=n:
        if n%d==0:
            fs.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:fs.append(n)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//r,p)!=1 for r in fs))
def test(p):
    g=root(p)
    gens=((1,1,0,1),(0,p-1,1,0),(g,0,0,1))
    ident=(1,0,0,1)
    mats=[]
    for k in range(3):
        v=[0]*12;v[2*k]=1;v[6+2*k+1]=1
        mats.append(v)
    def apply(G,F):
        a,b,c,d=G
        return [((a if row==0 else c)*F[j]+(b if row==0 else d)*F[6+j])%p
                for row in range(2) for j in range(6)]
    state={ident:[0]*12}
    pending=deque([ident])
    relators=0;basis={}
    while pending:
        G=pending.popleft()
        for k,H in enumerate(gens):
            J=mm(G,H,p)
            wanted=[(a+b)%p for a,b in zip(state[G],apply(G,mats[k]))]
            if J not in state:
                state[J]=wanted
                pending.append(J)
            else:
                prior=state[J]
                for s in (0,6):
                    rank_add([(wanted[s+j]-prior[s+j])%p for j in range(6)],p,basis)
                    relators+=1
    expected=p*(p-1)**2*(p+1)
    assert len(state)==expected
    assert (len(basis),6-len(basis))==(4,2)
    # For the natural representation, dimension of coboundaries is 2.
    # Hence all cocycles are coboundaries and H1 vanishes.
    print("GL2_H1_EXHAUSTIVE_GENERATOR_RELATIONS_PASS",p,
          "group_order",len(state),"relator_rows",relators,
          "constraint_rank",len(basis),"Z1_dim",2,"B1_dim",2,"H1_dim",0,
          flush=True)
for p in (5,7,11):test(p)
print("SCOPE_NO_GALOIS_FIELD_CLASS_GROUP_SHA_CALCULATION")
