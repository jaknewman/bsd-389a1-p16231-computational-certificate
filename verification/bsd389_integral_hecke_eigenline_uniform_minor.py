#!/usr/bin/env python3
"""Construct an actual p-INDEPENDENT integer Hecke-eigenline minor for 389a1.

This is a proof-grade linear-algebra project over the TRUE integral lattice
of level-389 sign-plus modular symbols, unlike the synthetic group-ring H.

Sage 10.9 API (documented):
  M=ModularSymbols(389,2,sign=+1,base_ring=QQ)
  M.integral_hecke_matrix(ell)
Hecke matrices in this canonical M.integral_structure() lattice are ZZ
matrices, not an arbitrary rational-basis reduction. Stack T_ell-a_ell(E)
for small ell until the QQ kernel is EXACTLY one-dimensional. Find a
nonzero integer (d-1)x(d-1) minor C of this same stacked matrix.
For EVERY prime p not dividing C, reduction of this integral matrix has
rank d-1, and the primitive rational eigenvector gives a nonzero
mod-p kernel => the kernel of these fixed Hecke constraints is dim1.

THIS C IS A UNIFORM CONGRUENCE/EIGENLINE BOUND, NOT A SHA
BOUND, NOT Fitt_2(Selmer), and says NOTHING about nonzero
two-prime Kurihara numbers at varying auxiliary conductors.
The result is not claimed until this is run by the user.

Usage in Sage:
  python -u verification/bsd389_integral_hecke_eigenline_uniform_minor.py \
    --output ~/bsd389_integral_hecke_eigenline_minor.json
"""
import argparse
import hashlib
import json
from pathlib import Path

from sage.all import (
    EllipticCurve, QQ, ZZ, GF, ModularSymbols, matrix,
    identity_matrix, vector, lcm, gcd, prime_range,
)

N=389
HECKE_PRIMES=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71)

