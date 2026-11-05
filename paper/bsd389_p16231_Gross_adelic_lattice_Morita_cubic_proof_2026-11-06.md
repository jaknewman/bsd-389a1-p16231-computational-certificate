# Global comparison of the p2 Gross lattice with Castella--Hsieh Appendix §6

Date 2026-11-06. This is a mathematical lattice proof supplementing actual Sage HNF and quaternionic transport certificates; check the Hecke eigenline gate independently.

Let p=16231, R the maximal left order of the Sage Brandt right ideal I32, B the definite quaternion algebra of discriminant 389, and i_p:R⊗Z_p≈M2(Z_p) the Peirce matrix chart built from the global optimal embedding omega. The chart was certified by 16 product identities modulo p^4 and by a unit determinant; omega is an actual global element of R with omega^2+omega+1=0. Since Z[omega]=O_K is the full ring of integers of K=Q(sqrt(-3)), this is an optimal embedding.

## Lattice identity, for EVERY unit a

In Appendix §6, r_2(a)_p is the upper unipotent matrix [[1,a/p²],[0,1]]; at all other primes r_2(a)_q=1. Let P2(a)=(r_2(a)*Rhat)∩B, a global right R ideal (as fractional lattice).

Multiply by the rational central scalar p². Its p-adic component is the integral right lattice
t_a*M2(Z_p), t_a=[[p²,a],[0,p²]].
For X in M2(Z_p), the conditions X ∈ t_a*M2(Z_p) are equivalent to

p² X11 - a X21 ≡ 0 (mod p^4);
p² X12 - a X22 ≡ 0 (mod p^4).

Indeed the two congruences, since a is a p-adic unit, force p²|X21 and p²|X22. The inverse t_a^{-1}X then has integral entries, and the reverse implication is immediate. At primes q !=p, p² is a unit in Z_q and p²P2(a)_q=R_q. Thus

**J2(a)={x in R: the above two mod-p^4 congruences hold} = p² P2(a)**

as globally integral right R-ideals, provided the Peirce chart is a genuine lift of the specified fixed i_p (which is already proved by the modulo-p^4 matrix unit identities for all congruences used in the computation). The index [R:J2(a)] is p^8, and the HNF in the repository computes exactly this kernel lattice. No sampling of a is needed for the mathematical equivalence.

## Morita transport to Sage's fixed Brandt module

The 33 Sage right ideals I_j are represented with a common right order R0, while R=left_order(I32). The ideal I32 is an invertible (R,R0) quaternionic bimodule. Consequently

**[J] in Cl(R) -> [J*I32] in Cl(R0)**

is an isomorphism of right-ideal class sets; it commutes with unramified Hecke correspondences. This explains why the actual code constructs T(a)=J2(a)*I32 and applies the fixed 33-component Brandt eigenvector V. It represents the same Gross right-ideal class function up to the integral eigenline normalization, not a different CM construction.

A separate exact Sage check of joint Hecke eigenspace dimension one and primitive V is now available at verification/bsd389_p16231_CH_Brandt_unique_JL_eigenline_gate.py. Its PASS still needs user execution.

## Cubic CM unit symmetry for ALL a

The globally embedded omega∈R^× acts by conjugation at p as diag(r0,r1). Therefore

omega * r_2(a) * omega^{-1} = r_2(mu*a),

where mu=r0/r1 modp² is a nontrivial cubic root of unity. Since omega is a unit of the GLOBAL order R at every finite prime, conjugation changes the right ideal by left multiplication by omega and a right unit. Thus J2(a), J2(mu*a), J2(mu²*a) have identical right ideal class under R, for every a in (Z/p²Z)^×. This establishes the cubic symmetry and the factor 3 for the entire class sum, not merely the four user-tested anchors.

## Principal-unit coordinate and ambiguity of Artin reciprocity

The quotient of local units modulo cubic global units is (Z/p²Z)^×/mu3, cyclic of order p(p−1)/3=H. The previously authenticated generator g=5+3omega of norm19 yields ratio w=138112843, decomposed uniquely into the Teich part tau and principal part u^s, where u=1+p and s=10816 modp. Thus

i_n=s*n modp, for 0<=n<H,

is precisely its coordinate in the p-Sylow quotient, once the Artin reciprocity identification has been fixed. Using geometric vs arithmetic reciprocity can invert this coordinate. Any such ambiguity changes i by multiplication by a nonzero scalar modulo p and therefore changes its quadratic binomial coefficient sum by a nonzero square (plus lower-moment terms); since M0=M1=0 modp the **nonvanishing of M2** is unaffected. Its specific value 4083 and normalized 3739 are tied to the stated generator/convention.

## What this mathematical proof does and does not close

It identifies the Gross lattices at all primes and all conductor-p² units and proves the cubic reduction for the entire ring-class orbit, with its Brandt-module Morita transport. The published Appendix §6 then transfers the finite degree-2 unit coefficient to the actual infinite theta modulo p, subject to the well-defined theta normalization (primitive eigenvector up to Z_p unit) and the application of Chida--Hsieh's functional equation. The separate formal lemma in paper/bsd389_p16231_exact_Iwasawa_order2_bridge_formal_lemma_2026-11-06.md derives exact order2 when the constant coefficient is zero and the functional equation applies.

None of these arguments alone determines the order of Sha[p∞]; a Selmer-dimension theorem is also required. Theorem B of Castella--Hsieh and their auxiliary-character existence results are possible routes to that consequence.
