#!/usr/bin/env python3
"""BSD 389a1 — global numerical classical-BSD baseline, NOT a proof.
Run with python -u from the activated SageMath/Miniforge environment.
"""
from sage.all import EllipticCurve, RealField, ZZ, proof
proof.all(True)
E = EllipticCurve("389a1")
assert list(E.ainvs()) == [0,1,1,-2,0]
assert E.conductor() == 389
assert E.rank(proof=True) == 2
assert len(E.gens(proof=True)) == 2
assert E.gens_certain()
assert E.torsion_order() == 1 and E.tamagawa_product() == 1
assert E.real_components() == 2 and E.is_minimal()
print("BSD389_GLOBAL_PHASE0_ARITHMETIC_GATES_PASS", flush=True)

R = RealField(120)
omega = R(E.period_lattice().omega(prec=120))
reg = R(E.regulator(proof=True, precision=120))
tam, tors = ZZ(E.tamagawa_product()), ZZ(E.torsion_order())
B = omega * reg * R(tam) / R(tors*tors)
print("BSD389_GLOBAL_REAL_PERIOD_BSD", omega, flush=True)
print("BSD389_GLOBAL_REAL_REGULATOR", reg, flush=True)
print("BSD389_GLOBAL_PREDICTED_LSTAR_SHA1", B, flush=True)

L = E.lseries().dokchitser(prec=120, algorithm="gp")
A = R(L.derivative(1,2))/2
Q = A/B
print("BSD389_GLOBAL_COMPLEX_LSTAR_DOKCHITSER_GP", A, flush=True)
print("BSD389_GLOBAL_NUMERICAL_SHA_RATIO", Q, flush=True)
assert abs(Q-1) < R("1e-10")
print("BSD389_GLOBAL_NUMERICAL_CONSISTENCY_PASS_NOT_A_THEOREM", flush=True)
try:
    LP = E.lseries().dokchitser(prec=100, algorithm="pari")
    AP = R(LP.derivative(1,2))/2
    print("BSD389_GLOBAL_COMPLEX_LSTAR_PARI", AP, flush=True)
    assert abs(AP-A) < R("1e-10")
    print("BSD389_GLOBAL_TWO_ALGORITHMS_NUMERICAL_AGREEMENT_PASS", flush=True)
except (NotImplementedError, ImportError, AttributeError, RuntimeError) as exc:
    print("BSD389_GLOBAL_PARI_OPTIONAL_UNAVAILABLE", type(exc).__name__, str(exc)[:200], flush=True)
print("BOUNDARY: numeric GP/PARI agreement does not certify interval arithmetic", flush=True)
print("BOUNDARY: predicted #Sha=1 is NOT proven, and Sha finiteness remains open", flush=True)
print("BOUNDARY: Sha[16231^infinity]=0 pertains to one prime only", flush=True)
print("BSD389_GLOBAL_PHASE0_NUMERICAL_AUDIT_COMPLETE", flush=True)
