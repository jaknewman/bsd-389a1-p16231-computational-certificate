#!/usr/bin/env python3
"""Genuine 19-neighbor transfer at conductor p^2, with independent P2 anchors.

K=Q(sqrt(-3)), E389a1, p=16231, m=p^2.
Start at actual P2^1 (conductor m), represented by T(1)=J2(1)*I32.
Construct q=m*omega inside its left maximal order L=T(1).left_order().
The norm-19 split roots of q^2+m*q+m^2 mod 19 are 9 and 4.
Let J_root=L.left_ideal([q-root,19]), then
 transport=T_next=J_root.conjugate()*T(1).
Check against the independently built true Gross P2 at a=w(g)
or its inverse, with w(g)=(5+3*r0)/(5+3*r1) mod m.

Crucial direct identity test: (g/19)*T_next == T(w(g))
for root9, with g=5+3omega; and same for conjugate root4.
Print explicit diagnostic if equality fails instead of silently
assuming an Artin reciprocity orientation.

This is one exact quaternionic 19-neighbor and NOT a theta coefficient.
"""
import json
from pathlib import Path
from sage.all import ZZ,QQ,matrix
import runpy

src=Path(__file__).with_name(
    "bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py")
env=runpy.run_path(str(src),run_name="NORM19_P2_IMPORT")
B=env["B"]
R=env["R"]
omega=env["omega"]
base=env["base"]
P=env["P"]
M=P*P
g=B(5)+3*omega
gc=B(2)-3*omega
assert g.reduced_norm()==gc.reduced_norm()==19
assert g*gc==B(19)
q=M*omega
assert q.reduced_trace()==-M and q.reduced_norm()==M*M
assert q*q+M*q+B(M*M)==0

def ideal_lattice_index(ideal,order):
    rows=lambda basis: matrix(QQ,
        [list(x.coefficient_tuple()) for x in basis])
    v=abs(rows(ideal.basis()).det()/rows(order.basis()).det())
    return ZZ(v)

w=(5+3*env["r0"])*pow(5+3*env["r1"],-1,M)%M
winv=pow(w,-1,M)
assert w==138112843
print("P2_NORM19_CRT_GALOIS_RATIO_PASS",w,winv,flush=True)

# Independently reconstruct P2 ideals at 1, w and w inverse from
# the certified congruence lattice and true p^4 split chart.
H,T=env["build"](1)
Hw,Tw=env["build"](w)
Hwi,Twi=env["build"](winv)
L=T.left_order()
assert L.discriminant()==389
assert q in L
print("P2_CONDUCTOR_P2_Q_IN_LEFT_ORDER_PASS",flush=True)

root_g=(M*11)%19
root_gc=(M*7)%19
assert root_g==9 and root_gc==4
assert (root_g*root_g+M*root_g+M*M)%19==0
assert (root_gc*root_gc+M*root_gc+M*M)%19==0
print("P2_NORM19_SPLIT_ROOTS_PASS",root_g,root_gc,flush=True)

records=[]
for label,root,h,target in [
    ("G",root_g,g,Tw),
    ("G_CONJUGATE",root_gc,gc,Twi)
]:
    J=L.left_ideal([q-B(root),B(19)])
    assert J.right_order().discriminant()==389
    assert q in J.right_order()
    index=ideal_lattice_index(J,L)
    assert index==19*19,("WRONG_J19_INDEX",label,index)
    transported=J.conjugate()*T
    assert transported.right_order()==T.right_order()
    print("P2_NORM19_ORIENTED_NEIGHBOR_INDEX_361_PASS",label,root,flush=True)

    # The global 19-prime generator h gives a candidate rational
    # left multiplier of reduced norm 1/19.
    proposed=(h/B(19))*transported
    direct_identity=(proposed==target)
    print("P2_NORM19_GLOBAL_MULTIPLIER_EQUALITY",
          label,direct_identity,flush=True)
    # Even if the two specific ideal lattices differ in normalization,
    # the right class must match the directly reconstructed Gross point.
    equivalent,alpha=target.is_right_equivalent(
        transported,certificate=True)
    if equivalent:
        assert alpha*transported==target
        print("P2_NORM19_RIGHT_EQUIVALENCE_WITNESS_PASS",
              label,"ROOT",root,flush=True)
    else:
        print("P2_NORM19_RIGHT_EQUIVALENCE_OPEN",
              label,"ROOT",root,flush=True)

    record={"direction":label,"root_mod19":root,
            "left_ideal_index":int(index),
            "global_multiplier_exact_identity":bool(direct_identity),
            "brandt_right_equivalent":bool(equivalent),
            "witness":str(alpha) if equivalent else None}
    records.append(record)
    assert equivalent, ("NO_EXPECTED_19_TRANSPORT",label,
                         "Possible orientation mismatch; no false PASS")
    if direct_identity:
        print("P2_NORM19_EXPLICIT_GLOBAL_TRANSPORT_PASS",label,flush=True)

assert len(records)==2
out=Path.home()/"bsd389_p16231_P2_norm19_one_step_transport.json"
report={
    "status":"P2_CONDUCTOR_P2_NORM19_TRANSPORT_PASS",
    "p":P,"m":M,"brandt_base_index":32,
    "galois_split_ratio_mod_p2":w,
    "galois_split_ratio_inverse_mod_p2":winv,
    "transport":records,
    "scope":"One +19 and one inverse norm19 ideal transport from a=1 only"}
out.write_text(json.dumps(report,indent=2)+"\n")
print("P2_NORM19_ONE_STEP_JSON",out,flush=True)
print("P2_NORM19_ONE_STEP_BOTH_DIRECTIONS_PASS",flush=True)
print("BOUNDARY_NO_THETA_SUM_OR_ALL_19_CYCLE_COMPUTATION",flush=True)
