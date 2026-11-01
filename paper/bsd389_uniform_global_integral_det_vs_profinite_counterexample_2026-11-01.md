# Global rank-two Selmer determinants: an exact \(\widehat{\mathbf Z}\) counterexample and the genuine integral descent needed

**2026-11-01. Status:** exact elementary algebraic result, independent of unproved BSD. It **does not prove** a uniform bound on the rational Tate–Shafarevich group for E=389a1. The construction is an **abstract counterexample**, not the Selmer module of any claimed elliptic curve.

## 1. The all-prime target already identified

For E=389a1, the proved rank 2 and absence of rational torsion yield, for each prime p, the Kummer/Pontryagin decomposition
\[
X_p:=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee
\simeq\mathbf Z_p^2\oplus\Sha(E/\mathbf Q)[p^\infty]^\vee .
\]
Hence
\[
I_p:=\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)
=\operatorname{Fitt}_{0,\mathbf Z_p}\bigl(\Sha[p^\infty]^\vee\bigr).
\]
The global-support goal is **one fixed integer** \(C\in\mathbf Z\setminus\{0\}\) and an **explicit finite** set S for which
\[
C\mathbf Z_p\subseteq I_p\quad\text{for every prime }p\notin S.
\]
At primes p∉S, p∤C, this implies \(I_p=\mathbf Z_p\) and \(\Sha[p^\infty]=0\). This implication follows from module theory only; **construction of C remains OPEN**.

## 2. Exact obstruction: a global profinite finite presentation does NOT provide C

Put \(R=\widehat{\mathbf Z}=\prod_{p\text{ prime}}\mathbf Z_p\).
The element
\[
b=(\,p\,)_p\in R
\]
is a **non-zero-divisor**: multiplication by b is injective in each domain \(\mathbf Z_p\), and therefore in the product ring R.

Define
\[
X=R^2\oplus(R/bR)^2.
\]
The final two summands have an honest **finite free presentation**
\[
0\longrightarrow R^2
\xrightarrow{\operatorname{diag}(b,b)}
R^2\longrightarrow (R/bR)^2\longrightarrow0,
\]
whose determinant is \(b^2\ne0\). Thus X is finitely presented over R, and even has a perfect two-term presentation of its torsion part. By the standard direct-sum Fitting identity,
\[
\boxed{\operatorname{Fitt}_{2,R}(X)=(b^2).}
\]

Now localize through the projection \(R\to\mathbf Z_p\). Fitting ideals commute with base change:
\[
X\otimes_R\mathbf Z_p
\simeq\mathbf Z_p^2\oplus(\mathbf Z_p/p\mathbf Z_p)^2,\quad
\boxed{\operatorname{Fitt}_{2,\mathbf Z_p}(X\otimes_R\mathbf Z_p)
=p^2\mathbf Z_p}
\]
**for every prime p**.

This respects the **square-order** constraint on a finite p-primary Sha (the abstract local torsion modules are of cardinality p²). It shows **a nonzero global determinant over R and a perfect R-complex do not bound the prime support**.

Indeed, if a fixed nonzero integer C satisfied \(C R\subseteq(b^2)\), then \(p^2\mid C\) for **every prime p**, impossible by Euclid. Even the weaker condition that \(I_p\) is a unit ideal for almost every p fails: it is \(p^2\mathbf Z_p\) at *every p*.

**Critical distinction:** the element \(b^2=(p^2)_p\) lies in the profinite coefficient ring R but does **not** arise from the diagonal copy of any rational number \(\Delta\in\mathbf Q^\times\) (nor the denominator-free integral copy of \(\mathbf Z\)). A **finite presentation over \(\widehat{\mathbf Z}\)** is not a finite presentation over \(\mathbf Z\).

