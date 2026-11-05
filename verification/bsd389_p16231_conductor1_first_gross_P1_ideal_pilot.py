#!/usr/bin/env python3
"""Authentic first Gross-point right ideal P_1^a for E389a1,K=sqrt(-3),p16231.

Requires the user-executed conductor-one local chart:
  ~/bsd389_p16231_conductor1_CM_base_and_local_split.json

Published CH definition:
 P_1^a=(r_1(a)*Rhat) intersect B,
 r_1(a)_p=[[1,a/p],[0,1]], r_1(a)_ell=1 for ell != p.

The global integral right ideal J(a)=p*P_1^a has local component
 [[p,a],[0,p]]*M2(Z_p) at p, and R_ell elsewhere.
Its basis is obtained as the kernel of two linear congruences mod p^2.
An independent inverse-matrix-basis computation checks the same lattice.

The RIGHT ideal must be transported to Brandt's fixed right order via
J(a)*I_base, where I_base is the right ideal with left order R_32.
The optional --classify searches the 33 exact right ideal classes.

NO giant theta sum, NO P_2^a construction and NO theta coefficient.
"""
import argparse
import hashlib
import json
from pathlib import Path
from sage.all import BrandtModule, QQ, ZZ, Zmod, matrix, vector, identity_matrix

P=16231
M=P*P
home=Path.home()
jsonpath=home/"bsd389_p16231_conductor1_CM_base_and_local_split.json"
raw=jsonpath.read_bytes()
data=json.loads(raw)
assert data["status"]=="CONDUCTOR1_CM_GLOBAL_AND_P_LOCAL_SPLIT_PASS"
assert data["p"]==P and data["modulus"]==M
assert data["selected_brandt_index"]==32
assert data["omega_split_roots"]==[49689135,213756225]

Bmod=BrandtModule(389,base_ring=QQ)
ideals=list(Bmod.right_ideals())
assert len(ideals)==33
base=ideals[32]
R=base.left_order()
quatalg=Bmod.quaternion_algebra()
basis=tuple(R.basis())
assert len(basis)==4
basis_map=matrix(QQ,4,4,
    lambda i,j: QQ(basis[j].coefficient_tuple()[i]))
flat=data["order_basis_images"]
assert len(flat)==4 and all(len(x)==4 for x in flat)
W=matrix(Zmod(M),4,4,lambda i,j: int(flat[j][i]))
assert int(W.det())%P!=0
assert int(W.det())%M == data["basis_map_determinant"]
W_inverse=W.inverse()
print("P1_CONDUCTOR1_SPLIT_CHART_LOADED_PASS",data["selected_brandt_index"],flush=True)
print("P1_CONDUCTOR1_SPLIT_CHART_SHA256",hashlib.sha256(raw).hexdigest(),flush=True)
# r_0(a)_p=[[1,a],[0,1]] belongs to GL2(Z_p), hence
# P_0^a is the base class 32 for every p-adic unit a.
# Its previously certified Brandt Hecke eigenvector entry is zero.
V=(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,
   0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0)
assert len(V)==33 and V[32]==0
print("CH_P0_ALL_UNITS_BASE_CLASS32_BRANDT_VALUE_ZERO_PASS",flush=True)

def coords(z):
    return basis_map.solve_right(vector(QQ,z.coefficient_tuple()))

def membership(z, h):
    t=coords(z)
    assert all(a.denominator()==1 for a in t)
    c=h.transpose().solve_right(vector(QQ,t))
    return all(x.denominator()==1 for x in c)

def hnf_basis(mat):
    return matrix(ZZ,mat).row_module().basis_matrix()

