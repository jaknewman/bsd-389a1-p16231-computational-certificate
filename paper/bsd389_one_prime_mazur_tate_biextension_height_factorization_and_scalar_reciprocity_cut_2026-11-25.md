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


## 7. SOURCE-VERIFIED UPGRADE: (SYM_q) IS A THEOREM of the original Mazur–Tate biextension

After direct examination of Ki-Seng Tan, *Refined theorems of the Birch and Swinnerton-Dyer type*, Ann. Inst. Fourier **45** (1995), §2.1 Remark (3), p.331, and §4.4 equation (60), p.360, **the auxiliary assumption (SYM_q) made in §3 is now DISCHARGED** for the genuine canonical Mazur–Tate pairing.

Tan §2.1 Remark (3) proves that the canonical local splitting on the original biextension equals its mirror image on the intersection of their domains. This includes the *tamely ramified* local trivialization (L4), where the first coordinate lies in \(A_v=E(K_v)\) and the second in \(B_v=E_1(K_v)\); both coordinates in \(B_v\) lie in the intersection. Thus the global **actual** biextension pairing obeys equation (60):
\[
\boxed{
\langle x,y\rangle_G=\langle y,x\rangle_G
\quad\text{for every }x,y\in B_S.}
\tag{TAN-60}
\]
This property is stated **BEFORE** Tan introduces any hypothesis \((\ell,G)\) is good in §4.4; it follows solely from principal self-duality and the canonical mirror splitting. It is therefore available without assuming either BSD or Sha finiteness.

**THEOREM (unconditional two-sided radical and scalar factorization).** For every good anomalous q with p||#E(Fq), and for the genuine single-prime p-order ray-class Mazur–Tate height, the divided form \(H_q(x,y)=h_q(x,p y)\) on the p-adically completed saturated MW lattice satisfies
\[
\boxed{H_q(x,y)=\alpha_q\,\ell_q(x)\ell_q(y),\qquad\alpha_q\in\mathbf F_p.}
\tag{S}
\]
The proof in §3, previously conditional on (SYM_q), is now unconditional by (TAN-60): if x∈kerℓ_q=B_{q,p}, then both x and py are in B_{q,p}, and
\(h_q(x,py)=h_q(py,x)=p h_q(y,x)=0\).
Combine with the right radical already proved in §2 to obtain (S).

**No hidden nonvanishing:** the theorem DOES NOT say \(\alpha_q\ne0\); at this stage \(\alpha_q\) may vanish.

**WARNING ABOUT TAN LEMMA 4.11:** Tan's Lemma 4.11(a) would imply that the first local height block is nondegenerate, BUT explicitly assumes the pair \((\ell,G)\) is *good*. Tan **Definition 3.13** defines "good" by demanding the **BSD conjecture true for (E,G)** plus the condition
\[
6w|\Sha_K|\prod_v m_v\not\equiv0\bmod\ell.
\]
This is a circular assumption for our all-prime BSD research, even if the local reduction cokernel has no p-part. **We therefore DO NOT invoke Tan's Lemma 4.11** to claim \(\alpha_q\) is a p-unit. Equation (60) itself is independent of this "good" hypothesis, as can be seen from its derivation from §2.1 Remark (3).

**References:** https://www.numdam.org/article/AIF_1995__45_2_317_0.pdf ; §2.1 pp.330–331, §3.13 p.350, §4.4 p.360 equations (60)–(61), Lemma 4.11 p.360. This upgrade supersedes the conditional status labels attached to (SYM_q) in §3, §4 and §6 of the earlier note.

### 7.1. Correct HONEST RATIONAL REPRESENTATIVES for the p-adic second point

The symbol \(h_q(e,p e)\) in §3 is shorthand for the unique p-adically extended height \(h_q:M_p\times M_{q,p}\to\mathbf F_p\). **The literal rational point p e need not reduce to zero modulo q**, because the prime-to-p component of E(Fq) may survive multiplication by p. It is WRONG to present it as an unqualified value of the original rational restricted pairing.

