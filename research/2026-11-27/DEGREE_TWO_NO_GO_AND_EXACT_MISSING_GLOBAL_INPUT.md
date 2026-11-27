# BSD 389a1 — No-go theorem for automatic degree-two primitivity; the remaining independent input

**27 November 2026 — formal obstruction, not a proof of BSD or of H2.**

## 1. The exact bottleneck

Write \(\partial_p^{(r)}\) for Kim's minimal p-adic divisibility index among Kurihara coefficients with \(r\) admissible auxiliary prime factors, and \(\partial_p^{(\infty)}=\min_r\partial_p^{(r)}\). For the good primes to which Castella–Sano Theorem B applies and the curve 389a1 with Tamagawa product 1, it gives

\[
\partial_p^{(\infty)}=0.
\]

Kim Theorem 1.8 says that, if the first nonzero coefficient occurs at degree two, then

\[
\operatorname{length}_{\mathbf Z_p}\left(
\operatorname{Sel}_{p^\infty}(E/\mathbf Q)/
\operatorname{Sel}_{p^\infty}(E/\mathbf Q)_{\rm div}
\right)
=\partial_p^{(2)}.
\]

With Mordell–Weil rank 2, the group on the left then identifies with \(\Sha(E/\mathbf Q)[p^\infty]\), provided it is finite. Its perfect alternating Cassels–Tate pairing forces even length. The sought theorem H2 is

\[
\partial_p^{(2)}=0 \quad\text{for every admissible good }p.
\]

In the rank-two situation this is precisely the assertion that the finite p-primary obstruction vanishes. It cannot be proved just by renaming that obstruction a “Bockstein regulator.”

## 2. A rigorous countermodel to formal contraction

For any odd prime \(p\) and integer \(e\ge1\), define the abstract cofinitely generated Selmer-shaped module

\[
S_{p,e}=(\mathbf Q_p/\mathbf Z_p)^2
\oplus(\mathbf Z/p^e\mathbf Z)^2.
\]

Its Pontryagin dual is

\[
X_{p,e}=\mathbf Z_p^2\oplus(\mathbf Z/p^e\mathbf Z)^2.
\]

It has **corank two**, precisely as the proved Mordell–Weil group. Its finite part has a **perfect alternating pairing**

\[
\langle(x,y),(u,v)\rangle=(xv-yu)/p^e\bmod\mathbf Z.
\]

The diagonal presentation matrix \(D_e=\mathrm{diag}(0,0,p^e,p^e)\) of \(X_{p,e}\) gives by explicit minors

\[
\operatorname{Fitt}_0(X_{p,e})=
\operatorname{Fitt}_1(X_{p,e})=0,\quad
\operatorname{Fitt}_2(X_{p,e})=(p^{2e}),\quad
\operatorname{Fitt}_3(X_{p,e})=(p^e),\quad
\operatorname{Fitt}_4(X_{p,e})=(1).
\]

Thus an abstract Kurihara-index sequence

\[
\partial_p^{(2)}=2e,\qquad \partial_p^{(4)}=0
\]

satisfies exactly the rank-two, parity, higher-Fitting, monotonicity, and limiting-unit constraints of Kim plus Castella–Sano, while **H2 is false**.

This is a counterexample to *logical implication from these general structural constraints*, not an assertion that this module is realized as the Selmer group of 389a1 (or even by a particular elliptic curve).

**Theorem (no formal unit-preserving contraction).**
There is no theorem of the form
“\(\partial_p^{(\infty)}=0\), corank Selmer 2, perfect alternating pairing and Kim's Fitting relations imply \(\partial_p^{(2)}=0\)”
without additional arithmetic hypotheses.
The family \(S_{p,e}\) proves this for every \(p\) and \(e\ge1\).

A true contraction inside the Kato/Selmer complex must therefore detect an arithmetic invariant not contained in the rank, the Euler factor's formal double zero, augmentation projections, parity, and refined nonvanishing alone.

## 3. What remains to prove for the *specific curve* 389a1

A non-circular strategy must produce **one independent global datum** not defined by \(\Sha\). Two concrete equivalent targets:

**Target A — a genuine degree-two Kurihara unit.** For every remaining good \(p\), construct admissible \(\ell_1,\ell_2\) and prove
\[
\delta_{\ell_1\ell_2}^{(p)}\not\equiv0\bmod p
\]
with the Néron-normalized modular symbols. This is exactly H2, but it is an *explicit computational/arithmetic witness* and not a formal contraction.

**Target B — a derived Kato determinant with independently proved integrality and primitivity.** Produce a canonical global rank-two derived Euler-system class in the *actual Selmer complex*, along with an integral regulator/duality comparison that identifies its image in the fully mixed augmentation quotient with the two-factor Kurihara coefficient, and prove the determinant is a p-unit **without** using \(\Sha[p^\infty]=0\) or H2 in its proof. This is the genuinely new theorem needed. The previous simple Euler \(Y^2\) division is invalid because multiplication by \(Y^2\) in \(\mathbf F_p[Y]/(Y^p)\) has a 2-dimensional kernel; projections erase the fully mixed class, and false pfaffian formulas are ruled out by explicit 389a1 examples.

Uniformity across all \(p\) would require an additional *global* argument ensuring the determinant's primitivity at every p, or a finite exceptional set together with rigorous tests on each remaining exceptional p. **A finite successful search of admissible pairs cannot substitute for this quantifier.**

## 4. Reproduction

Run the standard-library script:

\`\`\`bash
python3 research/2026-11-27/verification/bsd389_rank2_filtration_countermodel.py
\`\`\`

It checks all minors/Fitting valuations and perfect alternating pairing for \(p=5,7,107,599,1049,2003\) and \(e=1,2,3\).

## Primary literature

- Castella–Sano (2026), Theorem B: https://web.math.ucsb.edu/~castella/Kurihara.pdf
- Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf

**Scope:** exact formal obstruction and a sharp statement of missing arithmetic input. H2 and full BSD for 389a1 are not established by this note.
