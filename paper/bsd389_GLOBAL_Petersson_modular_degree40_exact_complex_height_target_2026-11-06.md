# Exact global Petersson-period identity for BSD 389a1

Date: 2026-11-06. A prime-INDEPENDENT nonconjectural identity of complex periods, not a proof of Sha finiteness or rank-two BSD.

## Proven input

E/Q: y^2+y=x^3+x^2-2x, conductor N=389, minimal invariant differential omega=dx/(2y+1), discriminant +389 and two real components. Let f in S_2(Gamma_0(389)) be the normalized eigenform, and let phi:X_0(389)->E be the optimal modular parametrization.

Its exact modular degree is 40: Sage sympow documentation states sympow.modular_degree(EllipticCurve('389a'))=40, independently consistent with the one-dimensional factor of J_0(389) in Stein's computations. Its Manin constant c_E=1 follows from the theorem for optimal semistable elliptic curves of Česnavičius, so phi*omega = +/-2*pi*i*f(z)dz.

Define Petersson inner product <f,f> = integral_(Gamma_0(389)\H) |f(z)|^2 dx dy, weight-2 convention. Let omega_R and omega_I be the primitive positive real and imaginary period lengths, with period lattice omega_R Z + i omega_I Z. The total real Neron period equals Omega_E=2 omega_R. The companion exact rank-zero modular-symbol result in PR #12 gives L(E^(-3),1)=4 omega_I/sqrt(3) and Omega_(E^-3)=2 omega_I/sqrt(3).

## Theorem 1 (exact degree/area identity)

40 omega_R omega_I = 4*pi^2 <f,f>.

Proof: The invariant area form (i/2)*omega wedge conjugate(omega) integrates over E(C) to the period lattice area omega_R omega_I. Pullback through the finite-degree phi multiplies its total integral by degree=40. On the upper half plane, inserting phi*omega=2*pi*i*f(z)dz makes the pullback area 4*pi^2*|f|^2 dx dy. The latter integrates to 4*pi^2 <f,f> on the fundamental domain. QED.

## Corollary 2 (exact new period and twist transfer)

Omega_E * L(E^(-3),1) = (4*pi^2/(5*sqrt(3))) * <f,f>.
Omega_E * Omega_(E^-3) = (2*pi^2/(5*sqrt(3))) * <f,f>.

Proof: Omega_E L_twist = (2 omega_R)*(4 omega_I/sqrt3) = (8/sqrt3)*(pi^2/10)<f,f>, using Theorem 1. The second identity uses Omega_twist=2 omega_I/sqrt3. QED.

## The actual rank-two target, now with an EXACT modular normalisation

By Artin factorization,
L''(E/K,1)/2 = L(E^(-3),1)*L''(E,1)/2, K=Q(sqrt(-3)).
Let Q_E=(L''(E,1)/2)/(Omega_E Reg_E). Then
(L''(E/K,1)/2)/(<f,f>*Reg_E) = (4*pi^2/(5*sqrt3))*Q_E.

Hence Q_E=1 is EQUIVALENT to the global rank-two Petersson/height identity:
(L''(E/K,1)/2)/(<f,f>*Reg_E) = 4*pi^2/(5*sqrt3).

**IMPORTANT:** This last identity is NOT proved here. It is just an EXACT equivalence reexpressing the still-unproved rank-two BSD leading term with the correct coefficient and no local p ambiguity. It would require a new rank-two archimedean Gross-Zagier/derived-height reciprocity theorem for this curve. A numerical agreement, Kato local certificate, or a rank-one Gross-Zagier result does not establish it.

No all-prime integral Selmer Fitting integer, Sha finite support, or complete BSD is claimed.

Sources: https://sources.debian.org/src/sagemath/10.10-2/src/sage/lfunctions/sympow.py ; https://paperzz.com/doc/7955077/computing-with-modular-symbols--modular-forms ; Česnavičius, The Manin constant in the semistable case (2018); previous exact twist period and L-value proof in this branch.
