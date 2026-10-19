# Full BSD phase 0 — PARI + Mellin numerical checks PASS

**2026-10-19**, user-supplied IONOS terminal output from activated SageMath 10.9 environment.

```text
BSD389_GLOBAL_PHASE0_ARITHMETIC_GATES_PASS
BSD389_GLOBAL_REAL_PERIOD_BSD 4.9804251217101101506427155838846049
BSD389_GLOBAL_REAL_REGULATOR 0.15246017794314375162432475704945582
BSD389_GLOBAL_PREDICTED_LSTAR_SHA1 0.75931650028842677023019260789472202
BSD389_GLOBAL_COMPLEX_LSTAR_PARI 0.75931650028842677023019260789472202
BSD389_GLOBAL_NUMERICAL_SHA_RATIO 1.0000000000000000000000000000000000
BSD389_GLOBAL_PARI_NUMERICAL_CONSISTENCY_PASS
BSD389_GLOBAL_COMPLEX_LSTAR_INDEPENDENT_MELLIN 0.759316500288426770230192607894722019078101
BSD389_GLOBAL_MELLIN_FOURIER_TAIL_BOUND 1.64553114372374e-39
BSD389_GLOBAL_MELLIN_INTEGRAL_TAIL_BOUND 4.580076494517071e-146
BSD389_GLOBAL_PARI_VS_INDEPENDENT_MELLIN_NUMERICAL_PASS
BOUNDARY: explicit Fourier and integration-tail bounds do not certify numerical quadrature error
BOUNDARY: numerical Lstar=Omega*Reg does NOT establish exact identity
BOUNDARY: Sha(E/Q) finiteness and global order remain to be proved
BSD389_GLOBAL_PHASE0_NUMERICAL_AUDIT_COMPLETE
EXIT_STATUS=0
```

**Status: PHASE0_NUMERICAL_PASS.** The coefficient is supported by independent PARI/Dokchitser and Mellin/q-expansion numerical evaluations. The Fourier and integration-tail bounds are explicit, but the *numerical quadrature* lacked interval-certified error. Agreement between the real period–regulator product and the complex L-function is not an exact BSD identity. Neither `Sha=0` nor its global finiteness is established.

**Next:** certified analytic coefficient enclosure via Arb `ComplexBallField.integral` with rigorous truncation bounds, followed independently by global Sha finiteness/order and an exact complex leading-term comparison.

Sage Arb source documentation: https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_arb.html
