# 389a1 — a genuine rank-two generalized Kato detection criterion for p-primary Sha FINITENESS, and the remaining mod-p strict-Selmer gap

**24 November 2026. Mathematical status:** Exact arithmetic specialization of the 2024 Castella–Hsieh theorem and Castella's Theorem 5.2.3 (arXiv:2312.01481). Proves the explicit rank-two Mordell–Weil strict class is nonzero without BSD; gives an if-and-only-if criterion for **p-primary Sha FINITENESS** under the auxiliary/ordinary hypotheses. Does NOT prove the generalized Kato class is nonzero, Sha[p]=0, all-prime finiteness, or complex strong BSD. No new finite computation is needed.

## 1. A strict Selmer class that is definitely NONZERO for 389a1

Let E/Q be 389a1, with saturated torsion-free MW basis P=(-1,1), Q=(0,-1). Let p>=5 be a prime of good ordinary reduction and V=V_pE, and write
\[
S_V=\operatorname{Sel}(\mathbf Q,V),\quad S_V^{(0)}=\ker\left(S_V\xrightarrow{\operatorname{loc}_p}H_f^1(\mathbf Q_p,V)\right).
\]

Because E(Q_p) is a one-dimensional p-adic Lie group, its Bloch–Kato finite local cohomology \(H_f^1(\mathbf Q_p,V)\simeq E(\mathbf Q_p)\otimes\mathbf Q_p\) is one-dimensional. Its formal logarithm \(\log_p\) is an isomorphism onto \(\mathbf Q_p\) after rationalization. The kernel of the elliptic formal logarithm on E(Q_p) consists of torsion points, so a global non-torsion P satisfies \(\log_p(P)\neq0\). (The same is true for Q.)

Let \(\kappa(P),\kappa(Q)\in S_V\) denote their global rational p-adic Kummer classes. Define the exact arithmetic class
\[
\boxed{w_p:=\log_p(Q)\,\kappa(P)-\log_p(P)\,\kappa(Q).}
\]
Its local logarithm equals zero, hence \(w_p\in S_V^{(0)}\). Because P and Q are linearly independent in E(Q)⊗Q_p (and global Kummer is injective), and the coefficients are not both zero, **\(w_p\neq0\)** unconditionally. This genuine known nonzero strict class does NOT force Sha[p] to vanish; it only accounts for the unavoidable one strict dimension arising from rank2 MW and local rank1.

## 2. Exact strict dimension and finite Sha distinction

Write \(c_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]\), which is well-defined because p-power Selmer is cofinitely generated. The p-adic rationalization of Kummer provides
\[
\dim_{\mathbf Q_p}S_V=2+c_p.
\]
The P-class has nonzero localization, so \(\operatorname{loc}_p:S_V\to H_f^1(\mathbf Q_p,V)\) is surjective. Therefore
\[
\boxed{\dim_{\mathbf Q_p}S_V^{(0)}=1+c_p.}
\]
For the large good-p tail, p-parity says \(c_p\) is even. The strict dimensions may be 1,3,5,... . In particular:
\[
\Sha(E/\mathbf Q)[p^\infty]\text{ finite}
\iff c_p=0
\iff \dim_{\mathbf Q_p}S_V^{(0)}=1.
\]
This is **not** equivalent to Sha[p^\infty]=0. The latter additionally requires that the finite p-torsion be trivial.

## 3. EXISTING rank-two generalized Kato theorem gives a noncircular iff

In *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2* (Forum of Mathematics, Sigma 2022), Castella–Hsieh construct generalized diagonal-cycle Kato classes. Castella, *Nonvanishing of generalised Kato classes and Iwasawa main conjectures* (arXiv:2312.01481, March 2026 version), **Theorem 5.2.3**, treats a choice (K,chi) of CM auxiliary data satisfying its **Choice 5.2.1**: 389 inert in K, p splits in K (and p ordinary), auxiliary auxiliary prime ell split in K, nonzero L(E^K,1) and L(E/K,chi,1), and chi nontrivial at a chosen p-adic place. The paper cites independent existence/nonvanishing results for the required auxiliary data.

