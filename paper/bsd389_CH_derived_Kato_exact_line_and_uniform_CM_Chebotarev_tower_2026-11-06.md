# Global BSD 389a1: the actual generalized-Kato class, its exact derived-height coefficient, and the CM-uniformity obstruction

**2026-11-06 — mathematical deductions; no previously certified numerical test is rerun.**

We retain: E=389a1, E(Q)=ZP⊕ZQ, rank analytic 2; K=Q(sqrt(-3)), E^{-3} has rank 0 and finite Sha; the existing p=16231 theta/Gross certificate and the already archived p-primary bounds. This note concerns the possible **all-prime integral bridge**, not a new proof of global BSD.

## Theorem I. The derived class ALREADY EXISTS; its exact rational line is known

For any good ordinary p>3 **split in K** and auxiliary finite-order CM weight-one theta form g=theta_psi meeting the precise hypotheses of Castella–Hsieh Theorems A and B (in particular N^-=389, nonzero L(E^{-3},1)L(E/K,chi,1), distinct U_p roots and \bar rho irreducible/ramified at 389), suppose that ord_T Theta_{f/K}=2.

Then Theorem B gives a nonzero *constructed* generalized Kato class
\[
\kappa_p:=\kappa_{\alpha,\alpha^{-1}}(f,g,g^*)\in
\operatorname{Sel}(\mathbf Q,V_pE),
\]
and Theorem A gives
\[
\operatorname{Sel}(\mathbf Q,V_pE)=E(\mathbf Q)\otimes\mathbf Q_p
\quad (\dim=2).
\]
Thus \Sha(E/Q)[p^\infty] is **finite**, not necessarily trivial. The paper does not require us to construct a new auxiliary rank-two Kolyvagin system to obtain this rational class: it is already constructed by Darmon–Rotger and analyzed by Castella–Hsieh.

Let \(\ell_P=\log_p(P)\), \(\ell_Q=\log_p(Q)\),
\[
\eta_p=\ell_Q P-\ell_P Q\neq0,\quad
H_p=h_p^{(2)}(P,Q)\neq0,\quad
\theta_{2,p}=\operatorname{coeff}_{T^2}\Theta_{f/K}.
\]
Theorem 5.5 of Castella–Hsieh gives the **exact class identity** over the appropriate coefficient extension of Q_p:
\[
\boxed{
\kappa_p
=C_p\,\frac{1-p^{-1}\alpha_p}{1-\alpha_p^{-1}}\,
\frac{\theta_{2,p}}{H_p}\,\eta_p.
}\tag{1}
\]
Here \(\alpha_p\) is the *unit root of the elliptic curve*'s Hecke polynomial and \(C_p\ne0\) is the article's algebraic comparison factor with \(C_p^2\in K(\chi,\alpha_p)^\times\). It depends on the choice of auxiliary CM character and embeddings/normalizations. **It is not given as a universal p-adic unit, nor as one fixed rational number independent of p.**

**Elementary derivation from Theorem 5.3:** The derived pairing \(h_p^{(2)}\) is alternating on the two-dimensional Selmer space; write \(\kappa_p=aP+bQ\). Theorem 5.3 gives \(h_p^{(2)}(\kappa_p,P)=C_p e_p\theta_{2,p}\ell_P\) and \(h_p^{(2)}(\kappa_p,Q)=C_p e_p\theta_{2,p}\ell_Q\), with \(e_p=(1-p^{-1}\alpha_p)/(1-\alpha_p^{-1})\). Since \(h(P,P)=h(Q,Q)=0\) and \(h(P,Q)=H_p\), we obtain \(-bH_p=C_p e_p\theta_{2,p}\ell_P\), \(aH_p=C_p e_p\theta_{2,p}\ell_Q\). This is exactly (1). The source guarantees the nonzero derived height in the ord_T=2 case; it is not asserted in the general situation when the theta order is higher.

**Application to the already certified p=16231 input:** The previously frozen theta argument gives ord_T Theta=2 with \(\theta_{2,p}\equiv3739\bmod p\) up to a unit of quaternionic/JL orientation and Gamma coordinate. Thus the leading theta coefficient is a p-unit, so the corresponding generalized Kato class lies on the same *rational* line Q_p·eta_p, and its exact scaling is governed by the nonzero derived height H_p and the algebraic factor C_p. We do NOT infer a unit in the *integral* Selmer lattice, nor a new Sha=0 result, from this equality alone.

