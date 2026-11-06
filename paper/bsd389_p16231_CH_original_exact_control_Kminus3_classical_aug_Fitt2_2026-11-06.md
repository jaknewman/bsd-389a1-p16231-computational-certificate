# E389a1, p=16231: exact anticyclotomic Selmer control at K=-3 and its classical augmentation

Date: 2026-11-06. **New theorem-level application of Chida–Hsieh Proposition 1.9 and their Proposition 1.7. No archived p-specific computation is rerun.** This corrects the previous impression that the discriminant -3 exclusion in Kim's 2026 *initial-Fitting* article obstructed every available exact *control* theorem.

## 1. Source distinction and hypotheses

Fix E/Q=389a1, K=Q(sqrt(-3)), p=16231. The accepted archived data give E(Q)=Z P+Z Q, a_p=128, good ordinary p, p split in K, p not dividing N_K=3 or N_E=389, residual E[p] absolutely irreducible (even surjective), and residual ramification at 389 (multiplicative reduction and v_389(Delta_min)=1). Put \(N^-=389\), one inert prime. Finally
\[
a_p(E)^2-1=128^2-1=16383\not\equiv0\pmod{16231}.
\]
This is *precisely* the weight-two (PO) assumption \(a_p^2\not\equiv1\bmod p\) in Chida–Hsieh.

The **original Chida–Hsieh 2014/15** paper *On the anticyclotomic Iwasawa main conjecture for modular forms*, section 1, assumes **any imaginary quadratic K** with p not dividing N D_K and one inert N^- factor; it does **not** require D_K>4. Proposition 1.9 then proves exact Selmer restriction for \(E[p^n]\) and the **Delta-ordinary** local conditions. This is a different theorem from Kim's *2026 article* whose written theorem setup assumes \(-D_K<-4\) and whose Theorem 1.1 moreover identifies **initial** Fitt0 of a particular classical Selmer. Do not apply the latter to K=-3 without separately extending its hypotheses.

Sources:
- Chida–Hsieh, *On the anticyclotomic Iwasawa main conjecture for modular forms*, Proposition 1.9, proof on printed pages 7–8 (and Lemmas 1.7–1.8): https://www.asahi-net.or.jp/~qa4m-cd/AIMC.pdf .
- Kim, *On the Fitting ideals of anticyclotomic Selmer groups of elliptic curves with good ordinary reduction*, Canadian Math. Bulletin 69 (2026), Theorem 1.1, Proposition 4.3, https://doi.org/10.4153/S000843952510088X .

## 2. The exact infinite-layer control statement (unconditional under accepted input)

Let \(\Gamma=\mathrm{Gal}(K_\infty/K)\simeq\mathbf Z_p\), \(\Lambda=\mathbf Z_p[[\Gamma]]\simeq\mathbf Z_p[[T]]\), \(A=E[p^\infty]\). Write \(S_\Delta(L,A)\) for the \(N^-\)-ordinary Selmer group of Chida–Hsieh: usual unramified conditions away from \(pN^-\), ordinary local conditions at primes over \(pN^-\), with \(\Delta=N^-=389\).

