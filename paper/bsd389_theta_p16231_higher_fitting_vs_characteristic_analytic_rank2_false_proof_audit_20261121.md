# E389a1: the exact higher-Fitting obstruction hidden by a quadratic anticyclotomic theta unit

2026-11-21. **Formal theorem, explicit three-module counterexample, and audit of a recent unrefereed rank-two BSD claim.**
No unconditional full Sha finiteness, p16231 Sha finiteness, or complex leading-term BSD identity is claimed.

E/Q: y^2+y=x^3+x^2-2x, N=389, MW rank2, true full basis
P=(-1,1), Q=(0,-1).
p=16231, K=Q(sqrt(-3)), Gamma~Z_p, Lambda=Z_p[[T]],
T=gamma-1, involution iota(T)=(1+T)^(-1)-1=-T/(1+T).

## 1. Upgrade of the archived 87,809,710-class Gross theta moment

The authentic user-computed full finite Gross theta record is
  results/bsd389_p16231_FULL_87809710_USER_PASS_2026-11-05.md
with raw first three moments (0,0,4083) modulo p.
The normalized coefficient is exactly
  a2 = -3*4986*4083 = 3739 mod 16231 != 0.
Its square is
  a2^2 = 5230 mod 16231 !=0.

The existing conditional arithmetic-to-analytic source proof cut is
  paper/bsd389_p16231_theta_firstlayer_invariant_2jet_to_sha_finiteness_proofcut_20261121.md
It includes the normalization, sign, and genuine Appendix 6
right-ideal provenance condition. THIS CONDITION IS NOT
automatically verified by the new formal algebra below.

**Theorem 1 (pure local Iwasawa algebra).** Suppose an integral
theta element Theta(T) in Lambda REALLY corresponds to
the archived finite theta and satisfies
   Theta(0)=0 EXACTLY,
   Theta'(0)=0 EXACTLY,
   [T^2]Theta == 3739 mod p.
Then
   Theta(T)=T^2*U(T), U in Lambda^×,
   (Theta)=(T^2),
   mu(Theta)=0, lambda(Theta)=2.
If the associated (definite) anticyclotomic p-adic
L-function is defined by
   L_ac(T)=Theta(T)*iota(Theta(T)),
then
   L_ac(T)=T^4*V(T), V in Lambda^×,
   (L_ac)=(T^4),
   mu(L_ac)=0, lambda(L_ac)=4,
   V(0)=U(0)^2 == 5230 mod p.

Proof. By exact vanishing of the first two coefficients,
Theta/T² lies in Lambda and has constant term a2,
a p-adic unit; so is itself invertible.
The involution has iota(T)=-T/(1+T), hence
  iota(Theta)=T²/(1+T)² * U(iota(T)).
The remaining factor V=U(T)*U(iota(T))/(1+T)² is a unit.
Its constant coefficient is a2². QED.

This theorem is a REAL strengthening of "ord_T=2",
but only for the correctly normalized genuine theta,
conditional on the previously documented source cut.

The usual definite p-adic L-function is a square/product
of theta with its involution, NOT theta itself:
see e.g. https://www.sciencedirect.com/science/article/abs/pii/S0022314X23000744
for an explicit construction of L_p=Theta Theta^*.

## 2. THE EXACT ALGEBRAIC NO-GO: characteristic ideal cannot control Sha corank

**Theorem 2 (three indistinguishable characteristic ideals).**
Let R=Z_p[[T]]. Consider the finitely presented torsion
R-modules
  A = (R/(T²)) (+) (R/(T²)),
  B = (R/(T)) (+) (R/(T)) (+) (R/(T)) (+) (R/(T)),
  C = A (+) (R/(p,T)) (+) (R/(p,T)).
All three have the SAME characteristic ideal:
  char_R(A)=char_R(B)=char_R(C)=(T⁴).
They have the same Iwasawa invariants mu=0, lambda=4.

Indeed the height-one characteristic multiplicities
come only from A and B's T-primary cyclic factors.
R/(p,T) is a FINITE R-module supported in codimension
two (pseudo-null), invisible to characteristic ideals.

Yet under augmentation R->Z_p, T->0:
  A/(T)A ~= Z_p²,
  B/(T)B ~= Z_p⁴,
  C/(T)C ~= Z_p² (+) (F_p)².

Their SECOND Fitting ideals are
  Fitt_{2,R}(A)=R,
  Fitt_{2,R}(B)=(T²),
  Fitt_{2,R}(C)=(p,T)².
After augmentation the respective ideals are
  Z_p,  (0),  (p²).

