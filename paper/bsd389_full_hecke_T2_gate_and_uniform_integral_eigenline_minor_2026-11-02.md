# First actual non-marginal Hecke constraint, and a global integral eigenline minor independent of Sha

**Date:** 2026-11-02. Two different and rigorously delimited advances:

1. A **four-cusp exact \(T_2\) relation** detects the artificial eight-term perturbation previously invisible to both complete Hecke marginal polynomials.
2. An exact **integer Hecke matrix-minor theorem** provides a program to construct a nonzero, **p-independent** integer \(C_{\mathrm{Hecke}}\), bounding the exceptional primes for **uniqueness of a Hecke eigenline on an explicitly defined integral Manin lattice**. This is an arithmetic global integer **different from the unknown** \(C_{\Sha}\) that would bound the second Selmer Fitting ideal. No implication of strong BSD or Sha finiteness.

Scripts have been **published but not yet run on the user's Ubuntu host** as of the initial note; their full Sage/eclib output and the numerical determinant \(C_{\mathrm{Hecke}}\) are **not preclaimed**.

## I. A concrete non-marginal \(T_2\) witness against the fake eight-term change

Let \(p=5\), \(q_1=41\), \(q_2=61\), \(n=2501\), with primitive roots \(g_1=6\bmod41\), \(g_2=2\bmod61\). In the CRT unit-group ring
\[
R=\mathbf F_5[X,Y]/(X^{40}-1,Y^{60}-1)
\]
consider the exact eight-term sign-plus element
\[
H=(1+X^{20}Y^{30})(1-X)(1-Y).
\]
The earlier [eight-term theorem](bsd389_kurihara_full_marginal_kernel_and_free_mixed_coefficient_2026-11-02.md) proves
\[
H(X,1)=H(1,Y)=0,\quad [TU]H(1+T,1+U)=2.
\]
Consequently the **formal** \(\Theta_E+3H\) changes the true E189a1 p5 mixed coefficient \(4\) to \(4+3\cdot2=0\bmod5\) while fixing both *entire* marginals.

### Exact sparse support at denominator 2501

The nonzero coefficient list of H at rational cusps \(a/2501\), \(a\) a unit modulo 2501, is
\[
\begin{array}{r|rrrrrrrr}
a&1&124&486&609&1892&2015&2377&2500\\
h(a/2501)&1&-1&1&-1&-1&1&-1&1
\end{array}
\]
The involution \(a\mapsto2501-a\) fixes these coefficients, so H has the required sign-plus symmetry. For the **artificial zero extension** \(h:\mathbf Q\to\mathbf F_5\), set \(h(r)=h(a/2501)\) if the reduced denominator of r is 2501 and numerator modulo 2501 is one of those eight residues, and \(h(r)=0\) otherwise. This extension is 1-periodic and even, but need NOT be a modular eigensymbol.

