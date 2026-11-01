# From the prime-uniform classical symbol to the **actual** mixed Mazur–Tate coefficient

**2026-11-01.** This note gives an exact theorem-level reformulation of two-prime Kurihara weights as a *bidegree (1,1) Taylor coefficient* in a finite group ring, a stronger precise limitation on what one-cusp primitivity can prove, and a reproducible **real E=389a1 p=5** test. **The new p=5 script HAS NOW BEEN USER-EXECUTED and ALL GATES PASSED**; see the post-execution update below. No uniform Sha or complete BSD result is claimed.

## 1. Exact coefficient-of-TU lemma

Let p>=5, and let q1,q2 be distinct auxiliary primes with p|(q_i−1). Put h_i=q_i−1 and fix primitive roots g_i of the cyclic groups G_i=(Z/q_iZ)^×. Via CRT, each pair (k,l) with 0<=k<h1 and 0<=l<h2 determines a unit a(k,l) modulo n=q1q2:
\[
a(k,l)\equiv g_1^k\pmod{q_1},\quad
a(k,l)\equiv g_2^l\pmod{q_2}.
\]
For any function f:G1×G2 -> F_p, define the group-ring element
\[
\Theta_f(X,Y)=\sum_{k=0}^{h_1-1}\sum_{\ell=0}^{h_2-1}
f(k,\ell)X^kY^\ell
\in \mathbf F_p[X,Y]/(X^{h_1}-1,Y^{h_2}-1).
\]
Since \((1+T)^{h_i}-1\) is divisible by \(T^2\) (because p|h_i), reducing modulo \((T^2,U^2)\) is well-defined independently of polynomial representative. Indeed, \((1+T)^{h_i}-1=h_iT+O(T^2)=O(T^2)\) modulo p.

The two-prime Kurihara functional is
\[
\begin{aligned}
L_{q_1,q_2,p}(f)
&=\sum_{k,\ell}(k\bmod p)(\ell\bmod p)\,f(k,\ell)\\
&=\boxed{[TU]\Theta_f(1+T,1+U).}
\end{aligned}
\]
**Proof:** the TU coefficient of \((1+T)^k(1+U)^\ell\) is exactly \(k\ell\) modulo p. This proof uses no conjectures and is valid even if the vector \(f\) has p-unit entries or is additively separable.

For the **actual elliptic curve**, set \(f_E(k,\ell)=m_E^+(a(k,\ell)/n)\bmod p\) with the same integral normalization as Castella–Sano/Kim. Then the right side is precisely the **mod p two-prime Kurihara number** \(\widetilde\delta_{q_1q_2}\) with the chosen roots and normalization.

**Change of primitive roots** \(g_1\mapsto g_1^{u_1}\), \(g_2\mapsto g_2^{u_2}\), where gcd(u_i,h_i)=1, multiplies the mixed coefficient by \((u_1u_2)^{-1}\bmod p\). This is a unit. Therefore **nonzero versus zero does not depend on primitive-root choices**; trying many root choices cannot solve an actual vanishing problem. This matters for the uniform strategy.

## 2. Even a nonzero mixed *rank* is insufficient: exact p-uniform counterexample

The earlier mixed finite-difference lemma shows \(L\) factors through the mixed quotient. One might hope that a nonzero mixed component of the E symbol would already imply \(L\ne0\). **This too is false at the level of general linear algebra.**

For every p>=5 and h_i divisible by p, define the concrete function
\[
f(k,\ell)=(k\bmod p)(\ell\bmod p).
\]
It has a **p-unit sample**, \(f(1,1)=1\), and for anchors (0,0) its mixed anchored difference is \(f\) itself:
\[
f(k,\ell)-f(k,0)-f(0,\ell)+f(0,0)=k\ell.
\]
It is nonzero and its mixed matrix over F_p has **rank exactly 1**. Nevertheless
\[
L_{q_1,q_2,p}(f)=
\biggl(\sum_{k=0}^{h_1-1}k^2\biggr)
\biggl(\sum_{\ell=0}^{h_2-1}\ell^2\biggr)=0\pmod p.
\]
Indeed, when p|h, each residue mod p occurs equally often, while \(\sum_{r\in F_p}r^2=0\) for p>=5. This remains compatible with sign-plus symmetry, because \((h_i/2)\equiv0\bmod p\) for q_i odd and p odd, so the simultaneous involution \((k,\ell)\mapsto(k+h_1/2,\ell+h_2/2)\) preserves f.

In other words, **even the combination "fixed unit sample + nonzero mixed variation + sign-plus symmetry" does NOT force a Kurihara witness**. It is the **specific contraction with the log-weight tensor**, not merely mixed rank, which must be nonzero on the real E eigensymbol.

This completely elementary obstruction can be checked for our historically used auxiliary pairs:
- p=5, q=(41,61), h=(40,60);
- p=7, q=(113,673), h=(112,672);
- p=107, q=(369793,383917), h=(369792,383916).

For contrast at p=5, the distinct *sign-plus symmetric* function supported on (1,1) and (21,31) has \(L=1+21\cdot31=652\equiv2\bmod5\), so the functional itself is nonzero. Both artificial functions are **not** the actual modular eigensymbol.

Independent [tiny pure-Python check](../verification/bsd389_kurihara_mixed_functional_obstruction.py), **not yet user-run**.

## 3. One inexpensive actual elliptic-curve pilot instead of a 71-billion-term restart

The user's earlier fully completed p=5 Kurihara certificate, with auxiliary primes \((41,61)\), computed \(\widetilde\delta_{2501}\equiv4\bmod5\) after an independently audited 390-Manin process. We now propose a **conceptually distinct implementation**, directly at denominator 2501.

