# The extra mod-2 Hecke eigenvector survives **every T_n with n≤65** — without checking composite n

**2026-11-02 — exact new deduction from genuine user-run 18-prime scan, and a disciplined stopping rule.** The lattice here is the explicit rank-33 integral, sign-plus, weight-2, level-389 modular-symbol lattice provided by Sage. It is **NOT** the elliptic Selmer group, \(\Sha\), or the full directly defined characteristic-2 modular-symbol module.

## 1. Genuine arithmetic evidence

The user executed [`verification/bsd389_hecke_mod2_exception_targeted_scan.py`](../verification/bsd389_hecke_mod2_exception_targeted_scan.py) on Ubuntu with `--max-prime 61`. The script authenticated the **actual** previous Smith output via SHA256 `86e79229d1c60d38ec59ecd8776c0c471716a1ffdf1098d46d58a8a59253f02a`, checked the **same primitive global integer Hecke eigenvector**, and computed the mod-2 ranks for **all 18 primes \(\ell\le61\)**. Each has \(\operatorname{rank}_{\mathbf F_2}=31\) in the growing stack, kernel dimension **2**. It reported `D_{\mathrm{stack}}=2`, which is exact because the previously certified rank-32 Smith determinantal gcd for \(T_2+2I,T_3+2I\) is already 2.

The real user stdout is archived [verbatim](../results/bsd389_hecke_mod2_exception_prime_scan_USER_PASS_2026-11-02.md). Output JSON on the user's host has SHA256
`0e24d302d61882689fe6084e9ed7302ddc0b483096744dc047c7e6a523970cf5`.
No JSON content has been secretly read; the check is user-reported genuine execution.

Denote
\[
M=M^+_{\mathbf Z}\otimes\mathbf F_2,\qquad \dim_{\mathbf F_2}M=33,
\]
and let
\[
K=\bigcap_{\substack{\ell\le61\\ \ell\ {\rm prime}}}
\ker\big(T_\ell-a_\ell(E):M\to M\big).
\]
The latest user computation proves
\[
\boxed{\dim_{\mathbf F_2}K=2.}
\]
Since already \(\dim\ker(T_2-a_2(E),T_3-a_3(E))=2\) from the actual Smith D=2, the common kernel for **all 18** prime operators actually **equals the original 2-dimensional kernel** of the first two operators. The entire extra mod2 vector survives every tested good-prime eigenrelation.

## 2. Universal exact deduction: all composite Hecke operators n≤65 also preserve K

