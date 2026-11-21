# E389a1 / p=16231: first-layer invariant theta 2-jet, exact source criterion and Sha finiteness proof cut

Date 2026-11-21. **Mathematical theorem and bounded verification,
not an unconditional certificate of full BSD or of Sha[16231]=0.**

The work closes one *normalization obstacle* from the earlier Gross
theta route: changes of anticyclotomic generator, Teich representative,
CM cubic unit and primitive Jacquet--Langlands eigenline do not change
the nonvanishing of the normalized T^2 coefficient modulo p, as long
as they are the legitimate automorphisms of the same published
theta construction. The last outstanding responsibility is **source
identity/provenance**: the H-point computation must genuinely
enumerate the right ideals of Castella--Hsieh Appendix §6.

Sources checked against the published, visually inspected pages:

- F. Castella, M.-L. Hsieh, *On the non-vanishing of generalised
  Kato classes for elliptic curves of rank 2*, Appendix §6 p.26
  formula for Theta_{f/K,n} and its finite-to-infinite congruence;
  Theorems A and B:
  https://web.math.ucsb.edu/~castella/Kato.pdf
- M. Chida, M.-L. Hsieh, *Special values of anticyclotomic
  L-functions for modular forms*, Theorem B / Thm 4.8,
  functional equation:
  https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf

## 1. Actual archived computational inputs

Set p=16231, K=Q(sqrt(-3)), N(E)=389 (inert in K),
alpha_p = 128 (mod p), and H=p*(p-1)/3=87809710.

The user's complete Sage/C++ norm-19 cyclic Gross theta run
(recorded on 2026-11-05):
  results/bsd389_p16231_FULL_87809710_USER_PASS_2026-11-05.md
reported
  (M0,M1,M2) = (0,0,4083) modulo p,
  sha256 of the fully sealed stream = 
  00467ec028517a10c2b6340311e2657601d589039bf62d73315419d312630286
  (digest from the archived user's reported log; not independently
  recreated in the current assistant environment).

A separate explicit source-lattice mathematical proof is at
  paper/bsd389_p16231_Gross_adelic_lattice_Morita_cubic_proof_2026-11-06.md
and the real user-run local source gate at
  results/bsd389_p16231_CH_appendix_local_formula_USER_PASS_2026-11-06.md.
The primitive single-dimensional Hecke eigenline is certified at
  results/bsd389_p16231_CH_JL_unique_primitive_eigenline_USER_PASS_2026-11-06.md.
The later full checkpoint and cubic CM return are audited by
  verification/bsd389_p16231_norm19_full_theta_postrun_audit.py
which reads the authentic saved user JSONs.

The exact normalized arithmetic is
  alpha_p^(-2) = 4986 mod p,
  c2 = -3*4986*4083 = 3739 mod p !=0.
The P1 contribution has zero degrees 0,1,2 modulo p because
  sum_{i=0}^{p-1} binom(i,j)=binom(p,j+1)=0 mod p
for j=0,1,2.

## 2. Universal second-binomial-moment transformation lemma

For a finite coefficient function F: F_p -> F_p define
  M0=sum_i F(i),
  M1=sum_i i F(i),
  M2=sum_i binom(i,2) F(i).
A change of index i' = u*i + b with u in F_p^×
and b in F_p changes the moments (by relabelling) as

  M0'=M0,
  M1'=u M1 + b M0,
  M2'=u^2 M2 + (u(u-1)/2 + u b) M1
                   + b(b-1)/2 M0.

**Proof:** the polynomial identity
  binom(ui+b,2)
   = u^2 binom(i,2) + (u(u-1)/2+ub)*i + binom(b,2)
holds in F_p[i] for odd p. Summing against F proves the
identities. QED.

If M0=M1=0, then
  **M2'=u^2 M2**.
So M2 !=0 iff M2' !=0, for ANY generator automorphism
and any fixed principal-unit translation. Multiplication
of the Gross parameter by an integral split-chart unit
just permutes Teich indices and shifts the common
principal-unit coordinate. A change of ring-class
Artin generator is an automorphism of the cyclic
p-part and rescales u; inversion is u=-1. They
cannot cancel a nonzero second moment.

The integral JL eigenline is rationally 1-dimensional
and primitive. Two such p-integral primitive eigenfunctions
for the **same Jacquet--Langlands transfer** differ by a
p-adic unit. Their weighted theta coefficients therefore
differ by a p-adic unit. A Morita equivalence of maximal
orders merely transports right-ideal classes and the
eigenfunction together. The global mu_3 quotient contributes
the factor 3, which is a p-unit at p=16231.

**Boundary:** the lemma covers changes that truly act by
these automorphisms on the **same arithmetic theta datum**.
It does not prove that an arbitrary different quaternionic
orbit or wrong global order yields the correct theta datum.

## 3. Source-lattice identity: a non-sampling proof condition

The Appendix uses r_2(a) with p-part
  [[1,a/p^2],[0,1]]
and the right R ideal
  P_2(a) = (r_2(a) Rhat) intersect B.

The project's integral lattice is
  J_2(a)={X in R:
    p^2 X11-a X21=0 mod p^4,
    p^2 X12-a X22=0 mod p^4},
in an integral Peirce chart R tensor Z_p=M2(Z_p).

For every unit a mod p^2, direct inversion of
  t_a = [[p^2,a],[0,p^2]]
shows
  **J_2(a)=p^2 P_2(a)**
as globally integral right R lattices (at all primes
other than p, the central p^2 is a unit). The
congruences force both X21,X22 divisible by p^2;
the remaining conditions say exactly that
t_a^(-1)X is integral.

