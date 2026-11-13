# E389a1: exact Frobenius dichotomy at p-admissible auxiliary primes

**2026-11-13. Unconditional elementary local theorem.** This is a correction to any over-broad claim that the two numerical Kurihara admissibility congruences alone imply a one-dimensional local Kummer quotient.

Let E/Q have good reduction at q≠p, p odd, and suppose q≡1 (mod p) and a_q(E)≡q+1≡2 (mod p). On V=E[p], the Frobenius characteristic polynomial satisfies
$$
\det(T-\operatorname{Frob}_q\mid V)
=T^2-a_q T+q\equiv(T-1)^2\bmod p.
$$
Because Frobenius is an invertible 2×2 matrix, its Jordan form over Fp is **exactly one of two options**:

- **Scalar:** Frob_q = I; then E(F_q)[p]=V has dimension 2.
- **Nonidentity unipotent:** Frob_q∼[[1,1],[0,1]]; then its fixed subspace E(F_q)[p] is a line of dimension 1.

For good q≠p, reduction and the pro-q formal kernel imply E(Q_q)/p≅E(F_q)/p, and for the finite group E(F_q), its mod-p quotient has the same Fp dimension as E(F_q)[p]. Hence
$$
\boxed{
\dim_{\mathbf F_p}E(\mathbf Q_q)/p=
\begin{cases}
2,&\rho_{E,p}(\operatorname{Frob}_q)=I,\\
1,&\rho_{E,p}(\operatorname{Frob}_q)\ne I.
\end{cases}}
$$
With the local Weil-pairing self-duality, the associated local cohomology H¹(Q_q,E[p]) has Fp dimension 4 or 2 respectively. This follows from the local Euler characteristic and local Tate duality.

An easy **sufficient**, but not necessary, numerical test for the one-dimensional case is v_p(#E(F_q))=1: if Frob were scalar, #E(F_q) would be divisible by p². Higher p-divisibility of #E(F_q) alone, however, does not imply scalar Frobenius.

### Exact E389a1 p=7 witnesses

For q=113,281,673, the traces are 9,-12,2 and q≡1,a_q≡2 mod7 in all cases. The new exact group-law certificate
[verification/bsd389_p7_bockstein_oldform_adversarial_audit.py](../verification/bsd389_p7_bockstein_oldform_adversarial_audit.py)
exhibits independent order-seven points (20,74), (22,61) on E(F281), so Frobenius_281=I and the local Kummer space has dimension 2. Since #E(F113)=105 and #E(F673)=672 each has 7-adic valuation 1, their Frobenius classes are nontrivial unipotent and their local Kummer spaces have dimension 1.

Thus (113,281) cannot satisfy the hypothesis that two rational MW generators surject onto *both* local Kummer spaces (the target dimension is 3, source dimension 2), whereas (113,673) can and indeed has an archived invertible MW-local determinant mod7.

The statement is about local Galois representations and Selmer *hypotheses*, not a proof that scalar Frobenius forces the Kurihara coefficient to vanish. The actual p7 Kurihara zero/nonzero comparison and the published Kato reciprocity theorem are detailed in the companion note [here](bsd389_p7_kato_reciprocity_oldform_vs_kurihara_and_full_torsion_2026-11-13.md).

**Verdict:** an exact p-independent two-case classification, with a new explicit p7 scalar Frobenius witness; no new Sha or BSD conclusion.
