# 389a1 — TRUE one-prime Mazur–Tate height factorization; reduction to ONE scalar identity per prime

**25 November 2026.** **PROVED:** the one-sided radical and rank-one factorization of the actual tame Mazur–Tate height at each anomalous auxiliary prime, by *functoriality in the modulus* and bilinearity alone; an exact two-character reduction; a conditional stronger symmetric local factorization and its determinant consequences. **NOT PROVED:** the required symmetry for the integral finite ray-class height on the restricted lattice from the original biextension convention, the scalar comparison with finite-field reduced Tate pairing, the Kato/Mazur–Tate leading-term equality, Sha finiteness uniformly or full BSD. Unlike fitting Kurihara values, this identifies an independently computable *one-prime* obstruction.

## 1. Correct domain at a SINGLE prime (not only at the two-prime conductor)

Let E=389a1, M=E(Q)/tors=ZP⊕ZQ and \(M_p=M\otimes Z_p\). Fix p≥5, a good q with
\[
q\equiv1\bmod p,\quad p\parallel\#E(\mathbf F_q),\quad
\dim_{\mathbf F_p}E(\mathbf F_q)/p=1,
\]
and suppose the reduction of M is nonzero in this local Fp-line. Fix an identification of the local quotient with Fp and let \(\ell_q:M_p\to F_p\) be the reduction functional.

The single-prime tame Mazur–Tate domain is
\[
M_{q,p}=E_{\{q\}}(\mathbf Q)\otimes Z_p
=\ker(\ell_q:M_p\to F_p).
\]
This is an exact identity of p-adic lattices: the q-local group has p-Sylow Z/p, so its full reduction kernel after Z_p completion is exactly the modp kernel. For the two-prime conductor q1q2, if (\ell_1,\ell_2) is an isomorphism on M/pM, then
\(M_{\{q_1,q_2\},p}=M_{q_1,p}\cap M_{q_2,p}=pM_p\).

The genuine Mazur–Tate biextension height for conductor q is a bilinear pairing
\[
h_q:M_p\times M_{q,p}\to F_p
\]
obtained by the natural ray-class quotient and the chosen primitive-root character. This pairing is DEFINED independently of all modular-symbol theta and any Sha assumptions; see Mazur–Tate 1987 and Darmon 1991 §2.2.

For the conductor q1q2, the genuine height projects onto each one-prime quotient by the canonical ray-class maps \(G_{\{q_1,q_2\}}\to G_{\{q_i\}}\). By functoriality of the biextension construction under quotienting the modulus, the p-projection to \(\chi_r=\ell_{q_1}^{\rm Dir}+r\ell_{q_2}^{\rm Dir}\) is the sum of the corresponding one-prime projections restricted to the common domain pM_p. This does not refer to Sha.

## 2. PROVED (unconditional bilinear algebra): the RIGHT radical is exactly the local reduction line, up to additional degeneracy

Define the divided height on the WHOLE p-adic MW lattice by
\[
H_q(x,y):=h_q(x,p y),\qquad x,y\in M_p.
\]
It descends to an Fp-bilinear form on \(\bar M=M_p/pM_p\) because the output has exponent p.

**THEOREM A (one-sided local factorization).** For every q as above, there exists a UNIQUE functional \(a_q\in\bar M^\vee\) such that
\[
\boxed{H_q(x,y)=a_q(x)\ell_q(y).}
\tag{A}
\]
In particular \(\operatorname{rank}(H_q)\le1\), and the RIGHT radical contains \(\ker\ell_q\).

**Proof.** For \(y\in M_{q,p}=\ker\ell_q\), \(h_q(x,y)\) is defined. Bilinearity in the second argument gives
\[
H_q(x,y)=h_q(x,py)=p\,h_q(x,y)=0\ \text{in }F_p.
\]
Thus H_q(x,-) factors through \(M_p/M_{q,p}\cong F_p\), for each x. Bilinearity in x produces a unique functional a_q with (A). NO symmetry or arithmetic local height comparison was invoked. QED.

This is a previously overlooked global consequence of the **TRUE one-prime domain**, and is stronger than the earlier two-prime lattice result pM_p: it proves rank ≤1 of the *genuine* derived Mazur–Tate height at EACH single prime, not merely of the separately defined finite-field reduced Tate form.

