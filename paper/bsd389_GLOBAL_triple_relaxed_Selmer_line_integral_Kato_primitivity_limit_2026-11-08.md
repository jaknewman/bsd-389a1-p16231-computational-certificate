# BSD 389a1 — A sharp Poitou–Tate relaxed-Selmer line and the limits of Kato primitivity (8 Nov 2026)

**2026-11-09 correction (primary-source audit).** Castella–Sano 2026, Theorem 2.1.3, proves the *integral unit* reciprocity relation `exp^*(res_p κ_n^Kato)=u_n · p^{t_p} · δ_n` with `u_n ∈ (Z_p/I_n)^×` and `p^{t_p}=#E(Q_p)[p∞]`. For the nonanomalous test primes 5,7,11,13,17 of E389a1, `t_p=0`. The comparison unit is **not** the missing theorem; the missing uniform assertion is the existence of a genuinely nonzero *two-prime* derived Kato/Kurihara specialization. Source: https://arxiv.org/pdf/2601.14504, Theorem 2.1.3.

**Mathematical status:** precise unconditional global Selmer consequence from Poitou–Tate for each prime satisfying the stated local hypotheses; exact new p=5/p=7 arithmetic calculations performed in Python. **Not** a proof of uniform Sha vanishing or the complex rank-two BSD leading coefficient.

## Sources and no-circularity audit

Chan-Ho Kim, *The refined Tamagawa number conjectures for GL₂*, arXiv:2505.09121, §4 (especially Remark 4.1, formula preceding Proposition 4.2), proves an explicit reciprocity formula in which the singular localization of the Kato-derived class maps under the dual exponential to a Kurihara number times a nonzero conductor-independent scalar involving local Euler and period constants. Castella–Sano Theorem 2.1.3 proves that the residual comparison scalar is a **unit**, up to the explicit factor `#E(Q_p)[p∞]`. At the test primes 5,7,11,13,17 this local torsion factor is one. This still does **not** turn a generic Kummer-local determinant into a two-prime unit Kurihara witness.

Castella–Sano, arXiv:2601.14504, Theorem B gives at least one **some-length** nonzero mod-p Kurihara number for every good p>=5 in the prime-conductor case under the stated hypotheses. It does NOT give a two-factor unit witness.

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), Theorem 1.3 **assumes** finiteness of Sha(E/F)[p∞]. It cannot be invoked as an independent proof of finiteness of Sha(E/Q)[p∞] in rank two. The full higher derivative leading-term comparison remains conjectural in their article.

## Exact new triple-relaxed Selmer theorem

Let V=E[p] for E: y²+y=x³+x²−2x, with saturated E(Q)=ZP⊕ZQ, P=(-1,1), Q=(0,-1). Fix p>=5 of good reduction with

(A) E(Q_p)[p]=0, so H¹_f(Q_p,V) has dimension 1 over F_p;
(B) two good auxiliary primes q1,q2 with Frobenius nonidentity-unipotent on E[p], so H¹_f(Q_qi,V) has dimension 1;
(C) the 2×2 localization matrix B of P,Q at q1,q2 is invertible;
(D) the local Kummer vector at p of P,Q is nonzero.

These hypotheses are verified directly at p=5, q=(41,61), and p=7, q=(113,673).

Put S=Sel_p(E/Q), and S^R the Selmer group with **full** local cohomology (relaxed) at R={p,q1,q2}, standard Kummer conditions elsewhere. Let D_R=⊕_{v in R} H¹(Q_v,V)/H¹_f(Q_v,V), a 3-dimensional Fp vector space, with local dual coordinates.

Poitou–Tate for the self-dual finite Galois module V gives an exact sequence

   0→S→S^R→D_R→S^∨→(S_R^strict)^∨→0,

where the third arrow is dual to the localization S→⊕_{v∈R}H¹_f(Q_v,V). Because Sha[p] is everywhere locally trivial, all its elements map to 0, whereas the MW basis maps at q1,q2 to the invertible B. Thus the image of S in the 3 local finite conditions has rank **exactly 2**, independently of dim Sha[p].

