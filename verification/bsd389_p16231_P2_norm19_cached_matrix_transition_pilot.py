#!/usr/bin/env python3
"""Fast exact norm19 Gross P2 oriented recurrence with finite local-state cache.

THE ALGEBRAIC SPEEDUP:
For I_j, R_j=left_order(I_j), q=m*omega in R_j, define
D(q)=R_j.left_ideal([q-9,19]).  This depends only on
(j, q basis coordinates modulo 19), at most 33*380=12540 keys.

For each NEW key, compute N=conjugate(D(q))*I_j, find j', beta with
beta*N=I_j'.  For ANY q with that key the exact actual Gross
neighbor is Tnext=(g(q)/19)*N, g(q)=5+3q/m.  Since g(q) COMMUTES
with q, its normalized CM embedding is beta*q*beta^-1.
Store the exact 4x4 rational basis-coordinate matrix of conjugation
by beta, as integer numerator matrix and common denominator.
Then every CACHE HIT is FOUR short integer dot-products -- no new
quaternionic ideal, classification or Sage matrix solve.

First pilot bootstraps from the USER PASS norm19 checkpoint n=5410
(or a prior fast checkpoint), compares slow quaternionic transitions,
checks independently built direct Gross anchors, and atomically
checkpoints the fast state and cached exact edge witnesses.

Before claiming full H=87809710 cycle, ALL steps must actually run.
"""
import argparse
import hashlib
import json
import os
import runpy
import time
from collections import Counter
from functools import reduce
from math import lcm
from pathlib import Path

ROOT=Path(__file__).resolve().parent
stream=runpy.run_path(str(ROOT/"bsd389_p16231_P2_norm19_cyclic_checkpoint_stream.py"),
                      run_name="FAST_GROSS_IMPORT")
E=stream["E"]
P=stream["P"];M=stream["M"];w=stream["w"];S=stream["S"];H=stream["H"]
B=E["B"];reps=E["reps"];V=E["V"];basis=E["basis"]
QQ=E["QQ"]; ZZ=E["ZZ"]; vector=E["vector"]; matrix=E["matrix"]
assert (P,M,w,S,H)==(16231,263445361,138112843,10816,87809710)
assert len(reps)==len(V)==33
ORDER=19
MAX_KEYS=33*ORDER*(ORDER+1)
HOME=Path.home()
SOURCE_CHECKPOINT=stream["CHECKPOINT"]
CACHE_PATH=HOME/"bsd389_p16231_norm19_cached_matrix_edges.json"
FAST_PATH=HOME/"bsd389_p16231_norm19_cached_fast_checkpoint.json"
BONE=(B(1),)+tuple(B.gens())
assert len(BONE)==4
source_sha=hashlib.sha256(
   (ROOT/"bsd389_p16231_P2_norm19_reduced_oriented_chain_moment_pilot.py").read_bytes()
).hexdigest()

def hash_object(o):
    return hashlib.sha256(
        json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def sealed(o):
    return dict(o,sha256=hash_object(o))

def validate_seal(o):
    assert o["sha256"]==hash_object({k:v for k,v in o.items() if k!="sha256"})

def atomic_json(path,data):
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(data,sort_keys=True,separators=(",",":"))+"\n")
    os.replace(tmp,path)

def key_for(j,z):
    return str(int(j))+":"+(",".join(str(int(t)%ORDER) for t in z))

def quat_from_rationals(nums):
    return sum((QQ(x)*b for x,b in zip(nums,BONE)),B(0))

def cm_checks(j,z):
    assert len(z)==4 and 0<=j<33
    # This inexpensive exact quaternion audit is run on NEW keys,
    # on slow/direct anchors, and on checkpoint restore.
    q=E["element"](j,z)
    assert q in reps[j].left_order()
    assert q.reduced_trace()==-M and q.reduced_norm()==M*M
    assert q*q+M*q+B(M*M)==0
    return q

def index_squared(D,R):
    mat=lambda b: matrix(QQ,[list(x.coefficient_tuple()) for x in b])
    return abs(mat(D.basis()).det()/mat(R.basis()).det())

def validate_edge(j,z,edge,check_new=False):
    q=cm_checks(j,z)
    R=reps[j].left_order()
    D=R.left_ideal([q-B(9),B(19)])
    assert index_squared(D,R)==361
    N=D.conjugate()*reps[j]
    k=int(edge["dest"])
    assert 0<=k<33
    beta=quat_from_rationals(edge["beta"])
    assert beta*N==reps[k],("CERTIFIED_EDGE_IDEAL_EQ_FAILED",j,k)
    d=int(edge["den"])
    nums=edge["matrix_num"]
    assert d>0 and len(nums)==4 and all(len(row)==4 for row in nums)
    columns=[]
    for b in basis[j]:
        t=beta*b*beta.inverse()
        v=E["coord_mats"][k].solve_right(vector(QQ,t.coefficient_tuple()))
        columns.append(v)
    for i in range(4):
        for c in range(4):
            assert QQ(nums[i][c])/d==columns[c][i]
    print("NORM19_CACHE_CERTIFIED_EDGE_PASS",j,key_for(j,z),"TO",k,
          flush=True) if check_new else None
    return beta

