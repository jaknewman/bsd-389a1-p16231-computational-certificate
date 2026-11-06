# Global BSD 389a1 — squarefree Fitting bound, precise rank-two Euler-system bottleneck

Date 2026-11-06. **No local certificate was rerun.** The analytic rank-two proof and the p-local Sha certificates are retained exactly as previously archived. This document proves an exact *conditional reduction* and isolates two source-verified hypotheses that must NOT be smuggled into a claimed global proof.

## A. Proven squarefree Fitting criterion

Let \(E/\mathbf Q=389a1\), with \(E(\mathbf Q)\cong\mathbf Z^2\) and trivial torsion. For a rational prime \(p\), put
\[
X_p:=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee,\qquad
I_p:=\operatorname{Fitt}_{2,\mathbf Z_p}(X_p).
\]
The already certified Kummer/Fitting isomorphism gives
\[
X_p\cong\mathbf Z_p^2\oplus\Sha(E/\mathbf Q)[p^\infty]^\vee,\quad
I_p=\operatorname{Fitt}_{0,\mathbf Z_p}
 (\Sha[p^\infty]^\vee).
\]

**Theorem A.** Suppose there is an independently defined nonzero *squarefree* integer \(C\), and a theorem proving
\[
C\mathbf Z_p\subseteq I_p\quad\text{for every odd prime }p.
\]
Then \(\Sha(E/\mathbf Q)[p^\infty]=0\) for every odd prime \(p\). If the archived exact two-primary Sha=0 certificate is accepted, then \(\Sha(E/\mathbf Q)=0\).

