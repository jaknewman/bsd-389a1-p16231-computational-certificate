# E389a1 — two new prime-primary Sha vanishing certificates from complete rank-two Kurihara sums (p=17,23)

Date: 2026-11-21.

**Status:** new exhaustive pure-Python Kurihara arithmetic at p=17 and p=23,
with frozen source Manin symbols and genuine finite-group arithmetic.
The deductions to p-primary Sha triviality use the published hypotheses and
theorems of Chan-Ho Kim, not a direct Selmer computation by this script.
A fresh independent Sage/eclib run at p=17 and p=23 has **not** been made.

## 1. Curve and integrality prerequisites

E=389a1, y^2+y=x^3+x^2-2x, conductor 389, c389=1,
MW rank exactly 2, torsion 0. Both p=17 and p=23 are good ordinary,
with a17=-6, #E(F17)=24 and a23=-4, #E(F23)=28.
Therefore E(Q_p)[p]=0. The source project has a separately certified
all-prime surjectivity gate for rho_E,p. The optimal semistable curve has
Manin constant c_E=1. These are the precise prerequisites, together with
p-integrality of the Neron-normalized plus modular symbols, for invoking
Kim's results.

Primary published reference:
C.-H. Kim, *The structure of Selmer groups and the Iwasawa main
conjecture for elliptic curves*, Theorems 1.8 and 1.10;
https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf

## 2. EXACT arithmetic at p=17

Auxiliary primes: q1=1667, q2=5237. Exact Legendre point counts:
  a1667=19, #E(F1667)=1649=17*97;
  a5237=87, #E(F5237)=5151=17*303.
Both are 1 mod 17, both traces are 2 mod 17, with
17 exactly dividing each group order.

The local MW matrix with basis P=(-1,1), Q=(0,-1),
up to row-wise choice of local generators, is
  [[1,6],[1,12]], determinant 6 mod17 (a unit).

The full modulus n=q1*q2=8,730,079 has
  phi(n)=8,723,176 unit residues.
The plus-symbol parity and q_i=1 mod 34 permit exactly
half the classes to be evaluated: 4,361,588 representatives.
The auxiliary primitive roots in the run are 2 and 3.
The exact full moments M00,M10,M01,M11 are
  [0,0,0,4] mod17.
Thus the genuine degree-two Kurihara number in the
frozen Neron-integral Manin convention is:
  delta_1667*5237 = 4 mod17 != 0.

## 3. EXACT arithmetic at p=23

Auxiliary primes: q1=1289, q2=3727. Point counts:
  a1289=25, #E(F1289)=1265=23*55;
  a3727=94, #E(F3727)=3634=23*158.
Both q are 1 mod23; both a_q are 2 mod23;
23 exactly divides each group order.

Local MW matrix:
  [[1,5],[1,12]], determinant 7 mod23 (a unit).

Full modulus n=q1*q2=4,804,103; phi(n)=4,799,088.
The original direct run evaluated ALL 4,799,088 units and
obtained the full moments
  [0,0,0,17] mod23,
with independent half-sum 20 and 2*20=17 mod23.

The committed reproducible script also evaluated 2,399,544
half-symmetry representatives and recovered the same full moments
  [0,0,0,17] mod23.
Auxiliary primitive roots are 6 and 3.
Hence
  delta_1289*3727 = 17 mod23 != 0.

## 4. Mathematical implication using Kim

Under Kim's p-integral/surjective/Tamagawa/Manin hypotheses,
a nonzero two-factor Kurihara number at minimal auxiliary
cardinality 2, together with the already proven rank MW(E)=2,
implies that the p-power Selmer group has no additional finite
part beyond the two-dimensional MW part. The minimality follows:
rank MW=2 implies Kurihara degree >=2; the exhibited unit
two-factor number implies degree <=2.

Therefore for p=17 and p=23:

  Sha(E/Q)[p^infty] = 0,

and, from the previously proved rank-one strict Selmer identity
at primes for which the MW localization is primitive,

  Fitt_1(X_p^str) = Z_p.

The separate exact rational local formal-group test is now also
completed for BOTH new p:
  p=17: #E(F17)=24, t([24]P)/17 = 2 mod17,
        t([24]P)/17=19 mod17^2,
        t([24]Q)/17=206 mod17^2,
        log_17(Q)/log_17(P)=239 mod17^2.
  p=23: #E(F23)=28, t([28]P)/23 = 7 mod23,
        t([28]P)/23=398 mod23^2,
        t([28]Q)/23=209 mod23^2,
        log_23(Q)/log_23(P)=273 mod23^2.
Thus P is a p-adic local primitive MW generator for BOTH p,
at every p^n; the strict Selmer exact theorem applies. As
Sha[p^infty]=0 by the Kurihara/Kim witness, this proves:
   Fitt_{1,Z_17}(X_17^str)=Z_17;
   Fitt_{1,Z_23}(X_23^str)=Z_23.
Verification: updated
  verification/bsd389_local_strict_line_p2_rational_20261121.py
which computes formal parameters by exact rational group law and
reduces modulo p^3. This is wholly independent of the modular-symbol
Kurihara calculation.

## 5. Computational provenance and limits

Run from the repository root with plain Python:

  python3 verification/bsd389_p17_p23_kurihara_complete_symmetry_20261121.py --p 17
  python3 verification/bsd389_p17_p23_kurihara_complete_symmetry_20261121.py --p 23

This script imports the frozen 390-entry Manin vector and
continued-fraction evaluator from
  verification/bsd389_p11_three_kurihara_independent_standard_python_20261121.py.
It pins the exact 390-entry vector via SHA256
  31ae823767e5a84a430efd68b49bb17298fa69ad9d91d8fdac34b061602387ee
where the bytes are values digit0..digit9 (not ASCII code points).

The vector originates from archived Sage/eclib modular-symbol
work and is independently benchmarked at p=5,7,11. The p=11
pair q=(397,991) was already authentically executed by the user
on Ubuntu in November; its delta=1 matches independent Python.

This script is an independent **full enumeration from frozen
source modular symbols**, not an independent re-derivation of
the Manin vector from q-expansions. A separate Sage/eclib run
at the new p17/p23 pairs is the remaining desirable provenance
cross-check, not an assumption in the mathematical use of
the correctly normalized frozen Manin vector.

No all-prime Kurihara nonvanishing theorem has been established.
The analogous p-independent annihilator of Sha, the remaining
exceptional p-primary components and the exact complex BSD
leading-term equality remain independent proof obligations.
