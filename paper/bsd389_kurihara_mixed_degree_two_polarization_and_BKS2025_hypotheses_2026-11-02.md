# Exact three-projection polarization of degree-two Kurihara coefficients; BKS 2025 theorem audit

Date: 2026-11-02. Curve: E389a1, rank 2.

## 1. New exact elementary polarization lemma (valid for any odd p)

Let R=F_p[X,Y]/(X^p,Y^p), and define for F in R the three polynomial substitutions F(T,T), F(T,0), F(0,T), read modulo T³ (p>=3). Then

**[XY]F = [T²] {F(T,T) - F(T,0) - F(0,T)}.**

Proof: a monomial X^a Y^b contributes to the right-hand side's degree 2 iff a+b=2, with both a,b>0 after cancellation of pure monomials, so only (a,b)=(1,1) survives. Constant term contributes -constant but not degree 2, so no assumption F in (X,Y)^2 is needed.

Apply to Theta_n = sum_{a in (Z/n)^×} [a/n]^+ sigma_a with properly p-integral Néron-normalized modular symbols and primitive-root discrete logs e_i(a) modulo p. Let F=Phi_p(Theta_n) where Phi_p(sigma_a)=(1+X)^e1(a)(1+Y)^e2(a). Define cyclic projections

Q_{u,v} = [T²] sum_a [a/n]^+ (1+T)^{u e1(a)+ v e2(a)}

for (u,v)=(1,1),(1,0),(0,1), with exponents reduced modulo p. Then

delta_(q1 q2) = Q_(1,1) - Q_(1,0) - Q_(0,1) (mod p).

Proof alternatively uses binom(e1+e2,2)-binom(e1,2)-binom(e2,2)=e1 e2 mod p, since p odd. The map sigma_(a,b) -> (1+T)^(u a+v b) is a legitimate group algebra homomorphism to F_p[T]/T^p; no unnoticed low-augmentation-term hypothesis is required.

This is a new *reformulation and independent audit route*, not a new global nonvanishing theorem. Its three cyclic sums are not automatically easier to evaluate at 70.98 billion indices and one must not claim a native replay or a verified p107 cyclic projection without actually computing them. For the frozen p107 archive, the previously reconstructed mixed coefficient is 34, so the three cyclic projections **should** obey Q11-Q10-Q01=34 if evaluated with the archived original symbols. No values of Q11,Q10,Q01 have been calculated.

### Local assistant-side validation

The binomial polarization equation was checked with standard integer arithmetic on 20 deterministic five-term input examples for each p=5,7,107 (60 examples total): `POLARIZATION_PASS 5 20`, `POLARIZATION_PASS 7 20`, `POLARIZATION_PASS 107 20`. This checks only algebraic identity, NOT the curve's modular symbols.

## 2. Primary-source audit: Burns–Kurihara–Sano 2025

D. Burns, M. Kurihara, T. Sano, *On Derivatives of Kato's Euler System and the Mazur-Tate Conjecture*, International Mathematics Research Notices 2025(4), rnaf012 (published 14 February 2025):
https://doi.org/10.1093/imrn/rnaf012

Accepted paper and earlier author version:
https://nms.kcl.ac.uk/david.burns/web_page/bks5.pdf

The paper **constructs an explicit comparison** between Kato zeta elements, Selmer complexes/Bockstein maps, and Mazur–Tate modular elements (sections 4–5). Therefore it is incorrect to claim that *all* cohomological comparison is missing. However:
- Theorem 4.1 proves Algebraic Generalized Perrin–Riou Conjecture (Conjecture 3.4) => Mazur–Tate under Hypothesis 2.2. It does not establish Conjecture 3.4 unconditionally for E389a1 in rank 2.
- Theorem 1.1 further explicitly assumes classical BSD for E/Q and Generalized Perrin–Riou Conjecture for relevant p. Using it to *prove* BSD or Sha finiteness would be circular.
- The unconditional Corollary 1.2 is specifically an **analytic-rank-one** case; E389a1 of rank 2 is not in its scope.
- The leading coefficient of Mazur–Tate degree 2 is a class in I(G)^2/I(G)^3 and its expected expression via regulator and finite arithmetic groups should not be asserted as an unconditional equality for rank 2.

### Actual proof frontier

What remains for a uniform rank-two Sha theorem is not a mere identification of delta as the mixed coefficient or a construction of an abstract map: it is **non-circular p-uniform primitivity** of the degree-two image, or an independent integral bound on the relevant Selmer/Fitting ideal. None follows from the polarization lemma, from the 2025 conditional theorem, or from the finitely many already certified primes.

## 3. No full BSD claim

The genuine Sage p-primary vanishing certificates for 2,5,7,11,13,107 and literature-based p3 witness remain as previously recorded. This note proves no all-prime Sha finiteness or complete strong BSD.
