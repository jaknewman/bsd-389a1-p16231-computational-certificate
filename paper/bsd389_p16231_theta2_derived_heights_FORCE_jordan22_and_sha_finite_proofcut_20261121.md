# E389a1, p=16231 — anticyclotomic theta T² forces the true Selmer Jordan type (2,2)

Date: 2026-11-21. **New, direct theorem-level consequence from Castella--Hsieh (2022), their derived-height filtration and ONE-SIDED anticyclotomic characteristic divisibility.**

This document REMOVES the need for a separately constructed nonzero action of
T=gamma−1 on the true Selmer module. It is NOT an independent rerun of the
user's 87,809,710 Gross class computations, and is NOT a proof of
Sha[16231∞]=0, all-prime global Sha finiteness or exact complex BSD.

## 1. Genuine Selmer and analytic setup

E/Q: y²+y=x³+x²−2x (389a1), N=389, full MW rank 2,
basis P=(-1,1), Q=(0,-1), rational torsion 0.
p=16231, good ordinary (a_p(E)=128), p splits in
K=Q(sqrt(-3)) because 16231≡1 mod 3.
389≡2 mod3, so 389 is inert: N^−=389 (one factor,
squarefree), N^+=1. Residual E[p] ramified at 389
since v_389(Delta_min)=1, via the nontrivial
Tate unipotent inertia. These meet the conditions
of Castella--Hsieh Theorem 4.1.
The archived exact real interval for the twist
has 4.51 < L(E^(-3),1) < 4.60, so
Sel(Q,V_p(E^(-3)))=0 by the rank-zero theorem.
Therefore S=Sel(K,V_pE)=Sel(Q,V_pE) as the
complex-conjugation (+)-eigenspace, and
  s=dim_Qp S >= rank E(Q)=2.

Let K_infty/K be the anticyclotomic Z_p-extension,
Lambda=Z_p[[T]], J=(T), and
  X_ac = Sel_{p∞}(E/K_infty)^vee
be the ACTUAL full Bloch--Kato Selmer dual,
NOT a relaxed/one-sided Selmer group.

**Primary source:** F. Castella and M.-L. Hsieh,
*On the nonvanishing of generalised Kato classes for elliptic curves
of rank 2*, Forum of Mathematics, Sigma (2022),
Theorem 4.1 and eqs. (5.9)--(5.10), proof of Theorem A
(§5.5), plus the Bertolini--Darmon/Pollack--Weston
one-sided divisibility quoted there:
https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864

## 2. Height filtration restricts the possible Jordan blocks

By Castella--Hsieh Theorem 4.1, there is a descending
filtration S^(i) on S and derived p-adic heights
  h^(i):S^(i)×S^(i) -> J^i/J^(i+1) ⊗ Q_p,
whose radical equals S^(i+1).
Cornut--Vatsal's universal-norm vanishing in the
definite (N^− odd) case makes S^(infinity)=0.

Their Theorem 4.1 states:
 - h^(i) is symmetric for odd i, alternating for even i;
 - h^(i)(tau x,tau y)=(-1)^i h^(i)(x,y).

Since tau is +1 on all of S here, h^(i)=0 when i
is ODD (p is odd). Consequently the corresponding
jumps e_i=dim(S^(i)/S^(i+1)) vanish for odd i.
For even i, the induced nondegenerate alternating
height form forces e_i to be EVEN.

Set e_(2r)>=0, even integers, with finite support.
Then the actual Selmer corank is
  s = sum_(r>=1) e_(2r).
The Iwasawa J-primary characteristic multiplicity
from Theorem 4.1(e), eq. (5.10) is
  v_J(char_Lambda X_ac) = sum_(r>=1) 2r * e_(2r).
Therefore the genuine arithmetic inequality
  **v_J(char X_ac) >= 2*s**
holds at p=16231. It is NOT true for an arbitrary
torsion module with the same characteristic series.

## 3. One-sided main-conjecture divisibility gives the OPPOSITE inequality