For an actual rational computation, choose a positive integer u with
\(u\equiv1\bmod p\) and \(\#E(\mathbf F_q)/p\mid u\). Then \(up e\in E_{\{q\}}(\mathbf Q)\) and \(\alpha_q=h_q(e,up e)\) in Fp.

For our p19 target:
- q=2243, \(\#E(\mathbf F_q)/19=119\), choose \(u=476=4\cdot119\equiv1\bmod19\); then the honest rational height is
\[
\boxed{\alpha_{2243}=h_{2243}(P,19\cdot476\,P)\ \stackrel?=17.}
\]
- q=3877, \(\#E(\mathbf F_q)/19=199\), choose \(u=3383=17\cdot199\equiv1\bmod19\); then
\[
\boxed{\alpha_{3877}=h_{3877}(Q,19\cdot3383\,Q)\ \stackrel?=18.}
\]
These are bona fide values of the **original** Mazur–Tate height on actual rational points, with the actual domain condition satisfied. The RHS are the **independently computed reduced Tate pairing weights**, not results of calculating the LHS. No equality of these scalar values has yet been proved or executed.

### 7.2. The exact rank-two matrix follows from TWO scalar identities, with no symmetry uncertainty

For the p19 basis (P,Q), the actual global ray-class projection to \(\chi_r=\chi_{2243}+r\chi_{3877}\) satisfies **as a proved identity**
\[
\boxed{\mathscr H_{\chi_r,19}
=\alpha_{2243}\begin{pmatrix}1&1\\1&1\end{pmatrix}
+r\alpha_{3877}\begin{pmatrix}0&0\\0&1\end{pmatrix}.}
\]
This is a TRUE biextension consequence of Tan-60 and modulus functoriality; it is NOT the predicted Tate pairing equality yet. The remaining exact single-prime scalar comparisons would yield the matrix
\(\bigl(\begin{smallmatrix}17&17\\17&17+18r\end{smallmatrix}\bigr)\bmod19\).

### 7.3. Absolute arithmetic stop sign

The nonvanishing claim \(\alpha_q\ne0\) is NOT available from Tan Lemma 4.11 in our present proof, because the lemma's "good" hypothesis **includes BSD over Q**. Any apparent all-prime Sha result deduced by invoking it would be circular. The genuinely independent next theorem is the exact local reciprocity formula
\[
h_q(e,up e)=
\log_{\zeta_q}t_{p,q}([N_q/p]\bar e,\bar e)
\]
at ONE q, with a proof from the canonical tame biextension splitting and local Kummer/Tate cohomology, respecting the precise q-root generator and sign. This statement is not established by (TAN-60) alone.

**Source audit date: 25 November 2026.** No new numerical pairwise Kurihara computation required.


## 8. NEW EXACT LOCAL-SUPPORT LEMMA: the actual one-prime global height scalar is ONE tame Poincaré splitting value

Here is a further reduction, independent of any BSD theorem and derived from Tan §2.1 and Definition 2.6. **It does NOT yet identify the tame Poincaré value with the reduced finite-field Tate pairing.**

Let q be a good auxiliary prime as in §1, \(p\parallel\#E(\mathbf F_q)\), \(p\ne q\), and let the only bad rational prime of E be 389, with Tamagawa number one. Let \(e\in E(\mathbf Q)\) be a MW generator of the one-dimensional local quotient E(Fq)/p; choose a positive integer \(u\equiv1\bmod p\), divisible by \(\#E(\mathbf F_q)/p\). Then \(b=up e\) reduces to O at q and is therefore in the honest global group \(B_{\{q\}}=E_{\{q\}}(\mathbf Q)\).

Denote by \(\mathscr P\) the actual Poincaré biextension of E×E by \(\mathbf G_m\). Choose a rational biextension lift \(\eta\in\mathscr P(\mathbf Q)\) of the rational pair \((e,u e)\); it exists since every \(\mathbf G_m\)-torsor over the field Q has a Q-point (Hilbert 90). Let
\[
\eta^{[p]}:=p_{\mathrm{second}}\cdot\eta
\]
be p-fold addition in the SECOND biextension direction: it lies over \((e,p u e)=(e,b)\) and hence belongs to the restricted Mazur–Tate biextension. Write \(\psi_v\) for Tan's canonical local splitting at each v, and \(\psi'_v\) for its mirror splitting.

**THEOREM (one-ramified-place support).** Let \(\chi_q\) be the order-p global ray-class quotient attached to q. Then
\[
\boxed{
h_q(e,up e)=
\chi_q\left(\,[\psi_q(\eta_q^{[p]})]\,\right)\in\mathbf F_p,
}
\tag{LS}
\]
where the bracket denotes the q-local tame idele class, with the understanding that the identity is in the genuine global class-field quotient (and therefore insensitive to global Q× and local pth powers). The RHS is independent of the chosen rational biextension lift \(\eta\).

**Proof.** By Tan Definition 2.6, the global value is the image of the idele of local splitting values \((\psi_v(\eta_v^{[p]}))_v\) under global ray-class reciprocity. For each finite v≠q, because E has good reduction there or has Tamagawa component group of order one at 389, the local point e lies in the self-dual intersection \(B_v=E_0(\mathbf Q_v)\subset A_v\). Tan §2.1 Remark (3) identifies \(\psi_v\) and its mirror \(\psi'_v\) on that intersection. Since the original \(\eta_v\) lies over \((e,u e)\) with BOTH coordinates in that intersection, its p-fold second-direction image has
\[
\psi_v(\eta_v^{[p]})=p\,\psi'_v(\eta_v).
\]
The ray-class character \(\chi_q\) has order p and therefore kills these local pth-power contributions. At the real place the order-p character is necessarily trivial (p odd). Only the q-local component can survive, proving (LS). If the rational lift \(\eta\) is replaced by \(c\eta\), \(c\in\mathbf Q^\times\), its p-fold second-direction lift differs by \(c^p\), which has trivial order-p ray-class image. QED.

**WARNING on notation:** A local splitting \(\psi_q\) takes values in \(\mathbf Q_q^\times/(1+q\mathbf Z_q)\), and the order-p ray-class quotient is mapped to \(\mathbf F_p\) using the prescribed primitive root/discrete logarithm orientation. One must keep this normalization explicit when comparing to the Miller reduced Tate pairing. The formula is NOT an assertion that an arbitrary q-local splitting is equal, as an element of Fq×, to a Miller function: the latter exact identification remains the research gap.

**IN PARTICULAR:** The single-prime scalar in the *proved* rank-one factorization is an honest **local tame-biextension obstruction**, not a generic global Kato L-value:
\[
\boxed{
\alpha_q
=h_q(e,up e)=\operatorname{logrec}_{q,p}
\big(\psi_q(\eta_q^{[p]})\big).
}
\tag{LOC}
\]
The reduced Tate weight \(w_q\) is another independent local construction. The remaining one-prime equality is exactly (LOC) \(=w_q\), with its primitive-root and sign convention. This isolates the comparison of two LOCAL pairings at a single finite field point, and DOES NOT require any finite-pair Kurihara sums or a rank-two Euler system.

**Source:** Ki-Seng Tan (1995), §2.1 Remark (3), pp.330–331; §2.2 Definition 2.6, pp.333–334; §4.4 proof of Lemma 4.11, especially pp.361–363, where all v≠v0 contributions disappear modulo ℓ by the same mirror-splitting principle. His Lemma 4.11 itself assumes BSD through "good" and is NOT being invoked for nondegeneracy; only the unconditional *local splitting property and definition of h* are used here.

### Remaining exact unproved compatibility

The desired **new local reciprocity theorem** is now a fully specified identity of two local constructions:
\[
\boxed{
\operatorname{logrec}_{q,p}\psi_q(\eta_q^{[p]})
\stackrel{?}{=}
\log_{\gamma_q^{(q-1)/p}}
t_{p,q}\!\left([\#E(\mathbf F_q)/p]\bar e,\bar e\right).
}
\tag{LOCAL-MT-TATE}
\]
The LHS depends on the CANONICAL TAME POINCARÉ splitting at q; the RHS depends on the independently defined reduced Tate pairing, calculable via Miller. A proof must identify the connecting homomorphism in the p-multiplication sequence of the local Poincaré biextension with the explicit finite-field Frobenius-Kummer operator \(-N_q\), including the root-of-unity/Artin-sign conventions. We have NOT proved that specific identification.

If LOCAL-MT-TATE is proved, Sections 2–4 and 7–8 yield the global HEIGHT equality \(\mathscr H_{\chi_r,p}=\mathcal B_{q_1,p}+r\mathcal B_{q_2,p}\) as a theorem. This would *not*, without a separate Kato leading-coefficient theorem, establish the global Kurihara ILTR conjecture or BSD.


## 9. IMPORTANT NEW NORMALIZATION DISCOVERY: a p-UNIT M_q^(-1) can intervene between biextension monodromy and the OLD reduced-Tate weight

The previous §7–8 candidate \(\alpha_q=w_q\) MUST NOT be treated as established. An exact finite-field algebraic comparison reveals a **potential prime-dependent missing unit**.

Let
\[
N_q=\#E(\mathbf F_q)=pM_q,\quad p\nmid M_q,\quad
e\in E(\mathbf Q),\ \ell_q(e)=1,
\]
and choose u as in §7.1, i.e. \(M_q\mid u\) and \(u\equiv1\bmod p\). Reduction of \(e\) gives \(\bar e\in E(\mathbf F_q)\). Define TWO points of order p:
\[
g_q=[M_q]\bar e,\qquad
b_q=[u]\bar e=[u/M_q]g_q.
\]
Because \(u/M_q\equiv M_q^{-1}\bmod p\), we have the **EXACT algebraic identity**
\[
\boxed{b_q=[M_q^{-1}\bmod p]\,g_q.}
\tag{NORM}
\]
The reduced Tate pairing is bilinear. Hence with the SAME second argument \(\bar e\),
\[
\boxed{
\log_\zeta t_{p,q}(b_q,\bar e)
=M_q^{-1}\log_\zeta t_{p,q}(g_q,\bar e)
=M_q^{-1}\,w_q\quad(\bmod p).
}
\tag{SCALE}
\]
This is PROVED from the finite group law, the true p-adic rational representative condition and Tate bilinearity alone.

**Why it changes the next proof:** The biextension lift \(\eta\) in the local-support formula (LS) lies over \((e,u e)\). Its q-reduction has SECOND coordinate \(b_q=[u]\bar e\in E(\mathbf F_q)[p]\). Multiplication by p in the SECOND biextension direction leads to the p-monodromy of this **b_q**, not of \(g_q=[M_q]\bar e\). Damien Robert, *Fast pairings via biextensions and cubical arithmetic*, Corollary 2.5 and Corollary 3.12, identifies finite-field p-monodromy in the Poincaré biextension with the Tate pairing, up to the declared principal-polarization sign convention.

**Consequently, IF** the canonical tame local Néron–Mazur–Tate splitting \(\psi_q\) in (LS) reduces to precisely that finite-field Poincaré p-monodromy with no further local scalar correction, the resulting normalized height must be
\[
\boxed{\alpha_q=\varepsilon_q M_q^{-1}w_q,\qquad
\varepsilon_q\in\{+1,-1\}\quad\text{(orientation-dependent)}.}
\tag{CORRECTED-CANDIDATE}
\]
A proof of the **IF** clause, matching the reduction of Tan's canonical tame splitting with Robert/Stange's finite-field Poincaré monodromy, is required. It is NOT provided by the elementary identity (SCALE). One should **not** simply assert that \(\alpha_q=w_q\), nor assert that the corrected candidate is already a theorem, before performing this normalization comparison.

For the concrete p19 examples,
\[
M_{2243}=119\equiv5\bmod19,\quad M_{2243}^{-1}\equiv4,\quad w_{2243}=17,
\]
\[
M_{3877}=199\equiv9\bmod19,\quad M_{3877}^{-1}\equiv17,\quad w_{3877}=18.
\]
Thus the *suggested* corrected p19 height scalars are
\[
\boxed{\alpha_{2243}\stackrel?=\varepsilon_1\cdot11,\qquad
\alpha_{3877}\stackrel?=\varepsilon_2\cdot2\quad(\bmod19),}
\]
rather than the old **unqualified** (17,18). This is a serious p-unit distinction. The old values are still the UNAMBIGUOUS independently computed reduced-Tate weights; the genuine biextension height values have NEVER BEEN evaluated directly, and the data do NOT decide which scalar normalization is correct.

With compatible self-duality orientations \(\varepsilon_1=\varepsilon_2=\varepsilon\), the corrected two-prime form would be
\[
\mathscr H_{\chi_r,p}
\stackrel?=\varepsilon\left(
M_{q_1}^{-1}\mathcal B_{q_1}
+r M_{q_2}^{-1}\mathcal B_{q_2}\right).
\tag{CORRECTED-HEIGHT}
\]
Its determinant is independent of the common sign, and
\[
\boxed{
\det(\mathscr H_{\chi_r,p})
\stackrel?=r(M_{q_1}M_{q_2})^{-1}
\det(\mathcal B_{q_1}+\mathcal B_{q_2}).}
\]
The empirical Kurihara law \(\tilde\delta_{q_1q_2}=2\det(\mathcal B_{q_1}+\mathcal B_{q_2})\) would then be consistent with a future **Kato-to-Mazur–Tate** comparison containing the explicit unit factor \(2M_{q_1}M_{q_2}\). But that latter global identity is STILL conjectural and needs a correct conductor/cokernel/period normalization; do not assume those factors are exactly \(2M_1M_2\) from finite matches alone.

**This is an actual useful falsification pressure on our ORIGINAL proposed height equality.** In particular it is WRONG to report the old predicted scalars 17,18 as computed genuine Mazur–Tate heights at p19. They are only local Tate weights.

Reference for monodromy interpretation: Damien Robert, *Fast pairings via biextensions and cubical arithmetic*, Corollary 2.5 and Corollary 3.12, https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/articles/biextensions.pdf . The paper carefully warns about divisor and sign conventions. Reference for tame canonical splittings: Tan (1995) §2.1 (L4), §4.4 eq. (60).


## 10. UPGRADE 2026-11-25 — LOCAL MONODROMY COMPARISON PROVED, WITH CORRECTED SCALAR

The normalization issue raised in §9 has now been resolved through a geometric proof, using the **canonical tame reduction splitting on the Néron/Poincaré biextension** (Tan §2.1 L4 and uniqueness) and the standard p-monodromy = finite-field Tate pairing theorem (Robert 2024, Corollaries 2.5 and 3.12). Full proof and assumptions:
[bsd389_2026-11-25_local_MT_Tate_monodromy_comparison_proof_corrected_Minverse.md](bsd389_2026-11-25_local_MT_Tate_monodromy_comparison_proof_corrected_Minverse.md).

**CORRECTED theorem, up to ONE global Artin/self-duality orientation sign \(\varepsilon\):**
\[
\boxed{
H_q(x,y)=\varepsilon M_q^{-1}\mathcal B_q(x,y),\quad
\mathscr H_{\chi_r,p}
=\varepsilon(M_{q_1}^{-1}\mathcal B_{q_1}+rM_{q_2}^{-1}\mathcal B_{q_2}),
\quad
M_q=\#E(\mathbf F_q)/p\bmod p.
}
\]
The geometric proof is independent of Sha finiteness, Kato zeta or modular-symbol numerics. In particular the (E) equalities \(\alpha_q=w_q\) previously labelled an open target are, with these weight conventions, **INCORRECT IN GENERAL**; the correct scalar is \(\varepsilon M_q^{-1}w_q\). Its remaining orientation sign must be frozen by the exact convention of local reciprocity.

At p19, this predicts actual divided Mazur–Tate height scalars \(\varepsilon\cdot11\) at q2243 and \(\varepsilon\cdot2\) at q3877, rather than the uncorrected 17,18; the determinant is 3 modulo19 and independent of \(\varepsilon\).

**Scope:** This completes the geometric *HEIGHT* bridge, with the declared sign convention. It does NOT give the global leading-coefficient/Kato regulator identity or prove any additional global primewise Sha vanishing. The empirical Kurihara congruence \(\delta_{q_1q_2}=2\det(\mathcal B_{q_1}+\mathcal B_{q_2})\) needs an independent **Kato/Mazur–Tate leading-term comparison** with local factors \(2M_{q_1}M_{q_2}\) and the genuine Selmer/Sha determinant.
