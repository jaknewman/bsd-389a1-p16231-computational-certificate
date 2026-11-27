#!/usr/bin/env python3
"""Exact Fitting-ideal countermodel to a degree-4 -> degree-2 unit contraction.

The module has rank-two Selmer corank and paired p-torsion:
X = Z_p^2 (+) (Z/p^e)^2. Its Fitting_2 content is p^(2e), whereas
Fitting_4 is the unit ideal, for any p and e>=1.

This is an abstract module model compatible with Kim's higher-Fitting
shape and with Castella--Sano's M_infinity=0. It is NOT claimed to
be the actual Selmer group of 389a1.
"""
from itertools import combinations

def diagonal_fitting_valuations(p,e):
    # Presentation diag(0,0,p^e,p^e) of the Pontryagin dual:
    # two free Z_p summands, two cyclic p^e summands.
    diag=(0,0,p**e,p**e)
    rank=len(diag)
    ideals=[]
    for i in range(rank+1):
        minor_size=rank-i
        minors=[]
        for picks in combinations(range(rank),minor_size):
            det=1
            for k in picks: det*=diag[k]
            minors.append(det)
        nonzero=[abs(x) for x in minors if x]
        if not nonzero:ideals.append(None);continue # zero ideal
        valuation=min(sum(1 for _ in range(0)) for x in nonzero) if False else None
        valuations=[]
        for x in nonzero:
            v=0
            while x%p==0:
                x//=p
                v+=1
            valuations.append(v)
        ideals.append(min(valuations))
    return ideals

for p in (5,7,107,599,1049,2003):
    for e in (1,2,3):
        f=diagonal_fitting_valuations(p,e)
        assert f==[None,None,2*e,e,0],(p,e,f)
        M2,M4=f[2],f[4]
        assert M2>0 and M4==0
        # Hyperbolic pairing on (Z/p^e)^2: (x,y),(u,v)
        # -> (x*v-y*u) / p^e in Q/Z; its matrix has determinant 1.
        n=p**e
        pairing=[[0,1],[-1,0]]
        det=pairing[0][0]*pairing[1][1]-pairing[0][1]*pairing[1][0]
        assert det%n==1
        print('COUNTERMODEL_PASS',p,e,'FITT_2_VAL',M2,
              'FITT_4_VAL',M4,'SHAFIN_ORDER',p**(2*e),
              'PAIRING_PERFECT',True)
print('NO_FORMAL_PRIMITIVE_CONTRACTION_FROM_CASTELLA_SANO_KIM_ALONE')
