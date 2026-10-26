# Two gates for Castella–Hsieh: exact twist -3 L-value and the correct order-nine ring class character

Date: 2026-10-26. New exact rational argument for the **first** nonvanishing factor; correction of previously selected cubic character. The **second** Rankin central factor still requires the adelic/test-vector/Waldspurger identification of our Gross period.

## 1. Character order correction

For `K=Q(sqrt(-3))`, conductor `f=53`, ring class group `C18`, the earlier stage-14/15/23 quaternionic Gross-orbit outputs produce the degree-eight polynomial

`P(X)=-1-X+X²+2X³-X⁴-2X⁵-X⁶+2X⁷+X⁸`.

These are **distinct arithmetic conclusions**:

`P(X) mod Phi_3(X)=0`, so `P(zeta_3)=0`;

`P(X) mod Phi_9(X)= -3X^5-3X^4+3X^3-3X`, so `P(zeta_9)!=0`;

`Norm_{Q(zeta9)/Q}(P(zeta9))=Res(Phi_9,P)=729=3^6`.

The toric candidate for proving Rankin central nonvanishing is thus the **order-nine** character `chi_9([l_19])=zeta_9`, not the cubic chi_3 promoted by mistake in the immediately preceding conductor-53 note. For Castella–Hsieh, choose a ring class character psi of order 9 satisfying `psi^2=chi_9`, for example `psi=chi_9^5` (since 2*5=1 mod9). Then `chi_9=psi/psi^tau` because complex conjugation inverts class group characters.

Explicit regularity at p=16231 follows from F_53[omega]/(omega²+omega+1). Put `g=(5+3omega)^312=(21,28)` and `h=(51-94omega)^312=(25,46)` (coefficients mod53). Since `g^3=omega`, g has exact order nine, `h=g^4`, and `Norm(51-94omega)=16231`, we have `chi_9(bar(p_16231))=zeta_9^4 !=1` up to complex conjugation and the choice of generator. The p-regularity gate is satisfied in the **correct** order-nine branch.

**Boundary:** Nonzero formal oriented Gross-orbit sum `P(zeta9)` alone does not prove the Rankin central value is nonzero until its identification with the appropriate adelic toric period and nonzero local test-vector factors in Waldspurger's formula is justified. Earlier stages 22–29 gave 18 exact ideal transports, local 53 embeddings and Brandt vector comparisons; the remaining item is a publishable comparison to the standard optimal-embedding test vector and local Waldspurger normalization, rather than repeating these sums.

## 2. Positive twist L-value by pure rational arithmetic

For the curve `E:y²+y=x³+x²−2x`, conductor N=389, global sign +1, let `E^(-3)` be its quadratic twist by the primitive character of discriminant -3. The twisted conductor is `N'=389*3²=3501` and the functional equation has sign `w(E^(-3))=w(E)*chi_{-3}(-389)=+1`. Thus Mellin inversion and the weight-two functional equation give the **exact convergent central expansion**

`L(E^(-3),1)=2*sum_{n>=1} a_n(E)*chi_{-3}(n)*exp(-c*n)/n`,

where `c=2*pi/sqrt(3501)` and the a_n are the standard elliptic newform coefficients. They are obtained independently by finite-field point counts: `a_p=-sum_{x in F_p} Legendre(1+4(x³+x²-2x),p)` for odd good primes; at p=2 directly enumerate solutions; all composite a_n arise from multiplicativity and Hecke prime-power recurrence.

An elementary rational bound `223/71<pi<22/7` and `591/10<sqrt(3501)<592/10` implies `53/500<c<107/1000` (i.e., 0.106<c<0.107). For the first M=100 terms, bound each exponential using the rational Taylor polynomial `S_70(x)=sum_{k=0}^70 (-x)^k/k!` and Lagrange remainder `|e^{-x}-S_70(x)| <= x^71/71!`. Since `chi_{-3}(n)` and a_n are exact integers, all finite-interval endpoints are rational.

For all n, the Hasse bound and Hecke recurrences imply `|a_n| <= d(n)*sqrt(n) <= 2n`. Therefore the infinite remainder after 100 terms is at most

`4*sum_{n=101}^infinity e^{-c*n} <= 44*(10/11)^101 < 1/300`

using `e^{-c} <= (1+c)^(-1) < 10/11`. Exact rational arithmetic in our independent program returned total rigorous interval

`4.524769101826934 < L(E^(-3),1) < 4.574549787573269`

(the displayed decimals are only diagnostics for exact rational endpoints), and checked the more robust exact inequalities

`9/2 < L(E^(-3),1) < 23/5`.

**Hence `L(E^(-3),1)>0` is now established independently of the Rankin period and without a numerical Sage/Dokchitser call**, conditional only on standard elliptic modularity, the twist conductor and functional equation and the elementary Hasse/Hecke identities.

## 3. Remaining Rankin central factor

The product required by Castella–Hsieh Theorem A is now reduced to

`L(E/K,chi_9,1) != 0`.

The explicit order-nine Gross polynomial has cyclotomic norm `729`, proving its algebraic nonvanishing as an oriented Brandt-weighted orbit sum. **Conditional theorem:** if the established 18-adic ideal transport agrees with the canonical Gross/Waldspurger class action for the order-f conductor53 test vector and the local factors are nonzero, then Waldspurger identifies the nonzero period with the nonzero Rankin value, thereby completing `L(E^(-3),1)*L(E/K,chi_9,1)!=0`. A complete independent comparison of test-vector local factors is still required for an unconditional Rankin-L-value claim.

Even under that theorem, Kato-class nonvanishing at one prime does not yield integral primitivity of generalized Kato classes for all primes and so cannot prove uniform vanishing of all prime-primary Sha components.

### Relevant references

- [Earlier conductor53 cubic note — cubic period is zero; order-nine correction supersedes its candidate nonvanishing route](conductor53_cubic_character_p16231_regular_but_not_uniform_2026-10-26.md).
- [Rank-two Kato classes, Castella–Hsieh](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864).
- [Waldspurger and toric test-vector principles](https://kimballmartin.github.io/papers/mw-rev.pdf).

---

## Updated 2026-10-26: mathematical adelic toric-period bridge now derived

The previously outstanding Waldspurger comparison is now reduced to an abstract theorem about the **already executed** Stages 22, 23, 29, and 30, in [the detailed proof](389a1_chi53_waldspurger_gross_orbit_exact_identification_2026-10-26.md). Stage29's initial optimality at 53 propagates through the exact norm-19 class action of Stage22 because 19 is coprime to 53. All 18 orbit members are thus genuinely optimal embeddings of O_53; they exhaust the class group C18. Stage30 establishes that the Brandt class function belongs to the Jacquet–Langlands eigenline of E, and Stage23 fixes its index/mass normalization. Its character-weighted orbit sum equals a nonzero scalar multiple of the **genuine** automorphic toric period, not an arbitrary formal polynomial.

The global Waldspurger implication **nonzero toric period => nonzero Rankin central L** then follows **without explicitly evaluating any local Waldspurger factors**. Thus, under the archived finite Sage evidence and its source conventions, `L(E/K,chi9,1) != 0` becomes a **computer-assisted conditional theorem**, not a new arithmetic hypothesis. For complete third-party reproducibility, the original numerical Stage29 output and all underlying stage14/22 JSON input data should be copied into the public repository. Four original scripts (14/22/23/30) are now archived at `historical/quaternion53/`; an optional shorter optimality certificate was created but has not run.

This does NOT establish a uniform bound on all Sha primes, nor an unconditional independently reproduced Rankin value without trusted finite input.