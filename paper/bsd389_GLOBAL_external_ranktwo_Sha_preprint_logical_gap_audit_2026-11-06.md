# Why a March-2026 public claim of rank-two Sha finiteness cannot yet close our GLOBAL proof

Date: 2026-11-06. This is a narrowly targeted mathematical inference audit of a third-party *unreviewed preprint claim*. We do NOT claim to have reviewed every line of the manuscript or to have refuted a theorem in general; we identify two concrete logical gaps in the conclusion AS WRITTEN. This prevents ungrounded import of a supposed all-prime Sha theorem into the 389a1 project.

Source: Xiong Wang, *The Birch and Swinnerton-Dyer Conjecture for Analytic Rank Two: A Complete Proof via Definite Anticyclotomic Iwasawa Theory*, ResearchGate March 2026, https://www.researchgate.net/publication/401385931_The_Birch_and_Swinnerton-Dyer_Conjecture_for_Analytic_Rank_Two_A_Complete_Proof_via_Definite_Anticyclotomic_Iwasawa_Theory. The audit concerns its §17.5 (printed page 70–71), particularly "Case 5: ell | N" and the concluding paragraph. No appeal to peer review alone replaces the mathematical audit.

## Gap 1 — an injection of rank two does NOT upper-bound Selmer corank by two

The manuscript states that MW rank two, the cofinite-generation of the p-infinity Selmer and its Kummer exact sequence entail
\(\operatorname{corank}_{Z_p} \mathrm{Sel}_{p^\infty}\le2\)
at bad reduction primes. This does not follow. The exact Kummer sequence is
\[
0\to E(Q)\otimes Q_p/Z_p
\to \mathrm{Sel}_{p^\infty}(E/Q)
\to\Sha(E/Q)[p^\infty]\to0,
\]
so, since rankMW=2,
\[
\boxed{
\operatorname{corank}_{Z_p} \mathrm{Sel}_{p^\infty}
=2+\operatorname{corank}_{Z_p}\Sha[p^\infty]
\ge2.
}
\]
Cofinite generation guarantees that this dimension is FINITE, not that it equals two. A perfectly valid abstract p-primary Kummer-type exact sequence with MW term (Qp/Zp)^2 and Sha quotient (Qp/Zp)^2 yields a cofinitely generated Selmer of corank **four**. No alternating Cassels–Tate pairing on the finite quotient of Sha rules out its divisible part: a Cassels–Tate pairing has the maximal divisible subgroup in its radical. Therefore the inference \(\le2\) is exactly the desired Sha finiteness assertion, not a consequence of Mordell–Weil rank.

## Gap 2 — finite p-primary components at EVERY p do NOT imply global Sha is finite

Even if one proved \(\Sha[p^\infty]\) is finite for every prime p, one would not have proved the direct sum over all primes is finite. Elementary counterexample:
\[
A=\bigoplus_{p\ {\rm prime}}(\mathbf Z/p\mathbf Z)^2.
\]
Every A[p∞] is finite and even has square order and a perfect alternating pairing, but A itself is infinite. A **single fixed integer** controlling p-support, a uniform Kolyvagin bound, or an equivalent all-but-finitely-many p-triviality theorem must additionally be proved. The paper's conclusion "each p-primary group finite, hence Sha finite" omits this support step.

These are counterexamples to *the stated logical implications*, not actual Tate–Shafarevich groups of elliptic curves. A separate argument might repair the manuscript, but until it is identified and source-reviewed, its global theorem cannot be treated as verified.

## Appropriate boundary for E389a1

The accepted exact analytic rank two and algebraic rank two for E389a1 do NOT close either logical gap. Existing verified p-primary certificates are meaningful but finite in number; they do not constitute uniform p-support.

The new exact global rank-zero twist identity in this PR proves
\[
L(E^{-3},1)/(\Omega_{E^{-3}}\prod c_\ell)=1
\]
without assuming the order of Sha of the twist. It is a separate, verified accomplishment and does not borrow the March-2026 claim.

The GLOBAL two obligations for E remain non-circular all-prime Sha finiteness/order control and the exact complex rank-two leading-coefficient/regulator identity.
