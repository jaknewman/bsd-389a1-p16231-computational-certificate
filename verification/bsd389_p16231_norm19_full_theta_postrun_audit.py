#!/usr/bin/env python3
"""Independent postrun checks: exact H-point histogram, moments and CM closure.
Requires the user's two real full native JSONs. Does NOT rerun 87.8M steps.
This certifies the computed finite layer, not an infinite Iwasawa theorem.
"""
import json
import runpy
from pathlib import Path

root=Path(__file__).resolve().parent
N=runpy.run_path(str(root/"bsd389_p16231_norm19_native_exact_stream.py"),
                 run_name="THETA_POSTRUN_AUDIT_IMPORT")
F=N["fast"]
E=N["E"]
P=N["P"]
M=N["M"]
W=N["W"]
H=N["H"]
assert (P,M,W,H)==(16231,263445361,138112843,87809710)

s=json.loads(N["CHECK"].read_text())
f=json.loads(N["FULL"].read_text())
F["validate_seal"](s)
F["validate_seal"](f)
assert s["status"]=="NORM19_NATIVE_EXACT_PREFIX_CHECKPOINT_PASS"
assert s["last_n"]==H-1 and s["a"]==pow(W,H-1,M)
assert s["p"]==P and s["m"]==M
assert sum(s["histogram"].values())==H
mom=s["moments_modp"]
assert len(mom)==3
assert all(0<=x<P for x in mom)
m0_from_hist=sum(int(E["V"][int(j)])*int(c)
                 for j,c in s["histogram"].items())%P
assert m0_from_hist==mom[0]
print("NORM19_FULL_HISTOGRAM_M0_REAGGREGATE_PASS",m0_from_hist,flush=True)

assert f["status"]=="NORM19_FULL_FINITE_RINGCLASS_CYCLIC_MOMENTS_PASS"
assert f["H"]==H and f["p"]==P and f["m"]==M and f["w"]==W
assert f["raw_moments_mod_p"]==mom
coeff=[(-3*4986*v)%P for v in mom]
assert f["finite_theta_c0_c1_c2_mod_p"]==coeff
assert mom==[0,0,4083] and coeff==[0,0,3739]
print("NORM19_FULL_FINITE_THETA_DEGREE2_NONZERO_PASS",
      mom,coeff,flush=True)

q=E["element"](s["class"],s["q_coordinates"])
assert q in E["reps"][s["class"]].left_order()
assert q.reduced_trace()==-M and q.reduced_norm()==M*M
assert q*q+M*q+M*M==0
unit=pow(W,H,M)
assert unit==213756225 and pow(unit,3,M)==1 and unit!=1
next_class,next_q,_=E["step"](s["class"],q)
direct_class,direct_q,_=E["normalize_anchor"](unit)
assert next_class==direct_class==9
z_next=tuple(int(x) for x in E["coords"](next_class,next_q))
z_direct=tuple(int(x) for x in E["coords"](direct_class,direct_q))
assert F["verify_oriented"](next_class,z_next,direct_class,z_direct)
print("NORM19_FULL_NORM19_LAST_STEP_CUBIC_CM_CLOSURE_PASS",
      H,"UNIT",unit,"CLASS",next_class,flush=True)
initial_class,initial_q,_=E["normalize_anchor"](1)
assert initial_class==next_class
print("NORM19_FULL_RETURN_TO_BASE_BRANDT_CLASS_PASS",initial_class,flush=True)
print("NORM19_FULL_FINITE_LAYER_POSTRUN_AUDIT_PASS",flush=True)
print("BOUNDARY_INFINITE_IWASAWA_SERIES_AND_SHA_NOT_PROVED",flush=True)
