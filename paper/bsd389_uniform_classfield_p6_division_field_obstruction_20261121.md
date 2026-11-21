# E389a1: a class-field-theoretic p^6 obstruction to nonzero Sha[p]

Date: 2026-11-21. Status: rigorous uniform **necessary condition** for p-primary Sha at eligible p, not a proof that the necessary condition fails for all sufficiently large p.

Let E/Q be the minimal curve
  E: y^2+y=x^3+x^2-2x
with discriminant 389, conductor 389, MW rank two, rational torsion zero, and global root number +1. The reduction at 389 is split multiplicative of type I_1 with Tamagawa factor 1. Its identity component over F_389 is F_389^× of order 388=4*97.

Fix a good p>=5, p not in {97,389}, and suppose the mod-p Galois image is GL_2(F_p), as is established for this curve. Let V=E[p], K=Q(E[p]), G=Gal(K/Q), and

  d_p = dim_Fp Hom_G(Cl(K)/p Cl(K), V).

Let r_p=dim_Fp(E(Q_p)/p E(Q_p)). Since p>=5 and E has good reduction at p, the local formal group is p-torsionfree and E(Q_p) has a Z_p direct summand of rank one. Hence

  r_p = 1 + dim_Fp E(Q_p)[p] in {1,2}.

When p does not divide #E(F_p), r_p=1. In the anomalous case r_p may be one or two; no unproved universal non-anomaly assertion is needed.

## Theorem: exact unconditional class-group inequality

For every such p,

  **d_p >= dim_Fp Sel(Q,E[p]) - r_p
         = 2 + dim_Fp Sha(E/Q)[p] - r_p.**

Consequently, if Sha(E/Q)[p] != 0, then

  **p^4 divides h(K)**,

and if moreover p does not divide #E(F_p), then

  **p^6 divides h(K)**.

Thus, for all sufficiently large good NON-ANOMALOUS primes, a prime-independent theorem asserting `v_p(h(Q(E[p]))) <= 5` would imply Sha(E/Q)[p] = 0. At anomalous primes, the sufficient numerical threshold is `v_p(h(Q(E[p]))) <= 3`. Such a class-number theorem is NOT established here or in any cited paper.

## Proof: restriction of the strict Selmer kernel to the division field

1. Put S_p=Sel(Q,E[p]). Let

       S_p^str = ker(S_p -> H^1(Q_p,E[p])).

   All Selmer classes localize at p into the Kummer image E(Q_p)/pE(Q_p), of F_p-dimension r_p. Therefore

       dim S_p^str >= dim S_p - r_p.

   The definition imposes a *zero* local condition at p. No assumption that a global MW point is locally primitive is necessary for this inequality.

2. For all finite primes l not in {389,p}, E has good reduction and p != l. By the Neron--Ogg--Shafarevich criterion, E[p] is unramified and local Kummer classes are unramified. Therefore every S_p^str class, restricted to a completion K_w for w|l, is unramified.

3. At the unique bad prime l=389, E has split multiplicative I_1 reduction. Its reduction filtration consists of a pro-389 formal kernel and a residue torus F_389^× of order 388, with component group of order 1. Thus E(Q_389)/pE(Q_389)=0 for p>=5, p!=97,389. Every Selmer localization at 389 is zero. Accordingly restriction to K_w is unramified there as well.

4. At primes above p, the strict localization is zero by definition, so its restriction to K_w is also zero. At infinite places there are no p-primary ramification complications (p odd); K contains Q(mu_p) and is totally imaginary.

5. Inflation--restriction yields an injection

       H^1(Q,E[p]) -> H^1(K,E[p])^G.

   Indeed H^1(G,V)=0 by Sah's lemma: the central scalar 2I is in GL_2(F_p), acts as multiplication by 2 on V, and 2-1 is invertible modulo p. As E[p] is trivial over K,

       H^1(K,V) = Hom_cont(G_K,V).

   Step 2--4 show that the image of S_p^str is unramified at every finite place of K. Global class field theory identifies such homomorphisms with Hom(Cl(K),V), and equivariance gives the injection

       S_p^str -> Hom_G(Cl(K)/p,V).

   Combining dimensions proves the inequality.

6. Rank E(Q)=2 and E(Q)_tors=0 give Kummer's exact sequence

       0 -> F_p^2 -> S_p -> Sha[p] -> 0.

   Hence dim S_p=2+dim Sha[p]. The parity theorem (global root sign +1) implies the divisible Sha corank is even, and Cassels--Tate's perfect alternating pairing on the finite reduced p-primary quotient implies its p-torsion dimension is even (p odd). Thus if Sha[p] is nontrivial, dim Sha[p]>=2. Consequently dim S_p>=4.

