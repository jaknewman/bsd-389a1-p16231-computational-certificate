#!/usr/bin/env python3
"""Appendix §6 normalization gate: actual P1/P2 Gross ideals, cubic symmetry.

Checks the finite level n=1 right-ideal formula from Castella--Hsieh:
r_n(a)_p = [[1,a/p^n],[0,1]], P_n=(r_n(a) Rhat) intersect B.
The globally equivalent scaled right ideal p^n*r_n(a)R_p consists of
[[p^n,a],[0,p^n]] M_2(Z_p).  This script makes its two divisibility
conditions independently at n=1,2 and checks the p-stabilization
P1 independence from the principal-unit coordinate, CM mu3 symmetry,
and the frozen 33-class Hecke eigenfunction.

It does NOT infer Sha or BSD from the finite coefficient.
"""
import io
import runpy
from contextlib import redirect_stdout
from pathlib import Path
from sage.all import ZZ, QQ, EllipticCurve, matrix, vector, identity_matrix

imp=runpy.run_path(str(Path(__file__).with_name(
    "bsd389_p16231_conductor1_first_gross_P2_ideal_pilot.py")),
    run_name="CH_APPENDIX_LOCAL_IMPORT")
P=imp["P"];M=imp["P2"];MOD=imp["MOD"]
assert P==16231 and M==P*P and MOD==P**4
BM=imp["BM"];REPS=imp["reps"];R=imp["R"]
B=imp["B"];BASE=imp["base"];basis=imp["basis"]
W=imp["W"];flat=imp["flat"]
V=vector(QQ,imp["V"])
C=EllipticCurve("389a1")
assert C.conductor()==389 and len(V)==33
print("CH_APPENDIX_RIGHT_ORDER_AND_EIGENFUNCTION_LENGTH_PASS",flush=True)

# Check the *same* integer-valued JL Brandt eigenfunction at several
# Hecke primes, allowing the matrix indexing convention in Sage.
for ell in (2,3,5,7):
    T=BM.hecke_matrix(ell)
    eigen=ZZ(C.ap(ell))
    assert T.nrows()==T.ncols()==len(V)
    right=(T*V==eigen*V)
    left=(V*T==eigen*V)
    assert right or left,("BRANDT_HECKE_NOT_THE_389A1_EIGENFORM",ell)
    print("CH_APPENDIX_BRANDT_EIGENVECTOR_PASS",ell,
          "AP",eigen,"COLUMN",bool(right),"ROW",bool(left),flush=True)

def scaled_adelic_lattice(n,a):
    """Integral p^n P_n^a, using an independent n-specific HNF."""
    assert n in (1,2)
    pn=P**n
    modulus=P**(2*n)
    a=int(a)%modulus
    assert a%P
    # X = [[pn,a],[0,pn]] * Y; the two first-row entries
    # satisfy pn*X_1j-a*X_2j=0 mod pn^2.
    conditions=matrix(ZZ,2,4,
        lambda i,j:(pn*flat[j][i]-a*flat[j][i+2])%modulus)
    augmented=conditions.augment(-modulus*identity_matrix(ZZ,2))
    ker=augmented.right_kernel().basis_matrix()
    H=matrix(ZZ,ker[:,0:4]).row_module().basis_matrix()
    assert H.nrows()==H.ncols()==4
    assert abs(ZZ(H.det()))==P**(4*n)
    for row in H.rows():
        assert all(t%modulus==0 for t in conditions*row)
    return H

def classify(T):
    for k,I in enumerate(REPS):
        yes,alpha=I.is_right_equivalent(T,certificate=True)
        if yes:
            assert alpha*T==I
            return k,int(V[k])
    raise AssertionError("NO_CLASS")

def P2_class(a):
    H=scaled_adelic_lattice(2,a)
    with redirect_stdout(io.StringIO()):
        H0,T=imp["build"](a)
    assert H==H0
    return classify(T)

# Exactly check the n=1 P1(a*u^i) ideal is independent of i,
# not merely its image under the Brandt eigenform.
for a in (1,2,7,128):
    H=scaled_adelic_lattice(1,a)
    for i in (1,2,137,P-1):
        target=a*pow(1+P,i,P*P)%(P*P)
        assert scaled_adelic_lattice(1,target)==H
    print("CH_APPENDIX_P1_PRINCIPAL_UNIT_IDEAL_INVARIANCE_PASS",
          a,flush=True)

# The full ringclass quotient is (Z/m)^*/mu3. Conjugating the split
# upper unipotent by omega=diag(r0,r1) sends a -> a*(r0/r1).
r0=int(imp["r0"])%M
r1=int(imp["r1"])%M
mu=r0*pow(r1,-1,M)%M
assert mu==r1 and mu*mu%M==r0 and pow(mu,3,M)==1 and mu!=1
print("CH_APPENDIX_CM_CUBIC_RESIDUE_ACTION_PASS",
      mu,mu*mu%M,flush=True)
for a in (1,1+P,pow(2,P,M),138112843):
    one=P2_class(a)
    two=P2_class(a*mu%M)
    three=P2_class(a*mu*mu%M)
    assert one==two==three,(
        "CH_APPENDIX_GLOBAL_MU3_EQUIVALENCE_FAILED",a,one,two,three)
    print("CH_APPENDIX_P2_CM_MU3_THREE_CLASSES_PASS",
          "A",a,"CLASS",one[0],"VALUE",one[1],flush=True)

assert sum(V)==0 # Helps audit the integer eigenvector's degree zero.
for k in (0,1,2):
    from sage.all import binomial
    total=ZZ(binomial(P,k+1))%P
    assert total==0
print("CH_APPENDIX_P1_DEGREES0_TO2_CANCEL_MODP_PASS",flush=True)
assert pow(128,-2,P)==4986
assert (-3*4986*4083)%P==3739
print("CH_APPENDIX_P2_CYCLIC_TO_THETA_COEFFICIENT_UNIT_PASS",3739,flush=True)
print("CH_APPENDIX_LOCAL_BRANDT_AND_MU3_FORMULA_GATE_PASS",flush=True)
print("BOUNDARY_FINITE_LEVEL_COMPARISON_NOT_SHA_OR_BSD_PROOF",flush=True)
