#!/usr/bin/env python3
"""Certified chunked genuine Gross P2 orbit + aggregation for E389a1,p16231.

Compute phi_f(P2^(a*(1+p)^i)) using the REAL p4 split ideal J2(a),
exact HNF, 16 right ideal closure tests and exact quaternionic right
equivalence witness. Reuse the certified conductor-ONE base R_32.

Default: --residue 1 --start 0 --count 512.
Optional: --mu3-check (checks three actual Gross class equalities).
After all 16231 i are computed for one Teich residue:
  --aggregate --residue 1
produces all three full i-moments mod p, not a global a-sum.
The correct theta coefficient still needs all 5410 Teich residue
representatives modulo the CM-unit subgroup mu3.

Source P2 builder is dynamically imported ONCE, never rederived.
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from math import comb
from collections import Counter
from contextlib import redirect_stdout
from io import StringIO

P=16231
MOD=P*P
U=1+P
# Frozen exact Sage-verified integer Brandt eigenvector.
V=(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,
   0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0)
assert len(V)==33 and V[29]==-2 and V[9]==-1 and V[32]==0
CHART_EXPECTED_SHA="63ff37e2338369ca4fc989d7a8974892c69b3359836aa395605b90e61162ff35"
OUTDIR=Path.home()/"bsd389_p16231_P2_u_orbit_chunk_certificates"

def expected_a(residue,i):
    a0=pow(residue,P,MOD)
    a=a0*(1+i*P)%MOD
    assert a==a0*pow(U,i,MOD)%MOD
    return a

def filename(residue,start,end):
    return OUTDIR/("r"+str(residue)+"_i"+str(start).zfill(5)+
                   "_"+str(end).zfill(5)+".json")

def load_modules():
    import runpy
    src=Path(__file__).with_name(
        "bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py")
    assert src.exists()
    e=runpy.run_path(str(src),run_name="P2_CHUNK_IMPORTED")
    assert e["P"]==P and e["P2"]==MOD and e["MOD"]==P**4
    assert tuple(e["V"])==V
    raw=e["raw"]
    source_hash=hashlib.sha256(raw).hexdigest()
    assert source_hash==CHART_EXPECTED_SHA, (
        "SOURCE_CHART_CHANGED",source_hash,CHART_EXPECTED_SHA)
    return e,source_hash

def run_one(e,a):
    output=StringIO()
    try:
        with redirect_stdout(output):
            H,T=e["build"](a)
    except Exception:
        print("GROSS_BUILDER_ERROR_OUTPUT",output.getvalue(),flush=True)
        raise
    matches=[]
    for j,I in enumerate(e["reps"]):
        yes,witness=I.is_right_equivalent(T,certificate=True)
        if yes:
            assert witness*T==I,("RIGHT_EQUIVALENCE_WITNESS_INVALID",a,j)
            matches.append((j,str(witness)))
            break
    assert len(matches)==1,("NO_BRANDT_CLASS_MATCH",a)
    j,witness=matches[0]
    return j,int(V[j]),witness

def test_mu3(e):
    # Global maximal CM order contains omega. In the split local chart
    # omega=diag(r0,r1), so conjugation sends n(a/p²) to n(lambda*a/p²),
    # lambda=r0/r1 mod p². Conjugation by the GLOBAL unit preserves the
    # right-ideal class, yielding a 3-fold symmetry in Teich a.
    r0,r1=e["r0"],e["r1"]
    lam=r0*pow(r1,-1,P**4)%(P**4)
    lam_mod=lam%MOD
    assert pow(lam_mod,3,MOD)==1 and lam_mod!=1
    assert lam_mod in (49689135,213756225)
    for i in (0,1,2):
        a=expected_a(1,i)
        labels=[]
        for k in range(3):
            aa=a*pow(lam_mod,k,MOD)%MOD
            j,v,_=run_one(e,aa)
            labels.append((j,v))
        assert len(set(labels))==1,("MU3_GROSS_CLASS_MISMATCH",i,labels)
        print("P2_MU3_GLOBAL_CM_UNIT_CLASS_SYMMETRY_PASS",
              "I",i,"CLASS",labels[0][0],"VALUE",labels[0][1],flush=True)
    print("P2_MU3_REDUCES_TEICH_REPRESENTATIVES",
          P-1,"TO",(P-1)//3,flush=True)

def chunk(residue,start,count,mu3):
    assert 1<=residue<P and 0<=start<P and 1<=count<=P-start
    dest=filename(residue,start,start+count)
    assert not dest.exists(),("CHUNK_ALREADY_EXISTS",str(dest),
                              "Use --aggregate or choose a new range.")
    e,chart_hash=load_modules()
    if mu3:
        test_mu3(e)
    begin=time.monotonic()
    values=[]
    counts=Counter()
    moments=[0,0,0]
    for i in range(start,start+count):
        a=expected_a(residue,i)
        j,v,wit=run_one(e,a)
        if residue==1 and i==0:
            assert j==9 and v==-1
        values.append({"i":i,"a":a,"brandt_class":j,
                       "brandt_value":v,"witness":wit})
        counts[j]+=1
        moments[0]=(moments[0]+v)%P
        moments[1]=(moments[1]+i*v)%P
        moments[2]=(moments[2]+comb(i,2)*v)%P
        if (i-start+1)%64==0 or i==start+count-1:
            print("P2_CHUNK_PROGRESS","RESIDUE",residue,
                  "LAST_I",i,"DONE",i-start+1,"OF",count,
                  "SECONDS",round(time.monotonic()-begin,3),flush=True)
    OUTDIR.mkdir(parents=True,exist_ok=True)
    payload={"status":"P2_GROSS_EXACT_CHUNK_PASS",
          "p":P,"residue":residue,"start":start,
          "end_exclusive":start+count,
          "source_local_chart_sha256":chart_hash,
          "points":values,
          "moment0_1_2_modp":moments,
          "brandt_class_histogram":dict(sorted(counts.items())),
          "scope":"One Teich residue subset of i; not the whole theta"}
    # Atomic write; avoid marking partial chunks complete on interruption.
    temp=dest.with_suffix(".tmp")
    temp.write_text(json.dumps(payload,indent=2)+"\n")
    temp.replace(dest)
    print("P2_EXACT_CHUNK_CERTIFICATE",dest,flush=True)
    print("P2_EXACT_CHUNK_SHA256",
          hashlib.sha256(dest.read_bytes()).hexdigest(),flush=True)
    print("P2_EXACT_CHUNK_MOMENTS_MODP",moments,flush=True)
    print("P2_EXACT_CHUNK_PASS",residue,start,start+count,flush=True)
    print("BOUNDARY_CHUNK_NOT_COMPLETE_I_OR_A_SUM_UNLESS_ALL_RECORDED",flush=True)

def aggregate(residue):
    OUTDIR.mkdir(parents=True,exist_ok=True)
    files=sorted(OUTDIR.glob("r"+str(residue)+"_i*.json"))
    assert files,"NO_CHUNKS_FOR_RESIDUE"
    full={}
    chart_hash=None
    counts=Counter()
    moments=[0,0,0]
    for path in files:
        raw=path.read_bytes()
        o=json.loads(raw)
        assert o["status"]=="P2_GROSS_EXACT_CHUNK_PASS"
        assert o["p"]==P and o["residue"]==residue
        assert chart_hash is None or o["source_local_chart_sha256"]==chart_hash
        chart_hash=o["source_local_chart_sha256"]
        start,end=o["start"],o["end_exclusive"]
        assert 0<=start<end<=P and len(o["points"])==end-start
        local=[0,0,0]
        for n,row in enumerate(o["points"]):
            i=row["i"]
            assert i==start+n and i not in full,("DUPLICATE_I",i)
            assert row["a"]==expected_a(residue,i)
            j=row["brandt_class"];v=row["brandt_value"]
            assert type(j) is int and 0<=j<33
            assert type(v) is int and V[j]==v
            assert isinstance(row["witness"],str) and row["witness"]
            full[i]=row
            counts[j]+=1
            vv=(v,i*v,comb(i,2)*v)
            for k in range(3):
                local[k]=(local[k]+vv[k])%P
                moments[k]=(moments[k]+vv[k])%P
        assert local==o["moment0_1_2_modp"],("CHUNK_MOMENT_MISMATCH",path)
        print("P2_AGGREGATE_CHUNK_SHA256",path.name,
              hashlib.sha256(raw).hexdigest(),flush=True)
    assert chart_hash==CHART_EXPECTED_SHA
    missing=[i for i in range(P) if i not in full]
    print("P2_AGGREGATE_COVERAGE",len(full),"OF",P,
          "MISSING",len(missing),flush=True)
    if missing:
        print("P2_AGGREGATE_INCOMPLETE_FIRST_MISSING",missing[:12],flush=True)
        raise SystemExit(2)
    assert len(full)==P and sum(counts.values())==P
    print("P2_FULL_ONE_TEICH_ORBIT_CLASS_HISTOGRAM",
          dict(sorted(counts.items())),flush=True)
    print("P2_FULL_ONE_TEICH_ORBIT_MOMENTS_MODP",
          moments,flush=True)
    contribution=[(-4986*m)%P for m in moments]
    print("P2_ONE_TEICH_ORBIT_THETA_DEG0_1_2_CONTRIBUTIONS_MODP",
          contribution,flush=True)
    for k in range(3):
        assert comb(P,k+1)%P==0
    summary={"status":"P2_FULL_ONE_TEICH_ORBIT_MOMENTS_PASS",
            "p":P,"residue":residue,"source_local_chart_sha256":chart_hash,
            "count":len(full),"moments_mod_p":moments,
            "theta_contributions_mod_p":contribution,
            "brandt_class_histogram":dict(sorted(counts.items())),
            "files":[p.name for p in files],
            "scope":"Full i orbit for ONE Teich residue, not full theta sum"}
    dest=OUTDIR/("r"+str(residue)+"_FULL_ORBIT_MOMENTS.json")
    dest.write_text(json.dumps(summary,indent=2)+"\n")
    print("P2_FULL_ONE_TEICH_ORBIT_RESULT",dest,flush=True)
    print("P2_FULL_ONE_TEICH_ORBIT_MOMENTS_PASS",flush=True)
    print("BOUNDARY_OTHER_5410_TEICH_UNIT_ORBITS_NOT_SUMMED",flush=True)
    print("BOUNDARY_THETA_ORDER2_AND_SHA_NOT_PROVED",flush=True)

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--residue",type=int,default=1)
    pa.add_argument("--start",type=int,default=0)
    pa.add_argument("--count",type=int,default=512)
    pa.add_argument("--mu3-check",action="store_true")
    pa.add_argument("--aggregate",action="store_true")
    args=pa.parse_args()
    if args.aggregate:
        aggregate(args.residue)
    else:
        chunk(args.residue,args.start,args.count,args.mu3_check)

if __name__=="__main__":
    main()
