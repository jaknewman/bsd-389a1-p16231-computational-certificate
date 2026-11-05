# The fixed-K auxiliary-character gate via the 53-anticyclotomic tower

2026-11-06. E=389a1, K=Q(sqrt(-3)), target Selmer prime ell=16231, auxiliary tower conductor prime q=53.

**Aim.** Apply Chida--Hsieh, Special values of anticyclotomic L-functions for modular forms, Theorem D / 5.9, with their *tower prime* p=q=53 and their *residual prime* ell=16231. This does NOT confuse those two primes. Prove that among the nonvanishing ring class characters guaranteed by the theorem there is one with chi(pbar_16231)!=1, giving distinct p=16231 roots for the weight-one auxiliary CM theta form.

## 1. Exactly matching Theorem D

E has N=389 and p=53 good ordinary, a_53=-6, nonzero mod53. Its finite CM field is K=Q(sqrt(-3)), D_K=-3, and 53 is inert (53≡2 mod3). Nminus=389 is inert in K (389≡2 mod3), squarefree, one prime, with (D_K,Nminus)=1.

The theorem's hypotheses:
- conductor-tower 53 satisfies 53^2 not dividing N=389;
- (D_K,Nminus)=1;
- residual ell=16231 does not divide 53*389*3, and ell>2-2=0;
- residual representation E[16231] is absolutely irreducible.

A direct group-theoretic proof of the last point: a reducible E[ell] gives a Q-rational cyclic ell-isogeny; ell=16231 is excluded by Mazur's theorem. Further E is semistable split multiplicative at389 with v_389(Delta_min)=1. The Tate curve inertia image therefore contains a nontrivial mod-ell transvection of order ell. By the elementary/Dickson classification of subgroups of GL2(F_ell), an irreducible subgroup containing such a transvection contains SL2(F_ell); determinant is the surjective mod-ell cyclotomic character, hence the image is GL2(F_ell). In particular the residual representation is absolutely irreducible.

Then CH Theorem D yields: for all but finitely many finite order characters chi of the 53-primary anticyclotomic extension Gamma_53^- of K, the central Rankin value L(E/K,chi,1) is nonzero (the published statement even gives nonvanishing modulo the residual ell).

## 2. Frobenius at the target prime has infinite 53-adic order

Write O_K=Z[omega], omega^2+omega+1=0 and Norm(a+b*omega)=a^2-a*b+b^2.
An exact norm representation of the target prime is

pi=145+51*omega,  Norm(pi)=145^2-145*51+51^2=16231.

Its conjugate is pi_bar=94-51*omega. The principal prime ideals (pi) and (pi_bar) are different: the explicit six units +-1,+-omega,+-omega^2 do not carry pi to pi_bar, and p=16231 splits.

Since K has class number 1, the ring class group of conductor 53^n is the local quotient

Pic(O_{53^n}) = (O_K/53^n)^* /
  ((Z/53^n)^* * image(O_K^*)).

The 53-primary part of the inverse limit is Gamma_53^- isomorphic to Z_53: because 53 is inert, the local norm-one principal-unit direction has one Z_53 dimension.

The Artin image of (pi) is the class of pi in this quotient, with inverse or conjugate depending on geometric reciprocity. If it had finite order in Gamma_53^-, the norm-one component of pi/pi_bar in K_53^* would have trivial 53-adic logarithm and hence be a 53-adic root of unity. Since pi/pi_bar belongs to the global number field K, being a root of unity in K_53 would imply it is an algebraic root of unity in K. That is impossible: the principal fractional ideal (pi/pi_bar) has different nonzero valuations at the two primes over16231. Thus this Artin element is nonzero of infinite order in Gamma_53^-.

Consequently for all characters chi of sufficiently large 53-power conductor, chi((pi)) !=1 and likewise chi((pi_bar))!=1. Indeed a nonzero t in Z_53 is 53^e times a unit; a character of order 53^n with n>e has nontrivial value at t.

## 2b. Stronger explicit mod-53² certificate (no logarithm ambiguity)

The above infinite-order argument is sharpened by a **finite, exact computation**. For pi=145+51*omega, put v=pi/pi_bar=pi²/16231 in the unramified local ring K_53. Writing v in the basis (1,omega), integer arithmetic modulo 53²=2809 gives

v=(2306,269) modulo 2809,
v^54=(425,848)=1+53*(8+16*omega) modulo 2809.

The residual norm-one subgroup over F_53 has order 53+1=54. Raising to 54 kills its prime-to-53 residue component. The first nonzero principal-unit tangent 8+16*omega has trace 2*8-16=0 mod53 and is NOT zero. Because the norm-one principal units form a one-dimensional Z_53 module, this proves that the pro-53 part of v is a **topological generator** rather than merely a nonzero element. Therefore every nontrivial 53-power-order character of this anticyclotomic tower is regular at the split target prime16231.

The complete finite certificate is verification/bsd389_p16231_aux53_frobenius_generator_gate.py. Its user-run PASS is not yet recorded; the residue computations (v, v^54) were independently reproduced by exact Python arithmetic during drafting.

## 3. Existence with BOTH central nonvanishing and regularity

Theorem D excludes only finitely many chi for which L(E/K,chi,1)=0. The Frobenius argument excludes only finitely many characters in the 53-power tower for which chi((pi_bar))=1. Their intersection complement is infinite.

Choose chi among this infinite set, with
L(E/K,chi,1) !=0,
chi(pbar_16231) !=1.

Since chi has odd 53-power order and is anticyclotomic, let psi be its unique square root, psi^2=chi. Then psi^tau=psi^(-1) and chi=psi/psi^tau. The associated weight-one CM theta newform g=theta_psi has distinct p=16231 Hecke roots alpha_g=psi(pbar), beta_g=psi(p), since their ratio is chi(pbar)!=1. Its conductor is prime to 389 and16231.

The separately executed rational-interval certificate proves
4.51 < L(E^K,1) <4.60.
Hence L(E,ad^0(g),1)=L(E^K,1)*L(E/K,chi,1) !=0.

This supplies precisely the auxiliary data required in Castella--Hsieh Theorem A and Theorem B without an explicit numerical evaluation at the first conductor53 character.

## 4. Arithmetic consequence once theta order2 is established

Other Theorem A hypotheses for E=389a1, p=16231:
global E sign+1, L(E,1)=0 (by rank2 and rank-zero theorem),
p good ordinary (a_p=128),
rho_bar irreducible and ramified at Nminus=389,
Nminus one inert squarefree prime,
rank E(Q)=2>0.

Therefore the order-two theta criterion plus Theorem B gives kappa_{α,α^{-1}} !=0 for this suitably selected CM weight-one g. Theorem A then gives dim_(Q_16231) Sel(Q,V_16231 E)=2. Kummer and proven MW rank2 yield finite Sha(E/Q)[16231^infinity].

***Boundary***: this does not assert Sha(E/Q)[16231^infinity]=0 and certainly not the full BSD leading-coefficient identity. The proof also depends on the exact finite-to-infinite theta identification in the companion paper; a numerical/finite check cannot replace that identification. A standalone academic review of the theorem hypotheses and class-field argument remains prudent before claiming unconditional theorem-level certification.

## Sources

Castella & Hsieh, 2022, Theorem A, Theorem B, Appendix section6:
https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864

Chida & Hsieh, Special values of anticyclotomic L-functions for modular forms, Theorem D and Theorem 5.9:
https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf
