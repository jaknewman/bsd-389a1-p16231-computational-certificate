# E389a1, p=16231: the no-finite-submodule gate is CLOSED by Pollack–Weston (2011), not by the D_K>4-restricted 2026 theorem

Date 2026-11-06. This is an application and exact algebraic deduction from **published primary sources** plus the already archived exact anticyclotomic theta-order-two and CH control certificates. It does not assert that a residual T-action has been constructed or that BSD is proved. No prior computation has been rerun.

## 1. The actual arithmetic Selmer module

Let \(E/\mathbf Q=389a1\), \(p=16231\), \(K=\mathbf Q(\sqrt{-3})\) and \(K_\infty/K\) its anticyclotomic Zp-extension. Let \(\Lambda=\mathbf Z_p[[T]]\), and let \(S_\Delta=\operatorname{Sel}_{N^-=389}(K_\infty,E[p^\infty])\) be the **N-minus-ordinary Selmer** group of Chida–Hsieh, and \(X_\Delta=S_\Delta^\vee\).

Previously certified, without rerun here:
- \(N=389=N^-\), **\(N^+=1\)**; 389 is inert in K; p is split; \((p,3\cdot389)=1\).
- E is semistable, \(a_p=128\), p ordinary, \(a_p^2\not\equiv1\bmod p\); \(\bar\rho_{E,p}\) surjective and ramified at 389.
- A correct theta-identification plus the full authentic Gross orbit proves the exact power-series order \(\Theta(T)=T^2u(T)\) with \(u(0)\in\mathbf Z_p^\times\).
- The CH one-sided main-conjecture theorem supplies \((\Theta\Theta^\iota)\subseteq\operatorname{char}_\Lambda(X_\Delta)\), so \(X_\Delta\) is \(\Lambda\)-torsion with \((T^4)\subseteq\operatorname{char}_\Lambda(X_\Delta)\).

The last theta identification is **computer-assisted and dependent on the archived source-identification hypotheses**, not a newly executed or independently peer-reviewed computation.

## 2. Pollack–Weston's exact comparison is sufficient at Nplus=1

Pollack and Weston, *On anticyclotomic μ-invariants of modular forms*, Compositio Math. **147 (2011)**, pp.1361–1364, define two Selmer structures:

* \(S_{\min}\): **strict/trivial local condition at all places away from p**, ordinary at p.
* \(S_{\Delta}\): the corresponding residual N-minus-ordinary local condition at places above \(N^-\), and strict at places above \(N^+\) (none for us).

Their Proposition 3.6 and its proof (printed p.1363–1364) gives, under their CR and ordinary hypotheses, the comparison
\[
0\longrightarrow S_\Delta(E[p^n])\longrightarrow
S_{\min}(E[p^\infty])[p^n]\longrightarrow
\prod_{\ell\mid N^+}\prod_{w\mid\ell}A^{G_{K_{\infty,w}}}/p^nA^{G_{K_{\infty,w}}}.
\]
**For E=389a1, Nplus=1, so this product is EMPTY and therefore the last arrow has zero target, for every n.** Taking the direct limit yields the **exact isomorphism**
\[
\boxed{\ S_\Delta=S_{\min}\ }\tag{1}
\]
as discrete \(\Lambda\)-modules.

The hypotheses CR hold: p>=5 ordinary, the residual representation is GL2-surjective, and the only inert N-minus prime 389 is ramified modp (in fact 389 is not ±1 modp, so that part of the stated CR definition is vacuous). K's discriminant -3 is coprime to pN, as required in the **original Pollack–Weston 2011 field setup**; unlike Kim's later 2026 initial-Fitting theorem, **the 2011 article has no restriction \(D_K>4\)**. The six global roots of unity in K have order prime to p.

## 3. The anticyclotomic no-finite theorem and its exact use

Greenberg's Proposition 4.14, *Iwasawa theory for elliptic curves* (LNM 1716, 1999), proves: if the relevant Selmer group over a cyclotomic Zp-extension is \(\Lambda\)-cotorsion and E(F)[p]=0, then it has **no proper finite-index \(\Lambda\)-submodule**. Pollack–Weston (2011), **in the proof of Proposition 3.6, explicitly state that this theorem generalizes to the anticyclotomic case they are treating**. Kim's 2026 Proposition 3.2 repeats the extension.

To apply: \(E(K)[p]=0\) because the image of \(G_K\) under the residual surjective \(\bar\rho_{E,p}\) is normal of index at most two in GL2(Fp), contains SL2(Fp) for p>=5, and hence has no fixed nonzero vector. The module \(S_{\min}=S_\Delta\) is \(\Lambda\)-cotorsion by the CH one-sided theta characteristic inclusion. Therefore the published anticyclotomic Greenberg–Pollack–Weston result gives **NO proper \(\Lambda\)-submodule of finite index in \(S_\Delta\)**.

Pontryagin duality exchanges a finite-index submodule of the discrete Selmer group with a nonzero **finite \(\Lambda\)-submodule** of \(X_\Delta\). Thus
\[
\boxed{H^0_{(p,T)}(X_\Delta)=0.}\tag{2}
\]
This closes the previously separated F=0 gate WITHOUT invoking Kim's D_K>4-restricted 2026 *Fitt0* theorem as a theorem for K=-3.

