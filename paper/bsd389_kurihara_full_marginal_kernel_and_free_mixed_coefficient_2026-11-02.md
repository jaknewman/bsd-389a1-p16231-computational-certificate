# An eight-term exact obstruction: even the **FULL** Hecke marginals leave the mixed Kurihara coefficient arbitrary

**2026-11-02. Theorem, self-contained algebraic proof.** This substantially sharpens the user's p5 verified full-mixed-rank synthetic counterexample. It shows that **exact knowledge of both entire one-variable marginal group-ring elements, not merely their first 2–3 coefficients, plus complete sign-plus symmetry, cannot algebraically constrain the mixed coefficient** \(\widetilde\delta_{q_1q_2}\) at all. This is a theorem on a *synthetic group-ring perturbation*, **not** a valid construction of new modular eigenforms or a proof of BSD/Sha finiteness.

## 1. Genuine user-reproduced reference result (2026-11-02)

The user ran `verification/bsd389_p5_maximal_mixed_rank_zero_kurihara_toy.py` on Ubuntu. All lines passed:
```text
P5_TOY_SIGN_PLUS_AND_UNIT_SAMPLE_PASS f_1_1 4 entries 2400
P5_TOY_ALL_FIVE_HECKE_MARGINAL_JETS_ZERO_PASS M00_M10_M20_M01_M02 [0, 0, 0, 0, 0]
P5_TOY_MIXED_ANCHORED_MATRIX_MAXIMAL_RANK_PASS rank 39 max 39
P5_TOY_FULL_RANK_AND_ALL_PURE_JETS_YET_M11_ZERO_PASS actual_M11 0 direct_mixed_contraction 0 unit_sample 4
BOUNDARY_SYNTHETIC_FUNCTION_NOT_REAL_EIGENSYMBOL_OR_SHA
```
[Verbatim user-run PASS](../results/bsd389_p5_maximal_mixed_rank_zero_kurihara_toy_USER_PASS_2026-11-02.md). It shows that even **maximum anchored mixed rank 39/39**, a unit sample, sign-plus symmetry and every Hecke-forced low/pure moment can coexist with \(M_{11}=0\).

The genuine E=389a1 distribution over the same 40×60 grid had rank 39/39 but \(M_{11}=4\bmod5\) [in the separately executed Sage/eclib script](../results/bsd389_p5_real_kurihara_mixed_jet_SAGE_PASS_2026-11-01.md). This is strictly about the p5 comparison; no universal p conclusion follows.

## 2. Universal exact group-ring theorem (valid every odd p, suitable even group orders)

Let \(p\) be an odd prime. Choose **any even integers** \(h_1,h_2\ge4\), e.g. \(h_i=q_i-1\) for odd auxiliary primes \(q_i\equiv1\pmod p\). Work over
\[
R_p=\mathbf F_p[X,Y]/(X^{h_1}-1,\ Y^{h_2}-1).
\]
Put \(s=X^{h_1/2}Y^{h_2/2}\in R_p\), so \(s^2=1\).
The sign-plus eigenspace is
\[
R_p^+=\{F\in R_p:sF=F\}.
\]
Define **one explicit element, with only eight terms**:
\[
\boxed{
H=(1+s)(1-X)(1-Y)\ \in R_p.}\tag{1}
\]
As \(h_i>2\), expanding (1) yields eight distinct signed monomials (coefficients ±1), hence \(H\ne0\) for any p.

### Theorem (all three properties hold exactly)

**(A) Sign-plus invariance:** \(sH=s(1+s)(1-X)(1-Y)=(s+s^2)(1-X)(1-Y)=H\), since \(s^2=1\).

**(B) BOTH COMPLETE one-variable marginals vanish identically:**
\[
\boxed{H(X,1)=H(1,Y)=0\in R_p,}\tag{2}
\]
because (1) contains the product \((1-X)(1-Y)\).
This is **much stronger** than each marginal lying in an augmentation ideal cubed and stronger than the five low/pure Taylor coefficient vanishings proved from Hecke for the genuine E eigensymbol. Consequently if the actual \(\Theta_E\) satisfies exact Hecke marginal formulas involving its fixed one-prime theta functions, then the *abstract* replacement \(\Theta_E+tH\) satisfies **those same entire marginal formulas** for every t∈Fp. (It may violate other full Hecke and Manin relations: we never claim it is another valid elliptic modular symbol.)

**(C) Its weighted mixed (1,1) Taylor coefficient is an invertible scalar:**
\[
\boxed{[TU]H(1+T,1+U)=2\in\mathbf F_p^\times.}\tag{3}
\]
Indeed \((1-X)(1-Y)\) becomes \(TU\), while \((1+s)\) has constant term \(1+1=2\). Thus coefficient TU equals 2 exactly, regardless of h1,h2, and is a unit at every odd p.

