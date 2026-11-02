# A genuine two-auxiliary **Mordell–Weil localization determinant** for p = 5, 7, 107

**2026-11-02.** This is a new, **independent elliptic-curve arithmetic** bridge between the known rank-two MW points and the very auxiliary primes of the historically computed two-prime Kurihara witnesses. The finite-field computations below were **executed locally by the assistant using a pure-Python elliptic group law**, independently of Sage/eclib and of the Kurihara symbol computations; the new GitHub verification script **has NOT YET been user-run on Ubuntu**. Its outputs are not silently claimed as authentic user stdout.

**Mathematical conclusion:** Three exact 2×2 local determinant matrices have p-unit determinants. This is not p-uniform. Together with **separately authenticated nonzero rank-two Kurihara δ**, exact surjectivity/Manin/local hypotheses and Kim's mod-p theorem, this gives an explicit Selmer localization route to Sha[p]=0. **Without the separate δ witness and theorem, a unit local determinant alone is NOT a Sha certificate.**

## 1. The actual arithmetic object, not a modular-symbol weight

Use the minimal elliptic curve
\[
E:y^2+y=x^3+x^2-2x,\quad N=389,\quad
P=(-1,1),\ Q=(0,-1).
\]
The project separately certifies the MW rank-two **saturated basis** P,Q with trivial torsion; saturation is used only in the final Kummer/Selmer interpretation, **not** in the finite-field computations.

