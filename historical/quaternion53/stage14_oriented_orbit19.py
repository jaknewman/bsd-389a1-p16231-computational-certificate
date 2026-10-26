#!/usr/bin/env python3
"""Stage 14: exact 19-neighbour CM orbit, no assumed class permutation.

Run in a Sage-enabled Python environment from the same directory as stage4 JSON.
The output is an audit of oriented embeddings, not yet a Waldspurger certificate.
"""
import json
from pathlib import Path
from sage.all import ZZ, QQ, BrandtModule, matrix, vector

H = Path.home()
raw = json.loads((H/'bsd389_quaternion_53_stage4_fast_candidates.json').read_text())
s10 = json.loads((H/'bsd389_chi53_stage10_local_ideal.json').read_text())
assert raw['completed_orders'] == 33
B = BrandtModule(389, base_ring=QQ)
reps = list(B.right_ideals())
assert len(reps) == 33
Q = B.quaternion_algebra()
allowed = [set(tuple(map(int,v)) for v in item['optimal_coefficients']) for item in raw['orders']]

basis_cache = [tuple(I.left_order().basis()) for I in reps]
coord_cache = [matrix(QQ, 4, 4,
    lambda r,c: QQ(basis_cache[i][c].coefficient_tuple()[r]))
    for i in range(33)]

def embed(i,n):
    return sum((ZZ(a)*b for a,b in zip(n,basis_cache[i])), Q(0))

def coord(i,q):
    w=coord_cache[i].solve_right(vector(QQ,q.coefficient_tuple()))
    assert all(a.denominator()==1 for a in w)
    return tuple(int(a) for a in w)

def step(i,n,root):
    assert root in (2,18)
    q=embed(i,n)
    assert q.reduced_trace()==1 and q.reduced_norm()==2107
    R=reps[i].left_order()
    J=R.left_ideal([q-ZZ(root), Q(19)])
    assert J.right_order().discriminant()==389
    T=J.conjugate()*reps[i]
    matches=[]
    for j,K in enumerate(reps):
        good, alpha=K.is_right_equivalent(T,certificate=True)
        if good:
            assert alpha*T==K
            newq=alpha*q*alpha**(-1)
            assert newq in K.left_order()
            newn=coord(j,newq)
            assert newn in allowed[j], ('not in optimal list',i,j,root,newn)
            matches.append((j,newn,str(alpha)))
    assert len(matches)==1, ('destination not unique',i,n,root,matches)
    return matches[0]

start=(int(s10['order_index']),tuple(map(int,s10['embedding_coefficients'])))
assert start[1] in allowed[start[0]]
output=H/'bsd389_chi53_stage14_orbit19.json'
visited=[]
seen=set()
state=start
for k in range(18):
    if state in seen:
        raise AssertionError(('repeated oriented state before 18',k,state))
    seen.add(state)
    i,n=state
    j,n2,wit=step(i,n,2)
    # The inverse prime must take us back: check as oriented embeddings.
    backj,backn,backwit=step(j,n2,18)
    assert (backj,backn)==state, ('inverse transport fails',k,state,(j,n2),(backj,backn))
    rec={'k':k,'index':i,'coefficients':list(n),'next_index':j,
         'next_coefficients':list(n2),'witness':wit,
         'inverse_witness':backwit}
    visited.append(rec)
    print('ORBIT_STEP',k,'FROM',i,'TO',j,'INVERSE_PASS',flush=True)
    output.write_text(json.dumps({'status':'PARTIAL','steps':visited},indent=2)+'\n')
    state=(j,n2)
print('ORBIT_AFTER_18',state,'START',start,flush=True)
assert state==start, ('not closed after 18',state,start)
assert len(seen)==18
# Distribution as a completely separate arithmetic sanity check.
values=[0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0]
assert len(values)==33
v=[values[r['index']] for r in visited]
A=sum(v[k] for k in range(0,18,3))
Bv=sum(v[k] for k in range(1,18,3))
C=sum(v[k] for k in range(2,18,3))
print('ORBIT_VALUES',v)
print('ORBIT_UNTWISTED_SUM',sum(v))
print('CANDIDATE_TORIC_ABC',A,Bv,C,'DIFFERENCES',A-C,Bv-C,flush=True)
# IMPORTANT: A,B,C are provisional until conventions, orientation, and
# the Waldspurger test vector / local factors are fully audited.
output.write_text(json.dumps({'status':'ORBIT_18_PASS','start':list(start[1]),
     'start_index':start[0],'steps':visited,'values':v,
     'candidate_ABC':[A,Bv,C], 'candidate_differences':[A-C,Bv-C],
     'waldspurger_local_audit':'OPEN'},indent=2)+'\n')
print('STAGE14_ORIENTED_ORBIT_18_PASS')
print('WALDSPURGER_TEST_VECTOR_AUDIT_OPEN')
print('OUTPUT',output)