## Theorem II. Even an *integral-unit* coefficient in the rational formula cannot alone detect finite Sha

The information in (1) is an identity in the rationalized Selmer space. Fix ANY odd p and consider the abstract cofinite Selmer-style dual
\[
X_p=\mathbf Z_p^2\oplus(\mathbf Z/p\mathbf Z)^2,
\qquad \operatorname{Fitt}_{2,\mathbf Z_p}(X_p)=p^2\mathbf Z_p.
\]
The finite group \((\mathbf Z/p)^2\) admits a perfect alternating (hyperbolic) Cassels–Tate-type pairing, so this example respects the standard square-order constraint on finite Sha.

After tensoring with Q_p, \(X_p\otimes\mathbf Q_p=\mathbf Q_p^2\). Choose a local logarithm \(\ell(P)=1,\ell(Q)=0\), a nondegenerate alternating derived pairing \(h^{(2)}(P,Q)=1\), and the formal values \(\theta_2=1\), \(C e=1\). Equation (1) is satisfied with \(\kappa=-Q=\ell_QP-\ell_PQ\) while the finite torsion is **NONZERO**. All rational data look identical to a model with \(X_p=\mathbf Z_p^2\) and Sha=0.

This is a **pure algebraic counterexample to the inference from rational-derived-height class equality alone to Sha[p]=0**, not a constructed elliptic curve nor a counterexample to any stronger integral main conjecture. Any true vanishing proof needs an additional theorem identifying an **integral** Selmer Fitting ideal and controlling finite torsion, not merely a rational shadow of the MW wedge.

## Theorem III. No FINITE number of imaginary quadratic auxiliary fields covers all good ordinary p

Let \(K_1,\ldots,K_m\) be any **finite** collection of imaginary quadratic fields and L their compositum. Complex conjugation \(c\in\operatorname{Gal}(L/\mathbf Q)\) restricts nontrivially to every K_i. Since L/Q is abelian, Chebotarev gives a set of rational primes p of positive Dirichlet density \(1/[L:\mathbf Q]\) whose Frobenius is c. Each such p is simultaneously **inert in every K_i**.

The curve E389a1 has no CM: its rational j-invariant is
\(j(E)=112^3/389=1404928/389\notin\mathbf Z\),
whereas rational CM j-invariants are algebraic integers. By Serre's ordinary/supersingular density theorem, the supersingular primes of a non-CM rational elliptic curve have density zero. Consequently the Chebotarev set above contains **positive-density many good ORDINARY primes** p inert in every K_i.

Castella–Hsieh Theorem A in the present ordinary CM theta setup **requires p to split in the chosen imaginary quadratic field**. Therefore:

\[
\boxed{\text{No fixed finite collection of imaginary quadratic CM auxiliary fields
can apply this split-p theorem to EVERY good ordinary p.}}
\]

This is a real global-uniformity obstruction. It is **not** a general no-go theorem for all conceivable Euler systems, or a claim that p cannot be handled by other methods. It means any proof based solely on this precise split-p auxiliary method must vary K infinitely often or obtain a distinct theorem for inert p. A finite patchwork of CM characters/fields cannot yield an all-prime proof.

## Theorem IV. The INFINITE conductor-53 ring-class tower removes regularity at every split p of K=-3

This is a constructive positive complement to Theorem III; unlike a fixed finite CM character, we take ALL levels \(53^n\) in one fixed imaginary field \(K=\mathbf Q(\sqrt{-3})\).

The prime 53 is inert in K. Let \(K_{53}\) be the unramified quadratic extension of Q_53 and \(U^1=\ker(N:O_{K_{53}}^\times\to\mathbf Z_{53}^\times)\). Its finite torsion subgroup has order 53+1=54; its pro-53 component has Z_53-rank one. Since K has class number one and units of order six, the pro-53 quotient of the anticyclotomic ring-class tower of conductors \(53^n\) is (up to finite groups of order prime to 53) this rank-one norm-one principal-unit group.

