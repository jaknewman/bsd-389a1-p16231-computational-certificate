# Global diagonal Fitting intersection: exact equivalence with full Sha finiteness

**2026-11-01. Exact elementary theorem.** This is a logical/proof-planning audit, **not** a proof that Sha(389a1) is finite and **not** the construction of a new arithmetic Euler-system element. The result exposes a circularity risk in the phrase "seek a global nonzero rational scalar inside all local second Fitting ideals."

## 1. Definitions from the unconditional rank-two Kummer theorem

For E/Q=389a1, proven \(E(\mathbf Q)\simeq\mathbf Z^2\). For each prime p,
\[
X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee,
\qquad A_p=\Sha(E/\mathbf Q)[p^\infty].
\]
The Kummer/Pontryagin split gives unconditionally
\[
X_p\simeq\mathbf Z_p^2\oplus A_p^\vee,\qquad
I_p:=\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)
   =\operatorname{Fitt}_{0,\mathbf Z_p}(A_p^\vee).
\]

Cofinite generation of Selmer yields for each p an exponent
\(e_p\in\mathbf Z_{\ge0}\cup\{\infty\}\) with
\[
 I_p=
 \begin{cases}
   p^{e_p}\mathbf Z_p,& e_p<\infty,\\
   (0),&e_p=\infty.
 \end{cases}
\]
If \(e_p<\infty\), \(A_p\) is finite and \(\#A_p=p^{e_p}\); if \(e_p=\infty\), \(A_p\) contains a nontrivial divisible component and is infinite. In particular \(e_p=0\iff A_p=0\).

## 2. Global **intersection** theorem

Define the genuinely diagonal integral ideal
\[
\mathcal C(E)=
\{n\in\mathbf Z:\ \iota_p(n)\in I_p\text{ for every prime }p\}
=\bigcap_p\iota_p^{-1}(I_p)\subseteq\mathbf Z,
\]
where \(\iota_p:\mathbf Z\to\mathbf Z_p\).

**Theorem (no BSD assumptions).**
\[
\boxed{
\mathcal C(E)\ne(0)
\quad\Longleftrightarrow\quad
\Sha(E/\mathbf Q)\text{ is finite}.
}
\]
Moreover, when Sha is finite,
\[
\boxed{\mathcal C(E)=(\#\Sha(E/\mathbf Q))\,\mathbf Z.}
\]

**Proof.** If some \(e_p=\infty\), then \(I_p=(0)\). As the diagonal map \(\mathbf Z\hookrightarrow\mathbf Z_p\) is injective, \(\mathcal C(E)=0\). Suppose all \(e_p\) are finite. The membership \(\iota_p(n)\in I_p\) for \(n\in\mathbf Z\setminus\{0\}\) is equivalent to \(v_p(n)\ge e_p\). Since a nonzero integer has only finitely many prime factors, such n exists **iff** \(e_p=0\) for all but finitely many p. These two conditions jointly say exactly that the direct sum of finite p-primary torsion groups \(A_p\) is finite. In that case its order \(N=\prod_pp^{e_p}=\#\Sha\) is a finite positive integer and \(n\in\mathcal C(E)\iff N\mid n\). Thus \(\mathcal C(E)=N\mathbf Z\). QED.

This applies to all p including 2,3 and bad p=389.

## 3. Finite excluded prime sets and rational scalars

For a **fixed finite set S**, define
\[
\mathcal C_S(E)=
\{n\in\mathbf Z:\iota_p(n)\in I_p
 \text{ for all }p\notin S\}.
\]
The same proof shows
\[
\boxed{\mathcal C_S(E)\ne0
\iff \bigoplus_{p\notin S}A_p\text{ is finite},}
\]
and, if nonzero, its positive generator equals the order
\(\prod_{p\notin S}\#A_p\).

For a fixed \(\Delta=a/b\in\mathbf Q^\times\) and p∤b,
\[
\Delta\in I_p\Longleftrightarrow a\in I_p,
\]
because b is a unit in \(\mathbf Z_p\). Hence the **existence** of some nonzero rational \(\Delta\) satisfying all the relevant local membership conditions, with some finite S plus primes dividing its denominator, is **logically equivalent** to finiteness of the corresponding prime-to-S Sha part.

**Important correction of research rhetoric:** Stating "find a rational \(\Delta\)" is **not itself a new technique**. Unless the scalar is independently constructed from arithmetic/geometric input **and** its comparison to the true Selmer Fitting ideals is proved without presupposing the finiteness of Sha, it just restates the conjectural target. Similarly, the tautological choice \(\Delta=\#\Sha\) when finite is not a proof method. One must exhibit **an explicit candidate from independent finite data** (for example, a rigorously constructed integral motivic/Euler-system zeta morphism), establish its rationality and nonvanishing and prove its integral realization in \(I_p\) uniformly in p.

## 4. Difference from the profinite counterexample

Over \(R=\widehat{\mathbf Z}\), the abstract module
\(X=R^2\oplus(R/bR)^2\) with \(b=(p)_p\) is finitely presented and has \(\operatorname{Fitt}_2=(b^2)\ne0\), but its local Fitting ideals are all \((p^2)\). The **diagonal intersection** \(\mathbf Z\cap(b^2)=(0)\), exactly as predicted by the theorem because the fake family has nontrivial p-torsion for infinitely many primes.

Thus there is no paradox: a nonzero ideal of the profinite product ring and a nonzero element in its **diagonal intersection with \(\mathbf Z\)** are different assertions. Rational descent is the hard arithmetic requirement, not an automatic property of determinant lines.

## 5. Mathematically honest next step

The proof target is no longer merely "prove some nonzero \(C\)" but:

**Produce independently of Sha an explicitly described, nonzero \(\Delta=a/b\in\mathbf Q^\times\) (or a rational determinant line with fixed \(\mathbf Z\)-lattice), and a theorem-level uniform comparison** with the actual \(I_p=\operatorname{Fitt}_2(X_p)\), outside an explicit finite S, including local Tamagawa factors and lattice normalization.

Such a construction would be a **new major theorem**, not a routine determinant calculation. The exact global intersection theorem diagnoses when a proposed scalar argument is circular; it does not establish the required construction.

Even proving the complete finiteness of Sha would leave the complex strong BSD identity
\[
L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\#\Sha(E/\mathbf Q)
\]
as a separate proof obligation.

References: [unconditional rank-two Fitting identity](bsd389_unconditional_rank2_kummer_fitt2_identity_2026-10-30.md); [constructive profinite counterexample](bsd389_uniform_global_integral_det_vs_profinite_counterexample_2026-11-01.md); [uniform issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8).
