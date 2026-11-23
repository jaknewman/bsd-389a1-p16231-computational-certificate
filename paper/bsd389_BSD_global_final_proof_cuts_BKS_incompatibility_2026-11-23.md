# 389a1 — two explicit global BSD proof cuts and a definitive BKS applicability obstruction

**2026-11-23.** This note records an elementary but decisive distinction between finite-level progress and an all-prime BSD proof. Each lemma is mathematically proved; the arithmetic comparison they require is **not** supplied. No full BSD proof is claimed.

## A. The BKS 2021 finite abelian Mazur–Tate theorem does NOT apply to our Kurihara fields

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system and the Mazur–Tate conjecture*, arXiv:2103.11535v1, Theorem 1.1(b) requires the extension degree \([F:\mathbf Q]\) to be coprime to \(\#E(\mathbf F_q)\) for every prime q dividing the conductor \(m\) of the extension (among other hypotheses). Theorem 1.1(d) additionally assumes that BSD over Q is true, and (e) assumes their generalized Perrin–Riou conjecture for positive rank.

Our *p^k-deep Kurihara-admissible primes* q satisfy
\[
q\equiv1\bmod p^k,\qquad a_q(E)\equiv2\bmod p^k.
\]
It follows immediately that
\[
\#E(\mathbf F_q)=q+1-a_q(E)\equiv0\bmod p^k.
\]
For our cyclic fields \(F\) of degree \(p^k\), \(p^k\) therefore divides both \([F:\mathbf Q]\) and \(\#E(\mathbf F_q)\): BKS's condition (b) fails **maximally** at every ramified auxiliary q, not just marginally. And condition (d) already assumes the desired BSD-over-Q conclusion. Thus BKS Theorem 1.1 cannot be inserted as a missing unconditional rank-two exact formula in our present auxiliary field argument.

For our concrete p=5,k=2 conductor 5351×13001,
\[
\#E(\mathbf F_{5351})=5375=25\cdot215,
\quad\#E(\mathbf F_{13001})=13075=25\cdot523,
\quad[F:\mathbf Q]=25.
\]
Both local point counts have already been user-executed and certified. In fact the first is divisible by 125, making the obstruction still stronger.

This incompatibility does **not** disprove the Mazur–Tate leading-term conjecture; it proves only that the named BKS theorem cannot establish it for these fields.

Reference: https://arxiv.org/abs/2103.11535 ; author manuscript https://nms.kcl.ac.uk/david.burns/web_page/bks5.pdf, Theorem 1.1.

## B. All-prime arithmetic goal: a finite support integral Fitting criterion, with no squarefree requirement

For \(E=389a1\) with \(E(\mathbf Q)\simeq\mathbf Z^2\), put
\[
X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee,\qquad
Y_p=\Sha(E/\mathbf Q)[p^\infty]^\vee.
\]
The exact p-infinity Kummer sequence and splitting of the free Z_p quotient prove
\[
X_p\simeq\mathbf Z_p^2\oplus Y_p,\qquad
\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)=\operatorname{Fitt}_{0,\mathbf Z_p}(Y_p).
\]
When Y_p is finite of length e_p, the latter ideal is \(p^{e_p}\mathbf Z_p\); if Y_p has positive free rank, it is zero.

**Theorem (known-prime-support shortcut).** Let S be a finite set of primes for which \(\Sha(E/\mathbf Q)[p^\infty]=0\) has *already* been independently proved. Suppose one constructs an explicit **nonzero integer D, without assuming Sha finiteness**, together with proved comparison inclusions
\[
D\mathbf Z_p\subseteq\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)
\qquad\text{for ALL primes }p.
\]
If **every prime divisor of D lies in S**, then
\[
\boxed{\Sha(E/\mathbf Q)=0.}
\]

**Proof.** For p not dividing D, the nonzero D is a p-unit; the inclusion forces Fitt2(X_p)=Z_p and Y_p=0. For primes dividing D, p is in S, so Y_p=0 by prior certification. This proves zero at every p, with finite support and no circular use of Sha finiteness. QED.

**Improvement over a squarefree-D shortcut:** D does NOT need to be squarefree, and its valuations can be arbitrarily large, provided its *support* belongs to the already-certified set S. For example, conditional on trustworthy individual p-primary certifications at 2,3,5,7,11,13,107, any D with prime divisors among these alone would suffice if the real all-prime Fitting comparison were independently constructed. The p-primary claims for other primes must not be silently promoted from numerical probes.

This is a strictly *weaker numerical target on D* than requiring D squarefree; it is not a construction of D or its arithmetic comparison. A fixed primitive 390-vector or Hecke Smith minor by itself does **not** provide the needed comparison onto true Sha at every p.

## C. Exact complex leading coefficient: integrality alone plus one certified short interval would suffice

Put
\[
\mathcal A(E)=\frac{L''(E,1)}{2\Omega_E\operatorname{Reg}_E},
\]
with the *correct* Néron period, the full saturated rank-two height regulator and Tamagawa/torsion factors (the latter both equal one here). Its central L-value and first derivative vanish exactly, and an Arb enclosure of \(L''(E,1)/2\) was user-recorded:
\[
L''(E,1)/2 \in [0.7593165002884268\pm 7.81\cdot10^{-17}].
\]

**Elementary exact equality criterion.** If one independently proves:
1. \(\mathcal A(E)\in\mathbf Z\) (this is an arithmetic theorem-level input, NOT inferred from numeric BSD, p-adic congruences or assumed finite Sha);
2. a *rigorous enclosure* \(0.5<\mathcal A(E)<1.5\), using independent certified enclosures for BOTH the full Néron period and regulator as well as L''/2;

then \(\mathcal A(E)=1\) exactly.

**Proof:** the only integer in \((1/2,3/2)\) is 1. This is an alternative proof cut for the exact **complex** equality, not a proof of global Sha finiteness. Even the integrality of \(\mathcal A(E)\) independent of BSD is presently NOT established for this rank-two curve. The numerical Omega and regulator in the project are *not* yet independent ball enclosures, so this shortcut is NOT presently a certificate.

The proposed integrality route is potentially weaker in *form* than determining an exact real transcendental equality, but proving it noncircularly is a major arithmetic task. The BKS positive-rank theorem cannot be invoked here because its hypothesis (d) assumes BSD over Q.

## D. Strict focus decision

The p^2 two-prime Kurihara witness criterion is a useful **sufficient** primewise Sha-vanishing test. Chebotarev already guarantees infinitely many admissible pairs but cannot guarantee the required weighted *global* Kurihara coefficient is nonzero. The all-large-p existence of witnesses remains an unproved rank-two arithmetic nonvanishing assertion; treating it as automatic would just repackage the original difficulty.

Two genuinely sufficient *noncircular* final outcomes would be:
- construct one D supported on the **already certified** primes with its true all-prime Selmer Fitt2 comparison; and separately prove \(\mathcal A(E)=1\) via a rank-two integral/archimedean comparison, or
- prove \(\Sha(E/\mathbf Q)=0\) uniformly by a different global Euler-system argument, and separately the exact complex leading-term equality.

Neither a finite number of p-specific auxiliary curves nor their relative BSD ratios controls the unknown base \(\mathcal A(E)\): Artin factorization cancels that base factor out of every relative ratio \(\mathcal A(E/K)/\mathcal A(E/\mathbf Q)\).

This note is a research proof-cut and source audit; it does not claim the missing integral all-prime comparison or complex regulator identity has been constructed.