The Bertolini--Darmon divisibility, refined by
Pollack--Weston and invoked by Castella--Hsieh
in the proof of Theorem A (§5.5, eq. (5.10)), is
  **(char_Lambda X_ac) ⊇ (Theta_(f/K)^2).**
This direction means that char(X_ac) DIVIDES Theta²
as an ideal. Hence
  **v_J(char X_ac) <= 2*ord_T Theta**.

Do not reverse this inclusion or substitute
a characteristic ideal of a DIFFERENT signed/relaxed
Selmer module. The referenced article uses
the exact X_ac as defined in §4.

## 4. The crucial equality and the forced two Jordan blocks

Suppose the archived full finite Gross coefficient
is correctly identified with Castella--Hsieh
Appendix §6's true Theta_(f/K), so that the
exact lower coefficients vanish and
  Theta_(f/K)=T²*U(T), U(0)∈Z_p^×.
Then ord_T Theta=2, and the three inequalities give

  **4 <= 2*s <= v_J(char X_ac) <= 4.**

Therefore s=2 and v_J(char X_ac)=4.
Moreover e_2=2 and e_i=0 for all i!=2:
since the e_(2r) are EVEN, and the total weighted
sum is 4, the only possible profile is e_2=2.

Castella--Hsieh Theorem 4.1(e) therefore yields
the ACTUAL Selmer pseudo-isomorphism
  **X_ac ~ (Lambda/(T²))^{⊕2} ⊕ M'**
