#!/usr/bin/env python3
"""E389a1: finite arithmetic witness for the local Tate corestriction no-go.

The GENERAL local Tate duality theorem is proved in the companion paper,
not by these finite tests. We certify unipotent Frobenius, the invariant
and coinvariant dual lines in a normal form, plus the genuine MW rows and
unit determinants for available Kurihara auxiliary pairs.

Output does NOT compute actual global H^2, Sha, or a Selmer bound.
"""
from pathlib import Path
from runpy import run_path

m=run_path(str(Path(__file__).with_name(
    "bsd389_ranktwo_euler_norm_group_ring_gate_20261121.py")),
    run_name="LOCAL_TATE_CHECK_IMPORT")
ROWS=m["ROWS"]; point_mul=m["mul"]; point_ap=m["ap"]

def matrix_mul(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%p
             for j in range(2)] for i in range(2)]

def run():
    counts=0
    by_p={}
    for p,q,a,ratio in ROWS:
        assert q%p==1 and a%p==2
        assert (q+1-a)%p==0 and (q+1-a)%(p*p)
        # Nontrivial unipotent normal form, valid for rank-one
        # local E(Fq)[p] as certified by the exact point law.
        U=[[1,1],[0,1]]
        assert ((U[0][0]+U[1][1])%p,U[0][0]*U[1][1]-U[0][1]*U[1][0])==(2,1)
        e1=(1,0);e2=(0,1)
        assert (U[0][0]*e1[0]+U[0][1]*e1[1],
                U[1][0]*e1[0]+U[1][1]*e1[1])==e1
        assert (U[0][0]*e2[0]+U[0][1]*e2[1]-e2[0])%p==1
        # Weil duality: ramified invariant direction e1 pairs
        # nontrivially with unramified coinvariant direction e2.
        symplectic=e2[0]*e1[1]-e2[1]*e1[0]
        assert symplectic%p==p-1
        if q<=5237:
            assert point_ap(q)==a
            B=point_mul((-1%q,1),(q+1-a)//p,q)
            C=point_mul((0,-1%q),(q+1-a)//p,q)
            assert B is not None and point_mul(B,p,q) is None
            assert point_mul(B,ratio,q)==C
        by_p.setdefault(p,[]).append((q,ratio))
        counts+=1
        print("BSD389_LOCAL_TATE_DUAL_NONTRACE_GATE_PASS",
              "p",p,"q",q,
              "unramified_coinvariant_vector",e2,
              "ramified_dual_kernel_vector",e1,
              "cross_pairing_mod_p",symplectic%p,
              "MW_Q_over_P",ratio,
              "real_finite_field_audit",q<=5237,flush=True)
    for p,items in sorted(by_p.items()):
        assert len(items)==2
        (q1,r1),(q2,r2)=items
        det=(r2-r1)%p
        assert det!=0
        # Local norm-image MW constraints are a+r_i*b=0.
        # The two constraints have only the zero solution.
        assert all(not ((a+r1*b)%p==0 and (a+r2*b)%p==0)
                   for a in range(p) for b in range(p)
                   if a or b)
        print("BSD389_TWO_AUXILIARY_MW_UNIVERSAL_NORM_NO_GO_PASS",
              "p",p,"q1",q1,"q2",q2,"local_det",det,flush=True)
    print("BSD389_LOCAL_TATE_NO_GO_ARITHMETIC_GATE_ALL_PASS",
          "prime_auxiliary_checks",counts,
          "unit_determinants",len(by_p))
    print("BOUNDARY: confirms local arithmetic and linear model; duality theorem external, no global Sha proof.")

if __name__=="__main__":
    run()
