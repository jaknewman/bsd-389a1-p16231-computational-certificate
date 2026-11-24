# 389a1 — Uniform full Kummer-image and two-prime Mordell–Weil localization basis at arbitrary depth

**24 November 2026. Mathematical status:** unconditional *theorem for all sufficiently large p* based on the known saturated MW basis, Serre open image, central-Sah vanishing and elementary Kummer theory plus Chebotarev. This proves **local** arithmetic availability at depth p^k; it does **NOT** imply any Kurihara two-factor coefficient is a p-unit, nor prove Sha finiteness or strong BSD. No computations are needed.

## Theorem

Let E/Q be 389a1 with E(Q)=Z P⊕Z Q and no torsion, P=(-1,1), Q=(0,-1). Then there is a (not necessarily explicit) bound B such that for every prime p>B and every integer k≥1, there exist infinitely many ordered pairs of distinct good primes (q1,q2) with
\[
q_i\equiv1\pmod{p^k},\qquad a_{q_i}(E)\equiv2\pmod{p^k},
\qquad
E(\mathbf F_{q_i})/p^k E(\mathbf F_{q_i})\simeq\mathbf Z/p^k.
\]
Upon choosing generators of the two cyclic groups, the simultaneous reduction map
\[
E(\mathbf Q)/p^k \longrightarrow
E(\mathbf F_{q_1})/p^k\oplus E(\mathbf F_{q_2})/p^k
\]
is an **isomorphism**. Indeed one can prescribe its matrix to be the identity modulo p^k, after suitable local identifications.

This is a uniform assertion about the MW points at **two** deeply Kurihara-admissible primes, not about a Kato/Euler-system coefficient.

## Proof 1 — exact Galois image over the division field

For p sufficiently large, by non-CM and Serre's open image theorem,
\[
\mathrm{Gal}(F_k/\mathbf Q)=\mathrm{GL}_2(\mathbf Z/p^k),\qquad
F_k=\mathbf Q(E[p^k]).
\]
Write \(V_k=E[p^k]\) and let \(M_k=F_k(p^{-k}P,p^{-k}Q)\) be the field obtained by adjoining the coordinates of chosen points \(R_P,R_Q\) with \([p^k]R_P=P\), \([p^k]R_Q=Q\). Because all p^k-torsion is rational over F_k,
\[
W_k:=\mathrm{Gal}(M_k/F_k)\hookrightarrow V_k^2
\]
by its two translation cocycles. This is a module stable under conjugation by \(\mathrm{GL}_2(\mathbf Z/p^k)\).

**Claim:** \(W_k=V_k^2\).

First use the central element \(-I\) in \(\mathrm{GL}_2(\mathbf Z/p^k)\). Its conjugation action on that group is trivial, while it acts on \(V_1=E[p]\) as \(-1\). Sah's lemma, since p is odd, gives
\[
H^1(\mathrm{GL}_2(\mathbf Z/p^k),V_1)=0.
\]
The inflation–restriction map
\[
H^1(\mathbf Q,V_1)\to H^1(F_k,V_1)
\]
is therefore injective. Since P,Q form a basis of the saturated group E(Q), their two Kummer classes \(\kappa_1(P),\kappa_1(Q)\in H^1(\mathbf Q,V_1)\) are linearly independent over Fp. Their restrictions to F_k remain independent.

The mod-p reduction \(\overline W_k\subseteq V_1^2\) is the image of \(W_k\) by multiplication by \(p^{k-1}\) on V_k (the same as reduction of its two translation coordinates under a chosen Z/p^k-basis). This is the joint Kummer Galois image for P,Q modulo p over F_k. It is GL₂(Fp)-stable. The natural module V_1 is absolutely irreducible with End_{GL₂(Fp)}(V_1)=Fp. Hence every submodule of \(V_1\oplus V_1\) is of the form \(V_1\otimes U\) for some Fp-subspace U⊂Fp². Were \(\overline W_k\) proper, some nontrivial linear combination of the two coordinate projections would vanish on \(\overline W_k\). The corresponding nonzero linear combination of \(\kappa_1(P),\kappa_1(Q)\) would then restrict to zero over F_k, contradicting the injectivity just proved.