## 3. The SYMMETRIC local factorization: one precisely isolated biextension property

For a principaly polarized elliptic curve it is natural to expect that the canonical tame height is symmetric when both inputs belong to its restricted lattice:
\[
\text{(SYM}_q\text{)}\qquad
h_q(x,y)=h_q(y,x)\quad\text{for every }x,y\in M_{q,p}.
\]
**CAUTION:** this exact symmetry at finite ray-class p-torsion and on the restricted mixed-domain lattice must be checked against the *specific integral Mazur–Tate biextension splitting*; symmetric rational/cyclotomic p-adic heights do NOT automatically establish (SYM_q). Treat it as a distinct verifiable property until its exact source proof is supplied.

**THEOREM B (conditional on SYM_q).** There is a UNIQUE scalar \(\alpha_q\in F_p\) such that
\[
\boxed{H_q(x,y)=\alpha_q\,\ell_q(x)\ell_q(y).}
\tag{B}
\]

**Proof.** By Theorem A, it suffices to show \(H_q(x,y)=0\) whenever \(x\in\ker\ell_q=M_{q,p}\). Then both \(x,py\) belong to \(M_{q,p}\), so (SYM_q) gives
\[
h_q(x,py)=h_q(py,x)=p\,h_q(y,x)=0,
\]
because \(x\) is in the second domain of h_q, and bilinearity in its first argument holds for all y. Therefore a_q(x)=0 for x∈kerℓ_q, so a_q=α_qℓ_q. QED.

Fix any rational point \(e_q\in M_p\) with \(\ell_q(e_q)=1\). The scalar is the genuine SINGLE-PRIME HEIGHT VALUE
\[
\boxed{\alpha_q=h_q(e_q,p e_q)\in F_p.}
\tag{C}
\]
This is independent of which such e_q is used (under SYM_q), without knowing any Kurihara two-factor coefficient. The scalar **may vanish**; symmetry does not prove it is a p-unit.

## 4. Exact character-affinity and two-character acceptance criterion

Take two such primes q1,q2 with (\ell_1,\ell_2):\bar M\to Fp² an isomorphism. Let \(\chi_r=\chi_{q_1}+r\chi_{q_2}\), r∈Fp×, be the diagonal ray-class character.

**THEOREM C (unconditional).** The ACTUAL divided Mazur–Tate height obeys
\[
\boxed{\mathscr H_{\chi_r,p}=H_{q_1}+rH_{q_2}.}
\tag{D}
\]
This is just functoriality under the ray-class projection and Fp-linearity in \chi, not a regulator conjecture.

Therefore for any TWO distinct \(r,s\in F_p\) (including, where relevant, the one-prime characters 0 and ∞), the identities
\[
\mathscr H_{\chi_r,p}=\mathcal B_{q_1}+r\mathcal B_{q_2},
\quad
\mathscr H_{\chi_s,p}=\mathcal B_{q_1}+s\mathcal B_{q_2}
\]
are EQUIVALENT to the TWO one-prime identities \(H_{q_i}=\mathcal B_{q_i}\) (subtract and divide by r−s).

Under both SYM_q conditions, the finite-field reduced-Tate forms satisfy
\[
\mathcal B_{q_i}=w_{q_i}\ell_i\otimes\ell_i.
\]
Then the full desired global *height* comparison is EXACTLY EQUIVALENT to
\[
\boxed{\alpha_{q_1}=w_{q_1},\qquad
\alpha_{q_2}=w_{q_2}.}
\tag{E}
\]
It is no longer a problem of proving arbitrary 2×2 identities, and there are NO two-prime Kurihara sums or Sha assumptions anywhere in this criterion.