Proof. For A and B, diagonal relations are respectively
diag(T²,T²) and diag(T,T,T,T), so take 0x0 and 2x2
minors as required by Fitt_2. For C use 4 generators
and the six relations with columns
  (T²,0,0,0), (0,T²,0,0),
  (0,0,p,0), (0,0,T,0),
  (0,0,0,p), (0,0,0,T).
The 2x2 minors generate exactly (p²,pT,T²)=(p,T)².
Base change of Fitting ideals under T->0 yields the
displayed augmentations. QED.

Thus even assuming an INTEGRAL ANTICYCLOTOMIC
MAIN CONJECTURE char_R(X_ac)=(L_ac)=(T⁴),
the characteristic equality by itself cannot distinguish:

- augmented torsion-free rank2 (A);
- augmented positive excess corank2 (B);
- augmented rank2 WITH NONZERO finite paired p-torsion (C).

This respects the even p-primary Cassels--Tate pairing
constraint for the synthetic finite alternative C.
These are formal module countermodels, NOT actual
Selmer modules of E389a1.

This is why an assertion "lambda_ac=4 => Selmer corank 2"
or "mu_ac=0 => degree-two Kurihara unit" cannot follow
from a characteristic-ideal main conjecture alone.

## 3. POSITIVE, sharp conditional theorem using second Fitting augmentation

Let M be a finitely presented torsion Lambda-module,
and assume an authentic finite-kernel/cokernel Iwasawa
control comparison (after tensoring Q_p) between
M/TM and the Pontryagin dual of the TRUE
Bloch--Kato Selmer group Sel_{p∞}(E/K).
Assume rank E(K)=2 (as in the project, rank E(Q)=2
and twist E^(-3)(Q) has rank 0).

**Proposition 3.** If
   Fitt_{2,Lambda}(M) evaluated at T=0
is a NONZERO ideal of Z_p (NOT NECESSARILY UNIT),
then Sha(E/K)[p∞] is finite; consequently
Sha(E/Q)[p∞] is finite for odd p.

Proof: Fitt base change gives a nonzero Fitt_2
ideal of M/TM. Over Q_p, the 2nd Fitting ideal
is nonzero precisely when the Q_p-dimension of
(M/TM) tensor Q_p is <=2. Under the assumed
control, corank Sel(E/K)<=2. The rank-two
Kummer injection gives >=2, so its cokernel
Sha(E/K)[p∞] has corank zero, hence is finite.
The degree-two restriction-corestriction on
Sha from Q to K is multiplication by 2, a
p-unit, so the Q-p-primary Sha component
injects and is finite. QED.

**What cannot be asserted:** the known p16231 theta
moment does NOT produce this 2nd Fitting element
of an ACTUAL anticyclotomic Selmer module.
Nor does char(M)=(Theta*Theta^*) ensure
Fitt_2(M)|_{T=0} !=0, as explicit B shows.
The correct Selmer local conditions, control
morphism and the higher-Fitting comparison
must be specified and proved, not inferred
from a main conjecture for a different module.

A still stronger condition that Fitt_2(M)|0 is
the UNIT ideal gives no p-torsion in the
augmented controlled module if an integral
finite-kernel/cokernel-free control theorem
is also available; we do not assume such
strong integral control here.

**Arithmetic takeaway:** A genuine augmented
Fitt2 nonzero witness is a sharply formulated
single-prime finite-Sha proof, while a
p-INDEPENDENT family of such comparisons with
a single nonzero integer D would tackle the
global uniform support. The theta quadratic
unit solves only the analytic factor, not the
integral comparison.

## 4. AUDIT of a March 2026 public "complete rank-two BSD" preprint

Wang Xiong, *The Birch and Swinnerton-Dyer Conjecture
for Analytic Rank Two: A Complete Proof via Definite
Anticyclotomic Iwasawa Theory*, ResearchGate,
March 2026 (unrefereed):
https://www.researchgate.net/publication/401385931_The_Birch_and_Swinnerton-Dyer_Conjecture_for_Analytic_Rank_Two_A_Complete_Proof_via_Definite_Anticyclotomic_Iwasawa_Theory

The posted manuscript's Section 17.2 and following
invoke the assertion
  corank_Zp Sel_{p∞}(E/Q) <= analytic_rank(E)=2
as "[Kat04, Theorem 17.4]". This is NOT a
general Kato theorem in analytic rank two.
Theorem 17.4 is cited in the Stein--Wuthrich
Iwasawa study to prove cotorsion of a
cyclotomic Iwasawa Selmer dual as a
Lambda-module, NOT this corank bound:
https://wstein.org/papers/works/works.pdf
§6.1, printed p.20-21.

At Section 17.5 the manuscript asserts that
"all but finitely many primes" are ordinary.
But Elkies' 1987 theorem proves that EVERY
elliptic curve over Q has infinitely many
SUPERSINGULAR primes:
https://people.math.harvard.edu/~elkies/math_pubs.html