Thus \(\overline W_k=V_1^2\). By Nakayama over the local ring \(\mathbf Z/p^k\), any submodule \(W_k\subseteq V_k^2\) surjecting modulo p is the whole module. This proves
\[
\boxed{\mathrm{Gal}(M_k/F_k)=E[p^k]^2.}
\]
No assumption on Sha is needed.

## Proof 2 — prescribing exact local MW coordinates by Chebotarev

Choose the nonidentity unipotent matrix
\[
U_k=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\in\mathrm{GL}_2(\mathbf Z/p^k).
\]
Its determinant is 1, trace is 2, and
\[
V_k/(U_k-1)V_k\simeq\mathbf Z/p^k
\]
canonically up to a unit after choosing the matrix's coordinate basis.

The projection \(\mathrm{Gal}(M_k/\mathbf Q)\twoheadrightarrow\mathrm{GL}_2(\mathbf Z/p^k)\) is surjective and its kernel is \(V_k^2\). Therefore a lift of \(U_k\) can be multiplied by arbitrary translation pairs from \(V_k^2\). Select one lift g_1 whose translation Kummer coordinates projected to \(V_k/(U_k-1)V_k\) are \((1,0)\), and another g_2 with projections \((0,1)\). The group extension need not split: the translations form the kernel and suffice to prescribe these fibers.

Chebotarev applied to the two nonempty conjugacy classes of g_1,g_2 gives infinitely many distinct primes q1,q2 outside the ramified set with the desired Frobenius elements. Their determinants/traces yield
\[
q_i\equiv1\pmod{p^k},\qquad a_{q_i}(E)\equiv2\pmod{p^k}.
\]
Moreover the unramified finite-field Kummer isomorphism is
\[
E(\mathbf F_q)/p^k
\simeq H^1(\mathbf F_q,E[p^k])
\simeq V_k/(\mathrm{Frob}_q-1)V_k,
\]
where the middle identification uses Lang's theorem for E/Fq. Hence both local mod-p^k groups are cyclic, and their reductions of P and Q are precisely the prescribed coordinates. The resulting 2×2 localization matrix is the identity, giving the claimed isomorphism.

This proves the uniform deep local-basis theorem.

## How it relates to the actual BSD obstruction

- This upgrades the already archived "deep auxiliary Frobenius U exists" result to **full two-generator MW localization control at every depth p^k**. It removes local linear dependence of P,Q as a possible explanation for failure of **finding good two-prime auxiliary choices** in the large-p tail.
- But Kurihara's \(\widetilde\delta_{q_1q_2}\) is a global modular-symbol/Kato cohomological derivative and is **not determined** by the two MW localization coordinates. An invertible MW local matrix **does not imply** \(\widetilde\delta_{q_1q_2}\not\equiv0\bmod p\). No reverse reciprocity is proved here.
- Kim's structural theorem + Castella–Sano 2026 already imply the sharp iff at large p:
\[
\Sha(E/\mathbf Q)[p^\infty]=0
\iff\exists q_1q_2:\widetilde\delta_{q_1q_2}\not\equiv0\bmod p.
\]
The present theorem guarantees plentiful **eligible MW-independent pairs** but NOT the nonvanishing of this global scalar at any of them. It therefore does not yet establish the right-hand side, all-p Sha finiteness, or exact complex BSD.
- This identifies a sharply isolated missing kind of theorem: a genuinely arithmetic *rank-two detection* principle comparing the full Kato class with the saturated MW localization determinant, in a way that bounds the two-prime derivative independently of the unknown Sha. This is much stronger than the local Chebotarev statement and is currently unproved.

**References:** Serre's open image theorem; Sah's lemma for central -I in H¹; Kummer theory; Chebotarev; Lang's theorem; Chan-Ho Kim, Theorem 1.8, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf ; Castella–Sano, Theorem B, https://web.math.ucsb.edu/~castella/Kurihara.pdf .
