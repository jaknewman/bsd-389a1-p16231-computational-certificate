# E=389a1: a new fully certified real period, rational-interval Néron–Tate regulator, and BSD numerical quotient

Date: 2026-11-21. **Unconditional geometric and height results, plus a numerical BSD-ratio interval CONDITIONAL ONLY on the earlier independently user-run rigorous Arb interval for L''(E,1)/2 and the already proved Mordell–Weil basis.**

We use E: y^2+y=x^3+x^2-2x, minimal discriminant +389, rank 2 with certified saturated basis P=(-1,1), Q=(0,-1), no torsion, Tamagawa product 1, two connected real components. We do NOT use any result about one particular exceptional prime in this paper.

## Theorem 1. Exact-real geometric period enclosed to 55 decimal places

Put Y=y+1/2 and
 f(x)=x^3+x^2-2x+1/4=(x-e_1)(x-e_2)(x-e_3),
 e_1>e_2>e_3.
Its cubic discriminant is exactly 389/16>0, so there are three distinct real roots. Define

 Delta=e_1-e_3, m=(e_2-e_3)/Delta,
 K(m)=\int_0^{pi/2}(1-m sin^2 theta)^(-1/2)dtheta.

For the Néron differential dx/(2y+1)=dx/(2Y),
both real connected components have equal period
  2 K(m)/sqrt(Delta).
Thus the full BSD real period is
  **Omega_E = 4 K(m)/sqrt(Delta)
             = 2 pi/[sqrt(Delta)*AGM(1,sqrt(1-m))].**

No modular/analytic BSD statement is used here.
We independently isolate all three roots by **340 exact rational
bisections each**, use the rational Machin identity
  pi = 16 arctan(1/5)-4 arctan(1/239)
with alternating rational series and rigorous tails, and
compute the arithmetic-geometric mean with **12 outward-rounded
integer-isqrt iterations**. For intervals A_n,B_n in the AGM
recurrence, the exact mean remains between B_n and A_n.
The resulting rigorously enclosed period is:

  **4.9804251217101101506427155838846049203121163606791400801**
  **< Omega_E <**
  **4.9804251217101101506427155838846049203121163606791400802**.

The endpoints are rational decimals rounded outwards;
the program itself tracks exact Fraction bounds considerably tighter
than this printed 55-decimal interval.
It uses neither floating point nor Sage.

## Theorem 2. Explicit global canonical-height convergence bound

The actual x-coordinate duplication law on E is

  x(2R) = A(X,Z)/B(X,Z), with x(R)=X/Z,

where the *integral homogeneous quartics* are

  A=X^4+4 X^2 Z^2-2 X Z^3+3Z^4,
  B=4X^3Z+4X^2Z^2-8XZ^3+Z^4.

There are two exact polynomial Bézout identities:

  (-48X²Z-32XZ²+144Z³) A
   +(12X³-4X²Z+40XZ²-43Z³) B = 389 Z^7,

  (66Z³-520Z²X+188ZX²+389X³) A
   +(-198Z³+108Z²X-212ZX²-47X³) B = 389 X^7.

Both identities are **verified coefficient-by-coefficient** by the
companion exact-rational code. Their coefficient-one norms are 323
and 1728 respectively. For primitive (X,Z), the identities prove
  gcd(A(X,Z),B(X,Z)) divides 389
and, writing H=max(|X|,|Z|),
  H^4/1728 <= max(|A|,|B|)/gcd(A,B) <= 17 H^4.

Therefore the logarithmic naive x-height satisfies
  **-log(1728) <= h_x(2R)-4h_x(R) <= log(17)**
for every nontorsion rational point R.

Define H_NT(R)=lim_{n->infty}4^(-n)h_x(2^n R);
this is **twice** the usual canonical point height
\hat h(R) in the standard BSD bilinear pairing convention.
The telescoping bound is
  **|H_NT(R)-4^(-n)h_x(2^n R)|
           <=log(1728)/(3*4^n).**

