# Sha[16231-infinity] via the generalised Kato theorems: precise conditions

Date 2026-11-06. E=389a1, K=Q(sqrt(-3)), p=16231.

## Input from the new finite Gross certificate and the published theta comparison

The full H=87809710 normalized p2 Gross points yield finite theta (modp) with b0=b1=0 and b2=3739!=0, with exact orientated CM closure and unique primitive 33-class Hecke eigenline. The p2 right ideal lattice matches the Castella--Hsieh Appendix §6 definition after scalar p2, and the P1 term vanishes modulo p in degrees0..2. Their congruence modulo ((1+T)^p-1) transfers the p-unit b2 to the actual infinite theta.

The trivial-character interpolation forces b0=0 exactly, as E has rank2 and L(E,1)=0 by the rank-zero theorem. The Chida--Hsieh involution with Nplus=1 and good-p local root sign +1, plus E global root sign +1, forces b1=0 exactly. Hence ord_T Theta_{f/K}=2, subject to the precise ideal-class identification already discussed in the accompanying proof note.

## Hypotheses for Theorems A+B

Consult the 2022 paper Theorem A at section1.2 and Theorem B. The needed assumptions are:

- p>3 good ordinary. Yes: a_p(E)=128 mod16231, so p is good ordinary.
- E global functional-equation sign +1 and L(E,1)=0. Yes, exact Sage root sign plus established rank2 and rank0 theorem.
- Auxiliary ring-class character chi of K for which L(E^K,1)*L(E/K,chi,1) != 0 and chi(pbar) !=1, so the weight-one theta form g=theta_psi has distinct p-stabilization roots.
- Residual representation irreducible. For a rational elliptic curve a reducible E[p] gives a rational p-isogeny. Mazur's prime-isogeny theorem excludes p=16231, hence irreducible.
- Nminus squarefree, odd number of inert factors. Nminus=389, yes, because 389≡2 (mod3).
- Residual ramification at 389. The curve has split multiplicative reduction and v_389(minimal discriminant)=1, so tame inertia on E[p] is nontrivially unipotent for p!=389 and p not dividing1.
- E(Q) rank>0. Proven rank2.

## Twist central value from a separately executed exact arithmetic certificate

The independent Fraction-only program
verification/bsd389_Kminus3_rankzero_Lvalue_exact_interval.py
proved 4.51 < L(E^K,1) < 4.60 using the absolutely convergent exponentially weighted approximate functional equation with rigorously bounded coefficients and tail. Its result was executed by the assistant in the container on 2026-11-06. In particular the twist factor in Theorem A is nonzero.

## Auxiliary character is the final explicit selection issue

Castella--Hsieh Appendix §6 states that for EVERY triple with the indicated field conditions (including nonzero quadratic twist), existence results of Vatsal and Chida--Hsieh furnish infinitely many ring-class characters chi of ell-power conductor coprime to Np with L(E/K,chi,1)!=0. The statement of their Theorem A additionally requires a regular weight-one p-stabilisation, equivalent to chi(pbar)!=1. One must either identify a specific character (e.g. the conductor-53 candidate previously constructed) with both properties, or cite a strengthened existence statement which guarantees the regularity restriction for the fixed p. Do not substitute the mere existence of some nonvanishing character for this technical condition without argument.

Once an appropriate chi is chosen, Theorem B gives a nonzero generalized Kato class kappa; Theorem A then gives
dim_(Q_p) Sel(Q,V_pE)=2.

The Kummer exact sequence identifies the difference between p-adic Selmer dimension and Mordell-Weil rank with the Z_p-corank of the p-primary Tate--Shafarevich group. Since rank E(Q)=2, this difference vanishes and the cofinitely generated p-primary group Sha(E/Q)[p^infinity] is finite. This says NOTHING about Sha[p^infinity] being zero: an arbitrary nontrivial finite p-group is consistent.

Even a rigorous finiteness theorem for Sha at p=16231 does not prove full BSD, nor the p-adic valuation of |Sha|. The latter requires additional integral main-conjecture, regulator and leading-term information.

## References

F. Castella and M.-L. Hsieh (2022), On the nonvanishing of generalised Kato classes for elliptic curves of rank 2, Theorems A, B, section6 Appendix; https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864

M. Chida and M.-L. Hsieh, Special values of anticyclotomic L-functions for modular forms, Theorem B (functional equation), 2018; https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf
