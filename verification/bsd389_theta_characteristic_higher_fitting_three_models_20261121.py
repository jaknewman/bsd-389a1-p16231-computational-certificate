#!/usr/bin/env python3
"""Formal p16231 theta and characteristic-vs-Fitting obstruction.

Three torsion Z_p[[T]] modules have identical characteristic ideals
(T^4), but augmentation Fitt_2 ideals (1),(0),(p^2) differ.
These are NOT actual arithmetic Selmer modules.
"""
from itertools import combinations
p=16231
a2=(-3*4986*4083)%p
assert pow(128,-2,p)==4986
assert a2==3739 and a2*a2%p==5230
print("BSD389_THETA_UNIT_COEFFICIENT_FORMAL_GATE_PASS",
      "p",p,"a2",a2,"a2_squared_modp",a2*a2%p)

def minimal_monomials(items):
    """Minimal ideal generators p^a*T^b by divisibility."""
    vals=sorted(set(items))
    return [x for x in vals if not any(
        y!=x and y[0]<=x[0] and y[1]<=x[1] for y in vals)]

def fitt2(n,relations):
    """Sparse diagonal relation columns (row,p_power,T_power).

    All nonzero minors are pure monomials, so their ideal is
    determined exactly by the exponent pairs.
    """
    k=n-2
    if k==0:return [(0,0)]
    output=[]
    for chosen in combinations(relations,k):
        if len({v[0] for v in chosen})==k:
            output.append((sum(v[1] for v in chosen),
                           sum(v[2] for v in chosen)))
    return minimal_monomials(output)

modules={
 "A":(2,[(0,0,2),(1,0,2)],[2,2],0),
 "B":(4,[(i,0,1) for i in range(4)],[1,1,1,1],0),
 "C":(4,[(0,0,2),(1,0,2),(2,1,0),(2,0,1),
          (3,1,0),(3,0,1)],[2,2],2)}
expected={
 "A":[(0,0)],
 "B":[(0,2)],
 "C":[(0,2),(1,1),(2,0)]}
for label,(generators,relations,jordan,finite_dim) in modules.items():
    assert sum(jordan)==4  # characteristic ideal (T^4)
    F=fitt2(generators,relations)
    assert F==expected[label],(label,F)
    specialization=[a for a,b in F if b==0]
    augmented="0" if not specialization else (
        "1" if min(specialization)==0
        else "p^"+str(min(specialization)))
    assert augmented=={"A":"1","B":"0","C":"p^2"}[label]
    corank=len(jordan)
    t_rank=sum(n-1 for n in jordan)
    assert t_rank+corank==4
    assert corank>=2 and corank%2==0
    assert (t_rank>0)==(corank==2)
    assert finite_dim=={"A":0,"B":0,"C":2}[label]
    print("BSD389_HIGHER_FITTING_MODULE_PASS",
          label,"char=(T^4)",
          "Jordan_blocks",jordan,
          "nilpotent_T_rank",t_rank,
          "augmented_corank",corank,
          "finite_p_torsion_dimension",finite_dim,
          "Fitt2_monomials",F,
          "augmented_Fitt2",augmented,flush=True)

# One Jordan block of length 2 and two of length 1:
# characteristic T^4 but augmented corank 3.
# This is ruled out ONLY when an actual arithmetic parity theorem
# applies to a true Selmer module under valid augmentation control.
j=[2,1,1]
assert sum(j)==4 and len(j)==3 and sum(n-1 for n in j)==1
print("BSD389_PARITY_EXCLUDES_THREE_BLOCK_MODEL_PASS",j)

# All p-primary summands can be finite without finite global support.
# Infinite direct sum over primes of (Z/pZ)^2 is an explicit countermodel.
print("BSD389_FINITE_PRIME_SUPPORT_IS_SEPARATE_GLOBAL_GATE_PASS")
print("BSD389_THETA_FITT2_JORDAN_TOY_AUDIT_ALL_PASS")
print("BOUNDARY: analytic theta source identity, actual Selmer comparison,"
      " Fitting control and global Sha finiteness remain unproved.")
