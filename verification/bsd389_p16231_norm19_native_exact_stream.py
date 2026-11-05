#!/usr/bin/env python3
"""Exact C++/Sage hybrid ring-class Gross P2 theta moments, p=16231.

Cpp_int core applies only integer matrices certified by genuine Sage
quaternionic norm19 right-ideal equivalence witnesses. On an unknown
local mod19 key, execution stops, Sage derives the exact edge, and
the native stream continues. Atomic checkpoints NEVER overwrite
user-certified n=16231 Python artifacts.
"""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import time
from collections import Counter

ROOT=Path(__file__).resolve().parent
fast=runpy.run_path(str(ROOT/"bsd389_p16231_P2_norm19_cached_matrix_transition_pilot.py"),
                    run_name="NATIVE_GROSS_IMPORT")
E=fast["E"]
P=fast["P"];M=fast["M"];W=fast["w"];S=fast["S"];H=fast["H"]
assert (P,M,W,S,H)==(16231,263445361,138112843,10816,87809710)
B=E["B"];V=E["V"];REPS=E["reps"]
HOME=Path.home()
CORE=ROOT/"bsd389_p16231_norm19_native_matrix_core.cpp"
SO=HOME/"bsd389_p16231_norm19_native_matrix_core.so"
EDGE=HOME/"bsd389_p16231_norm19_native_exact_edges.json"
CHECK=HOME/"bsd389_p16231_norm19_native_exact_checkpoint.json"
FULL=HOME/"bsd389_p16231_norm19_complete_cyclic_theta_moments.json"
SOURCE_SHA=fast["source_sha"]
CORE_SHA=hashlib.sha256(CORE.read_bytes()).hexdigest()
USER_STATE_SHA="36c1e557221416bc943fd5ab1637a90c1d2b149fe330f7f8f7c32087d89f6a95"
USER_EDGES_SHA="111ea4dfc9109dc8cabef4d44e6fc74543ce139394e3e070cf8adfc9f5c7c3f1"

def get_native():
    compiler=shutil.which("g++")
    if not compiler:
        raise SystemExit("NORM19_NATIVE_NEEDS_GPLUSPLUS_WITH_BOOST_HEADERS")
    # Conda's C++ compiler may use its own sysroot and not search
    # /usr/include; find the header in the active env explicitly.
    candidates=[Path(os.environ["CONDA_PREFIX"])/"include"
                ] if os.environ.get("CONDA_PREFIX") else []
    candidates += [Path("/usr/include"),Path("/usr/local/include")]
    includes=[p for p in candidates
              if (p/"boost/multiprecision/cpp_int.hpp").is_file()]
    if not includes:
        raise SystemExit(
            "NORM19_NATIVE_MISSING_BOOST_HEADERS: "
            "install into activated sage environment: "
            "conda install -c conda-forge libboost-headers")
    if not SO.exists() or CORE.stat().st_mtime>SO.stat().st_mtime:
        command=[compiler,"-O3","-std=c++17","-shared","-fPIC"]
        command += ["-I"+str(p) for p in includes]
        command += [str(CORE),"-o",str(SO)]
        print("NORM19_NATIVE_BOOST_INCLUDE_DIRS",
              [str(p) for p in includes],flush=True)
        subprocess.run(command,check=True,timeout=120)
    print("NORM19_NATIVE_CPP_COMPILED_PASS",CORE_SHA,flush=True)
    lib=ctypes.CDLL(str(SO))
    for name in ("bsd_register_edge","bsd_set_state"):
        fn=getattr(lib,name);fn.argtypes=[ctypes.c_char_p];fn.restype=ctypes.c_int
    lib.bsd_run_until.argtypes=[ctypes.c_uint64]
    lib.bsd_run_until.restype=ctypes.c_int
    for name in ("bsd_state_text","bsd_missing_key","bsd_error"):
        getattr(lib,name).restype=ctypes.c_char_p
    lib.bsd_cache_size.restype=ctypes.c_int
    return lib

def native_error(lib,code,label):
    assert code>=0,(label,code,lib.bsd_error().decode())

