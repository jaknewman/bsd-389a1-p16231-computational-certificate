# E389a1 p=107: Pollack logarithm and signed Selmer, exact quadratic comparison

Date 2026-11-16. Scope: exact formal derivation conditional on authentic Manin normalization and matching the analytic function to the published integral main conjecture. No new global Sha finiteness.

## 1. Primary identities and sign identification

Take p=107, alpha^2=-p, T=gamma-1 with gamma=1+p. The Sage supersingular p-adic L-series has two coordinates L_{p,alpha}=G(T)+alpha H(T). Its plus modular-symbol measure at conductor p^3 is

mu(a+p^3 Z_p) = alpha^{-3} m^+(a/p^3) - alpha^{-4} m^+(a/p^2),

divided by the number of real components (2). Thus the coefficient T^2 in the n=3 approximation is

[T^2] L_{p,alpha}^{(3)} = (alpha A3 - B3)/(2p^2),

where B3 = sum_{a mod p^3 unit} binom(j_3(a),2) m^+(a/p^2). In particular [T^2]G^(3) = -B3/(2p^2), independently of A3.

Kurihara–Pollack, Two p-adic L-functions and rational points on elliptic curves with supersingular reduction, equations (3)-(4) and section 1.5:
L_{p,alpha}=f(T) log_p^+(T)+alpha g(T) log_p^-(T),
char_Lambda(X^-)=(f(T)) in their convention. Here
log_p^+(T)= (1/p) product_{n>=1} (Phi_{2n}(1+T)/p),
so log_p^+(0)=1/p. If ord_T f>=2, then [T^2]f=p[T^2]G. This correctly tracks scalar G -> f -> MINUS signed Selmer, notwithstanding the + in log_p^+.

Sources: https://math.bu.edu/people/rpollack/Papers/Two_padic_Lfunctions_and_rational_points_on_elliptic_curves_with_ss_reduction.pdf ; https://math.bu.edu/people/rpollack/Papers/On_the_padic_Lfunction_of_a_modular_form_at_a_ss_prime.pdf ; https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/schemes/elliptic_curves/padic_lseries.py

## 2. All p^3 lifts reduce to one p^2 moment

For each b in (Z/p^2)^x, its p lifts to mod p^3 have exponents j_3=j_2(b)+p*k mod p^2, k in F_p. Thus sum over k of binom(j_3,2) = p binom(j_2(b),2) mod p^2, so B3=p*C2 mod p^2.

The new independently enumerated finite arithmetic gives C0=C1=0 and C2=86 mod 107 (5671 symmetry pairs and discrete-log matches). Therefore
p[T^2]G^(3) = -B3/(2p) = -86/2 = 64 mod 107.

## 3. Precision

Sage's supersingular n=3 degree-2 coefficient is controlled up to O(alpha^{-1}) in alpha-adic precision. The scalar part of alpha^{-1} O_{Q_p(alpha)} lies in Z_p; multiplying by p improves scalar precision to O(p). Therefore the analytic scalar coefficient obeys p[T^2]G ≡64 mod107, PROVIDED the archived 390-symbol vector represents the same normalized plus modular symbols as Sage's measure at conductor 107^2. This is the remaining input comparison; the p^3 cusp sum is not needed for this congruence.

Once ord_T f>=2, the formula log_p^+(0)=1/p gives [T^2]f ≡64 mod107.

## 4. Algebraic rank-two closure criterion

Assume the authentic normalization comparison above; the semistable supersingular integral signed main conjecture matches f with X^-; B.D. Kim's no-finite-Lambda-submodule theorem applies; and base-field Selmer injects into signed Gamma-invariants while its saturated rank-two MW group is included.

Then rank-two MW implies ord_T(char_Lambda(X^-))>=2, hence f has no T^0 or T^1 terms. Its T^2 coefficient is a p-unit, hence f=T^2*unit and char_Lambda(X^-)=(T^2). With no finite Lambda-submodule, the torsion Lambda-module X^- injects into a Z_p-free rank-two module. Its Gamma coinvariants have rank at least 2 by the MW subgroup, so T acts trivially on X^- tensor Q_p and thus X^- itself. Therefore signed Gamma-invariants are (Q_p/Z_p)^2 and equal the base MW subgroup; base Selmer has no excess and Sha(E/Q)[107^infty]=0.

This theorem-level implication must NOT be presented as independently certified for p107 until the vector-to-Sage analytic normalization and exact external theorem hypotheses are fully checked. The historical independent p107 Sage Sha certificate remains distinct.

## 5. Uniformity boundary

This is a one-prime criterion and not a single integer D annihilating all Sha. All-prime Sha finiteness and the complex rank-two BSD leading coefficient are not deduced.