def construct_edge(j,z):
    q=cm_checks(j,z)
    R=reps[j].left_order()
    D=R.left_ideal([q-B(9),B(19)])
    assert index_squared(D,R)==361
    N=D.conjugate()*reps[j]
    found=None
    for k,ideal in enumerate(reps):
        yes,beta=ideal.is_right_equivalent(N,certificate=True)
        if yes:
            assert beta*N==ideal
            found=(k,beta)
            break
    assert found is not None
    k,beta=found
    beta_inv=beta.inverse()
    cols=[]
    for source_b in basis[j]:
        v=E["coord_mats"][k].solve_right(
            vector(QQ,(beta*source_b*beta_inv).coefficient_tuple()))
        cols.append(v)
    denominators=[int(cols[c][i].denominator())
                  for c in range(4) for i in range(4)]
    d=lcm(*denominators)
    nums=[[int(d*cols[c][i]) for c in range(4)] for i in range(4)]
    edge={"dest":int(k),"den":int(d),"matrix_num":nums,
          "beta":[str(QQ(t)) for t in beta.coefficient_tuple()]}
    validate_edge(j,z,edge,check_new=False)
    return edge

def mat_step(j,z,cache):
    key=key_for(j,z)
    miss=key not in cache
    if miss:
        assert len(cache)<MAX_KEYS,("UNEXPECTED_TOO_MANY_MOD19_CM_STATES",len(cache))
        cache[key]=construct_edge(j,z)
    edge=cache[key]
    den=edge["den"];num=edge["matrix_num"]
    values=[sum(num[r][c]*z[c] for c in range(4))
            for r in range(4)]
    assert all(x%den==0 for x in values),("CM_MATRIX_NOT_INTEGRAL",key)
    znew=tuple(x//den for x in values)
    return int(edge["dest"]),znew,miss

def verify_oriented(j,z,j2,z2):
    if j!=j2:
        return False
    if tuple(z)==tuple(z2):
        return True
    if j!=32:
        return False
    # R32 has six units (±1,±omega,±omega²); units of
    # reduced norm 1 act on the oriented embedding.
    q=cm_checks(j,z)
    qb=cm_checks(j2,z2)
    omega=E["omega"]
    return any(u*q*u.inverse()==qb
               for u in (B(1),omega,omega*omega))

def read_source_state():
    o=json.loads(SOURCE_CHECKPOINT.read_text())
    j,q,n=stream["validate_checkpoint"](o)
    return j,tuple(int(v) for v in E["coords"](j,q)),n,int(o["a"]), \
           list(o["moments_modp"]),Counter(o["histogram"]), \
           int(o["max_abs_q_coordinate"]),o["data_sha256"]

def read_cache():
    if not CACHE_PATH.exists():
        return {}
    data=json.loads(CACHE_PATH.read_text())
    validate_seal(data)
    assert data["source_sha256"]==source_sha
    assert data["p"]==P and data["m"]==M and data["order"]==ORDER
    rows=data["edges"]
    assert len(rows)<=MAX_KEYS
    for key,edge in rows.items():
        assert len(key.split(":"))==2
        assert len(edge["matrix_num"])==4 and edge["den"]>0
        assert len(edge["beta"])==4 and 0<=edge["dest"]<33
    print("NORM19_CACHED_MATRIX_EDGES_RESTORED",len(rows),flush=True)
    return rows

def save_cache(cache):
    data=sealed({"status":"NORM19_CACHED_MATRIX_EDGES",
                 "p":P,"m":M,"order":ORDER,
                 "source_sha256":source_sha,
                 "edges":cache})
    atomic_json(CACHE_PATH,data)
    print("NORM19_CACHED_MATRIX_EDGE_TABLE_SAVED",len(cache),
          data["sha256"],flush=True)

def save_fast(j,z,n,a,mom,hist,maxcoord,origin,cache):
    o=sealed({
        "status":"NORM19_MATRIX_CACHED_FAST_PREFIX_PASS",
        "p":P,"m":M,"w":w,"S":S,"H":H,
        "source_sha256":source_sha,
        "origin_checkpoint":origin,
        "last_n":n,"a":int(a),"class":int(j),
        "q_coordinates":[int(x) for x in z],
        "moments_modp":list(map(int,mom)),
        "histogram":dict(hist),"max_abs_q_coordinate":int(maxcoord),
        "edge_cache_count":len(cache),
        "scope":"Certified prefix only; not the full theta"})
    save_cache(cache)
    atomic_json(FAST_PATH,o)
    print("NORM19_FAST_CACHED_CHECKPOINT_PASS",n,o["sha256"],
          "EDGES",len(cache),flush=True)

def bootstrap():
    if FAST_PATH.exists():
        o=json.loads(FAST_PATH.read_text())
        validate_seal(o)
        assert o["status"]=="NORM19_MATRIX_CACHED_FAST_PREFIX_PASS"
        assert o["p"]==P and o["m"]==M and o["w"]==w and o["S"]==S and o["H"]==H
        assert o["source_sha256"]==source_sha
        j=int(o["class"]); z=tuple(int(a) for a in o["q_coordinates"])
        n=int(o["last_n"])
        assert int(o["a"])==pow(w,n,M)
        cm_checks(j,z)
        assert sum(o["histogram"].values())==n+1
        print("NORM19_FAST_CACHED_CHECKPOINT_RESTORED",n,flush=True)
        return j,z,n,int(o["a"]),list(o["moments_modp"]),Counter(o["histogram"]), \
               int(o["max_abs_q_coordinate"]),o["origin_checkpoint"]
    j,z,n,a,mom,hist,maxcoord,digest=read_source_state()
    assert n>=128
    print("NORM19_FAST_BOOTSTRAP_FROM_USER_SLOW_STREAM_PASS",n,
          "CLASS",j,flush=True)
    return j,z,n,a,mom,hist,maxcoord,digest

def audit_slow(j,z,newj,newz,n):
    q=cm_checks(j,z)
    sj,sq,_=E["step"](j,q)
    sz=tuple(int(t) for t in E["coords"](sj,sq))
    assert sj==newj,("SLOW_BRANDT_MISMATCH",n,sj,newj)
    assert verify_oriented(newj,newz,sj,sz),(
        "SLOW_ORIENTED_CM_MISMATCH",n,newj,newz,sz)
    print("NORM19_FAST_VS_SLOW_EXACT_ORIENTED_PASS",n,newj,flush=True)

def direct_anchor(j,z,a,n):
    k,qd,_=E["normalize_anchor"](a)
    kd=tuple(int(t) for t in E["coords"](k,qd))
    assert verify_oriented(j,z,k,kd),(
        "FAST_DIRECT_P2_ANCHOR_MISMATCH",n,j,k,z,kd)
    print("NORM19_FAST_DIRECT_GROSS_ANCHOR_PASS",
          n,"CLASS",j,flush=True)
    if n==P:
        assert a==121898074 and j==24
        print("NORM19_FAST_TEICH_P_STEP_PASS",n,
              "A",a,"CLASS",j,flush=True)

def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--target-n",type=int,default=7168)
    pa.add_argument("--audit-every",type=int,default=128)
    pa.add_argument("--oracle-every",type=int,default=512)
    pa.add_argument("--checkpoint-every",type=int,default=256)
    args=pa.parse_args()
    assert 0<=args.target_n<H
    assert args.checkpoint_every>0
    assert args.audit_every>=0 and args.oracle_every>=0
    t0=time.monotonic()
    cache=read_cache()
    j,z,n,a,mom,hist,maxcoord,origin=bootstrap()
    assert args.target_n>=n,("TARGET_IS_BEFORE_EXISTING_FAST_CHECKPOINT",n)
    # Verify stored cache entries lazily on the FIRST use after restore,
    # not just their JSON seal; a persisted witness must be a real ideal
    # equality, not mere source text.
    restored=set(cache)
    verified=set()
    misses=0
    hits=0
    for k in range(n+1,args.target_n+1):
        oldj,oldz=j,z
        ck=key_for(oldj,oldz)
        if ck in restored and ck not in verified:
            validate_edge(oldj,oldz,cache[ck])
            verified.add(ck)
        j,z,miss=mat_step(oldj,oldz,cache)
        if miss: misses+=1
        else: hits+=1
        a=(a*w)%M
        assert a==pow(w,k,M)
        i=(S*k)%P
        val=int(V[j])
        moments=(1,i,i*(i-1)//2)
        mom=[(mom[r]+moments[r]*val)%P for r in range(3)]
        hist[str(j)]+=1
        maxcoord=max(maxcoord,max(abs(v) for v in z))
        if args.audit_every and k%args.audit_every==0:
            audit_slow(oldj,oldz,j,z,k)
        if args.oracle_every and (
            k%args.oracle_every==0 or k==args.target_n):
            direct_anchor(j,z,a,k)
        if k%args.checkpoint_every==0 or k==args.target_n:
            cm_checks(j,z)
            save_fast(j,z,k,a,mom,hist,maxcoord,origin,cache)
            print("NORM19_FAST_CACHED_PROGRESS",k,
                  "MOMENTS",mom,"CACHE_HITS",hits,"NEW_EDGES",misses,
                  "TOTAL_EDGES",len(cache),
                  "MAX_COORD",maxcoord,
                  "ELAPSED",round(time.monotonic()-t0,3),flush=True)
    if args.target_n==n:
        print("NORM19_FAST_ALREADY_AT_TARGET",n,flush=True)
    print("NORM19_FAST_CACHED_MATRIX_PILOT_PASS",
          args.target_n,"CACHE_HITS",hits,"NEW_EDGES",misses,
          "SECONDS",round(time.monotonic()-t0,3),flush=True)
    print("NORM19_FAST_CACHED_EDGE_UPPER_BOUND",MAX_KEYS,flush=True)
    print("BOUNDARY_PREFIX_NOT_FULL_RINGCLASS_THETA",flush=True)
    print("BOUNDARY_SHA_AND_BSD_NOT_PROVED",flush=True)

if __name__=="__main__":
    main()
