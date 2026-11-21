# E389a1: fast rigorously certified Néron–Tate regulator and a 2.7e−16 BSD numerical ratio window

2026-11-21. **Positive unconditional arithmetic result** for the regulator,
and a rigorous analytic-to-arithmetic ratio interval conditional ONLY on
the independent user-executed October 2026 Arb enclosure for L''(E,1)/2.
Neither the finiteness of full Sha nor the exact complex BSD formula is used.

We do not revisit any already completed particular-prime component.
This document concerns only the GLOBAL complex BSD leading-term problem.

Curve E/Q: y²+y=x³+x²−2x, conductor/minimal discriminant 389,
exact Mordell–Weil rank 2 with saturated basis
P=(-1,1), Q=(0,-1), P+Q=(4,8), no rational torsion,
Tamagawa factor 1 and two real connected components.

## 1. A safe global real chart and its exact Tate coefficient bounds

Translate x by +3: X=x+3. This produces the integral,
globally minimal Weierstrass model

  y²+y = X³−8X²+19X−12.

Its invariants are
  b2=-32, b4=38, b6=-47, b8=15, Delta=389.
Writing t=1/X, Tate's archimedean series has
  z(t)=1−38t²+94t³−15t⁴.

The real curve has x on [e3,e2] union [e1,+infty),
where e3<e2<e1 are the real roots of
  x³+x²−2x+1/4.
By exact rational signs:

  -41/20<e3<−2,
  13/100<e2<7/50,
  9/10<e1<91/100.

Thus every real point has t in the union

  (0,10/39) union (50/157,20/19).

The derivative satisfies
  z'(t)=−2t(38−141t+30t²).
The quadratic 38−141t+30t² is decreasing on
[0,20/19], positive at 10/39 and negative
at 50/157. Therefore z decreases on the
first real-coordinate interval and increases
on the second. Exact rational endpoint
evaluation proves:

  **1/50 < z(t) < 64 FOR EVERY REAL E POINT.**

The elementary inequality is a genuine GLOBAL
uniform bound, not based on the first 35 sampled points.

The shifted x-coordinate doubles by the exact map

  X(2R) =
    (X⁴−38X²+94X−15) /
    (4X³−32X²+76X−47).

Because the curve's only bad reduction prime is 389,
and the three integral input points P, Q, P+Q have
2y+1 equal to 3, −1, and 17 respectively,
all three reduce to nonsingular points at 389.
Cremona, *Algorithms for Modular Elliptic Curves*
chapter III §3.4, Proposition 3.4.1(a) states that
the finite local canonical height is ZERO at every
prime where an integral point has nonsingular reduction.
This includes 389. At all other primes E has good
reduction and the points are integral, hence all
finite local terms vanish in CREMONA'S NORMALIZATION.
Thus the exact GLOBAL twice-canonical height is
given by the Tate archimedean series alone:

  **H(R)=2*hat{h}(R)
         =log(X(R))
          +sum_{j>=0}4^(−j−1)*log(z(2^jR)).**

We use Cremona's twice-canonical height as the
diagonal of the BSD height pairing, so there
is no missing factor of 2.

By the global bound on z, after N terms:

  **|H(R) − H_N(R)| <= log(64)/(3*4^N).**

For N=35 this is strictly less than 1.175e−21.

Source: https://johncremona.github.io/book/fulltext/chapter3.pdf,
chapter III §3.4, pp. 72–75, especially eq. (3.4.2),
Proposition 3.4.1(a), and Tate's real-height series.

## 2. Exact interval arithmetic, without Sage or floating point

All numbers are represented as integer lower/upper
bounds on a fixed 10^100 grid. Addition, subtraction,
multiplication and reciprocal of positive intervals
have explicitly outward integer rounding.

For log(v)>0, reduce by a power of 2 to m in [1,3),
then use the atanh formula

  log(m)=2*sum_{j=0}^{N−1}u^(2j+1)/(2j+1)
         + R_N, u=(m−1)/(m+1),
  0 <= R_N <= 2*u^(2N+1)/[(2N+1)*(1-u²)].

N=95 is used with interval endpoints, so the
logarithm bounds are rigorous; log2 itself
is computed by the same series at u=1/3.
No binary floating point enters the proof.

