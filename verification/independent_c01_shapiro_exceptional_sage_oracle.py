#!/usr/bin/env python3
"""High-p adversarial exact-coset plus direct Sage n3 oracle.

Select reproducible pairs reaching Shapiro infinity and Manin relation
branches using exact Z-valued matrices, not C01 pushforward outputs.
For each pair recompute directly SUM_(c=0..p-1) (c-kappa)*m(y/p^3)
from Sage/eclib, compare to the unmodified SHA-frozen C++ full-J
engine running on exactly that pair. The frozen C++ source is NOT edited.
The oracle uses Sage eclib, so it remains a shared modular symbol input.
New test: not yet run; the code must be exercised on the user server.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from sage.all import EllipticCurve, QQ, ZZ

N=389
P=16231
P2=P*P
P3=P2*P
TOTAL=P*(P-1)
EXPECTED_CPP_SHA="6d206751fe676e9594445335da15471430908107768ec80f10b60f088fcfce09"
EXPECTED_REL_SHA="9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
ROOT=Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def matmul(a,b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])

def inverse(a):
    assert a[0]*a[3]-a[1]*a[2]==1
    return (a[3],-a[1],-a[2],a[0])

def fragments(x):
    r,s=x,P2
    hm2,hm1=0,1
    km2,km1=1,0
    conv=[]
    while s:
        q,r,s=r//s,s,r%s
        hn=q*hm1+hm2
        kn=q*km1+km2
        conv.append((hn,kn))
        hm2,hm1=hm1,hn
        km2,km1=km1,kn
    assert conv[-1][0]*P2==conv[-1][1]*x
    out=[(1,conv[0][0],0,conv[0][1])]
    for j in range(len(conv)-1):
        z=-1 if j%2==0 else 1
        h,k=conv[j]
        hh,kk=conv[j+1]
        out.append((z*h,hh,z*k,kk))
    assert all(t[0]*t[3]-t[1]*t[2]==1 for t in out)
    return out

def key(mat,n):
    c,d=mat[2]%n,mat[3]%n
    return c*pow(d,-1,n)%n if d else n

def qidx(mat):
    assert mat[2]%N==0
    d=mat[3]%P
    return mat[2]*pow(N*d,-1,P)%P if d else P

def ri(j,rinf):
    return (1,0,N*j,1) if j<P else rinf

def trace_pair(id,reps,maprep,rinf):
    x=1+id//P+P*(id%P)
    counts={"gen":0,"rel":0,"e0":0,"e1":0}
    for f in fragments(x):
        idx=maprep[key(f,N)]
        row=reps[idx]
        H=matmul(f,inverse(row["matrix"]))
        assert H[2]%N==0
        j0=qidx(H)
        h=matmul(H,inverse(ri(j0,rinf)))
        assert h[2]%(N*P)==0
        if j0==P:counts["e0"]+=1
        if row["generator"]>=0:
            counts["gen"]+=1
        else:
            counts["rel"]+=1
            for t in row["relations"]:
                X=matmul(ri(j0,rinf),inverse(t["A"]))
                assert X[2]%N==0
                j1=qidx(X)
                hi=matmul(X,inverse(ri(j1,rinf)))
                assert hi[2]%(N*P)==0
                if j1==P:counts["e1"]+=1
    return counts

def choose(reps,maprep,rinf):
    # Found by an independent exact-integer pass over the original Manin
    # export: id=38 hits an inner infinity transport, and id=67 hits
    # both an outer infinity transport and 66 inner infinity transports.
    # Additional fixed IDs probe low, middle, and terminal pair ranges.
    fixed=(0,38,67,P+3,TOTAL//2,TOTAL-1)
    selected=[(id,trace_pair(id,reps,maprep,rinf)) for id in fixed]
    byid=dict(selected)
    assert byid[38]["e1"]>0 and byid[67]["e0"]>0
    assert byid[67]["e1"]>0
    print("HIGH_P_ADVERSARIAL_EXCEPTIONAL_IDS",
          {"e0":67,"e1":38},"id_67",byid[67],flush=True)
    return selected

def modp_symbol(value):
    q=QQ(value)
    n,d=int(q.numerator()),int(q.denominator())
    assert d%P
    return n*pow(d,-1,P)%P

def sage_contribution(id,f,alpha_inv):
    a,b=1+id//P,id%P
    x=a+P*b
    q=((pow(a,P-1,P2)-1)//P)%P
    u=(b*pow(a,-1,P)-q)%P
    w=((2*u-1)*pow(a,-1,P))%P
    lift=pow(a,P2,P3)*pow(P+1,u,P3)%P3
    assert (lift-x)%P2==0
    kappa=((lift-x)%P3)//P2
    weighted=0
    for c in range(P):
        y=x+P2*c
        m3=modp_symbol(f(QQ(y)/P3))
        weighted=(weighted+(c-kappa)*m3)%P
    # Derived without M0, M1 or Shapiro: J_pair is alpha^(-1)*
    # w*sum_c(c-kappa)*m((x+p^2*c)/p^3) in F_p.
    return w*alpha_inv*weighted%P

def binary_contribution(id,binary,table,export_stream,temp_dir):
    checkpoint=temp_dir/("pair_%09d.chk"%id)
    result=subprocess.run([str(binary),str(table),str(id),str(id+1),
                           str(checkpoint)],input=export_stream,
                          capture_output=True,text=True,check=True)
    term="INDEPENDENT_SCALAR_INTERVAL_PASS start=%d end=%d J_mod_p="%(id,id+1)
    matches=re.findall(re.escape(term)+r"(\d+)",result.stdout)
    assert len(matches)==1,(id,result.stdout[-1000:])
    return int(matches[0])

def main():
    export=ROOT/"historical/originals/bsd389_tame_relation_export_p16231.json"
    table=Path.home()/"bsd389-c01-v14-production/v65_independent_terminal/eclib_beta_table.bin"
    binary=Path.home()/"bsd389-evidence-frozen/bsd389_independent_J"
    exporter=ROOT/"verification/export_shapiro_transport_stream.py"
    assert sha(export)==EXPECTED_REL_SHA
    assert sha(binary)==EXPECTED_CPP_SHA
    assert table.is_file()
    data=json.loads(export.read_text())
    reps=data["reps"]
    rinf=tuple(data["rinf"])
    assert len(reps)==390 and len(data["generators"])==67
    maprep={key(tuple(z["matrix"]),N):i for i,z in enumerate(reps)}
    assert len(maprep)==390
    selected=choose(reps,maprep,rinf)
    inp=subprocess.run([sys.executable,str(exporter),str(export)],
                       capture_output=True,text=True,check=True).stdout
    E=EllipticCurve("389a1")
    lp=E.padic_lseries(ZZ(P),implementation="eclib")
    assert lp._prec_bounds(3,3)[2]>=2
    assert lp._quotient_of_periods_to_twist(1)==1
    assert E.real_components()==2 and E.ap(P)==128
    f=lp.modular_symbol
    ainv=pow(128,-1,P)
    with tempfile.TemporaryDirectory(prefix="bsd389_direct_c01_") as temp:
        for id,counts in selected:
            direct=sage_contribution(id,f,ainv)
            native=binary_contribution(id,binary,table,inp,Path(temp))
            assert direct==native,(id,direct,native,counts)
            if id==0:assert direct==2316
            if id==P+3:assert direct==11725
            print("HIGH_P_DIRECT_SAGE_VS_FROZEN_C01_PASS",
                  "id",id,"direct",direct,"native",native,
                  "branches",counts,flush=True)
    assert any(c["e0"]>0 for _,c in selected)
    assert any(c["e1"]>0 for _,c in selected)
    print("HIGH_P_DIRECT_SAGE_EXCEPTIONAL_E0_E1_ORACLE_PASS",flush=True)
    print("BOUNDARY: sampled adversarial high-p local check, not full direct Sage n3.",flush=True)

if __name__=="__main__":
    main()
