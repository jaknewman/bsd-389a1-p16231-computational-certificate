# E389a1: uniform precise p^2 auxiliary Frobenius, independent Kummer directions, and universal-norm no-go

2026-11-21. This is a **new unconditional existence/density theorem** for
precise arithmetic auxiliaries at each prime p with surjective mod-p Galois
image, plus two new complete *particular* Kurihara certificates. It DOES NOT
prove that any two-factor Kurihara number is nonzero for all p, the finiteness
of global Sha, or the complex BSD leading-term identity.

E/Q: y²+y=x³+x²-2x, conductor 389, saturated MW generators
P=(-1,1), Q=(0,-1). Fix p>=5 with rho_{E,p} surjective. LMFDB
reports this for all p; Serre's semistable uniform theorem alone suffices
for every p>=11. The determinant of the p-adic Tate representation is the
full p-adic cyclotomic character.

Sources:
- Serre lifting lemma, e.g. Lombardo, Bounds for Serre's open image theorem,
  Lemma 3.14: https://arpi.unipi.it/retrieve/e0d6c92c-5181-fcf8-e053-d805fe0aa794/Bounds%20for%20Serre%27s%20Open%20Image%20Theorem.pdf
- LMFDB E389a1: https://www.lmfdb.org/EllipticCurve/Q/389a1/
- Kummer pairing and finite division fields: Silverman,
  The Arithmetic of Elliptic Curves, VIII §1.
- Rank-two unit Kurihara/Fitting comparison: Kim, Theorem 1.8,
  https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
- Companion norm obstruction:
  paper/bsd389_ranktwo_euler_norm_lift_integrality_and_tame_local_obstruction_20261121.md

## 1. The full joint field has independent Kummer and p² torsion kernels

Let V=E[p]=Fp², K1=Q(E[p]),
  M=K1([p]^{-1}P,[p]^{-1}Q),
  K2=Q(E[p²]),
  L=M K2,
  G=Gal(K1/Q)=GL2(Fp).

**Lemma 1.** Gal(M/K1)=V², as a G-module with two natural copies
of V.

Proof. It is a G-stable subgroup H of V². If it is proper,
the semisimple G-module V² has a nonzero G-equivariant
functional V²->V vanishing on H; since End_G(V)=Fp,
this is (v,w)->a v+b w with (a,b)!=(0,0). Then the
global Kummer class of aP+bQ restricts to zero on G_{K1}.
The restriction H¹(Q,V)->H¹(K1,V) is injective by Sah's lemma:
the central element 2I of G acts on V by 2!=1. Thus
aP+bQ belongs to p E(Q), contradiction with the
saturated full MW basis. Therefore H=V². QED.

**Lemma 2 (Serre).** Gal(K2/K1)=Mat₂(Fp), through
1+p B modulo p².

Proof. Reduction rho_p is full GL2(Fp). For p>=5, the
closed commutator subgroup of the p-adic image contains
SL2(Zp) (Serre lifting lemma). The determinant is the
full cyclotomic Zp^×, so the whole image is GL2(Zp).
Taking the kernel modulo p² proves the claim. QED.

**Lemma 3.** M and K2 are linearly disjoint over K1.

Proof. The Galois group of an intersection J=M∩K2,
viewed as a quotient of Gal(M/K1)=V² and of
Gal(K2/K1)=Mat₂(Fp), is a G-module. The central
element -I of G acts as -1 on V², but trivially on
Mat₂(Fp) by conjugation. Since p is odd, no nonzero
common G-quotient can have both actions. Therefore
J=K1. QED.

Consequently the Frobenius distributions of Kummer
translations (vP,vQ) and of the p² matrix lift,
conditional on mod-p Frobenius A0, are independent
and uniform in V² and Mat₂(Fp), respectively.
This is a genuinely global independence theorem;
it does not rely on Sha finiteness.

## 2. Exact density of auxiliary primes with BOTH valuations one

Take U=[[1,1],[0,1]] in GL2(Fp). Its centralizer
has order p(p-1), hence its conjugacy class has
density 1/[p(p-1)] in G.

Fix A0=U. Every lift A in GL2(Z/p²) is uniquely
of the form
  A=[[1+p alpha,1+p beta],[p gamma,1+p delta]]
mod p², with four arbitrary Fp parameters.
The elementary determinant identities are:
  det A = 1+p(alpha+delta-gamma) mod p²,
  det(I-A) = -p gamma mod p².
At any good prime q with Frobenius A:
  det A=q mod p²,
  det(I-A)=#E(Fq) mod p².
