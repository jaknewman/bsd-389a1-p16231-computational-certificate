# UNCONDITIONAL UNIFORM ODD-PRIME Kato theorem for the -3 twist of E=389a1: Sha[p∞]=0 for EVERY p>=5

Date: 2026-11-06. This is a genuinely GLOBAL result for the auxiliary rank-zero twist, valid simultaneously for infinitely many primes and including the bad multiplicative prime 389. No prior p-primary heavy computation is rerun. **The result is for the -3 TWIST, not the original rank-two E.**

## Accepted nonconjectural input fixed in PR #12

Let E/Q: y²+y=x³+x²−2x, conductor 389, and let A=E^(-3): y²+y=x³−3x²−18x−7, conductor 3501. The original E is semistable, non-CM, its mod-p Galois representation is surjective for every p>=11 by Mazur's semistable theorem, and archived independent certificates cover p=5 and p=7. The relevant p-adic image is full for p>=5 (standard lifting lemma from surjective mod-p image with cyclotomic determinant).

The following statements have been independently established in the prior global papers without the BSD conjecture:
- L(A,1)=4 Omega_E^-/sqrt(3) EXACT via the integral optimal modular-symbol / Manin–Drinfeld construction;
- The full real Neron period Omega_A=2 Omega_E^-/sqrt(3), exactly;
- A(Q)_tors is trivial, rank A(Q)=0 (by exact twist central L-nonvanishing / Kolyvagin);
- Tamagawa c_3(A)=2 and c_389(A)=1, all other c_l=1;
- Thus the exact algebraic BSD *analytic* quotient is
  L(A,1)*#A(Q)_tors²/(Omega_A * product_l c_l(A))=1.
No equality with the actual Sha order was assumed.

## Lemma: twist mod-p Galois image remains surjective, for EVERY p>=5

Let p>=5, p!=3 and let rho_p:G_Q→GL_2(F_p) be the surjective representation of E[p]. The only nontrivial quadratic quotient of GL_2(F_p) is the quadratic determinant character, because SL_2(F_p) is perfect for p>=5 and the abelianization of GL_2(F_p) is F_p^× via det. Under the Weil pairing, det rho_p is the mod-p cyclotomic character. Its unique quadratic subextension is
\[
Q(\sqrt{(-1)^{(p-1)/2}p}).
\]
This is NOT the twist quadratic field Q(sqrt(-3)) for p>=5. Hence chi_-3 does not factor through rho_p. It follows that the product map (rho_p,chi_-3) has full image GL_2(F_p)×{±1}: its projection to GL_2 is onto, and its intersection with the kernel (on the character factor) must be all of {±1} because chi does not factor. Therefore the kernel of chi alone also maps surjectively onto GL_2(F_p).

For the twist A=E^(-3), the representation is rho_A,p(g)=chi_-3(g)rho_p(g). Since the chi=+1 fiber already maps surjectively onto GL_2(F_p), rho_A,p is surjective for EVERY p>=5. By the standard p-adic lifting theorem for p>=5 and cyclotomic determinant, the full Tate-module representation to GL_2(Z_p) is surjective. QED.

The argument works equally at p=389 (which is NOT the conductor of chi), because the quadratic field from det mod389 is Q(sqrt(+389)) and not Q(sqrt(-3)).

## Theorem: a genuinely UNIFORM all-p>=5 vanishing statement

Kato's rank-zero upper bound, as quoted with precise conditions by the Sage 10.10 sha_tate.py bound_kato() docstring, states:

If L(A,1)≠0, p is an odd prime at which A has NO ADDITIVE reduction, and the p-adic Galois image is surjective (or suitably Borel), then the p-valuation of the order of Sha(A)[p∞] is at most the p-valuation of
  L(A,1)*#A(Q)_tors²/(Omega_A * product_l c_l(A)).

Source: https://sources.debian.org/src/sagemath/10.10-3/src/sage/schemes/elliptic_curves/sha_tate.py , method bound_kato; underlying Kato, Astérisque 295 (2004). The exact implementation's bad-prime exception list consists of 2, additive reduction primes, residual non-surjectivity exceptions, and prime-square divisors of the analytic BSD order. We use the theorem, NOT an unexecuted Sage output.

For A the **only additive prime is 3**. Its other bad prime 389 is multiplicative, not additive, so every p>=5 meets the reduction condition, INCLUDING p=389.

The Galois-image lemma verifies the surjective-image hypothesis for ALL p>=5. The previously proved exact analytic rank-zero quotient is 1, whose p-adic valuation is zero at every p. Thus Kato's theorem yields
\[
0\le v_p(\#\Sha(A)[p^\infty])\le v_p(1)=0,
\]
for every prime p>=5, without individual p-local computation.

\[
\boxed{\Sha(E^{(-3)}/Q)[p^\infty]=0\quad\text{for EVERY prime }p\ge5.}
\]
This is genuinely uniform infinite-prime support control for the twist.

Since Gross–Zagier–Kolyvagin already proves Sha(A/Q) finite at analytic rank zero, we conclude unconditionally that its order is a power of 2 times a power of 3:
\[
\boxed{\#\Sha(E^{(-3)}/Q)=2^a 3^b\quad(a,b\ge0).}
\]

Cassels–Tate alternating pairing on finite Sha imposes **even exponents** at 2 and 3 (for an elliptic curve with principal polarization): in fact its total order is a perfect square, so a,b are even. Thus Sha(A) has order a square supported only at 2,3.

## Consequence for the BASECHANGE arithmetic of E itself

Quadratic restriction/corestriction for odd p gives exact decomposition
Sha(E/K)[p∞] ≅ Sha(E/Q)[p∞] ⊕ Sha(A/Q)[p∞].

For every p>=5 the twist term just PROVED zero, hence
\[
\boxed{\Sha(E/K)[p^\infty]\cong\Sha(E/Q)[p^\infty]\qquad(\forall p\ge5).}
\]
This includes EVERY good ordinary/supersingular prime and p=389. The unknown global Sha(E/Q) is still open: this theorem removes the twist component uniformly but does not bound the original rank-two primary groups.

At p=3 the twist has additive reduction and Kato's stated rank-zero theorem does not directly apply; at p=2 it excludes the prime. Independent 2/3 descent or another valid theorem is needed to rule out these two remaining twist components.

## Exact scope and STOP RULE

Proven here: one simultaneous arithmetic theorem for infinitely many primes, not a sequence of simulations, with the **original** rank-zero twist and independently proved full algebraic L-value.

NOT proven:
- Sha(E^(-3)/Q)=0 (2- and 3-primary parts remain);
- Sha(E/Q)[p∞] finite or zero at infinitely many non-certified p, because Kato's rank-zero bound has no input when L(E,1)=0;
- an all-prime uniform determinant D for the RANK-TWO curve;
- rationality or exact equality of L''(E,1)/2 with Omega_E Reg_E.

The separate October 2026 low-Selmer-corank *preprint* would give full twist BSD (and twist Sha zero) if its newly claimed theorem is valid, but that CONDITIONAL route is not used in this unconditional Kato conclusion.
