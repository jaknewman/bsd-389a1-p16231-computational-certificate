# E389a1: the published Kato–Kurihara bridge and an adversarial p=7 test for the two-prime Selmer comparison

**2026-11-13.** This note separates (A) an existing, proved explicit reciprocity law, (B) newly verified elementary finite-field arithmetic, and (C) pre-existing user-authenticated Sage/eclib Kurihara values. It makes no global \(\Sha\)-finiteness or BSD assertion.

## 1. Fixed-prime cohomological reciprocity is already available in the literature

Primary source: F. Castella–T. Sano (2026), *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, §2.1.2, Theorem 2.1.3:
https://arxiv.org/html/2601.14504#S2.SS1.SSS2
(the authors cite C.-H. Kim, Theorem 3.11, and K. Kim–M. Kim–H. Sun 2020).

For p>3 with surjective residual representation and p-unit Manin constant, and an admissible squarefree n>1, the derived Kato class satisfies a finite-level explicit reciprocity formula, in the source's compatible coefficient module \(\mathbf Z_p/I_n\):

$$
\exp_{\omega_E}^*(\operatorname{res}_p(\kappa_n^{\mathrm{Kato}}))
=u_n\cdot p^{t_p}\,\widetilde\delta_n
\quad\bmod I_n,
\qquad u_n\in(\mathbf Z_p/I_n)^\times,
\qquad p^{t_p}=\#E(\mathbf Q_p)[p^\infty].
\tag{1}
$$

This is **an existing theorem**, not a novel comparison map constructed in the project. It must be applied with the exact derived-class, local-condition and Manin-normalization conventions of the original paper. It is **not** a homomorphism from the integral oldform Hecke cokernel onto the full Selmer dual.

