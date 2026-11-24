# 389a1 — Exact two-prime strict Selmer identification with the genuine Sha[p^k], and a Poitou–Tate no-go for relaxed local tests

**2026-11-24. Theorem (conditional only on the already-proved large-p local Kummer–Chebotarev pair-existence theorem).** This is genuine finite-level global Selmer algebra, valid WITHOUT assuming Sha finite, Kato primitivity, any BSD leading-term equality, or any higher-rank Euler system. **No new computation is needed.**

## 1. Assumptions and notation

Let E/Q be 389a1, E(Q)=Z P⊕Z Q with no torsion and saturated basis P=(-1,1), Q=(0,-1). Fix a prime p sufficiently large for the previously proved full-image/Kummer–Chebotarev theorem, and an arbitrary k>=1. Write R_k=Z/p^k and V_k=E[p^k].

Choose *distinct* good primes q1,q2, different from p, with Frobenius conjugate to U_k=[[1,1],[0,1]] modulo p^k and with the prescribed Kummer translations (1,0), (0,1). Their existence for all large p,k is proved in paper/bsd389_uniform_deep_Kummer_Chebotarev_MW_local_basis_theorem_2026-11-24.md.

For i=1,2 define
\[
L_i=H_f^1(\mathbf Q_{q_i},V_k)
\simeq E(\mathbf Q_{q_i})/p^k E(\mathbf Q_{q_i})
\simeq E(\mathbf F_{q_i})/p^k E(\mathbf F_{q_i})
\simeq R_k.
\]
These are the *usual finite-level Kummer* local conditions, **not** the p-infinity local Kummer conditions (which vanish at primes away from p).

Let L=L1⊕L2≅R_k², let S=Sel_{p^k}(E/Q), and M=E(Q)/p^k E(Q)≅R_k². Kummer gives an exact sequence
\[
0\to M\xrightarrow{\kappa}S\xrightarrow{\pi}\Sha(E/\mathbf Q)[p^k]\to0.
\tag{1}
\]
By the Chebotarev choice, the simultaneous finite localization map \(\lambda:S\to L\) has the property that \(\lambda_M=\lambda\circ\kappa:M\to L\) is an **isomorphism** (indeed identity in chosen bases).

Set
\[
S^{00}(q_1,q_2):=\ker(\lambda)
\]
(the usual Selmer group made *strict at exactly the two good auxiliary places*, with ordinary conditions elsewhere).

## 2. Exact theorem: Sha[p^k] IS the strict Selmer kernel

**THEOREM.** For every such p,k and q1,q2 there is a natural, pair-dependent R_k-module isomorphism
\[
\boxed{S^{00}(q_1,q_2)\xrightarrow{\sim}\Sha(E/\mathbf Q)[p^k].}
\tag{2}
\]
Moreover the full finite-level Selmer splits **canonically relative to the selected pair**:
\[
\boxed{S=\kappa(M)\oplus S^{00}(q_1,q_2),}
\tag{3}
\]
with explicit projection
\[
\mathrm{pr}_{00}(s)
=s-\kappa\bigl(\lambda_M^{-1}(\lambda(s))\bigr).
\tag{4}
\]

**Proof.** Since \(\lambda_M\) is an isomorphism, the endomorphism \(\kappa\lambda_M^{-1}\lambda\) of S is a projector onto \(\kappa(M)\). Its complementary projector is (4), whose image is exactly \(\ker\lambda\). Thus (3) holds as R_k-modules without needing a splitting of (1) a priori. The restriction of \(\pi\) from (1) to \(\ker\lambda\) is injective because \(\ker\pi=\kappa(M)\) and \(\ker\lambda\cap\kappa(M)=0\); it is surjective because every class s∈S becomes an element of \(\ker\lambda\) after subtracting its unique MW localization correction (4). Hence (2). QED.

This is **stronger than a mod-p statement**: the integral group structure of every finite-level Sha[p^k] is completely identical to a finite strict Selmer group at two *explicitly choosable* rational primes.

The theorem does **not** say the strict Selmer group is zero, nor that calculating the local MW determinant has calculated it. All unknown Sha information is concentrated into the strict kernel.

## 3. Poitou–Tate theorem: relaxing exactly these two local conditions creates NO new global Selmer classes

Let \(S^{\mathrm{rel}}(q_1,q_2)\) be the Selmer group with **full H¹** at the two primes and ordinary finite Kummer conditions elsewhere. Since E[p^k] is self-dual by Weil pairing, the ordinary local conditions are self-orthogonal under Tate local duality.