The new [Sage direct mixed-jet pilot](../verification/bsd389_p5_kurihara_mixed_jet_direct.py):

1. Uses primitive roots (6 mod41, 2 mod61), which generate all units, and CRT.
2. Evaluates **1,200 exact eclib plus-symbols** at denominators 2501, one per simultaneous sign-plus orbit; fills all 2,400 CRT positions by the proven \(m^+(-r)=m^+(r)\).
3. Compares **24** representative rational symbols with Sage's independent implementation, not the eclib oracle.
4. Computes the four lowest Taylor coefficients \(M_{00},M_{10},M_{01},M_{11}\) of \(\Theta_{2501}(1+T,1+U)\). They are **unknown until real execution**.
5. Computes the mixed anchored finite-difference matrix rank in F5 (new structural observation) and verifies \([TU]\Theta\) equals the weighted mixed-difference contraction.
6. Changes both primitive roots and independently verifies that \(M_{11}\) scales by the predicted F5-unit.
7. Checks the historically reported result \(M_{11}=\widetilde\delta_{2501}=4\bmod5\).

**The new pilot HAS NOW PASSED** on the user's actual Sage Ubuntu server and tests the actual E eigensymbol and its two-prime variation, unlike the synthetic obstruction above. It validates the mixed-coefficient interpretation at p5 with an independent direct algorithm, **not** a proof that the analogous coefficient remains nonzero for all p.

## 3 bis. Actual user-run PASS and universal Hecke deduction of the *entire* quadratic jet

User terminal run [archived here](../results/bsd389_p5_real_kurihara_mixed_jet_SAGE_PASS_2026-11-01.md) reports:
```text
P5_ALL_2400_CRT_UNITS_SYMMETRIC_COMPLETE_PASS eclib_evaluations 1200 direct_independent_sage_samples 24
P5_THETA_LOWEST_MOMENTS M00 0 M10 0 M01 0 M11 4
P5_MIXED_ANCHORED_JET_PASS direct 4 difference 4 matrix_rank 39 nonzero_mixed_entries 1846
P5_PRIMITIVE_ROOT_CHANGE_UNIT_SCALING_PASS old 4 new 3 factor 2
P5_INDEPENDENT_DIRECT_KURIHARA_DELTA_MATCH_PASS p 5 n 2501 delta_mod_p 4
```
The anchored mixed difference matrix has 40 rows and 60 columns, the first row/column zero, so **rank 39 is the maximum mathematically possible**. The new direct \(\delta=4\) agrees with the historically exhaustive independent Kurihara calculation. All 24 independent Sage spot checks pass.

A new **universal Hecke marginal theorem**, proved from the exact modular-symbol relation (not experimental extrapolation), now shows substantially more than the four computed low bidegree-\((0,0),(1,0),(0,1),(1,1)\) moments. For every odd p≥5 and p-admissible pair,
\[
\bar\Theta_{q_1q_2}(X,1)
=(2-X^d-X^{-d})\,\bar\theta_{q_1}(X)
=-X^{-d}(X^d-1)^2\bar\theta_{q_1}(X)
\in (X-1)^3
\]
because \(\bar\theta_{q_1}(1)=(a_{q_1}-2)m(0)=0\pmod p\). The second marginal likewise lies in \((Y-1)^3\). Hence **\(M_{20}=M_{02}=0\pmod p\)** in addition to the three directly measured zero coefficients. Therefore the **full total-degree-2** Taylor jet for the actual p5 user run satisfies
\[
\boxed{
\Theta_{2501}(1+T,1+U)\equiv4TU\pmod{5,(T,U)^3}.
}
\]
The two pure-quadratic zeros are **theorem-derived**, not numerical outputs claimed to have been emitted by the original p5 script. [Complete universally quantified proof and conventions](bsd389_kurihara_hecke_marginals_force_low_jets_2026-11-01.md). [New small standalone point-count and marginal-factor audit](../verification/bsd389_p5_hecke_marginal_local_audit.py) is **published but not yet user-run**, and makes no new 2501-denominator symbol evaluations.

This shows **all other degree≤2 moments must vanish for EVERY admissible pair**, but it **does not force the single remaining coefficient \(M_{11}\) to be nonzero**. At p5 it is truly nonzero because of the independent run; that remains a p-specific fact.

---

## 4. Last arithmetic gap

The correct global conjectural implication would need some theorem controlling the bidegree-(1,1) coefficient of \(\Theta_{q_1q_2}\) for a *varying p-admissible pair* \((q_1(p),q_2(p))\), with p-integral period/Manin normalization. Under the good-prime hypotheses of Kim and the unrestricted nonvanishing theorem of Castella–Sano, **existence of a nonzero coefficient for some pair is equivalent to \(\Sha(E/Q)[p^\infty]=0\)**. It cannot be inferred from:
- a fixed \(-1\) classical modular-symbol sample;
- the integer gcd of a finite symbol table being 1;
- the mixed variation matrix merely having nonzero rank;
- changing primitive roots;
- Chebotarev's existence of basic admissible auxiliary primes;
- unrestricted-degree Kurihara nonvanishing.

A viable further theorem needs an **integral arithmetic Fitting/Euler-system comparison** that specifically forces the nonzero (1,1) coefficient at some conductor of degree two, without assuming a rank-two Sha bound.

References: [Castella–Sano, pp.2–3](https://web.math.ucsb.edu/~castella/Kurihara.pdf), [Kim Theorem 1.8, p.7](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf), [our independently audited one-cusp theorem](bsd389_fixed_rational_manin_Dg1_exact_certificate_and_limit_2026-11-01.md).
