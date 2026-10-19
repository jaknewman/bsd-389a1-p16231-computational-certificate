# BSD 389a1 — all-prime local ramification and a determinantal uniform Selmer criterion
Date: 2026-10-19. Author: Jerry Armando Kasa.

**STATUS:** Two uniform Galois properties and a conditional integer-linear-algebra theorem are rigorous. No uniform bound on the prime support of Sha has been proved.

## A. Uniform ramification at the single bad prime

For E: y^2+y=x^3+x^2-2x, the minimal discriminant is +389 and the conductor is 389. The only bad prime q=389 has multiplicative reduction with v_389(Delta_min)=1. For every prime l !=389, the l-torsion Galois representation is **ramified at 389**.

**Proof:** Over an unramified quadratic extension of Q_389 if necessary, E is a Tate curve with parameter q_E of valuation 1. For l !=389, the local l-torsion sequence 0 -> mu_l -> E[l] -> Z/l ->0 has nontrivial tame inertia unipotent part whenever l does not divide v_389(q_E). Since v_389(q_E)=1, the extension class has nonzero inertia for *every* such l. An unramified quadratic twist does not affect inertia. QED.

The earlier user-executed SageMath 10.9 computation returned rho.non_surjective(A=1000)==[]. Per Sage's proof contract this establishes im(rho_bar_l)=GL_2(F_l) **for all primes l**, not only l<=1000. These two all-prime results remove the residual-image and auxiliary-local-ramification hypotheses for every **good ordinary prime p>=5** (the bad prime 389 and supersingular primes require different hypotheses). Sage's `p_primary_order` implementation tests `v_q(q_E) % p != 0` for at least one conductor prime q||N, precisely the valuation-one condition.

**Do not conclude from these two properties that Sha(E/Q)[p]=0 for any new p.** The p-adic leading coefficient and comparison with the regulator remain p-dependent and essential.

Primary sources:
- Sage Sha.p_primary_order: https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py
- Tate curve inertia criterion: Serre (1972) and https://mathoverflow.net/questions/707/reference-for-the-standard-tate-curve-argument
- Previous all-prime image certificate: ../results/all_prime_galois_surjectivity_uniform_H1_vanishing_PASS_2026-10-19.md

## B. Precise determinantal criterion for a uniform exceptional integer

Let S_0 be any fixed finite set of primes. Suppose we produce **one actual integral matrix** A in M_{m x n}(Z), m >= n, rank_Q(A)=n, and, for every prime l outside S_0, an *arithmetically constructed, certified injective map*

    Sha(E/Q)[l] -> ker(A mod l : F_l^n -> F_l^m).

Let d(A) be the positive gcd of all n-by-n minors of A (nonzero since rank_Q(A)=n). Then:

    l not in S_0 and l does not divide d(A)  ==>  Sha(E/Q)[l]=0.

**Proof:** If l does not divide the gcd of maximal minors, some n-by-n minor has nonzero determinant modulo l, so A mod l has full column rank, hence its kernel is zero. Injectivity forces Sha[l]=0. Any nontrivial l-primary Sha contains l-torsion, so Sha[l^infinity]=0. QED.

Therefore the **explicit uniform integer**

    C_E = d(A) * product(l for l in S_0)

would contain every possible prime divisor of Sha, *provided the stated integral model and injections are actually proved*.

### The hard missing object

We do **not** possess the crucial uniform Selmer-to-matrix injection. Constructing an arbitrary matrix from modular symbols, Mordell–Weil heights or congruence numbers and taking minors does **not** satisfy the hypothesis. In particular, the already computed 390 Manin-symbol relations, 67 tame generators or 2x2 Neron–Tate regulator are **not** known to produce such an injection and must not be promoted into a Sha annihilator.

A realistic research route is a derived rank-two Euler/Kolyvagin-system or Selmer-complex integral comparison furnishing one finite, p-independent arithmetic complex or matrix, together with its exact local conditions and a proof of the injection. Such a construction would be new substantive mathematics, not a computational routine.

## C. What our existing data do and do not close

**Closed:** analytic rank precisely 2, algebraic rank 2, exact 2-Selmer and 3-Selmer minimality, proved 5/7/11/13-primary bounds, all-prime surjective residual image, all-prime ramification at bad conductor prime 389, rank-one twist D=-19 and its Sha finiteness by Gross–Zagier–Kolyvagin; significant conditional 16231 computational certificate.

**Open:** actual p-independent A/injection; any uniform support bound C_E for Sha, global Sha finiteness and exact complex BSD leading term. The new rank-one quadratic twist does not itself supply this missing uniform comparison; finite many imaginary fields cannot cover every split prime by Dirichlet.

**Action:** seek a theorem constructing this **integral rank-two comparison**, or identify a valid alternative non-matrix uniform bound. For a future candidate, demand (i) exact integer matrix, (ii) full-rank-over-Q certificate, (iii) a written injection proof for all primes outside explicit S_0, (iv) nonzero maximal-minor gcd computation, (v) separate checks of the finitely many primes dividing C_E. No numerical coincidence substitutes for (iii).


## D. Why ordinary Iwasawa theory cannot by itself make the exceptional set finite

Elkies proved that every elliptic curve over Q has **infinitely many supersingular good primes**. Thus the assertion that ordinary-prime criteria apply outside a finite set is false, even after proving full residual image and all-prime inertia at 389. A globally uniform argument must incorporate supersingular primes, e.g. with a suitable signed theory, or avoid ordinary/supersingular distinctions by working integrally.

Reference: Noam D. Elkies, *The existence of infinitely many supersingular primes for every elliptic curve over Q*, Invent. Math. 89 (1987), 561–568, listed on https://people.math.harvard.edu/~elkies/math_pubs.html .

## E. Exact invariants check and correction

For `[a1,a2,a3,a4,a6]=[0,1,1,-2,0]`:

```text
b2 = 4, b4 = -4, b6 = 1, b8 = -3
Delta_min = -b2^2*b8 - 8*b4^3 - 27*b6^2 + 9*b2*b4*b6 = +389.
v_389(Delta_min)=1
```

**The sign is +389** (not -389 as incorrectly written in some preliminary notes). There are two real connected components, consistent with the positive discriminant. Since the ramification argument depends on the valuation 1, not on the sign, it is unaffected.
