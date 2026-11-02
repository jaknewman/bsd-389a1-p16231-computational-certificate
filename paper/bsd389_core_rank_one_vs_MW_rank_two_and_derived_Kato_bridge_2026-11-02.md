# E389a1: core rank one versus Mordell–Weil rank two — precise Kato derivative bridge

Date: 2026-11-02. New source-based mathematical obstruction to a naive application of rank-two Euler systems.

## 1. Core rank computation

For E/Q of conductor 389 and p>=5 with surjective residual representation, take T=T_p(E). The canonical Mazur–Rubin Selmer structure F_can has core Selmer rank

chi(T,F_can) = rank_{Z_p} T^- + corank_{Z_p} H^0(Q_p,T*) = 1.

Complex conjugation on T has (+1,-1) eigenspaces, each rank one; the local invariant term vanishes in the customary hypotheses. See the original Mazur–Rubin core-rank formula as reproduced in Büyükboduk's Kolyvagin-system paper:
https://preprints.ihes.fr/storage/tamagawa.pdf (Theorem 13 / Example 14).

For the self-dual Bloch–Kato finite Selmer conditions F_f, Poitou–Tate/Bloch–Kato dimension comparison yields **core difference zero** (not two):
dim_Qp H_f^1(Q,V) - dim_Qp H_f^1(Q,V*(1)) = 0
for V=V_p(E) (the two Selmer spaces are dual/self-dual via the Weil pairing; the local p de Rham contribution 1 is canceled by the real contribution 1). This does not say that dim H_f^1(Q,V) is zero; it is at least MW rank two, and could be larger if the p-primary Sha has positive corank. See Bellaïche's Bloch–Kato exposition:
https://people.brandeis.edu/~jbellaic/preprint/BKHawaii2.pdf (Theorem 2.2).
The notion of core rank depends on the Selmer structure and is **not** the Mordell–Weil rank.

## 2. Why this matters for a higher-rank Kolyvagin strategy

Mazur–Rubin, *Controlling Selmer groups in the higher core rank case*, J. Théor. Nombres Bordeaux 28 (2016), 145–183, doi:10.5802/jtnb.933:
https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.933/

Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II: the general theory*, accepted 2025:
https://kclpure.kcl.ac.uk/portal/en/publications/on-the-theory-of-higher-rank-euler-kolyvagin-and-stark-systems-ii/

A rank-r higher Kolyvagin derivative map applies to suitable rank-r Euler systems with matching Selmer/core-rank structure and all their precise hypotheses. It does **not** automatically convert the ordinary Kato Euler system (rank one in the standard framework) into a primitive rank-two system merely because E(Q) has rank two.

At rank two we should look at **higher derivatives of Kato's rank-one zeta element** and their regulators and refined reciprocity, NOT simply postulate a rank-two Euler system from P wedge Q.

## 3. A directly relevant published theorem

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024), 855–919, doi:10.2969/jmsj/90699069:
https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_article/-char/en

Their Generalized Perrin–Riou Conjecture concerns precise congruences between derivatives of Kato's zeta element and higher L-derivatives. They establish, under technical hypotheses, an unconditional **order-of-vanishing part in arbitrary rank**, and a higher-rank Rubin formula. The full leading-coefficient identity and p-unit primitivity needed for all-large-p Sha triviality are NOT claimed unconditionally by the abstract and must not be substituted from this partial result.

## 4. A mathematically testable exact next target

For an appropriate family of auxiliary squarefree conductors n=q1 q2 and p satisfying the hypotheses, write down the actual BKS derivative-of-zeta-element construction and its integral quotient (augmentation filtration and tensor coefficient module), then:

1. Determine whether the order >=2 follows unconditionally from the rank-two E(Q) and BKS hypotheses.
2. Identify the precise projected degree-two coefficient and compare its normalization to Kim's \\widetilde{\\delta}_n.
3. Show that this coefficient is a p-unit for at least one admissible two-prime n, for all sufficiently large p, *without* assuming finiteness of Sha. This third step is unproved and is equivalent to the desired Selmer/Fitting conclusion under Kim/Castella–Sano hypotheses.

### Status

Core rank distinction is established theoretically. No new global prime-uniform nonvanishing theorem is claimed. All actual user-executed certificates p2 and p5,7,11,13,107 remain valid and independent; the literature-derived p3 Heegner result retains its stated provenance.
