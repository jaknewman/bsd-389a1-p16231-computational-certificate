#!/usr/bin/env python3
"""Independent arithmetic audit of the completed Sage Kurihara p=11 JSON.

Independent checks: elliptic-curve group law and point counts at 11, 397,
991, auxiliary finite-field Kummer wedge; primitive roots; both canonical
390-array SHA-256 commitments; 390-vector contraction and mod-11 delta.
This does NOT re-evaluate all 196713 eclib modular symbols; the source Sage
script did, and compared its 390-coefficient accumulation with its direct
symbol-by-Manin computation.
"""
import argparse
import hashlib
import json
from pathlib import Path

P = 11
QS = ((397, 24, 374, 34, 10, 5), (991, -53, 1045, 95, 7, 6))
SHA_M = 'a8f442e9bfd29e9176d43fc765c6357516b9b4956a08b60d999cdecf58a4c9cd'
SHA_W = 'c05dbcaffeded931355c9b5fff24d28ed351d82c2ae4259167716ef1000a7219'

def curve_point(x, y, p):
    return (y*y+y-x*x*x-x*x+2*x) % p == 0

def add(Pt, Qt, p):
    if Pt is None: return Qt
    if Qt is None: return Pt
    x,y=Pt;u,v=Qt
    if x==u and (y+v+1)%p==0: return None
    if x==u:
        d=pow((2*y+1)%p,-1,p)
        lam=(3*x*x+2*x-2)*d%p
        nu=(-x*x*x-2*x-y)*d%p
    else:
        d=pow((u-x)%p,-1,p)
        lam=(v-y)*d%p
        nu=(y*u-v*x)*d%p
    X=(lam*lam-1-x-u)%p
    Y=(-lam*X-nu-1)%p
    assert curve_point(X,Y,p)
    return X,Y

def mul(n, point, p):
    v=None
    while n:
        if n&1: v=add(v,point,p)
        point=add(point,point,p)
        n>>=1
    return v

def point_count(p):
    # For y^2+y = x^3+x^2-2x, square discriminant is
    # 1+4(x^3+x^2-2x); p is odd.
    out=1
    for x in range(p):
        disc=(1+4*(x*x*x+x*x-2*x))%p
        out+=1 if disc==0 else 2 if pow(disc,(p-1)//2,p)==1 else 0
    return out

def primitive(g, q):
    n=q-1; fs=[]; d=2
    while d*d<=n:
        if n%d==0:
            fs.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:fs.append(n)
    return all(pow(g,(q-1)//r,q)!=1 for r in fs)

def digest(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def local_audit(local=None):
    assert point_count(P)==16
    rows=[]
    for idx,(q,ap,n,h,k,g) in enumerate(QS):
        assert q%P==1 and (q+1-ap)%P==0
        assert point_count(q)==n==q+1-ap
        assert h==n//P and h%P!=0
        assert primitive(g,q)
        X=mul(h,(-1,1),q);Y=mul(h,(0,-1),q)
        assert X is not None and Y is not None
        assert mul(P,X,q) is None and mul(P,Y,q) is None
        assert mul(k,X,q)==Y
        assert sum(mul(t,X,q)==Y for t in range(P))==1
        rows.append([1,k])
        if local is not None:
            entry=local[idx]
            for key,val in {'q':q,'ap':ap,'E_Fq_order':n,'h':h,'coordinates':[1,k]}.items():
                assert entry[key]==val,(key,entry[key],val)
            assert entry['hP']==list(X) and entry['hQ']==list(Y)
    assert rows==[[1,10],[1,7]]
    det=(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])%P
    assert det==8
    print('P11_INDEPENDENT_ELLIPTIC_POINT_COUNTS_AND_WEDGE_PASS',rows,det)

def audit(data):
    local_audit(data['q_local_data'])
    assert data['status']=='P11_KURIHARA_FULL_COMPLETE'
    assert data['curve']=='389a1'
    for key,val in {'p':11,'q1':397,'q2':991,'n':393427,
                    'half_representatives':196713,'local_wedge_det_mod11':8}.items():
        assert data[key]==val,(key,data[key],val)
    assert data['primitive_roots']==[5,6]
    M=data['manin390']; W=data['W390']
    assert len(M)==len(W)==390
    assert all(type(v) is int and 0<=v<P for v in M+W)
    assert digest(M)==data['manin390_sha256']==SHA_M
    assert digest(W)==data['W390_sha256']==SHA_W
    contracted=sum(m*w for m,w in zip(M,W))%P
    assert contracted==data['direct_manin_half_sum']==data['weight_contract_half_sum']==6
    delta=(2*contracted)%P
    assert delta==data['delta_mod11']==1 and data['delta_unit'] is True
    assert 0<data['count_nonzero_weights']<=data['count_units']<=196713
    assert data['count_edges']>=data['count_nonzero_weights']
    print('P11_AUTHENTIC_USER_JSON_390_HASHES_AND_CONTRACTION_PASS')
    print('P11_FULL_KURIHARA_DELTA_MOD11',delta,'NONZERO',bool(delta))
    print('IMPLICATION_KIM_THEOREMS_1_8_1_10_SHA11_PRIMARY_ZERO')
    print('SCOPE: JSON arithmetic audited, not independent re-execution of all modular symbols')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path)
    p.add_argument('--self-test',action='store_true')
    args=p.parse_args()
    if args.self_test:
        local_audit()
        print('LOCAL_SELF_TEST_PASS')
    if args.input:
        audit(json.loads(args.input.read_text(encoding='utf-8')))
    elif not args.self_test:p.error('Provide --input or --self-test')

if __name__=='__main__':main()
