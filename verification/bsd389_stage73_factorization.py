#!/usr/bin/env python3
"""Stage 73: exact finite-field factorization on a supplied eigensymbol subspace.
Run: python bsd389_stage73_factorization.py --selftest
     python bsd389_stage73_factorization.py --input stage73.json
Input JSON: {"p":16231, "T":[[...],...], "lambda":[...],
             "B":[[...],...]}.
T has n columns; lambda has n coordinates. Optional B has n rows and d
columns spanning the desired subspace. If omitted, uses the full ambient space.
All operations are exact modulo p and use SageMath.
"""
import argparse, json
from sage.all import GF, matrix, vector, identity_matrix

def analyze(data):
    p=int(data['p']); F=GF(p)
    t=data['T']; lam=data['lambda']; n=len(lam)
    assert n>0 and isinstance(t,list) and len(t)>0 and all(len(r)==n for r in t)
    T=matrix(F,t); L=matrix(F,1,n,lam)
    if 'B' in data:
        rows=data['B']; assert len(rows)==n and rows and len(rows[0])>0
        d=len(rows[0]); assert all(len(row)==d for row in rows)
        B=matrix(F, rows)
        assert B.rank()==d, 'B must have independent columns'
    else:
        B=identity_matrix(F,n)
    A=T*B; ell=L*B
    k=A.rank(); augmented=A.stack(ell); rk=augmented.rank()
    result={'p':p,'ambient_dim':n,'subspace_dim':B.ncols(),
            'transport_rank':k,'augmented_rank':rk,
            'factors':rk==k}
    if rk==k:
        # Solve A^T mu = ell^T; no uniqueness claimed.
        mu=A.transpose().solve_right(ell.transpose().column(0))
        assert matrix(F,1,A.nrows(),list(mu))*A==ell
        result['mu']=[int(v) for v in mu]
        result['identity_verified']=True
    else:
        # kernel vector v with Av=0 and ell*v!=0
        ker=A.right_kernel()
        v=next((v for v in ker.basis() if (ell*v)[0]!=0),None)
        assert v is not None
        x=B*v
        assert T*x==0 and (L*x)[0]!=0
        result['kernel_witness_subspace']=[int(z) for z in v]
        result['kernel_witness_ambient']=[int(z) for z in x]
        result['lambda_on_witness']=int((L*x)[0])
        result['witness_verified']=True
    return result

def selftest():
    yes=analyze({'p':107,'T':[[1,1,0],[0,1,1]],'lambda':[2,3,1]})
    assert yes['factors'] and yes['identity_verified']
    no=analyze({'p':107,'T':[[1,1,0],[0,1,1]],'lambda':[0,0,1]})
    assert not no['factors'] and no['witness_verified']
    # Restriction can eliminate an ambient obstruction.
    restrict=analyze({'p':107,'T':[[1,1,0],[0,1,1]],'lambda':[0,0,1],
                      'B':[[1,0],[0,1],[0,0]]})
    assert restrict['factors']
    print('STAGE73_SELFTEST_PASS')
    for x in (yes,no,restrict): print(json.dumps(x,sort_keys=True,default=int))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input');parser.add_argument('--selftest',action='store_true')
    a=parser.parse_args()
    if a.selftest: selftest();return
    if not a.input: parser.error('provide --input JSON or --selftest')
    with open(a.input) as f: data=json.load(f)
    result=analyze(data)
    print('STAGE73_FACTOR_PASS' if result['factors'] else 'STAGE73_KERNEL_OBSTRUCTION',json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