Reference: [Stacks Project, Lemma 15.8.4](https://stacks.math.columbia.edu/tag/07Z6), direct-sum/base-change rules for Fitting ideals.

## 3. Stronger circularity audit: global finite \(\mathbf Z\)-module models are equivalent to Sha finiteness

**Theorem for the fixed E=389a1.** Suppose there exists a finitely generated \(\mathbf Z\)-module M and, for **every prime p**, an isomorphism of \(\mathbf Z_p\)-modules
\[
M\otimes_{\mathbf Z}\mathbf Z_p\simeq X_p.
\]
Then \(\Sha(E/\mathbf Q)\) is **finite**. Conversely, if \(\Sha\) is finite, such an M exists as an abstract module.

**Proof.** Structure theorem over Z: \(M\simeq\mathbf Z^r\oplus T\), with finite T. The known **rigorously certified** \(\Sha[5^\infty]=0\) gives \(X_5\simeq\mathbf Z_5^2\); hence \(r=2\) and \(T[5^\infty]=0\). At every p, \(X_p\simeq\mathbf Z_p^2\oplus\Sha[p^\infty]^\vee\), while
\(M\otimes\mathbf Z_p\simeq\mathbf Z_p^2\oplus T[p^\infty]\).
Cancellation and invariant factors over the discrete valuation ring \(\mathbf Z_p\) yield
\(\Sha[p^\infty]^\vee\simeq T[p^\infty]\).
Thus the total Sha has only the finitely many p dividing \(\#T\), and every part is finite: Sha is finite. Conversely, if Sha is finite, set \(M=\mathbf Z^2\oplus\Sha^\vee\), where \(\Sha^\vee=\operatorname{Hom}(\Sha,\mathbf Q/\mathbf Z)\) is a finite abelian group. The Kummer decomposition supplies the required completions. QED.

**Interpretation:** producing such a finite global M **from independent arithmetic construction** would indeed **prove** finiteness, but merely *postulating* M is as strong as assuming the goal. An unspecified "global Selmer complex" is not a shortcut unless its finite integral model, local Selmer identifications and rational determinant can be **proved without invoking Sha finiteness**.

## 4. Precise non-circular sufficient theorem: one rational scalar with integral comparisons

Let \(S\) be a finite explicit prime set. **Suppose one constructs**
\(\Delta=a/b\in\mathbf Q^\times\) in lowest terms, *independently of p*, and a proven comparison showing
\[
\Delta\in I_p\subseteq\mathbf Z_p\qquad
(p\notin S,\ p\nmid b).
\]
Then setting \(C=|a|\ne0\) proves
\[
I_p\supseteq a\mathbf Z_p \quad (p\notin S,\ p\nmid b),
\]
because b is a p-adic unit. Hence
\[
\Sha(E/\mathbf Q)[p^\infty]=0
\quad\text{for every }p\notin S\cup\{p:p\mid ab\}.
\]
At the remaining nonexcluded primes dividing a, the stronger bound is
\[
\#\Sha(E/\mathbf Q)[p^\infty]\le p^{v_p(a)}.
\]
The excluded primes in S and those dividing b would require separate bounds.

**The only unproved mathematical input is the existence and integrality of \(\Delta\) and the comparison to \(I_p\)**. This is the desired new theorem, not something supplied by local C01/Kurihara computations or the Gross-orbit norm 729.

## 5. Appropriate framework and remaining archimedean work

The motivic fundamental/determinant line and its p-adic integral lattice are the natural setting to formulate a **rationally descended** global zeta element. The **Equivariant Tamagawa Number Conjecture** (Bloch–Kato; Fukaya–Kato; Fontaine–Perrin-Riou) predicts exactly this sort of compatibility among a rational line, its p-adic realizations and the complex leading \(L\)-value. See [Fouquet, §2.2.3, Conjecture 2.11](https://jep.centre-mersenne.org/item/10.5802/jep.38.pdf) and [2026 survey of motivic fundamental lines, §2.10](https://link.springer.com/article/10.1007/s40687-026-00646-7).

**Do NOT assume** ETNC or an integral rank-two zeta isomorphism for E389a1: doing so would incorporate a BSD-strength input, potentially including the desired conclusion. A legitimate proof must produce the relevant zeta element, prove its integral comparison at all primes outside explicit S, and separately justify the complex period/height normalization. Naming a determinant line or confirming the algebraic toric norm 729 is **insufficient**.

## 6. Required next mathematical construction

Instead of running more finite p-specific tests, demand an independently defined candidate \(\Delta\) with the following verifiable features:

1. A **rational** construction \(\Delta\in\mathbf Q^\times\) or a free rank-one Z-lattice with a specified rational trivialization, not merely an element of \(\prod_p\mathbf Z_p\).
2. A globally fixed nonzero numerator, explicitly factorizable after a proof \(\Delta\ne0\).
3. A **uniform p-integral comparison theorem** \(\Delta\in\operatorname{Fitt}_{2,\mathbf Z_p}(X_p)\) for every p outside a finite, explicitly determined set S.
4. Independent comparison of the complex leading coefficient to the periods and rank-two height regulator (BSD strong issue #9).

**Status: items 1–4 NOT PROVED for E389a1.** The counterexample in §2 is an exact theorem explaining why the distinction matters; it is not a BSD breakthrough and does not claim to resolve any remaining Sha component.

Related tracking: [uniform support issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8) and [full complex BSD issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
