# 389a1 — the actual cyclotomic rank-two Kato derivative, its canonical Bockstein morphism, and the precise unproved comparison

**Date:** 2026-11-23. **Status:** audit of published theorems and a new elementary rank-two test lemma. This is not a proof of global Sha finiteness, nor of exact complex BSD. No numerical calculation was performed or requested.

## 1. The decisive archimedean rank mismatch

Let E/Q be 389a1 and p an odd prime. Put T=T_p(E). The Weil pairing identifies T^*(1) with T. Since complex conjugation c has determinant -1 on T and c²=1, its (+1) and (-1) eigenspaces each have rank one over Z_p. Thus
\[
Y_{\mathbf Q}(T)=H^0(\mathbf R,T^*(1))
\cong\mathbf Z_p
\]
has rank **one**, even though MW(E/Q) has rank **two**.

In Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems II*, Corollary 6.20(a), the parameter called r for the canonical Euler-system-to-Fitting construction is constrained by
\[
r=\operatorname{rank}_R\bigoplus_{v\mid\infty}H^0(K_v,T^*(1)).
\]
For our natural representation over Q this is **r=1**, not 2. Therefore **taking their abstract r=2 Kolyvagin-derivative map and feeding it Kato's usual rank-one Euler system does not construct a rank-two Selmer/Fitt2 comparison**. The Mordell–Weil rank must not be silently identified with the Euler-system core rank. This precise mismatch eliminates a tempting but invalid shortcut.

Source: BSS II, Corollary 6.20(a), https://nms.kcl.ac.uk/david.burns/web_page/bss.pdf .

## 2. The correct canonical rank-two object ALREADY EXISTS

The right object is not a fabricated exterior-square Kato Euler system. Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024), Proposition 4.4 and Definition 4.5, constructs a cyclotomic Darmon derivative.

Let \(\Gamma=\mathrm{Gal}(\mathbf Q_\infty/\mathbf Q)\simeq\mathbf Z_p\), \(\Lambda=\mathbf Z_p[[\Gamma]]\), \(\gamma\) a topological generator, and \(I=(\gamma-1)\) the augmentation ideal. Let \(\mathbf H^1=\varprojlim_n H^1(\mathbf Q_n,S,T)\), and let \(z_\infty\in\mathbf H^1\) denote the correctly normalized integral Kato zeta element (auxiliary factors c,d suppressed). For MW rank 2, Proposition 4.4 proves unconditionally **in this cyclotomic setting**
\[
z_\infty\in I\,\mathbf H^1 .
\]
Because \(\mathbf H^1\) is \(\Lambda\)-free of rank one under the source's hypotheses, there is a **unique** class \(w\in\mathbf H^1\) with
\[
z_\infty=(\gamma-1)w.
\]
The compatible finite-layer classes obtained by corestricting w give the first Kato–Darmon derivative
\[
\boxed{\kappa_\infty\in H^1(\mathbf Z_S,T_p(E))\otimes_{\mathbf Z_p} I/I^2.}
\]
The source explicitly notes that **no Generalized Perrin–Riou conjecture is needed for the existence of this class** (Introduction 1.3.1, Proposition 4.4).

This is a genuine existing cohomological object, rather than an unverified Kurihara distribution or a theta-only cokernel.

Primary source: https://kurihara.math.keio.ac.jp/bks4.pdf , introduction around pp. 858–860, Proposition 4.4, Definition 4.5.

## 3. The canonical Bockstein morphism ALREADY EXISTS; equality is conjectural

The same article constructs a canonical homomorphism
\[
\boxed{\mathrm{Boc}_\infty:
\bigwedge_{\mathbf Z_p}^{2}H^1(\mathbf Z_S,T_p(E))
 \longrightarrow H^1(\mathbf Z_S,T_p(E))\otimes_{\mathbf Z_p}I/I^2}
\]
after the paper's auxiliary basis choices/identifications and, if needed, extension of scalars as stated there. In the rank-two rational Mordell–Weil basis P,Q we can examine
\[
b_p:=\mathrm{Boc}_\infty(\kappa(P)\wedge\kappa(Q)).
\]
The *generalized Perrin–Riou leading-term conjecture* (BKS 2024, Conjecture 1.6, Proposition 4.14) states an identity of the form
\[
\boxed{\kappa_\infty
   =\frac{L_S^{(2)}(E,1)}{\Omega_\xi R_\infty}\,
     R_\omega^{\mathrm{Boc}}}
\]
with the source's exact S-truncated L-function, periods and Bockstein regulator conventions. It is **not a theorem in analytic rank two**. The coefficient is not automatically the untruncated BSD ratio: finitely many Euler factors, periods and auxiliary normalizations must be restored.