where char(M') is prime to T.
Since the one-sided divisibility and Theta=T²U
imply char(X_ac) divides T^4, and v_J=4,
the characteristic ideal is EXACTLY
  **char(X_ac)=(T^4)**.
Thus char(M')=(1), i.e. M' is pseudo-null (finite
over Z_p); after removing finite kernels/cokernels,
  **X_ac ~ (Lambda/(T²))^{⊕2}.**

In particular, on the J-primary rational
localization the operator T has EXACT
Jordan type [2,2], with
  dim_Qp(W/TW)=2,
  rank_Qp(T|W)=2,
  T²|W=0,
where W is the J-primary module after inverting p
(not the whole rationalized module if other
characteristic factors existed).

This is the sought "nontrivial T-action" BIT,
PROVED WITHOUT independently constructing a class
and, indeed, strengthened to an exact Jordan type.
The stronger structure uses the derived-height
arithmetic and cannot be inferred from
char=(T⁴) for arbitrary modules.

Finally s=2 and rank E(K)=2 imply the
Q_p/Z_p-corank of Sha(E/K)[p∞] is zero.
This p-primary group is cofinitely generated,
therefore FINITE. Restriction-corestriction of
degree [K:Q]=2, prime to p, injects the
p-primary Sha(E/Q) into Sha(E/K), so
  **Sha(E/Q)[16231∞] is FINITE.**

This is a theorem CONDITIONAL only on authenticating
the theta order-two input in the true Gross
theta normalizations; NOT conditional on additional
analytic auxiliary conductor-53 characters,
the generalized Kato Theorems A+B, an independently
constructed Selmer Jordan matrix, or the full
two-sided Iwasawa main conjecture.

## 5. Precise finite theta input and current provenance boundary

The user's archived **FULL** computation at p=16231 has
  H=p(p-1)/3 = 87,809,710
right-ideal orbit classes,
  raw moments (M0,M1,M2)=(0,0,4083) mod p.
Using the actual ordinary unit root,
  alpha_p^(-2)=128^(-2)=4986 mod p,
the first finite theta coefficients are
  (0,0,-3*4986*4083)=(0,0,3739) mod p.
The square leading coefficient is 3739²=5230 mod p,
a unit. The code checks these in plain Python.

The complete source identification is addressed in
  paper/bsd389_p16231_Gross_adelic_lattice_Morita_cubic_proof_2026-11-06.md
and authenticated (user-reported) PASS gates:
  results/bsd389_p16231_FULL_87809710_USER_PASS_2026-11-05.md
  results/bsd389_p16231_CH_appendix_local_formula_USER_PASS_2026-11-06.md
  results/bsd389_p16231_final_cubic_closure_PASS_2026-11-06.md.
The universal lattice identity of the paper is
  J_2(a)=p²*P_2(a)
for ALL units a modulo p² (not just samples),
with fixed Morita transport by the 33-class
Brandt ideal I32, and cubic global CM unit symmetry.

Castella--Hsieh Appendix §6 provides
  Theta_infty ≡ Theta_1 mod ((1+T)^p-1).
Reducing mod p, (1+T)^p-1 ≡ T^p, so the
quadratic coefficient transfers unchanged mod p.

For EXACT zeros below T²:
- L(E,1)=0 because E has certified rank two and
  nonzero central L would imply MW rank zero.
  By interpolation, Theta(0)² is a nonzero
  explicit factor times L(E/K,1)=0.
  Thus Theta(0)=0 exactly.
- Chida--Hsieh's theta functional equation
  in the N^+=1, global-sign +1, local-good-p-sign
  +1 branch gives Theta^*=Theta. For
  T↦-T/(1+T), comparing T coefficients
  with zero constant gives a1=0 exactly.
- a2 ≡ 3739 !=0 mod p, hence ord_T Theta=2.

**Remaining distinction:** The previous computations
are authentic USER-REPORTED runs in the repository,
not a NEW independent execution of all 87,809,710
Gross steps in the present conversation. The
global identification of the finite norm19 stream
with the article's exact theta coefficients is
proved in accompanying mathematical notes and
checked by sampled Sage certificates; this turn
does not add an independent end-to-end byte
replay of the native full stream. It would be
incorrect to claim an entirely independent,
machine-checked unconditional Sha certificate
based on the short Python audit alone.

**What is now eliminated as unnecessary:**
- constructing and verifying a global cohomology
  class with T-action ≠0 as a separate "Jordan bit";
- assuming an unproved two-sided Iwasawa main
  conjecture;
- choosing a regular conductor-53 aux character
  merely to pass through Theorems A+B;
- computing an expensive p² or p³ theta
  conductor layer merely to prove exact T-order,
  provided the functional-equation and first
  layer input are genuine.

**What is NOT proved:**
Sha[16231∞] triviality (only finiteness); a
uniform all-large-p support bound for Sha;
the exact complex BSD leading-term formula.

## 6. Mathematical audit of the earlier misleading NO-GO argument

The earlier formal-model note
  paper/bsd389_theta_p16231_higher_fitting_vs_characteristic_analytic_rank2_false_proof_audit_20261121.md
gave three artificial modules A,B,C of identical
characteristic ideal (T⁴) whose augmentations
have different ranks/torsion. Those are
CORRECT abstract counterexamples: characteristic
ideals alone cannot detect augmentation ranks
without extra structural hypotheses.

However, module B=(Lambda/T)^4 CANNOT model the
true anticyclotomic Selmer under Theorem 4.1:
it has FOUR odd-degree J-primary jumps,
whereas tau=+ and the derived-height alternating
symmetry forces all odd jumps to vanish.
Module C can model finite residual p-torsion;
hence the argument establishes FINITENESS, NOT
triviality, of the p-primary Sha component.

The prior research request to "build a true
Selmer presentation and show TW!=0" is
mathematically redundant for p16231 once
the theta2 input and the genuine derived-height
theorems are certified.

## 7. Reproduction

  python verification/bsd389_p16231_derived_height_jordan_gate_20261121.py

This short script verifies the stated Frobenius trace,
finite Gross moment normalization, unique allowable
even-jump profile and formal Jordan model.
It does not perform the 87-million-step Gross orbit
or reconstruct the actual Selmer complex.

Core sources:
- Castella--Hsieh (2022), Theorem 4.1, eq. (5.10), §5.5
  https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864
- Chida--Hsieh, *Special values of anticyclotomic L-functions*,
  Theorem B/4.8 (the theta functional equation):
  https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf
- Project's authentic finite theta and conductor-53
  records cited above.
