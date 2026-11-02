# From the genuine T₂ integer minor 29,000 to *exact* Hecke-congruence exceptions via Smith invariants

**2026-11-02. Research state:** The full \(T_2\) Sage/eclib arithmetic and the level-389 integer modular-symbol computation were **actually run by the user**. A new exact, not conjectural deduction from that run shows that **the optimal Hecke-congruence integer for \(T_2\) has exactly \(5^3\) as its 5-part**. A separate Smith refinement script is published but **not yet user-run**. All claims concern a precisely chosen **integral modular-symbol Hecke lattice**, **NOT \(\Sha\)**, Selmer \(Fitt_2\), degree-two Kurihara unit for all p, or complete BSD.

## 1. Two genuine successful user runs, with rigorous boundaries

**First run, true \(T_2\) at four rational cusps:** [verbatim user transcript](../results/bsd389_T2_Hecke_and_integral_minor_29000_USER_PASS_2026-11-02.md). In both Sage and eclib, for \(r=1/2501\),
\[
(m(r),m(2r),m(r/2),m((r+1)/2))=(2,-2,-1,-1).
\]
Therefore \(-2m(r)-m(2r)-m(r/2)-m((r+1)/2)=-4+2+1+1=0\) **exactly**.

The deliberately synthetic eight-term perturbation extended by zero away from its eight \(2501\)-denominator cusps has \(H\)-values \((1,0,0,0)\), so adding \(3H\) produces an exact Hecke defect \(-6\equiv4\bmod5\). This **rejects that specific zero extension**, not all conceivable modularly compatible extensions.

**Second run, real integral modular-symbol Hecke matrix:** same [user transcript](../results/bsd389_T2_Hecke_and_integral_minor_29000_USER_PASS_2026-11-02.md). The level-389 sign-plus Sage integral modular-symbol lattice has rank **33**. The matrix
\[
A_2=T_2-a_2(E)I=T_2+2I\in\operatorname{Mat}_{33}(\mathbf Z)
\]
has rational rank **32** and an **integral primitive right-kernel generator** of 33 coordinates, 17 nonzero. One exact \(32\times32\) minor has absolute determinant
\[
\boxed{29000=2^3\cdot5^3\cdot29.}
\]
Direct reduction yielded \(\operatorname{rank}_{\mathbf F_5}(A_2)=29\), so \(\dim\ker=4\) at p5; and \(\operatorname{rank}_{\mathbf F_7}=\operatorname{rank}_{\mathbf F_{107}}=32\), so \(\dim\ker=1\) at 7,107. The canonical user-local baseline JSON has SHA256:
\[
\texttt{afccd10890e7c24f591f828576e78f901de7ba83b46fe17a7582567233297c64}.
\]
The source exporter: [`verification/bsd389_integral_hecke_eigenline_uniform_minor.py`](../verification/bsd389_integral_hecke_eigenline_uniform_minor.py).

**Immediate exact theorem, no new user computation:** if \(p\nmid 29000\), the chosen integral matrix \(A_2\bmod p\) has rank exactly 32, kernel dimension 1. The selected minor is **not automatically the best possible gcd over all maximal minors**.

## 2. New theorem: **exact 5-adic valuation of the gcd of all T₂ maximal minors**

Let \(d_1,\dots,d_{32}\in\mathbf Z_{>0}\) denote the 32 nonzero Smith elementary divisors of \(A_2\). Define
\[
D_2:=d_1d_2\cdots d_{32}
=\gcd\big\{|\det B|:B\text{ is a }32\times32\text{ minor of }A_2\big\},
\]
the exact \(32\)-nd determinantal divisor.

**Theorem (already forced by the *reported* successful user run):**
\[
\boxed{D_2=125\,u,\quad u\mid232=2^3\cdot29.}
\]
In particular \(\boxed{v_5(D_2)=3}\), the prime 5 is **genuinely a congruence-exception for \(T_2\) alone**, and the only *possible* other exceptional primes are 2 and 29.

**Proof:** One \(32\times32\) minor is 29000, hence \(D_2\mid29000\). The Smith diagonal reduction of \(A_2\bmod5\) has rank equal to the number of elementary divisors not divisible by 5. It has rank 29; therefore exactly \(32-29=3\) of the 32 nonzero Smith factors are divisible by 5, so \(v_5(D_2)\ge3\). But \(v_5(29000)=3\), so \(v_5(D_2)=3\) exactly. The quotient \(u=D_2/5^3\) divides \(2^3\cdot29=232\). QED.

Thus \(D_2\) is **exactly one of**
\[
125,\ 250,\ 500,\ 1000,\ 3625,\ 7250,\ 14500,\ 29000,
\]
and we can *decide which* by computing Smith elementary divisors of the already certified matrix — without scanning primes or the enormous Kurihara conductor. This is a genuinely stronger unconditional deduction, but only about the **fixed T₂ integral-lattice eigenspace**.

