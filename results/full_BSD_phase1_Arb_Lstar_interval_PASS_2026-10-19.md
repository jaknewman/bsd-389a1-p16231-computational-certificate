# Full BSD 389a1 — rigorous analytic coefficient via Arb: PASS

**Date:** 2026-10-19. **Environment:** SageMath 10.9, Miniforge Sage, IONOS Ubuntu. **Evidence:** full terminal log furnished by the researcher, exit code 0.

## Terminal certificate

```text
BSD389_PHASE1_ARITHMETIC_AND_Q_EXPANSION_PASS 160
BSD389_ARB_RIGOROUS_SEGMENT 0 1 [-0.0451413809238283187 +/- 3.54e-20]
BSD389_ARB_RIGOROUS_SEGMENT 1 2 [0.333221776826244379702 +/- 3.36e-22]
BSD389_ARB_RIGOROUS_SEGMENT 2 4 [0.4712356450642956 +/- 4.34e-17]
BSD389_ARB_RIGOROUS_SEGMENT 4 7 [4.593217151e-7 +/- 3.20e-17]
BSD389_ARB_RIGOROUS_FOURIER_TAIL_UPPER [2.959789335187813409037290982347741100952315655336e-25 +/- 3.97e-74]
BSD389_ARB_RIGOROUS_INTEGRAL_TAIL_UPPER [4.580076494517071307852765672875705702993550033425e-146 +/- 4.62e-196]
BSD389_ARB_RIGOROUS_ANALYTIC_LSTAR_ENCLOSURE [0.7593165002884268 +/- 7.81e-17]
BSD389_ARB_RIGOROUS_ANALYTIC_LSTAR_RADIUS 4.8312490e-17
BSD389_PHASE1_ANALYTIC_ENCLOSURE_PASS
BOUNDARY: L(E,1)=0 must be separately exact-certified (not inferred from numeric Lstar)
BOUNDARY: period/regulator are NOT enclosed here; no equality of transcendental factors proved
BOUNDARY: global Sha finiteness and #Sha=1 remain unproved
EXIT_STATUS=0
```

## Mathematical statement

Under the separately established analytic central vanishing `L(E,1)=0` and even root number `w(E)=+1`, the functional equation gives `L'(E,1)=0`. For `c=2*pi/sqrt(389)` and `f(iy/sqrt(389))=sum_{n>=1} a_n exp(-c*n*y)`, the Mellin transform shows

```text
L''(E,1)/2 = c * integral_1^infinity f(iy/sqrt(389))*log(y)^2 dy
           = c * integral_0^infinity exp(t)*t^2*
                (sum_{n>=1} a_n exp(-c*n*exp(t))) dt .
```

Exact `a_n` up to `n=160` come from `E.anlist(160)[1:]`. Arb complex ball integration rigorously encloses the integrals on `[0,1],[1,2],[2,4],[4,7]`; explicit valid coefficient majorant `|a_n| <= 2n` bounds the remainder of the Fourier series and the positive tail `t>=7`. The outputs above enclose `L''(E,1)/2` at absolute error below `8e-17` (reported representation `+/- 7.81e-17`). The `full.rad()` report has a different display of radius due to Sage ball presentation; archive the actual ball object rather than replacing it with an arbitrarily narrower decimal interval.

## Comparison and limits

Independent numerical PARI/Mellin phase-0 values:
```text
Lstar ≈ 0.75931650028842677023019260789472202
Omega ≈ 4.9804251217101101506427155838846049
Reg   ≈ 0.15246017794314375162432475704945582
Omega * Reg ≈ 0.75931650028842677023019260789472202
```

The Arb interval **does not** turn their decimal equality into an exact identity. Sage's period and regulator were not computed as certified real balls by this script; `Sha(E/Q)=0` and its finiteness are not proved by it.

### Sources

- [Arb-certified integration Sage source](../sage/full_BSD_phase1_Arb_Lstar_interval.py)
- [PARI / Mellin baseline PASS](full_BSD_phase0_PARI_MELLIN_PASS_2026-10-19.md)
- [Full BSD research programme](../paper/full_BSD_389a1_research_program_2026-10-19.md)

**Next research gate:** recover/check exact modular-symbol certificate for `L(E,1)=0`; rigorously enclose `Omega` and `Reg`; treat global `Sha` finiteness and exact leading-term comparison as independent, harder obligations.
