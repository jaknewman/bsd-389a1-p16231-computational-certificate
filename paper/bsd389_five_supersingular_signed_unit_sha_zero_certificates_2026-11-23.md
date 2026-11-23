# 389a1 — five supersingular p-primary components eliminated by the quadratic signed-moment gate

**23 November 2026.** A new exact-arithmetic computation for E=389a1 at p=1049,2957,6661,8263, extending the previously authenticated p=599 C2=543. Each p^2 moment was **fully evaluated** by the assistant in an ECMAScript numerical isolate against the independently archived *integer* 390-dimensional Manin symbol. The implied Sha statements use the source-normalized Pollack-plus comparison and the published signed main conjecture; these are computer-assisted p-primary results subject to the same original modular-symbol provenance and independent mathematical review as the p599 proof. No single computation is a uniform all-prime statement.

The previous p599 Pollack-plus source-level proof is:
[bsd389_p599_Pollack_scalar_signed_unit_and_Sha_zero_proof_2026-11-23.md](bsd389_p599_Pollack_scalar_signed_unit_and_Sha_zero_proof_2026-11-23.md).

## 1. Five fully evaluated genuine modular-symbol moments

For p good supersingular (a_p=0), \(\gamma=1+p\), and \(a\) a unit modulo \(p^2\), write \(a\equiv\tau(a)\gamma^{j_2(a)}\) with \(\tau(a)\) Teichmüller. Define
\[
C_{k,p}=\sum_{a\in(\mathbb Z/p^2)^\times}
\binom{j_2(a)}{k}\,m_E^+(a/p^2)\pmod p,\qquad k=0,1,2.
\]
Using plus-symbol symmetry \(m(a/p^2)=m((p^2-a)/p^2)\), process only \(p(p-1)/2\) representatives. The input is the **same integer-valued level-389 Manin edge vector in all computations**; there is no p-dependent fitted symbol data.

Full exact runs:

| p | count p(p−1)/2 | a_p(E) | C0 mod p | C1 mod p | C2 mod p | Pollack-plus [T²] mod p | status |
|--:|--:|--:|--:|--:|--:|--:|:--|
| 599 | 179101 | 0 | 0 | 0 | 543 | 28 | unit |
| 1049 | 549676 | 0 | 0 | 0 | 202 | 948 | unit |
| 2957 | 4370446 | 0 | 0 | 0 | 410 | 2752 | unit |
| 6661 | 22181130 | 0 | 0 | 0 | 2995 | 1833 | unit |
| 8263 | 34134453 | 0 | 0 | 0 | 4734 | 5896 | unit |