The fixed invertible (R,R0) bimodule I32 transports J2(a)
to the 33-class right R0 Brandt module, preserving
unramified Hecke eigenfunctions. The full order embedding
omega in R has omega^2+omega+1=0, and conjugation by
omega identifies the three unit-related classes
a,mu*a,mu^2*a for EVERY a. The norm-19 ratio w has order
H modulo global mu3, yielding a complete class orbit
once its exact oriented transport has been certified.

**Important:** the exact lattice proof relies on the
computed Peirce chart being the actual lift of the
same global R and omega in the authenticated full
theta stream. The archived universal lattice proof
and sampled Sage source tests support that, but a
new independent re-derivation of every native edge
witness was not carried out in this turn.

## 4. Formal infinite-theta order-two lemma (full proof)

Let F(T)=a0+a1 T+a2 T^2+... in Z_p[[T]], p odd.
Suppose:
(a) F(0)=a0=0 exactly;
(b) a1=0 mod p and a2!=0 mod p;
(c) F(-T/(1+T))=eps*U(T) F(T) with
    eps=±1 and U(T) in 1+T Z_p[[T]].

Then **a1=0 exactly and ord_T(F)=2**.

Proof: the T coefficient yields -a1=eps*a1.
If eps=+1 then 2a1=0 so a1=0.
If eps=-1 and U=1+u1*T+..., the T^2 coefficient gives
  2a2=-(1+u1)a1.
Since a1 is divisible by p and a2 is a unit, this is
impossible modulo p. Thus eps=+1 and a1=0. QED.

For the actual Castella--Hsieh theta series,
their Appendix congruence says
  Theta_infty = Theta_1 mod ((1+T)^p - 1).
Reducing mod p yields equality of its first p coefficients
because (1+T)^p-1=T^p in F_p[[T]]. Hence the actual
source c2=3739, if correct, transfers to a2!=0.

The trivial-character interpolation of Theta_infty
has square proportional to L(E/K,1). Because rank E(Q)=2,
the rank-zero theorem gives L(E,1)=0 and therefore
L(E/K,1)=L(E,1)L(E^(-3),1)=0. Thus a0=0 exactly.
The Chida--Hsieh functional equation has U(T)=1 in
the N^+=1 case, and eps=±1. The lemma now forces
  ord_T Theta_infty = 2.

NO n=2 or n=3 *theta* computation is required to deduce
the order from this first finite layer once the source
identity, trivial zero and functional equation apply.
This is logically sharper than extrapolating from
c0=c1=0 only modulo p.

## 5. Theorem-level Selmer implication: exactly what is and is not finished

Castella--Hsieh Theorem B gives a nonzero generalized
Kato class from ord_T Theta=2 when their Theorem A
hypotheses are satisfied. Their Theorem A then yields
  dim_{Q_p} Sel(Q,V_p E)=2.

At p=16231, E is good ordinary (a_p=128 nonzero modp),
389 is inert in K=-3, p splits in K,
the mod-p representation is irreducible and ramified
at 389, and E has root number +1 and rank two.
The separate user's exact real-interval certificate
establishes L(E^(-3),1)>0. For such triples,
the Appendix §6 explicitly invokes the analytic
existence results of Vatsal/Chida--Hsieh to provide
an auxiliary ring-class character with the needed
nonzero Rankin L-value. The project also has its own
53-tower regularity/existence certificate.

Therefore we have the following **rigorous conditional
computer-assisted theorem**:

  IF the full archived 87,809,710-point Gross
  computation is a correct source-normalized evaluation
  of the Appendix §6 theta element (as its
  all-a lattice identity and postrun checks aim
  to certify), THEN
      dim_{Q_16231} Sel(Q,V_16231 E)=2
      and Sha(E/Q)[16231^infty] is FINITE.

Proof: ord_T theta=2 as above; Theorems B, A;
then Kummer gives corank_Zp Sha[p∞]
=dim Sel(V_pE)-rank E(Q)=2-2=0.
As Sha[p∞] is cofinitely generated, corank zero
implies it is finite. QED.

**Not established here:** the p-adic valuation/order of
that finite group, its triviality, finiteness of all
other p-primary Sha components, an independent byte-level
audit of the entire long native computation, or the
strong complex BSD leading-term equality.

Crucially, "p-unit theta c2" does NOT imply
"unit Fitt2(X_p)" without an integral regulator/main
conjecture comparison. Theorem A gives *rational*
Selmer dimension, not Sha[p∞]=0.

## 6. Reproducibility and exact next cut

The newly committed
  verification/bsd389_p16231_theta_firstlayer_invariance_20261121.py
was run by the assistant in a local Python environment:
  BSD389_THETA_P1_LOW_DEGREES_VANISH_PASS
  BSD389_THETA_GROSS_CLASS_COUNT_PASS 87809710
  BSD389_THETA_FINITE_C2_UNIT_PASS 4986 4083 3739
  BSD389_THETA_AFFINE_ORIENTATION_INVARIANCE_PASS
  BSD389_THETA_FUNCTIONAL_SIGN_AND_LINEAR_VANISHING_FORMAL_LEMMA_PASS.

It does NOT recompute user-owned Gross classes. To certify
the remaining computational hypothesis without re-running
the expensive stream, reuse the existing full postrun audit:
  verification/bsd389_p16231_norm19_full_theta_postrun_audit.py.
For global source identification, use the
  verification/bsd389_p16231_castella_hsieh_appendix_local_formula_gate.py
together with the universal lattice proof in §3.

Current status: proven normalization/functional 2-jet lemmas,
authentic archived Gross finite result, and a precisely
identified source-completeness proof cut. No unqualified
claim of p16231 Sha finiteness.
