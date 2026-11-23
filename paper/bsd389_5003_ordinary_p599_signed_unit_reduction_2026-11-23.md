# E389a1, 23 Nov 2026 — certified 5003-prime ordinary range and a signed supersingular Sha criterion

**Status.** A published unconditional finite-range Sha result and an elementary **general** signed-Selmer unit lemma are proved here. The p=599 conductor-p² integral moment has been recomputed independently in JavaScript from an authenticated integer Manin input. The conversion from that moment to the *publishedly normalized* signed Pollack p-adic L-function remains a **source-sensitive independent gate**. Until it is independently certified, the p599 Sha-vanishing application below is conditional, not promoted as a new unconditional theorem. None of this proves all-prime Sha finiteness or strong complex BSD.

## A. Exactly what Stein–Wuthrich already prove (2013)

Stein–Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. **82** (2013), Theorem 12.3, printed page 1788 ([author PDF](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=32)), proves for E=389a1 that Sha[p]=0 at p=2 and **all 5005 good ordinary primes** p<48859 except p=16231. The literal "5005" counts the good ordinary p=3 and all good ordinary p>=5; the theorem *excludes* 16231 from its conclusion.

Directly sieving [5,48859) gives 5022 primes, of which 5021 are good (p !=389). The list of excluded supersingular p is:
  107,599,1049,2957,6661,8263,9397,9551,14633,15101,28591,30671,30869,31799,34781,36263,45161.
The only other ordinary exception is 16231. Therefore **5003** good ordinary p>=5 are proved Sha[p]=0 by Stein–Wuthrich. Adding the archived separate proof-grade p=107 Iwasawa/Kurihara certificate yields **5004** good primes p>=5 within that finite interval known to have Sha[p∞]=0.

For each of these primes, any nontrivial p-primary torsion group would have a nontrivial p-torsion element; hence Sha[p]=0 implies Sha[p∞]=0. The remaining **17 good** not covered by these inputs are
  599,1049,2957,6661,8263,9397,9551,14633,15101,16231,28591,30671,30869,31799,34781,36263,45161.
p=389 is bad and outside this good-prime list. This is a finite-range statement, **NOT** a bound on possible Sha prime divisors and NOT a uniform all-large-p theorem.

Stein–Wuthrich’s proof is a large published computation accepted here as an external arithmetic theorem, **not** independently rerun. The p=107 addition uses the separately archived user report and its stated computational provenance.

## B. An elementary rank-r signed Iwasawa criterion (new clean formulation)

Let E/Q be a semistable elliptic curve, p>=5 a good supersingular prime, E(Q)[p]=0, MW rank r, residual mod-p image sufficiently large that E[p∞](Q∞)=0. Let Q∞/Q denote the cyclotomic Zp-extension and Lambda=Zp[[T]], T=gamma-1.

Assume the following *actual arithmetic*, not formal synthetic, inputs:

(1) The minus signed cyclotomic Selmer dual X^- is torsion over Lambda and its characteristic ideal equals the **genuinely normalized** Pollack minus p-adic L-function (L_p^-(T)). This is proved for semistable E and supersingular p>2 by Burungale–Skinner–Tian–Wan (arXiv:2409.01350v2, Theorem 1.3).

(2) X^- has **no nonzero finite Lambda-submodule**. B. D. Kim, *The plus/minus Selmer groups for supersingular primes*, J. Aust. Math. Soc. 95 (2013), Theorem 1.1 supplies precisely this when the signed Selmer is cotorsion, under its local hypotheses (minus branch needs no extra split hypothesis).

(3) Restriction injects the ordinary Selmer group over Q into the Gamma-invariants of the minus signed Selmer group over Q∞, with the full divisible rank-r Mordell–Weil subgroup in its image. For p>=5, residual GL2(Fp)-surjectivity implies E[p∞](Q∞)=0, so global H1 restriction is injective by inflation-restriction. At the base level, rational local Kummer classes lie in the minus trace-norm conditions. Non-p local conditions agree in the relevant semistable Tamagawa-p-unit setting.

**Proposition.** Under (1)–(3), if the coefficient [T^r] L_p^-(T) is a p-adic unit, then
\[
\boxed{\Sha(E/\mathbb Q)[p^\infty]=0.}
\]

**Proof without assuming Sha finite.**

