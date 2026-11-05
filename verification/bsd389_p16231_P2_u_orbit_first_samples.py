#!/usr/bin/env python3
"""Small EXACT sample of genuine conductor-one P_2(a*(1+p)^i) Gross classes.

The P2 helper is loaded once: the Hensel/Peirce p4 chart is reused for
all samples.  Each requested point is rebuilt by the exact p8-index
congruence kernel and classified with an exact right-ideal witness.

Default: a=1 and i=0,1,2,3,4,8,16.
Optional --residue r specifies Teichmuller a=r^p mod p².

MATH: P1(a*u^i) is independent of i, since u=1+p and the P1 local
right ideal depends only on a modulo p.  Thus all first 3 (T^k, k<3)
P1 contributions in the level-n1 finite theta coefficients vanish mod p
after summing i=0,...,p-1, since sum_i binom(i,k)=binom(p,k+1)=0 modp.
This script checks only *sample points*, not the complete i/a sums.
"""
import argparse
import hashlib
import json
import runpy
import sys
import time
from pathlib import Path

P=16231
P2=P*P
U=1+P
SCRIPT=Path(__file__).with_name(
    "bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py"
)
assert SCRIPT.is_file()
env=runpy.run_path(str(SCRIPT),run_name="p2_orbit_import")
build=env["build"]
ideals=env["reps"]
V=env["V"]
assert len(ideals)==len(V)==33
assert env["P"]==P and env["P2"]==P2
assert V[32]==0 and V[29]==-2 and V[9]==-1

def get_class(T):
    for j,I in enumerate(ideals):
        ok,witness=I.is_right_equivalent(T,certificate=True)
        if ok:
            assert witness*T==I
            return j,witness
    raise AssertionError("NO_BRANDT_CLASS_FOUND")

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--residue",type=int,default=1)
    pa.add_argument("--indices",nargs="+",type=int,
                    default=[0,1,2,3,4,8,16])
    args=pa.parse_args()
    residue=args.residue%P
    assert residue
    a_teich=pow(residue,P,P2)
    assert a_teich%P==residue
    assert pow(a_teich,P-1,P2)==1
    print("P2_ORBIT_TEICHMULLER_BASE_PASS",residue,a_teich,flush=True)

    indices=list(args.indices)
    assert len(indices)==len(set(indices))
    assert all(0<=i<P for i in indices)
    data=[]
    t0=time.monotonic()
    for i in indices:
        a=a_teich*pow(U,i,P2)%P2
        start=time.monotonic()
        _H,T=build(a)
        j,witness=get_class(T)
        value=int(V[j])
        if residue==1 and i==0:
            assert a==1 and j==9 and value==-1
        rec={"i":i,"a_mod_p2":a,"brandt_class":j,"brandt_value":value,
             "right_ideal_witness":str(witness)}
        # For residue=1, P1 is provably class29 for all i:
        # r1(u^i)=r1(1)*n((u^i-1)/p) with n integral at p.
        if residue==1:
            assert a%P==1
            bracket=(128*(-2)-value)%P
            rec["n1_individual_bracket_mod_p"]=bracket
        data.append(rec)
        print("P2_ACTUAL_GROSS_U_ORBIT_POINT_PASS",
              "I",i,"A",a,"CLASS",j,"VALUE",value,
              "BRACKET_MODP",rec.get("n1_individual_bracket_mod_p","NOT_CALCULATED"),
              "SECONDS",round(time.monotonic()-start,3),flush=True)
    # Finite-field combinatorics: P1-part of the first 3 moments
    # vanishes modulo p after the complete i-sum.
    from math import comb
    for k in range(3):
        assert comb(P,k+1)%P==0
        print("THETA_N1_P1_PART_CANCELS_MODP_FOR_T_POWER",k,flush=True)
    print("P2_ORBIT_SAMPLES_ONLY_NOT_FULL_THETA_MOMENT",len(data),flush=True)
    out=Path.home()/(
        "bsd389_p16231_P2_u_orbit_sample_residue"+str(residue)+".json"
    )
    report={"status":"P2_U_ORBIT_FIRST_SAMPLES_PASS",
       "p":P,"residue_modp":residue,"teich_base_mod_p2":a_teich,
       "source_local_chart_sha256":hashlib.sha256(
         env["raw"]).hexdigest(),
       "sample_count":len(data),"points":data,
       "scope":"Finite sample only; not a complete Gross theta coefficient"}
    out.write_text(json.dumps(report,indent=2)+"\n")
    print("P2_ORBIT_SAMPLES_JSON",out,flush=True)
    print("P2_U_ORBIT_FIRST_SAMPLES_PASS",len(data),
          "SECONDS",round(time.monotonic()-t0,3),flush=True)
    print("BOUNDARY_C2_SUM_OVER_ALL_I_AND_A_NOT_COMPUTED",flush=True)
    print("BOUNDARY_THETA_ORDER_TWO_NOT_PROVED",flush=True)

if __name__=="__main__":
    main()
