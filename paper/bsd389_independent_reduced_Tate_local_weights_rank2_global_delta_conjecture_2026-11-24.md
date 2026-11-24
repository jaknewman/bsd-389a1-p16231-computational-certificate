# 389a1: a ZERO-FREE-PARAMETER rank-two Mazur–Tate/Kurihara congruence from *independent reduced Tate pairings*

**24 November 2026. Research status:** The local finite-field bilinear forms and their intrinsic basis-change/primitive-root laws are mathematically PROVED. An independent Python Miller algorithm produced exact local weights with no access to any two-prime Kurihara sums. Independently computed complete genuine 390-Manin Kurihara sums agree with the *a priori fixed scalar TWO* on **137 pairs at five distinct primes p=5,7,11,13,17**. The full quantified global congruence is **CONJECTURAL**; its proof would imply a substantive new all-large-p Sha-vanishing theorem, and cannot be inferred from finite tests. The exact complex BSD leading term is a separate obligation.

## 1. Canonical finite-field weight (no pair δ is used)

Let p≥5, q≠p,389 be a good rational prime satisfying
\[
q\equiv1\bmod p,\qquad a_q(E)\equiv 2\bmod p,\qquad
v_p(\#E(\mathbf F_q))=1.
\]
Then \(E(\mathbf F_q)/pE(\mathbf F_q)\) and \(E(\mathbf F_q)[p]\) are each 1-dimensional Fp spaces. Fix a generator \(e_q\) of the former, viewed as a point in E(Fq). Set \(N_q=\#E(\mathbf F_q)=p M_q\) with p∤M_q, and
\[
g_q=[M_q]e_q\in E(\mathbf F_q)[p]^\times.
\]
This depends only on the class of e modulo p; it is a generator of E(Fq)[p].

Let \(t_{p,q}\) denote the **reduced Tate pairing**
\[
t_{p,q}:E(\mathbf F_q)[p]\times E(\mathbf F_q)/pE(\mathbf F_q)
\longrightarrow\mu_p(\mathbf F_q),
\]
computed by a Miller function \(f_{p,g}\) of divisor \(p[g]-p[O]\), an auxiliary point R avoiding the divisor, and
\[
t_{p,q}(g,e)=
\left[\frac{f_{p,g}(e+R)}{f_{p,g}(R)}\right]^{(q-1)/p}\in\mu_p(\mathbf F_q).
\]
The reduced pairing is perfect on these 1-dimensional spaces. Hence \(t_{p,q}(g_q,e_q)\) is a **primitive pth root of unity**, and any discrete logarithm of it against a chosen primitive pth root is a p-unit.

Choose a primitive root \(\gamma_q\in\mathbf F_q^\times\) and set \(\zeta_q=\gamma_q^{(q-1)/p}\). Define the independent **Tate weight**
\[
\boxed{
w_{p,q}(e_q,\gamma_q):=
\log_{\zeta_q}\bigl(t_{p,q}([N_q/p]e_q,e_q)\bigr)
\in\mathbf F_p^\times.}
\tag{1}
\]
This weight requires ONLY finite-field point counts, group law, reduced Tate pairing and primitive-root convention; NO modular symbols, no global Kato class, no δ_{q_iq_j} data, and no Sha assumption.

**Proved normalization:** if the local generator is replaced by \(a e_q\) modp, then \(w_q\mapsto a^2 w_q\). Meanwhile the local MW row \(v_q=(\ell_q(P),\ell_q(Q))\) transforms as \(v_q\mapsto a^{-1}v_q\). Thus the product \(w_iw_j\det(v_i,v_j)^2\) is independent of the chosen local generators. If \(\gamma_q\mapsto\gamma_q^b\) for b∈Fp×, then \(w_q\mapsto b^{-1}w_q\), exactly as the local discrete-log factor in \(\delta_{q_iq_j}\) transforms. This makes the proposed global formula intrinsically normalized rather than dependent on an arbitrary fitted unit vector.

## 2. New fully explicit rank-two global reciprocity conjecture

For E=389a1 with its saturated rational generators P=(-1,1), Q=(0,-1), each good p and q_i satisfying §1, define the actual genuine Hecke/Manin-normalized two-factor Kurihara coefficient \(\tilde\delta_{q_iq_j}\in\mathbf F_p\) by the complete plus modular-symbol sum, with \(\log_{\gamma_{q_i}},\log_{\gamma_{q_j}}\) chosen in (1).

**Conjecture (independent local Tate regulator formula, ILTR):**
\[
\boxed{
\forall p\gg1,\quad\forall q_i\ne q_j
\text{ as above},\qquad
\tilde\delta_{q_iq_j}
=
2\,w_{p,q_i}w_{p,q_j}
\det(v_{q_i},v_{q_j})^2
\pmod p.
}
\tag{ILTR}
\]
One may also ask for this at every p≥5 satisfying the ordinary Kim/CS hypotheses; no global claim is assumed proved.

Define the independent rank-one local symmetric bilinear forms
\[
H_q=w_{p,q}v_q v_q^{\mathsf T}\in\operatorname{Sym}^2(\mathbf F_p^2).
\]
The exact Cauchy–Binet identity gives
\[
\det\left(\sum_q X_qH_q\right)
=\sum_{i<j}w_iw_j\det(v_i,v_j)^2X_iX_j.
\]
Thus (ILTR) is equivalent to asserting the genuine Kurihara mixed two-factor coefficients equal **twice the mixed coefficients of a regulator built entirely from local reduced Tate pairings**. Unlike the earlier quadratic-volume fit, (ILTR) contains **ZERO adjustable parameters**.

The factor TWO is the SAME for all five tested p. It has not been derived theoretically from the Néron-period and modular-symbol normalization, so **proving its exact normalisation is part of the missing arithmetic theorem**.

## 3. Fully independent finite arithmetic verification: 137 / 137

The local weights were independently computed with a dependency-free Python implementation of the elliptic curve group law and reduced Tate pairing via Miller's algorithm, evaluating \(f_{p,g}(e+R)/f_{p,g}(R)\). For representative q at p=5,7,11 we repeated evaluation over 31–35 independent auxiliary shifts R; the reduced value was unchanged. Bilinearity \(t(g,2e)=t(g,e)^2\) was separately checked.

The true Kurihara numbers came from a separate C++17 complete unit-residue enumerator using the authenticated 390-Manin edge vector, *not* from the local Python program.

### p=5: 15 q, 105 independent pairs

    q: 41 61 131 211 251 271 571 641 751 991 1031 1181 1321 1381 1811
    local Tate w: 3 1 1 2 3 3 2 2 2 4 4 1 3 4 3

All 105 independently known δ residues satisfy ILTR with coefficient **2**. The old finite-sample fitted factorization had C_fit=3 and u=(1,2,2,4,1,1,4,4,4,3,3,2,1,3,1). Independent Tate weights give u=2w mod5 and so C_fit*(2)^2=3*4=**2 mod5**.

In particular \(\delta_{41\cdot61}=4\), while the independent local Tate weights are w41=3, w61=1, local slopes s41=3, s61=0. The predicted value is \(2\cdot3\cdot1\cdot(0-3)^2=4\bmod5\).

### p=7: 5 q, 10 independent pairs

    q: 113 673 1429 2423 3389
    local Tate w: 1 4 4 3 4

These EXACTLY equal the formerly fitted units, and the old fitted global C=2 is unchanged. All 10 pair residues match the fixed ILTR formula.

### p=11: 6 q, 15 independent pairs

    q: 397 991 1321 3389 3433 4643
    local Tate w: 8 1 9 9 8 4

The former independently fitted u=(1,7,8,8,1,6) are related by u=7w mod11, and C_fit=7 gives C_fit*7²=**2 mod11**. All 15 complete Kurihara pair sums agree. There are 15 independent four-prime cross identities. For q397,991, slopes 10 and7, \(\delta=2\cdot8\cdot1\cdot(7-10)^2=1\bmod11\), independently matching the historical witness.

### p=13: 4 BRAND-NEW q, 6 held-out authentic pairs

    q:      131 911 1249 2237
    slopes:  2   8    7   10
    Tate w: 11   7   11   10

The SIX independent full Manin-symbol sums, compared directly to ILTR with no weight or scalar fitting:

    pair         predicted actual
    131,911        6        6
    131,1249       5        5
    131,2237       1        1
    911,1249      11       11
    911,2237       1        1
    1249,2237      4        4

The one QLVR quadruple also passes (normalized products 2,2,2).

### p=17: 2 BRAND-NEW q, one held-out authentic pair

    q:     1667 5237
    slopes: 6    12
    Tate w: 16   16

The independently predicted residue is \(2\cdot16\cdot16\cdot(12-6)^2\equiv4\bmod17\), and complete independent Manin enumeration gives **δ=4 mod17**.

**TOTAL:** 105+10+15+6+1=**137 genuine two-prime values** at p=5,7,11,13,17, with a globally fixed literal coefficient **2** and independently determined q-only local weights. No counterexample in this bounded test. These are finite congruences, **not a proof for unbounded p or q**.

## 4. Conditional theorem: ILTR would IMPLY a genuine all-large-p Sha result

**THEOREM (proved conditional implication).** Assume ILTR for all sufficiently large p in the above good/unipotent setting, and the published Kim Theorem 1.8, Castella–Sano Theorem B arithmetic hypotheses, all satisfied for the non-CM semistable E389a1 outside a finite set. Then
\[
\boxed{\Sha(E/\mathbf Q)[p^\infty]=0\quad\text{for all sufficiently large }p.}
\]

**Proof.** The independently proved Kummer–Chebotarev theorem for E389a1 supplies for each sufficiently large p two distinct good primes q1,q2 with Frobenius nonidentity unipotent modp and the localization vectors of P,Q forming a GL2(Fp) matrix. The local cyclic p-group condition and \(p\parallel\#E(\mathbf F_q)\) may additionally be imposed by prescribing suitable lifts modp² of those unipotent matrices, using the full \(\mathrm{GL}_2(\mathbf Z/p^2)\) image for p sufficiently large: choose a lift for which \(\det(1-\mathrm{Frob}_q)\) has p-valuation exactly1. Because the Kummer extension over the full division field has full E[p]² translation image, the two chosen local MW rows can still be prescribed independently. Chebotarev then supplies q1,q2 as required.

The reduced local Tate pairing on each rank-one E(Fq)[p]×E(Fq)/p is perfect, so the independently defined w_qi are p-units. The local determinant is a p-unit by construction, and p≥5 implies 2 a p-unit. ILTR therefore forces the true \(\tilde\delta_{q_1q_2}\not\equiv0\bmod p\). Kim's structural theorem with CS's theorem B then gives \(\Sha(E/\mathbf Q)[p^\infty]=0\). QED.

The conclusion is a true noncircular logical consequence of **the NEW explicit arithmetic congruence hypothesis**; but ILTR itself has NOT been proved, and should not be silently assumed from finite computations.

## 5. Precise missing arithmetic step, not an empty reformulation

Prove a rank-two **integral modular-symbol/derived-Kato-to-reduced-Tate-regulator reciprocity** establishing ILTR directly for all good admissible unipotent pairs, with no Sha finiteness hypothesis. The proven Poitou–Tate duality already explains the determinant SQUARED; the independently constructed local Tate pairings now supply all its LOCAL UNIT factors. The only remaining part of the identity is the GLOBAL coefficient and its normalization (2). This is a sharply specified arithmetic theorem involving two independently defined, explicitly computable sides—not an abstract existence condition or a coefficient fitted from δ.

There is a crucial risk: the Mazur–Tate *leading-term conjecture* in rank2 ordinarily involves the true Sha order, so a universal ILTR with coefficient2 independent of p would directly exclude Sha[p]≠0. Thus proving ILTR for all p is **in essence a strong new BSD-type theorem**, and it is not an immediate corollary of the one-sided Bullach–Honnor Fitting containment or of the Cauchy–Binet identity. This is why we do NOT claim a full BSD proof on the strength of 137 checks.

Even proving ILTR (and hence globally finite Sha with finitely many remaining small primes) does not give the separate exact complex leading coefficient \(L''(E,1)/2=\Omega_E\operatorname{Reg}_E\). This remains an independent obligation.

## 6. Reproducibility

- Assistant-executed, independently implemented local Python verifier: /mnt/data/bsd389_local_tate_weight_independent.py, exact output:
  - INDEPENDENT_REDUCED_TATE_WEIGHTS_PASS p 5 count 15 global scalar2;
  - same p7 count5 scalar2; p11 count6 scalar2;
  - LOCAL_TATE_WEIGHTS_26_OF_26_PASS.
- Archived independent C++17 authentic Kurihara enumerator in verification/bsd389_quadratic_volume_small_pairs.cpp, now covering p5,p7,p11; standalone complete enumerations at p13 and p17 were executed with the same authenticated 390 symbol vector and confirmed p13 (6/6) and p17 (1/1).
- Source benchmark p5 (41,61) δ4; p7 (113,673) δ2; p11 (397,991) δ1 are independently reproduced in the genuine C++ Manin arithmetic.
- Exact B-H theorem: https://arxiv.org/pdf/2511.07203 ; Kim theorem: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf ; Castella–Sano 2026: https://web.math.ucsb.edu/~castella/Kurihara.pdf .
