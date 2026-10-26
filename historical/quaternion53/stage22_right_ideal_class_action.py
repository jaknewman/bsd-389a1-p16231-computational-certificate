#!/usr/bin/env python3
"""Stage 22: exact right-ideal realization of 18 CM transports.

The rational right ideals stand for adelic double classes. This certifies
unoriented right-ideal transitions plus K-embeddings, not an unstated oriented
local test-vector comparison with any specific Waldspurger theorem.
Run inside an activated Sage Python environment in /home/bsdadmin.
"""
from pathlib import Path
import json
from sage.all import QQ, ZZ, BrandtModule, sage_eval, matrix

H=Path.home()
D=json.loads((H/'bsd389_chi53_stage14_orbit19.json').read_text())
assert D['status']=='ORBIT_18_PASS'
steps=D['steps']
assert len(steps)==18
M=BrandtModule(389,base_ring=QQ)
reps=list(M.right_ideals())
assert len(reps)==33
B=M.quaternion_algebra()
ii,jj,kk=B.gens()
local={'i':ii,'j':jj,'k':kk}

def quat(s):
    return B(sage_eval(str(s), locals=local))
def emb(idx,c):
    basis=tuple(reps[idx].left_order().basis())
    return sum((ZZ(n)*b for n,b in zip(c,basis)), B(0))

cert=[]
for k,row in enumerate(steps):
    assert int(row['k'])==k
    src=int(row['index']); dst=int(row['next_index'])
    assert src==int(steps[k]['index'])
    assert dst==int(steps[(k+1)%18]['index'])
    q=emb(src,row['coefficients'])
    qnext=emb(dst,row['next_coefficients'])
    I=reps[src]; K=reps[dst]
    R=I.left_order()
    assert q.reduced_trace()==1 and q.reduced_norm()==2107
    assert q in R
    # Elliptic prime ideal (19, theta - 2), transported as left ideal.
    J=R.left_ideal([q-B(2),B(19)])
    Rprime=J.right_order()
    assert Rprime.discriminant()==389
    assert q in Rprime
    def det_basis(basis):
        return matrix(QQ, [list(b.coefficient_tuple()) for b in basis]).det()
    index=abs(det_basis(J.basis())/det_basis(R.basis()))
    assert index==361, ('unexpected ideal index',k,index)
    # Right R0 ideal realization of the Gross action; alpha is a rational
    # left multiplier, which does not change its adelic double class.
    transported=J.conjugate()*I
    alpha=quat(row['witness'])
    assert alpha != 0
    assert alpha*transported==K, ('RIGHT_IDEAL_EQUALITY_FAILURE',k)
    assert alpha*q*alpha.inverse()==qnext, ('EMBEDDING_FAILURE',k)
    # Root-2 prime vs inverse root-18: the inverse transport is verified
    # directly from the actual source and destination ideals.
    Jback=K.left_order().left_ideal([qnext-B(18),B(19)])
    Tback=Jback.conjugate()*K
    back=quat(row['inverse_witness'])
    assert back*Tback==I, ('INVERSE_IDEAL_FAILURE',k)
    assert back*qnext*back.inverse()==q, ('INVERSE_EMBEDDING_FAILURE',k)
    cert.append({'k':k,'source':src,'destination':dst,'alpha':str(alpha),
                 'right_ideal_identity':True,'embedding_identity':True,
                 'inverse_right_ideal_identity':True,
                 'index_J':int(index)})
    print('ADELIC_RIGHT_IDEAL_STEP',k,src,'TO',dst,
          'J_INDEX',index,'FORWARD_EXACT','PASS','INVERSE_EXACT','PASS',flush=True)

assert len(cert)==18
out=H/'bsd389_chi53_stage22_adelic_right_ideals.json'
out.write_text(json.dumps({
    'status':'RIGHT_IDEAL_TRANSPORT_PASS',
    'convention':'right ideals I_i over fixed R0; left ideal J=R_i(q-2)+19R_i; I_next=alpha*conj(J)*I_i',
    'steps':cert,
    'scope':'exact right-ideal double-class and embedding transport; orientation and local test-vector comparison remain separate',
    'waldspurger_identification':'OPEN'},indent=2)+'\n')
print('STAGE22_RIGHT_IDEAL_DOUBLE_CLASS_18_PASS')
print('STAGE22_EMBEDDING_TRANSPORT_18_PASS')
print('STAGE22_INVERSE_TRANSPORT_18_PASS')
print('ADELIC_ORIENTATION_AT_389_OPEN')
print('WALDSPURGER_TEST_VECTOR_OPEN')
print('OUTPUT',out)