#!/usr/bin/env python3
"""Optimality of all 18 oriented conductor-53 CM embeddings, exactly.

For q^2-q+2107=0, O_53=Z[q], O_K=Z[(q-27)/53]. Because 53 is
prime, R intersect Q(q) = O_53 iff (q-27)/53 NOT IN R.
This script reads the original stage14 18 embeddings and recomputes
integral coordinate membership in the actual 33 Brandt left orders.
No floating point, Waldspurger constants, Hecke sums or 19-action replay.

Run in the existing Sage-enabled Ubuntu shell:
  python -u verification/chi53_optimal_embedding_one_fraction_criterion.py

NOT YET EXECUTED on the user server.
"""
from sage.all import BrandtModule, ZZ, QQ, matrix, vector
from pathlib import Path
import json

H=Path.home()
s14=json.loads((H/"bsd389_chi53_stage14_orbit19.json").read_text())
assert s14["status"]=="ORBIT_18_PASS"
rows=s14["steps"]
assert len(rows)==18
M=BrandtModule(389,base_ring=QQ)
reps=list(M.right_ideals())
assert len(reps)==33
B=M.quaternion_algebra()

def coords(x,basis):
    bas=matrix(QQ,4,4,lambda i,j: QQ(basis[j].coefficient_tuple()[i]))
    return bas.solve_right(vector(QQ,list(x.coefficient_tuple())))

seen=set()
for k,row in enumerate(rows):
    idx=int(row["index"])
    n=tuple(map(ZZ,row["coefficients"]))
    assert 0<=idx<33 and (idx,n) not in seen
    seen.add((idx,n))
    basis=tuple(reps[idx].left_order().basis())
    assert len(basis)==4
    q=sum((n[j]*basis[j] for j in range(4)),B(0))
    assert q.reduced_trace()==1 and q.reduced_norm()==2107
    assert q*q-q+2107==0
    omega=(q-B(27))/53
    assert omega*omega+omega+1==0
    a=coords(omega,basis)
    denominators=[int(c.denominator()) for c in a]
    assert all(d in (1,53) for d in denominators)
    assert 53 in denominators,("EMBEDDING_NONOPTIMAL",k,idx,list(a))
    print("CHI53_ORIENTED_OPTIMAL_EMBEDDING_PASS",k,
          "BRANDT_CLASS",idx,"MAXIMAL_ORDER_GENERATOR_DENOMS",
          denominators,flush=True)
assert len(seen)==18
print("CHI53_ALL_18_OPTIMAL_EMBEDDINGS_PASS",flush=True)
print("CHI53_INITIAL_GROSS_POINT_CONDUCTOR_EXACTLY_53_PASS",flush=True)
print('BOUNDARY: optimality only; use archived stage22 and stage30 for the remaining arithmetic data.', flush=True)