def primitive_rational_kernel_vector(A):
    K=A.change_ring(QQ).right_kernel()
    assert K.dimension()==1
    u=K.basis()[0]
    den=ZZ(1)
    for x in u:
        den=lcm(den,ZZ(QQ(x).denominator()))
    v=vector(ZZ,[ZZ(den*x) for x in u])
    g=ZZ(0)
    for x in v:
        g=gcd(g,ZZ(x))
    assert g>0
    v=vector(ZZ,[x//g for x in v])
    assert any(v) and A*v==vector(ZZ,A.nrows())
    assert gcd([abs(ZZ(x)) for x in v])==1
    return v

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,
                    default=Path.home()/'bsd389_integral_hecke_eigenline_minor.json')
    ap.add_argument('--probe-primes',default='5,7,107',
                    help='comma separated finite-field sample probes')
    args=ap.parse_args()
    E=EllipticCurve(QQ,[0,1,1,-2,0])
    assert ZZ(E.conductor())==N
    M=ModularSymbols(N,2,sign=+1,base_ring=QQ)
    d=int(M.dimension())
    assert d>1
    print('HECKE_INTEGRAL_MANIN_AMBIENT_DIM',d,flush=True)
    lattice=M.integral_structure()
    assert int(lattice.rank())==d
    print('HECKE_INTEGRAL_LATTICE_RANK_PASS',d,flush=True)

    stacked=matrix(ZZ,0,d)
    used=[]
    rational_rank=0
    for ell in HECKE_PRIMES:
        B=matrix(ZZ,M.integral_hecke_matrix(ell))
        assert B.nrows()==d and B.ncols()==d
        ap_ell=ZZ(E.ap(ell))
        A=B-ap_ell*identity_matrix(ZZ,d)
        stacked=stacked.stack(A)
        used.append([int(ell),int(ap_ell)])
        rational_rank=int(stacked.rank())
        assert rational_rank<=d-1,(
            'NO_E_RATIONAL_HECKE_KERNEL',ell,rational_rank,d)
        print('HECKE_INTEGRAL_STACK_PROGRESS',
              'ell',ell,'ap',ap_ell,'rows',stacked.nrows(),
              'rank_Q',rational_rank,'target',d-1,flush=True)
        if rational_rank==d-1:
            break
    assert rational_rank==d-1,(
        'INSUFFICIENT_FIXED_HECKE_OPERATORS',used,rational_rank,d)
    v=primitive_rational_kernel_vector(stacked)
    print('HECKE_INTEGRAL_FIXED_OPERATORS_Q_EIGENLINE_DIM1_PASS',
          'number_hecke_primes',len(used),'rank',rational_rank,flush=True)
    print('HECKE_INTEGRAL_PRIMITIVE_GLOBAL_KERNEL_VECTOR_PASS',
          'entries',len(v),'nonzero',sum(x!=0 for x in v),flush=True)

    # Select rows and columns of a maximal-rank square minor.
    # If possible pick mod-5 pivot subsets, so this single integer minor
    # is guaranteed coprime to 5 and gives an immediate p5 certificate.
    A_Q=stacked.change_ring(QQ)
    rank=rational_rank
    B5=stacked.change_ring(GF(5))
    if int(B5.rank())==rank:
        base=B5
        pivot_field='GF(5)'
    else:
        base=A_Q
        pivot_field='QQ'
    rows=list(base.transpose().echelon_form().pivots())
    cols=list(base.echelon_form().pivots())
    assert len(rows)==len(cols)==rank
    sq=stacked.matrix_from_rows_and_columns(rows,cols)
    det=ZZ(sq.det())
    assert det!=0
    C=abs(det)
    assert (C%5!=0)==(pivot_field=='GF(5)')
    print('HECKE_UNIFORM_INTEGER_NONZERO_MINOR_PASS',
          'size',rank,'abs_det_bits',int(C.nbits()),
          'pivot_field',pivot_field,flush=True)
    print('HECKE_UNIFORM_INTEGER_DETERMINANT',C,flush=True)

    # A primitive integral kernel vector is nonzero modulo all p.
    # For p∤C, det minor is invertible modulo p, so rank>=d−1;
    # its kernel vector gives rank<=d−1. This is the complete theorem.
    sample={}
    for token in args.probe_primes.split(','):
        if not token.strip():
            continue
        p=int(token.strip())
        assert p>=2 and ZZ(p).is_prime()
        A_mod=stacked.change_ring(GF(p))
        r=int(A_mod.rank())
        minor_unit=(C%p)!=0
        if minor_unit:
            assert r==rank and any(ZZ(x)%p for x in v)
        sample[str(p)]={'modp_rank':r,
                        'kernel_dim':d-r,
                        'minor_unit':minor_unit}
        print('HECKE_INTEGRAL_FINITE_FIELD_PROBE',
              'p',p,'rank',r,'kernel_dimension',d-r,
              'selected_minor_unit',minor_unit,flush=True)

    obj={
        'curve':'389a1','level':N,'sign':1,
        'ambient_dim':d,'integral_lattice_rank':int(lattice.rank()),
        'hecke_primes_and_ap':used,
        'stacked_rows':int(stacked.nrows()),
        'rational_rank':rank,
        'kernel_dim_Q':d-rank,
        'primitive_integer_eigenvector':[int(x) for x in v],
        'maximal_minor_rows':rows,'maximal_minor_columns':cols,
        'maximal_minor_det':str(det),
        'uniform_integer_C':str(C),
        'sample_primes':sample,
        'scope':('For EVERY p not dividing C, the kernel of the FIXED '
                 'integral Hecke matrices is dimension one in their '
                 'integral modular-symbol lattice mod p. This does '
                 'NOT give nonzero two-prime Kurihara M11 or Sha Fitt2.')
    }
    encoded=json.dumps(obj,sort_keys=True,separators=(',',':')).encode()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(encoded+b'\n')
    digest=hashlib.sha256(encoded).hexdigest()
    print('HECKE_UNIFORM_CANONICAL_JSON_SHA256',digest,flush=True)
    print('HECKE_UNIFORM_REPORT',args.output,flush=True)
    print('HECKE_UNIFORM_ALL_P_OUTSIDE_DIVISORS_C_EIGENLINE_RIGID_PASS',
          'conditional_on_correct_integral_hecke_matrices',flush=True)
    print('BOUNDARY_C_HECKE_IS_NOT_C_SHA_AND_DOES_NOT_PROVE_BSD',flush=True)

if __name__=='__main__':
    main()