Therefore the simultaneous conditions
  v_p(q-1)=v_p(#E(Fq))=1
are EXACTLY
  gamma!=0, alpha+delta-gamma!=0 mod p.
These are two independent nonzero linear forms
on a 4D Fp-space. There are p²(p-1)² eligible
lifts of the p⁴ possible lifts, proportion
  (1-1/p)².

For a given unipotent U, the image of U-I is
the line Fp e1. The local reduction Kummer
quotient V/(U-I)V is one-dimensional, represented
by the e2 coordinate. Since the p-th root
fields have independent translations, the two
Kummer residues for P and Q are independently
uniform in Fp. Requiring one to be NONZERO and
the other ZERO has proportion (p-1)/p².

By Chebotarev, each of the two conjugacy-stable
sets of primes has the EXACT density
  [1/(p(p-1))] * [(p-1)²/p²] * [(p-1)/p²]
  **= (p-1)²/p⁵ > 0.**

**Theorem 4 (unconditional given full rho_p).**
There exist disjoint infinite sets Q_P(p), Q_Q(p),
each of density (p-1)²/p⁵, such that every q
in each set satisfies
  p||(q-1), p||#E(Fq), Frob on E[p]
  nontrivially unipotent, and
  E(Fq)/pE(Fq) ~ Fp,
with reduction row (P,Q) equal to (nonzero,0)
for Q_P and (0,nonzero) for Q_Q.

Thus for EVERY qP in Q_P and qQ in Q_Q,
the rank-two MW localization
  (E(Q)/p) -> E(F_qP)/p (+) E(F_qQ)/p
is an isomorphism and has UNIT determinant mod p.
All p-adic valuation-one auxiliary eligibility
requirements are met simultaneously.

## 3. Stronger equidistribution of ALL p+1 local MW directions

More generally the pair of reductions
([P]_q,[Q]_q) in Fp² is uniform. For any
prescribed projective ratio/direction
lambda in P¹(Fp), the set with the resulting
NONZERO local row spanning lambda and both
exact valuation-one conditions has density
  **(p-1)²/p⁵**.
There are p+1 possible projective rows.
The density of primes with a NONZERO MW row and
the two exact valuation-one conditions is
  **(p+1)(p-1)²/p⁵**.

This is exact finite Galois equidistribution, not
a heuristic independence assumption or an
effective upper bound on the FIRST such prime.

## 4. Universal local norm obstruction at the SAME selected primes

For such q, q=1 mod p and E[p] is unramified at q.
The local cyclic degree-p subfield L_{p,q} of Q(mu_q)
is totally tamely ramified at q.

Local Tate duality (proved in the companion norm paper)
gives
  im(Cor:H¹(L_{p,q,w},E[p])->H¹(Q_q,E[p]))
  ∩ H¹_ur(Q_q,E[p]) = 0.
The local Kummer image of a global MW class is
unramified at q. If it is a corestriction, its
reduction in E(Fq)/p must therefore vanish.

Choose qP in Q_P(p) and qQ in Q_Q(p).
For v=a kappa(P)+b kappa(Q) in E(Q)/p:
- being a global corestriction from L_{p,qP}
  forces a=0 modulo p;
- being a global corestriction from L_{p,qQ}
  forces b=0 modulo p.
Hence **NO nonzero MW/p class can be a simultaneous
global corestriction from both cyclic degree-p fields**.

This establishes the formerly prime-specific no-go
UNIFORMLY for EVERY p with surjective mod-p image,
without choosing explicit auxiliary primes.

It is a theorem about norm/corestriction lifts of
existing MW classes, NOT a proof that Sha has
no extra Selmer classes or that every Kurihara
two-factor coefficient is a unit.

## 5. New exact p5 and p7 full Kurihara witnesses with pure MW directions

An independent exhaustive C++ Manin continued-fraction
computation with the archived 390-coordinate normalized
plus-symbol vector (SHA256 of shifted numeric vector:
31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee)
gave the following FULL two-factor moment vectors:

| p | (q1,q2) | all units | (M00,M10,M01,M11) mod p |
|---|---|---:|---|
| 5 | (41,61) | 2,400 | (0,0,0,4), frozen regression |
| 5 | (61,991) | 59,400 | (0,0,0,3), NEW |
| 7 | (2423,8597) | 20,819,512 | (0,0,0,5), NEW |

For p5:
  q61: a_q=-8, #E(Fq)=70, row (P,Q)=(unit,0);
  q991: a_q=-53, #E(Fq)=1045, row (P,Q)=(0,unit).
For p7:
  q2423: a_q=30, #E(Fq)=2394, row (0,unit);
  q8597: a_q=58, #E(Fq)=8540, row (unit,0).
All four also have p||(q-1) and p||#E(Fq).

The first p5 regression was independently authenticated
using Sage/eclib in an earlier user-run certificate.
The two NEW computations share its exact *frozen*
integral 390-Manin vector and continued-fraction
algorithm; this is not an independent fresh extraction
of the modular-symbol vector from Sage/eclib.
An optional separate Sage audit is appropriate
before treating the new values as publication-ready.

Reproducible checks:
 verification/bsd389_p2_precise_auxiliary_chebotarev_gate_20261121.py
 verification/bsd389_primitive_p2_kurihara_cpp_audit_20261121.cpp
Both were locally compiled/executed by the assistant with
PASS outputs. The former verifies the finite p²
matrix-lift census at p=5,7,11,13 and the four
genuine local elliptic point-count/point-law rows.
The latter computes the three complete Kurihara sums
and tests the known regression.

## 6. THE HARD REMAINING STEP, explicitly separated

Although we can force both local MW directions and exact
p-adic auxiliary valuations at every prime p, this
does NOT imply the corresponding two-factor Kurihara
coefficient is nonzero. If Sel(Q,E[p]) has dimension
>2 because of additional Sha[p], Kim's theorem
forces ALL two-factor mod-p Kurihara coefficients
to vanish even though our selected MW localization
matrix is invertible.

Thus "choose good auxiliaries by Chebotarev" is now
completely solved, including the p² valuation gates.
The genuinely missing input is a new *global*
nonvanishing/primitivity argument for the rank-two
derived Kato system, or an independently constructed
p-uniform integral Fitting element.

Nothing in these theorems alone proves full Sha
finiteness or the complex exact leading-term BSD
identity. In particular no integer D satisfying
D∈Fitt_2(Sel_{p∞}^vee) for all large p is constructed.
