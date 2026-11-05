#!/usr/bin/env python3
"""Exact restartable stream of normalized/oriented norm19 Gross P2 points.

Preserves 128-step USER_PASS (129 points n=0..128) as an optional
bootstrap, then keeps only ONE state (Brandt class, integral CM element)
plus moment accumulators, not an ever-growing list of quaternionic
ideals. Snapshot checkpoints are atomically written with self-digest.

No full cycle or global theta nonvanishing claim before 87809710 steps.
"""
import argparse
import hashlib
import json
import os
import runpy
import time
from collections import Counter
from pathlib import Path

E=runpy.run_path(str(Path(__file__).with_name(
    "bsd389_p16231_P2_norm19_reduced_oriented_chain_moment_pilot.py")),
    run_name="NORM19_REDUCED_STREAM_IMPORT")
P=E["P"];M=E["M"];w=E["w"];S=E["S"];H=E["H"]
reps=E["reps"];V=E["V"]
assert (P,M,w,S,H)==(16231,263445361,138112843,10816,87809710)
assert len(reps)==len(V)==33
HOME=Path.home()
PILOT=HOME/"bsd389_p16231_P2_norm19_reduced_orbit_128steps.json"
CHECKPOINT=HOME/"bsd389_p16231_P2_norm19_cyclic_stream_checkpoint.json"
ORBIT_DIR=HOME/"bsd389_p16231_P2_u_orbit_chunk_certificates"

