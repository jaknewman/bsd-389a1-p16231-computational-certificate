# E389a1: two-prime Poitou–Tate relaxation rigidity and exact transverse-Selmer/Sha[p] identity

**Date:** 2026-11-13.
**Scope:** proved global-cohomological result under stated finite-local hypotheses. The theorem does **not** show vanishing of Sha at any new prime and does **not** prove BSD.

## 1. Setup and genuine arithmetic input

Let
$$E/\mathbf Q:\ y^2+y=x^3+x^2-2x,$$
and let $p\ge5$ be a rational prime. The certified Mordell–Weil group has rank two, no torsion, and integral basis $P=(-1,1)$, $Q=(0,-1)$.

Set $V=E[p]$ and let $\mathcal F$ denote the standard mod-p Selmer structure: at every place $v$ the local condition $L_v$ is the image of the Kummer map $E(\mathbf Q_v)/p\to H^1(\mathbf Q_v,V)$. These local conditions are self-annihilating under local Tate duality after identifying the Cartier dual $V^*(1)$ with $V$ through the Weil pairing.

Let $q_1,q_2$ be distinct good primes different from $p$ with one-dimensional finite conditions
$$L_i=L_{q_i}=E(\mathbf Q_{q_i})/p\simeq\mathbf F_p.$$
Assume the Mordell–Weil localization matrix
$$
A_p=
\begin{pmatrix}
\operatorname{loc}_{q_1}(P)&\operatorname{loc}_{q_1}(Q)\\
\operatorname{loc}_{q_2}(P)&\operatorname{loc}_{q_2}(Q)
\end{pmatrix}
$$
is invertible modulo $p$, relative to fixed bases of $L_i$. This is the entire arithmetic hypothesis.

Define $S=H^1_{\mathcal F}(\mathbf Q,V)$ (ordinary Selmer); $S_0$ by replacing $L_{q_i}$ with zero (strict at both); and $S_{\rm rel}$ by replacing $L_{q_i}$ with all $H^1(\mathbf Q_{q_i},V)$ (relaxed at both). Elsewhere the local conditions are unchanged.

## 2. Theorem 1: relaxation rigidity

**Under the hypotheses above:**
$$
\boxed{S_{\rm rel}=S.}\tag{R}
$$

**Direct proof.** Let $c\in S_{\rm rel}$. For every $s\in S$, the sum of local Tate pairings over all places is zero by global reciprocity:
$$
\sum_v\langle c_v,s_v\rangle_v=0.
$$
Outside $q_1,q_2$, both classes lie in their ordinary self-orthogonal Kummer conditions, so the terms vanish. At the two distinguished places,
$$
\langle c_{q_1},s_{q_1}\rangle_{q_1}
+\langle c_{q_2},s_{q_2}\rangle_{q_2}=0.
$$
The image of $S$ in $L_1\oplus L_2$ contains the localization of the two rational points $P,Q$, which is all of $L_1\oplus L_2$ because $A_p$ is invertible. Varying $s$ independently in the two coordinates shows $c_{q_i}\in L_i^\perp=L_i$ for both $i$. Thus $c$ also satisfies all the ordinary conditions and belongs to $S$. The reverse inclusion is tautological. QED.

**Exact Poitou–Tate sequence crosscheck.** The dual of the strict local condition $0$ is the full local $H^1$; the dual of the ordinary condition is itself. Mazur–Rubin, *Kolyvagin Systems*, Theorem 2.3.4, gives the five-term exact sequence
$$
0\longrightarrow S_0
\longrightarrow S
\xrightarrow{\lambda} L_1\oplus L_2
\longrightarrow S_{\rm rel}^{\vee}
\longrightarrow S^\vee
\longrightarrow0.
\tag{PT}
$$
Here $\vee$ is finite-dimensional $\mathbf F_p$ dual; the map into $S_{\rm rel}^\vee$ is the local Tate-duality map (not an invented map from Hecke symbols). Surjectivity of $\lambda$ forces the dual inclusion $S^\vee_{\rm rel}\to S^\vee$ to be an isomorphism, equivalent to (R). Primary-source theorem: https://www.nzdr.ru/data/media/biblio/kolxoz/M/MA/MAg/Mazur%20B.%2C%20Rubin%20K.%20Kolyvagin%20systems%20%28AMS%2C%202004%29%28ISBN%200821835122%29%28O%29%28102s%29_MAg_.pdf

## 3. Theorem 2: the transverse Selmer group is Sha[p]

Assume in addition $\dim_{\mathbf F_p}H^1(\mathbf Q_{q_i},V)=2$; this holds at the sample q_i below, for nontrivial unipotent mod-p Frobenius with $q_i\equiv1\pmod p$ and $\dim E(\mathbf F_{q_i})[p]=1$.

