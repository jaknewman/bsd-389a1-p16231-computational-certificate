#!/usr/bin/env sage -python
"""BSD389: independent small Sage arithmetic gate for p=16231.

The mathematical implication from p-adic leading coefficient to Kato's
p-primary upper bound is checked against the installed Sha method.

CONDITIONAL INPUT: analytic coefficient A_2/p=9534 comes from historic
V19 C01 + independent level-2 certificate. This program does NOT
recompute the p-adic L-series, certify a historic executable, or invoke
Sha.p_primary_bound, which internally computes the expensive L-series.
"""
from sage.all import EllipticCurve, ZZ, proof, log
import hashlib
import inspect
from pathlib import Path

p=ZZ(16231)
P=int(p)
E=EllipticCurve('389a1')
proof.all(True)
print('KATO389_GATE_START p=16231',flush=True)
assert list(map(int,E.ainvs())) == [0,1,1,-2,0]
assert E.conductor() == ZZ(389)
assert E.is_minimal() and E.is_good(p) and E.is_ordinary(p)
assert E.ap(p) == ZZ(128)
assert E.real_components() == 2
assert E.tamagawa_product() == 1 and E.torsion_order() == 1
assert not E.has_cm()
assert E.rank(proof=True) == 2
assert len(E.gens(proof=True)) == 2 and E.gens_certain()
assert E.galois_representation().is_surjective(p)
Et,D=E.minimal_quadratic_twist()
assert ZZ(D) == 1 and Et.is_isomorphic(E)
assert E.tate_curve(ZZ(389)).parameter().valuation() == 1
print('KATO389_LOCAL_RANK2_SURJECTIVE_ORDINARY_PASS',flush=True)

lp=E.padic_lseries(p,implementation='eclib')
assert lp._quotient_of_periods_to_twist(1) == 1
bounds=lp._prec_bounds(3,3)
assert len(bounds)>=3 and bounds[2]>=2
assert int(lp.alpha(6).lift())%P == 128
print('KATO389_NORMALIZATION_LEVEL3_PRECISION_PASS',list(map(str,bounds)),flush=True)

reg=E.padic_regulator(p,prec=6)
assert reg.valuation() == 3
K=reg.parent()
reg_lead=int((reg/(p**3)).lift())%P
assert reg_lead==1930
alpha=K(lp.alpha(6))
lg=log(K(1+p))
B=E.tamagawa_product()*reg*(1-1/alpha)**2/(E.torsion_order()**2*lg**2)
assert B.valuation()==1
B_lead=int((B/K(p)).lift())%P
assert B_lead==9534
print('KATO389_REGULATOR_BSD_FACTOR_PASS',reg_lead,B_lead,flush=True)

# Source-level audit: no expensive recomputation or monkey-patching.
Sha=E.sha()
f_bound=inspect.getsource(type(Sha).p_primary_bound)
f_padic=inspect.getsource(type(Sha).an_padic)
assert 'shan = self.an_padic(p, prec=0, use_twists=True)' in f_bound
assert 'return shan.valuation()' in f_bound
assert 'shan = lstar / bsdp' in f_padic
assert 'lstar = lps[r]' in f_padic
assert 'bsdp = tam * reg * eps / tors / lg**r' in f_padic
assert '(1 - arith.kronecker_symbol(D, p) / lp.alpha())**2' in f_padic
for method,fn in [('p_primary_bound',type(Sha).p_primary_bound),('an_padic',type(Sha).an_padic)]:
    file=Path(inspect.getfile(fn))
    print('SAGE_METHOD_SOURCE',method,str(file),hashlib.sha256(file.read_bytes()).hexdigest(),flush=True)
print('KATO389_INSTALLED_BOUND_METHOD_SEMANTICS_PASS',flush=True)

# Integer arithmetic and logical inference from authenticated input digests.
J0,J1=16014,4703
J=(J0+J1)%P
assert J==4486
A2_level2=19460969
assert A2_level2==1199*P
inv_den=pow(4*128*128,-1,P)
assert inv_den==9362
correct=(J*inv_den)%P
assert correct==8335
A2_lead=(1199+correct)%P
assert A2_lead==B_lead==9534
assert A2_lead*P==154746354
assert A2_lead*pow(B_lead,-1,P)%P==1
print('KATO389_CONDITIONAL_ANALYTIC_COEFFICIENT_PASS',J,A2_lead,flush=True)
print('KATO389_CONDITIONAL_QUOTIENT_UNIT_PASS v_p=0 digit=1',flush=True)
print('KATO389_CONDITIONAL_SHA_P_PRIMARY_TRIVIAL_BY_PROVED_BOUND',flush=True)
print('BOUNDARY: coefficient J_ref=J_V19 still assumes trusted historic C01 machine execution',flush=True)
print('BOUNDARY: Sha.p_primary_bound(16231) NOT called; no new full L-series computation',flush=True)
print('KATO389_ARITHMETIC_GATE_PASS',flush=True)