Let S=Sel_{p∞}(E/Q). Its divisible MW subgroup (Qp/Zp)^r injects into Sel^-∞^Gamma, so the Zp-rank of X^-/TX^- is >=r. Each summand in the elementary-divisor decomposition of the Lambda-torsion module X^- which contributes to its coinvariant rank contributes at least one to ord_T char(X^-). Therefore ord_T L_p^- >=r. Since the coefficient of T^r is a p-unit, L_p^-(T)=T^r U(T), U(0)∈Zp×; in particular char(X^-)=(T^r) and mu=0.

By the Lambda structure theorem X^- is pseudo-isomorphic to a direct sum of Lambda/(T^{e_j}), sum e_j=r. Since X^- has no finite Lambda-submodule, it embeds with finite cokernel in the latter Zp-free rank-r module. Thus X^- is itself Zp-free of rank r.

The action A=T on X^- is nilpotent over Qp, but
  rank_Qp(X^-/TX^-)>=r=rank_Zp(X^-);
therefore A=0 on X^-⊗Qp, hence A=0 integrally (X^- Zp-torsion-free). Thus X^-≈(Lambda/T)^r and
  Sel^-∞^Gamma ≈(Qp/Zp)^r.
The rank-r divisible MW subgroup injects into this latter group. An injection of two copies of (Qp/Zp)^r of the same finite rank is an isomorphism (Pontryagin dual of an injective endomorphism is a surjective automorphism of the finite free Zp-module). The ordinary Selmer over Q lies between the MW subgroup and signed∞^Gamma; hence it equals MW, and its Kummer quotient Sha[p∞]=0. QED.

**Important:** A nonzero [T^r] *formal* p-adic series, a numerical BSD ratio, or a coefficient belonging to a differently normalized de Rham component is insufficient; it must be the genuine analytic signed L_p^- of (1).

## C. Genuine p599 data and the remaining normalization gate

For E389a1 at p=599, a599=0 and the curve is semistable with residual GL2(F599) image. The archived full conductor-p² modular-symbol computation and a separate integral 390-Manin reconstruction yield, at p²=358801:
  179101 plus-symmetry representatives,
  (C0,C1,C2)=(0,0,543) mod 599.
The p599 independent integer-Manin source is on the existing branch
  proof/p599-signed-main-conjecture-unit-closure-2026-11-15,
at verification/bsd389_p599_independent_integral_390_moment_20261115.py.

**New execution in this conversation:** using a *fresh JavaScript continued-fraction evaluator*, not the older Python evaluator, the complete 390-digit integral Manin input was fetched from the user's GitHub and all 179101 representatives recomputed:
  {"input_length":390,"half_representatives":179101,"C0":0,"C1":0,"C2":543}.
This adds computational crosschecking of the genuine integer-Manin moment; it does **not** reproduce the user's eclib Manin vector.

A previously derived proposed Pollack/Castella source comparison on the other research branch is
\[
[T^2]L_{p}^{-}(T)\equiv-\tfrac{C_2}{2}\pmod p
\]
under the exact level-three approximation and logarithm-matrix conventions. If its normalization and error precision are independently authenticated in the same normalizations as BSTW Theorem 1.3, then at p599
\[
[T^2]L_{599}^{-}\equiv -543/2 \equiv 28\not\equiv0\pmod{599}.
\]
Then Proposition B **would prove** Sha[599∞]=0 without an independent full p599 Kurihara computation or an unproved rank-two p-adic BSD formula.

This last analytic-to-signed identification is **not established anew** by an integer Manin moment alone. The older branch labels the p599 conclusion REVIEW_REQUIRED; we keep the same boundary. The next proof obligation is a direct source-level demonstration of the signed coefficient and precision (or a short Sage Pollack signed series calculation identifying its source normalization). Do not promote "599 closed" before that specific gate.

## D. Global BSD boundary

Even if p599 were fully certified, this would eliminate only one of the finite-range exceptions. The infinite tail p>=48859 still requires an independent uniform Selmer/Kurihara argument or a genuine global integral annihilator; the complex rank-two leading coefficient identity remains a separate theorem to establish.

### Sources

- Stein–Wuthrich (2013), Theorem 12.3, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
- Burungale–Skinner–Tian–Wan (2024), Theorem 1.3, https://arxiv.org/pdf/2409.01350
- B. D. Kim (2013), Theorem 1.1, https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/plusminus-selmer-groups-for-supersingular-primes/7AD9B7AB53A73F23F8E78F78488FA75C
- p599 prior computational branch as documented in §C.