**Theorem A.** There is an exact isomorphism
\[
\boxed{S_\Delta(K,A)\xrightarrow{\sim}S_\Delta(K_\infty,A)^\Gamma.}\tag{A}
\]
Consequently, with \(X_\Delta=S_\Delta(K_\infty,A)^\vee\), there is an **integral**, \(\mathbf Z_p\)-linear isomorphism
\[
\boxed{X_\Delta/TX_\Delta\xrightarrow{\sim}S_\Delta(K,A)^\vee.}\tag{A'}
\]

**Proof by Chida–Hsieh Prop. 1.9.** Their assertion for \(E[p^n]\) over each finite \(L=K_m\) has exactly hypotheses (PO) and (Irr), already checked above. For clarity, their proof consists of:
1. \((E[p^n])^{G_{K_\infty}}=0\) by irreducibility and the pro-p nature of \(K_\infty/K\), so global inflation–restriction is exact;
2. away from p and Delta the anticyclotomic tower is unramified, and restriction on unramified local H1 is injective;
3. at Delta=389, **inert in K**, the tower is completely split locally, so there is no local restriction kernel;
4. at p, the ordinary local quotient has no Galois invariants by Lemma 1.8, since its unit-root Frobenius is \(128\bmod p\ne\pm1\).
Their finite-coefficient exact control passes to the direct limit in n and the tower limit in m, yielding (A). Pontryagin duality identifies invariants with coinvariants, giving (A'). No additional D_K>4 hypothesis occurs in the source statement or proof; p=16231 is coprime to the exceptional six roots of unity of K=-3. QED.

## 3. Identification with the TRUE classical Selmer at the base

**Theorem B.** At the base field K, with the same p and conditions, the Chida–Hsieh \(\Delta\)-ordinary Selmer group agrees with the classical p-infinity Kummer Selmer:
\[
\boxed{S_\Delta(K,A)=\mathrm{Sel}_{p^\infty}(E/K).}\tag{B}
\]

**Proof, place-by-place.**
- For v not dividing pN_E, E has good reduction, v∤p, and the unramified H1 local condition equals the local Kummer finite condition.
- For the unique prime v|389, E is multiplicative with p-residual ramification. Chida–Hsieh Proposition 1.7(1), proof following it, states and proves at \(\ell|N^-\) with ramified residual representation that the ordinary and finite local H1 conditions coincide at every \(p^n\). They therefore coincide for A=E[p∞].
- For each v|p, p is split in K, so K_v=Q_p. E has good ordinary reduction and is nonanomalous: \(\#E(\mathbf F_p)=16104\not\equiv0\bmod p\). The finite local Kummer and ordinary Greenberg conditions coincide in this nonanomalous case. This is the standard local comparison (e.g. Bertolini–Darmon–Venerucci, *Congruences between modular forms and the Birch and Swinnerton-Dyer conjecture*, section discussing the non-anomalous condition); it can also be deduced from the ordinary exact filtration and \(H^0(K_v,A/F^+A)=0\), as in Chida–Hsieh Lemma 1.8 and the local Kummer formal-group calculation.

These exhaust the local conditions. QED.

**Important:** (B) proves equality at the BASE K, which is enough for the desired augmentation. We do **not** claim the classical and ordinary Selmer coincide at every finite K_m or at K_infty under no further hypotheses. The 2026 Kim theorem's stronger all-layer initial-Fitting statement is not being imported into K=-3.

## 4. Exact no-gap augmentation/Fitting identity for the actual Delta-ordinary anticyclotomic module

Combine (A'), (B), the rank-two Kummer/Pontryagin splitting over K and the quadratic plus/minus decomposition for odd p:

\[
X_\Delta/TX_\Delta
\cong\mathrm{Sel}_{p^\infty}(E/K)^\vee
\cong \mathbf Z_p^2\oplus
 \Sha(E/\mathbf Q)[p^\infty]^\vee
 \oplus\Sha(E^{(-3)}/\mathbf Q)[p^\infty]^\vee.
\]

Here rank E(K)=2 because the certified twist E^{-3} has analytic rank zero and Kolyvagin gives its algebraic rank zero and finite Sha. Let
\(I_+=\mathrm{Fitt}_{0,\mathbf Z_p}(\Sha(E/\mathbf Q)[p^\infty]^\vee)\),
\(I_-=\mathrm{Fitt}_{0,\mathbf Z_p}(\Sha(E^{-3}/\mathbf Q)[p^\infty]^\vee)\).

**Theorem C (EXACT, integral, not pseudo-equivalent).**
\[
\boxed{
\frac{\mathrm{Fitt}_{2,\Lambda}(X_\Delta)+(T)}{(T)}
=I_+I_- .
}\tag{C}
\]

**Proof:** Fitting ideals commute with base change \(\Lambda\to\Lambda/(T)=\mathbf Z_p\); \(\mathrm{Fitt}_2(\mathbf Z_p^2\oplus M)=\mathrm{Fitt}_0(M)\); and \(\mathrm{Fitt}_0(M\oplus N)=\mathrm{Fitt}_0(M)\mathrm{Fitt}_0(N)\). No Sha finiteness is assumed. QED.

Since \(\Lambda\) is local with maximal ideal \(\mathfrak m=(p,T)\), (C) also yields the exact logical equivalence
\[
\boxed{
\mathrm{Fitt}_{2,\Lambda}(X_\Delta)=\Lambda
\iff
\Sha(E/\mathbf Q)[p^\infty]=0
\ \mathrm{AND}\
\Sha(E^{-3}/\mathbf Q)[p^\infty]=0.
}\tag{D}
\]
The twist group is finite, but may have p-torsion unless separately bounded; do NOT silently discard \(I_-\).

## 5. Exactly what we achieved and what remains

**Closed for p=16231:** the previously conditional integral control isomorphism *for the explicit Chida–Hsieh Delta-ordinary Selmer module*, its comparison to classical Selmer at the base K, and the consequent exact higher-Fitting augmentation factorization. This uses a published 2014/15 proposition applicable to discriminant -3, not Kim's more restricted 2026 initial-Fitting theorem.

**NOT closed:** a constructive p-integral Euler/Kolyvagin reciprocity law generating an actual unit **second Fitting minor at (p,T)** of \(X_\Delta\); the order of the p-primary finite Sha of the twist (unless separately proved); a single all-p finite-support integer; or the exact complex rank-two BSD leading term. Theta quadratic coefficient being a unit and initial Fitting0 agreement do not force the higher Fitting unit: see the universal 4x4 algebraic counterexample in the same branch.

Theorem C is NOT a proof that \(I_+=\mathbf Z_p\), merely a proven exact bridge identifying the unknown ideal at p=16231. Any future calculation/reciprocity must measure a nonzero 2x2 minor modulo (p,T), not just \(\Theta''(0)\) or \(\Theta^2\).