For E=389a1, the point count \(\#E(\mathbf F_2)=5\) gives \(a_2(E)=2+1-5=-2\). The **exact weight-two Hecke identity**, valid for the true normalized modular symbol \(m=m_E^+\), is
\[
a_2\,m(r)=m(2r)+m(r/2)+m((r+1)/2).
\tag{H2}
\]

Take \(r=1/2501\). The four cusp inputs are
\[
r={1\over2501},\quad 2r={2\over2501},\quad
r/2={1\over5002},\quad
(r+1)/2={1251\over2501}.
\]
The eight-term perturbation has the **exact** values
\[
\boxed{(h(r),h(2r),h(r/2),h((r+1)/2))=(1,0,0,0).}
\]
The last zero holds because \(1251\bmod41=21\notin\{1,6,35,40\}\), the q1-side support set of H. Therefore, for \(\widetilde m=m+3h\), the \(T_2\) Hecke defect equals
\[
\begin{aligned}
a_2\widetilde m(r)-\widetilde m(2r)-\widetilde m(r/2)
-\widetilde m((r+1)/2)
&=3a_2=-6\\
&\equiv\boxed{4\bmod5}.
\end{aligned}
\]
Thus **\(\widetilde m=m+3h\) with this particular zero extension cannot satisfy the genuine \(T_2\) eigenrelation**. This supplies an explicit *non-marginal*, four-cusp constraint capable of detecting H.

**Scope caveat:** The fact that the **zero extension** fails (H2) does **NOT** prove that some *different extension* of its eight fixed denominator-2501 changes could not satisfy Hecke; nor does it establish full Manin and conductor compatibility. It is not a uniform theorem about p, and not a Sha proof.

[Executable short source](../verification/bsd389_p5_T2_nonmarginal_manin_gate.py) has an `--algebra-only` branch checking this computation without Sage, and the default branch additionally checks the **unperturbed true identity (H2) exactly through both independently normalized Sage and eclib modular-symbol implementations** at the four cusps. It also verifies that the synthetic \(\widetilde m\) violates it. An optional `--eigenline` computes the **entire level-389 sign-plus E-Hecke eigensymbol dimension** over \(\mathbf F_5\) and over \(\mathbf Q\) using Sage's documented native algorithm; dimension 1 is **not assumed** before the run.

## II. A truly fixed integer from the integral modular-symbol Hecke lattice

This is a **mathematically more promising and distinct** p-uniform arithmetic construction: certify the uniqueness of the E Hecke eigensymbol on a *fixed integral* Manin lattice for every p outside the prime factors of an explicitly computable nonzero integer.

Sage documents the **integral Hecke matrices**
`M.integral_hecke_matrix(ell)` as the representation of \(T_\ell\) on its lattice `M.integral_structure()`. See [Sage Modular Symbols, integral Hecke matrix](https://doc.sagemath.org/html/en/reference/modsym/sage/modular/modsym/space.html) and [Sage's modular_symbol_space(E,+1,GF(p))](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_modular_symbols.html) (the latter is a *separate* mod-p space and must not be automatically conflated with integral-lattice reduction).

Let
\[
M^+_{\mathbf Z}= \text{Sage's finite integral Hecke lattice
  in weight-2, sign-plus level-389 modular symbols}.
\]
It is free of finite rank \(d\). For each prime \(\ell\nmid389\) let \(A_\ell=T_\ell-a_\ell(E)\in\mathrm{Mat}_d(\mathbf Z)\). Stack a finite list \(\ell_1,\ldots,\ell_t\) into an exact integer matrix
\[
A=\begin{bmatrix}A_{\ell_1}\\A_{\ell_2}\\\vdots\\A_{\ell_t}\end{bmatrix}
\in\mathrm{Mat}_{td\times d}(\mathbf Z).
\]
The characteristic-zero E-eigensymbol line is known to have dimension **1**, so by adding sufficiently many Hecke operators the exact rank of A over Q becomes \(d-1\). This rank equality is explicitly **checked rather than assumed** by the script.

### Exact linear-algebra theorem, requiring only one integer minor

Assume the arithmetic program has certified \(\operatorname{rank}_{\mathbf Q}(A)=d-1\). Let \(\Delta\in\mathbf Z\setminus\{0\}\) be the determinant of **any** nonzero \((d-1)\times(d-1)\) minor of A and \(C_{\mathrm{Hecke}}=|\Delta|\).

**Theorem (fully p-uniform, elementary):**
\[
\boxed{
\forall p\nmid C_{\mathrm{Hecke}},\quad
\dim_{\mathbf F_p}\ker(A\bmod p)=1.
}
\]
**Proof.** The selected integer minor remains invertible modulo such p, so \(\operatorname{rank}_{\mathbf F_p}(A)\ge d-1\). Since \(\operatorname{rank}_{\mathbf Q}(A)=d-1\), there exists a primitive integral nonzero \(v\in\ker_{\mathbf Z}(A)\), found by clearing denominators of a rational kernel generator then dividing the coordinate gcd. Because \(v\) is primitive, \(v\bmod p\ne0\) at *every p*. It is in the mod-p kernel, so \(\operatorname{rank}_{\mathbf F_p}(A)\le d-1\). Both inequalities give rank d−1 and kernel dimension 1. QED.

This does **not** require a full Smith normal form, rational p-adic L-function, or any assumption on Sha. The set of exceptional primes for **this fixed lattice-Hecke system** is contained in the finitely many divisors of C. The program can pick the pivot rows/columns from the reduction mod 5 when its rank is d−1, yielding a single \(\Delta\) **coprime to 5** and an immediate p5 instance; otherwise it reports that p5 is not certified by that minor.

### The essential distinction from the actual Sha bound

**\(C_{\mathrm{Hecke}}\) is not \(C_{\Sha}\).** It controls a *linear eigensymbol congruence* inside a fixed finite-dimensional integral Hecke lattice. It does not bound the degree-2 coefficient \(\widetilde\delta_{q_1q_2}\) as \(q_1,q_2\) vary with p, even if the eigensymbol is **unique**. A unique nonzero eigenline may be annihilated by a specific weighted two-prime functional; the earlier weighted-moment counterexamples already illustrate this logical distinction.

Furthermore, an integral lattice in the *characteristic-zero* modular-symbol space can differ by a finite torsion/base-change defect from the full directly defined mod-p modular-symbol module. The theorem as proved here is **about the specified integral lattice and its reduction**. To infer all facts about the full mod-p modular symbols without conditions, those base-change factors must be independently checked. The script deliberately does NOT claim such a comparison.

The new [Sage source and proof-producing integer-minor exporter](../verification/bsd389_integral_hecke_eigenline_uniform_minor.py) uses the documented `integral_hecke_matrix(ell)`, stacks operators and checks rank, finds the primitive integral kernel generator, selects a nonzero determinant and emits a **canonical SHA256-pinned report** with chosen row/column indices and a few independent mod-p ranks. Neither the numerical determinant nor its factorization is known before the user's run.

## III. Decision and next bridge

The most productive sequence is now:
1. **Finish the four-cusp \(T_2\) test** on the true E symbol with Sage+eclib; this validates that marginal-invisible 8-term errors are seen by a full Hecke operator.
2. **Construct the actual fixed integer \(C_{\mathrm{Hecke}}\)** in the level-389 integral Manin lattice and certify kernel dimension 1 outside its prime factors. This gives a **real** global integer derived from a finite arithmetic calculation without assuming Sha.
3. Study a genuinely integral **two-auxiliary degree-(1,1) derivative/eigensymbol regulator** functional and prove it is nonzero for some varying pair under these uniquely normalized Hecke-eigenline constraints. The missing step is **not** equivalent to "uniqueness of eigensymbol" and may require an Euler/Kolyvagin/Selmer comparison.
4. Even an all-p rank-two Kurihara theorem would settle the relevant p-primary Sha obstruction (under Kim's hypotheses) **not automatically the exact complex BSD leading-term formula**.

**Current verdict:** The exact non-marginal \(T_2\) algebra is established, the p-uniform integer-minor theorem is proved, the actual integer computation has **not** been performed by the user, and both Sha finiteness and complex strong BSD remain UNPROVED.