A separate **exact Legendre-symbol point count** also confirms \(\#E(\mathbb F_p)=p+1\) for all five p (thus no p-local rational torsion). Each p is prime, good and supersingular, with full residual Galois image from the project's earlier surjectivity certificate.

For p2957 there are **two independent exponent algorithms** yielding the same \((C_0,C_1,C_2)=(0,0,410)\): the original Fermat-quotient modular power per a, and the new Teichmüller precomputation below. For p1049 the original Fermat quotient method was used; for p6661 and p8263 the new fast Teichmüller method was used. The complete p599 run was previously independently checked using the original eclib Sage table and the integer 390-Manin vector. The new ECMAScript loop was not an *independent source* for that 390-vector; it is independent code and exhaustively recomputes the sums.

## 2. New exact fast Teichmüller exponent lemma

Write \(a=r+pt\) with \(r\in\{1,\ldots,p-1\}\) and \(0\le t<p\). The Teichmüller lift of \(r\) modulo \(p^2\) is \(\tau_r=r^p\pmod{p^2}\). Thus \(\tau_r=r+p h_r\) for an integer \(h_r\pmod p\). Since
\[
\frac{a}{\tau_r}
=1+p(t-h_r)\tau_r^{-1}
\equiv 1+p(t-h_r)r^{-1}\pmod{p^2},
\]
while \((1+p)^j\equiv1+pj\pmod{p^2}\), the principal-unit exponent is
\[
\boxed{j_2(a)\equiv (t-h_r)r^{-1}\pmod p.}
\]
This is an **exact arithmetic identity for every odd p**, not a probabilistic shortcut. After precomputing the \((p-1)\) lifts \(r^p\bmod p^2\) and inverses \(r^{-1}\bmod p\), each of the \(p(p-1)/2\) symbols needs no modular exponentiation to obtain \(j_2(a)\). Multiple sample a were crosschecked against the original Fermat-quotient formula
\[
j_2(a)\equiv-\frac{a^{p-1}-1}{p}\pmod p.
\]

The same script reconstructs plus modular symbols using the authentic 390 integer Manin edges (continued-fraction unimodular decomposition) and performs the complete weighted sum. A reusable standalone Python implementation with the 390-entry input embedded was committed:
[verification/bsd389_supersingular_p2_signed_moments_exact.py](../verification/bsd389_supersingular_p2_signed_moments_exact.py).

## 3. Actual arithmetic implication, not a p-adic BSD conjecture

As proved in the preceding p599 source audit, Sage’s measure and Pollack’s decomposition imply, in Pollack’s own **plus** sign convention,
\[
[T^2]L_p^{+,P}\equiv-C_{2,p}/2\pmod p.
\]
The precise proof uses the elementary \(p^3\to p^2\) binomial summation, the \(\alpha\)-adic \(-1\) error bound for the finite n=3 distribution, and Pollack's half-logarithm value \(1/p\) at \(T=0\). The identity is source-sensitive but **p-independent for a_p=0** in the semistable curve setting.

Burungale–Skinner–Tian–Wan (arXiv:2409.01350v2, Theorem 1.3) prove \(\operatorname{char}_{\Lambda_p}X_p^+=(L_p^+)\); B. D. Kim (2013) proves no nonzero finite \(\Lambda_p\)-submodules of this signed Selmer dual. The base Mordell–Weil rank two injects into its \(\Gamma\)-invariant signed Selmer. An *actual* p-unit quadratic coefficient forces \(\operatorname{char}_{\Lambda_p}X_p^+=(T^2)\). The module-theoretic argument in the previous note then forces \(X_p^+\simeq\mathbb Z_p^2\) with trivial \(T\)-action and \(\Sha(E/\mathbb Q)[p^\infty]=0\), without assuming any BSD leading-term equality or prior finiteness of Sha.

Therefore, for the five p of §1, subject to the authentic computational normalizations,
\[
\boxed{
\Sha(E/\mathbb Q)[p^\infty]=0
\qquad\forall p\in\{599,1049,2957,6661,8263\}.
}
\]

This is a **finite-prime computer-assisted statement**. A nonzero quadratic moment for some p is a sufficient criterion and does not imply its nonvanishing for *all* p.

## 4. Updated finite-range inventory and the actual global challenge

Stein–Wuthrich Thm12.3 proves Sha[p∞]=0 for exactly 5003 good ordinary p>=5 below48859; archival p107 covers another good supersingular prime. Our five supersingular unit computations add five distinct good primes. Thus **5009** good p>=5 below48859 are controlled by the union of these sources.

Of 5021 good p>=5 in this interval, only these **12** remain outside that union:
\[
9397,\ 9551,\ 14633,\ 15101,\ 16231,\ 28591,\ 30671,\ 30869,\ 31799,\ 34781,\ 36263,\ 45161.
\]
The prime 389 is the sole bad prime in the interval. Some of these, including 16231, have **separate existing finiteness results**; the above 12 are merely exceptions to the displayed zero-certificates, not proof of nonzero Sha.

**Global BSD remains OPEN.** Even if all 12 finite exceptions and bad 389 were controlled, infinitely many p>=48859 would remain. Uniform prime-support control for all large p, and the **exact** complex equality \(L''(E,1)/2=\Omega_E\operatorname{Reg}_E\#\Sha\), require new input and are not inferred by our five p-specific unit computations.

## References

1. Stein–Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory* (2013), Theorem 12.3: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf
2. Pollack, *On the p-adic L-function of a modular form at a supersingular prime* (2003): https://math.bu.edu/people/rpollack/Papers/On_the_padic_Lfunction_of_a_modular_form_at_a_ss_prime.pdf
3. Burungale–Skinner–Tian–Wan, *Zeta elements for elliptic curves and applications* (2024), Theorem 1.3: https://arxiv.org/pdf/2409.01350
4. B. D. Kim, *The plus/minus Selmer groups for supersingular primes* (2013), Theorem 1.1: https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/plusminus-selmer-groups-for-supersingular-primes/7AD9B7AB53A73F23F8E78F78488FA75C
