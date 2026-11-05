#!/usr/bin/env python3
"""Test universal conductor-p² norm19 Gross transport at independent anchors.

The algebraic identity to be confirmed for any unit a mod m=p²:

 (g/19) * conjugate(L(a).left_ideal([m*omega-9,19])) * T(a)
      = T(w*a),   w=(5+3*r0)/(5+3*r1) mod m.

Analogously for gbar=2-3omega, root4 and w^-1. Both identities
were already Sage-verified for a=1 on user's Ubuntu.

This program checks diverse nontrivial a (principal units and
Teichmuller components) and then iterates forward from T(1),
comparing every output to the directly reconstructed Gross ideal.

Strict rational quaternion ideal equality is required at each step,
not just coincidence of the 33-class Brandt label.
"""
import argparse
import contextlib
import io
import json
import runpy
import time
from pathlib import Path
from sage.all import QQ, ZZ, matrix

ENV=runpy.run_path(
    str(Path(__file__).with_name(
        "bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py")),
    run_name="NORM19_GENERAL_IMPORT"
)
P=ENV["P"]
M=P*P
B=ENV["B"]
omega=ENV["omega"]
reps=ENV["reps"]
V=ENV["V"]
base=ENV["base"]
assert P==16231 and M==263445361 and len(reps)==33

g=B(5)+3*omega
gc=B(2)-3*omega
assert g*gc==B(19)
assert g.reduced_norm()==19 and gc.reduced_norm()==19
w=(5+3*ENV["r0"])*pow(5+3*ENV["r1"],-1,M)%M
wi=pow(w,-1,M)
assert w==138112843 and wi==56004792
q=M*omega
assert q*q+M*q+B(M*M)==0
assert M%19==6
assert (M*11)%19==9 and (M*7)%19==4

def det_rows(basis):
    return matrix(QQ,[list(z.coefficient_tuple()) for z in basis]).det()

def get_T(a, cache):
    a=int(a)%M
    assert a%P
    if a not in cache:
        with contextlib.redirect_stdout(io.StringIO()):
            H,T=ENV["build"](a)
        cache[a]=T
    return cache[a]

def neighbor(T, conjugated=False):
    L=T.left_order()
    assert q in L and L.discriminant()==389
    root=4 if conjugated else 9
    el=gc if conjugated else g
    J=L.left_ideal([q-B(root),B(19)])
    assert J.right_order().discriminant()==389
    assert q in J.right_order()
    index=abs(det_rows(J.basis())/det_rows(L.basis()))
    assert index==361,("NORM19_INDEX_NOT_361",index)
    ans=(el/B(19))*J.conjugate()*T
    assert ans.right_order()==T.right_order()
    return ans

def classify(T):
    for j,I in enumerate(reps):
        ok,alpha=I.is_right_equivalent(T,certificate=True)
        if ok:
            assert alpha*T==I
            return j,int(V[j])
    raise AssertionError("NO_BRANDT_MATCH")

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--steps",type=int,default=8,
                     help="forward 19-neighbor iterations with independent Gross anchors")
    args=cli.parse_args()
    assert 1<=args.steps<=32
    begin=time.monotonic()
    cache={}
    # a=1 has already been certified in both directions.
    # Here test genuinely different p-adic units and Teich representatives.
    seeds=[1+P,1+2*P,pow(2,P,M),pow(3264,P,M),w]
    assert len(set(seeds))==5 and all(z%P for z in seeds)
    for a in seeds:
        src=get_T(a,cache)
        dst=get_T(w*a,cache)
        inv=get_T(wi*a,cache)
        assert neighbor(src)==dst,("NORM19_FORWARD_FAILED",a)
        assert neighbor(src,True)==inv,("NORM19_INVERSE_FAILED",a)
        j0,v0=classify(src)
        j1,v1=classify(dst)
        j2,v2=classify(inv)
        print("P2_NORM19_GENERAL_ANCHOR_BOTH_STRICT_IDENTITIES_PASS",
              "A",a,"CLASS",j0,"VALUE",v0,
              "FORWARD_CLASS",j1,"FORWARD_VALUE",v1,
              "INVERSE_CLASS",j2,"INVERSE_VALUE",v2,
              flush=True)
    print("P2_NORM19_NONTRIVIAL_ANCHORS_PASS",len(seeds),flush=True)

    # Now start at the true P2(a=1) lattice and generate successors
    # ONLY through the global quaternionic norm19 neighbor formula.
    # Direct P2 reconstruction is used solely as an independent oracle.
    T=get_T(1,cache)
    a=1
    for i in range(1,args.steps+1):
        T=neighbor(T)
        a=a*w%M
        oracle=get_T(a,cache)
        assert T==oracle,("NORM19_CHAIN_DIRECT_P2_MISMATCH",i,a)
        j,v=classify(T)
        print("P2_NORM19_ITERATED_GROSS_P2_CHAIN_PASS",
              "STEP",i,"A",a,"CLASS",j,"VALUE",v,flush=True)
    print("P2_NORM19_ITERATED_CHAIN_COMPLETE_PASS",args.steps,flush=True)
    print("P2_NORM19_GENERAL_A_AND_CHAIN_AUDIT_PASS",
          "SECONDS",round(time.monotonic()-begin,3),flush=True)
    print("BOUNDARY_PILOT_ANCHORS_NOT_FULL_87809710_ORBIT",flush=True)
    print("BOUNDARY_NO_GLOBAL_THETA_C2_OR_SHA_PROOF",flush=True)

if __name__=="__main__":
    main()
