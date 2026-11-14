#!/usr/bin/env python3
"""Exact E389a1 local arithmetic for a one-gate class-field parity theorem.

The mathematical theorem uses external Tate local duality, Sah's lemma,
global class field theory and Dokchitser-Dokchitser p-parity.
This checker does NOT compute a p-ramified class group, Sha or BSD.
"""
from math import isqrt

def isprime(p):
    return p >= 2 and all(p%q for q in range(2,isqrt(p)+1))

def count_mod(q):
    assert isprime(q) and q != 2
    total=1
    singular=0
    for x in range(q):
        d=(4*x*x*x+4*x*x-8*x+1)%q
        if d==0:
            total+=1
            if (3*x*x+2*x-2)%q==0:
                singular+=1
        elif pow(d,(q-1)//2,q)==1:
            total+=2
    return total,singular

a1,a2,a3,a4,a6=0,1,1,-2,0
b2=a1*a1+4*a2
b4=a1*a3+2*a4
b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4
c6=-(b2**3)+36*b2*b4-216*b6
Delta=-(b2*b2*b8)-8*b4**3-27*b6*b6+9*b2*b4*b6
assert (c4,c6,Delta)==(112,-856,389)
assert (95*95+c6)%389==0
print('BAD389_SPLIT_I1_EXACT_PASS',c4,c6,Delta,95)

n,sing=count_mod(389)
assert n==389 and sing==1
node_x,node_y=299,194
assert (node_y*node_y+node_y-node_x**3-node_x**2+2*node_x)%389==0
assert (2*node_y+1)%389==0
assert (-3*node_x*node_x-2*node_x+2)%389==0
assert n-1==388==4*97
print('BAD389_SMOOTH_POINTS_AND_NODE_PASS',n,(node_x,node_y),388)

for p,expected_n in ((5,9),(7,13),(11,16),(13,17),(97,107),(599,600),(16231,16104)):
    points,_=count_mod(p)
    assert points==expected_n
    ap=p+1-points
    local_389=0 if p>=5 and p not in (97,389) else 'EXCEPTION'
    local_p_singular=1 if points%p else 'ANOMALOUS'
    print('E389A1_LOCAL_COHOMOLOGY_INPUT_PASS',p,points,ap,local_389,local_p_singular)

# EXACT FORMAL CONSEQUENCES of the p-parity theorem + rank-one local quotient
# for hypothetical m_p = dimension of a genuine equivariant class field Hom.
for m in range(2,13):
    epsilon=m%2
    sel=m-epsilon
    sha=sel-2
    assert sel%2==0 and sha==2*(m//2-1)
    print('ONE_GATE_PARITY_DIMENSION_IDENTITY',m,epsilon,sel,sha)
print('NO ACTUAL CLASSFIELD MULTIPLICITY m_p, SHA OR GLOBAL BSD CALCULATED')
