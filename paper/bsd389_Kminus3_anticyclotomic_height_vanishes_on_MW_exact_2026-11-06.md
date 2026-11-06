# Anticyclotomic height zero on ALL rational rank-two MW classes: the exact reason a derived height is essential

Date 2026-11-06. A general, p-uniform \(\pm\)-eigenspace proof in the fixed quadratic field \(K=\mathbf Q(\sqrt{-3})\), not a numerical computation.

Let \(E/\mathbf Q=389a1\), with \(E(\mathbf Q)\simeq\mathbf Z^2\) and quadratic twist \(E^{-3}\) of Mordell–Weil rank 0. Hence \(E(K)\otimes\mathbf Q_p = E(K)^+\otimes\mathbf Q_p=E(\mathbf Q)\otimes\mathbf Q_p\) for every odd p (via standard quadratic restriction and corestriction).

For any p for which an equivariant anticyclotomic p-adic height pairing is defined, let
\[
h_p^{ac}:E(K)\otimes\mathbf Q_p\times E(K)\otimes\mathbf Q_p
\longrightarrow\Gamma^{ac}\otimes\mathbf Q_p\simeq\mathbf Q_p
\]
be the bilinear pairing associated to a p-adic class-field-theory character which is *odd* under complex conjugation \(c\), so
\[
\boxed{h_p^{ac}(cx,cy)=-h_p^{ac}(x,y).}
\]

**Theorem.** For every x,y in \(E(K)\otimes\mathbf Q_p\), \(h_p^{ac}(x,y)=0\).


**Applicability warning (crucial for 389a1):** The Agboola–Castella 2019 BDP theorem assumes the *Heegner hypothesis* (every prime dividing N splits in K). Here (389\equiv2\pmod3) is **inert** in (K=\mathbf Q(\sqrt{-3})), so that paper's BDP leading-term formulas **cannot be invoked for our chosen K**. We use only the general character-theoretic sign relation for an anticyclotomic-equivariant height; its conclusion is a formal sign argument independent of the Heegner setting. The Castella–Hsieh generalized Kato/definite-quaternionic theta framework is distinct and has precisely the odd inert (N^-=389) hypothesis relevant to E389a1. Their theta coefficient cannot be equated to the classical ordinary anticyclotomic MW height determinant.

**Proof.** Since the \((-)\)-eigenspace of \(E(K)\otimes Q_p\) is zero, \(cx=x\) and \(cy=y\). Galois equivariance gives
\(h_p^{ac}(x,y)=-h_p^{ac}(x,y)\), hence \(2h_p^{ac}(x,y)=0\). Because p is odd, the height vanishes. This is true for the complete rank-two MW space, not only for selected P,Q. QED.

Consequently the ordinary determinant of anticyclotomic p-adic heights on P,Q vanishes identically for *every p*. In particular, a nonzero order-two coefficient of an anticyclotomic theta/L-function cannot legitimately be identified with this ordinary 2×2 MW height determinant. The terms **derived heights**, Bockstein corrections, classes outside the MW subspace, or enhanced regulators are indispensable.

This does not contradict:
- nonzero **cyclotomic** p-adic regulator coefficients, which use the \(+1\) Galois direction and have been separately computed in the project for p=599 and p=16231;
- order-two anticyclotomic theta coefficients from the Gross/Brandt computations, whose cohomological interpretation involves derived-height formulas rather than the identically zero ordinary rank-two anticyclotomic MW determinant.

It also does not itself prove any Sha[p∞] finiteness, integrality bound, or BSD leading-term equality. The correct strict-Selmer quotient it would need to control is given by
\`paper/bsd389_Kminus3_exact_strict_Selmer_geometric_line_and_Sha_corank_2026-11-06.md\`.

Primary mathematical sources for the anticyclotomic equivariance identity:
- Darmon, *Elliptic curves and class field theory*, p-adic anticyclotomic height relation \(h(cx,cy)=-h(x,y)\): https://www.math.mcgill.ca/darmon/pub/Articles/Research/29.Millenium/millenium.pdf .
- Agboola et al., *On anticyclotomic variants of the p-adic Birch and Swinnerton-Dyer conjecture*, Remark 2.6, same Galois-equivariance and isotropic +/- eigenspaces: https://web.math.ucsb.edu/~agboola/papers/BSD-BDP-web.pdf .
- Castella–Hsieh (2022), derived anticyclotomic heights and generalized Kato classes, Theorems A/B and Theorem 5.3.
