# Three newly computed rank-two Kurihara witnesses for 389a1: p = 11, 13, 17

**Date:** 2026-11-26. **Scope:** finite, executable modular-symbol certificates and prime-by-prime Selmer consequences. **Not a proof of full BSD.** Calculations were run in the assistant's working container, and should be independently repeated and reviewed before being presented as externally certified.

## The curve and the verified arithmetic inputs

\[
E/\mathbb Q: y^2+y=x^3+x^2-2x,\quad
N=\Delta_{\min}=389,\quad E(\mathbb Q)\simeq\mathbb Z^2.
\]

The group has a saturated basis \(P=(-1,1),Q=(0,-1)\), with trivial torsion, and the only Tamagawa factor is \(c_{389}=1\). Its optimal Manin constant is 1. LMFDB: https://www.lmfdb.org/EllipticCurve/Q/389a1/ . The initial normalized modular symbols \(m^+(7/389)=-1\) and \(m^+(5/389)=-2\) have been independently verified by both Sage and eclib in the project repository, results/bsd389_single_cusp_global_unit_USER_RUN_PASS_2026-11-01.md.

## Reproducible finite witness computations

| p | q1 | q2 | a_q1 | a_q2 | #E(F_q1) | #E(F_q2) | delta_(q1 q2) mod p | independent MW local determinant mod p |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 11 | 397 | 991 | 24 | -53 | 374 | 1045 | **1** | **8** |
| 13 | 131 | 911 | 2 | -24 | 130 | 936 | **6** | **6** |
| 17 | 1667 | 5237 | 19 | 87 | 1649 | 5151 | **4** | **6** |

For all three rows, both auxiliary primes are congruent to 1 mod p and both Frobenius traces are congruent to 2 mod p. Their local group orders have exactly one factor of p, so each E(F_q)/p is one-dimensional. The direct point count at the primary p is 16, 17 and 24 respectively, each prime to p; therefore E(Q_p)[p]=0 (the odd-p formal-group kernel over unramified Q_p has no p-torsion).

The Python program `bsd389_p11_p13_p17_kurihara_independent.py` reconstructs the 390-dimensional Manin-edge model over F_p with exact S/R identities, plus sign and T2 = -2. For each p in {7,11,13,17}, it checks a matrix rank of 389 and directly checks that the reconstructed Neron symbols have m(7/389)=-1 and m(5/389)=-2 modulo p. It also tests all imposed relations and the independent Hecke operators T3, T5, T7 on further cusps.

The authentic Kurihara sum is evaluated as

\[
\widetilde\delta_n=\sum_{a\in(\mathbb Z/n\mathbb Z)^\times}m^+(a/n)\prod_{q\mid n}\log_{g_q}(a\bmod q)\pmod p,
\]

with primitive roots g_q computed explicitly. This is the formula of Kim §1.4, no p-adic BSD approximation. Full and half-symmetry scans agree for p11 (393426 full residues) and p13 (119340 full residues), and the known p7 witness delta_(113*673)=2 is independently reconstructed as a normalization regression.

For p17, the Python half scan includes 4,365,039 residues and gives 4 mod17. A separate compiled native C++ implementation, using the exact same independently reconstructed and pinned 390-entry Manin table, enumerated **all 8,730,078 residues** without the half-symmetry reduction and independently obtained **4 mod17**. Source `bsd389_kurihara_native_full.cpp` and input `bsd389_p17_manin_mod17.txt` are included.

The independent group-law calculation reduces P,Q mod each auxiliary prime, projects into the order-p subgroup, and obtains the local rows:

| p | row q1 | row q2 | det |
|--:|:--|:--|--:|
| 11 | (1,10) | (1,7) | 8 |
| 13 | (1,2) | (1,8) | 6 |
| 17 | (1,6) | (1,12) | 6 |

These local determinants are **cross-checks**, not replacements for the global Kurihara numbers.

## Rigorous local/Galois hypotheses for Kim's theorem

- **Residual surjectivity at p=11,13,17.** At good Frobenius primes q=2,3,5 respectively, the characteristic polynomials have discriminant -4, -8, -11, whose residues mod p are 7, 5, 6 respectively, all nonsquares. Thus the residual representation is irreducible. The multiplicative I_1 reduction at 389 and v_389(Delta)=1 gives a nontrivial order-p transvection in the image of inertia for these p. By Dickson's classification (p >= 5), an irreducible subgroup containing such a transvection contains SL2(F_p). The cyclotomic determinant is surjective, so the image is GL2(F_p). LMFDB also reports full mod-p image for every prime.
- **Manin:** optimal E, constant 1 (hence prime to p).
- **Local p-torsion:** #E(F_p) equals 16,17,24 respectively and p does not divide this number.
- **Tamagawa:** product 1.
- **Minimal order:** Kim Theorem 1.8 yields \(\mathrm{ord}(\widetilde\delta)=\mathrm{corank}_{\mathbb Z_p}\mathrm{Sel}_{p^\infty}\ge 2\) since rank MW is two. The nonzero two-prime witness gives \(\mathrm{ord}(\widetilde\delta)\le2\), so equality holds.

## Prime-by-prime mathematical consequence

By C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.10, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf , for each p in {11,13,17} we get a canonical isomorphism

\[
\mathrm{Sel}(\mathbb Q,E[p])\xrightarrow{\sim}E(\mathbb F_{q_1})/p\oplus E(\mathbb F_{q_2})/p\simeq\mathbb F_p^2.
\]

But the saturated Mordell-Weil rank-two group gives \(E(\mathbb Q)/p\simeq\mathbb F_p^2\). The Kummer sequence

\[
0\to E(\mathbb Q)/p\to\mathrm{Sel}(\mathbb Q,E[p])\to\Sha(E/\mathbb Q)[p]\to0
\]

thus forces \(\Sha(E/\mathbb Q)[p]=0\), and therefore \(\Sha(E/\mathbb Q)[p^\infty]=0\), for **p = 11, 13, 17**.

The argument does not presume BSD or prior Sha finiteness. This is an original independently reproducible finite-certificate application of a published theorem; a separate Sage/eclib direct verification of the three newly reported mod-p Kurihara coefficients is advisable before public proof certification.

## How to repeat

```bash
python3 bsd389_p11_p13_p17_kurihara_independent.py
# For the p=17 full 8,730,078-residue audit independently in C++:
g++ -std=c++17 -O3 bsd389_kurihara_native_full.cpp -o bsd389_kurihara_native_full
./bsd389_kurihara_native_full bsd389_p17_manin_mod17.txt 17 1667 5237 2 3 1
```

The run stdout saved in `bsd389_new_three_primes_run.log` is a container execution transcript, not a user's Ubuntu execution.

## Boundary: BSD remains unproved globally

These prove or certify **only three additional p-primary parts** of Sha. There is still no uniform bound covering all primes, including 2,3,389, and there is no proof of the exact archimedean BSD leading-term identity \(L''(E,1)/2=\Omega_E\mathrm{Reg}(E)\). The fact that LMFDB lists analytic Sha 1 is a numerical BSD prediction, not a general proof of global Sha finiteness.