All logarithms of the exact integer heights are enclosed
using only rational arithmetic: write M=2^k x,
x in [1,2], bound x by its top 125 binary bits,
and use the positive atanh expansion
  log(x)=2 sum_{j>=0}((x-1)/(x+1))^(2j+1)/(2j+1)
with a rigorous geometric tail bound. No floating point.

The points are P=(-1,1), Q=(0,-1), and
P+Q=(4,8). The BSD height pairing is
  <P,P>=H_NT(P), <Q,Q>=H_NT(Q),
  <P,Q>=[H_NT(P+Q)-H_NT(P)-H_NT(Q)]/2.
Its determinant is the actual saturated-basis regulator Reg_E.

Using 10 exact duplications for each of x=-1,0,4,
and including all analytic and rounding errors, the program proves

  **0.152455827790 < Reg_E < 0.152464449577**.

The decimal rounding is deliberately outward; the exact
Fraction interval is narrower. A numerical reference
0.15246017794314375... lies inside; reference consistency
is not used to derive the interval. The rational height
calculation independently confirms Reg_E>0.

## Theorem 3. Certified global archimedean BSD numerical quotient

The user's previously executed certified Sage Arb integration
in results/full_BSD_phase1_Arb_Lstar_interval_PASS_2026-10-19.md
rigorously encloses
   L''(E,1)/2 in [0.7593165002884268 +/- 7.81e-17].
We deliberately WIDEN this to the rational interval
   **L''(E,1)/2 in [0.7593165002884267,0.7593165002884269]**.
This applies after the user's separate EXACT modular-symbol
proof L(E,1)=0 and the certified functional equation of sign +.

Form the true numerical quotient
  R_BSD = [L''(E,1)/2]/[Omega_E*Reg_E]
        = L''(E,1)/(2 Omega_E Reg_E)
because torsion and Tamagawa factors are both 1.

Outward rational interval evaluation with the independently
certified factors proves:

  **0.999971982756 < R_BSD < 1.000028533857**.

This is the first complete, independently interval-certified
ARCHIMEDEAN RATIO gate in the project. It is a theorem of
real-number numerical analysis, not a BSD identity.

**Conditional integer consequence:** If the FULL BSD
leading-term formula holds (including finiteness of Sha),
then R_BSD=#Sha(E/Q) must be a positive integer. Since the
entire certified interval lies in (0,2) and contains only
the integer 1, the identity would FORCE

  **Sha(E/Q) = 0**.

This is a one-way implication from FULL BSD, not
a proof that BSD is true. We do NOT assume that R_BSD
is rational, integer or has a bounded denominator.
The certified numerical proximity of two real numbers,
however close, cannot prove their exact equality.

## What is still genuinely missing

1. A proof of finite prime support and finite exponent of
   Sha(E/Q), independent of the BSD leading-term formula.
2. A rank-two complex leading-term identity equating
   L''(E,1)/2 EXACTLY to Omega_E Reg_E times the proven
   finite arithmetic order. Such an identity is not
   provided by precise numerical integration, height
   computation, or the current general Kato system.

In particular an eventual two-prime unit Kurihara theorem
for all large p would address prime support but would
NOT automatically prove this complex leading-term identity.
Likewise, even proving Sha(E/Q)=0 would not turn the
certified ratio interval into an exact identity.

## Reproducibility

Three pure standard-library Python scripts, no Sage:
- verification/bsd389_real_period_exact_rational_agm_20261121.py
- verification/bsd389_canonical_regulator_exact_duplication_20261121.py
- verification/bsd389_global_archimedean_ratio_rational_interval_20261121.py

Run the third with all three in the same folder:
  python verification/bsd389_global_archimedean_ratio_rational_interval_20261121.py

The scripts were executed successfully in the assistant's
container on 2026-11-21. Typical execution for 10-height
duplications is about 20 seconds on the available machine,
driven by exact million-bit rational-number arithmetic.
The interval endpoints above came from actual stdout.
The earlier Arb Lstar is user-reported and archived,
not independently re-integrated in this turn.
