#!/usr/bin/env python3
"""Independent one-pair C01/Sage coefficient oracle for 389a1, p=16231.

Three-way identity, modulo p or p^2:
  (a) native V11 one-pair sparse TSV contracted with independent V65 table,
  (b) M0(D_x), M1(D_x) directly from 16231 Sage/eclib symbol values,
  (c) actual finite-level n=3-minus-n=2 quadratic contribution at x
      using Sage's measure formula and Teichmuller exponents.

Important: (c) is only ONE base residue x of p(p-1), NOT an independent
full level-3 Sage series evaluation or new proof of global BSD.

Run with Sage's Python:
  python -u verification/local_level3_native_eclib_oracle.py --a 1 --b 0
"""
import argparse
from array import array
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

from sage.all import EllipticCurve, QQ, ZZ

P=16231
P2=P*P
P3=P2*P
N=389
NG=67
ALPHA_P2=179060520
ALPHA_P=128
SOURCE_SHA="9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
BINARY_SHA="31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63"
TABLE_SHA="aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c"

PROJECT=Path(__file__).resolve().parents[1]
HOME=Path.home()
EXPORT=PROJECT/"historical/originals/bsd389_tame_relation_export_p16231.json"
BINARY=HOME/"bsd389-c01-v11-test/bsd389_c01_v11_aggregated"
TABLE=HOME/"bsd389-c01-v14-production/v65_independent_terminal/eclib_beta_table.bin"

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for blk in iter(lambda:f.read(1048576),b""):
            h.update(blk)
    return h.hexdigest()

def residue(q, modulus):
    z=QQ(q)
    num=int(z.numerator()); den=int(z.denominator())
    if den%P==0:
        raise ArithmeticError("p divides eclib modular symbol denominator")
    return num*pow(den,-1,modulus)%modulus

def moments_from_v65(slot,rows,cache,inverses,alpha_inv):
    if slot in cache:
        return cache[slot]
    g,j=divmod(slot,P+1)
    assert 0<=g<NG and 0<=j<=P
    row=rows[g];fG=row[0];fP=row[1];fs=row[2:]
    invN=pow(N,-1,P)
    if j==0:
        m0=(fG-alpha_inv*fP)%P
        summ=sum(s*fs[s] for s in range(P))%P
    elif j<P:
        u=N*j%P
        e=inverses[u]
        m0=(fG-alpha_inv*fs[e])%P
        summ=(-(e*fP))%P
        for s in range(1,P):
            den=(1-u*s)%P
            if den:
                summ=(summ+s*inverses[den]*fs[s])%P
    else:
        m0=(fG-alpha_inv*fs[0])%P
        summ=0
        for t in range(P):
            den=(-40+N*t)%P
            if den==0:
                val=fP
            else:
                s=(-1669*inverses[den])%P
                val=fs[s]
            summ=(summ+t*val)%P
    cache[slot]=(m0,(alpha_inv*summ)%P)
    return cache[slot]

def load_table():
    assert sha(TABLE)==TABLE_SHA,"V65 eclib table SHA mismatch"
    b=TABLE.read_bytes()
    assert len(b)==20+NG*(P+2)*2
    assert b[:8]==b"BSD65F01"
    assert [int.from_bytes(b[k:k+4],"little") for k in (8,12,16)]==[P,N,NG]
    assert sys.byteorder=="little"
    rows=[]
    pos=20
    for _ in range(NG):
        row=array("H")
        row.frombytes(b[pos:pos+2*(P+2)])
        assert len(row)==P+2 and max(row)<P
        assert (sum(row[2:])+row[1]-128*row[0])%P==0
        rows.append(row)
        pos+=2*(P+2)
    return rows

