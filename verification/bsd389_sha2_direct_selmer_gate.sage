# E389a1: independent 2-primary Sha gate using Sage's 2-Selmer implementation.
# Run: sage verification/bsd389_sha2_direct_selmer_gate.sage
# A zero 2-Selmer Sha bound (assuming certified MW rank) proves Sha[2]=0,
# hence Sha[2^infinity]=0. The result is NOT known prior to the user's run.
from sage.all import *
E = EllipticCurve("389a1")
assert E.ainvs() == (0,1,1,-2,0)
assert E.conductor() == 389
print("SHA2_CURVE_PASS", E.ainvs(), flush=True)

# The rank-two basis and its saturation were independently certified earlier
# in this research project; check proof-mode rank locally rather than infer
# rank from conjectural analytic BSD data.
try:
    r = E.rank(proof=True)
    print("SHA2_RANK_PROVED", r, flush=True)
except Exception as exc:
    print("SHA2_RANK_NOT_CERTIFIED", type(exc).__name__, str(exc), flush=True)
    raise

assert r == 2, "Certified MW rank must equal 2"

# Official Sage docs: returns dim_F2 Sha[2] with certified algebraic rank.
b = E.sha().two_selmer_bound()
print("SHA2_TORSION_DIMENSION_UPPER_BOUND", b, flush=True)
if b == 0:
    print("SHA2_PRIMARY_ZERO_PASS", flush=True)
else:
    print("SHA2_NONZERO_BOUND_ONLY", b, flush=True)
print("BOUNDARY_SHA_ALL_PRIMES_NOT_PROVED", flush=True)
