# BSD 389a1 — A Kurihara two-prime criterion uniform across reduction types (2026-11-08)

**Verdict:** a rigorous implication from Kim's Theorem 1.1 (preprint arXiv:2505.09121), including supersingular p, but **NOT** an all-prime theorem: the missing assertion is the uniform existence of two-prime nonzero witnesses. The exact complex BSD coefficient remains open. No old certificates rerun.

## Theorem (conditional on Kim's published statement and its hypotheses)

E: y²+y=x³+x²−2x, N=389, Δmin=+389, rank MW=rank analytic=2, torsion=1, Tamagawa product=1. Fix an odd p with *large Galois image* in the sense of Kim. Suppose there are distinct auxiliary primes q1,q2 with

- q_i ∤ 389p;
- q_i ≡1 (mod p);
- a_{q_i}(E)≡q_i+1 (mod p);

and the **minimally integrally normalized** Kurihara number δ̃_{q1q2} (Definition 2.4 in Kim) has **nonzero reduction modulo p**.

Then **Sha(E/Q)[p∞]=0**. This applies to ordinary and supersingular p alike, provided large image. A nonzero unrelated Jref/Manin checkpoint is not necessarily Kim's complete δ̃.

**Proof.** In Kim's notation ord(δ̃)=min{ν(n):δ̃_n≠0}. The sign of E is +1 and 2 is invertible modulo p, so the functional equation w(f)(−1)^ν(n)δ̃_n=δ̃_n kills odd ν(n). δ̃_1=0 since L(E,1)=0. Consequently ord(δ̃)≥2. A nonzero two-prime witness gives ord(δ̃)=2. In Kim's Theorem 1.1, Sel_{p∞}(E/Q) has divisible corank ord(δ̃)=2 and finite quotient length ∂^(2)(δ̃)−∂^(∞)(δ̃). A **unit** two-prime witness implies BOTH ∂^(2)=0 and ∂^(∞)=0. Thus Sel_{p∞}≅(Qp/Zp)^2, and as E(Q) has rank 2, Kummer makes the Sha quotient zero. QED.

This is much stronger than merely proving Sha[p∞] finite. It relies on a full pair witness and the large-image hypothesis at that p, not on the single-prime local Frobenius tests.

## Exact finite-field diagnostic

By completing the square, (2y+1)^2=4x³+4x²−8x+1 and therefore a_p=−Σ_{x∈Fp}(4x³+4x²−8x+1|p). Direct modular exponentiation gives:

- p=107: a_p=0; #E(Fp)=108; SUPERSINGULAR;
- p=599: a_p=0; #E(Fp)=600; SUPERSINGULAR;
- p=16231: a_p=128; #E(Fp)=16104; ORDINARY.

Elkies proved every E/Q has infinitely many supersingular primes (Invent. Math. 89 (1987)). Therefore the Castella good-ordinary theorem, even with classes proved nonzero at *every ordinary p*, would leave infinitely many primes unchecked; it cannot alone yield uniform finite support.

## Exact remaining global gate

A genuinely uniform result sufficient to kill all large-image Sha components is:

> For all sufficiently large primes p there exist admissible q1(p),q2(p) with δ̃_{q1(p)q2(p)} nonzero mod p.

Then Kim yields Sha[p∞]=0 for all such p. Finitely many excluded primes still require independent certificates (especially p=3).

No *fixed pair* (q1,q2) can prove this assertion, as its admissibility requires p|gcd(q1−1,q2−1), allowing only finitely many p. The proof must supply moving auxiliary primes or a new p-independent global annihilator.

The earlier p=107 2M native pilot remains PARTIAL_ONLY; it is not a witness. The archived p=16231 Jref data are not automatically Kurihara numbers without a proven full normalization/summation identity.

## The COMPLEX gate is distinct

The exact Mellin–Fricke series and degree-40 Faltings–Hriljac height determinant in PR #12 give two exact expressions, but their equality is not known:

L''(E,1)/2 = 2π Σ_{n≥1} a_n ∫_{1/√389}^∞ e^(−2πnt) log²(t√389)dt

and  Ω_E Reg_E=(Ω_E/1600)det[height_J(βP_i,βP_j)].

Kim's **discrete** Bloch–Kato Selmer formula does not prove the complex archimedean equality. An independent rank-two height/L'' theorem, or independent rationality/denominator bound for Q_E=(L''/2)/(Ω_E Reg_E), is still required.

## Sources

- Chan-Ho Kim, *The refined Tamagawa number conjectures for GL2*, arXiv:2505.09121, Theorem 1.1, Theorem 1.2 and Corollary 1.5: https://arxiv.org/pdf/2505.09121 , https://arxiv.org/abs/2505.09121 .
- Elkies, *The existence of infinitely many supersingular primes for every elliptic curve over Q*, Invent. Math. 89 (1987), 561–568.
- Existing PR #12 source: `paper/bsd389_DIRECT_GLOBAL_exact_Mellin_Lstar_uniform_Sha_two_gates_2026-11-06.md` and Faltings–Hriljac/modular-degree40 notes.

**No claim of global Sha finiteness, all-p witness existence, rationality of Q_E, or exact BSD.**
