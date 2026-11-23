#!/usr/bin/env python3
"""E=389a1, K=sqrt(-43), p=11: source-normalized 110 Gross P2 Brandt values.

This script requires Sage 10.x and the real BrandtModule(389). It verifies
the global quaternion algebra isomorphism, transports actual ideals into
Sage's Brandt right order with certified equivalences, checkpoints each
class, and evaluates the true n=1 quadratic theta coefficient mod 11.
No fake/archived Gross weights are accepted.

Example:
 sage -python verification/bsd389_Kminus43_p11_Gross_Brandt_110_sage.py --max-new 2
 sage -python verification/bsd389_Kminus43_p11_Gross_Brandt_110_sage.py --max-new 0
"""
import argparse
import json
import time
from pathlib import Path
from sage.all import QQ, ZZ, BrandtModule, matrix, vector

P=11
M=121
E_VEC=(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,
       2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0)
INV_CHART=((12,50,77,110),(98,5,70,23),(0,111,88,0),(0,120,14,0))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-new",type=int,default=2,
                    help="new classes to check in this run; 0=all remaining")
    ap.add_argument("--checkpoint",type=Path,
                    default=Path.home()/"bsd389_Kminus43_p11_Gross_Brandt_110.json")
    args=ap.parse_args()
    assert args.max_new>=0
    start=time.monotonic()
    BM=BrandtModule(389,base_ring=QQ)
    reps=list(BM.right_ideals())
    assert len(reps)==33 and len(E_VEC)==33
    B=BM.quaternion_algebra()
    x,y,_=B.gens()
    assert x*x==B(-2) and y*y==B(-389),("UNEXPECTED_BRANDT_MODEL",B)
    # Exact algebra isomorphism (-43,-389) -> (-2,-389):
    # i=(17x-7xy)/30 has i²=-43 and anticommutes with y.
    i=(17*x-7*x*y)/30
    assert i*i==B(-43) and i*y+y*i==B(0)
    omega=(1+i)/2
    J=(16*i+i*y)/43
    basis=(B(1),omega,J,omega*J)
    R=B.quaternion_order(list(basis))
    assert R.is_maximal()
    assert omega.reduced_norm()==11 and J.reduced_norm()==15
    assert J*omega==(1-omega)*J-16
    gram=matrix(ZZ,4,4,lambda a,b: ZZ((basis[a]*basis[b]).reduced_trace()))
    assert gram.det()==-389**2
    V=vector(QQ,E_VEC)
    for ell in (2,3):
        assert BM.hecke_matrix(ell)*V==ZZ(-2)*V
    print("REAL_BRANDT_PRIMITIVE_EIGENLINE_AND_MAXIMAL_ORDER_PASS",flush=True)

    # Each representative has common RIGHT order and a potentially
    # different LEFT maximal order. At least one left order is conjugate
    # to R by maximal-order type completeness of the Brandt ideal classes.
    print("SEARCH_EXACT_MAXIMAL_ORDER_CONJUGATOR",flush=True)
    base_index=None
    gamma=None
    for k,ref in enumerate(reps):
        try:
            candidate=R.isomorphism_to(ref.left_order(),conjugator=True)
            if candidate is None:
                continue
            trans=R.unit_ideal()*candidate
            if trans.right_order()!=ref.left_order():
                continue
            if not ((trans*ref).is_right_equivalent(ref)):
                continue
        except (ValueError,ArithmeticError,NotImplementedError,RuntimeError,TypeError):
            continue
        base_index=k
        gamma=candidate
        print("ACTUAL_BRANDT_ORDER_CONJUGATOR_PASS",k,str(gamma),flush=True)
        break
    assert base_index is not None,"NO_EXACT_MAXIMAL_ORDER_MATCH"
    base=reps[base_index]
    R0=base.right_order()

    # The four basis images in the fixed 11-adic chart are:
    # [[1,0],[0,1]], diag(11,111), [[5,23],[114,116]],
    # [[55,11],[70,50]].  INV_CHART is their exact inverse mod121.
    def coordinates(q):
        return [ZZ(sum(INV_CHART[r][j]*q[j] for j in range(4))%M)
                for r in range(4)]

    def actual_ideal(b):
        assert b%P
        h1=coordinates((b,0,1,0))
        h2=coordinates((0,b,0,1))
        rows=[h1,h2]+[[ZZ(M if r==s else 0) for s in range(4)]
                       for r in range(4)]
        H=matrix(ZZ,rows).row_module().basis_matrix()
        assert H.nrows()==H.ncols()==4 and abs(H.det())==M*M
        elements=[sum((H[r,c]*basis[c] for c in range(4)), B(0))
                  for r in range(4)]
        I=R.right_ideal(elements,is_basis=True)
        assert I.right_order()==R
        return I

    cp=args.checkpoint
    if cp.exists():
        payload=json.loads(cp.read_text(encoding="utf-8"))
        assert payload["status"] in ("PARTIAL_110_GENUINE_BRANDT",
                                     "ALL_110_GENUINE_BRANDT_WEIGHTS_COMPUTED")
        assert payload["base_index"]==base_index
        assert payload["gamma"]==str(gamma)
        done={int(k):v for k,v in payload["records"].items()}
        print("RESTART_FROM_CHECKPOINT",len(done),
              "status",payload["status"],flush=True)
    else:
        done={}

    def save():
        report={"status":"PARTIAL_110_GENUINE_BRANDT","curve":"389a1",
                "K_disc":-43,"p":11,"base_index":base_index,
                "gamma":str(gamma),
                "records":{str(k):v for k,v in sorted(done.items())},
                "boundary":"No theta certificate until all 110 authentic ideal classes are checked"}
        tmp=cp.with_suffix(cp.suffix+".tmp")
        tmp.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
        tmp.replace(cp)

    count=0
    for k in range(110):
        if k in done:
            continue
        b=pow(39,k,M)
        a=b*pow(45,-1,M)%M
        tau=pow(a%P,P,M)
        principal=a*pow(tau,-1,M)%M
        assert principal%P==1
        exponent=(principal-1)//P
        assert exponent==(k-4)%P
        I=actual_ideal(b)
        T=(I*gamma)*base
        assert T.right_order()==R0
        winner=None
        witness=None
        for idx,ref in enumerate(reps):
            ok,wit=ref.is_right_equivalent(T,certificate=True)
            if ok:
                assert wit*T==ref
                winner=idx
                witness=wit
                break
        assert winner is not None,("UNCLASSIFIED_GROSS_IDEAL",k)
        done[k]={"slope":int(b),"source_parameter":int(a),
                 "principal_exponent":int(exponent),"index":int(winner),
                 "brandt_weight":int(E_VEC[winner]),
                 "right_equivalence_witness":str(witness)}
        save()
        count+=1
        print("GENUINE_GROSS_BRANDT_VALUE_PASS",k,winner,int(E_VEC[winner]),
              "completed",len(done),"elapsed",round(time.monotonic()-start,2),
              flush=True)
        if args.max_new and count>=args.max_new:
            break
    if len(done)!=110:
        print("PARTIAL_ONLY_NOT_THETA_CERTIFICATE",len(done),"/110",flush=True)
        return
    assert set(done)==set(range(110))
    assert {done[k]["slope"] for k in done}=={a for a in range(M) if a%P}
    moments=[]
    for degree in (0,1,2):
        total=0
        for rec in done.values():
            exponent=rec["principal_exponent"]
            c=[1,exponent,exponent*(exponent-1)//2][degree]
            total+=c*rec["brandt_weight"]
        moments.append(total%P)
    # The P1 contribution to degree2 is zero mod11:
    # sum_i binomial(i,2)=binomial(11,3)=165.
    # a_11=-4: alpha=-4 mod11, -alpha^-2 = 2 mod11.
    c2=2*moments[2]%P
    report=json.loads(cp.read_text(encoding="utf-8"))
    report["status"]="ALL_110_GENUINE_BRANDT_WEIGHTS_COMPUTED"
    report["moments_mod11"]=moments
    report["theta2_mod11_up_to_JL_unit"]=c2
    report["theta2_unit"]=bool(c2)
    report["boundary"]="Theta2 does not supply the integral Selmer gamma-action or full BSD"
    tmp=cp.with_suffix(cp.suffix+".tmp")
    tmp.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    tmp.replace(cp)
    print("ALL_110_GENUINE_GROSS_BRANDT_CLASSES_CERTIFIED",flush=True)
    print("RAW_THETA_MOMENTS_MOD11",moments,flush=True)
    print("AUTHENTIC_THETA2_MOD11",c2,"UNIT",bool(c2),flush=True)
    print("BOUNDARY_NO_SEL_MER_GAMMA_ACTION_OR_FULL_BSD",flush=True)

if __name__=="__main__":
    main()