At p=7 the exact prior point count \(\#E(\mathbf F_7)=13\) guarantees \(E(\mathbf Q_7)[7^\infty]=0\): the good-reduction formal group has no 7-torsion and the reduction group has order prime to 7. Hence \(t_7=0\), and modulo 7

$$
\overline{\exp_{\omega_E}^*(\operatorname{res}_7(\kappa_n))}
=\bar u_n\,\overline{\widetilde\delta_n}.
$$

Thus, for the genuinely calculated p=7 pairs, vanishing/nonvanishing of this **dual-exponential image** matches the mod-7 Kurihara coefficient. A zero dual-exponential image does **not** imply a zero global Kato class.

## 2. Independent exact elliptic-curve arithmetic at p=7

The curve is \(E:y^2+y=x^3+x^2-2x\). The companion dependency-free script recomputes every trace by the exact Legendre sum \(-\sum_x\left(\frac{4x^3+4x^2-8x+1}{q}\right)\). Its result is:

| q | a_q | #E(F_q) | v7(#E(F_q)) | #E(F_q)/7^v mod7 |
|---|---:|---:|---:|---:|
| 113 | 9 | 105 | 1 | 1 |
| 281 | -12 | 294 | 2 | 6 |
| 673 | 2 | 672 | 1 | 5 |

The **new exact two-point certificate at q=281** consists of
$$R=(20,74),\quad S=(22,61)\in E(\mathbf F_{281}).$$
The independent group-law implementation proves \(7R=7S=O\) and \(S\notin\langle R\rangle\) (and \(R+S=(210,36)\)). Thus
$$
E(\mathbf F_{281})[7]\simeq(\mathbf Z/7)^2.
\tag{2}
$$
Since 294 has exactly 7² in its factorization, the whole 7-primary part is \((\mathbf Z/7)^2\); \(E(\mathbf F_{281})\simeq\mathbf Z/7\oplus\mathbf Z/42\).

For good primes q≠p the local Kummer image is \(E(\mathbf F_q)/p\), whose dimension equals \(\dim_{\mathbf F_p}E(\mathbf F_q)[p]\). Consequently:

$$
\dim L_{113}=1,\qquad\dim L_{281}=2,\qquad\dim L_{673}=1.
\tag{3}
$$

In particular the p=7 congruence conditions \(q\equiv1\pmod7,\ a_q\equiv2\pmod7\) **do not imply the local Kummer line condition** required by our prior two-prime Poitou–Tate theorem. This is a concrete obstruction, not just an unverified hypothesis. The pair (113,281) has local target dimension \(1+2=3\), strictly greater than the rational MW mod-7 dimension 2, so the MW images CANNOT be surjective. The previously certified (113,673) pair does have two one-dimensional lines and a unit MW localization determinant (3 mod7).

At q=281, Frobenius on E[7] is the identity, since all 49 points of E[7] are F281-rational. At q113/q673 the 7-torsion is only 1-dimensional.

## 3. Normalized oldform direction is not Kurihara primitivity

For standard oldform degeneracy maps at q∤389 the normalized 2×2 pairing is
$$D_q=\begin{pmatrix}q+1&a_q\\a_q&q+1\end{pmatrix}.$$
Its antidiagonal eigenvalue is \(q+1-a_q=\#E(\mathbf F_q)\). For n=q1q2 the fully mixed vector \((1,-1,-1,1)\) in \(D_{q1}\otimes D_{q2}\) has eigenvalue
$$\lambda_{\rm mix}=\#E(\mathbf F_{q1})\#E(\mathbf F_{q2}).$$
Its saturation by the **full exact** \(p\)-valuation is always a p-adic unit by definition. The freshly rerun p7 values are:

| q pair | v7(lambda_mix) | (lambda_mix/7^v) mod7 | archived true delta_n mod7 |
|---|---:|---:|---:|
| 113·281 | 3 | 6 | **0** |
| 113·673 | 2 | 5 | **2** |

The delta columns are NOT freshly computed here: they are from the genuine complete Sage/eclib 2026-10-29 user run archived at
[results/bsd389_k7_hecke_zero_nonzero_dual_PASS_2026-10-29.md](../results/bsd389_k7_hecke_zero_nonzero_dual_PASS_2026-10-29.md), which checks exact Hecke fibres and original Manin-symbol sums. The new independent script verifies only the local point counts, integral eigenvalue arithmetic and the two concrete E[7] generators.

**Counterexample to a precise invalid inference:**
$$
(\lambda_{\rm mix}/7^{v_7(\lambda_{\rm mix})})\in\mathbf Z_7^\times
\ \centernot\implies\
\widetilde\delta_n\not\equiv0\pmod7.
\tag{4}
$$

The structural arithmetic difference is visible already in the **auxiliary Kurihara ideal**
$$
I_q=(q-1,\ a_q-q-1)\mathbf Z_7,\qquad I_n=\prod_{q\mid n}I_q.
$$
For both pairs, \(v_7(I_n)=2\), whereas the oldform mixed eigenvalues have valuations 3 and 2 respectively. For q281 the second factor in \(\#E(\mathbf F_{281})=294\) cannot be read off from \(v_7(I_{281})=1\). The filtrations are **not** identical.

This does **not** prove that full 7-torsion at q281 caused delta_n=0; it only proves the two primes differ sharply in local Galois type and that the naive local-unit criterion fails.

## 4. Exact revised research target

- **Already proved by published theorems:** the finite-level Kato-to-Kurihara explicit reciprocity law, and the Selmer-structure/Fitting comparison under Kim/Castella–Sano conditions.
- **Already proved by our earlier project notes:** when a chosen pair has two 1D local Kummer spaces and the MW localization matrix is invertible, strict/transverse Selmer equals \(\Sha[p]\).
- **Still open:** a genuinely **all-large-p, two-prime** nonvanishing theorem for \(\widetilde\delta_{q_1(p)q_2(p)}\), with admissible primes that also meet the 1D line conditions when applying the semilocal theorem, and compatible normalizations across all p. The unrestricted-degree nonvanishing theorem is insufficient to force degree two.

A proposed independent integral Euler/Kolyvagin construction should be tested against both archived p7 pairs, not only the nonzero one. Any proposed universal identity from oldform mixed eigenvalues to Kurihara units is false unless it incorporates a genuinely **global modular-symbol/cohomological correction**.

**Verdict:** we have identified the existing published cohomological map and supplied a new exact finite-field witness of the difference between p-admissibility and 1D local Kummer hypotheses, plus a robust adversarial regression. No new p-primary Sha vanishing and no global BSD proof.
