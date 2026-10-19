# Global BSD phase 0 — first PARI PASS and one-line Mellin repair (2026-10-19)

IONOS SageMath 10.9 terminal confirms:
```text
BSD389_GLOBAL_PHASE0_ARITHMETIC_GATES_PASS
BSD389_GLOBAL_REAL_PERIOD_BSD 4.9804251217101101506427155838846049
BSD389_GLOBAL_REAL_REGULATOR 0.15246017794314375162432475704945582
BSD389_GLOBAL_PREDICTED_LSTAR_SHA1 0.75931650028842677023019260789472202
BSD389_GLOBAL_COMPLEX_LSTAR_PARI 0.75931650028842677023019260789472202
BSD389_GLOBAL_NUMERICAL_SHA_RATIO 1.0000000000000000000000000000000000
BSD389_GLOBAL_PARI_NUMERICAL_CONSISTENCY_PASS
```
The immediately following `assert len(coeffs) == M` failed in the **optional independent Mellin stage**, so full phase-0 final marker/exit-zero have NOT yet been obtained.

**Cause confirmed:** `E.anlist(n)` includes `a_0,...,a_n` (length `n+1`). The prior expression `E.anlist(M+1)[1:]` produced `M+1`, not `M`, coefficients. A single-line correction `E.anlist(M)[1:]` produces exactly `a_1,...,a_M` for `M=260`. Suggested command on host:

```bash
sed -i 's/E\.anlist(M + 1)\[1:\]/E.anlist(M)[1:]/' ~/bsd389_bsd_globale_phase0_v2.py
python -u ~/bsd389_bsd_globale_phase0_v2.py 2>&1 | tee ~/bsd389_bsd_globale_phase0_v2.log
echo "EXIT_STATUS=$?"
```

**Independent non-Sage corroboration** using exact small-prime point counts for `y²+y=x³+x²−2x`, prime-power recurrences and multiplicativity yields 260 coefficients with first 20 `[1,-2,-2,2,-3,4,-5,0,1,6,-4,-4,-3,10,6,-4,-6,-2,5,-6]`; 48-decimal-place mpmath Mellin quadrature reports

```
0.759316500288426770230192607894722019078101226
```

This Mellin quadrature is **not rigorously interval-enclosed**, so its 35-digit agreement with PARI and `Ω·Reg` does **not** prove full BSD. Pending corrected executable's terminal PASS.