The heights of the exact saturated basis P,Q
and their sum P+Q are enclosed by the algorithm:

  H(P) in (0.686667083305586585723140,
           0.686667083305586585725489);
  H(Q) in (0.327000773651604951842576,
           0.327000773651604951844925);
  H(P+Q) in (1.550624054570643537753191,
             1.550624054570643537755540).

Polarization gives
  <P,Q>=[H(P+Q)−H(P)−H(Q)]/2
and the genuine Mordell–Weil regulator
  Reg_E=H(P)H(Q)−<P,Q>².
The certified new interval is:

  **0.15246017794314375162 < Reg_E
                            < 0.15246017794314375163.**

The result agrees with, but does not use as an
input, the prior Sage/LMFDB numeric reference.

## 3. Real period + L'' Arb bound + canonical regulator

The previously produced independently rational
root/AGM period certificate yields

  4.9804251217101101506427155838846049203121163606791400801
    < Omega_E <
  4.9804251217101101506427155838846049203121163606791400802.

This Omega_E incorporates BOTH real connected
components and is in the same BSD normalization
as Reg_E and L''(E,1)/2.

The independent Sage 10.9 Arb *rigorous*
L''(E,1)/2 enclosure was executed by the user
on 2026-10-19 and archived in
  results/full_BSD_phase1_Arb_Lstar_interval_PASS_2026-10-19.md.
The new script conservatively widens it to
  0.7593165002884267 < L''(E,1)/2
                       < 0.7593165002884269.

Combining the three fully rigorous intervals gives:

  **0.99999999999999990
      < L''(E,1)/(2*Omega_E*Reg_E)
      < 1.00000000000000018.**

The width is 2.8e−16 in the outward-rounded
17-decimal display, around ELEVEN orders tighter
than the previous 3e−5 relative ratio interval.
This proves a real-number inequality, NOT an identity.

## 4. A sharp elementary rationality/denominator bridge

Let R_BSD denote the positive REAL number in §3.
From the certified interval we have

  **|R_BSD−1| < 1 / 5,000,000,000,000,000.**

Therefore the following arithmetic implication
is proved without assuming BSD:

  IF R_BSD=a/b in lowest terms, a,b positive integers,
     and b<=5,000,000,000,000,000,
  THEN a=b and R_BSD=1 EXACTLY.

Proof: if a!=b then |a/b−1|>=1/b>=1/B,
contradicting the certified bound. QED.

**CRITICAL:** Neither the RATIONALITY of the rank-two
leading-term quotient nor a bound on its denominator
is established by the current general rank-two
theory. This is a noncircular, very sharp sufficient
extra condition, NOT a proof of the missing complex
leading-term identity.

If strong BSD itself holds, then R_BSD=#Sha is
an integer, so automatically #Sha=1. That
conditional integer observation already followed
from the earlier weaker interval; the new 18-digit
result strengthens its numerical certificate but
does NOT prove the BSD identity.

In particular, one may NOT infer that R_BSD has
denominator 1 from the known integral modular
parametrization, the rationality of L(E,1)/Omega
in analytic rank zero, or the rank-two MW lattice.
Such a statement would amount to a new rank-two
rationality theorem and requires proof.

## 5. Reproducibility and scope

Actual assistant-executed, pure Python stdlib files:

- verification/bsd389_fast_tate_series_regulator_certificate_20261121.py
- verification/bsd389_tate_18decimal_BSD_ratio_interval_20261121.py

Both have been executed locally and the exact source
bytes compared by Git blob SHA-1 to the repository
versions. The scripts rely on the independently
authenticated previous Arb Lstar and AGM period
endpoints, rather than repeating those expensive
calculations.

Remaining full BSD obligations:
(A) independent GLOBAL uniform prime support and
    finite exponent control of Sha(E/Q);
(B) a GENUINE exact complex leading-term theorem
    yielding R_BSD=1 without presupposing it.

The 18-digit numeric certificate provides neither
(A) nor (B), but substantially constrains any
future exact rank-two algebraicity/denominator
comparison and removes computational uncertainty
about the global regulator from our proof search.