def build(a):
    a=int(a)%M
    assert a%P
    # For matrix X=[[x11,x12],[x21,x22]],
    # [[p,a],[0,p]]^(-1)*X has integral entries iff
    # p*x11-a*x21 = p*x12-a*x22 = 0 mod p^2.
    D=matrix(ZZ,2,4,lambda i,j:
             (P*int(flat[j][i])-a*int(flat[j][i+2]))%M)
    aug=D.augment(-M*identity_matrix(ZZ,2))
    K=aug.right_kernel().basis_matrix()
    assert K.nrows()==4 and K.ncols()==6
    H=hnf_basis(K[:,0:4])
    assert H.nrows()==H.ncols()==4
    assert abs(int(H.det()))==P**4
    assert all(int((D*H.row(i))[t])%M==0
               for i in range(4) for t in range(2))
    print("P1_CONGRUENCE_KERNEL_INDEX_P4_PASS",a,flush=True)

    # Independent construction: pull back an explicit basis of
    # [[p,a],[0,p]] M2(Z/p^2) plus p^2*R.
    local_targets=((P,0,0,0),(0,P,0,0),
                   (a,0,P,0),(0,a,0,P))
    generators=[]
    for t in local_targets:
        v=W_inverse*vector(Zmod(M),t)
        generators.append([ZZ(int(z)) for z in v])
    for j in range(4):
        generators.append([M*ZZ(i==j) for i in range(4)])
    H2=hnf_basis(matrix(ZZ,generators))
    assert H2.row_module()==H.row_module()
    print("P1_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS",a,flush=True)

    # Four global Z-basis elements of the right ideal.
    elems=[sum((ZZ(H[i,j])*basis[j] for j in range(4)),
               quatalg(0)) for i in range(4)]
    J=R.right_ideal(elems,is_basis=True)
    assert J.right_order()==R
    for z in elems:
        for b in basis:
            assert membership(z*b,H)
    print("P1_RIGHT_IDEAL_CLOSURE_16_PASS",a,flush=True)

    T=J*base
    assert T.right_order()==base.right_order()
    print("P1_GLOBAL_RIGHT_BRANDT_IDEAL_PASS",a,flush=True)
    return H,J,T

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--a",type=int,default=1,
                    help="p-adic unit a modulo p^2; default a=1")
    ap.add_argument("--teich-residue",type=int,
                    help="replace a by Teichmuller lift of residue mod p")
    ap.add_argument("--classify",action="store_true",
                    help="perform exact, potentially costly 33-class search")
    args=ap.parse_args()
    a=args.a
    if args.teich_residue is not None:
        residue=args.teich_residue%P
        assert residue
        a=pow(residue,P,M)
        assert pow(a,P-1,M)==1
        print("P1_TEICHMULLER_LIFT_PASS",residue,a,flush=True)
    H,J,T=build(a)
    res={
        "status":"P1_CONDUCTOR1_RIGHT_IDEAL_CONSTRUCTED_PASS",
        "p":P, "modulus":M, "a":int(a)%M,
        "source_local_chart_sha256":hashlib.sha256(raw).hexdigest(),
        "base_brandt_index":32,
        "basis_coordinate_HNF":[list(map(int,v)) for v in H.rows()],
        "norm_ideal_index":P**4,
        "scope":"One true conductor-one adelic P_1^a right ideal only"
    }
    if args.classify:
        hits=[]
        for k,ideal in enumerate(ideals):
            if ideal.is_right_equivalent(T):
                hits.append(k)
                print("P1_BRANDT_CLASS_CANDIDATE",k,flush=True)
        assert len(hits)==1, ("BRANDT_CLASS_UNIQUENESS_FAILED",hits)
        res["brandt_class"]=hits[0]
        print("P1_CONDUCTOR1_TRUE_GROSS_BRANDT_CLASS_PASS",a,hits[0],flush=True)
    else:
        print("P1_CLASSIFICATION_NOT_REQUESTED",flush=True)
    dest=home/("bsd389_p16231_gross_P1_a"+str(int(a)%M)+
               ("_class.json" if args.classify else "_ideal.json"))
    dest.write_text(json.dumps(res,indent=2)+"\n")
    print("P1_RESULT_JSON",dest,flush=True)
    print("P1_CONDUCTOR1_RIGHT_IDEAL_PILOT_PASS",flush=True)
    print("BOUNDARY_ONLY_P1_NOT_P2; NO_ACTUAL_THETA_MOMENT_YET",flush=True)

if __name__=="__main__":
    main()