7. The ordinary local Kummer dimension r_p is at most 2, so the inequality gives d_p>=2. In the nonanomalous case r_p=1, it gives d_p>=3.

8. **Elementary G-module lemma:** Let M be an F_p[G]-module and V an absolutely irreducible 2-dimensional G-module with End_G(V)=F_p. If d=dim Hom_G(M,V), then M has a G-equivariant surjection onto V^d. To see this, choose a basis f_1,...,f_d of Hom_G(M,V). If F=(f_1,...,f_d):M->V^d were not surjective, its image would be a proper subrepresentation of the *semisimple* G-module V^d. The latter has a nonzero G-equivariant projection V^d->V that kills the image. Such a projection is a nontrivial F_p-linear combination of the coordinate projections by Schur's lemma, contradicting the independence of the f_i. Therefore F is surjective.

   Applied to M=Cl(K)/p, the lemma implies `p^(2d_p) | h(K)`. As d_p>=2 in general, and >=3 for nonanomalous p, we obtain the claimed p^4 and p^6 divisibilities. QED.

## Stronger inequality in terms of the actual class-number valuation

Because 2d_p<=v_p(h(K)),

   dim_Fp Sha[p] <= floor(v_p(h(K))/2) + r_p - 2.

The right-hand side is an actual integer arithmetic upper bound, derived without presuming finiteness of Sha, but it depends on the p-class group of the highly varying division field K. In particular a small class-number valuation would give a zero Sha[p] upper bound, as above.

## Why this does NOT yet prove global finiteness

- We have not proved a theorem bounding v_p(h(Q(E[p]))) by 5 (or 3 at anomalous primes) for all sufficiently large p. Existing Selmer/class-group comparison results predominantly yield *lower* bounds on the standard Galois-isotypic class-group component, not the required eventual *upper* bound.
- Even such a theorem would prove only that Sha has finite prime support. Independent p-primary finiteness at the remaining finitely many primes is still required to prove full finiteness.
- The standard Weil/Tate class-field machinery is not by itself a global upper bound on class numbers of the tower of growing division fields.
- The known unramified extension of K forced by the rank-two Mordell--Weil group (even when Sha=0) means that the naively stronger statement p does not divide h(K) is generally impossible: at every nonanomalous p in the theorem, the inequality already implies p^2 divides h(K), independently of Sha.

Mathematical predecessors: Dipendra Prasad and Sudhanshu Shekhar, *Relating Tate-Shafarevich group of an elliptic curve with class group*, and follow-up papers on class groups of torsion fields. Their Selmer/class-group inequality provides the key idea; the above p^4/p^6 specialization and explicit 389-adic torus condition are its application to E389a1.

Primary reference: https://mathweb.tifr.res.in/conferences/mpnts2020/nts2020/Dipendra_Prasad.pdf , main theorem/slides 2020 (semistability, residual irreducibility, Selmer and class-group comparison). Additional background: https://www.sciencedirect.com/science/article/pii/S0022314X24001434 .


## Precise sufficient uniform statement (conditional, and currently unproved)

Let S be a finite set of primes containing {2,3,97,389}. Assume
there is a number B such that, for all good p>B with p not in S,

* if p does not divide #E(F_p), then p^6 does NOT divide h(Q(E[p]));
* if p divides #E(F_p), then p^4 does NOT divide h(Q(E[p])).

Then Sha(E/Q)[p]=0 for every such p. By p-primary torsion,
Sha(E/Q)[p^infty]=0. It follows that Sha has FINITE PRIME
SUPPORT. If the finitely many residual p-primary groups are
separately known finite, then the ENTIRE Sha is finite.

The displayed hypotheses are entirely ordinary number-field
class-number assertions and do not themselves mention Sha.
They are not known and are genuinely stronger than the
statement we wish to prove, since the V-isotypic class group
may contain classes unrelated to elliptic Selmer.

A basic size warning: when the mod-p image is GL2(F_p),
  [Q(E[p]):Q]=(p^2-1)(p^2-p).
For p=5,17,23,16231 these degrees are respectively
  480, 78336, 267168, 69399181987336800.
Therefore this criterion is principally a target for
a NEW structural class-number theorem; computing
the whole class number separately for large p is not a
viable uniform algorithm.

The field K contains Q(mu_p), so the root discriminant
of K is already at least
  p^((p-2)/(p-1)).
This grows with p. Classical discriminant/root-discriminant
lower bounds for high-degree unramified extensions therefore
do not by themselves force the absence of unramified
p-extensions as p grows. In particular do NOT infer the
desired p^6 nondivisibility merely from Hermite--Minkowski
or Brauer--Siegel.

**VERDICT:** We have proved a genuinely uniform arithmetic
necessary condition on a different family of finite groups,
not an unconditional tail theorem. Claiming global Sha
finiteness here would be circular.