### Exact exceptional-prime criterion for any stacked system

For a fixed **integer** matrix A of rank r over \(\mathbf Q\), its nonzero Smith elementary divisors \(s_1,\dots,s_r\) satisfy:
\[
D(A)=\prod_{i=1}^rs_i,\qquad
\boxed{\operatorname{rank}_{\mathbf F_p}(A)=r\quad\Longleftrightarrow\quad p\nmid D(A).}
\]
Because Smith reduction uses unimodular integer row/column matrices, the characterization holds **simultaneously for every prime p**, not just sampled primes.

Now stack \(A_2, A_3, A_5, A_7,\ldots\), where \(A_\ell=T_\ell-a_\ell(E)I\) are calculated on **the same** integral modular-symbol lattice. Because the true E-eigenline is in each kernel, and \(A_2\) already has rational rank 32, the stacked matrix has rational rank **exactly 32** if every operator is consistent. Its determinantal divisor \(D_{\mathrm{stack}}\) **divides \(D_2\)** because stacking rows adds minors and cannot increase their gcd. In particular
\[
\boxed{D_{\mathrm{stack}}\mid D_2\mid29000.}
\]
**No new exceptional prime can ever appear** in a correctly constructed stack that already includes \(T_2+2I\). Additional Hecke operators may eliminate some of the three candidate primes \(2,5,29\). This is a rigorously p-uniform arithmetic reduction derived from an actual integer matrix, without assuming anything about \(\Sha\).

## 3. New proof-producing executable for the *optimal* Hecke congruence factor

The source [`verification/bsd389_hecke_smith_all_prime_exception_refinement.py`](../verification/bsd389_hecke_smith_all_prime_exception_refinement.py) is already committed but **not yet user-executed**. It:

- Authenticates the existing user-generated baseline canonical JSON via SHA256 `afccd10890e7c24f591f828576e78f901de7ba83b46fe17a7582567233297c64`.
- Reconstructs \(A_2\) on the documented Sage integral Hecke lattice; verifies the primitive integer eigenvector and recomputes the exact 29000 chosen minor, plus original p5/p7/p107 ranks.
- Stacks \(A_\ell=T_\ell-a_\ell(E)I\) for selected \(\ell=2,3,5,7,\ldots\), checking each \(\mathbf Z\)-matrix annihilates **the same primitive E-eigenvector**, to avoid accidentally changing bases or eigenspaces.
- Computes the **exact full Smith invariants** and their nonzero product \(D_{\mathrm{stack}}\), i.e. the gcd of all maximal minors, at each stage.
- Cross-checks the Smith-predicted ranks with independent finite-field matrix ranks at \(p=2,5,29,7,107\); verifies monotone divisibility and \(D_{\mathrm{stack}}\mid29000\). This covers **all possible new congruence exceptions** because no prime outside \(2,5,29\) can divide the global determinant.
- Saves a canonical SHA256-pinned JSON with the invariant factors, precise exception-prime list and the primitive 33-coordinate kernel vector.

**Suggested first quick execution:** `--max-operators 3` (operators \(T_2,T_3,T_5\)); then decide whether extending to 8 provides anything. Since the baseline T2 mod5 kernel has dimension 4, the new finite-field ranks show whether T3 or T5 cuts it to dimension 1. **We do not preclaim the refined integer \(D_{\mathrm{stack}}\) or that p5 will cease to be exceptional.**

The Sage documentation specifies the integral Hecke lattice API and differs from an arbitrary rational basis: [Sage modular-symbol integrality](https://doc.sagemath.org/html/en/reference/modsym/sage/modular/modsym/space.html). The [matrix elementary-divisors documentation](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_integer_dense.html) records the Smith invariant relationship, and notes that computing elementary divisors is faster than full Smith transformation matrices.

## 4. Why even D=1 would not prove Sha[p]=0 or complete BSD

Even if the new exact stacked integer is \(D=1\), proving **unique mod-p Hecke eigenline inside this chosen integral lattice for every prime p**, that is **not equivalent** to nonzero degree-two Kurihara coefficient \(M_{11}\) at **any** auxiliary conductor. A primitive eigenvector can be killed by a p-dependent weighted functional. Moreover, the completed \(\mathbf Z\)-lattice and its reduction need not coincide with the entire mod-p Manin-symbol cohomology without an integral base-change comparison.

The known \(p=5\) Selmer/Sha vanishing results from earlier independent descent are **not threatened by a four-dimensional kernel of T2 alone**: these are fundamentally different invariants. The integer \(\boxed{D_{\mathrm{stack}}\text{ is NOT }C_{\Sha}}\) remains essential.

To obtain full BSD we still need (i) global finiteness and/or identification of all p-primary \(\Sha\), and independently (ii) the exact complex leading term
\[
L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\#\Sha(E/\mathbf Q).
\]
Neither follows from the integral Hecke congruence calculation.

References: [uniform Sha support issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8) and [exact complex BSD issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