In that case an exact determinant identity follows:
\[
\det\mathscr H_{\chi_r,p}
=r\,\alpha_{q_1}\alpha_{q_2}\,
\det\begin{pmatrix}\ell_{q_1}(P)&\ell_{q_1}(Q)\\
                    \ell_{q_2}(P)&\ell_{q_2}(Q)
     \end{pmatrix}^{2}.
\tag{F}
\]
The determinant factorization (F) requires SYM_q and only the existence of the height scalars α_i, **not** the equality α_i=w_i. If no symmetry is granted, Theorem A still yields
\[
\det\mathscr H_{\chi_r,p}
=r\det\begin{pmatrix}a_{q_1}(P)&a_{q_1}(Q)\\
                    a_{q_2}(P)&a_{q_2}(Q)
    \end{pmatrix}
   \det\begin{pmatrix}\ell_{q_1}(P)&\ell_{q_1}(Q)\\
                      \ell_{q_2}(P)&\ell_{q_2}(Q)
   \end{pmatrix},
\]
which is a NONTRIVIAL unconditional rank-one factorization of the true tame derived regulator.

## 5. Frozen numerical single-prime targets for E389a1, p=19 (NO fitted parameters)

For q1=2243 and q2=3877, the independently computed reductions and Tate weights are
\[
v_1=(1,1),\ w_1=17;\qquad v_2=(0,1),\ w_2=18\quad(\bmod19).
\]
Thus the **INDEPENDENT Tate forms** on the saturated basis (P,Q) are
\[
\boxed{\mathcal B_{2243}=\begin{pmatrix}17&17\\17&17\end{pmatrix},\qquad
\mathcal B_{3877}=\begin{pmatrix}0&0\\0&18\end{pmatrix}\pmod{19}.}
\]
The exact desired true biextension-height matrix, for *every* diagonal character r, is
\[
\boxed{\mathscr H_{\chi_r,19}\stackrel?=
\begin{pmatrix}17&17\\17&17+18r\end{pmatrix}\pmod{19}.}
\]

**Minimal genuine heights to establish (under verified SYM_q):**
\[
h_{2243}(P,19P)\stackrel?=17,\quad
h_{3877}(Q,19Q)\stackrel?=18.
\]
The local-kernel vectors are \(Q-P\) at 2243 and P at 3877. With no symmetry assumption, add the true one-sided evaluations to test the left radical:
\[
h_{2243}(Q-P,19P)\stackrel?=0,\quad
h_{3877}(P,19Q)\stackrel?=0.
\]
The right-radical vanishing follows ALREADY from Theorem A and does not need to be computed.

If the desired equality is proved, its determinant at r=1 will equal \(17\cdot18\equiv2\) mod19, so twice this determinant reproduces the previously computed genuine Kurihara coefficient 4 mod19. **That latter coefficient is NOT used to define or solve for any height entry.**

Analogous q-only targets are available for p5 with (41,61): v41=(1,3), w41=3, v61=(1,0),w61=1. Their reduced-Tate matrices are [[3,4],[4,2]] and [[1,0],[0,0]] mod5.

## 6. What is genuinely still unproved

(1) Verify (SYM_q) for the original *finite tame ray-class* Mazur–Tate biextension pairing at a good anomalous q (NOT just for a rationalized p-adic height).
(2) Prove the SINGLE-PRIME scalar height reciprocity \(h_q(e,pe)=\log_\zeta t_{p,q}([N_q/p]\bar e,\bar e)\) using the actual biextension/finite-field Kummer formalism, including exact unit/sign normalizations.
(3) Separately compare the true Kato/Mazur–Tate mixed theta coefficient with the genuine regulator, **retaining the global Selmer/Sha determinant factor**. Even a full proof of (1),(2) would not establish BSD without (3).

No additional pairwise modular-symbol computation can replace these tasks. The present note records an exact THEOREM A and its clear, falsifiable upgrade, and does not label (E) as proved.

Primary sources:
- Mazur–Tate (1987), *Refined conjectures of the Birch and Swinnerton–Dyer type*, Chapter II.
- Henri Darmon (1991), *Euler systems and refined conjectures of Birch–Swinnerton-Dyer type*, §2.2: https://www.math.mcgill.ca/darmon/pub/Articles/Research/06.Euler-systems/paper.pdf
- Burns–Kurihara–Sano (2021), §2.2, definition of the mixed-domain tame height: https://arxiv.org/abs/2103.11535
- Prior proven one-prime reduced Tate forms and independent Miller weights: paper/bsd389_independent_reduced_Tate_local_weights_rank2_global_delta_conjecture_2026-11-24.md
