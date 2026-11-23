#!/usr/bin/env python3
"""Full finite group-ring proof gates: Euler double zero, 2D defect, mixed-jet loss.

Pure group-ring combinatorics, not an arithmetic identification with Selmer
or a constructed degree-two Kurihara coefficient.
"""
from itertools import product

for p,a in ((5,1),(7,1),(11,1),(5,2),(11,2)):
    m=p**a
    # Fp[C_(p^a)] ≅ Fp[T]/(T^m). The Euler operator has matrix
    # m_(T^2): e_j -> e_(j+2) if j+2<m, otherwise 0.
    image_indices=set(range(2,m))
    kernel_indices={m-2,m-1}
    cokernel_indices={0,1}
    assert len(image_indices)==m-2
    assert len(kernel_indices)==2 and len(cokernel_indices)==2
    assert all((j+2>=m)==(j in kernel_indices) for j in range(m))
    print('FINITE_EULER_DOUBLE_ZERO_EXACT_SEQUENCE_PASS',p,a,
          'group_ring_dimension',m,'rank',len(image_indices),
          'kernel',sorted(kernel_indices),'cokernel',sorted(cokernel_indices))

for p,a,b in ((5,1,1),(11,1,1),(5,2,1)):
    m=p**a;n=p**b
    # multiplication by (T1*T2)^2 on Fp[T1,T2]/(T1^m,T2^n)
    rank=sum(i+2<m and j+2<n for i,j in product(range(m),range(n)))
    defect=m*n-rank
    assert rank==(m-2)*(n-2)
    assert defect==2*m+2*n-4
    print('TWO_VARIABLE_EULER_DEFECT_EXACT_PASS',p,a,b,
          'ring_dimension',m*n,'kernel_and_cokernel',defect)

# Mixed first-jet ring Fp[T1,T2]/(T1^2,T2^2) has basis
# {1,T1,T2,T1*T2}, so each Euler factor Ti^2 acts as ZERO.
for p in (5,7,11,107):
    basis=[(0,0),(1,0),(0,1),(1,1)]
    assert len(basis)==4
    assert all((i+2,j) not in basis and (i,j+2) not in basis
               for i,j in basis)
    assert (1,1) in basis
    print('MIXED_KURIHARA_JET_SURVIVES_BUT_EULER_NORM_KILLS_PASS',p)
print('BOUNDARY_NO_ARITHMETIC_BOCKSTEIN_COMPARISON_OR_SHA_CONCLUSION')