Let **ANY rational prime q≠3,53 with q≡1 mod3** be split in K; pick a generator \(\pi\in O_K\) of one prime \(\mathfrak q\) above q (possible because h_K=1), with Norm(\pi)=q. The norm-one unit
\[
u_q=\pi/\overline{\pi}\in U^1
\]
has **nontrivial image in the pro-53 quotient**. Indeed, if its pro-53 component were trivial, u_q would lie in the finite torsion subgroup \(\mu_{54}\), so \(u_q^{54}=1\) in \(K_{53}\). The field embedding \(K\hookrightarrow K_{53}\) is injective, hence \(u_q^{54}=1\) in K; thus \(u_q\in O_K^\times=\mu_6\). But then the prime ideals \((\pi)=(\bar\pi)\), contradictory since q is split and unramified.

Therefore, for EVERY split q (not merely q=16231),
\[
\boxed{\exists n\ge1,\ \exists\text{ ring-class character }\chi
\text{ of 53-power order and conductor dividing }53^n:
\chi(\overline{\mathfrak q})\ne1.}
\]
Moreover, as the local pro-53 Frobenius element is nonzero in a \(\mathbf Z_{53}\)-group, for all sufficiently deep **primitive** characters of conductor \(53^n\) the value remains \(\ne1\). This is exactly the *regularity/distinct-weight-one-p-stabilization* condition used in Castella–Hsieh when q is the residual ordinary prime.

**Scope:** This theorem supplies a regular auxiliary character for **all split q** from one infinite tower. It does **NOT** prove \(L(E/K,\chi,1)\ne0\), the theta order 2, or a uniform integral Selmer Fitting bound. Nonvanishing theorems such as Chida–Hsieh's Theorem D may add the L-value condition under their own hypotheses for **each fixed q**, but the tower calculation alone says nothing about those analytic conditions or finite Sha. q inert in K remains outside Castella–Hsieh's split-q theorem; Theorem III proves no finite list of K can remove that coverage issue.

## Decisive implication for the global-BSD research strategy

1. The sought derived class is not missing: **it is already a theorem** (Castella–Hsieh) and in our order-two cases agrees rationally with the MW logarithmic wedge via (1). Stop demanding its reinvention.
2. A p-adic unit theta coefficient + a nonzero derived height detect **rational** Selmer corank, not the finite p-primary subgroup. The precise missing object is an integral, p-uniform **comparison to \(\operatorname{Fitt}_2(\operatorname{Sel}_{p^\infty}^\vee)\)**.
3. No finite family of split-CM quadratic fields covers ordinary primes. The infinite 53-power ring-class tower is a genuine, all-split-q solution to the *regularity* condition but does not by itself solve the inert-q or integral-Fitting tasks.
4. The exact complex identity \(L''(E,1)/2=\Omega_E\operatorname{Reg}(E)\#\Sha\) is a separate theorem obligation, not implied by any of the above p-adic equalities.

**Results established in this note:** Theorems II–IV are exact new elementary cohomological/algebraic/Chebotarev/local-class-field-theoretic deductions; Theorem I is the exact application and linear-algebra derivation of a *published* theorem to our previously certified setup. **Full BSD and all-prime Sha finiteness are NOT established.**

## Primary references

- F. Castella and M.-L. Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2*, Forum of Mathematics, Sigma 10 (2022), **Theorems A, B, 5.3, 5.5**, https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864.
- J.-P. Serre, *Quelques applications du théorème de densité de Chebotarev*, IHÉS Publ. Math. 54 (1981), https://pmihes.centre-mersenne.org/articles/10.1007/BF02698692/.
- D. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Chap. V, Theorem 4.7 (supersingular primes of non-CM E have density 0).
- Chida–Hsieh, *Special values of anticyclotomic L-functions for modular forms*, Theorem D for qualified fixed residual primes and anticyclotomic towers: https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf.
- Project previous authentic p=16231 theta/Gross archive: \`paper/bsd389_p16231_theta_order2_closed_analytic_argument_2026-11-06.md\`; \`results/bsd389_p16231_final_cubic_closure_PASS_2026-11-06.md\`.
