# Selmer bridge lemma: from a finite p-adic L-function jet to Sha[p^\infty]=0

**Status: algebraic argument; the analytic measure and source-theorem hypotheses must be audited separately for every application.** This note does *not* prove BSD over Q.

## Algebraic statement

Let \(\Lambda=\mathbf Z_p[[T]]\), \(p\) odd, and let
\(X=\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)^\vee\)
be a finitely generated torsion \(\Lambda\)-module for the cyclotomic
\(\mathbf Z_p\)-extension \(\mathbf Q_\infty/\mathbf Q\).
Assume:

1. \(\mathrm{rank}\,E(\mathbf Q)=2\), \(E(\mathbf Q)[p]=0\);
2. \(X\) has **no nonzero finite** \(\Lambda\)-submodule;
3. the characteristic ideal of \(X\) divides a power series
   \(F(T)\in\mathbf Z_p[[T]]\), with \(\mu(F)=0\), \(\lambda(F)=2\).

Then \(X\cong \mathbf Z_p^2\) with \(T\) acting as zero and
\(\Sha(E/\mathbf Q)[p^\infty]=0\).

The identical conclusion holds if instead
\(T\operatorname{char}_\Lambda(X)\mid F(T)\) and
\(\mu(F)=0,\lambda(F)=3\); this is the split multiplicative variant.

## Proof

The characteristic-ideal divisibility gives \(\mu(X)=0\) and
\(\lambda(X)\le2\). By the structure theorem for torsion
\(\mathbf Z_p[[T]]\)-modules, \(X\) is finitely generated over
\(\mathbf Z_p\) with rank \(s\le2\), up to finite p-primary torsion.
That torsion is a finite \(\Lambda\)-submodule and therefore zero.
Consequently \(X\cong\mathbf Z_p^s\) as a \(\mathbf Z_p\)-module.

There is no p-torsion point of \(E\) over \(\mathbf Q_\infty\):
if \(E(\mathbf Q_\infty)[p]\neq0\), the finite-dimensional
\(\mathbf F_p\)-module \(E(\mathbf Q_\infty)[p]\) has a nonzero invariant
under the pro-p group \(\Gamma=\operatorname{Gal}(\mathbf Q_\infty/\mathbf Q)\).
This would give \(E(\mathbf Q)[p]\neq0\), a contradiction.

Inflation-restriction therefore injects
\(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)\) into
\(\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)^\Gamma\).
The two independent rational points give an injection of
\((\mathbf Q_p/\mathbf Z_p)^2\) into these \(\Gamma\)-invariants.
Dualizing, \(X/TX\) admits a quotient \(\mathbf Z_p^2\).
Since \(X\cong\mathbf Z_p^s\), \(s\le2\), it follows that \(s=2\)
and the endomorphism \(T\colon X\to X\) is zero.

Thus the invariants of the cyclotomic Selmer are exactly
\((\mathbf Q_p/\mathbf Z_p)^2\), already filled by the two rational
Kummer classes. The Selmer group over \(\mathbf Q\) is therefore
filled by these classes. The global Kummer exact sequence
implies \(\Sha(E/\mathbf Q)[p^\infty]=0\). QED.

## Source audit and required external input

* Wuthrich, *On the Integrality of Modular Symbols and Kato's Euler System for Elliptic Curves*, Documenta Mathematica **19** (2014), Corollary 19:
  ordinary semi-stable \(\operatorname{char}_\Lambda(X)\mid L_p\);
  split multiplicative \(I\operatorname{char}_\Lambda(X)\mid L_p\),
  where \(I\) is the full cyclotomic augmentation ideal.
  [Primary PDF](https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-19/12.pdf)
* Greenberg, *Iwasawa Theory for Elliptic Curves* (1998),
  Proposition 4.15: a \(\Lambda\)-cotorsion Selmer with the stated local
  good ordinary/multiplicative condition and small ramification index
  has no proper finite-index \(\Lambda\)-submodules.
  [Primary preprint](https://arxiv.org/abs/math/9809206).
* For the split multiplicative case, **the projection from the full
  cyclotomic Iwasawa algebra onto the trivial tame-character component
  must be checked**, so the exceptional factor \(I\) indeed becomes
  \((T)\).
* For the good ordinary case, the raw finite modular-symbol
  coefficient \(C_p\) is **not itself** a definition of \(L_p(E,T)\).
  One must check the unit-root \(\alpha\)-stabilization, the lower
  coefficients, tame-character projection, and the period normalization
  before substituting \(F=L_p\).
* The finite computations and the above lemma do **not** prove the
  required coefficients are units for all sufficiently large primes.
  Nor do they establish the complex BSD leading-term equality.

The preceding proof is a conditional-on-the-stated-hypotheses
**algebraic lemma**, not an identification of every recorded moment
with the published \(p\)-adic \(L\)-function.
