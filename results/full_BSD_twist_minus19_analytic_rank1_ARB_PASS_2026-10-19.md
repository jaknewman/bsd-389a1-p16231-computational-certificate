# BSD 389a1: quadratic twist D=-19 has analytic rank exactly one — certified Arb PASS

**Run:** 2026-10-19, SageMath 10.9, active Miniforge environment, IONOS Ubuntu. Evidence: user's complete terminal output, `EXIT_STATUS=0`. **Research scope:** auxiliary quadratic twist only; NOT global BSD for 389a1.

## Curve and field

```text
E: y^2+y=x^3+x^2-2x       N_E=389
D_K=-19 (fundamental)      K=Q(sqrt(-19))
E^D conductor=140429       twist root number=-1
Kronecker(-19,389)=+1      Kronecker(-19,16231)=+1
52^2 ≡ -19 (mod 389)       7139^2 ≡ -19 (mod 16231)
```

## Arb terminal output (verbatim)

```text
BSD389_DMINUS19_HEEGNER_SPLITTING_PASS D=-19 N_twist=140429 w=-1
BSD389_DMINUS19_ARB_FINITE_SUM [9.07564283881115519487219595503701229878 +/- 7.37e-39]
BSD389_DMINUS19_FOURIER_TAIL_UPPER [0.0051420656137407479785235463701949262043374018 +/- 1.18e-47]
BSD389_DMINUS19_RIGOROUS_LPRIME_ENCLOSURE [9.1 +/- 0.0295]
BSD389_DMINUS19_TWIST_ANALYTIC_RANK_ONE_PASS
BOUNDARY: Does not prove Sha(389a1/Q) is finite or full complex BSD.
BOUNDARY: New 2026 derived-Heegner theorem is only p-primary and has additional hypotheses.
EXIT_STATUS=0
```

## Mathematical justification

For `w(E^D)=-1`, the functional equation forces `L(E^D,1)=0`. The Mellin transform gives

```text
L'(E^D,1) = 2 sum_{n≥1} a_n(E)*chi_{-19}(n)*E1(2*pi*n/sqrt(140429))/n.
```

The script uses `E.anlist(512)[1:]` exactly and Arb's enclosing `ComplexBallField.exp_integral_e(1)`. The global coefficient bound `|a_n(E)| ≤ d(n) sqrt(n) ≤2n` and `E1(x) ≤ exp(-x)/x` give the explicit remainder

```text
R_512 ≤ 4*exp(-c*513)/(c*513*(1-exp(-c)))
     ≤ 0.00514206561374075..., c=2*pi/sqrt(140429).
```

The Arb sum with signed tail enclosure is strictly positive. Hence `L'(E^D,1) ≠0`, giving **analytic rank one** of the twist. Together with the previously certified `ord L(E,s)=2`, Artin formalism yields **analytic rank three** over `K`.

This satisfies a necessary analytic-rank condition for considering derived-Heegner/Kolyvagin methods at suitable primes. It does **not** itself certify nontriviality of a derived Kolyvagin class, satisfy every hypothesis of a particular theorem, or give uniform control of Sha across all primes.

## Next mathematical obligations

1. Check any selected derived-Heegner theorem's **full** local and residual-representation hypotheses, precise statement and exact derivative-class nonvanishing requirement; do not infer these from twist analytic rank alone.
2. A result about a **fixed** prime `p` does not establish global finiteness of `Sha(E/Q)` without a uniform finite-support theorem.
3. Full complex BSD additionally needs an exact leading-term identity, not the numerical agreement at 35 decimal digits.

See [global obstruction and K=-19 road map](../paper/global_BSD_obstruction_and_Heegner_D_minus19_2026-10-19.md). Source on IONOS: `bsd389_twist_minus19_Arb_rank1.py` (prior SHA-pinned).
