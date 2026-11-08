#!/usr/bin/env python3
"""Exact Fp linear algebra for three-place Poitou-Tate relaxed Selmer line.
Global existence uses Poitou-Tate; this script does not compute a global cocycle,
Kato or Kurihara, and does not establish Sha or BSD.
"""
from itertools import product

CASES = {
    5: {'p_coordinates': (2,4), 'B': ((1,3),(1,0)), 'q': (41,61), 'expected': (1,2,1)},
    7: {'p_coordinates': (5,3), 'B': ((1,3),(1,6)), 'q': (113,673), 'expected': (1,5,4)},
}

def row_rank(rows,p):
    z=[list(v) for v in rows]
    i=0
    for j in range(len(z[0])):
        k=next((k for k in range(i,len(z)) if z[k][j] % p), None)
        if k is None: continue
        z[i],z[k]=z[k],z[i]
        inv=pow(z[i][j]%p,-1,p)
        z[i]=[(w*inv)%p for w in z[i]]
        for k in range(len(z)):
            if k!=i:
                a=z[k][j]%p
                z[k]=[(z[k][c]-a*z[i][c])%p for c in range(len(z[k]))]
        i+=1
    return i

for p,entry in CASES.items():
    F=(entry['p_coordinates'],)+entry['B']
    assert row_rank(F,p)==2
    assert row_rank(entry['B'],p)==2
    ker=[u for u in product(range(p),repeat=3) if all(sum(u[i]*F[i][j] for i in range(3))%p==0 for j in range(2))]
    assert len(ker)==p
    t=next(u for u in ker if u[0]==1)
    assert t==entry['expected'],(p,t,entry['expected'])
    assert all(u[0]!=0 for u in ker if u!=(0,0,0))
    assert t[1]!=0 and t[2]!=0
    print('TRIPLE_RELAXED_PT_LOCAL_KERNEL_PASS',p,entry['q'],'loc_MW',F,'line',t,'kernel_size',len(ker))
    print('SINGULAR_P_AND_BOTH_Q_NONZERO_PASS',p,t)
print('BOUNDARY: global existence via Poitou-Tate; no Kato identity, Sha vanishing, or BSD')
