# Uniform local logarithm lattice and saturation for E389a1 (2026-11-06)

No previous numerical certificate was rerun. This is a symbolic theorem for any good p>=5 with p not dividing N_p=#E(F_p).

**Lemma 1 — integral normalized logs.** For R∈E(Q), [N_p]R belongs to the p-adic formal subgroup E_1(Q_p), whose formal parameter t=-x/y and formal logarithm lie in pZ_p. Because N_p is a p-unit, log_p(R)=N_p^(-1)log_p([N_p]R) lies in pZ_p. Use the minimal invariant differential dx/(2y+1).

**Lemma 2 — the exact saturation index.** Let M=Z_p P⊕Z_p Q, and define the functional L:M→Z_p by L(R)=log_p(R)/p. Put a=L(P), b=L(Q) and d=min(v_p(a),v_p(b)), finite since P and Q are non-torsion. Let u=a/p^d, v=b/p^d, with at least one a p-unit. Then

- ker(L)=Z_p·(vP-uQ), a saturated rank-one lattice;
- the natural logarithmic Kato-shadow tilde_eta=bP-aQ=p^d(vP-uQ);
- [ker(L):Z_p tilde_eta]=p^d and Fitt_0(coker L)=p^d Z_p.

Proof: on basis (P,Q), the row matrix of L is (a,b)=p^d(u,v). Over the DVR Z_p, the primitive row (u,v) is equivalent by GL_2(Z_p) to (1,0); the kernel and cokernel follow.

**Corollary — correct Euler-factor cancellation.** Castella–Hsieh (2022), Theorem 5.5, states over the rational p-adic Selmer space that
kappa_p = C_p e_p theta_2/H_p * eta_p,
where eta_p=log_p(Q)P-log_p(P)Q, H_p is the derived anticyclotomic height h_p^(2)(P,Q), and e_p=(1-alpha_p/p)/(1-alpha_p^(-1)).
Since eta_p=p tilde_eta, this becomes
kappa_p=C_p*(p e_p)*(theta_2/H_p)*tilde_eta.
For a good ordinary nonanomalous p, p e_p=(p-alpha_p)/(1-alpha_p^(-1)) is a p-adic unit. Relative to the SATURATED generator vP-uQ, the coefficient is C_p*(p e_p)*(theta_2/H_p)*p^d. Thus its valuation is v_p(C_p/H_p)+v_p(theta_2)+d: the previous apparent universal p^(-1) denominator was *already canceled by the MW log divisibility*. Integral Kolyvagin/Fitting comparison is still unproved.

For p=16231, previously certified a_p=128, N_p=16104 prime to p, p e_p=8306 mod p and theta_2=3739 mod p. Hence (p e_p)*theta_2=6231 mod p. The *local logarithmic saturation exponent* d is not yet certified and must not be presumed zero. No claim is made that Sha[p∞] vanishes or that complete BSD follows.

The nonanomalous good primes have natural density one for this non-CM curve: anomalous p>=7 have a_p=1 by Hasse, and the set a_p=1 has density zero by Serre's open image + Chebotarev. Density one does not mean all but finitely many.

Reference: Castella–Hsieh, Forum Math Sigma 10 (2022), Theorem 5.5, https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864 .
