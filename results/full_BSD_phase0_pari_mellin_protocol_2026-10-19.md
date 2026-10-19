# Global BSD phase 0 — SageMath 10.9 correction and independent Mellin check (2026-10-19)

**Status:** prepared, locally syntax-checked; full corrected script **not yet run on IONOS**.

Original IONOS run produced:
```
BSD389_GLOBAL_PHASE0_ARITHMETIC_GATES_PASS
BSD389_GLOBAL_REAL_PERIOD_BSD 4.9804251217101101506427155838846049
BSD389_GLOBAL_REAL_REGULATOR 0.15246017794314375162432475704945582
BSD389_GLOBAL_PREDICTED_LSTAR_SHA1 0.75931650028842677023019260789472202
ValueError: algorithm must be "pari" or "magma"
EXIT_STATUS=1
```

This is a Sage 10.9 interface incompatibility with the old `algorithm='gp'`, **not** a BSD contradiction. Official PARI L-functions docs support `E.lseries().dokchitser(prec=140,algorithm='pari').derivative(1,2)` for this exact rank-2 curve.

The corrected working script `bsd389_bsd_globale_phase0_v2.py` SHA-256:
`3155e2c2e3f3ad06c028b38af6e645847f55999c3b6292a6c2ed20edfd432910`.

It additionally verifies the analytic leading coefficient by the independent *Mellin transform* formula. Put `c=2*pi/sqrt(389)`, `f(i*y/sqrt(N))=sum a_n exp(-c*n*y)`. For even root sign +1 and analytic order at least two:

```
L''(E,1)/2 = c * integral_0^infinity exp(t)*t^2
              * sum_{n>=1} a_n exp(-c*n*exp(t)) dt.
```

The integral is approximated with `mpmath`, Fourier coefficients `a_1,...,a_260` from Sage's exact `E.anlist(261)`, and cutoff `t<=7`. Numerical trial **independently checked outside Sage** by calculating the first 260 `a_n` from prime-field point-counts, prime power recurrences, and multiplicativity yielded:

```
Lstar_Mellin = 0.7593165002884267702301926078947220190781
```

Analytic tail upper bounds, using `|a_n|<=d(n)*sqrt(n)<=2*n`:

```
Fourier truncation at n=260: < 1.646e-39
Integral t>7:               < 4.581e-146
```

The **quadrature error itself was not bounded by interval arithmetic**, so neither this nor PARI numerical agreement proves BSD.

Pending: execute corrected script on IONOS and archive original PASS log. `Sha(E/Q)=0` and exact complex BSD leading-term identity both remain open as proved statements.
