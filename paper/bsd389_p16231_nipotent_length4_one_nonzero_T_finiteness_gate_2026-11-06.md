> **UPDATE (2026-11-06): no-finite-submodule condition NOW PROVED for the arithmetic X_delta, under the accepted CH/Theta archive hypotheses.** Pollack–Weston (Compositio 2011, Proposition 3.6 **proof**) explicitly extends Greenberg 1999 Proposition 4.14 to their anticyclotomic setting, and for E389a1 we have **Nplus=1**, so their finite-level comparison error product is empty. Their original field assumptions permit K=Q(sqrt(-3)). Since E(K)[p]=0, residual GL2-surjective, and CH theta divisibility makes X_delta torsion, their no-finite theorem gives F=0. Thus the free Zp-rank ≤4/nilpotent T description in this document applies to the ACTUAL arithmetic X_delta at p16231. **The residual T mod p nonvanishing required for Sha=0 is still NOT proved.** [Full argument and original source text](bsd389_p16231_Pollack_Weston_Greenberg_no_finite_exact_Kminus3_Nplus1_2026-11-06.md).

# 389a1, p=16231: a length-four nilpotent Iwasawa reduction and a one-entry mod-p criterion

2026-11-06 — **New exact algebraic theorem conditional only on the accepted theta-order-two/Chida–Hsieh divisibility inputs, with an explicit separate no-finite-submodule gate.** NO earlier high-cost Gross, Sage, modular-symbol, Kurihara or cyclotomic certificate has been reexecuted. This does not prove Sha vanishing or full BSD.

## Arithmetic inputs

Let \(p=16231\), \(K=\mathbf Q(\sqrt{-3})\),
\(\Lambda=\mathbf Z_p[[T]]\), \(\mathfrak m=(p,T)\), and
\[
X=\operatorname{Sel}_{N^-=389}(K_\infty,E[p^\infty])^\vee
\]
with the exact Chida–Hsieh **Delta-ordinary** Selmer conditions and integral base control already documented separately in the PR.

The accepted previous full finite Gross theta calculation, the exact finite-to-infinite comparison, and trivial-character/involution arguments give
\[
\Theta(T)=T^2u(T),\quad u(T)\in\Lambda^\times,
\]
where the coefficient of \(T^2\) is a unit (normalized residue 3739). This equality, not a mere nonzero approximation, is the input.

Chida–Hsieh's one-sided anticyclotomic main conjecture (Compositio Math. 151 (2015), Theorem 1), under (CR+) and (PO), states
\[
(\Theta\cdot\Theta^\iota)\subseteq\operatorname{char}_\Lambda(X).
\]
For our theta, \(\Theta\cdot\Theta^\iota=T^4 \times\mathrm{unit}\); since \(\iota(T)=-T/(1+T)\) is a unit multiple of T,
\[
\boxed{(T^4)\subseteq\operatorname{char}_\Lambda(X).}\tag{A}
\]
The theorem's residual, ordinary and local hypotheses hold for the accepted p data: \(a_p=128\), \(128^2-1\equiv152\ne0\bmod p\), \(p\nmid 3\cdot389\), \(N^-=389\) is a single inert prime, residual GL2 surjectivity and conductor valuation one. The original CH argument had a subsequently repaired freeness issue for non-minimal residual modular forms, but here \(N^+=1\), so the residual-minimality condition away from \(N^-\) is vacuous; see Kim–Pollack–Weston, *On the freeness of anticyclotomic Selmer groups* (2016), Theorem 1.5 and discussion.

## Theorem 1 — UNCONDITIONAL algebraic reduction modulo the maximal finite submodule

Let \(R=\mathbf Z_p[[T]]\), and M any finitely generated torsion R-module whose characteristic ideal contains \((T^4)\).

Let \(F=H^0_{\mathfrak m}(M)\) be its maximal **finite-length R-submodule**. Then:

1. There exists a unique integer \(0\le a\le4\) such that \(\operatorname{char}_R(M)=(T^a)\).
2. \(\boxed{T^a(M/F)=0}\).
3. \(\boxed{M/F\simeq\mathbf Z_p^a}\) as a \(\mathbf Z_p\)-module. In particular, \(M/F\) is completely specified by a single nilpotent \(\mathbf Z_p\)-linear matrix of size \(a\le4\).

**Proof.** The ring R is a 2-dimensional regular local UFD. The height-one support of M is contained in V(T) because its characteristic generator divides \(T^4\), so the characteristic divisor is exactly \(T^a\), \(a\le4\). At the height-one prime (T), R_(T) is a DVR and M_(T) has length a. Its elementary divisors are R_(T)/(T^{e_i}) with sum e_i=a, hence \(T^aM_{(T)}=0\). At every other height-one prime, M localizes to zero. Therefore \(T^aM\) is supported at the maximal ideal \(\mathfrak m\), and is finite length, hence lies in F. Thus \(T^a(M/F)=0\). This makes \(M/F\) finitely generated over \(R/(T^a)\), which is finite free of rank a over \(\mathbf Z_p\). If \(M/F\) had nonzero p-power torsion, its p-power torsion subgroup would be a finite nonzero R-submodule; the preimage of that subgroup in M would be a finite R-submodule strictly containing F, contradiction. Thus M/F is \(\mathbf Z_p\)-torsion-free and finite, hence free of rank r. Localizing at (T) inverts p and preserves the rank as the Qp-dimension of M/F, so r=length_R_(T) M_(T)=a. QED.

This theorem requires **no assumption F=0**. It identifies exactly the finite codimension-two error that may prevent the desired direct 4×4 matrix model.

## Theorem 2 — exact ONE-NONZERO-ENTRY test if the finite error vanishes