def digest(obj):
    return hashlib.sha256(
        json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def validate_checkpoint(o):
    assert o["status"]=="NORM19_REDUCED_STREAM_CHECKPOINT_PASS"
    assert o["p"]==P and o["m"]==M and o["generator"]==w
    assert o["H"]==H and o["S"]==S
    assert o["data_sha256"]==digest({k:v for k,v in o.items()
                                    if k!="data_sha256"})
    n=int(o["last_n"])
    assert 0<=n<H and int(o["a"])==pow(w,n,M)
    j=int(o["brandt_class"])
    assert 0<=j<33
    z=list(map(int,o["q_coordinates"]))
    assert len(z)==4
    q=E["element"](j,z)
    assert q in reps[j].left_order()
    assert q.reduced_trace()==-M and q.reduced_norm()==M*M
    assert q*q+M*q+M*M==0
    assert len(o["moments_modp"])==3
    assert all(0<=int(x)<P for x in o["moments_modp"])
    hist=o["histogram"]
    assert sum(hist.values())==n+1
    assert sum(k.isdigit() and 0<=int(k)<33 for k in hist)==len(hist)
    assert max(abs(x) for x in z)<=o["max_abs_q_coordinate"]
    return j,q,n

def make_object(j,q,n,a,mom,hist,maxcoord,origin):
    z=[int(v) for v in E["coords"](j,q)]
    o={"status":"NORM19_REDUCED_STREAM_CHECKPOINT_PASS",
       "p":P,"m":M,"H":H,"generator":w,"S":S,
       "origin":origin,"last_n":n,"a":int(a),
       "brandt_class":int(j),"q_coordinates":z,
       "moments_modp":[int(t) for t in mom],
       "histogram":dict(sorted(hist.items(),key=lambda kv:int(kv[0]))),
       "max_abs_q_coordinate":int(maxcoord),
       "scope":"Accumulated only n=0..last_n, not global theta"}
    o["data_sha256"]=digest(o)
    validate_checkpoint(o)
    return o

def atomic_store(obj):
    CHECKPOINT.parent.mkdir(exist_ok=True,parents=True)
    tmp=CHECKPOINT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n")
    os.replace(tmp,CHECKPOINT)
    print("NORM19_STREAM_CHECKPOINT_PASS",obj["last_n"],
          obj["data_sha256"],flush=True)

def bootstrap():
    if CHECKPOINT.exists():
        o=json.loads(CHECKPOINT.read_text())
        j,q,n=validate_checkpoint(o)
        print("NORM19_STREAM_RESTORE_EXACT_ORIENTED_STATE_PASS",
              n,"CLASS",j,flush=True)
        return j,q,n,int(o["a"]),list(o["moments_modp"]),Counter(o["histogram"]),int(o["max_abs_q_coordinate"]),o["origin"]
    if PILOT.exists():
        raw=PILOT.read_bytes()
        p=json.loads(raw)
        assert p["status"]=="REDUCED_ORIENTED_NORM19_FINITE_PILOT_PASS"
        assert p["p"]==P and p["conductor"]==M
        assert p["galois_generator_ratio"]==w
        assert p["steps"]==128 and len(p["states"])==129
        assert p["truncated_moments_mod_p"]==[16213,8425,12622]
        vals=[0,0,0]
        hist=Counter()
        for n,row in enumerate(p["states"]):
            assert row["n"]==n and row["a_mod_p2"]==pow(w,n,M)
            assert row["i_mod_p"]==S*n%P
            j=int(row["brandt_class"])
            val=int(row["value"])
            assert val==int(V[j])
            hist[str(j)]+=1
            i=row["i_mod_p"]
            for k,weight in enumerate((1,i,i*(i-1)//2)):
                vals[k]=(vals[k]+weight*val)%P
        assert vals==p["truncated_moments_mod_p"]
        assert hist==Counter({str(k):v for k,v in p["brandt_histogram"].items()})
        row=p["states"][-1]
        j=int(row["brandt_class"])
        q=E["element"](j,row["q_basis_coordinates"])
        assert q in reps[j].left_order()
        assert q.reduced_trace()==-M and q.reduced_norm()==M*M
        assert q*q+M*q+M*M==0
        q2=E["normalize_anchor"](pow(w,128,M))[1]
        assert q==q2, "USER_128_PILOT_EMBEDDING_NO_LONGER_MATCHES"
        maxcoord=int(p["max_abs_q_basis_coordinate"])
        obj=make_object(j,q,128,pow(w,128,M),vals,hist,maxcoord,
                        "User 128-step pilot SHA256 "+hashlib.sha256(raw).hexdigest())
        atomic_store(obj)
        print("NORM19_STREAM_BOOTSTRAP_128_USER_PILOT_PASS",flush=True)
        return j,q,128,pow(w,128,M),vals,hist,maxcoord,obj["origin"]

    j,q,_=E["normalize_anchor"](1)
    assert j==9
    val=int(V[j]); hist=Counter({str(j):1})
    z=E["coords"](j,q)
    maxcoord=max(abs(int(x)) for x in z)
    mom=[val%P,0,0]
    obj=make_object(j,q,0,1,mom,hist,maxcoord,"Fresh Gross P2(a=1)")
    atomic_store(obj)
    print("NORM19_STREAM_BOOTSTRAP_FRESH_P2_PASS",flush=True)
    return j,q,0,1,mom,hist,maxcoord,obj["origin"]

def check_anchor(n,j,q,a,check_teich):
    k,qd,_=E["normalize_anchor"](a)
    assert k==j,("BRANDT_ORACLE_MISMATCH",n,j,k)
    assert q==qd,("CM_ORIENTATION_ORACLE_MISMATCH",n,j)
    print("NORM19_STREAM_DIRECT_GROSS_EMBEDDING_PASS",n,j,flush=True)
    if check_teich and n==5410:
        i=(S*n)%P
        assert i==1805
        candidates=sorted(ORBIT_DIR.glob("r1_i*.json"))
        matching=[]
        for path in candidates:
            o=json.loads(path.read_text())
            if o["start"]<=i<o["end_exclusive"]:
                row=o["points"][i-o["start"]]
                assert row["i"]==i and row["brandt_value"]==int(V[j])
                assert row["brandt_class"]==j
                matching.append(path.name)
        assert len(matching)==1,("MISSING_TEICH_BRIDGE",matching)
        print("NORM19_STREAM_5410_STEP_TRUE_TEICH_ORBIT_BRIDGE_PASS",
              "I",i,"CLASS",j,"VALUE",int(V[j]),
              "SOURCE",matching[0],flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target-n",type=int,default=2048,
                    help="include every state n=0..target_n exactly once")
    ap.add_argument("--checkpoint-every",type=int,default=256)
    ap.add_argument("--oracle-every",type=int,default=512)
    ap.add_argument("--bridge-5410",action="store_true")
    ap.add_argument("--bridge-16231",action="store_true")
    args=ap.parse_args()
    assert 0<=args.target_n<H and args.checkpoint_every>=1
    assert args.oracle_every>=0
    j,q,n,a,mom,hist,maxcoord,origin=bootstrap()
    assert n<=args.target_n,("TARGET_BEFORE_CHECKPOINT",n,args.target_n)
    t0=time.monotonic()
    for k in range(n+1,args.target_n+1):
        j,q,_=E["step"](j,q)
        a=(a*w)%M
        assert a==pow(w,k,M)
        i=(S*k)%P
        value=int(V[j])
        weights=(1,i,i*(i-1)//2)
        for m in range(3):
            mom[m]=(mom[m]+weights[m]*value)%P
        hist[str(j)]+=1
        z=E["coords"](j,q)
        maxcoord=max(maxcoord,max(abs(int(t)) for t in z))
        n=k
        if (args.oracle_every and n%args.oracle_every==0) or \
           (args.bridge_5410 and n==5410) or \
           (args.bridge_16231 and n==P):
            check_anchor(n,j,q,a,args.bridge_5410)
            if args.bridge_16231 and n==P:
                # At step p, w^p is exactly the Teichmuller component.
                # Independent genuine P2 anchor already user-certified
                # for a=121898074, Brandt class 24, value zero.
                assert a==pow(w,P,M)==121898074
                assert (S*n)%P==0
                assert j==24 and int(E["V"][j])==0
                print("NORM19_STREAM_P_STEP_TEICH_ANCHOR_PASS",
                      n,"A",a,"CLASS",j,"VALUE",int(E["V"][j]),flush=True)
        if n%args.checkpoint_every==0 or n==args.target_n:
            o=make_object(j,q,n,a,mom,hist,maxcoord,origin)
            atomic_store(o)
            print("NORM19_STREAM_PROGRESS",n,"OF",H-1,
                  "MOMENTS",mom,"MAX_COORD",maxcoord,
                  "ELAPSED",round(time.monotonic()-t0,3),flush=True)
    o=json.loads(CHECKPOINT.read_text())
    assert validate_checkpoint(o)[2]==args.target_n
    print("NORM19_STREAM_EXACT_PREFIX_PASS",args.target_n+1,
          "MOMENTS",o["moments_modp"],flush=True)
    print("NORM19_STREAM_LAST_STATE_CLASS",j,flush=True)
    print("NORM19_STREAM_MAX_CM_COORD",maxcoord,flush=True)
    print("NORM19_STREAM_RESULT",CHECKPOINT,flush=True)
    print("BOUNDARY_PREFIX_NOT_FULL_87809710_THETA_SUM",flush=True)
    print("BOUNDARY_THETA_C2_AND_SHA_NOT_PROVED",flush=True)

if __name__=="__main__":
    main()