### Exact free mixed-coefficient corollary

Given **ANY** sign-plus invariant \(\Theta\in R_p^+\) and **ANY target** \(d\in\mathbf F_p\), put \(m=[TU]\Theta(1+T,1+U)\) and
\[
\boxed{
\Theta_d=\Theta+\frac{d-m}{2}H.}\tag{4}
\]
Then:
\[
s\Theta_d=\Theta_d,\qquad
\Theta_d(X,1)=\Theta(X,1),\quad
\Theta_d(1,Y)=\Theta(1,Y),
\]
but
\[
\boxed{[TU]\Theta_d(1+T,1+U)=d.}
\]
This proof shows that **even knowing the FULL Hecke-predicted two marginals at each conductor leaves \(M_{11}\) completely undetermined** in the unrestricted sign-plus group-ring class. Nonvanishing must come from **additional arithmetic constraints linking the actual E-eigenline and distributions across levels**, not from any marginal identity whatsoever.

This also proves the p5 local \((a_{41},a_{61},d_1,d_2)\) audit, even enhanced to exact knowledge of \(\theta_{41}\) and \(\theta_{61}\), cannot on its own force \(M_{11}=4\); the independent real E symbol computation carries essential information.

## 3. Canonical eight-term sparse CRT support, verified with no huge arrays

In the exponent coordinates \(0\le k<h_1,\ 0\le\ell<h_2\), formula (1) has coefficients
\[
\begin{aligned}
H=\sum_{\epsilon=0}^1\bigl(
&X^{\epsilon h_1/2}Y^{\epsilon h_2/2}
-X^{1+\epsilon h_1/2}Y^{\epsilon h_2/2}\\
&-X^{\epsilon h_1/2}Y^{1+\epsilon h_2/2}
+X^{1+\epsilon h_1/2}Y^{1+\epsilon h_2/2}
\bigr).
\end{aligned}
\]
In particular, at the user's known auxiliary pairs p5/(41,61), p7/(113,673), p107/(369793,383917), **only eight cells** are needed to validate both full marginals zero and \([TU]H=2\). The standard-library [small checker](../verification/bsd389_two_prime_full_marginal_kernel_8term.py) is published; at note creation it is **not yet user-run**, so no PASS is attributed to the user's machine. The universal theorem is algebraic and does **not** rely on running that script.

## 4. Sharpening the correct remaining BSD proof obligation

The previous step proved that **a unit cusp, five low-jet zero coefficients and even full mixed rank** do not force the mixed coefficient. This theorem removes **all** ambiguity about marginal strengthening: *no further amount of data about the two single-variable marginals alone can determine the mixed Kurihara coefficient*, because H lies in their common kernel while its mixed derivative is a p-unit.

This says **nothing** about the \(\mathbf F_p\)-subspace of true Hecke eigensymbols satisfying **all** modular Manin relations, Hecke eigenrelations, boundary/cuspidality, distribution across conductors and the norm relations of Euler/Kolyvagin systems. It would be mathematically incorrect to conclude that an arbitrary \(\Theta+tH\) remains a true E modular eigen-symbol. Precisely these global constraints are where a successful proof must work.

### Exact formulation for next theorem candidate

Let \(\mathscr S_{E,p}^{(2)}\) denote **the rigorously specified** \(\mathbf F_p\)-subspace (or module with affine constraints) of distributions at n=q1q2 that arise from the **same** E-eigenform via *all* Manin and full Hecke relations and compatible conductor-normalized maps; this subspace must be defined before claiming its structure.

Then the pending problem is to prove that for each p outside a fixed finite set **there exists some admissible pair** such that the mixed functional
\[
L_{q_1,q_2,p}(\Theta)
=[TU]\Theta(1+T,1+U)
\]
is nonzero on the *specific canonical E-symbol class*, not merely on a synthetic sign-plus group-ring vector. A different proof route would need an independently constructed global rational Euler/Kolyvagin Fitting comparison, whose existence is not inferred from the fixed \(-1\) cusp and whose p-integrality is proved uniformly.

At primes where Castella–Sano and Kim apply, the desired nonzero two-prime coefficient is a **Sha-triviality criterion**, not a consequence of the unrestricted nonvanishing theorem. The full Sha finiteness/support theorem, and separately the exact complex rank-two BSD leading-term formula, remain UNPROVED.

See [uniform Sha issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8), [strong BSD complex issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