Assume additionally \(F=0\) for our arithmetic M=X, i.e., X has no finite nonzero \(\Lambda\)-submodule. (The standard Greenberg–Viola / Kim no-finite-submodule criterion is a possible input; **its extension to the specific \(-3\) field must be justified rather than silently invoking Kim's field-restricted 2026 article**.)

Then X is \(\mathbf Z_p^a\) with a nilpotent action \(T_X\), a≤4. Nakayama's lemma gives
\[
\mu_\Lambda(X)
=\dim_{\mathbf F_p}X/(p,T)X
=a-\operatorname{rank}_{\mathbf F_p}(\overline{T_X}).
\]

Independently, the already proved exact CH Selmer control at the base K, Kummer, quadratic decomposition, Dokchitser p-parity and Cassels–Tate imply
\[
\mu_\Lambda(X)
=2+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
+\dim_{\mathbf F_p}\Sha(E^{-3}/\mathbf Q)[p]
\in\{2,4,6,\ldots\}.
\]
As \(a\le4\), only \(\mu=2\) or 4 can occur.

**Theorem 2.** Under the above arithmetic inputs and \(F=0\):
\[
\boxed{
T_X(X)\not\subset pX
\quad\Longrightarrow\quad
\Sha(E/\mathbf Q)[p^\infty]
=\Sha(E^{-3}/\mathbf Q)[p^\infty]=0.
}\tag{B}
\]

**Proof.** The condition means the action of T on \(X/pX\) is nonzero, hence
\(\operatorname{rank}_{\mathbf F_p}\bar T\ge1\). Therefore
\(\mu_\Lambda(X)=a-\operatorname{rank}\bar T\le4-1=3\).
The proven evenness and lower bound 2 force \(\mu=2\). Nakayama plus control/Kummer imply both Sha[p] groups vanish, hence their p-primary parts vanish. QED.

**Additional corollary.** If \(a\le3\), both p-primary Sha parts vanish automatically under \(F=0\). If \(a=4\), then
\[
\boxed{\overline{T_X}\ne0
\iff\operatorname{rank}_{\mathbf F_p}\bar T=2
\iff\mu_\Lambda(X)=2
\iff\text{both Sha p-primary parts vanish},}
\]
whereas \(\overline{T_X}=0\iff\mu=4\) and the total Sha[p] dimension is exactly 2.

Thus, **if the no-finite-submodule theorem applies**, the target for p=16231 has been reduced from a unit Fitt2 minor to a *single demonstrably nonzero residual anticyclotomic Galois action on the genuine Selmer dual*. The latter has NOT yet been exhibited arithmetically, and proving it is mathematically equivalent to the Sha conclusion **in this reduction**. The existing theta unit does NOT imply it.

## Theorem 3 — exact impossibility of inferring that action from all existing characteristic data

For every integer e≥1, set
\[
B_e(T)=\begin{pmatrix}p^e&T\\T&0\end{pmatrix},\qquad
A_e=\operatorname{diag}(B_e,B_e),\quad
M_e=\operatorname{coker}_\Lambda A_e.
\]
Then
\[
\operatorname{Fitt}_{0,\Lambda}(M_e)=(T^4),\quad
\operatorname{char}_\Lambda(M_e)=(T^4),
\]
M_e is free of rank four over Zp and has **NO finite Lambda-submodule**, and \(\overline T=0\) on M_e/pM_e, while
\[
\boxed{
M_e/TM_e\simeq
 \mathbf Z_p^2\oplus
 (\mathbf Z/p^e)^2.
}
\]
The finite augmentation defect has order \(p^{2e}\), an **arbitrarily large perfect square**.

**Proof.** Each block has relations \(Tu=0\) and \(Tv=-p^e u\) on a Zp-basis u,v, so its Zp-module is free of rank two; T acts by the matrix with the single entry \(-p^e\), zero modulo p. Determinant of B_e is \(-T^2\), and specializing T=0 yields one free and one p^e-torsion factor per block. Two blocks give the assertions. No finite Lambda-submodule is possible in a Zp-free module. QED.

This model proves that even the **full exact one-sided characteristic ideal plus no finite Lambda submodule, a unit quadratic theta, parity, and exact augmentation control**, in the absence of a genuine residual Iwasawa action, cannot place ANY upper bound on the order of finite Sha. It is an ABSTRACT module, not the Selmer of an elliptic curve.

## What is genuinely NEW and what remains

Proved exactly in this note:
- The unconditional mod-maximal-finite-submodule rank≤4/free/nilpotent reduction (Theorem 1), once the accepted CH+theta characteristic-divisibility is applied to X.
- The single-nonzero-entry sufficiency, conditional on a justified no-finite-submodule theorem (Theorem 2), with full parity-based proof.
- Parametric counterexample e≥1 showing arbitrary hidden square-order defects consistent with every initial characteristic statement (Theorem 3).

Still not proved:
- A complete **no finite Lambda submodule** theorem for this exact Delta-ordinary module at K=-3, if not validated by applicable Greenberg–Viola methods.
- The nonzero residual T-action on the **actual arithmetic X**, not an artificial matrix.
- A uniform p-independent integral Selmer/Sha support bound, and the exact archimedean BSD leading coefficient.

**Do not call these conditional reductions a proof of Sha[16231∞]=0 or complete BSD.**

## Primary sources
- Chida–Hsieh, *On the anticyclotomic Iwasawa main conjecture for modular forms*, Theorem 1 and Proposition 1.9, Compositio Math. 151 (2015), https://www.asahi-net.or.jp/~qa4m-cd/AIMC.pdf.
- Kim–Pollack–Weston, *On the freeness of anticyclotomic Selmer groups* (2016), correction of an Euler-system freeness gap in PW/CH, https://rpollack9974.github.io/web/Papers/freeness.pdf.
- Chan-Ho Kim, *On the Fitting ideals of anticyclotomic Selmer groups*, Canadian Math. Bulletin 69 (2026), Proposition 3.2, https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-the-fitting-ideals-of-anticyclotomic-selmer-groups-of-elliptic-curves-with-good-ordinary-reduction/D7D2EA9FA52A23B92319F3D44F5E9884 .
- Dokchitser–Dokchitser, p-parity theorem; Cassels–Tate alternating pairing, cited in the previous PR note about even Selmer generator gaps.
- Preceding proven control and theta papers in this research branch.