def register(lib,key,e):
    j,res=key.split(":")
    residues=list(map(int,res.split(",")))
    assert len(residues)==4 and all(0<=x<19 for x in residues)
    A=e["matrix_num"]
    assert len(A)==4 and all(len(r)==4 for r in A)
    row=[int(j),*residues,int(e["dest"]),int(e["den"]),
         *(A[r][c] for r in range(4) for c in range(4))]
    assert len(row)==23
    rc=lib.bsd_register_edge(" ".join(map(str,row)).encode())
    assert rc==0,("REGISTER_EDGE_FAILED",key,rc,lib.bsd_error().decode())

def read_native(lib):
    vals=list(map(int,lib.bsd_state_text().decode().split()))
    assert len(vals)==46,len(vals)
    n,a,j=vals[:3]
    z=tuple(vals[3:7]);mom=vals[7:10]
    hist=Counter({str(i):v for i,v in enumerate(vals[10:43]) if v})
    maxcoord,hits,misses=vals[43:]
    assert 0<=n<H and 0<a<M and 0<=j<33
    assert sum(hist.values())==n+1
    return dict(n=n,a=a,j=j,z=z,mom=mom,hist=hist,
                maxcoord=maxcoord,hits=hits,misses=misses)

def configure_native(lib,s):
    row=[s["n"],s["a"],s["j"],*s["z"],*s["mom"],
         *(s["hist"].get(str(j),0) for j in range(33)),s["maxcoord"]]
    rc=lib.bsd_set_state(" ".join(map(str,row)).encode())
    assert rc==0,("NATIVE_SET_STATE_FAIL",rc,lib.bsd_error().decode())
    assert read_native(lib)["n"]==s["n"]

def cm_audit(s):
    q=E["element"](s["j"],s["z"])
    assert q in REPS[s["j"]].left_order()
    assert q.reduced_trace()==-M and q.reduced_norm()==M*M
    assert q*q+M*q+B(M*M)==0
    assert s["a"]==pow(W,s["n"],M)

def bootstrap():
    if CHECK.exists():
        o=json.loads(CHECK.read_text());fast["validate_seal"](o)
        assert o["status"]=="NORM19_NATIVE_EXACT_PREFIX_CHECKPOINT_PASS"
        assert (o["p"],o["m"],o["w"],o["S"],o["H"])==(P,M,W,S,H)
        assert o["core_sha256"]==CORE_SHA and o["source_sha256"]==SOURCE_SHA
        x=json.loads(EDGE.read_text());fast["validate_seal"](x)
        assert x["status"]=="NORM19_NATIVE_EXACT_EDGE_CACHE"
        assert x["core_sha256"]==CORE_SHA and x["source_sha256"]==SOURCE_SHA
        cache=x["edges"]
        assert len(cache)>=o["edge_count"]
        if len(cache)==o["edge_count"]:
            assert x["sha256"]==o["edge_sha256"]
        s=dict(n=o["last_n"],a=o["a"],j=o["class"],
               z=tuple(o["q_coordinates"]),mom=list(o["moments_modp"]),
               hist=Counter(o["histogram"]),maxcoord=o["max_abs_q_coordinate"])
        cm_audit(s)
        print("NORM19_NATIVE_EXACT_CHECKPOINT_RESTORED_PASS",
              s["n"],"EDGE_KEYS",len(cache),flush=True)
        return s,cache
    old=json.loads(fast["FAST_PATH"].read_text())
    fast["validate_seal"](old)
    assert old["sha256"]==USER_STATE_SHA and old["last_n"]==P
    assert old["class"]==24 and old["a"]==121898074
    prev=json.loads(fast["CACHE_PATH"].read_text())
    fast["validate_seal"](prev)
    assert prev["sha256"]==USER_EDGES_SHA and len(prev["edges"])==7216
    s=dict(n=old["last_n"],a=old["a"],j=old["class"],
           z=tuple(old["q_coordinates"]),mom=list(old["moments_modp"]),
           hist=Counter(old["histogram"]),
           maxcoord=old["max_abs_q_coordinate"])
    cm_audit(s)
    print("NORM19_NATIVE_BOOTSTRAP_FROM_USER_16231_PASS",
          s["j"],len(prev["edges"]),flush=True)
    return s,prev["edges"]