At each good q_i ≠p, the local singular quotient
\[
H_s^1(\mathbf Q_{q_i},V_k)
=H^1(\mathbf Q_{q_i},V_k)/L_i
\]
is perfectly R_k-dual to L_i. Poitou–Tate change of Selmer local conditions gives
\[
0\to S\to S^{\rm rel}
  \longrightarrow H_s^1(\mathbf Q_{q_1},V_k)\oplus H_s^1(\mathbf Q_{q_2},V_k)
  \xrightarrow{\delta} S^\vee.
\tag{5}
\]
Local Tate orthogonality identifies \(\delta\) with the transpose of \(\lambda:S\to L\). Since \(\lambda\) is SURJECTIVE (already on M), \(\delta\) is INJECTIVE. Thus
\[
\boxed{S^{\rm rel}(q_1,q_2)=S.}
\tag{6}
\]

This is an exact, perhaps counterintuitive no-go: at MW-independent auxiliary primes the relaxed Selmer group does not grow *at all*, even if the true Sha is nonzero or infinite at p∞.

The local pairing in (5) is an R_k-perfect pairing; the argument does not depend on vector-space dimensions and remains valid at **every p^k depth**.

## 4. Parity makes a rank-one bound sufficient (but does not supply one)

Assume additionally the established p-parity theorem in the large-p tail for E389a1 (functional sign +1, algebraic MW rank2), or Kim's p-parity corollary. Since the p-primary Sha is cofinitely generated, it decomposes into a maximal divisible group (Qp/Zp)^c and a finite group F. The p-primary Cassels–Tate pairing on the finite quotient F is perfect alternating; therefore the number of p-primary cyclic factors of F is even.

Kim's p-parity formula gives
\[
2+c=\mathrm{corank}_{\mathbf Z_p}\mathrm{Sel}_{p^\infty}(E/\mathbf Q)\equiv0\pmod2,
\]
hence c is even. Therefore
\[
\boxed{\dim_{\mathbf F_p}S^{00}(q_1,q_2)[p]
=\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]\equiv0\pmod2}
\]
for k=1, where S^{00}=Sha[p] by (2). (The notation S^{00}[p] is redundant at level p; both modules are annihilated by p.)

Thus if an *independent arithmetic theorem* could bound \(\dim_{\mathbf F_p}S^{00}\le1\), then it would vanish and Sha[p∞]=0. This parity simplification is not itself an upper bound and is logically equivalent to the desired vanishing once such a bound is supplied.

## 5. Rigorous consequence: local MW independence cannot force a Kurihara unit

By Kim's Theorem 1.8 together with Castella–Sano 2026 Theorem B, at all sufficiently large p,
\[
\Sha(E/\mathbf Q)[p^\infty]=0
\iff\exists n=q'_1q'_2:\tilde\delta_n\not\equiv0\bmod p.
\tag{7}
\]
The chosen pair q1,q2 with invertible MW localization is guaranteed by Chebotarev for **all** large p even in the hypothetical case that \(\Sha[p]\ne0\). Indeed (2) shows that the extra global classes survive precisely as \(\ker\lambda\), which the MW matrix alone does not see. (6) shows that even allowing ramification at both primes introduces no further constraints capable of killing that kernel.

Thus there is **no formal implication**
\[
\det(\lambda_M)\in R_k^\times
\quad\Longrightarrow\quad
\tilde\delta_{q_1q_2}\bmod p\ne0.
\]
Any valid proof of such an implication FOR E389a1 would necessarily contain a new arithmetic theorem ruling out the strict Selmer kernel, and would essentially settle the missing global Sha obstruction. The Kato/Kurihara explicit reciprocity theorem gives genuine access to the relevant cohomology classes, but supplies no vanishing of this kernel simply from MW localization surjectivity.

**Correct new acceptance test:** produce a **genuine Kato-derived cohomological bound**
\[
\boxed{\dim_{\mathbf F_p} S^{00}(q_1,q_2)\le1}
\]
for the Chebotarev-selected pair uniformly in large p (parity then gives zero). Alternatively prove directly \(S^{00}=0\), or construct an independent all-p Fitt2 order bound. The required bound is not in the project or cited theorems.

This is an exact *Selmer formulation* and a proof of the strict/relaxed dichotomy, not a full BSD result. It rules out further useless searches for more MW-independent pairs: their existence has been settled universally.

**Sources:** Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.8, Corollary 1.12, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf ; Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B, https://web.math.ucsb.edu/~castella/Kurihara.pdf ; Poonen–Stoll, *The Cassels–Tate pairing on polarized abelian varieties*, https://arxiv.org/abs/math/9911267; Poitou–Tate comparison and exact Kummer sequence.
