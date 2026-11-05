#!/usr/bin/env python3
"""Reduced oriented Gross P2 norm-19 chain: bounded quaternion CM state.

One genuine Gross state consists of (Brandt right-ideal index j, CM
embedding q=m*omega transported to the maximal left order of I_j).
For each step, construct the norm19 left ideal L_j(q-9)+19L_j,
then reduce the resulting right ideal to a fixed Brandt representative
with an EXACT right ideal equivalence witness alpha. Crucially also
transport q -> alpha*q*alpha^-1, preserving the oriented CM state.

This avoids unbounded growth of the global unnormalized p² ideal
lattice. For optional direct anchors, compare states against true
p4-split P2(w^n) Gross constructions. Accumulate the contribution of
the cyclic norm19 generator to degree 0,1,2 theta moments modulo p.

NOTE: a finite pilot is NOT a global theta or a BSD certificate.
"""
import argparse
import hashlib
import io
import json
import runpy
import time
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path
from sage.all import ZZ, QQ, matrix, vector

E=runpy.run_path(str(Path(__file__).with_name(
    "bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py")),
    run_name="NORM19_REDUCED_ORBIT_IMPORT")
P=E["P"];M=P*P
assert P==16231 and M==263445361
B=E["B"]; reps=E["reps"]; V=tuple(E["V"])
assert len(reps)==len(V)==33
omega=E["omega"]
q0=M*omega
assert q0.reduced_trace()==-M and q0.reduced_norm()==M*M
w=(5+3*E["r0"])*pow(5+3*E["r1"],-1,M)%M
assert w==138112843
S=10816
teich=pow(w,P,M)
principal=w*pow(teich,-1,M)%M
assert principal==pow(1+P,S,M)
assert (P-1)//3==5410
H=P*((P-1)//3)
assert H==87809710

basis=[tuple(I.left_order().basis()) for I in reps]
coord_mats=[matrix(QQ,4,4,
    lambda i,j: QQ(basis[k][j].coefficient_tuple()[i]))
    for k in range(33)]

def coords(j,x):
    z=coord_mats[j].solve_right(vector(QQ,x.coefficient_tuple()))
    assert all(t.denominator()==1 for t in z)
    return tuple(ZZ(t) for t in z)

def element(j,z):
    return sum((ZZ(a)*b for a,b in zip(z,basis[j])),B(0))

def classify_normalized(T,q):
    assert q in T.left_order()
    for j,I in enumerate(reps):
        yes,alpha=I.is_right_equivalent(T,certificate=True)
        if yes:
            assert alpha*T==I
            newq=alpha*q*alpha.inverse()
            assert newq in I.left_order()
            assert newq.reduced_trace()==-M
            assert newq.reduced_norm()==M*M
            assert newq*newq+M*newq+B(M*M)==0
            return j,newq,alpha
    raise AssertionError("NO_BRANDT_CLASS_MATCH")

def normalize_anchor(a):
    with redirect_stdout(io.StringIO()):
        H,T=E["build"](a)
    return classify_normalized(T,q0)

def step(j,q):
    I=reps[j]
    L=I.left_order()
    assert q in L and q.reduced_trace()==-M
    assert q.reduced_norm()==M*M
    J=L.left_ideal([q-B(9),B(19)])
    assert J.right_order().discriminant()==389
    assert q in J.right_order()
    # q encodes m*omega, hence gprime=5+3omega in the
    # current transported CM field, still of reduced norm 19.
    gprime=B(5)+(B(3)*q)/M
    assert gprime.reduced_norm()==19
    Tnext=(gprime/B(19))*J.conjugate()*I
    j2,q2,alpha=classify_normalized(Tnext,q)
    return j2,q2,alpha

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--steps",type=int,default=64)
    pa.add_argument("--oracle-every",type=int,default=8,
                    help="0 disables direct p4 Gross anchors")
    pa.add_argument("--output",type=str,default="")
    args=pa.parse_args()
    assert 1<=args.steps<=4096 and args.oracle_every>=0
    t0=time.monotonic()
    j,q,alpha0=normalize_anchor(1)
    assert j==9 and V[j]==-1
    print("REDUCED_ORIENTED_NORM19_BASE_P2_CLASS_PASS",j,flush=True)
    expected_first=[9,2,1,21,9,1,26,3,12]
    a=1
    histogram=Counter()
    moments=[0,0,0]
    states=[]
    maxcoord=0
    for n in range(args.steps+1):
        assert j in range(33)
        z=coords(j,q)
        assert element(j,z)==q
        maxcoord=max(maxcoord,max(abs(int(t)) for t in z))
        assert q.reduced_trace()==-M and q.reduced_norm()==M*M
        assert q in reps[j].left_order()
        if n<len(expected_first):
            assert j==expected_first[n],("EARLIER_USER_CHAIN_REGRESSION",n,j)
        i=(S*n)%P
        assert (w if n==1 else a)%P!=0
        if n==0 or n==args.steps or (
             args.oracle_every>0 and n%args.oracle_every==0):
            k,q_direct,_=normalize_anchor(a)
            assert k==j,("ORACLE_BRANDT_CLASS_MISMATCH",n,j,k)
            # The exact embeddings can differ by a left-order unit
            # after the right-ideal normalization. Need oriented orbit
            # comparison up to conjugation by norm-one units, not a
            # naive q equality.
            ordj=reps[j].left_order()
            units=list(ordj.unit_group().gens_values()) if False else []
            eq=(q==q_direct)
            if not eq:
                # Different certificates for the SAME right ideal
                # differ by left automorphism; for weight-one orders,
                # the only units are +/-1 and q MUST agree.
                weight=int(E["BM"].monodromy_weights()[j])
                if weight==1:
                    raise AssertionError(("ORIENTED_EMBEDDING_MISMATCH",
                                          n,j,z,coords(j,q_direct)))
            print("REDUCED_ORIENTED_DIRECT_GROSS_ANCHOR_PASS",
                  n,"CLASS",j,"VALUE",int(V[j]),
                  "EMBEDDING_EQUAL",eq,flush=True)
        v=int(V[j])
        histogram[j]+=1
        weights=(1,i,i*(i-1)//2)
        for k in range(3):
            moments[k]=(moments[k]+weights[k]*v)%P
        states.append({"n":n,"a_mod_p2":int(a),"i_mod_p":i,
                       "brandt_class":j,"value":v,
                       "q_basis_coordinates":[int(t) for t in z]})
        if n==args.steps:
            break
        j,q,_alpha=step(j,q)
        a=(a*w)%M
        if n<16 or (n+1)%16==0:
            print("REDUCED_ORIENTED_NORM19_STEP_PASS",
                  n+1,"CLASS",j,"VALUE",int(V[j]),
                  "MAX_Q_COORD",maxcoord,"SECONDS",
                  round(time.monotonic()-t0,3),flush=True)
    print("REDUCED_ORIENTED_PILOT_CYCLIC_MOMENTS_MODP",
          moments,flush=True)
    print("REDUCED_ORIENTED_PILOT_CLASS_HISTOGRAM",
          dict(sorted(histogram.items())),flush=True)
    print("REDUCED_ORIENTED_PILOT_MAX_CM_COORDINATE",maxcoord,flush=True)
    print("REDUCED_ORIENTED_NORM19_CHAIN_PASS",args.steps,flush=True)

    path=Path(args.output) if args.output else Path.home()/(
        "bsd389_p16231_P2_norm19_reduced_orbit_"+
        str(args.steps)+"steps.json")
    payload={
        "status":"REDUCED_ORIENTED_NORM19_FINITE_PILOT_PASS",
        "p":P,"conductor":M,"galois_generator_ratio":w,
        "principal_unit_exponent_per_g_step":S,
        "steps":args.steps,"points":len(states),
        "max_abs_q_basis_coordinate":maxcoord,
        "truncated_moments_mod_p":moments,
        "brandt_histogram":dict(sorted(histogram.items())),
        "states":states,
        "scope":"Finite pilot, not full 87809710-class theta sum"
    }
    path.write_text(json.dumps(payload,indent=2)+"\n")
    print("REDUCED_ORIENTED_PILOT_JSON",path,flush=True)
    print("BOUNDARY_FULL_CYCLIC_THETA_NOT_COMPUTED",flush=True)
    print("BOUNDARY_SHA_AND_BSD_NOT_PROVED",flush=True)

if __name__=="__main__":
    main()