def store(s,cache):
    cm_audit(s)
    assert len(cache)<=12540
    ec=fast["sealed"]({
        "status":"NORM19_NATIVE_EXACT_EDGE_CACHE","p":P,"m":M,
        "core_sha256":CORE_SHA,"source_sha256":SOURCE_SHA,
        "edges":cache})
    # Store edge table first, then state. An edge superset can be resumed.
    fast["atomic_json"](EDGE,ec)
    record=fast["sealed"]({
        "status":"NORM19_NATIVE_EXACT_PREFIX_CHECKPOINT_PASS",
        "p":P,"m":M,"H":H,"w":W,"S":S,
        "source_sha256":SOURCE_SHA,"core_sha256":CORE_SHA,
        "source_user_checkpoint_sha256":USER_STATE_SHA,
        "last_n":s["n"],"a":s["a"],"class":s["j"],
        "q_coordinates":list(s["z"]),
        "moments_modp":s["mom"],"histogram":dict(s["hist"]),
        "max_abs_q_coordinate":s["maxcoord"],"edge_count":len(cache),
        "edge_sha256":ec["sha256"],
        "scope":"Prefix only until last_n=87809709"})
    fast["atomic_json"](CHECK,record)
    print("NORM19_NATIVE_EXACT_CHECKPOINT_PASS",s["n"],
          "MOMENTS",s["mom"],"EDGES",len(cache),
          "SHA256",record["sha256"],flush=True)

