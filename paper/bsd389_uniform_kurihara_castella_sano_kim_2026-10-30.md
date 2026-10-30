# All-but-finitely-many Kurihara mod-p nonvanishing for 389a1, and the exact remaining rank-two criterion

**Date:** 2026-10-30. **Status:** theorem-level mathematical deduction from the exact hypotheses of a January 20, 2026 **preprint** by Francesc Castella–Takamichi Sano (Theorem B), Chan-Ho Kim's Theorem 1.8, Mazur's optimal Manin-constant result and Serre's open image theorem. **This is NOT a proof of finite Sha or a uniform two-prime Kurihara unit witness.** The theorem is a source-verified preprint statement; independent peer-review status has not been established. No large new computer calculation is claimed.

## 1. An overlooked uniform theorem: Castella–Sano, Theorem B

**Primary reference:** F. Castella and T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, preprint dated **January 20, 2026**, [author PDF](https://web.math.ucsb.edu/~castella/Kurihara.pdf), printed **page 3**, Theorem A, Corollary A and **Theorem B**; [arXiv 2601.14504](https://arxiv.org/abs/2601.14504).

Their Theorem B: For any non-CM elliptic curve E/Q and prime p>3 with **surjective E[p] Galois representation** and **optimal Manin constant prime to p**, the refined Kurihara conjecture
\[
\mathcal M_\infty(\delta)=\operatorname{ord}_p(\mathrm{Tam}_E)
\]
holds if either **(i)** p is of *good ordinary* reduction, or **(ii)** p is of *good supersingular* reduction and the conductor N is **squarefree**. This is proved in the preprint by Theorem A, equating refined Kurihara primitivity to Kato's Iwasawa main conjecture, and the known ordinary/supersingular IMC theorems cited there (Wan; Burungale–Castella–Skinner; Castella–Liu–Wan; Burungale–Skinner–Tian–Wan, per their bibliography). We use the theorem **as explicitly stated**, not stronger variants.

For E=389a1, model [0,1,1,-2,0], conductor N=389, N squarefree; **Tamagawa product 1**; p≠389 gives good reduction and for p≥5 either ordinary or supersingular. E is optimal in its isogeny class and **p^2 does not divide N**, so Mazur's result cited by Castella–Sano (printed page 2) ensures p does not divide the optimal Manin constant. Thus, for **EVERY p>3 with p≠389 and surjective residual Galois image**,
\[
\boxed{\mathcal M_\infty(\delta_p)=0.}
\]
By the definition \(\mathcal M_\infty=0\) (Corollary A on page 3), this implies **there exists some admissible squarefree n=n(p)** such that \(\delta_n\not\equiv0\pmod p\). The number of factors \(\nu(n)\) is **NOT bounded by two** in the theorem.

Non-CM check for the fixed curve: \(j(E)=112^3/389=1404928/389\notin\mathbf Z\), whereas rational CM j is an algebraic integer. By **Serre's open image theorem**, the representation \(E[p]\) is surjective for every p except finitely many. Combined with the preceding theorem, **the unrestricted Kurihara mod-p nonvanishing holds for every p outside a finite (not explicitly bounded here) exceptional set**. This is a genuinely all-but-finite mathematical result **independent of the chi53 norm-729 calculation** and it does not require p to split in any fixed imaginary quadratic field.

**This corrects the previous issue #8 target:** "for every p, find some admissible n with δ_n nonzero" is already established by the cited preprint (under explicit local hypotheses); only the **rank-two** condition \(\nu(n)=2\) is unresolved.

## 1 bis. The exceptional set is **explicit** for E389a1: Mazur's semistable surjectivity theorem

The general Serre open-image theorem in §1 is sufficient, but unnecessarily weak for this particular curve. **Mazur's theorem (1978, Theorem 4)** states:

> If \(E/\mathbf Q\) is **semistable** and \(p\ge11\) is prime, then \(\bar\rho_{E,p}\) is surjective.

This exact formulation is reproduced as **Theorem 2.1** in Grigorov–Jorza–Patrikis–Stein–Tarnita-Pătrașcu, *Computational Verification of the Birch and Swinnerton-Dyer Conjecture for Individual Elliptic Curves*, [source PDF §2.1.2, printed page 5](https://www.wstein.org/papers/bsdalg/bsdalg2.pdf), and in Mayle–Wang (2024) [*On the effective version of Serre's open image theorem*](https://doi.org/10.1112/blms.13002).

E389a1 has conductor \(N=389\) (prime) and minimal discriminant \(\Delta=+389\) with \(v_{389}(\Delta)=1\). Its unique bad reduction is **multiplicative**, so E is **semistable**. Consequently, for **EVERY** prime \(p\ge11\), Mazur supplies the precise surjectivity required by Castella–Sano, with *no unknown surjectivity exceptions*. For \(p\ne389\), the reduction is good and either ordinary or supersingular, and \(N\) is squarefree; p-unit Manin constant and \(\mathrm{Tam}_E=1\) hold.

**Exact unconditional-uniform conclusion from the published/prerequisite theorems:**
\[
\boxed{\forall\text{ primes }p\ge11,\ p\ne389:
\qquad\mathcal M_\infty(\delta_p)=0.}
\]
Equivalently, **for every such p** there exists an admissible squarefree auxiliary conductor \(n(p)\) (not necessarily with 2 prime divisors) such that
\[
\boxed{\delta_{n(p)}\not\equiv0\pmod p.}
\]
This statement needs **no numerical search over p**, no input from \(\chi_{53}\), and no assumption of finiteness of Sha. Its excluded primes are explicitly \(\{2,3,5,7,389\}\) if one wants a statement covering *all* rational primes without importing the separate small-prime residual tests. The previously user-run surjectivity checks at \(p=5,7\), if accepted with their source certificates, extend the mod-p nonvanishing to every \(p\ge5\), \(p\ne389\). Theorem B does **not** directly apply at the multiplicative prime 389; Theorem A could apply if its own separate local Iwasawa main-conjecture hypothesis were established there.

**Crucial logical boundary:** This is uniform **unrestricted-degree** Kurihara nonvanishing, NOT the sought uniform **two-prime** nonvanishing and NOT a finite-support bound on Sha.

---

## 2. Kim's exact Selmer structure refines this to a prime-by-prime trichotomy

**Primary reference:** C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, [arXiv:2203.12159v6 PDF](https://arxiv.org/pdf/2203.12159), printed **page 7**, Theorem **1.8 (1)–(3)**, and page 6 definitions.

For a good p satisfying the above hypotheses, the nontrivial family \(\{\delta_n\}\) has
\[
\rho_p:=\operatorname{ord}(\delta)
=\operatorname{corank}_{\mathbf Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbf Q)
\]
and, writing \(m_i(p)=\partial^{(i)}(\delta)\) for the minimum p-adic valuation among \(\delta_n\) with **exactly i** distinct admissible auxiliary prime divisors,
\[
\operatorname{length}_{\mathbf Z_p}
\left(\operatorname{Sel}_{p^\infty}/\operatorname{Sel}_{p^\infty,\mathrm{div}}\right)
=m_{\rho_p}(p)-m_\infty(p).
\]
For our E, **m∞(p)=0** by Castella–Sano and the Tamagawa product 1. By certified Mordell–Weil rank 2 and the exact Kummer injection, **ρ_p≥2**.

Set \(m_2(p):=\partial^{(2)}(\delta)\in\mathbf Z_{\ge0}\cup\{\infty\}\), using **Kim's exact valuation of a residue modulo I_n**, not the valuation of an arbitrary integer lift to an unspecified modulus. Then:

- **m2(p)=0.** There exists n=q1q2 for which \(\delta_n\) is a unit mod p. Hence \(\rho_p\le2\) and thus \(\rho_p=2\). The nondivisible Selmer length is \(0-0=0\), so Selmer is cofree of corank 2. The rank-2 Kummer subgroup fills its maximal divisible subgroup and yields
  \[
  \boxed{\Sha(E/\mathbf Q)[p^\infty]=0.}
  \]

- **0<m2(p)<∞.** Some two-prime Kurihara number is nonzero modulo its defining I_n but all are divisible by p. Then \(\rho_p=2\) and \(\operatorname{length}\mathrm{Sel}_{p^\infty}/\mathrm{div}=m_2(p)\). The rank-two Kummer subgroup again fills the divisible part, so \(\Sha(E/\mathbf Q)[p^\infty]\) is finite of **order \(p^{m_2(p)}\)** (indeed its order is a square for p odd, consistent with the paired cyclic factors in Kim's theorem).

- **m2(p)=∞.** No two-prime \(\delta_n\) is nonzero in its defining residue ring. Thus \(\rho_p>2\) (by rank lower bound and Kim's equality), and the Kummer quotient \(\Sha[p^\infty]\) has a **nontrivial divisible \((\mathbf Q_p/\mathbf Z_p)^{\rho_p-2}\)** component; it is infinite. This is an exact classification, *assuming the two cited theorem statements*.

Therefore, for these **good p with surjective E[p]**,
\[
\boxed{
\Sha(E/\mathbf Q)[p^\infty]=0
\iff
\exists q_1\neq q_2 \text{ p-admissible with }
\delta_{q_1q_2}\not\equiv0\pmod p .
}
\]

**Warning:** "there exists at least one n of arbitrary length with δ_n nonzero mod p" now follows from Castella–Sano, but it **does not imply** m2(p)=0. Inferring the two-prime assertion from the unrestricted theorem would be equivalent to assuming the target Sha[p]-triviality. In particular, no fixed integer \`C=729\` has been proved to bound support of Sha.

## 3. Connection to verified historical calculations and the next real route

Historical user-executed p=107 data: n=369793·383917, \(\delta_n=34\pmod{107}\) with genuine complete 710-block archive SHA256 \`b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754\`, as traced in [p107/Kim theorem note](bsd389_p107_kim_two_prime_sha_criterion_2026-10-30.md). These supply **m2(107)=0**, not merely the unrestricted m∞(107)=0 theorem, hence the specific Sha107 result under the source/archive trust boundary. The separate supersingular p107 cyclotomic shortcut corroborates the p-adic regulator unit but is not needed here.

Previously proved exact group-theoretic Chebotarev lemma supplies infinitely many locally admissible auxiliary q at each surjective p. **The 2026 Castella–Sano theorem strengthens that** by proving at least one Kurihara number (at *possibly more than two q*) is a mod-p unit, without producing an explicit q or restricting the degree of n.

The remaining all-p Sha-support target can be stated sharply as:

> Construct a **single finite explicitly bounded set S** such that every p∉S with surjective residual image admits **a unit Kurihara number at exactly two auxiliary primes**; equivalently, prove m2(p)=0 for all p∉S using an additional arithmetic argument.

The conjunction "Serre + Castella–Sano + Kim" alone does **not** establish m2=0 for almost all p, Sha finite, or BSD. One needs to control the **minimum *degree* ν(n)** of a nonzero δ, not just the minimum *valuation* across all degrees.

An alternative, potentially more promising uniform route would build a single p-independent *integral determinant for the rank-two Selmer complex* whose p-local determinant controls the **two-prime** Kurihara Fitting ideal. Castella–Sano's **§2.2 determinantal formulation of Kato's IMC** is a concrete reference for the relevant complexes. But no p-independent determinant with a proved implication Sha[p]≠0⇒p|C has been constructed here. The hard step is p-uniform **integral** comparison, not Chebotarev or unrestricted Kato system nonvanishing.

**Scope:** As of this writing, the outstanding global finiteness of the full Sha of rank-two 389a1 is not established by these theorems or the numerical p-specific certificates. The paper is a January 2026 preprint, and further peer review of theorem hypotheses is welcome before publication-grade claims.
