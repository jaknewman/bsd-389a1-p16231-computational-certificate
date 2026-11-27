# The tame-trivial projection and the exceptional augmentation factor

**27 November 2026 — exact algebraic comparison.** This note audits the passage from Wuthrich's *full cyclotomic Iwasawa algebra* to Greenberg's \(\mathbf Z_p\)-cyclotomic Selmer module. It is not an independent computation of a modular symbol or a proof of the complex BSD formula.

## 1. The two Iwasawa algebras

Let \(p\ge5\) be odd, \(K_\infty=\mathbf Q(\zeta_{p^\infty})\), and let \(\mathbf Q_\infty\) denote the unique cyclotomic \(\mathbf Z_p\)-extension of \(\mathbf Q\). Write

\[
G=\operatorname{Gal}(K_\infty/\mathbf Q)\simeq\Delta\times\Gamma,\qquad
|\Delta|=p-1,\qquad\Gamma\simeq\mathbf Z_p.
\]

With \(\Lambda_{\rm full}=\mathbf Z_p[[G]]\) and \(\Lambda=\mathbf Z_p[[\Gamma]]\simeq\mathbf Z_p[[T]]\), define the *integral* idempotent

\[
e_0=\frac1{p-1}\sum_{\delta\in\Delta}\delta
\in\mathbf Z_p[\Delta].
\]

Then \(e_0\Lambda_{\rm full}\simeq\Lambda\). Applying \(e_0\) is exact on \(\mathbf Z_p\)-primary modules because \(p-1\) is invertible in \(\mathbf Z_p\).

## 2. Comparison of global Selmer conditions

Let \(A=E[p^\infty]\). Since \(\Delta\) has order prime to \(p\), for any \(\Delta\)-module of p-primary torsion,

\[
H^i(\Delta,M)=0\quad(i>0).
\]

Inflation-restriction therefore gives

\[
H^1(\mathbf Q_\infty,A)\xrightarrow{\sim}
H^1(K_\infty,A)^\Delta.
\]

The same argument holds after restricting to ramification at the primes of good and bad reduction and at the corresponding local decomposition groups, whose \(\Delta\)-parts also have order prime to \(p\). Thus the Kummer local conditions descend exactly, and

\[
\boxed{\operatorname{Sel}_{p^\infty}(E/\mathbf Q_\infty)
\simeq\operatorname{Sel}_{p^\infty}(E/K_\infty)^\Delta.}
\]

Because the idempotent \(e_0\) is invariant under inversion, the Pontryagin dual of the right-hand side is the \(e_0\)-component of the full cyclotomic Selmer dual. Accordingly,

\[
\boxed{X_\Gamma\simeq e_0X_{\mathrm{full}}\quad\text{and}\quad
\operatorname{char}_{\Lambda}(X_\Gamma)=
e_0\bigl(\operatorname{char}_{\Lambda_{\rm full}}(X_{\mathrm{full}})\bigr).}
\]

Here the equality of characteristic ideals uses the direct-product decomposition of \(\Lambda_{\rm full}\) under \(e_0\) and the assumption of torsion.

## 3. The split multiplicative exceptional factor

Wuthrich's Corollary 19 (Documenta Mathematica **19**, 2014, pp. 398–399) states the ideal divisibility

\[
I\cdot\operatorname{char}_{\Lambda_{\rm full}}(X_{\mathrm{full}})
\mid\bigl(L_p(E)\bigr)
\]

when \(p\) is a split-multiplicative prime of semistable reduction. Here

\[
I=\ker\bigl(\operatorname{aug}:\Lambda_{\rm full}\to\mathbf Z_p\bigr)
\]

is the **full augmentation ideal**, not an arbitrary Euler factor.

Under \(e_0\), augmentation becomes evaluation at \(\gamma=1\). Hence

\[
\boxed{e_0I=(\gamma-1)=(T)\subset\Lambda.}
\]

Applying \(e_0\) to Wuthrich's divisibility yields exactly

\[
\boxed{
T\cdot\operatorname{char}_\Lambda(X_\Gamma)
\mid L_p^{(\eta=0)}(E,T).
}
\]

This removes the ambiguity of passing from the full tame character algebra to the trivial tame branch.

## 4. Application to 389a1: what is logically certified

For \(E:y^2+y=x^3+x^2-2x\) at \(p=389\), split multiplicative reduction gives \(a_{389}=1\). If the **Néron-normalized** 390-entry rational modular-symbol table reproduces the standard analytic \(L_{389}^{(\eta=0)}(E,T)\), the exact finite measure computation gives

\[
L_{389}^{(\eta=0)}(E,T)\equiv321\,T^3+O(T^4)\pmod{389},
\qquad321\not\equiv0\pmod{389}.
\]

By the projection theorem above and Wuthrich, it follows that

\[
\mu(X_\Gamma)=0,\qquad\lambda(X_\Gamma)\le2.
\]

Greenberg, *Iwasawa Theory for Elliptic Curves*, Proposition 4.15, applies if \(X_\Gamma\) is \(\Lambda\)-torsion (as ensured by the cited Kato/Wuthrich theory), because the ramification index of \(\mathbf Q_{389}/\mathbf Q_{389}\) is \(1\le389-2\), and \(E\) has multiplicative reduction there. Thus \(X_\Gamma\) has no nonzero finite \(\Lambda\)-submodule.

Combining the two independent Mordell–Weil Kummer classes and the algebraic argument recorded in \`SELMER_BRIDGE_LEMMA.md\`, we deduce

\[
\boxed{\Sha(E/\mathbf Q)[389^\infty]=0}
\]

**conditional only on the explicitly identified normalization and independently authenticated finite calculation**—not on BSD or a conjectural Iwasawa main conjecture. The remaining audit is the *exact comparison of the cached modular-symbol table and the analytic p-adic measure*, not the \(\Delta\)-projection or the formal characteristic-ideal inequality.

**Publication standard:** independent Sage/eclib reproduction and a full check of the p=389 analytic measure convention remain mandatory before promoting this reported certificate from a draft research branch to a fully reviewed theorem.

## Primary sources

- Wuthrich, [*On the integrality of modular symbols and Kato's Euler system for elliptic curves*](https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-19/12.pdf), Corollary 19 and §5.
- Greenberg, [*Iwasawa Theory for Elliptic Curves*](https://arxiv.org/abs/math/9809206), Proposition 4.15.
- [SageMath p-adic L-series](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/padic_lseries.html), measure formula and tame character component.