def load_existing_teich_orbit():
    folder=HOME/"bsd389_p16231_P2_u_orbit_chunk_certificates"
    files=sorted(folder.glob("r1_i*.json"))
    assert len(files)==32,("NEED_FULL_32_AUTHENTIC_CHUNKS",len(files))
    first=folder/"r1_i00000_00512.json"
    assert hashlib.sha256(first.read_bytes()).hexdigest()==(
        "2a12796dd1fd56351e82c2337c02d74d578ab87fa01f40c564dc37c79ad66db5")
    rows=[None]*P
    sums=[0,0,0]
    for fn in files:
        o=json.loads(fn.read_text())
        assert o["status"]=="P2_GROSS_EXACT_CHUNK_PASS"
        assert o["p"]==P and o["residue"]==1
        lo,hi=o["start"],o["end_exclusive"]
        assert len(o["points"])==hi-lo
        sub=[0,0,0]
        for i,row in enumerate(o["points"],lo):
            assert 0<=i<P and rows[i] is None and row["i"]==i
            assert row["a"]==(1+i*P)%M
            j,v=row["brandt_class"],row["brandt_value"]
            assert int(V[j])==v
            rows[i]=(j,v)
            for k,x in enumerate((1,i,i*(i-1)//2)):
                sub[k]=(sub[k]+x*v)%P
                sums[k]=(sums[k]+x*v)%P
        assert sub==o["moment0_1_2_modp"]
    assert all(z is not None for z in rows)
    assert sums==[0,10775,5515]
    print("NORM19_NATIVE_EXISTING_COMPLETE_TEICH_ORBIT_RECHECK_PASS",sums,flush=True)
    return rows

def next_stop(n,target,checkpoint_every,oracle_every,teich_enabled):
    stops=[target,((n//checkpoint_every)+1)*checkpoint_every]
    if oracle_every:stops.append(((n//oracle_every)+1)*oracle_every)
    if teich_enabled:stops.append(((n//5410)+1)*5410)
    return min(v for v in stops if v>n)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target-n",type=int,default=50000)
    ap.add_argument("--checkpoint-every",type=int,default=8192)
    ap.add_argument("--oracle-every",type=int,default=8192)
    ap.add_argument("--teich-crosscheck",action="store_true")
    args=ap.parse_args()
    assert P<=args.target_n<H
    assert args.checkpoint_every>=1 and args.oracle_every>=0
    t0=time.monotonic()
    lib=get_native()
    s,cache=bootstrap()
    assert s["n"]<=args.target_n
    print("NORM19_NATIVE_REGISTER_CERTIFIED_MATRIX_EDGES",len(cache),flush=True)
    for key,edge in cache.items():register(lib,key,edge)
    assert lib.bsd_cache_size()==len(cache)
    configure_native(lib,s)
    teich=load_existing_teich_orbit() if args.teich_crosscheck else None
    new_edges=0
    while s["n"]<args.target_n:
        n0=s["n"]
        stop=next_stop(n0,args.target_n,
                       args.checkpoint_every,args.oracle_every,bool(teich))
        while True:
            rc=lib.bsd_run_until(stop)
            native_error(lib,rc,"NORM19_NATIVE_EXACT_MATRIX_STEP")
            s=read_native(lib)
            if rc==0:
                assert s["n"]==stop
                break
            assert rc==1
            key=fast["key_for"](s["j"],s["z"])
            native_key=lib.bsd_missing_key().decode().split()
            assert key==native_key[0]+":"+",".join(native_key[1:])
            assert key not in cache
            # Sage builds a real norm-19 oriented quaternion ideal,
            # proves exact equivalence and certifies its 4x4 matrix.
            edge=fast["construct_edge"](s["j"],s["z"])
            cache[key]=edge
            register(lib,key,edge)
            new_edges+=1
            if new_edges%256==0:
                print("NORM19_NATIVE_NEW_CERTIFIED_EDGES",
                      new_edges,"TOTAL",len(cache),
                      "AT_N",s["n"],flush=True)
        if args.oracle_every and s["n"]%args.oracle_every==0:
            fast["direct_anchor"](s["j"],s["z"],s["a"],s["n"])
            print("NORM19_NATIVE_INDEPENDENT_GROSS_ORIENTATION_PASS",
                  s["n"],flush=True)
        if teich is not None and s["n"]%5410==0:
            i=S*s["n"]%P
            j,v=teich[i]
            assert s["j"]==j and int(V[j])==v,(
                "TRUE_16231POINT_TEICH_ORBIT_BRIDGE_FAILED",
                s["n"],i,s["j"],j)
            print("NORM19_NATIVE_COMPLETED_TEICH_ORBIT_BRIDGE_PASS",
                  s["n"],"I",i,"CLASS",j,"VALUE",v,flush=True)
        if s["n"]%args.checkpoint_every==0 or s["n"]==args.target_n:
            store(s,cache)
            print("NORM19_NATIVE_EXACT_PROGRESS",s["n"],
                  "OF",H-1,"MOMENTS",s["mom"],"EDGE_KEYS",len(cache),
                  "NEW_EDGES",new_edges,"EXACT_NATIVE_STEPS",s["hits"],
                  "SECONDS",round(time.monotonic()-t0,3),flush=True)
    assert s["n"]==args.target_n
    if s["n"]==H-1:
        assert sum(s["hist"].values())==H
        coeff=[(-3*4986*k)%P for k in s["mom"]]
        record=fast["sealed"]({
            "status":"NORM19_FULL_FINITE_RINGCLASS_CYCLIC_MOMENTS_PASS",
            "H":H,"p":P,"m":M,"w":W,
            "raw_moments_mod_p":s["mom"],
            "finite_theta_c0_c1_c2_mod_p":coeff,
            "checkpoint":str(CHECK),"certified_edges":str(EDGE),
            "boundary":"Finite theta layer; Iwasawa order and Sha still need proof"})
        fast["atomic_json"](FULL,record)
        print("NORM19_NATIVE_FULL_RINGCLASS_GROSS_MOMENTS_PASS",
              s["mom"],flush=True)
        print("NORM19_NATIVE_FULL_THETA_C012_MODP",coeff,flush=True)
        print("BOUNDARY_FINITE_LAYER_NOT_FULL_IWASAWA_ORDER",flush=True)
    else:
        print("NORM19_NATIVE_EXACT_PREFIX_PASS",s["n"]+1,
              "MOMENTS",s["mom"],"EDGE_KEYS",len(cache),flush=True)
        print("BOUNDARY_FULL_87809710_CLASS_SUM_NOT_YET_COMPUTED",flush=True)
    print("NORM19_NATIVE_HYBRID_DRIVER_PASS",args.target_n,
          "NEW_EDGES",new_edges,
          "SECONDS",round(time.monotonic()-t0,3),flush=True)

if __name__=="__main__":
    main()