Choose **any** complementary local lines $L_i^{\rm tr}$ with
$$
H^1(\mathbf Q_{q_i},V)=L_i\oplus L_i^{\rm tr}.
$$
Let $S_{\rm tr}$ be the global Selmer group with these local lines replacing $L_i$ at $q_1,q_2$ (and ordinary conditions elsewhere). Then:
$$
\boxed{S_{\rm tr}=S_0\simeq\operatorname{Sha}(E/\mathbf Q)[p].}\tag{T}
$$

**Proof.** Clearly $S_0\subseteq S_{\rm tr}\subseteq S_{\rm rel}$. By (R), every class in $S_{\rm tr}$ also lies in $S$, so its localization at each $q_i$ belongs to both $L_i$ and $L_i^{\rm tr}$, hence is zero. Thus $S_{\rm tr}=S_0$.

By the Kummer sequence
$$
0\to E(\mathbf Q)/pE(\mathbf Q)\to S\to\operatorname{Sha}(E/\mathbf Q)[p]\to0,
$$
the map $M=E(\mathbf Q)/pE(\mathbf Q)\to L_1\oplus L_2$ is an isomorphism. Therefore the retraction
$$
r:S\overset{\lambda}{\longrightarrow}L_1\oplus L_2
\overset{(\lambda|_M)^{-1}}{\longrightarrow}M
$$
satisfies $r|_M=\mathrm{id}$ and $\ker r=\ker\lambda=S_0$. Hence $S=M\oplus S_0$ and the Kummer quotient identifies $S_0$ canonically relative to the selected localization data with $\operatorname{Sha}[p]$. QED.

Consequently
$$
S_{\rm tr}=0\Longleftrightarrow
\operatorname{Sha}[p]=0\Longleftrightarrow
\operatorname{Sha}[p^\infty]=0.
$$
The final equivalence needs no *global* finiteness hypothesis: a nonzero p-primary torsion group always has an element of order p.

**Terminology caution.** The chosen complementary lines need not be the canonical Mazur–Rubin **Kolyvagin transverse local condition**; they are simply linear complements. Identifying their explicit classes with derived Kato classes requires additional proofs. Equation (T) is not itself a Kolyvagin-system primitivity theorem.

## 4. Existing concrete MW matrices and finite-field-only audit

The following genuine user-recorded MW local matrices are in [the saved results](../results/bsd389_MW_local_determinants_USER_RUN_PASS_2026-11-02.md).

| p | q₁,q₂ | A_p | det mod p | A_p⁻¹ mod p |
|---:|---|---|---:|---|
| 5 | 41,61 | [[1,3],[1,0]] | 2 | [[0,1],[2,3]] |
| 7 | 113,673 | [[1,3],[1,6]] | 3 | [[2,6],[2,5]] |
| 107 | 369793,383917 | [[1,15],[1,53]] | 38 | [[38,70],[76,31]] |

The independent pure-Python companion [finite-field linear algebra audit](../verification/bsd389_poitou_tate_two_prime_linear_audit.py) verifies the determinants, inverses and exact zero kernel for the transpose pairing $A_p^t$. It does *not* compute $\Sha$ or prove global Poitou–Tate by experiment.

The separate user-executed proof-mode Sage bounds for p=5,7,107 imply, using (T), that the associated **strict and transverse Selmer groups vanish**. This is a new reformulation of the already proved p-primary vanishing, **not** another independent proof of it.

## 5. The precise arithmetic gap after the theorem

For any p with an MW-local unit pair, **all** extra p-Selmer classes are in the strict/transverse group $S_0=S_{\rm tr}\simeq\operatorname{Sha}[p]$. Our local MW 2×2 determinant proves the ordinary localization is surjective, and Poitou–Tate proves relaxation adds nothing. Neither implies $S_0=0$; an extra two-dimensional p-Sha can exist in the strict kernel without contradicting these facts.

The actual next **noncircular** input must show $S_{\rm tr}=0$ through an explicit, valid Kolyvagin/Euler-system primitivity or independent global cohomological computation. In particular, a proven degree-two Kurihara unit for the same p would suffice under Kim's hypotheses; but the local matrix and global reciprocity do not themselves prove such a unit. All-large-p vanishing and complex BSD remain open.

This supplies an exact, p-uniform *cohomological* bridge from MW localizations to the **actual** Sha obstruction, unlike the unsupported arrow from an integral Hecke eigensymbol module to the full Selmer dual in the earlier candidate.

**Verdict:** two proved theorems (R), (T) and reproducible local matrix checks, **not** BSD.