**Primary source locations:** Pollack–Weston 2011, PDF introduction p.1353 (field requirements), §3.1–3.2, Proposition 3.6 and its **proof** p.1363–1364 (“[Gre99, Proposition 4.14] ... generalizes to the case we are considering”). Greenberg 1999, Proposition 4.14, pp.103–104. Kim 2026 Proposition 3.2, p.24 restates extension.

## 4. Consequence: a genuine finite-rank nilpotent arithmetic module

The preceding algebraic theorem in this branch already proved that any finitely generated torsion \(\Lambda\)-module with characteristic ideal dividing \((T^4)\) becomes \(\mathbf Z_p\)-free rank \(a\le4\) and nilpotent \(T^a=0\) after quotienting its maximum finite \(\Lambda\)-submodule. By (2), **there is no such finite submodule here**. Hence
\[
\boxed{X_\Delta\cong\mathbf Z_p^a,\qquad 2\le a\le4,\qquad T^aX_\Delta=0.}\tag{3}
\]
The lower bound 2 follows from the exact base-field control giving two free MW directions in \(X_\Delta/TX_\Delta\).

Here \(T_X\) is the actual action of a chosen topological generator of \(\Gamma=\operatorname{Gal}(K_\infty/K)\) minus 1 on the arithmetic Selmer dual. The module is described by a **single integral nilpotent a×a matrix**, but its entries are NOT supplied by the theta polynomial or the characteristic ideal.

Let \(\bar T_X\) be its reduction on \(X_\Delta/pX_\Delta\). Exact control at \(T=0\), Kummer, quadratic plus/minus splitting, Dokchitser p-parity and Cassels–Tate show
\[
\mu_\Lambda(X_\Delta)
=a-\operatorname{rank}_{\mathbf F_p}(\bar T_X)
=2+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
+\dim_{\mathbf F_p}\Sha(E^{(-3)}/\mathbf Q)[p]
\in\{2,4,6,\ldots\}.
\]
Since \(a\le4\), only \(\mu=2\) or 4 remain.

**Exact conditional single-action criterion:**
\[
\boxed{
\bar T_X\ne0\quad\Longrightarrow\quad
\Sha(E/\mathbf Q)[16231^\infty]
=\Sha(E^{(-3)}/\mathbf Q)[16231^\infty]=0.}\tag{4}
\]
If \(a\le3\), the same conclusion follows with no T-action measurement. If \(a=4\), \(\bar T_X\) is forced to have either rank 0 (possible p-torsion) or rank 2 (no p-torsion); rank 1 is excluded by parity.

**Crucial nonclaim:** Theorem (4) is a **sufficient** condition that has not yet been proved for the actual arithmetic \(X_\Delta\). The source-verified theta order and one-sided main conjecture **do not force \(\bar T_X\ne0\)**. Abstract modules \(\coker\operatorname{diag}(B_e,B_e)\) with \(B_e=\bigl(\begin{smallmatrix}p^e&T\\T&0\end{smallmatrix}\bigr)\) have exactly the same characteristic ideal \((T^4)\), no finite \(\Lambda\)-submodules, and \(\bar T=0\), with augmentation p-torsion \((\mathbf Z/p^e)^2\) for arbitrary e. They are not actual Selmer modules and do not contradict any actual arithmetic theorem.

## 5. Research boundary: local result versus complete BSD

Proved here: actual applicability of anticyclotomic no-finite-submodule source at K=-3 with N+=1, removing one genuine technical obstacle without new numerical runs; X_\Delta becomes a true 2–4-dimensional free Zp-module with nilpotent T.

NOT proved: one nonzero residual T-action (or rank a<=3), any new independent **unconditional** Sha[p] vanishing, uniform exclusion of every rational p (including inert and bad p), and the exact complex rank-two leading coefficient formula. The archived p=16231 cyclotomic Kato proof remains separately computer-assisted conditional on its authentic frozen inputs. Even a full p16231 proof would not imply full BSD globally.

## Sources

- R. Pollack and T. Weston (2011), *On anticyclotomic μ-invariants of modular forms*, Compositio Math. 147, 1353–1381, Proposition 3.6 and its proof: https://doi.org/10.1112/S0010437X11005318
- R. Greenberg (1999), *Iwasawa theory for elliptic curves*, Proposition 4.14; original text: https://cjhb.site/Files.php/books/Differential%20Geometry/04_Curves_and_Surfaces/Arithmetic%20Theory%20of%20Elliptic%20Curves%20-%20J.%20Coates.pdf
- C.-H. Kim (2026), *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Proposition 3.2: https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-the-fitting-ideals-of-anticyclotomic-selmer-groups-of-elliptic-curves-with-good-ordinary-reduction/D7D2EA9FA52A23B92319F3D44F5E9884
- Chida–Hsieh (2015), one-sided main conjecture, \`paper/bsd389_p16231_nipotent_length4_one_nonzero_T_finiteness_gate_2026-11-06.md\`.
