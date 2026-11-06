# 389a1 global -3 twist: conditional all-prime Sha=0 from the October 2026 low-Selmer-corank BSD PREPRINT

Date 2026-11-06. **This is a conditional theorem-application note, not a new independent proof of the 2026 preprint.** Its assumptions and logical scope are explicit to avoid importing unreviewed mathematics as classical fact. It has no conclusion for rank-two Sha(E/Q) without a genuinely new theorem.

## Relevant new source, status

The October 7, 2026 OpenAI math release, *Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank*, Theorem 1.1 (preprint, no known independent specialist verification or Lean formalization identified), claims:

For ANY elliptic curve A/Q, if for SOME prime q the full q-power Selmer corank is 0 or 1, then the strong BSD leading term formula holds for A and its entire Sha is finite.

Source: https://github.com/openai/math/blob/main/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/01-introduction.tex . Independent catalogue expressly marks this release “To be verified”: https://open-math-atlas.com/famille/002-the-full-bsd-formula-from-low-selmer-corank . Therefore treat the theorem as a clear CONDITIONAL SOURCE INPUT unless and until independently reviewed or accepted; publishing the paper does not itself certify every proof step.

## Exact derivation for our twist (conditional only on validity of that preprint)

Let A=E^(-3): y²+y=x³−3x²−18x−7, conductor 3501.

Previously UNCONDITIONALLY established:
- L(A,1)>0 by a rigorous rational series enclosure, hence rank A(Q)=0 and Sha(A/Q) FINITE by Gross–Zagier–Kolyvagin.
- A(Q)_tors=0 by the full rational-point theorem E(Q(sqrt(-3)))=E(Q).
- Exact modular symbol / Gauss/Manin proof of L(A,1)/Omega_A=2.
- Exact local Tamagawa numbers c_3(A)=2, c_389(A)=1, all others 1.
- Therefore its entire known analytic BSD quotient L(A,1) / (Omega_A * product c_l(A)) is exactly 1.

Since rank A(Q)=0 and Sha(A/Q) is already known finite, for every prime q not dividing the finite integer #Sha(A/Q), the Kummer exact sequence implies
Sel_(q-infinity)(A/Q) = 0, so s_q(A)=0.
There EXISTS at least one such q because a nonzero integer has finitely many prime divisors. Thus the 2026 preprint's low-Selmer-corank hypothesis holds for A **without specifying a q or assuming that Sha(A) has order 1**.

If its Theorem 1.1 is valid, it therefore gives the exact strong BSD rank-zero identity for A:
L(A,1) = Omega_A * product_l c_l(A) * #Sha(A/Q) / (#A(Q)_tors)^2.
All factors but #Sha are exactly known, and their ratio is 1, hence
\[
\boxed{ \Sha(E^{(-3)}/Q)=0. }
\]

**The boxed statement is CONDITIONAL ON THE OCTOBER 2026 PREPRINT'S VALIDITY.** It is not proved just by the modular symbol value. It is not a consequence of earlier classical rank-zero Kolyvagin finiteness alone.

## Consequence for every odd prime p simultaneously (under the same conditional input)

The exact odd-primary quadratic restriction/corestriction theorem already proved in PR #12 gives, for all odd p without exceptions:
Sha(E/K)[p-infinity] ≅ Sha(E/Q)[p-infinity] ⊕ Sha(A/Q)[p-infinity].
Consequently, conditional on the above twist vanishing,
\[
\boxed{
\Sha(E/K)[p^\infty]\cong\Sha(E/Q)[p^\infty]
\quad\text{for EVERY odd }p,
}
\]
including p=3, p=389 and ordinary/supersingular p. Thus the formerly unknown finite exceptional support of the twist disappears from the global **odd-prime** comparison, but this is STILL only an equivalence between the same unknown rank-two arithmetic groups. It does not prove their finiteness or triviality.

At p=2, do NOT assert an integral splitting under the quadratic idempotents (1±tau)/2; a separate 2-descent/2-primary comparison is necessary.

## Why the same 2026 theorem CANNOT settle 389a1 directly

For original E=389a1 with rank E(Q)=2, the Kummer injection
(E(Q)⊗Q_q/Z_q) ≅ (Q_q/Z_q)^2 → Sel_(q-infinity)(E/Q)
gives s_q(E)>=2 for **EVERY** prime q, whether or not Sha(E)[q-infinity] vanishes. Therefore its s_q in {0,1} hypothesis is IMPOSSIBLE for our rank-two curve, not merely unverified. Nor can quadratic base change or an isogeny turn the two rational MW directions into a rank-one situation: rank E(K)=2 and rank Res_(K/Q)E_K=2.

This is the exact scope boundary: any rank-two global Sha/complex-BSD conclusion still needs a genuinely new rank-two theorem, with a simultaneous uniform all-prime integral Selmer bound and an exact archimedean regulator comparison.

No historical p-primary computation was rerun, and no full rank-two BSD proof is claimed.