The same section infers global finiteness from
p-primary finiteness at varying p. This
is FALSE without finite p-support:
  G= direct_sum_{p prime} (Z/pZ)^2
has each G[p∞] finite of square order, while
G itself is infinite. Even establishing
every p-primary component finite would
not prove global Sha finiteness.

Finally the manuscript uses Cassels--Tate
alternation/square order of FINITE Sha to
deduce nonexistence of infinite divisible
Sha components. Alternation on the finite
reduced quotient does NOT supply such a
bound on the corank of the divisible subgroup.
The synthetic module B in Section 2 shows
the relevant module-theoretic logical gap.

**Verdict:** its claimed all-rank-two
finiteness conclusion does not follow from
its arguments, and it is not a legitimate
source for our missing p-uniform Sha proof.
These are concrete false inferences, not
an argument based merely on peer-review status.

For comparison, D. Zagier's 2026
*BSD Dichotomy* preprint explicitly notes
that no rank>=2 elliptic curve is currently
known to have its FULL Sha finiteness proved:
https://people.mpim-bonn.mpg.de/zagier/files/preprints/BSD_Dichotomy.pdf
This contextual observation is NOT used
as a mathematical premise.

## 5. Exact next arithmetic experiment

A valid next certificate would:
1. Identify the TRUE anticyclotomic Selmer
   module M and the exact local conditions;
2. Produce a finite presentation or genuine
   derived Selmer complex (not only its
   characteristic series);
3. Compute the image under augmentation of
   a genuine 2nd Fitting generator/determinant;
4. Establish the required Selmer control
   at augmentation and rank-two Kummer image;
5. Prove nonvanishing of this image without
   assuming Sha finite.

For uniform global support, the construction
must vary coherently with p and have a fixed
nonzero rational/integral bound. No such
uniform arithmetic element is currently
constructed. The complex exact BSD
leading-term comparison is also separate.


## 6. Stronger one-bit sufficient criterion: prove a nontrivial algebraic Bockstein/Jordan block

Assume for THIS PARAGRAPH ONLY:
(A) an actual anticyclotomic Selmer dual M of E/K is a
    finitely generated torsion Lambda-module with
    char_Lambda(M)=(T^4) (as would follow from the
    correctly normalized theta and an appropriate full
    main conjecture);
(B) a TRUE rational control theorem gives
    M/(T)M tensor Q_p ~= X_p(E/K) tensor Q_p;
(C) E(K) has MW rank 2 and the p-Selmer corank
    over K is even (for p odd this follows here
    from decomposing E over K into E and its
    quadratic twist, with their individually
    proven Q-parity properties).

Then set W=M tensor_{Z_p} Q_p. The absence of p-power
char factors and the characteristic polynomial
T^4 imply W is 4-dimensional over Q_p, with
T acting nilpotently (Jordan blocks all at zero).
Write b for the number of T-Jordan blocks and
j for rank_{Q_p}(T:W->W). Rank-nullity gives
    b=dim_{Q_p}(W/TW)=4-j.

By the rational control theorem, b is the p-Selmer
corank of E/K, hence b>=2 (MW rank) and b is even.
Since b<=4, we have **b in {2,4}**.

Therefore the following remarkable equivalence holds
under the stated genuine arithmetic inputs:

   **T acts NONTRIVIALLY on W  <=> b=2
       <=> Sha(E/K)[p^infty] is finite.**

More quantitatively:
- T=0 on W => b=4; the Selmer has excess
  corank 2 and Sha(E/K)[p^infty] infinite.
- T!=0 on W => j>=1, b<=3; parity forces
  b=2 (hence j=2), and Sha finite.

This is an EXACT ONE-BIT arithmetical certificate
rather than a full determinant calculation:
one need only exhibit ONE actual Selmer Iwasawa
cohomology class x, not killed by multiplication
by gamma-1 after inverting p.

But the word "actual" is indispensable: the
nontrivial T-variation of the ANALYTIC theta
does NOT prove nontrivial T-variation of the
ALGEBRAIC Selmer module without a derived
comparison or some extension-class calculation.
Indeed modules A and B have the same theta-based
characteristic ideal, but T acts nontrivially
on A and zero on B.

This one-bit criterion is CONDITIONAL on (A)-(C);
the present work does NOT establish the
underlying arithmetic comparison. It is a
genuinely weaker *target* than computing the
entire Fitt2 determinant once char=(T^4)
and p-Selmer parity are supplied.

For rank 2 and p=16231, E^(-3)(Q) has rank 0
by the project’s archived twist L-value/rank-zero
certificate, so rank E(K)=2. The exceptional
Gross source-normalization cut remains to be
independently closed before asserting (A).
