# p=107 — Kurihara two-prime witness and Kim's exact Selmer structure theorem

**Date:** 2026-10-30. **Status:** mathematical implication **proved conditional on the frozen full-data certificate** (710 completed production blocks, and matching p-integral normalized modular symbols); the archived computation's user-reported PASS is historical, and a fresh archive-SHA + arithmetic-gates replay is requested. This is not a proof of complete BSD or of Sha vanishing at all primes.

## 1. Exact arithmetic input

For E: y²+y=x³+x²−2x, N=389, Δ_min=+389, rank E(Q)=2, torsion=0, Tamagawa product=1, let
\`\`\`text
p = 107, q1 = 369793, q2 = 383917
n = 141969819181
a_q1 = 2, a_q2 = -854
q1-1 = 107 * 3456, #E(F_q1) = 107 * 3456
q2-1 = 107 * 3588, #E(F_q2) = 107 * 3596
\`\`\`
Both q are prime and meet q ≡ 1 (mod p), a_q ≡ q+1 (mod p). Their Kurihara residue ideals are I_q1=I_q2=(107) in Z_107. The reduced 107-torsion E(F_107)[107] vanishes since #E(F_107)=108 (this check is supplementary, not an extra condition of Theorem 1.8).

The curve is the optimal model 389a1 for conductor 389, so the optimal Manin constant is prime to 107 by Mazur's theorem (p² does not divide N); residual representation at 107 is surjective (Sage-certified).

## 2. Genuine full Kurihara data and source/audit boundary

For the two chosen primitive roots g1=g2=5, define
\[
\widetilde\delta_n =
\sum_{a\in(\mathbf{Z}/n)^\times}
  [a/n]^+ \log_{g_1}(a)\log_{g_2}(a)
  \pmod{107}.
\]
The historical native and independently audited Manin source used 390 eclib-normalized classes. The complete numerical result from **710 disjoint half-range blocks** is
\[
 \frac12 \widetilde\delta_n\equiv17\pmod{107},
 \qquad
 \boxed{\widetilde\delta_n\equiv34\ne0\pmod{107}.}
\]
This is the exact **auxiliary-conductor Kurihara delta**, not the cyclotomic p² moment studied at p599.

Frozen checksums and source assertions:
\`\`\`text
Manin M390 SHA256 00cdb5cd7ad9c7093877836412a77fe3f67985aa2e1878ddd03b8092ab90ee2f
W390 SHA256 ee3fa1f5fca6de2b04300cbcc042e00e1a19a0e060adb24d2f3b90afabc0f8d0
native executable SHA256 dfe879e69947b51b9762f6c72772ea80c56a8c7dfb8efe3a4823414cfa7e16b4
complete archive SHA256 b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754
archive pathname ~/bsd389_k107_certificate_COMPLETE_20261028.tar.gz
\`\`\`
Archival reports: [mathematical certificate](K107_certificat_mathematique_2026-10-28.md), [native integer/CF loop correctness](K107_preuve_correction_noyau_20261028.md), [finite group ring bridge](K107_Dplus_pont_des_deux_moteurs.md). A SHA match authenticates **the archived bytes** but is not a second traversal of all 70,984,909,590 half-range numerators. Independence comes from the audited 390 Manin entries, differential controls, checkpoint coverage and the source invariant, which need to remain in the reproducibility manifest.

## 3. Theorem applied: Chan-Ho Kim, Theorem 1.8 (2025 preprint, 2026 AJM publication)

**Reference:** C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8 (1), (3). [Preprint PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf), page 7. See also Castella–Sano, [*On refined nonvanishing conjectures by Kurihara and Kolyvagin*](https://web.math.ucsb.edu/~castella/Kurihara.pdf), page 3.

For p ≥ 5, surjective residual representation, Manin constant prime to p and some nonzero Kurihara number, Kim proves, *without a prior finiteness assumption for Sha*:

1. The Z_p-corank of Sel_{p∞}(E/Q) equals
   \(\rho=\min\{\nu(m): \widetilde\delta_m\ne0\}\).
2. Writing \(M_i=\partial^{(i)}(\widetilde\delta)\) for the minimum valuation of the complete collection with i auxiliary primes and \(M_\infty=\partial^{(\infty)}\), the finite-length quotient Sel_{p∞}/(maximal divisible subgroup) has length \(M_\rho-M_\infty\).

Because our two-prime witness is nonzero, \(\rho\le2\). By the Kummer injection
\(E(Q)\otimes(Q_p/Z_p)\hookrightarrow Sel_{p∞}\), the proven rank 2 gives \(\rho\ge2\); therefore \(\rho=2\).

The **mod-p unit** witness makes \(M_2=0\); by definition \(0\le M_\infty\le M_2\), so \(M_\infty=0\). Kim's Theorem 1.8(3) now yields
\[
\operatorname{length}_{Z_{107}}(Sel_{107^\infty}/Sel_{\mathrm{div}})=0.
\]
Thus \(Sel_{107^\infty}\cong(Q_{107}/Z_{107})^{\oplus2}\) as a divisible p-primary group.

The Kummer exact sequence
\[
0\longrightarrow E(Q)\otimes(Q_{107}/Z_{107})
\longrightarrow Sel_{107^\infty}
\longrightarrow\Sha(E/Q)[107^\infty]\longrightarrow0
\]
injects a divisible group \((Q_{107}/Z_{107})^2\) into a divisible group of the same corank. Any **injective endomorphism** of \((Q_p/Z_p)^2\) is an automorphism (dually it is a surjective endomorphism of the finite free \(Z_p^2\) module), so this injection is surjective. Therefore
\[
\boxed{\Sha(389a1/Q)[107^\infty]=0}
\]
**conditional only on authenticating and accepting the archived full Kurihara calculation and normalization along with the reported arithmetic gates**. No conjectural BSD equality and no independent Sha finiteness assumption are used.

## 4. Cheap independent second route

A new independent script, [\`verification/bsd389_p107_supersingular_p2_shortcut.py\`](../verification/bsd389_p107_supersingular_p2_shortcut.py), computes the tame-trivial cyclotomic conductor-107² quadratic moment from **5,671 plus-pairs**, checks all Hecke p²→p fibres and the normalized supersingular regulator. The exact p599 Hecke/Frobenius lemma applies to p107 because a_107=0 and the curve has 2 real components. This second route may or may not certify a unit ratio at p107; **its numerical output is currently pending**. If its first moment or normalized regulator is not a unit, it is inconclusive and the archived K107/Kim route remains the primary certificate.

## 5. Minimal replay without 71-billion-term recomputation

\`\`\`bash
python -u verification/bsd389_kim_kurihara_sha107_bridge.py \
  --archive ~/bsd389_k107_certificate_COMPLETE_20261028.tar.gz

python -u verification/bsd389_p107_supersingular_p2_shortcut.py
\`\`\`
The first hashes the **actual full archive** and independently recomputes local prime point counts; it does not itself re-audit each block. The second independently tests the small analytic route with Sage. Save outputs and update the status ledger **only after genuine successful user execution**.

**Scope:** This certificate at p107, even together with the p599 certificate, does not prove Sha finite/trivial for all p or the full BSD formula. The uniform-support D+ problem remains distinct.
