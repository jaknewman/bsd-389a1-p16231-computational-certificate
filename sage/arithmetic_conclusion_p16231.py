#!/usr/bin/env sage -python
"""Arithmetic audit bridge, 389a1 at p=16231.

This does not re-run the historic C01/V19 sum or the expensive
Sha.p_primary_bound(), whose internal an_padic() recomputes the L-series.
The analytic coefficient is taken from the archived *conditional*
C01/level-2 certificate; the deductions here are mathematical.
"""
from sage.all import EllipticCurve, ZZ, Qp
import inspect

p = ZZ(16231)
P = int(p)
E = EllipticCurve("389a1")
assert E.conductor() == 389
assert E.rank(proof=True) == 2
assert E.is_good(p) and E.is_ordinary(p) and E.ap(p) == 128
assert E.galois_representation().is_surjective(p)
assert E.tamagawa_product() == 1
assert E.torsion_order() == 1
assert E.real_components() == 2
assert ZZ(E.minimal_quadratic_twist()[1]) == 1
assert E.tate_curve(ZZ(389)).parameter().valuation() == 1
print("LOCAL_KATO_SKINNER_URBAN_GATES_PASS",flush=True)

lp = E.padic_lseries(p)
bounds = lp._prec_bounds(3,3)
assert bounds[2] >= 2
alpha = lp.alpha()
assert int(alpha.residue()) == 128
print("LEVEL3_COEFFICIENT_PRECISION_PASS",list(bounds),flush=True)

K = Qp(p, prec=12)
reg = E.padic_regulator(p)
assert reg.valuation() == 3
B = K(E.tamagawa_product()) * K(reg) * (1 - K(alpha)**(-1))**2 \
    / (K(E.torsion_order())**2 * K(1+p).log()**2)
assert B.valuation() == 1
B0 = int((B / K(p)).residue())
assert B0 == 9534
print("BSD_REGULATOR_NORMALIZATION_PASS",B0,flush=True)

# Exact congruences, conditional on the historical C01 measurement:
J = 4486
A2_level2 = 19460969
assert J == (16014+4703)%P
assert A2_level2 == 1199*P
correction = J*pow(4*128*128,-1,P)%P
assert correction == 8335
A20 = (1199+correction)%P
assert A20 == B0 == 9534
assert A20*P == 154746354
assert (A20*pow(B0,-1,P))%P == 1
print("C01_TO_LSTAR_CONDITIONAL_PASS A2/p=9534 ratio_mod_p=1 v_p=0",flush=True)

src = inspect.getsource(type(E.sha()).p_primary_bound)
assert "self.an_padic(p, prec=0, use_twists=True)" in src
assert "return shan.valuation()" in src
print("SAGE_P_PRIMARY_BOUND_SIGNATURE_PASS",flush=True)
print("CONDITIONAL_ARITHMETIC_IMPLICATION: #Sha[16231^infinity] <= 1",flush=True)
print("CONDITIONAL_ARITHMETIC_IMPLICATION: Sha[16231^infinity] = 0",flush=True)
print("BOUNDARY: full historical L-series NOT independently recomputed",flush=True)
