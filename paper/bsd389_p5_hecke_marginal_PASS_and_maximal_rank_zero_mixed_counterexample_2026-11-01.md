# Validated p=5 Hecke marginals — and a maximal-rank, Hecke-jet-compatible zero-mixed-moment obstruction

**Date:** 2026-11-01. **Main conclusion:** the genuine E=389a1 local p=5 Hecke audit is a user-executed **PASS**, consistent with the direct nonzero genuine Kurihara coefficient \(M_{11}=4\). Separately, a new **synthetic** 40×60 mod-5 distribution demonstrates that **even maximal anchored mixed rank 39/39, a p-unit value, sign-plus symmetry, and all five Hecke-forced lower/pure moments zero DO NOT imply \(M_{11}\ne0\)**. This is a sharp logical audit, not a counterexample to BSD or an eigenform theorem.

## 1. The exact authenticated local result

The user's independent Python audit of q1=41, q2=61 on the curve E: y²+y=x³+x²−2x, p=5 returned:

\`\`\`text
P5_HECKE_INDEPENDENT_POINTCOUNTS_PASS a41 -3 a61 -8
P5_HECKE_MARGINAL_GROUP_RING_FACTOR_JETS_PASS log61_mod41 34 log41_mod61 54 first (0, 0, 4) second (0, 0, 4)
P5_HECKE_PURE_QUADRATIC_MOMENTS_FORCED_ZERO_PASS M00 0 M10 0 M20 0 M01 0 M02 0
P5_MIXED_M11_HISTORICAL_USER_RUN 4 NOT_RECOMPUTED_BY_THIS_LOCAL_AUDIT
BOUNDARY_UNIVERSAL_HECKE_JET_STRUCTURE_NOT_UNIFORM_M11_NONVANISHING
\`\`\`

[Verbatim authenticated user-run log](../results/bsd389_p5_hecke_marginal_local_audit_USER_RUN_PASS_2026-11-01.md).

The local script independently computes a41, a61 via Fq point counts and logs d1=34, d2=54. Each modulo-5 factor \(a_{q_2}-(1+T)^d-(1+T)^{-d}\) has truncated jet \((0,0,4)\). The exact Hecke marginal theorem [proved separately](bsd389_kurihara_hecke_marginals_force_low_jets_2026-11-01.md) puts each one-prime theta into I, hence both two-prime marginals into I³. Therefore the genuine p5 direct coefficient \(M_{11}=4\) from the [distinct 2400-unit Sage/eclib run](../results/bsd389_p5_real_kurihara_mixed_jet_SAGE_PASS_2026-11-01.md) gives
\[
\boxed{\Theta_{2501}(1+T,1+U)\equiv4TU\bmod(5,(T,U)^3)}.
\]
The local factor script **never recomputed** \(M_{11}\), and its output clearly says so.

## 2. Even full mixed rank + all Hecke-forced jets do NOT imply a nonzero mixed coefficient

Set p=5, h1=40, h2=60. Work over F5 on the CRT exponent grid
\((k,\ell)\in\mathbf Z/40\times\mathbf Z/60\).

Define cyclic backward shifts
\(S_k g(k,\ell)=g(k-1,\ell)\) and
\(S_\ell g(k,\ell)=g(k,\ell-1)\).
Let
\[
D_k=1-S_k,\qquad D_\ell=1-S_\ell.
\]
Pick two functions \(g_1,g_2\) invariant under the simultaneous plus involution \((k,\ell)\mapsto(k+20,\ell+30)\), and form
\[
\boxed{f=D_k^3g_1+D_\ell^3g_2\in\mathbf F_5^{40\times60}.}
\tag{A}
\]
The shifts commute with this involution, so f is also sign-plus symmetric.

**The exact five Hecke jet zeros follow without any randomness.** For each \(\ell\), \(\sum_k\binom{k}{r}D_k^3g_1(k,\ell)=0\) in F5 for r=0,1,2: discrete summation by parts applies because h1=40 is a multiple of 5 and the polynomial weights are periodic modulo 5; their third backward finite difference is zero. The same holds with k/l exchanged for D_l³g2. Therefore
\[
M_{00}(f)=M_{10}(f)=M_{20}(f)=M_{01}(f)=M_{02}(f)=0.
\]
Indeed the two **whole marginals** satisfy
\[
\Theta_f(X,1)= (1-X)^3 H_1(X),\qquad
\Theta_f(1,Y)=(1-Y)^3 H_2(Y)
\]
in F5 group rings for appropriate H_i, because sums of differences telescope. This is at least as strong as the Hecke-derived \(I_i^3\) condition (but does not claim f is a Hecke eigen-symbol).

**More importantly, the mixed Kurihara coefficient itself vanishes identically for such f:**
\[
\begin{aligned}
M_{11}(D_k^3g_1)
&=\sum_{k,\ell}k\ell D_k^3g_1(k,\ell)=0,\\
M_{11}(D_\ell^3g_2)
&=\sum_{k,\ell}k\ell D_\ell^3g_2(k,\ell)=0,
\end{aligned}
\]
again because a third finite difference kills a linear weight. Thus **M11(f)=0**, despite potentially very nontrivial mixed variation.

**An explicit deterministic maximal-rank instance:** choose the first 20 rows of each \(g_i\) from the first byte of SHA256 strings \`A0:k:l\` and \`B0:k:l\`, reduced modulo 5; fill the other 20 by the sign-plus involution. The tiny source
[\`verification/bsd389_p5_maximal_mixed_rank_zero_kurihara_toy.py\`](../verification/bsd389_p5_maximal_mixed_rank_zero_kurihara_toy.py) carries out all construction and finite-field Gaussian elimination. Independent local calculations of the deterministic construction gave:
\[
\boxed{
f(1,1)=4\ne0,\quad
\mathrm{rank}_{\mathbf F_5}[\Delta_{0,0}f]=39
\text{ (the absolute maximum)},\quad
M_{11}(f)=0.
}
\]
All five pure/lower moments vanish and sign-plus symmetry holds exactly. The source **has been published but has not yet been run on the user's Ubuntu server**. These are about a **synthetic function**, not a genuine E modular-symbol distribution.

The direct E=389a1 p5 experiment and the synthetic maximal-rank toy now have the same favorable measurable structural properties, **except the crucial genuine \(M_{11}\) value**:
- Actual E: anchored mixed rank 39; mixed coefficient 4 mod5.
- Synthetic f: anchored mixed rank 39; mixed coefficient 0 mod5.

This makes the remaining proof obligation concrete: **the Hecke marginal relations, sign-plus symmetry, existence of a unit symbol and full mixed rank by themselves cannot rule out vanishing of the weighted mixed contraction.**

## 3. Precise next arithmetic theorem (still OPEN)

One needs information genuinely special to the **Hecke eigenform and its arithmetic field-extension distribution**, not merely the structural low-jet Hecke marginal congruences or matrix ranks. Specifically, one must construct/identify a p-integral arithmetic Euler/Kolyvagin derivative class or a global Selmer comparison whose unit leading coefficient forces
\(\exists q_1(p),q_2(p): M_{11}(E;q_1,q_2)\ne0\pmod p\)
for all p outside a finite explicit set, **without presupposing the desired Sha bound**.

For the good primes covered by Castella–Sano and Kim, this is equivalent to the rank-two \(p\)-primary Sha triviality target, and its uniform version is not settled by any of the finite computations or the above algebraic lemmas.

**Full BSD remains unproved:** the complete Sha finiteness/triviality and the exact complex leading-term identity are independent remaining obstacles.
