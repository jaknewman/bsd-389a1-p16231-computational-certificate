# 389a1 at p=599 — source-normalized Pollack scalar quadratic unit and signed Selmer Sha-vanishing argument

**23 November 2026.** This is a **computer-assisted theorem proposal with source-level normalization audited against primary Pollack (2003), the current SageMath supersingular source, Burungale–Skinner–Tian–Wan (2024) and B. D. Kim (2013)**. It uses a user-authenticated historic genuine modular-symbol input, a second historical independent integral-Manin reconstruction and a fresh all-179101-representative JavaScript recomputation on 2026-11-23. Its mathematical steps are exact, but they remain subject to independent human review of the agreement between the archived integral modular-symbol vector and the true Néron-normalized eclib plus symbols. It is **not** a claim of global Sha finiteness or strong BSD.

## 1. Arithmetic input and true normalization

E=389a1: y²+y=x³+x²−2x; N=389, squarefree and semistable; rank E(Q)=2, torsion1, c_389=1, c_Manin=1, residual GL2(F599) surjective. p=599, a_p=0 (good supersingular).

The user's archived **genuine eclib** modular-symbol table has hash
  fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
and its conductor-p² moments are (C0,C1,C2)=(0,0,543) mod p. This was independently reconstructed from a *different* integral 390-Manin vector in branch
\`proof/p599-signed-main-conjecture-unit-closure-2026-11-15\`, verification file \`bsd389_p599_independent_integral_390_moment_20261115.py\`.

On 23 Nov the assistant independently fetched this 390-entry exact source and recomputed **all 179101 half units** via a new JavaScript continued-fraction evaluator: C0=C1=0, C2=543, signed scalar candidate -543/2=28 mod599. The new standalone Python checker in the active research PR redundantly implements this full integral computation.

## 2. Exact p³→p² arithmetic, without enormous conductor-p³ modular symbols

Fix p=599, alpha²=−p and gamma=1+p, as in Sage’s \`pAdicLseriesSupersingular.series(n=3,prec=3,eta=0)\`. Let
\[
j_n(a)\in\mathbf Z/p^{n-1}\mathbf Z
\quad\text{be determined by}\quad
a\equiv\omega(a)\gamma^{j_n(a)}\pmod{p^n}.
\]
Put \(w(j)=\binom j2\), and let \(m^+(a/p^n)\) be the PLUS Néron-normalized modular symbols.

The exact Sage supersingular measure is
\[
\mu_\alpha(a+p^3\mathbf Z_p)
=\alpha^{-3}m^+(a/p^3)-\alpha^{-4}m^+(a/p^2).
\]
Since \(\alpha^4=p^2\), \(\alpha^{-3}=\alpha/p^2\), \(\alpha^{-4}=1/p^2\). Sage divides the plus measure by **two** because E389a1 has exactly two connected real components. Thus
\[
[T^2]\mathcal L_\alpha^{(3)}
=(\alpha A_3-B_3)/(2p^2)
\]
with
\[
A_3=\sum_{a\bmod p^3}w(j_3(a))m^+(a/p^3),\quad
B_3=\sum_{a\bmod p^3}w(j_3(a))m^+(a/p^2).
\]
All sums are over units and Teichmüller exponents as in the original source.

For each fixed b mod p², its p lifts have j_3 congruent to j_2(b)+p k for k=0,...,p−1. Because
\[
\sum_{k=0}^{p-1}\binom{j+pk}{2}
\equiv p\binom{j}{2}\pmod{p^2}
\]
for every integer j and odd p, we have
\[
\boxed{B_3\equiv p C_2\pmod{p^2}.}
\]
In particular \(B_3\) is divisible by p and \(B_3/p\equiv543\bmod599\). No A_3 cusp values are needed to compute the **scalar** coefficient of the eigenvalue distribution.

## 3. From the alpha-eigenvalue distribution to a genuine signed Iwasawa coefficient

Pollack, *On the p-adic L-function of a modular form at a supersingular prime* (Duke Math. J. 118 (2003)), Introduction eq. (1), §4, Theorem 5.1, defines the two genuine bounded signed functions by
\[
\mathcal L_\alpha(T)=G(T)+\alpha H(T)
=\mathcal L^{+,P}_p(T)\,\log_p^+(T)
+\alpha\,\mathcal L^{-,P}_p(T)\,\log_p^-(T).
\]
The superscript P denotes Pollack’s *own* sign convention. Both half-logs have constant \(1/p\), from their cyclotomic-product definition. Pollack’s plus corresponds to the **scalar** G. A conventional change of +/- labels between Pollack and other authors does not matter: the 2024 signed main conjecture and the 2013 no-finite-submodule theorem apply to **both** in this F=Q cyclotomic setting.

**Exact order-two lower-coefficient gate.** The known MW rank 2 maps injectively into the Gamma-invariants of the plus and minus signed Selmer over Q∞ (base local rational points satisfy both signed trace conditions; full residual GL2 means E[p∞](Q∞)=0). Together with the proved 2024 signed main conjectures, this implies \(T^2\mid \mathcal L_p^{+,P}\) and \(T^2\mid\mathcal L_p^{-,P}\); no unproved p-adic BSD leading term is invoked. Therefore the *scalar* \(T^2\) coefficient satisfies
\[
[T^2]G(T) = \frac1p [T^2]\mathcal L_p^{+,P}(T)
\]
with no contamination from lower logarithm derivatives.

**Rigorous precision.** Sage’s own \`pAdicLseriesSupersingular._prec_bounds(3,3)[2]\` is \(2\cdot2-(3+2)=-1\) in the alpha-adic valuation \(v_\alpha(\alpha)=1,v_\alpha(p)=2\); hence the error of the n=3 approximate scalar quadratic coefficient lies in \(\mathbf Z_p\): indeed
\[
\alpha^{-1}\mathcal O_{\mathbf Q_p(\alpha)}
=\alpha^{-1}\mathbf Z_p+\mathbf Z_p
\]
and \(\alpha^{-1}=-\alpha/p\) has no scalar part. Multiplying by p makes the scalar error divisible by p.

Consequently, combining the exact n=3 coefficient, p-adic precision and Pollack log(0)=1/p gives
\[
\begin{split}
[T^2]\mathcal L_p^{+,P}
&\equiv p\,[T^2]\mathcal L_\alpha^{(3)}\big|_{\mathrm{scalar}}\\
&=-\frac{B_3}{2p}\equiv-\frac{C_2}{2}
\equiv\boxed{28}\pmod{599}.
\end{split}
\]
**This is a unit coefficient of the *genuine signed function*, not merely a formal coefficient of the modular-symbol polynomial.** The only arithmetic-input dependency is the authentic normalized modular-symbol table noted in §1. The sign choice is immaterial for unit/nonunit purposes; do NOT silently swap the sign labels in written references.

### Source-level references checked

- SageMath source \`sagemath/sage\` develop, \`src/sage/schemes/elliptic_curves/padic_lseries.py\`: the supersingular \`series\` doc explicitly uses \(\gamma=1+p\), \`measure\` uses \(\alpha^{-n}m^+(a/p^n)-\alpha^{-n-1}m^+(a/p^{n-1})\); \`series\` divides by \`self._E.real_components()\` for +; \`_prec_bounds\` uses \([2 e_j-(n+2)]\). Fetched source blob SHA \`9f4faa665bb36ad6e711291807d8b85cceea04d1\`.
- Pollack 2003 original, Introduction (1), Theorem 5.1, half-log cyclotomic-product definition: https://math.bu.edu/people/rpollack/Papers/On_the_padic_Lfunction_of_a_modular_form_at_a_ss_prime.pdf

## 4. Arithmetic consequence from proven theorems, not a BSD assumption

Burungale–Skinner–Tian–Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350v2, **Theorem 1.3**, establishes for our semistable E and p599 the Kobayashi signed main conjectures:
\[
\operatorname{char}_{\Lambda}(X^\pm)=(L^\pm_p)
\]
for each sign, with Lambda=Zp[[T]].

From the MW rank 2, both signed characteristic ideals have T-adic vanishing order at least 2, as noted above. Section 3 gives a p-unit coefficient at T² for one of the signed functions, so its ideal is **exactly** \((T^2)\).

B. D. Kim, *The plus/minus Selmer groups for supersingular primes*, J. Aust. Math. Soc. 95 (2013), **Theorem 1.1**, gives absence of nonzero finite Lambda-submodules for the dual signed Selmer under the theorem’s conditions. For F=Q, even the additional plus-sign local conditions are satisfied (p splits trivially over Q/Q and is totally ramified in Q∞/Q).

The following elementary signed-module lemma finishes the arithmetic deduction:

> If \(X\) is the genuine signed Selmer dual for a rank-r curve E/Q, has \(\operatorname{char}_\Lambda X=(T^r)\), and no nonzero finite Lambda-submodule, and the rank-r global MW divisible group embeds into \(Sel^\pm(Q∞)^\Gamma\) with the full ordinary Selmer embedding there, then \(\Sha(E/Q)[p^\infty]=0\).

Proof: The Lambda structure theorem embeds X with finite cokernel into \(\bigoplus_j\Lambda/(T^{e_j})\) with \(\sum e_j=r\), since the kernel is finite and must be zero. Thus X is Zp-free rank r. The action of T on X⊗Qp is nilpotent. Since the MW injection gives rank(X/TX)>=r, T=0 rationally and hence integrally. Therefore \(X/TX=\mathbf Z_p^r\), so its Pontryagin dual is \((Qp/Zp)^r\). The saturated divisible MW subgroup injects and exhausts this group; the ordinary Selmer lies between it and the signed-invariant group, so equals MW. By Kummer \(\Sha[p^\infty]=0\).

Applied with \(r=2,p=599\) and the nonzero signed coefficient 28, this yields the **computer-assisted conclusion**
\[
\boxed{\Sha(E389a1/\mathbf Q)[599^\infty]=0.}
\]
This conclusion does **not** rely on (i) an assumed finite Sha, (ii) the rank-two p-adic BSD leading-term conjecture, (iii) a full conductor-p³ modular-symbol enumeration, or (iv) a two-prime Kurihara coefficient at p599.

## 5. Scope and independent-verification boundary

Mathematically the deduction is exact under the authentic modular-symbol input and standard cited theorems. The source-normalization point previously labeled REVIEW_REQUIRED has been explicitly traced through Sage and Pollack here, including the mixed sign-label convention.

For proof auditing, the assistant has **not** rerun the user’s original Sage/eclib 179101 conductor-p² symbols, although it independently evaluated 179101 integer Manin-symbol representatives using a different JavaScript implementation, relying on a separately archived integer Manin vector. An independent audit that the archived 390 integer symbols are precisely the Néron-normalized eclib symbols (already verified at fixed rational cusps by prior user work) remains useful to guard against data corruption.

This establishes one additional p-primary Sha component, **not** finite support of Sha or its entire order, and **not** the exact complex BSD L''/2 formula. Only primes not covered by published ordinary-range results remain for the p<48859 portion, and infinitely many p>=48859 remain altogether.

### Primary sources

- Burungale–Skinner–Tian–Wan, arXiv:2409.01350v2, Thm1.3: https://arxiv.org/pdf/2409.01350
- B. D. Kim, *The plus/minus Selmer groups for supersingular primes*, Theorem1.1: https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/plusminus-selmer-groups-for-supersingular-primes/7AD9B7AB53A73F23F8E78F78488FA75C
- Pollack (2003), Theorem5.1, half-log product: https://math.bu.edu/people/rpollack/Papers/On_the_padic_Lfunction_of_a_modular_form_at_a_ss_prime.pdf
- SageMath source: https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/padic_lseries.py
