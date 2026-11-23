# E389a1: a nonzero Cassels–Tate-compatible model surviving ALL 20 VAL1 theta/Fitting/norm constraints

2026-11-23. This is a **rigorous countermodel to an invalid inference**, not a claimed construction of actual Sha(E/K_r). It narrows the next arithmetic problem: compute the true norm coinvariants or an equivalent Selmer/local control map. The previously verified finiteness and sharper **conditional** order bounds are not invalidated.

## The exact group ring and input

Let R=Z_5[C_25]=Z_5[T]/((1+T)^25-1), T=sigma-1, and N=sum(sigma^i,0<=i<25). Let theta=F_r(1+T) be any one of the genuine twenty VAL1 Mazur–Tate coefficient vectors. The verified integral Taylor conditions are
\[
c_0=0,\quad 25\mid c_1,\quad 5\mid c_2,\quad 5\mid c_3,\qquad
\theta=\sum_{j=0}^{24}c_jT^j.
\]
The recorded data have c_2/5 nonzero mod 5 and their exact nontrivial cyclotomic resultants are nonzero. The latter yields a finite ring R/(N,theta), with the established Smith types (length 8 or 12).

## A concrete nonzero model

Set
\[
D=R/(T)\simeq\mathbf Z_5,\qquad
Y_0=R/(5,T^2)\simeq\mathbf F_5[T]/(T^2),\qquad
X_0=D^{\oplus2}\oplus Y_0.
\]

Then:
1. X_0 has exactly **three** minimal generators over the local ring R. It has a genuine exact sequence
   \[
   0\to Y_0\to X_0\to\mathbf Z_5^2\to0
   \]
   with trivial action on the rank-two quotient.
2. Norm N acts as 25 on the quotient and **zero** on Y_0. Indeed
   \[
   N=25+300T+2300T^2+\cdots+T^{24}
   \]
   so N is zero modulo (5,T^2).
3. Fitting ideals multiply under direct sum and Fitt_0(R/I)=I:
   \[
   \operatorname{Fitt}_{0,R}(X_0)
     =(T)^2(5,T^2)=(5T^2,T^4).
   \]
   **Every one of the twenty actual theta_r belongs to this Fitting ideal**. To prove it without any formal power-series divisibility error, write c_1=25k and use the exact group relation
   \[
   25T=-300T^2-2300T^3-\sum_{j=4}^{25}\binom{25}{j}T^j.
   \]
   Thus in R the T² and T³ coefficients of theta become
   \(c_2-300k\) and \(c_3-2300k\), both divisible by 5. Hence
   \[
   \theta\in(5T^2,T^4)=\operatorname{Fitt}_{0,R}(X_0).
   \]
   Inversion sigma->sigma^{-1} preserves this ideal, so the statement is unchanged for theta#.
4. The underlying abelian group of Y_0 is (Z/5)^2, of order **25**. In basis (1,T), sigma acts by
   \[
   A=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
   \]
   Its determinant is 1; it preserves the perfect alternating form
   \[
   \langle (a,b),(c,d)\rangle=(ad-bc)/5\pmod{\mathbf Z}.
   \]
   This is the algebraic parity and Galois-invariance pattern expected of a *finite* odd-primary Cassels–Tate group. It is NOT evidence that the real Sha has this form.
5. Since theta and N annihilate Y_0, it is a module over the **actual** quotient R/(N,theta), irrespective of whether its Smith length is 8 or 12. Also
   \[
   \#(X_0/NX_0)=5^6,\qquad
   \#Y_0=5^2=\#(X_0/NX_0)/5^4.
   \]

**Conclusion (logical no-go):** Even with the genuine 20 histograms, all exact Smith computations, finite R/(N,theta), theta in the actual Fitt_0, rank-two trivial quotient, d_R(X)<=3, norm annihilation and an invariant alternating form on Y, these statements alone **do not imply Y=0**. An additional genuinely arithmetic restriction is necessary.

## Sharp next target (not a circular equality)

For the **actual** arithmetic X_r, Y_r under the proven rank-stability and norm annihilation assumptions, the snake lemma already gives
\[
0\to Y_r\to X_r/NX_r\to(\mathbf Z_5/25)^2\to0.
\]
Therefore
\[
\boxed{\Sha(E/K_r)[5^\infty]=0
\iff\#(X_r/NX_r)=5^4.}
\]

This is the **norm-coinvariant index criterion**. It targets a finite module and can in principle be attacked by restriction/corestriction, Poitou–Tate local conditions or a genuine descent calculation. It cannot be inferred from theta-Fitting inclusion or theta matrix Smith factors alone; the countermodel above gives index 5^6 instead of 5^4. A useful alternative is a computation proving Y_r/(5,T)Y_r=0, which then yields Y_r=0 by Nakayama, but this also demands extra arithmetic information.

The user-executed twenty-line transcript and its SHA-checking source establish the theta input conditions; the separate companion script verifies their reduction into the Fitting ideal of the explicit countermodel. The companion does NOT calculate true Selmer or Sha.

Primary external input for the **real** arithmetic Fitting containment: Bullach–Honnor, *On the refined 'Birch--Swinnerton-Dyer type' conjectures of Mazur and Tate*, Theorem 1.4(b), Hypothesis 1.2 and Remark 1.5(a), https://arxiv.org/pdf/2511.07203.


## Update 2026-11-23 — genuine arithmetic NONVANISHING, superseding the earlier zero target

A subsequent *arithmetic*, rather than formal group-ring, argument proves that the **twenty real degree-25 fields carry nonzero true Sha[5]**, conditional on the already established rank-stability, full residual image and base Sha5 certificates. At the totally ramified prime q=13001, \(E(\mathbf F_q)[5]\simeq\mathbf F_5^2\) while the rational MW image modulo 5 is only one-dimensional (Q=2P). Poitou–Tate produces a 3-dimensional Q-relaxed Selmer group, and tame inertia kills its new local ramification after restriction to K. Since E(K)=E(Q) has mod-5 dimension 2, the third genuine Selmer class has a nonzero Sha image. The true Fitting bound also forces the invariant Selmer dimension to equal 3. This is proved in [the new theorem](bsd389_p5_all20_relaxed_Selmer_nonzero_Sha_theorem_2026-11-23.md), with the independently executable finite-field local audit in ../verification/bsd389_p5_all20_local_13001_relaxed_selmer_sha_nonzero_gate.py.

**Important correction of research direction:** the equality \(\#(X_r/N_GX_r)=5^4\) is still a correct iff-criterion for *zero* Sha, but the new theorem shows it is **false for each of these twenty fields**. Indeed the genuine arithmetic coinvariant index is at least \(5^6\), and the true Sha5 has order at least \(5^2\) by the finite alternating Cassels–Tate pairing. Combining with the earlier upper bounds yields \(5^2\le\#\Sha[5^\infty]\le5^{20}\) for r mod 5 in {1,2}, and \(5^2\le\#\Sha[5^\infty]\le5^{32}\) for r mod 5 in {3,4}. This is **not a claim about Sha(E/Q) at all primes**.
