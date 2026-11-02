# The integral Hecke eigensymbol of 389a1 is rigid at **EVERY ODD rational prime**: D(T₂,T₃)=2

**November 2, 2026. Status: genuine user-executed exact arithmetic plus an elementary all-prime Smith theorem.** The result holds in the explicitly selected Sage integral, weight-two, sign-plus, level-389 modular-symbol lattice. It is **NOT** a theorem on the true elliptic Selmer \(\operatorname{Fitt}_2\), \(\Sha\), two-prime Kurihara numbers, or strong complex BSD. It also does **NOT** automatically identify the reduction of this integral lattice with the entire modular-symbol space defined directly over \(\mathbf F_2\).

## I. Real user-source data (all outputs actually obtained)

The user ran [the integral Smith program](../verification/bsd389_hecke_smith_all_prime_exception_refinement.py) with `--max-operators 3`. It authenticated the earlier integral-operator source JSON hash
`afccd10890e7c24f591f828576e78f901de7ba83b46fe17a7582567233297c64`,
reconstructed a 32×32 minor of determinant 29000 for \(T_2+2I\), and checked the p5/7/107 baseline ranks. Its full actual output is archived [here](../results/bsd389_integral_hecke_smith_2_3_5_USER_PASS_2026-11-02.md).

Let \(M_{\mathbf Z}^+\) denote the rank-33 lattice `ModularSymbols(389,2,sign=+1,base_ring=QQ).integral_structure()\). For each good prime \(\ell\), define \(A_\ell=T_\ell-a_\ell(389a1)I\in\mathrm{Mat}_{33}(\mathbf Z)\). In particular \(a_2=-2,a_3=-2,a_5=-3\).

The **user's exact Smith computations** prove:

| Stacked constraints | Number of rows | QQ rank | GCD of all rank-32 minors | Mod-2 rank | Mod-5 rank | Mod-29 rank |
|---|---:|---:|---:|---:|---:|---:|
| \(A_2\) | 33 | 32 | \(14500=2^2\cdot5^3\cdot29\) | 31 | 29 | 31 |
| \(A_2;A_3\) | 66 | 32 | **\(2\)** | **31** | **32** | **32** |
| \(A_2;A_3;A_5\) | 99 | 32 | **\(2\)** | **31** | **32** | **32** |

The report is SHA256-pinned to
`86e79229d1c60d38ec59ecd8776c0c471716a1ffdf1098d46d58a8a59253f02a`
and stored on the user's machine at
`~/bsd389_hecke_smith_refinement.json`. The JSON has not been uploaded to this repository: we archive the genuine stdout, not an imaginary data attachment.

## II. Exact group-structure and **all-odd-prime theorem**

Set
\[
A=\begin{pmatrix}A_2\\A_3\end{pmatrix}
\in\mathrm{Mat}_{66\times33}(\mathbf Z).
\]

**Theorem 1 (integral cokernel).** The user-certified 32 nonzero Smith invariants of \(A\) have product exactly **2**. Each is a strictly positive integer, so **31 are 1 and one is 2**. The remaining Smith diagonal entry is zero, because \(A\) has rational rank 32. Hence
\[
\boxed{\operatorname{coker}(A^\mathsf{t}:\mathbf Z^{66}\to\mathbf Z^{33})
  \simeq\mathbf Z\oplus\mathbf Z/2\mathbf Z.}
\]

*Proof.* The structure theorem for finitely generated abelian groups and Smith normal form apply to \(A^\mathsf t\), whose nonzero invariant factors are the same 32 factors; one zero factor contributes the free \(\mathbf Z\). QED.

**Theorem 2 (uniform odd-prime rigidity).** For **every odd rational prime p**, including p=3,5,7,29,107,389 and every arbitrarily large p,
\[
\boxed{\dim_{\mathbf F_p}\ker(A\bmod p)=1.}
\]
At p=2 the kernel dimension is **2**.

*Proof.* Smith row and column changes are unimodular over \(\mathbf Z\), and hence remain invertible modulo every p. The single diagonal factor 2 is invertible modulo p precisely when p is odd. At odd p, rank(A modp)=32, leaving kernel dimension 1; at p2, rank=31 and kernel dimension 2. QED.

Thus the fixed **two-operator** Hecke system \(T_2+2I,\ T_3+2I\) has exactly one eigenvector line modulo **every odd prime**, over its specific *integral* lattice. This is a theorem for infinitely many primes from a single finite source computation; NO infinite scan or conjectural large-p extrapolation is involved.

**Important nuance:** "unique common kernel over the chosen integral lattice modulo p" is NOT synonymous with "the entire space of modular symbols constructed in characteristic p is one-dimensional." In particular sign-plus eigenspaces and 2-integral base change require care at p2.

## III. Entire congruence exception set from ANY extension: **only p=2 remains**

Add any further integer Hecke operators \(A_\ell\), provided **all share the same primitive integral E eigensymbol vector** as the authentic \(A_2,A_3\), and let
\[
B=\begin{pmatrix}A_2\\A_3\\A_{\ell_1}\\\vdots\end{pmatrix}
\]
be the larger stack. Its rational rank remains 32. Let \(D(B)\) be the product of its 32 nonzero Smith invariants, equivalently the gcd of all rank-32 maximal minors.

Because stacking adds rows while retaining the originals, any old rank-32 minor of A remains one of the rank-32 minors of B. Therefore
\[
\boxed{D(B)\mid D(A)=2.}
\]
In particular **no odd prime can EVER become an exception** after adding compatible Hecke constraints.

Here is an even sharper algorithmic consequence.

**Theorem 3 (ONE mod-2 rank test determines the EXACT full integer invariant).**
\[
\boxed{
D(B)=
\begin{cases}
1,&\operatorname{rank}_{\mathbf F_2}(B)=32,\\
2,&\operatorname{rank}_{\mathbf F_2}(B)=31.
\end{cases}}
\]
*Proof.* From \(D(B)\mid2\), it is either 1 or 2. By Smith theory, \(D(B)\) is even iff the reduction modulo2 loses rank relative to its rank 32 over Q. Therefore, modulo2 rank32 iff D=1, and rank31 iff D=2. No other mod2 rank is possible for a B containing A. QED.

This is extremely economical: **after the one genuine exact Smith certificate \(D(A)=2\), we need no further Smith normal forms**. The entire congruence problem reduces to an incremental **rank calculation over \(\mathbf F_2\)** for a handful of additional integer Hecke matrices.

The user run already says adding \(A_5\) leaves rank31 and D=2. We therefore propose \(A_7,A_{11},\ldots\), checking just mod2 rank. If any raises rank to32, the single finite calculation will certify
\[
\boxed{\operatorname{coker}(B^\mathsf t)\simeq\mathbf Z}
\]
and **common kernel dimension one modulo EVERY prime p**, including p2, in that lattice. If no tested operator raises rank, **no conclusion about ALL possible further operators or full characteristic-two modular symbols is drawn**.

## IV. Why the next bounded test is arithmetically meaningful

Sage's documented weight-2 level-389 Sturm bound is **65**:
[official Sage documentation, sturm_bound(389,2)=65](https://doc.sagemath.org/html/en/reference/modfrm/sage/modular/dims.html). The Sturm theorem states that \(T_1,\dots,T_{65}\) generate the corresponding cusp-form Hecke algebra as a \(\mathbf Z\)-module for trivial character:
[Sage arithmetic subgroup documentation](https://doc-gitlab.sagemath.org/html/en/reference/arithgroup/sage/modular/arithgroup/arithgroup_generic.html). The full level-389 modular-symbol lattice includes an Eisenstein component, however, so a test of good-prime \(T_\ell\) for \(\ell\le61\) **must not be silently promoted** to a complete statement about all mod2 Hecke operators on the full ambient lattice. A careful full modular-symbol base-change and bad-prime operator audit would still be needed for such a conclusion.

The new [light mod-2 scan script](../verification/bsd389_hecke_mod2_exception_targeted_scan.py) authenticates the user's SHA-pinned Smith report, checks its precisely recorded mod2 rank31 for \(T_2,T_3,T_5\), and then calculates the mod2 ranks of a progressively larger stack using only the actual Sage integral Hecke matrices. The universal D|2 theorem converts each mod2 rank into an **exact all-prime determinant** of the enlarged stack. The script saves a canonical SHA256-pinned JSON and stops early if rank32 is found. **Not yet executed by the user**.

## V. Strict separation from Birch–Swinnerton-Dyer

This result provides a genuine, clean, integral **Hecke eigenspace congruence theorem** for all odd primes with a single remaining mod2 exception. It **does not** compute, estimate, or bound
\[
\operatorname{Fitt}_{2,\mathbf Z_p}
 (\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee)
\quad\text{or}\quad
\Sha(E/\mathbf Q)[p^\infty].
\]
A 1-dimensional modp eigenspace does not imply that the specific **two-prime Kurihara** linear functional is nonzero on the authentic E eigensymbol, nor that a globally rational Euler/Kolyvagin class with the needed integral Fitting comparison exists.

Even if the last mod2 congruence exception is eliminated, this would **not prove Sha finite** or the separate exact complex BSD rank-two leading-term formula \(L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\#\Sha\).

**Operational conclusion:** Stop doing unnecessary Smith computations and very large two-prime modular-symbol searches. A modest F2-only run answers the final congruence-prime question for the chosen matrices; then the actual BSD research must move back to genuinely arithmetic *M11 / integral Selmer Fitt₂ comparison*, not conflate the congruence integer 2 with a Sha bound.

Related: [uniform Sha support issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8), [full strong BSD complex issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