The paper's Theorem 1.14 explicitly assumes full Sha finiteness, analytic rank equality, an Iwasawa main conjecture, the generalized Perrin–Riou conjecture, and Bockstein nonvanishing to deduce a p-part of BSD. It is therefore **circular to cite Theorem 1.14 for global finiteness** without independently proving that assumption.

The canonical **morphism itself is not missing**. The hard unproved step is an exact, integral comparison between a genuine derivative class and the Bockstein regulator vector, with enough primitivity/control to read a second Fitting ideal.

## 4. A genuinely exact rank-two determinant test

This small lemma reduces any claimed equality between cohomological vectors to two checkable algebraic obligations.

**Lemma.** Let \(O=\mathbf Z_p\), \(M\) be free of rank two over O, \(W\) free of rank one, \(b\in M\otimes W\) *primitive* (not divisible by p), and \(k\in M\otimes W\) arbitrary. The following are equivalent:

(A) \(k=a b\) for some \(a\in O\);

(B) \(b\wedge k=0\in\bigwedge^2 M\otimes W^{\otimes2}\).

Moreover, if (B) holds then a is **unique and integral**, and for any O-linear functional \(\lambda:M\otimes W\to O\) with \(\lambda(b)\in O^\times\),
\[
\boxed{a=\lambda(k)/\lambda(b).}
\]

**Proof.** Choose bases of M and W. Since b is primitive, at least one coordinate is a p-adic unit; perform a matrix in GL₂(O) taking b to (1,0). Then b∧k=0 says the second coordinate of k is zero. The first coordinate is the unique a∈O. All statements, including the functional formula, follow by change of basis. QED.

If b is not primitive (e.g. p-adic regulator degenerate or divisible by p), **vanishing of the wedge only proves rational colinearity**: the coefficient may lie in Q_p and have a denominator. This distinction is precisely why a numerical congruence of Kato/Bockstein coordinates does not imply integral Fitt2 control.

## 5. 389a1 proof cut, with NO expendable computations

Already available: saturated rational generators P,Q; analytic rank exactly 2 (exact modular-symbol central zero + Arb positive L''/2); some individual p-primary Sha vanishing certificates. Unconditionally available from published BKS in the cyclotomic setting: the class \(\kappa_\infty\) and the Bockstein map.

What is **not available** and is essential:
1. establish the **integral lattice and primitivity** of the actual rank-two Bockstein class (or formulate the exact nonprimitive comparison and control its index);
2. prove **the arithmetic equality**, not merely a p-adic congruence, between genuine \(\kappa_\infty\) and the appropriately normalized Bockstein leading vector;
3. supply the genuine Selmer-complex local-condition comparison ensuring that a resulting scalar bounds \(\mathrm{Fitt}_{2,\mathbf Z_p}(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee)\);
4. make that control **uniform in p** (or produce one p-independent integer D with the rigorously verified all-prime inclusion), and independently recover the untruncated **complex** normalization.

This is a sharpened attack with a *pre-existing canonical morphism*, not a proof of its conjectural special-value identity. No new valuation-specific modular-symbol run is justified until one of (1)–(4) is obtained theoretically.

The two published frameworks must not be conflated: BSS's Euler-system rank-one input is forced by the archimedean representation; BKS's rank-two **Darmon derivative** handles the MW rank two using the first cyclotomic augmentation layer.

## References

- Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II*, Theorem 1.2, Corollary 6.20(a). https://nms.kcl.ac.uk/david.burns/web_page/bss.pdf
- Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan **76** (2024), Proposition 4.4, Definition 4.5, Conjecture 1.6, Proposition 4.14, Theorem 1.14. https://kurihara.math.keio.ac.jp/bks4.pdf
