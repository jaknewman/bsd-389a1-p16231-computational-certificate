# E389a1: exact-degree splitting of individual Sha torsors and zero visibility in J_0(389)

**Date: 2026-11-13.** **Mathematical status:** two exact deductions from published theorems and existing p-primary certificates. Neither proves the finiteness of the entire Tate–Shafarevich group, the nonvanishing of all-large-p degree-two Kurihara classes, nor strong complex BSD.

## 1. Cassels–Lichtenbaum: an individual Sha class has a splitting field of *exactly* its order

Let E be any elliptic curve over a number field k, and let $\xi \in \Sha(E/k)$ have finite order $n$.

**Theorem 1 (classical, with elementary consequence).**
$$
\boxed{\min\{[L:k]:\, L/k\text{ finite},\
\operatorname{res}_{L/k}(\xi)=0\}=n.}\tag{1}
$$

**Proof.** The genus-one E-torsor $C_\xi$ has period n, the order of its Weil–Châtelet cohomology class. Cassels–Lichtenbaum's theorem says that **period=index** for a torsor of an elliptic curve over a number field which is everywhere locally soluble, as $C_\xi$ is. Thus its index is n. The index-attainment lemma for genus-one curves shows there exists a finite degree-n extension L/k on which $C_\xi$ has a rational point, so $\operatorname{res}_{L/k}(\xi)=0$.

Conversely for *every* finite splitting field M/k, restriction–corestriction gives $[M:k]\xi=0$, so n divides $[M:k]$. Hence degree n is optimal. QED.

**Precise references:**
- Tom Fisher, *Visibility of Tate–Shafarevich Groups*, Definitions 2.1, Lemma 2.2 and Theorem 2.7 (Cassels–Lichtenbaum): https://www.dpmms.cam.ac.uk/~taf1000/papers/visibility.pdf.
- Pete L. Clark, *The period-index problem in WC-groups II*, introduction (identifies the Cassels–Lichtenbaum result for Sha): https://plclark.github.io/PeteLClark/Research/wc2.pdf.

**Correction to the project's 2026-11-13 previous note:** The existence of a *not necessarily solvable* degree-$p^n$ extension killing each individual order-$p^n$ Sha class **does not require Kim's 2026 theorem**; it is already implied by Cassels–Lichtenbaum. Kim's genuinely different additional feature is a solvable / ring-class splitting construction under that paper's hypotheses. The degree-$p^n$ extension from Theorem 1 need not have solvable Galois closure. Theorem 1 is **not** a uniform splitting field for the whole $\Sha[p^n]$.

## 2. Finiteness and uniform visibility — Fisher's fixed-ambient theorem

For an embedding of abelian varieties $i:E\hookrightarrow B$ define
$$
\mathrm{Vis}_B\Sha(E/k)
=\ker(\Sha(E/k)\to H^1(k,B)).
$$
The visibility subgroup is always finite for a fixed B, even if global Sha is unknown, because the connecting homomorphism
$$
(B/E)(k)\to H^1(k,E)
$$
has image equal to $\ker(H^1(k,E)\to H^1(k,B))$. The image is finitely generated (Mordell–Weil for $B/E$) and torsion (Weil–Châtelet), hence finite.

Tom Fisher's Lemma 4.6 makes the converse precise: for any subgroup $S\subseteq H^1(k,E)$, every element of S is visible in some **single fixed** abelian variety B containing E if and only if S is finite. Therefore the statement “construct one fixed B in which all of Sha becomes visible” is **equivalent** to global Sha finiteness, not a proof unless B and the necessary visibility maps can be constructed without circular assumptions.

## 3. Concrete E389a1 theorem: absolutely no Sha visibility in J_0(389)

Let
$$E/\mathbf Q: y^2+y=x^3+x^2-2x,\quad J=J_0(389).$$
E is the $\Gamma_0(389)$-optimal quotient. Let $\varphi:X_0(389)\to E$ be the minimal modular parametrization. The modular degree is

$$
\deg(\varphi)=40=2^3\cdot5.
$$

This exact integer is publicly recorded by LMFDB: https://www.lmfdb.org/EllipticCurve/Q/389a1/ and its underlying data page https://www.lmfdb.org/EllipticCurve/Q/data/389.a1.

The Albanese/Jacobian pushforward $\pi=\varphi_*:J\to E$ and its dual pullback $\iota=\varphi^*:E\hookrightarrow J$ (the optimal quotient dual) satisfy the exact *canonical polarization* identity

$$
\boxed{\pi\circ\iota=[40]:E\longrightarrow E.}\tag{2}
$$