Under its Galois hypotheses, for E389a1 of positive even analytic rank, the theorem establishes
\[
\boxed{\kappa_p^{\rm gen}(E;K,\chi)\neq0\Longrightarrow \dim_{\mathbf Q_p}S_V=2.}
\]
It also proves the **converse** provided \(\operatorname{loc}_p:S_V\to E(\mathbf Q_p)\otimes\mathbf Q_p\) is nonzero. For our curve that proviso is ALREADY SATISFIED by the non-torsion rational point P. Consequently for every p and auxiliary choice to which the theorem applies,
\[
\boxed{
\kappa_p^{\rm gen}(E;K,\chi)\neq0
\iff \dim_{\mathbf Q_p}S_V=2
\iff \Sha(E/\mathbf Q)[p^\infty]\text{ is FINITE}.
}
\]
This **iff is a published theorem specialized to our rank-two curve**, not an original claim about unconditional generalized-Kato nonvanishing.

Furthermore whenever these conditions hold, the theorem says \(\kappa_p^{\rm gen}\) spans the strict rational Selmer, hence for a UNIQUE \(\lambda_p\in\mathbf Q_p^\times\)
\[
\boxed{\kappa_p^{\rm gen}=\lambda_p w_p.}
\]
The existence/nonzero value of lambda is a consequence after finiteness/nonzero κ; it **cannot** be inferred from w_p≠0 alone. Without p-primary finiteness, w_p remains nonzero but the generalized Kato class vanishes under the source hypotheses. This is the central noncircularity gate.

## 4. Why this is NOT yet the requested uniform mod-p bound

Our previously proved exact two-Chebotarev-prime finite-level identity says
\[
S_{p}^{00}(q_1,q_2)\simeq\Sha(E/\mathbf Q)[p]
\]
when the two localizations of P,Q are independent. The target \(\dim_{\mathbf F_p}S_p^{00}\le1\), together with parity, gives **Sha[p]=0** (and then p-primary Sha=0).

The generalized Kato theorem above controls \(\dim_{\mathbf Q_p}S_V\), hence only the **divisible p-corank** of Sha. It does NOT exclude finite nonzero Sha[p]. Algebraic example:
\[
S_V\simeq\mathbf Q_p^2,\quad \Sha[p^\infty]\simeq(\mathbf Z/p)^2,\quad
S_V^{(0)}\simeq\mathbf Q_p\, w_p.
\]
This is compatible with the generalized Kato rational criterion \(\kappa_p^{\rm gen}\neq0\), but \(S_p^{00}\simeq(\mathbf F_p)^2\neq0\). Even an integral primitive generator of the *free* strict summand cannot by itself eliminate this finite torsion.

Thus the two mathematically distinct required assertions for genuine p-primary triviality are:
1. rational **nonzero** \(\kappa_p^{\rm gen}\) (to rule out infinite-corank Sha);
2. an **integral Fitting/Kurihara two-factor unit** (to rule out finite p-torsion).

Kim Theorem 1.8 + Castella–Sano Theorem B already combine both into the sharper single equivalence
\[
\Sha(E/\mathbf Q)[p^\infty]=0
\iff \exists q_1q_2:\widetilde\delta_{q_1q_2}\neq0\pmod p.
\]
The generalized Kato route is genuinely different and useful for proving **FINITENESS at a fixed p**, but its nonvanishing is itself unknown uniformly, and it does not currently shortcut the two-factor criterion.

## 5. What constitutes acceptable NEW evidence; no wasted computations

A genuine cohomological certificate of \(\kappa_p^{\rm gen}\neq0\) for a particular ordinary p, *not* merely the nonvanishing of auxiliary twisted complex L-values or of the known vector w_p, would prove Sha[p^\infty] finite at that p. The usual dual-exponential reciprocity evaluation at the central L-value is **zero** when analytic rank is 2, so the first nonvanishing of a **derived** Abel–Jacobi/p-adic L-value would need to be certified with its precise integral normalization and a proven nonzero-class implication.

To establish global Sha0, such primewise nonvanishing would still need a **uniform p-tail assertion** and a finite-torsion order bound; the known rank2 generalized Kato theorem does not assert either. Therefore NO new brute-force Kurihara sums, Smith matrices, auxiliary field classes, or more MW-independent prime choices are justified by this note.

References:
- F. Castella, *Nonvanishing of generalised Kato classes and Iwasawa main conjectures*, arXiv:2312.01481, Theorem 5.2.3, Choice 5.2.1, Remark 5.2.5: https://arxiv.org/abs/2312.01481 .
- F. Castella, M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics Sigma, 2022: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864 .
- C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.8: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf .
- F. Castella, T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, 2026 Theorem B: https://arxiv.org/abs/2601.14504 .
