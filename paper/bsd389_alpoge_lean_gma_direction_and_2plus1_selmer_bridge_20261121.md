# E389a1: exact GMA block bridge from Alpöge–Claude RH Lean and why ordinary Hecke congruences cannot bound Sha

Date 2026-11-21. Status: two unconditional algebraic Galois-module lemmas, a checked finite-field regression, a sharp direction-of-inequality obstruction, and one conditional arithmetic research target. **No new finiteness of Sha and no full BSD claimed.**

## 1. Provenance: what the Alpöge–Claude Lean argument actually proves

The paper https://alpo.ge/remark.pdf outlines (i) theta-lift chain divisibility at inert primes on CM curves, (ii) a Bost slope bound for integral automorphic lattices, (iii) a separate congruence-module-to-cocycle estimate. Its author says the lift count scales as m~sqrt(X); auxiliary hosts vary with X.

Actual Lean declaration, in the mirror of the released source:

src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LengthHeckeValueIdealLeDeterminantBound.lean,
namespace GlobalTheory.CutDetOrd, theorem main:

    length_O(O / ccOff) <= length_O(cocRho) + sum_chi length_O(cocChi).

Its proof invokes determinantLemma_discreteValuationRing_quotientLength_bound. This is a **lower bound on the right-hand cohomological mass**, not an upper bound. The same mismatch persists when the right-hand cocycles are interpreted by Selmer groups: the inequality 0 <= length Sha is tautological and cannot bound Sha.

The RH source additionally contains Formalism/SharpRestriction/GrowthBounds/WeilJacquetShalikaLaw.lean, where Conclusion1 is local divisibility of the theta-chain columns, NOT an integral matrix with cokernel equal to the Selmer dual of 389a1.

The Iwasawa window's groups III^1_l(F,h) have coefficients Q_l/Z_l(-h) over abelian CM number fields. These are *not* the elliptic-curve group Sha(E389a1/Q). Also, in the RH guide, E denotes a varying CM host FIELD, not our elliptic curve.

Independent source-oriented guide (preliminary, not refereed):
https://github.com/aapolipponen/rh-lean-check-lumi/blob/main/docs/04-chain-and-one-half.md

## 2. New exact obstruction: ordinary adjoint deformation cannot give E[p] via a direct Galois linear map

Let p>=5 and let V=E[p], with residual image containing -I. Let W=ad^0(V)=trace-zero endomorphisms of V under conjugation. Then

    Hom_{G_Q}(W,V)=0 and Hom_{G_Q}(V,W)=0.

Proof: choose sigma with rho_V(sigma)=-I. Sigma acts as -1 on V but by conjugation as +1 on W. For F:W->V equivariant, F(w)=F(sigma w)=sigma F(w)=-F(w), hence F=0 since p odd. The same proof applies to V->W. QED.

Consequently the standard Wiles/Taylor–Wiles deformation tangent space H^1(Q,ad^0 rho_E) is NOT the Selmer H^1(Q,E[p]) we need for BSD. A numerical congruence ideal associated to the ordinary weight-two E-newform cannot be relabelled as a direct Fitting bound for Sha(E).

This obstruction concerns **direct equivariant maps of coefficient representations**. It does not rule out higher Ext, Eisenstein extensions, derived regulators, or automorphic functoriality.

## 3. New positive repair: a reducible three-dimensional GMA has exactly the correct E[p] block

Let R=V direct_sum F_p with Galois action r(g)=diag(rho_V(g),1), and consider W3=ad^0(R).

The upper-right block

    B = { [[0,0,x],[0,0,y],[0,0,0]] : x,y in F_p }

is G_Q-stable under conjugation. For every g:

    diag(rho_V(g),1) * B(v) * diag(rho_V(g)^(-1),1)
       = B(rho_V(g)*v).

Hence **B is canonically isomorphic to V as a G_Q-module**. It is a direct summand of the G_Q-module W3 (the other matrix blocks are invariant), so H^1(Q,B) is a direct summand of H^1(Q,W3). After using B~V, imposing local Kummer conditions at all places gives precisely the standard mod-p Selmer of E. No Sha finiteness enters this representation-theoretic lemma.

Likewise the lower-left block is V^dual. A reducible 2+1 deformation is therefore the correct *coefficient architecture* if one wants the GMA block-determinant method to see the elliptic Selmer rather than the adjoint Selmer.

**Warning:** It is not proved that any automorphic 3-dimensional deformation / Hecke congruence family actually realizes this residual representation with the desired Bloch–Kato/Kummer local conditions, nor that its congruence ideal bounds the E-block Selmer in the needed direction. The isobaric formal sum rho_E direct_sum 1 is not automatically a regular algebraic cuspidal GL3 representation; the theta lifts in the RH proof cannot simply be specialized to it.

## 4. Sharp finite-level toy countermodel to direction reversal

At a prime p, take a formal Pontryagin Selmer dual

    X_p^toy = Z_p^2 direct_sum (Z/p)^2,

with torsion length 2 and Fitt_2(X_p^toy)=(p^2). Give an unrelated congruence module length zero (unit ideal). The Lean direction

    length(congruence)=0 <= length(cocycles)=2