The standard weight-2, trivial-character **good-prime Hecke algebra** has the exact identities on modular symbols:
\[
T_{mn}=T_mT_n\quad((m,n)=1),
\]
\[
T_{\ell^r}=T_\ell T_{\ell^{r-1}}-\ell T_{\ell^{r-2}}
\quad(\ell\nmid389,\ r\ge2),
\quad T_1=I .
\]
These are integral identities, so they survive reduction modulo 2.
Primary references: [Magma, Hecke operators on modular symbols](https://docs.magma-maths.org/ModularArithmeticGeometry/ModularSymbols/operators.html) and [official Sage Hecke-module documentation](https://doc.sagemath.org/html/en/reference/hecke/sage/modular/hecke/module.html).

The normalized Fourier eigenvalues \(a_n(E)\) obey the **same** recurrences: \(a_{mn}=a_ma_n\) if \(\gcd(m,n)=1\), and \(a_{\ell^r}=a_\ell a_{\ell^{r-1}}-\ell a_{\ell^{r-2}}\) when \(\ell\nmid389\).

**Theorem.** For **every integer \(1\le n\le65\)** and \(v\in K\),
\[
\boxed{(T_n-a_n(E))v=0\quad\text{in }M.}
\]

**Proof.** Every prime factor of any \(n\le65\) is at most 61 (the largest prime \(\le65\)). All such prime operators have the prescribed eigenvalue on K by the 18-prime user check. Apply the prime-power Hecke recurrence by induction on the exponent \(r\) to see that each \(T_{\ell^r}\) acts on K as \(a_{\ell^r}(E)\); then apply coprime multiplicativity to the prime-power factorization \(n=\prod \ell_i^{r_i}\). All coefficients are integers and all \(n\le65\) are coprime to 389, so no bad-prime formula is needed. QED.

**Corollary.** The full stack of \(\{T_n-a_n(E)\}_{n=1}^{65}\) on this same integral lattice has **mod-2 kernel dimension exactly 2**: it contains the 2-dimensional K by the theorem, and it is contained in K because it includes the 18 prime operators. The rational rank of the enlarged stack is still 32 (the true primitive integer eigensymbol persists), so its exact rank-32 determinantal divisor remains **2**, by the previously established \(D_{\mathrm{stack}}\mid2\) and the rank loss modulo2.

This is an exact theorem, *not* a new numerically executed scan of composite indices.

## 3. The essential Sturm caveat: cusp algebra versus the ambient integral plus lattice

For level \(389\), weight \(2\), the classical Sturm bound is **65**; its theorem identifies a finite spanning set of the **cuspidal** Hecke algebra, as stated in [Sage's arithmetic subgroup documentation](https://passagemath.org/docs/10.8/html/en/reference/arithgroup/sage/modular/arithgroup/arithgroup_generic.html).

But the user's **rank-33 ambient sign-plus modular-symbol lattice** contains an Eisenstein component. Sage explicitly warns in the [ambient Hecke module `hecke_bound()` documentation](https://doc.sagemath.org/html/en/reference/hecke/sage/modular/hecke/ambient_module.html) that its default bound for **noncuspidal spaces is an unproven guess** and should not automatically be promoted to a theorem.

**Accordingly** we have proved that \(K\) persists under **all \(T_n\) for \(1\le n\le65\)**; we do **not** assert from this alone that it persists under every Hecke operator \(T_n\) at arbitrarily large index on the entire integral, noncuspidal module. A direct proof of such a global mod2 congruence would require an integral Hecke generation argument for this *whole* lattice, including its Eisenstein piece, or an explicit all-index congruence of Hecke algebra characters.

This caveat does **not** weaken the already certified odd-prime theorem: the two-operator Smith invariant \(D(T_2,T_3)=2\) proves, without Sturm, **one-dimensional kernel for every odd prime** on this chosen integral lattice.

## 4. Decision: stop pursuing p=2 for the uniform-Sha goal

The original research aim is a prime-uniform bound on the actual Tate–Shafarevich group of \(E=389a1\), not a Hecke-congruence invariant. The **p2-primary Sha component has an entirely separate existing descent line in the project**, and the Hecke mod2 congruence kernel (dimension 2) must **not** be interpreted as an element of \(\Sha[2]\).

There is **no mathematical need to eliminate 2 from the Hecke determinant** to obtain a useful all-but-finitely-many-p statement: \(D(T_2,T_3)=2\) already controls the chosen integral Hecke eigenspace at **every odd prime**. Further unbounded Hecke-operator scans would be redundant for this purpose.

**The remaining difficult arithmetic implication is untouched:**
\[
\text{unique primitive integral Hecke eigensymbol at odd p}
\quad\not\Longrightarrow\quad
\exists\text{ admissible }q_1,q_2:
\widetilde\delta_{q_1q_2}(E)\ne0\pmod p.
\]
Even genuine all-odd-prime eigenline uniqueness is weaker than a unit second-order Kurihara derivative, and neither proves an integral \(\operatorname{Fitt}_2(\operatorname{Sel}_{p^\infty}^\vee)\) unit. An independent **Euler/Kolyvagin/Selmer comparison** with field-extension norm relations, or another new arithmetic mechanism, remains necessary to prove the missing uniform Sha finite support. The complex leading-term equality of strong BSD is also independently unresolved.

**Status:** p2 eigenline phenomenon persists through the complete numerical Sturm index window; the Hecke congruence branch is **complete for every odd prime** and should be treated as a separate successful auxiliary result, not as BSD solved.

[Uniform Sha issue #8](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/8) · [strong BSD complex issue #9](https://github.com/jaknewman/bsd-389a1-p16231-computational-certificate/issues/9).