**Proof.** The inclusion forces \(I_p\ne(0)\), hence \(A_p:=\Sha[p^\infty]\) is finite. Writing \(I_p=p^{e_p}\mathbf Z_p\), the inclusion gives \(e_p\le v_p(C)\le1\). But the nondegenerate alternating Cassels–Tate pairing on the finite \(A_p\) makes \(\#A_p=p^{e_p}\) a perfect square; thus \(e_p\) is even and can only be zero. Therefore \(A_p=0\). This holds for every odd \(p\). The already certified 2-part handles \(p=2\). QED.

**This is not a proof that such a comparison exists.** Its mere existence with some squarefree C is, given Cassels–Tate and 2-Sha zero, equivalent to the sought Sha=0; a non-circular method must construct the specific C and prove its arithmetic comparison independently.

## B. A tempting concrete C=2, and the exact missing map

The already executed Smith certificate gives the determinant divisor of the stacked integral modular-symbol Hecke operators \(D(T_2,T_3)=2\), on its specified rank-33 lattice.

If one could prove **for the actual Selmer modules** that
\[
\boxed{2\mathbf Z_p\subseteq I_p\quad\text{for every odd }p,}
\]
then the unit 2 would immediately force \(I_p=\mathbf Z_p\) and all odd Sha groups zero, with no more computations. However **the Smith theorem does not give this inclusion**: \(I_p\) concerns genuine Selmer groups, whereas the Smith invariant concerns Hecke-congruence linear algebra. No canonical arithmetic morphism or Euler-system reciprocity law supplying this comparison has been constructed in the repository. In particular, the number 2 must not be christened "\(C_{\rm Sha}\)" without such a theorem.

A **real**, non-circular bridge would be a proved morphism between a complex of arithmetic Selmer cohomology and the \(\mathbf Z\)-integral Hecke/motivic lattice, together with compatibility of Fitting ideals and proof that the map's cokernel is killed by 2 (or another fixed squarefree integer). Establishing such a morphism, not another Smith determinant calculation, is the actual target.

## C. Rank of Mordell–Weil ≠ core rank of a Selmer structure

For the canonical Selmer structure on \(T_pE\) over \(\mathbf Q\), the core Selmer rank in Mazur–Rubin's theory is **one**, computed by the \((-1)\)-eigenspace of complex conjugation. It remains one even though \(E(\mathbf Q)\) has algebraic rank **two**. See Mazur–Rubin, *Controlling Selmer groups in the higher core rank case*, and the stated example for an elliptic curve in the core-rank literature.

Consequently **one cannot directly apply a "rank-two Kolyvagin system" theorem with core rank \(r=2\)** by simply substituting \(\operatorname{rank}E(\mathbf Q)=2\). To use Burns–Sakamoto–Sano's higher-rank rigidity/Fitting theorem, one first needs an explicitly constructed **modified Selmer structure of the required core rank**, plus a proven comparison back to the *true* Bloch–Kato/Kummer Selmer structure. Changing local conditions introduces a correction complex; dropping it invalidates the conclusion about actual Sha.

This is a structural arithmetic bottleneck, not a missing numerical test.

## D. 2024–2025 Burns–Kurihara–Sano theorem audit

- Their *On derivatives of Kato's Euler system for elliptic curves* (J. Math. Soc. Japan 76 (2024)) establishes important derivative/order-of-vanishing results in arbitrary rank, but the precise leading-coefficient comparison belongs to the Generalized Perrin–Riou framework and remains conditional in the rank-two situation needed for full complex BSD.
- In the March 2021 version of *On derivatives of Kato’s Euler system and the Mazur–Tate conjecture*, **Theorem 1.1 explicitly assumes "E validates the Birch and Swinnerton-Dyer Conjecture over Q" as (d)**, as well as the Generalized Perrin–Riou conjecture as (e), to obtain the desired Mazur–Tate conclusion. That direction is **BSD ⇒ refined identity**, not a proof of BSD. See https://arxiv.org/abs/2103.11535v1 (Theorem 1.1). The published 2025 paper's abstract describes theoretical evidence, not a solved higher-rank leading-term theorem.
- Theorems of Burns–Sakamoto–Sano on higher-rank Euler/Kolyvagin/Stark systems **can** compare a suitable *primitive* system's initial term with a dual Selmer Fitting ideal under the exact Gorenstein/core-rank hypotheses. But we have **not** constructed such a primitive rank-two system with correct Selmer local conditions for E389a1, nor an all-p rationally descended comparison scalar. The known MW basis wedge \(P\wedge Q\) is not by itself a norm-compatible Euler system, and "primitive in the MW lattice" does not imply "primitive as a Kolyvagin system."

## E. Exact scope of the GRH alternative

Goldfeld's theorem connects the unrestricted original prime-product conjecture to RH for the single L-function \(L(E,s)\), but neither that RH nor the established analytic rank-two certificate creates the required Selmer-to-Hecke comparison. The GRH route is therefore an **optional independent analytic goal**, not a substitute for part B.

## Verified accomplishments versus missing theorem

Already accepted without repetition: algebraic rank 2, rigorously analytic rank 2 (October 19 Arb and modular symbol), Hecke Smith determinant 2, previously certified p-primary parts, source-level p16231 cyclotomic bridge, existing exact Kummer/Fitting identity.

**New fully proved statement in this note:** the squarefree uniform-Selmer-Fitting comparison implies global Sha=0, leveraging the Cassels–Tate pairing.

**Still missing:** independent *existence/construction* of that uniform comparison, and any exact archimedean theorem \(L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\). Neither should be reported as resolved.

## Sources

- J. H. Silverman, *The Arithmetic of Elliptic Curves* (or *Advanced Topics*), Cassels–Tate pairing and perfect-square order for finite elliptic-curve Sha; see also https://www.wstein.org/books/bsd/bsd/node24.html .
- B. Mazur and K. Rubin, *Controlling Selmer groups in the higher core rank case*, https://www.numdam.org/articles/10.5802/jtnb.933/ .
- D. Burns, R. Sakamoto, and T. Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II*, https://arxiv.org/abs/1805.08448 .
- D. Burns, M. Kurihara, and T. Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), DOI 10.2969/jmsj/90699069.
- D. Burns, M. Kurihara, and T. Sano, *On derivatives of Kato's Euler system and the Mazur–Tate conjecture*, IMRN 2025, DOI 10.1093/imrn/rnaf012; arXiv March 2021 Theorem 1.1 explicitly assumes BSD.
