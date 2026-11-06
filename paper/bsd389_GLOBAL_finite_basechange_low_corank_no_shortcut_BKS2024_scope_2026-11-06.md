# GLOBAL BSD 389a1 — Finite base-change cannot reduce Selmer rank or hide the Sha-finiteness gap; BKS 2024 hypotheses audited

Date 2026-11-06. **A new all-number-fields proof and primary-source scope audit** for the direct global rank-two programme in PR #12. No previous p-local certificate is rerun, no analytic or BSD equality is assumed or claimed. The main result is a precise *no-shortcut theorem* governing every finite auxiliary field, rather than another local numerical experiment.

## Theorem A — any finite extension of Q retains rank at least two and Selmer corank at least two

Let E/Q be 389a1 with proved free Mordell–Weil basis P=(-1,1), Q=(0,-1). For ANY finite number field F/Q, the natural map E(Q)→E(F) is injective. Thus the two points P,Q remain linearly independent:
\[
\boxed{\mathrm{rank}\,E(F)\ge2.}
\]
For every rational prime p, the global Kummer injection over F yields
\[
(E(F)\otimes Q_p/Z_p)\hookrightarrow\mathrm{Sel}_{p^\infty}(E/F).
\]
Consequently
\[
\boxed{\mathrm{corank}_{Z_p}\mathrm{Sel}_{p^\infty}(E/F)\ge2}
\quad\text{for EVERY F and p.}
\]

This excludes the rank-zero/one / low-(0,1)-Selmer-corank BSD theorems in every finite base extension, not merely in the previously considered K=Q(sqrt(-3)). A change of field CANNOT lower the two rational MW directions.

## Theorem B — Sha finiteness over F is AT LEAST as strong as Sha finiteness over Q

Fix ANY finite F/Q, and put d=[F:Q]. Restriction and corestriction on Galois H1, and on locally trivial classes, satisfy
\[
\mathrm{cor}_{F/Q}\,\mathrm{res}_{F/Q}=[d].
\]
For a rational prime p write d=p^a m with (m,p)=1. If xi lies in
\(\ker(\Sha(E/Q)[p^\infty]\to\Sha(E/F)[p^\infty])\),
then d xi=0, whence \(p^a xi=0\) because multiplication by m is an automorphism on p-primary torsion. Hence
\[
\boxed{\ker(\mathrm{res}|_{\Sha[p^\infty]})
\subseteq\Sha(E/Q)[p^a].}\tag{1}
\]
The group on the right is FINITE for each finite a: it is a quotient of the finite p^a-Selmer group by the finite quotient E(Q)/p^a E(Q) (Kummer exact sequence). In particular when p∤d, the map is injective.

Thus **for EVERY finite F and EVERY p**
\[
\boxed{\Sha(E/F)[p^\infty]\text{ finite}
\ \Longrightarrow\ \Sha(E/Q)[p^\infty]\text{ finite}.}\tag{2}
\]
Indeed image of restriction is a subgroup of a finite group, and kernel (1) is finite.

Moreover, as d-torsion Sha(E/Q)[d] is finite by finite descent,
\[
\boxed{\Sha(E/F)\text{ finite}
\ \Longrightarrow\ \Sha(E/Q)\text{ finite}.}\tag{3}
\]
No conjectural global finiteness is used in any of these implications.

**Important direction:** A proof of finiteness upstairs is a VALID route to proving it downstairs, but is never an “easier rank-zero/one problem” for E=389a1: Theorem A forces rank at least two upstairs. The implication in (2) means that importing a theorem ASSUMING Sha(E/F)[p∞] finite does not discharge the sought Sha(E/Q)[p∞] finiteness; the source theorem assumes a condition strong enough to already contain the conclusion.

## Theorem C — exact 2024 Burns–Kurihara–Sano scope for analytic rank two

The peer-reviewed article David Burns, Masato Kurihara, Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), pp.855–919, is mathematically rigorous but often its subtitle “arbitrary rank” is read too strongly. Its actual statements specify:

- At the **START of Introduction §1.2.1** (printed p.856), the setup assumes r>0, E(Q)[p]=0 **AND Sha(E/Q)[p∞] FINITE**, before defining the canonical \(\eta^{BSD}\) object.
- **Hypothesis 2.2(iii), printed p.866**, explicitly assumes \(\Sha(E/Q)[p^\infty]\) is finite.
- **Theorem 1.3(b), printed p.857**, proves order-of-vanishing under the assumption that **\(\Sha(E/F)[p^\infty]\) is finite**. By Theorem B above, this assumption is already at least as strong as the finiteness sought over Q.
- **Corollary 1.12 (Corollary 7.4), printed p.861**, proves a p-adic BSD formula up to a p-unit from Iwasawa main conjecture, again only if \(\Sha(E/Q)[p^\infty]\) is FINITE.
- **Theorem 1.14 (Theorem 7.6), printed p.861**, assumes **the full \(\Sha(E/Q)\) is finite**, equality of analytic and algebraic ranks, the main conjecture and Generalised Perrin-Riou conjecture, plus Bockstein regulator nonvanishing, before concluding the p-part of BSD.

These are genuine higher-rank results, but **none proves for rank-two 389a1 the still missing all-p finiteness from the data already certified**. In particular:
\[
\boxed{\text{BKS 2024 + already known } \mathrm{rank}=2 \not\Longrightarrow
\Sha(389a1)\text{ finite}.}
\]

This is NOT a criticism of the paper: it states its hypotheses accurately; the paper does not claim unconditional rank-two Sha finiteness.

Primary source, publisher PDF (also fully text-verified, with page-857 screenshot): https://kurihara.math.keio.ac.jp/bks4.pdf ; https://doi.org/10.2969/jmsj/90699069 .

## Positive conclusion and next proof gate (not just a verbal restatement)

The previous PR #12 global projectors and height identities remain correct **in their stated scope**. Theorems A–C now establish a **single global screening test** for a candidate route:

1. **If its hypothesis** asserts finite p-primary Sha over Q or over ANY finite extension F, it cannot serve as a noncircular proof of the missing finiteness. Prove that hypothesis from independent input first.
2. **If its proof applies only when Selmer corank ≤1**, it cannot apply to the original E=389a1 over ANY finite F by Theorem A.
3. **If it identifies a determinant only over Qp or up to p-units**, it cannot prove the exact complex rank-two identity nor bound the p-support of finite Sha groups, without a specified GLOBAL integral comparison.

A genuinely new proof needs an Euler/Kolyvagin/Selmer result whose hypotheses do NOT imply finite Sha, which **produces** (rather than assumes) a uniform integral Selmer bound, or an independent second-complex-derivative arithmetic-height theorem. Such a result is still missing. We should not disguise another equivalence or rephrased goal as an advance on the missing theorem.

No old p-primary re-run or proof of full BSD is claimed.
