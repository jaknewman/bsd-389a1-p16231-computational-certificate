# E389a1: identify the ACTUAL Castella–Hsieh theta series and first p=16231 anticyclotomic layer

**Date:** 2026-11-05. Corrected source-level research target, with the 2022 Castella–Hsieh paper inspected including PDF printed pages 4, 9, 26, 27.

## 1. The crucial character separation

In Castella–Hsieh *On the non-vanishing of generalized Kato classes for elliptic curves of rank two*, Forum Math. Sigma 10 (2022), Theorem 2.3 (printed p. 9), the theta family is \`Theta_(f/K,chi)(T)\`, and **\`Theta_(f/K)(T)=Theta_(f/K,1)(T)\` means the trivial ring-class character chi=1**.

The symbol *f* refers to the weight-2 modular newform of elliptic curve E=389a1, **not** the fixed conductor-53 order. Theorem B requires \`ord_T(Theta_(f/K,1))=2\`, not the first nonzero coefficient of our finite conductor-53 chi9 toric polynomial and not a theta series twisted by chi9.

The separate order-9 character chi9 of Pic(O_53) enters Theorem A as the nonzero auxiliary adjoint Rankin factor \`L(E/K,chi9,1)\`, in \`L(E,ad0(theta_psi),1)=L(E^K,1) L(E/K,chi9,1)\`. The two tasks are logically different, though both use quaternionic Brandt computations.

**This corrects an ambiguity in some older project's notation \`Theta_(53/K)\`: a fixed order-f conductor must not be substituted for the modular form subscript f.**

Primary source: https://web.math.ucsb.edu/~castella/Kato.pdf (Theorem 2.3 and after Remark 2.4, printed page 9; Theorem B, printed page 5).

## 2. Exact published finite-theta formula

Castella–Hsieh, Appendix §6, printed page 26, define (with p-adic unit root alpha_p of X²−a_p(E)X+p, p-stabilized Hecke vector phi_f on definite quaternionic right ideal classes, local splitting/diagonalization i_p, u=1+p):

Theta_(f/K,n)(T) =
alpha_p^(-(n+1)) ∑_(i=0)^(p^n−1) ∑_(a∈mu_(p−1))
    [alpha_p phi_f(P_n^(a u^i)) − phi_f(P_(n+1)^(a u^i))] (1+T)^i

where P_n^a is built from the adelic matrix (1,ap^(−n);0,1) in the split quaternionic local chart. These finite theta elements project from the actual pro-p Iwasawa element modulo (1+T)^(p^n)−1.

The trivial-character theta uses **new p-power conductor CM points** P_n^a for n>=1. The 18 old optimal conductor-53 orbit embeddings do not provide them. Our archived frozen 33-dimensional Brandt Hecke eigenvector is still directly reusable once these new local CM points are correctly constructed.

The first n=1 expression has p(p−1)=16231*16230=**263,429,130** naive (i,a) summands. This is a practical reason to design exact compressed Brandt-class counts / moment aggregation instead of naively recomputing another huge sum. At n=2 the naive summation increases massively; no such full run is claimed.

## 3. First genuine p-primary ring-class quotient for K=Q(sqrt(-3))

For K discriminant -3 and p=16231 split, h_K=1, and nonmaximal order O_(p^n) of conductor p^n has class number

h(O_(p^n)) = (p^n/3)(1−1/p) = p^(n−1)(p−1)/3, for n>=1.

Thus h(O_p)=**5,410** is prime to p, whereas h(O_(p²))=**87,809,710** has p-adic valuation 1 and the ratio h(O_(p²))/h(O_p)=**16,231**. The first nontrivial Z_p quotient from the ring-class conductor tower therefore appears at conductor p².

The explicit local algebra O_K/p² ≅ (Z/p²)×(Z/p²) has two roots of omega²+omega+1 mod p:
**6044, 10186**,
and their Hensel lifts mod p²:
**49689135, 213756225**.
They satisfy sum -1 and product 1 modulo p². The p-principal-unit element (1+p) mod p² has order p, displaying the order-p quotient. This does **not** construct the full quaternionic diagonalization i_p: R⊗Z_p ≃ M₂(Z_p) and does not compute any actual Gross point.

## 4. Finite layer n=1: exact coefficient extraction

Let W_i = ∑_(a∈mu_(p−1)) [alpha_p phi_f(P_1^(a u^i)) − phi_f(P_2^(a u^i))] modulo p, for i=0,..,p−1. For k=0,1,2,

[T^k] Theta_(f/K,1)(T) ≡ alpha_p^(−2) ∑_(i=0)^(p−1) binom(i,k) W_i (mod p).

At p=16231, alpha_p ≡ a_p=128 mod p and **alpha_p^(−2) ≡4986 mod16231**.

These are moment formulas which require *genuine* Gross-point values or independently verified row sums as input. They constitute neither new theta data nor proof that the lower integral coefficients vanish. In Λ/(p,(1+T)^p−1), the relation is T^p=0; hence degrees 0..2 are unambiguous **mod p** at n=1. To establish ord_T Theta=2, independently justify vanishing of the exact constant/linear coefficients (or use an appropriate published theorem providing ord>=2) and show c2≠0 over Q_p. A zero result mod p for c2 would be inconclusive about higher p-adic valuation. One should use stronger n/precision if necessary. We do not assert that the n=1 mod-p test alone can always settle the theorem's hypothesis.

A standard-library arithmetic / optional-moment auditor is committed at:
[verification/bsd389_p16231_anticyclotomic_first_layer_preflight.py](../verification/bsd389_p16231_anticyclotomic_first_layer_preflight.py).

## 5. A published independent positive benchmark *for E=389a1*

Castella–Hsieh Appendix Table 1, printed p. 27, explicitly lists the genuine theta series **E=389a1, p=11, K=Q(sqrt(-2))** (not our p16231,K−3 example), with

Theta_(f/K) ≡ 10 T² + 69 T³ + T⁴ + 103 T⁵ + 106 T⁶ + 66 T⁷ + 117 T⁸ + 55 T⁹ + 110 T¹⁰
  mod (11²,T¹¹).

The authors state this verifies ord_T Theta=2 and hence nonvanishing of generalized Kato classes for that case. This provides a published target to reproduce on a *small* p before scaling any new quaternionic p=16231 Gross-point pipeline. The separate user's Sage p11-primary Sha-zero certificate is still independently stronger with respect to **finite p-torsion**, while the authors' result concerns rational-p Selmer corank.

## 6. Remaining mathematical gate and no-circularity note

The new correct task at p16231 is to construct the **trivial-character, pro-p theta** for the pair E389a1,K−3, with its p-local Gross-point tower and prove its leading augmentation degree is exactly 2. Then, assuming the auxiliary nonzero Rankin factor and all hypotheses of Castella–Hsieh Theorems A/B (some input archived computer-assisted), one gets nonzero generalized Kato class and dim_(Qp)Sel(Q,VpE)=2, i.e., **finite**, not necessarily trivial, Sha[p∞].

Crucially the finite conductor-53 character's polynomial norm 729 only addresses a separate auxiliary factor and never proves \`ord_T Theta=2\`; the prior finite C18 idempotent augmentation no-go applies.

No global finite support of Sha, p16231 theta coefficient, or strong BSD proof is claimed.

### Sources

- Castella–Hsieh, original PDF: https://web.math.ucsb.edu/~castella/Kato.pdf, §§2.4,5.6,Appendix §6.
- Published journal page: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864
- Historical user certificates on optimality, Stage22 exact transports, Stage30 Hecke eigenspace and finite norm729: results folder, 2026-11-05.