At a good prime \(q\ne p\) with \(p\mid\#E(\mathbf F_q)\) and \(p^2\nmid\#E(\mathbf F_q)\), there is exactly one p-primary cyclic factor of order p in \(E(\mathbf F_q)\). Write \(N_q=\#E(\mathbf F_q)=q+1-a_q\). Multiplication by \(N_q/p\) maps the p-primary component isomorphically to \(E(\mathbf F_q)[p]\), because \(p\nmid N_q/p\). It kills all prime-to-p primary factors, so it induces the reduction of \(E(\mathbf F_q)/pE(\mathbf F_q)\simeq E(\mathbf F_q)[p]\) **up to an invertible Fp-scalar**.

For each \(q\) select the nonzero element \(B_q=[N_q/p]\bar P\) as the local basis when available (all six cases below). Express
\[
[N_q/p]\bar P = a_q^{(P)} B_q,\qquad
[N_q/p]\bar Q = a_q^{(Q)} B_q
\]
with \(a_q^{(P)},a_q^{(Q)}\in\mathbf F_p\). For the ordered pair \((q_1,q_2)\), define the **local MW restriction matrix**
\[
R_p(P,Q;q_1,q_2)=
\begin{pmatrix}
a_{q_1}^{(P)}&a_{q_1}^{(Q)}\\
a_{q_2}^{(P)}&a_{q_2}^{(Q)}
\end{pmatrix}.
\]
The condition \(\det R_p\ne0\bmod p\) is independent of the chosen generator \(B_q\): changing basis multiplies one row by an element of Fp×.

The finite group law is implemented from the *actual* long Weierstrass equation. For points \((x_i,y_i)\), at distinct x-coordinates the chord slope is \(\lambda=(y_2-y_1)/(x_2-x_1)\), for doubling \(\lambda=(3x^2+2x-2)/(2y+1)\), and
\[
x_3=\lambda^2-x_1-x_2-1,\qquad
y_3=\lambda(x_1-x_3)-y_1-1.
\]
All operations occur exactly in \(\mathbf F_q\), and every finite-field output is checked to satisfy the original equation. For the point count the quadratic discriminant in y is \(D(x)=1+4(x^3+x^2-2x)\); hence \(a_q=-\sum_{x\in F_q}\left(\frac{D(x)}q\right)\). No floating point.

## 2. NEW genuine finite-field computations: six local rows, three unit determinants

| p | q | a_q | #E(F_q) | [#E(F_q)/p] | local row (P,Q) |
|---|---:|---:|---:|---:|---|
| 5 | 41 | −3 | 45 | 9 | (1,3) |
| 5 | 61 | −8 | 70 | 14 | (1,0) |
| 7 | 113 | 9 | 105 | 15 | (1,3) |
| 7 | 673 | 2 | 672 | 96 | (1,6) |
| 107 | 369793 | 2 | 369792 | 3456 | (1,15) |
| 107 | 383917 | −854 | 384772 | 3596 | (1,53) |

These q each satisfy \(q\equiv1\bmod p\), \(a_q\equiv q+1\bmod p\), and \(p\parallel \#E(\mathbf F_q)\). The computed full local matrices therefore are
\[
R_5=
\begin{pmatrix}1&3\\1&0\end{pmatrix},\quad
R_7=
\begin{pmatrix}1&3\\1&6\end{pmatrix},\quad
R_{107}=
\begin{pmatrix}1&15\\1&53\end{pmatrix},
\]
with EXACT determinant residues:
\[
\boxed{\det R_5=2\bmod5,\quad
\det R_7=3\bmod7,\quad
\det R_{107}=38\bmod107.}
\]
The inverses are respectively 3, 5 and 31. Thus in all three examples, the two known rational points span the complete 2-dimensional sum of the two one-dimensional **local** Kummer targets.

**Independent small local p-torsion gate:** exact point counts also give
\[
\#E(F_5)=9,\quad \#E(F_7)=13,\quad \#E(F_{107})=108,
\]
none divisible by its residue prime. Since E has good reduction at p=5,7,107 and its formal group over Qp has no p-torsion for odd p, these suffice to conclude \(E(Q_p)[p]=0\), as required in Kim's modp theorem.

The local arithmetic was executed in the assistant's current Python container, and its independent transcript is archived [here](../results/bsd389_MW_local_determinants_ASSISTANT_EXECUTED_2026-11-02.md). The new reproducible script for the user's **Sage or plain Python** environment is [here](../verification/bsd389_MW_two_auxiliary_local_determinants.py), published but not yet user-executed.

## 3. The precise, **conditional-on-Kurihara-certificate** Sha bridge (no circular finiteness assumption)

**Primary source:** Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves* (May 2025), **Theorem 1.10**, printed PDF p.8, [author/journal PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf). Under mod-p surjectivity, p-unit Manin constant, \(E(Q_p)[p]=0\), and p-unit Tamagawa factors, Kim proves that for a nonzero mod-p Kurihara number \(\widetilde\delta_n\) at the **minimal auxiliary cardinality** \(\nu(n)=\operatorname{ord}(\widetilde\delta^{(1)})\), the natural map
\[
\mathrm{Sel}(\mathbf Q,E[p])\xrightarrow{\ \simeq\ }
  \bigoplus_{q\mid n}E(\mathbf Q_q)\otimes\mathbf F_p
  \simeq\bigoplus_{q\mid n}E(\mathbf F_q)/p
\]
is an isomorphism.

For E389a1 with genuinely proved Mordell–Weil rank2, **IF a nonzero Kurihara witness exists with exactly two auxiliary primes**, then \(\operatorname{ord}(\widetilde\delta)=2\): the nonzero degree-two witness gives ≤2, while Kim's Theorem 1.8 (or lower-bound rank) gives ≥2 because rank MW=2. Thus the auxiliary-cardinality hypothesis of Kim's modp localization applies.

**For the same n**, our matrix \(\det R_p\ne0\) shows the image of MW/p is *already* the full 2-dimensional local target. By Kim's isomorphism, \(\mathrm{Sel}(E[p])\) has exactly dimension 2, and so the exact Kummer sequence
\[
0\to E(\mathbf Q)/pE(\mathbf Q)
 \to\mathrm{Sel}(\mathbf Q,E[p])\to\Sha(E/\mathbf Q)[p]\to0
\]
forces \(\Sha[p]=0\). Since any nonzero p-primary torsion group contains an element killed by p, it follows \(\Sha[p^\infty]=0\). **This does not assume Sha finiteness a priori.**

This is an explicit "two known points, two local primes" **Selmer/Sha argument** once the hypotheses and the *actual* Kurihara witness are certified. For the same pairs, historically reported Kurihara residues are:
- p5 q=(41,61), \(\delta=4\bmod5\) (**independently user-reproduced direct 2400-position mixed-jet computation**);
- p7 q=(113,673), \(\delta=2\bmod7\) (previous arithmetic archive; not recalculated here);
- p107 q=(369793,383917), \(\delta=34\bmod107\) (previous complete certificate archive with frozen SHA256 `b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754`; not recalculated here).

**Critical provenance warning:** The new local determinant verification code does **not** verify any Kurihara delta. For p107 it offers an **optional** explicit SHA256 match against the pre-existing external complete archive, which authenticates archive bytes, *not* the mathematical soundness or its algorithm. The script and this note do NOT introduce a fresh independently completed 71-billion-term p107 modular-symbol computation. The Kim/Sha conclusion is **conditional on accepting previously certified δ and the exact Kim theorem prerequisites**.

## 4. What this changes and what it does not

What is genuinely new here is **an additional arithmetic group-law witness**, parallel to the modular-symbol and Hecke calculations, that shows the MW wedge \(P\wedge Q\) **does not vanish under localization at the precise two-prime conductors already used**. These three unit determinants carry useful independent evidence about the arithmetic meaning of the rank-two Kurihara certificates.

It would be incorrect to infer a **p-uniform** statement from three sample primes or the existence of any primitive MW wedge: the Kolyvagin auxiliary primes \(q_i\) *depend on p*, and a hypothetical nonzero degree-two Kurihara functional depends on the actual Euler-system arithmetic as well. There is **no fixed determinant here** that bounds \(\Sha\) outside finitely many p. The conjectural uniform implication still needs to produce, for each good large p, an *arithmetically compatible* nonzero \(\widetilde\delta_{q_1q_2}\) or an independent integral \(\operatorname{Fitt}_2\) comparison. **Full BSD remains open** (uniform Sha finiteness + exact complex leading term).

**Sources:** [Kim Theorems 1.8 and 1.10](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf); [Castella–Sano 2026, Theorems A/B on unrestricted auxiliary degree](https://web.math.ucsb.edu/~castella/Kurihara.pdf); [uniform Sha research issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).