holds, while the desired reverse bound 2<=0 fails. Both nonzero torsion factors can be paired alternately, mimicking the Cassels–Tate parity requirement. This toy does NOT describe the actual Sha of E389a1.

The genuine project's integral Hecke Smith scalar 2, optimal projector beta*alpha/40 and MW local 2-by-2 matrices still do not produce the missing reverse comparison for E[p].

## 5. The exact arithmetic target for a usable transfer

Sufficient noncircular package:

(A) Construct an **actual arithmetic** 2+1 residual GMA/deformation context with upper-right block V=E[p], at every p outside an explicit finite set, and prove its global and local integral conditions match the strict E-Selmer group after modding out the saturated rank-two MW part.

(B) Produce a fixed finite abelian group C from a p-independent integral automorphic complex (or a fixed nonzero determinant D), constructed before Sha is known, with a justified surjection

    C tensor Z_p --> Sha(E/Q)[p^infty]^dual

for all p outside the finite set. Equivalently, exhibit D in Fitt_2(X_p) for all such p. IMPORTANT: an ordinary adjoint congruence lower bound is not (B), even if it involves the same Hecke eigenvalue.

(C) Establish bounded integrality/denominators across p and the *upper bound* on elliptic Selmer length, with p-local, bad-prime and Tamagawa corrections. Exceptional primes require separate exponent bounds.

Then #Sha[p^infty] divides #C[p^infty] for every covered p, giving a fixed global bound outside the finite set. With exceptional p exponent control this proves Sha finite. There is currently NO established (A)+(B)+(C), so this is a specified research obligation rather than a theorem about actual Sha.

A key distinction from the RH proof: the CM host fields, integral theta chains and determinant ranks vary with the analytic scale X. A family of nonzero D(X) with |D(X)| growing does NOT yield one fixed common annihilator of Sha. A fixed-rank finite integral arithmetic comparison is needed.

## 6. Finite arithmetic regression (assistant executed, not a Sage computation)

verification/bsd389_alpoge_gma_offdiagonal_coefficient_gate_20261121.py
tests at p=5,7,11,107,599, with 16 exact matrix conjugations each and synthetic length-direction checks. All outputs PASS in assistant local Python. The matrix lemma is proven symbolically in section 3; the code only checks samples.

### Explicit finite check for E's non-CM status

For minimal model y^2+y=x^3+x^2-2x, b2=4, b4=-4, b6=1, b8=-3, c4=112 and discriminant 389, so j=c4^3/389=1404928/389, nonintegral. E has no CM (singular moduli are algebraic integers). Local supersingular height-two formal groups may nevertheless become isomorphic after extension; this is NOT a global arithmetic comparison.

## 7. Next actionable direction

Try to locate a *2+1 Eisenstein/congruence* construction (e.g. Klingen-type lift) whose mod-p offdiagonal cocycle is E[p], then test the **direction of its Selmer/Fitting bound**, and only then ask for a single p-independent determinant and slope bound.

This precisely corrects the over-optimistic transfer 'RH determinant -> E Sha' and preserves the rigorous structural insight of the Lean GMA proof.

## 8. New exact Hodge–Tate regularity obstruction for the 2+1 candidate

The rational p-adic representation V_p(E) has Hodge–Tate weights 0 and 1 in a cohomological convention (or 0 and -1 in the dual Tate-module convention). Its trivial 1-dimensional companion has weight 0, so the natural 3-dimensional direct sum V_p(E) plus Q_p has a repeated Hodge–Tate weight 0. It is **not regular**. Thus it is NOT an immediate instance of the regular algebraic GL3 cuspidal automorphic representation theorem invoked for the RH construction.

More generally take R_p(a,b)=V_p(E)(a) direct_sum Q_p(b) with fixed integer Tate twists a,b. The upper-right Galois module of ad(R_p(a,b)) is V_p(E)(a-b). To keep it isomorphic to the untwisted V_p(E) as a p-adic Galois representation one must have a=b: comparing determinants forces cyclotomic^(2(a-b))=1, and the p-adic cyclotomic character has infinite image. But a=b leaves the original Hodge–Tate weight repeated, so the 3-dimensional sum is not regular.

If a!=b removes the repeated weight, the upper-right coefficient is the **wrong twisted motive** V_p(E)(a-b). At the residual mod-p level one could choose a-b divisible by p-1, making cyclotomic^(a-b) trivial mod p; this does not identify the p-infinity Selmer conditions, and choosing such a nonzero twist for all arbitrarily large p requires a twist that depends on p. No fixed nonzero integer k has (p-1)|k for all large p. In fact even an isom of residual representations V[p](k)~V[p] requires (p-1)|2k by determinants, which is impossible for all sufficiently large p unless k=0.

**Precise repair needed:** a nonregular/Eisenstein automorphic deformation and an integral Selmer comparison compatible with the E[p] upper-right block, or a derived comparison that corrects the Tate twist; regular-algebraic GL3 alone does not supply this.

Sources for the regularity/Hodge–Tate distinction: Michael Harris, Takagi notes (https://webusers.imj-prg.fr/~michael.harris/Takagi.pdf); contemporary background on regular algebraic automorphic Galois representations https://arxiv.org/abs/2607.11763 .