The induced Galois cohomology composite is multiplication by 40. Hence if $\xi\in\ker(H^1(\mathbf Q,E)\xrightarrow{\iota_*} H^1(\mathbf Q,J))$, then $40\,\xi=0$.

For the *Tate–Shafarevich subgroup*, the project's **genuine user-executed Sage 10.9 proof-mode certificates** establish
$$
\Sha(E/\mathbf Q)[2^\infty]=0
\quad\text{and}\quad
\Sha(E/\mathbf Q)[5^\infty]=0.
$$
Sources:
- [2-primary direct Selmer certificate](../results/bsd389_sha2_direct_selmer_USER_PASS_2026-11-02.md).
- [5-primary Sage bound](../results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md); independently p=5 appears in Kim's published 389a1 example: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf.

Thus no nonzero class in Sha is annihilated by 40. We have proved

$$
\boxed{
\mathrm{Vis}_{J_0(389)}\Sha(E/\mathbf Q)
=\ker\bigl(\Sha(E/\mathbf Q)\to H^1(\mathbf Q,J_0(389))\bigr)
=0.
}\tag{3}
$$

Equivalently, $\iota_*:\Sha(E/\mathbf Q)\hookrightarrow H^1(\mathbf Q,J)$ is **injective on the entire, not assumed finite Sha**. This is a precise 389a1-specific negative result about one fixed modular Jacobian, **not** a claim that Sha itself is zero.

For any prime $p\nmid40$, injectivity on the p-primary subgroup even follows from (2) alone. The p=2,5 certificates close the remaining cases.

**Verification note:** A companion Sage script is provided for (i) the exact modular degree, (ii) the separate 2-primary and 5-primary bounds. It has **not** been executed by the assistant because Sage is unavailable locally; the user-run 2 and 5 certificates in the prior repository are genuinely archived and LMFDB independently publishes the modular degree. This note does not label a new Sage run as PASS.

## 4. An exact necessary conductor level in the existing p=16231 K=-3 ring-class tower

For the *fixed* quadratic field $K=\mathbf Q(\sqrt{-3})$, $p=16231$ splits and the ring-class group of order $\mathcal O_{p^m}$, $m\ge1$, has order
$$
h_m=p^{m-1}\frac{p-1}{3}=5410\,p^{m-1}.
$$
The associated full ring-class field $F_m/K$ satisfies
$$
[F_m:\mathbf Q]=2h_m=10820\,p^{m-1},\qquad
v_p([F_m:\mathbf Q])=m-1.
$$
These formulas extend the exact user-verified cases m=1,2 in [the earlier preflight](../results/bsd389_p16231_anticyclotomic_first_layer_PREFLIGHT_USER_PASS_2026-11-05.md).

If a p-primary Sha class $\xi$ of *exact order $p^n$* is killed by restriction to this *particular* F_m, the degree divisibility in Theorem 1 forces
$$
\boxed{n\le m-1,\qquad\text{hence }m\ge n+1.}\tag{4}
$$
Equivalently,
$$
\ker\bigl(\Sha(E/\mathbf Q)[p^\infty]\to\Sha(E/F_m)[p^\infty]\bigr)
\subseteq\Sha(E/\mathbf Q)[p^{m-1}].
$$
The restriction kernel is therefore **finite at every fixed level m**, without any assumption of global Sha finiteness. For m=1, restriction is injective on the p-primary Sha; for m=2, only p-torsion can be in the kernel.

**Limitation:** Necessary condition (4) does not say a class of order $p^n$ becomes trivial at level $m=n+1$, nor that Kim's 2026 theorem selects this fixed field K or this tower. Those are separate arithmetic assertions that have not been proved.

## 5. How this changes the BSD research route

We now have:
1. Exact optimal splitting degree for **each individual** Sha torsor, already classical.
2. A rigorous **zero visibility** result for the existing fixed modular Jacobian at level 389.
3. A necessary conductor growth inequality in the *actual* K=-3 ring-class p=16231 tower.

Thus neither “find some p-power-degree splitting field for each class” nor “use the existing J_0(389) to make every Sha class visible” can supply the missing all-large-p global Selmer/Fitt₂ bound. A successful method would need a **new independent integral Galois-cohomological or higher Euler/Kolyvagin system comparison** (possibly with varying auxiliary levels), coupled to a proof of primitivity, not just the existing Hecke Smith determinant 2 or the MW wedge.

The theorem's negative scope is sharply limited: invisibility in J_0(389) does not preclude visibility in higher-level modular Jacobians or other abelian varieties. Even if complete Sha finiteness were proved, the **exact complex BSD leading-term identity** remains separate.

**Verdict:** Two genuine rigorous theorems and one conductor bound, with no unsupported claim that BSD or Sha finiteness is solved.
