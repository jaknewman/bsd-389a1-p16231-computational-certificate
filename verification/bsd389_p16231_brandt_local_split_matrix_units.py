#!/usr/bin/env python3
"""Exact Sage construction of R_i tensor Z/p^2 -> M2(Z/p^2) at p=16231.

Uses one *actual* stage14 CM embedding q, with q^2-q+2107=0 and
omega=(q-27)/53 satisfying omega^2+omega+1=0.  The two known Hensel
roots of omega modulo p^2 give idempotents e and f in the local order.

Find off-diagonal matrix units x=e*b_i*f, y=f*b_j*e (normalized), and
check all four matrix-unit relations, a unimodular representation of
the integral quaternion maximal order, and all 16 product identities
on the selected integral Z-basis.  Outputs a small JSON certificate.

THIS IS LOCAL SPLITTING ONLY: does not construct p^2-conductor optimal
embeddings or Gross-point classes, theta derivatives, or Sha bounds.

Run inside activated Sage:
  python -u verification/bsd389_p16231_brandt_local_split_matrix_units.py
"""
import hashlib
import json
from pathlib import Path
from sage.all import BrandtModule, QQ, ZZ, Zmod, matrix, vector

P=16231
MOD=P*P
R0=49689135
R1=213756225
assert (R0*R0+R0+1)%MOD==0
assert (R1*R1+R1+1)%MOD==0
assert (R0+R1+1)%MOD==0
assert (R0*R1)%MOD==1
assert ((R0-R1)%P)!=0

home=Path.home()
source=home/"bsd389_chi53_stage14_orbit19.json"
raw=source.read_bytes()
data=json.loads(raw)
assert data["status"]=="ORBIT_18_PASS"
rows=data["steps"]
assert len(rows)==18
row=rows[0]
idx=int(row["index"])

BM=BrandtModule(389,base_ring=QQ)
reps=list(BM.right_ideals())
assert len(reps)==33 and 0<=idx<33
B=BM.quaternion_algebra()
R=reps[idx].left_order()
basis=tuple(R.basis())
assert len(basis)==4
basis_coords=matrix(QQ,4,4,
    lambda i,j: QQ(basis[j].coefficient_tuple()[i]))

def coords(q):
    return basis_coords.solve_right(vector(QQ,list(q.coefficient_tuple())))

def red(q):
    q=QQ(q)
    n=int(q.numerator())%MOD
    d=int(q.denominator())%MOD
    assert d%P!=0, ("NOT_P_INTEGRAL",q)
    return n*pow(d,-1,MOD)%MOD

def localzero(q):
    return all(red(t)==0 for t in coords(q))

def same(q,w):
    return localzero(q-w)

q=sum((ZZ(z)*basis[j] for j,z in enumerate(row["coefficients"])),B(0))
assert q in R
assert q.reduced_trace()==1 and q.reduced_norm()==2107
omega=(q-B(27))/53
assert omega*omega+omega+1==0

# Idempotents in R tensor Z/p^2 induced by the split embedding of K.
e=(omega-B(R1))/(R0-R1)
f=B(1)-e
assert same(e*e,e)
assert same(f*f,f)
assert localzero(e*f)
assert localzero(f*e)
assert red(e.reduced_trace())==1
assert red(f.reduced_trace())==1
print("P16231_LOCAL_IDEMPOTENTS_HENSEL_PASS",idx,flush=True)

# Construct E12, E21 using the actual integral left-order basis.
selected=None
for i,bi in enumerate(basis):
    x=e*bi*f
    for j,bj in enumerate(basis):
        y0=f*bj*e
        c=red((x*y0).reduced_trace())
        if c%P:
            y=pow(c,-1,MOD)*y0
            if (same(x*y,e) and same(y*x,f)
                and same(e*x,x) and same(x*f,x)
                and same(f*y,y) and same(y*e,y)
                and localzero(x*x) and localzero(y*y)):
                selected=(i,j,x,y,c)
                break
    if selected is not None:
        break
assert selected is not None, "NO_LOCAL_MATRIX_UNITS_FOUND"
i,j,x,y,c=selected
print("P16231_LOCAL_E12_E21_MATRIX_UNITS_PASS",i,j,c,flush=True)

ring=Zmod(MOD)
def tr(z):
    return red(z.reduced_trace())

def image(z):
    # E11=e, E12=x, E21=y, E22=f.
    # tr(e*z*y) = matrix entry (1,2);
    # tr(x*z*e) = matrix entry (2,1).
    return matrix(ring,2,2,[
        tr(e*z*e), tr(e*z*y),
        tr(x*z*e), tr(f*z*f)
    ])

iden=matrix(ring,2,2,[1,0,0,1])
E11=matrix(ring,2,2,[1,0,0,0])
E12=matrix(ring,2,2,[0,1,0,0])
E21=matrix(ring,2,2,[0,0,1,0])
E22=matrix(ring,2,2,[0,0,0,1])
assert image(B(1))==iden
assert image(e)==E11
assert image(x)==E12
assert image(y)==E21
assert image(f)==E22
assert image(omega)==matrix(ring,2,2,[R0,0,0,R1])
assert image(q)==matrix(ring,2,2,[
    (27+53*R0)%MOD,0,0,(27+53*R1)%MOD])
print("P16231_LOCAL_OMEGA_SPLIT_DIAGONAL_PASS",flush=True)

maps=[image(b) for b in basis]
for a in range(4):
    assert int(maps[a].trace())==red(basis[a].reduced_trace())
    assert int(maps[a].det())==red(basis[a].reduced_norm())
    for b in range(4):
        assert image(basis[a]*basis[b])==maps[a]*maps[b],(
            "LOCAL_ORDER_MULTIPLICATION_FAIL",a,b)
print("P16231_LOCAL_MAXIMAL_ORDER_16_PRODUCTS_PASS",flush=True)

# Integral basis map is invertible mod p, hence an isomorphism of
# maximal local orders as Z/p^2 modules.
flat=[[int(M[0,0]),int(M[0,1]),int(M[1,0]),int(M[1,1])]
      for M in maps]
col=matrix(ring,4,4,lambda a,b:flat[b][a])
d=int(col.det())%MOD
assert d%P!=0
print("P16231_BRANDT_LOCAL_SPLIT_UNIMODULAR_PASS",d,flush=True)

jsonreport={
    "status":"P16231_BRANDT_LOCAL_SPLIT_MATRIX_UNITS_PASS",
    "source_stage14_sha256":hashlib.sha256(raw).hexdigest(),
    "brandt_order_index":idx,
    "p":P, "modulus":MOD,
    "omega_roots":[R0,R1],
    "chosen_basis_indices_E12_E21":[i,j],
    "matrix_unit_scale_original":c,
    "basis_images":flat,
    "basis_image_determinant_mod_p2":d,
    "scope":"Local maximal-order splitting only; no conductor-p² Gross point or anticyclotomic theta derivative."
}
dest=home/"bsd389_p16231_brandt_local_split_matrix_units.json"
dest.write_text(json.dumps(jsonreport,indent=2)+"\n")
print("P16231_BRANDT_LOCAL_SPLIT_JSON",str(dest),flush=True)
print("P16231_BRANDT_LOCAL_SPLIT_MATRIX_UNITS_PASS",flush=True)
print("BOUNDARY_NO_GROSS_POINT_CLASS_ASSIGNMENTS_YET",flush=True)
print("BOUNDARY_NO_THETA_DERIVATIVE_OR_SHA_PROOF",flush=True)