Consequently **there is an exact one-dimensional global quotient**

   **dim_Fp(S^R/S)=3−2=1.**

Furthermore, S_R^strict is isomorphic to Sha(E/Q)[p] (the q-local MW matrix is injective, while Sha is locally zero). The singular localization of S^R/S is exactly the one-dimensional annihilator of the 2-dimensional localization image of the MW basis.

Let
   A = ((ell_p(P),ell_p(Q)), (lambda_q1(P),lambda_q1(Q)), (lambda_q2(P),lambda_q2(Q)))
be the 3×2 local MW matrix, with the p and q local spaces identified with Fp using any compatible bases. Then the singular tuple (t,y1,y2) of every c∈S^R satisfies

   A^T·(t,y1,y2)^T=0.

Since B is invertible, setting t=1 gives its **unique** normalized nonzero vector

   (t,y1,y2)=(1,−(B^T)^−1·ell_p),

where ell_p=(ell_p(P),ell_p(Q)). Because ell_p is nonzero, the auxiliary components are not both zero.

The sequence and normalization show that a global relaxed cohomology class with **p-singular coordinate 1** ALWAYS EXISTS under (A)-(C), even if Sha[p] is nonzero. Hence existence of a p-singular primitive *generic cohomology class* is NOT a Sha-vanishing criterion. The missing claim must concern the special derived Kato **Euler/Kolyvagin system**, with its norm relations, nonzero index and integral comparison; it cannot be replaced by the general Poitou–Tate existence result.

## Exact p=5 and p=7 realizations

Previously certified Kummer q-local matrices and independently computed p-local formal logarithms yield:

p=5, (q1,q2)=(41,61):
  A=[[2,4],[1,3],[1,0]] (mod 5);
  annihilator line <(1,2,1)> ⊂ F_5³.

p=7, (q1,q2)=(113,673):
  A=[[5,3],[1,3],[1,6]] (mod 7);
  annihilator line <(1,5,4)> ⊂ F_7³.

The standalone exact-integer/Fp verifier enumerated all vectors in Fp³ and verified the kernel has precisely p elements and both generators have nonzero p and q coordinates:

  TRIPLE_RELAXED_PT_LOCAL_KERNEL_PASS p 5  (1,2,1)
  TRIPLE_RELAXED_PT_LOCAL_KERNEL_PASS p 7  (1,5,4)

**These are local singular COORDINATES of a globally existing class via Poitou–Tate, not explicit cocycle values of Kato's derived system.** The existing δ_41·61=4 (mod5), δ_113·673=2 (mod7) are archival separate Kato/Kurihara calculations and do not identify that special class with this generic one.

## The still decisive missing arithmetic assertion

At good p>=5, proving an integrally normalized *two-prime Kurihara number* δ_{q1 q2} not ≡0 mod p for at least one admissible pair would make Kim's theorem imply Sha(E/Q)[p∞]=0. Castella–Sano only gives some-length nonvanishing. Our local determinant and this Poitou–Tate line are not enough.

A route through the conjectural generalized Perrin–Riou/Bockstein regulator identity also needs explicit verification of its hypotheses and would not by itself identify the **complex** L''/2 with the real Néron–Tate regulator. Never treat the assumed p-primary Sha finiteness in Burns–Kurihara–Sano Theorem 1.3 as an input obtained independently.

## References

- Chan-Ho Kim, arXiv:2505.09121, §4 and Proposition 4.2: https://arxiv.org/pdf/2505.09121
- Castella–Sano, arXiv:2601.14504, Theorem B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Burns–Kurihara–Sano, J. Math. Soc. Japan 76 (2024), Theorem 1.3: https://kurihara.math.keio.ac.jp/bks4.pdf
- Mazur–Rubin, Kolyvagin systems (2004), Poitou–Tate Selmer comparison theorem 2.3.4.
- Verification: verification/bsd389_triple_relaxed_selmer_line_20261108.py.

**No uniform finiteness of Sha or exact rank-two complex BSD asserted.**
