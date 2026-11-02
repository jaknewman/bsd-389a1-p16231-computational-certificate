#!/usr/bin/env python3
"""Targeted, inexpensive mod-2 rank scan of true integral level-389 Hecke operators.

The USER'S GENUINE 2026-11-02 Sage run proved:
  * lattice rank 33;
  * Smith determinant for stack (T2+2, T3+2) = 2;
  * rank over F2 of that stack = 31; other odd-p ranks = 32.
Hence coker(A^t) = Z (+) Z/2 for THIS FIXED stack.
This script asks the ONLY remaining congruence question:
do any further good-prime integral Hecke matrices T_l-a_l(E)
increase the F2 rank to 32 (the upper bound from the common
primitive integer E-eigenvector)?

Reads and authenticates the user's genuine Smith JSON checksum, then
reconstructs its rank/provenance, and checks additional primes ell<=61
without recomputing any Smith matrices. The Sage Sturm bound at
weight 2 level 389 is 65; the program prints this as context and does
NOT claim that testing Hecke primes <=61 alone exhausts all operators
on the entire integral modular-symbol lattice, or all modular symbols
in characteristic 2. A complete structural p=2 argument requires
care with the +/- signs and integral base change in characteristic 2.

Exact scope: congruence eigenspace ONLY, never Sha/Fitt2/Kurihara.

Run:
  python -u verification/bsd389_hecke_mod2_exception_targeted_scan.py \
    --output ~/bsd389_hecke_mod2_exception_scan.json --max-prime 61
"""
import argparse
import hashlib
import json
from pathlib import Path

from sage.all import (
    ZZ, QQ, GF, ModularSymbols, EllipticCurve, matrix,
    identity_matrix, vector, prime_range,
)
from sage.modular.dims import sturm_bound

N = 389
DIM = 33
EXPECTED_SHA = "86e79229d1c60d38ec59ecd8776c0c471716a1ffdf1098d46d58a8a59253f02a"
PREVIOUS_PRIMES = (2,3,5)


def load_pinned(path):
    raw=path.read_bytes()
    o=json.loads(raw)
    canonical=json.dumps(o,sort_keys=True,separators=(",", ":")).encode()
    assert raw==canonical+b"\n", "NONCANONICAL_SMITH_JSON"
    digest=hashlib.sha256(canonical).hexdigest()
    assert digest==EXPECTED_SHA,("USER_SMITH_JSON_SHA256_MISMATCH",digest)
    assert o["curve"]=="389a1"
    assert o["level"]==N
    assert o["ambient_integral_lattice_dim"]==DIM
    assert o["final_exact_gcd_of_all_rank32_minors"]=="2"
    assert [s["hecke_prime"] for s in o["steps"]]==list(PREVIOUS_PRIMES)
    for s in o["steps"]:
        assert s["probes"]["2"]["rank"]==31
    print("HECKE_MOD2_ORIGINAL_USER_SMITH_SHA256_PASS",digest,flush=True)
    return o


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--baseline",type=Path,default=Path.home()/
                    "bsd389_hecke_smith_refinement.json")
    ap.add_argument("--output",type=Path,default=Path.home()/
                    "bsd389_hecke_mod2_exception_scan.json")
    ap.add_argument("--max-prime",type=int,default=61)
    ap.add_argument("--all-primes",action="store_true",
                    help="keep checking after kernel becomes one dimensional")
    args=ap.parse_args()
    assert args.max_prime>=5

    baseline=load_pinned(args.baseline)
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    assert int(E.conductor())==N
    M=ModularSymbols(N,2,sign=+1,base_ring=QQ)
    assert int(M.dimension())==DIM
    assert int(M.integral_structure().rank())==DIM
    bound=int(sturm_bound(N,2))
    assert bound==65
    print("HECKE_MOD2_STURM_BOUND_CONTEXT",bound,
          "cuspidal_forms_not_automatic_full_mod2_base_change",
          flush=True)
    F=GF(2)
    v=vector(F,baseline["primitive_integer_kernel_vector"])
    assert len(v)==DIM and any(v)
    stacked=matrix(F,0,DIM)
    steps=[]
    for ell in prime_range(args.max_prime+1):
        ell=int(ell)
        if ell==N:
            continue
        A=matrix(ZZ,M.integral_hecke_matrix(ell))
        assert A.nrows()==A.ncols()==DIM
        A-=ZZ(E.ap(ell))*identity_matrix(ZZ,DIM)
        Ab=A.change_ring(F)
        assert Ab*v==vector(F,DIM),("HEKKE_NOT_SAME_INTEGRAL_EIGENVECTOR",ell)
        stacked=stacked.stack(Ab)
        rank=int(stacked.rank())
        assert 31 <= rank <= 32,("BAD_MOD2_RANK",ell,rank)
        if ell in PREVIOUS_PRIMES:
            assert rank==31,("INCONSISTENT_REAL_USER_SMITH_BASELINE",ell,rank)
        print("HECKE_MOD2_PRIME_EIGENRANK",
              "ell",ell,"ap",int(E.ap(ell)),
              "rank",rank,"kernel_dim",DIM-rank,flush=True)
        steps.append({"ell":ell,"a_ell":int(E.ap(ell)),
                      "mod2_rank":rank,"kernel_dim":DIM-rank})
        if rank==32 and not args.all_primes:
            print("HECKE_MOD2_EXCEPTION_ELIMINATED_FOR_FIXED_STACK_PASS",
                  "by_prime",ell,"odd_prime_results_unchanged",flush=True)
            break
    final=steps[-1]
    if final["mod2_rank"]==31:
        print("HECKE_MOD2_EXTRA_EIGENVECTOR_PERSISTS_WITH_TESTED_PRIMES",
              "largest_checked_prime",final["ell"],flush=True)
    else:
        print("HECKE_MOD2_COMMON_KERNEL_DIM1_PASS",
              "largest_checked_prime",final["ell"],flush=True)
    report={
        "curve":"389a1",
        "baseline_sha256":EXPECTED_SHA,
        "sturm_bound_weight2_level389_cuspidal":bound,
        "integral_lattice_dimension":DIM,
        "tested":steps,
        "final_F2_rank":final["mod2_rank"],
        "final_F2_kernel_dimension":final["kernel_dim"],
        "odd_prime_Fp_kernel_dimension":1,
        "scope":("Fixed level-389 integral modular-symbol Hecke matrices, "
                 "not Sha/Fitting, not full characteristic-2 modular-symbol "
                 "base change, not a proof of complete BSD.")
    }
    encoded=json.dumps(report,sort_keys=True,separators=(",", ":")).encode()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(encoded+b"\n")
    digest=hashlib.sha256(encoded).hexdigest()
    print("HECKE_MOD2_SCAN_CANONICAL_JSON_SHA256",digest,flush=True)
    print("HECKE_MOD2_SCAN_REPORT",args.output,flush=True)
    print("BOUNDARY_HEKKE_CONGRUENCE_ONLY_NOT_SHA_FITTING_OR_BSD",flush=True)


if __name__=="__main__":
    main()
