# Universal C01–Sage n=3 minus n=2 correction: algebraic audit

Date: 2026-10-26. **Claimed scope:** an algebraic congruence for the Sage 10.9 ordinary distribution *under the stated modular-symbol, period, and Hecke identities*. It is not a full independent replacement for eclib or for the high-p Shapiro source-to-reference proof.

Let p be an odd prime of good ordinary reduction, alpha the p-adic unit root of X²-a_p X+p, and m the plus modular symbol in Sage's `L_ratio` normalization. Set gamma=1+p, n=2,3, and let mu_n(t)=alpha^(-n)[m(t/p^n)-alpha^(-1)m(t/p^(n-1))]. Work modulo p² in the quadratic coefficient of the trivial Teichmuller branch, with twist D=1. Assume the real-components factor is 2 and the period quotient is 1, as checked for 389a1. All rational modular symbols must be p-integral.

## Step 1. Cyclotomic lifts

Every x in (Z/p²Z)^x has a unique representation x=omega(a) gamma^u (mod p²), where 1<=a<p and 0<=u<p. Write x=a+pb, let omega(a) be the Teichmuller lift mod p³, and define kappa=(omega(a)*gamma^u-x)/p² (mod p). For c mod p, y=x+p²c has exponent j=u+pv (mod p²), with v=(c-kappa)*a^(-1) mod p, because gamma^(pv)=1+p²v (mod p³) and omega(a)=a (mod p).

The binomial weight difference has the exact congruence

`binom(j,2)-binom(u,2) = p*v*(2u-1)/2 (mod p²)`.

Define `w=(2u-1)*a^(-1) mod p`. The correction in the sum of binomial moments is therefore `p*w*(c-kappa)/2 mod p²`.

## Step 2. Distribution

For the good ordinary measure and every fixed x (mod p²), its finite distribution relation is

`sum_{c=0}^{p-1} mu_3(x+p²c)=mu_2(x)`.

This follows from the defining measure, the level-389 Hecke relation for the normalized modular symbol, and `alpha²-a_p*alpha+p=0`. The relation is essential: it cancels the level-2 `binom(u,2)` contribution exactly when the level-3 fibers are grouped over x.

Sage's `series(n=3,prec=3)` divides the plus-symbol sum by `E.real_components()=2`. Combining with the `1/2` in the preceding binomial identity gives the `1/4` factor:

`A2^(3)-A2^(2) = (p/4) sum_{a,b} w sum_c (c-kappa) mu_3(x+p²c) (mod p²)`.

## Step 3. Collapse to two Shapiro moments modulo p

Let Dx be the integral matrix `[1,x;0,p²]`, beta_c `[1,c;0,p]`, and P `[p,0;0,1]`. Define `F(D)=m(D.infinity)-m(D.0)` and `M0(D)=F(D)-alpha^(-1)F(PD)`, `M1(D)=alpha^(-1)sum_c c F(beta_c D)`.

The matrix/cusp orientations are `F(Dx)=-m(x/p²)`, `F(P Dx)=-m(x/p)`, `F(beta_c Dx)=-m((x+p²c)/p³)`. As `sum_c(c-kappa)=0 mod p`, the lower m(x/p²) term in mu_3 drops out when multiplied by these weights. Multiplying by alpha² gives

`alpha² sum_c (c-kappa)mu_3(x+p²c) = -[M1(Dx)-kappa*M0(Dx)] (mod p)`.

Here the Hecke relation `sum_c F(beta_c Dx)+F(PDx)=a_p F(Dx)`, along with `alpha≡a_p (mod p)`, identifies `alpha^(-1)sum_c F(beta_c Dx)≡M0(Dx) mod p`. The formula's sign uses the cusp orientation F(D)=m(infinity)-m(D.0), not its reverse.

Define the reference full scalar independently of every particular implementation:

`J_ref = -sum_{a=1}^{p-1}sum_{b=0}^{p-1} w(a,b)[M1(Dx)-kappa(a,b)M0(Dx)] (mod p)`.

Combining the previous lines proves the source-convention congruence

`A2^(3)-A2^(2) = p*J_ref/(4*alpha²) (mod p²)`.

### Scope, computational gates, and regression evidence

- All three algebraic steps apply to general odd good ordinary p **under the listed assumptions**; the 1/4 is not a fitted constant.
- The level-3 global Sage series at p=16231 was not directly evaluated. Its coefficient precision bound `_prec_bounds(3,3)[2] = 2` and necessary normalization are separate source-level gates.
- The equivalence between the actual `verification/independent_c01_scalar_J.cpp` and the mathematical J_ref invokes the audited continued-fraction / Manin / Shapiro transport algebra; independent full-domain computations agree on J=4486 modulo 16231 but still share V65 eclib and original Manin export.
- At p=5: alpha=7 mod25, A2(n2)=14, A2(n3)=24, J=2 mod5, correction=10 mod25; direct level3 agrees with Sage series.
- At p=7: alpha=16 mod49, A2(n2)=19, A2(n3)=33, J=4 mod7, correction=14 mod49; direct level3 agrees with Sage series.
- At p=16231: two full independent J runs give 4486; two full level2 runs give 1199p; two height algorithms give B_p/p=9534. Hence **if** the preceding universal identity and source-to-J_ref computations are faithful, A2(n3)/p=1199+8335=9534 modulo p, which gives a p-adic unit quotient. Applying the documented Kato/Sage p-primary upper bound requires all its hypotheses; the function itself was not executed.

Nothing here proves exact equality of a p-adic BSD quotient with 1, the all-prime BSD conjecture, or the complex leading-term formula.

Primary sources pinned to SageMath 10.9: `src/sage/schemes/elliptic_curves/padic_lseries.py` methods `measure`, `pAdicLseriesOrdinary.series`, `_prec_bounds`; `src/sage/schemes/elliptic_curves/sha_tate.py` methods `an_padic`, `p_primary_bound`.

Executed small-prime certificate: [p5 and p7 direct Sage-level3 regressions](../results/bridge_small_primes_5_7_direct_n2_n3_sage_PASS_2026-10-26.md). Existing full bridge: [original C01–Sage source-derived identity](c01_to_sage_quadratic_coefficient_identity_2026-10-24.md).
