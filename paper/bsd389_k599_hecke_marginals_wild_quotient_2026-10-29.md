# BSD 389a1: Hecke marginal cancellation and wild quotient of the Kurihara coefficient

**Date:** 2026-10-29. **Status:** rigorous algebraic implication from standard Hecke distribution and the certified auxiliary-prime data. Small-prime Sage regression supplied but not yet user-executed. This is NOT an accelerated algorithm and not a Sha certificate.

## The exact Hecke fibre identity

Let E=389a1 and let S(r)=[r]^+ be the integrally normalized plus modular symbol, periodically extended to rational r. For primes q1!=q2 away from N=389 and b in (Z/q1)^*, put n=q1*q2. The standard weight-two Hecke relation is

 a_(q2) S(r) = S(q2*r) + sum_(j=0)^(q2-1) S((r+j)/q2).

Use r=b/q1, and remove from the sum the unique numerator a=b+j*q1 that is divisible by q2. Its symbol becomes S(q2^(-1)*b/q1). Therefore

 sum_(a mod n, (a,n)=1, a=b mod q1) S(a/n)
 = a_(q2)*S(b/q1) - S(q2*b/q1) - S(q2^(-1)*b/q1).

All rational arguments are understood modulo Z. This identity is exact over the coefficient ring of the normalized modular symbol and has a corresponding q1/q2-swapped version.

## Forced vanishing of the constant and first logarithmic moments

Fix p>=5 with q_i = 1 mod p and a_(q_i)=q_i+1=2 mod p, as holds at p=599 for q1=6912461 (a_q1=1799=2+3*599) and q2=13963889 (a_q2=-4191=2-7*599).

Let ell_i:(Z/q_i)^* -> F_p be additive discrete logs and S(a)=S(a/n) mod p on units, 0 otherwise. Sum the Hecke fibre formula (i) without weights and (ii) with ell_1(b). In (ii), multiplication by q2 and q2^(-1) shifts the logarithm by opposite constants, which cancel. Hence exactly modulo p,

 M0 = sum_(a in units mod n) S(a) = 0,
 M1 = sum_a ell_1(a)*S(a) = 0,
 M2 = sum_a ell_2(a)*S(a) = 0.

More precisely, M1 = (a_q2-2) * sum_(b in units mod q1) ell_1(b)*S(b/q1) mod p; M2 = (a_q1-2) * sum_(b in units mod q2) ell_2(b)*S(b/q2) mod p.

For all units t mod n, after replacing b=t*a and expanding ell_i(t^(-1)*b)=ell_i(b)-ell_i(t), the mixed moment is *multiplicatively translation-invariant*:

 sum_a ell_1(a)*ell_2(a)*S(t*a)
 = sum_a ell_1(a)*ell_2(a)*S(a) mod p.

This is a global exact congruence but does not determine the common value.

## Quotient by the tame prime-to-p subgroup

Both q_i-1 are divisible by p exactly once: q1-1 = 599*11540 and q2-1 = 599*23312. Let H_i be the subgroup of p-th powers of F_qi^*, of order m_i=(q_i-1)/p. The product H=H1*H2 has order m1*m2=269020480; each ell_i is constant on its cosets. Therefore the unit group admits a quotient G/H isomorphic to (Z/p)^2 with p^2=358801 cosets.

For u,v in F_p define
 T_(u,v) = sum_((a,n)=1, ell_1(a)=u, ell_2(a)=v) S(a/n) mod p.
Then the exact Kurihara coefficient is

 delta_n = sum_(u,v in F_p) u*v*T_(u,v).

Define the wild quotient theta polynomial
 F(X,Y)=sum_(u,v) T_(u,v)*(1+X)^u*(1+Y)^v mod (p,X^2,Y^2).
The Hecke marginals imply
 F(X,Y) = delta_n*X*Y mod (p,X^2,Y^2).

Thus the desired value is precisely the *one mixed coefficient of a four-dimensional truncated algebra*. There are only 358801 tame quotient classes, but EACH such class contains 269020480 original residues.

## Computation and limitations

This algebra describes the exact p-primary projection of the Mazur-Tate element. **It does not reduce the time needed to evaluate the tame orbit sums T_(u,v)**. Materializing all T_(u,v) by direct summation still requires 96524817244480 unit evaluations (48262408622240 using even sign symmetry). Similarly, the separate additive Fourier trace presentation has 14376 scalar targets versus the original 390 Manin-edge weights; lower-dimensional output does not imply a faster algorithm.

The correct next problem is an explicit arithmetic oracle for the tame norm of the modular symbol, or an equivalent transfer/Hecke algorithm that computes the coefficient of X*Y without enumerating the huge tame cosets.

**New small-prime test, currently not user-run:** verification/bsd389_kurihara_hecke_moment_translation_p5.py. It checks all 40 and 60 Hecke fibres for q1=41,q2=61, zero lower moments, delta_2501=4 mod5, and invariance under t=2,7,17,599 using actual Sage/eclib symbols.

Original implementation of direct Kurihara sums: Alexandru Ghitza and Chan-Ho Kim, https://github.com/aghitza/kurihara_numbers (direct sum over unit numerators).
