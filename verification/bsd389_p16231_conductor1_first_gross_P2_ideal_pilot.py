#!/usr/bin/env python3
"""Actual conductor-one Gross point P_2^a via p^4 local splitting.

Starting with the Sage-certified conductor-one CM embedding into the
maximal left Brandt order R_32, construct the Hensel/Peirce split chart
mod p^4.  Define J_2(a)=p^2 P_2^a using exactly two congruences mod p^4.
Cross-check HNF with an independent inverse-matrix construction, certify
index p^8 and right ideal closure, and optionally classify its Brandt
right ideal class with an exact quaternion witness.

This is one point, NOT the full theta series or its T^2 coefficient.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path
from sage.all import BrandtModule, QQ, ZZ, Zmod, matrix, vector, identity_matrix

P=16231
P2=P*P
MOD=P**4
home=Path.home()
source=home/"bsd389_p16231_conductor1_CM_base_and_local_split.json"
raw=source.read_bytes()
data=json.loads(raw)
assert data["status"]=="CONDUCTOR1_CM_GLOBAL_AND_P_LOCAL_SPLIT_PASS"
assert data["p"]==P and data["modulus"]==P2
assert data["selected_brandt_index"]==32
BM=BrandtModule(389,base_ring=QQ)
reps=list(BM.right_ideals())
assert len(reps)==33
base=reps[32]
R=base.left_order()
B=BM.quaternion_algebra()
basis=tuple(R.basis())
assert len(basis)==4
coord_matrix=matrix(QQ,4,4,
    lambda i,j:QQ(basis[j].coefficient_tuple()[i]))
omega=sum((ZZ(z)*basis[i]
           for i,z in enumerate(data["omega_basis_coordinates"])),B(0))
assert omega in R and omega.reduced_trace()==-1
assert omega.reduced_norm()==1 and omega*omega+omega+B(1)==0

def hensel_p4(r2):
    r=int(r2)
    assert (r*r+r+1)%P2==0
    for n in (2,3):
        step=P**n
        quotient=((r*r+r+1)//step)%P
        deriv=(2*r+1)%P
        assert deriv!=0
        r=(r-quotient*pow(deriv,-1,P)*step)%(P**(n+1))
        assert (r*r+r+1)%(P**(n+1))==0
    return r

r0,r1=[hensel_p4(x) for x in data["omega_split_roots"]]
assert (r0+r1+1)%MOD==0
assert (r0*r1)%MOD==1
assert (r0-r1)%P
print("P2_HENSEL_SPLIT_ROOTS_P4_PASS",r0,r1,flush=True)

def coords(x):
    return coord_matrix.solve_right(vector(QQ,list(x.coefficient_tuple())))

def red(t):
    t=QQ(t)
    n=int(t.numerator())%MOD
    d=int(t.denominator())%MOD
    assert d%P,("NON_P_INTEGRAL",t)
    return n*pow(d,-1,MOD)%MOD

def zero(x):
    return all(red(c)==0 for c in coords(x))

def same(x,y):
    return zero(x-y)

e=(omega-B(r1))/(r0-r1)
f=B(1)-e
assert same(e*e,e) and same(f*f,f)
assert zero(e*f) and zero(f*e)
print("P2_P4_LOCAL_IDEMPOTENTS_PASS",flush=True)

i,j=list(map(int,data["matrix_unit_basis_indices"]))
x=e*basis[i]*f
y0=f*basis[j]*e
scale=red((x*y0).reduced_trace())
assert scale%P
y=pow(scale,-1,MOD)*y0
assert same(x*y,e) and same(y*x,f)
assert zero(x*x) and zero(y*y)
assert same(e*x,x) and same(x*f,x)
assert same(f*y,y) and same(y*e,y)
print("P2_P4_LOCAL_MATRIX_UNITS_PASS",i,j,scale,flush=True)

ring=Zmod(MOD)
def tr(z):
    return red(z.reduced_trace())

def image(z):
    return matrix(ring,2,2,[
        tr(e*z*e),tr(e*z*y),tr(x*z*e),tr(f*z*f)
    ])

eye=matrix(ring,2,2,[1,0,0,1])
assert image(B(1))==eye
assert image(omega)==matrix(ring,2,2,[r0,0,0,r1])
images=[image(b) for b in basis]
for t in range(4):
    assert int(images[t].trace())==red(basis[t].reduced_trace())
    assert int(images[t].det())==red(basis[t].reduced_norm())
    for u in range(4):
        assert image(basis[t]*basis[u])==images[t]*images[u]
print("P2_P4_LOCAL_16_PRODUCTS_PASS",flush=True)

flat=[[int(m[0,0]),int(m[0,1]),int(m[1,0]),int(m[1,1])]
      for m in images]
W=matrix(ring,4,4,lambda i,j:flat[j][i])
det=int(W.det())%MOD
assert det%P
assert det%P2==int(data["basis_map_determinant"])%P2
for old,new in zip(data["order_basis_images"],flat):
    assert all(int(a)%P2==int(b)%P2 for a,b in zip(old,new))
print("P2_P4_SPLIT_LIFTS_CERTIFIED_P2_CHART_PASS",det,flush=True)

V=(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,
   0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0)
assert len(V)==33 and V[32]==0

def hnf_rows(mat):
    return matrix(ZZ,mat).row_module().basis_matrix()

def is_member(q,H):
    z=coords(q)
    assert all(t.denominator()==1 for t in z)
    coefficients=H.transpose().solve_right(vector(QQ,z))
    return all(t.denominator()==1 for t in coefficients)

def build(a):
    a=int(a)%MOD
    assert a%P,("A_NOT_UNIT",a)
    print("P2_GROSS_UNIT_PARAMETER",a,flush=True)
    # J_2(a)_p=[[p^2,a],[0,p^2]] M2(Z_p);
    # two congruences p^2*X11-a*X21=0, similarly column2 mod p^4.
    D=matrix(ZZ,2,4,lambda i,j:
             (P2*flat[j][i]-a*flat[j][i+2])%MOD)
    augmented=D.augment(-MOD*identity_matrix(ZZ,2))
    kernel=augmented.right_kernel().basis_matrix()
    assert kernel.nrows()==4 and kernel.ncols()==6
    H=hnf_rows(kernel[:,0:4])
    assert H.nrows()==H.ncols()==4
    assert abs(int(H.det()))==P**8
    for k in range(4):
        assert all(int(t)%MOD==0 for t in D*H.row(k))
    print("P2_CONGRUENCE_KERNEL_INDEX_P8_PASS",flush=True)

    # Independent preimage of t*E11,t*E12,t*E21,t*E22,
    # plus p^4 times the full maximal order.
    targets=((P2,0,0,0),(0,P2,0,0),
             (a,0,P2,0),(0,a,0,P2))
    inv=W.inverse()
    generators=[]
    for t in targets:
        z=inv*vector(ring,t)
        generators.append([ZZ(int(v)) for v in z])
    for k in range(4):
        generators.append([MOD*ZZ(k==j) for j in range(4)])
    H2=hnf_rows(matrix(ZZ,generators))
    assert H2.row_module()==H.row_module()
    print("P2_INDEPENDENT_LOCAL_MATRIX_PREIMAGE_PASS",flush=True)

    elements=[sum((ZZ(H[k,j])*basis[j] for j in range(4)),B(0))
              for k in range(4)]
    J=R.right_ideal(elements,is_basis=True)
    assert J.right_order()==R
    for z in elements:
        for b in basis:
            assert is_member(z*b,H)
    print("P2_RIGHT_IDEAL_CLOSURE_16_PASS",flush=True)
    T=J*base
    assert T.right_order()==base.right_order()
    print("P2_GLOBAL_RIGHT_BRANDT_IDEAL_PASS",flush=True)
    return H,T

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--a",type=int,default=1)
    parser.add_argument("--classify",action="store_true")
    args=parser.parse_args()
    a=args.a%MOD
    H,T=build(a)
    report={
       "status":"P2_CONDUCTOR1_RIGHT_IDEAL_PILOT_PASS",
       "base_brandt_index":32,"p":P,"p_power":4,
       "a":a,"source_local_chart_sha256":hashlib.sha256(raw).hexdigest(),
       "local_omega_roots_p4":[r0,r1],
       "local_order_basis_map_p4":flat,
       "local_order_basis_map_determinant_p4":det,
       "lattice_basis_HNF":[list(map(int,z)) for z in H.rows()],
       "ideal_index":P**8,
       "scope":"Single true conductor-one Gross P2 point; not a theta series"
    }
    if args.classify:
        start=time.monotonic()
        winner=None
        for j,ideal in enumerate(reps):
            print("P2_CLASSIFY_TESTING",j,"OF",len(reps),flush=True)
            yes,wit=ideal.is_right_equivalent(T,certificate=True)
            if yes:
                assert wit*T==ideal
                winner=j
                report["brandt_class"]=j
                report["right_equivalence_witness"]=str(wit)
                report["brandt_eigenvector_value"]=int(V[j])
                print("P2_RIGHT_IDEAL_EQUALITY_WITNESS_PASS",j,flush=True)
                print("P2_CONDUCTOR1_TRUE_GROSS_BRANDT_CLASS_PASS",a,j,flush=True)
                print("P2_TRUE_GROSS_BRANDT_VALUE_PASS",a,int(V[j]),flush=True)
                break
        assert winner is not None,"NO_BRANDT_CLASS_MATCH"
        print("P2_CLASSIFY_ELAPSED_SECONDS",
              round(time.monotonic()-start,3),flush=True)
    else:
        print("P2_CLASSIFICATION_NOT_REQUESTED",flush=True)
    output=home/("bsd389_p16231_gross_P2_a"+str(a)+
                 ("_class" if args.classify else "_ideal")+".json")
    output.write_text(json.dumps(report,indent=2)+"\n")
    print("P2_RESULT_JSON",output,flush=True)
    print("P2_CONDUCTOR1_RIGHT_IDEAL_PILOT_PASS",flush=True)
    print("BOUNDARY_ONE_P2_POINT_NOT_THETA_DERIVATIVE_OR_SHA_PROOF",flush=True)

if __name__=="__main__":
    main()
