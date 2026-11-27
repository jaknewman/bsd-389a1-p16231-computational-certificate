#!/usr/bin/env python3
"""Finite exact rank-four Kurihara cross-comparison; no BSD conclusion.

Verifies unit-covariance under arbitrary primitive-root changes and gives
counterexamples to any unit-proportional Pfaffian relation between δ_4 and
δ_2. Numerical δ values are reproduced by kuri4.cpp in this same package.
"""
from itertools import product, combinations
P=5
pairs={
(41,61):4,(41,131):1,(41,211):2,(41,251):3,
(61,131):2,(61,211):4,(61,251):1,
(131,211):0,(131,251):1,(211,251):2
}
quartic={
(41,61,131,211):2,
(41,61,131,251):0,
(41,61,211,251):0,
(41,131,211,251):4,
}

def calc(q, nums, q4):
    a,b,c,d=q
    terms=[nums[a,b]*nums[c,d],nums[a,c]*nums[b,d],nums[a,d]*nums[b,c]]
    pf=(terms[0]-terms[1]+terms[2])%P
    wick=sum(terms)%P
    cumulant=(q4-wick)%P
    return pf,wick,cumulant

for q,value in quartic.items():
    pf,wick,cum=calc(q,pairs,value)
    print('FOUR_SUPPORT',','.join(map(str,q)),'DELTA4',value,
          'PFAFFIAN_PAIR',pf,'SYMMETRIC_WICK_PAIR',wick,'CONNECTED_DEFECT',cum)
assert calc((41,61,131,211),pairs,2)[0]==0
assert calc((41,61,131,251),pairs,0)[0]==4
assert calc((41,61,131,211),pairs,2)[2]==4
assert calc((41,61,131,251),pairs,0)[2]==4
print('PFAFFIAN_UNIT_PROPORTIONALITY_REFUTED_BOTH_DIRECTIONS_PASS')

# All 4^5 unit changes log_{g_i} -> c_i log_{g_i}.
qs=(41,61,131,211,251)
for coeffs in product(range(1,P),repeat=len(qs)):
    c=dict(zip(qs,coeffs))
    modified={(a,b):v*c[a]*c[b]%P for (a,b),v in pairs.items()}
    for q,value in quartic.items():
        fac=1
        for a in q:fac=fac*c[a]%P
        newv=value*fac%P
        oldpf,oldwick,oldcum=calc(q,pairs,value)
        newpf,newwick,newcum=calc(q,modified,newv)
        assert (newpf,newwick,newcum)==tuple(t*fac%P for t in (oldpf,oldwick,oldcum))
print('PRIMITIVE_ROOT_UNIT_COVARIANCE_EXHAUSTIVE_PASS',4**5,'root_rescalings')
print('BOUNDARY: Pfaffian/Wick factorization is false; no general primitive contraction proved')