def native_one_pair(a,b):
    assert sha(BINARY)==BINARY_SHA,"V11 historical ELF SHA mismatch"
    assert sha(EXPORT)==SOURCE_SHA,"original Manin export SHA mismatch"
    pair_id=(a-1)*P+b
    with tempfile.TemporaryDirectory(prefix="bsd389_local_oracle_") as tmp:
        path=Path(tmp)/"pair.tsv"
        done=subprocess.run([str(BINARY),str(EXPORT),str(pair_id),
                             str(pair_id+1),str(path)],
                            text=True,capture_output=True,check=True)
        assert "V11_AGGREGATE_PASS" in done.stderr
        items=[]
        previous=-1
        for line in path.read_text().splitlines():
            slot,c0,c1=map(int,line.split())
            assert previous<slot<NG*(P+1)
            assert 0<=c0<P and 0<=c1<P and (c0 or c1)
            items.append((slot,c0,c1))
            previous=slot
    return items

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--a",type=int,default=1)
    parser.add_argument("--b",type=int,default=0)
    args=parser.parse_args()
    a,b=args.a,args.b
    assert 1<=a<P and 0<=b<P
    assert ALPHA_P2%P==ALPHA_P
    assert (ALPHA_P2*ALPHA_P2-128*ALPHA_P2+P)%P2==0
    alpha_inv_p=pow(ALPHA_P,-1,P)
    alpha_inv_p2=pow(ALPHA_P2,-1,P2)
    invs=[0]+[pow(k,-1,P) for k in range(1,P)]

    E=EllipticCurve("389a1")
    assert E.conductor()==N and E.real_components()==2
    assert E.ap(ZZ(P))==128 and E.is_ordinary(ZZ(P))
    modular=E.modular_symbol(sign=+1,implementation="eclib",normalize="L_ratio")

    rows=load_table()
    items=native_one_pair(a,b)
    cache={}
    Jnative=0
    for slot,c0,c1 in items:
        m0,m1=moments_from_v65(slot,rows,cache,invs,alpha_inv_p)
        Jnative=(Jnative+c0*m0+c1*m1)%P
    print("LOCAL_NATIVE_V65_CONTRACTION",a,b,
          "sparse_slots",len(items),"J_mod_p",Jnative,flush=True)

    x=a+P*b
    ferm=((pow(a,P-1,P2)-1)//P)%P
    u=(b*invs[a]-ferm)%P
    w=(2*u-1)*invs[a]%P
    omega=pow(a,P2,P3)
    gamma=1+P
    kappa=((omega*pow(gamma,u,P3)-x)%P3)//P2
    assert 0<=kappa<P
    assert (omega*pow(gamma,u,P3)-x)%P2==0

    mx2=residue(modular(QQ(x)/P2),P2)
    mx1=residue(modular(QQ(x)/P),P2)
    M0=(-mx2+alpha_inv_p*mx1)%P

    # This is an ACTUAL local level-3 sum over every one of the p lifts,
    # using independent eclib modular symbols, without the C01 accumulator.
    weighted=0
    sum_c_values=0
    sum_mu3=0
    a3_local=0
    binom2=u*(u-1)//2
    inv2=pow(2,-1,P2)
    for c in range(P):
        y=x+P2*c
        assert 0<y<P3 and y%P2==x
        v=((c-kappa)*invs[a])%P
        j=u+P*v
        assert (omega*pow(gamma,j,P3)-y)%P3==0
        my3=residue(modular(QQ(y)/P3),P2)
        weighted=(weighted+c*my3)%P
        sum_c_values=(sum_c_values+my3)%P2
        mu3=pow(alpha_inv_p2,3,P2)*(my3-alpha_inv_p2*mx2)%P2
        sum_mu3=(sum_mu3+mu3)%P2
        a3_local=(a3_local+(j*(j-1)//2)*mu3)%P2
        if c in (0,4095,8191,12287,P-1):
            print("LOCAL_LEVEL3_PROGRESS",a,b,"lifts_done",c+1,flush=True)
    M1=(-alpha_inv_p*weighted)%P
    Jdirect=(-w*(M1-kappa*M0))%P
    assert Jnative==Jdirect,(
        "C01 native/V65 table vs direct level3 eclib mismatch",Jnative,Jdirect)
    print("LOCAL_NATIVE_DIRECT_ECLIB_J_PASS",a,b,Jdirect,flush=True)

    mu2=alpha_inv_p2**2*(mx2-alpha_inv_p2*mx1)%P2
    assert sum_mu3==mu2,("measure distribution fails",sum_mu3,mu2)
    assert (sum_c_values-(128*mx2-mx1))%P2==0,(
        "Hecke distribution fails")
    print("LOCAL_SAGE_HECKE_DISTRIBUTION_PASS",a,b,flush=True)

    a3_local=a3_local*inv2%P2
    a2_local=(binom2*mu2*inv2)%P2
    delta_local=(a3_local-a2_local)%P2
    expected=(P*Jnative*pow(4*ALPHA_P*ALPHA_P,-1,P))%P2
    assert delta_local==expected,(
        "finite-level n3-n2 and C01 correction disagree",delta_local,expected)
    print("LOCAL_SAGE_LEVEL3_MINUS_LEVEL2_PASS",a,b,
          "difference_mod_p2",delta_local,
          "J_over_4alpha2_mod_p",expected//P,flush=True)
    print("LOCAL_INDEPENDENT_ANALYTIC_C01_BRIDGE_PASS",a,b,flush=True)
    print("BOUNDARY: verified a single x=a+p*b, not the sum over p(p-1) residues",flush=True)

if __name__=="__main__":
    main()
