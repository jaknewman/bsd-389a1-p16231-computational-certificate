# Genuine one-cusp Sage/eclib user-run certificate PASS (2026-11-01)

**Provenance:** all lines below are copied from the user's newly supplied Ubuntu/Sage terminal output. The script [`verification/bsd389_single_cusp_global_unit.py`](../verification/bsd389_single_cusp_global_unit.py) executes four rational-cusp calls through **each** of Sage's and eclib's independent modular-symbol implementations; it does not read the previously generated 389-entry JSON. This is real **user-reported execution**, not a remote CI result.

## Actual command

```bash
python -u verification/bsd389_single_cusp_global_unit.py \
    2>&1 | tee ~/bsd389_single_cusp_global_unit.log
```

## Verbatim stdout

```text
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 382 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 384 value -2
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 7 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle sage a 5 value -2
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 382 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 384 value -2
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 7 value -1
ONE_CUSP_DIRECT_VALUE_PASS oracle eclib a 5 value -2
ONE_CUSP_BOTH_SAGE_ECLIB_8_DIRECT_VALUES_PASS checks 8
ONE_CUSP_EXACT_BEZOUT_PASS (-1)-(-2)=1
ONE_CUSP_P_UNIFORM_CLASSICAL_SYMBOL_UNIT_PASS m_plus(7/389)=-1 all_rational_primes
BOUNDARY_NO_TWO_PRIME_KURIHARA_OR_SHA_FITTING_IMPLICATION
```

## Exactly supported conclusion

For the curve E=389a1 and Néron/`L_ratio`-normalized plus modular symbol, both implementations independently verify
[
m_E^+(7/389)=m_E^+(382/389)=-1,quad
m_E^+(5/389)=m_E^+(384/389)=-2.
]
The first value alone is a unit in (mathbf Z_p) **for every prime p**, without a prime scan. Combined with the independently audited 389-entry canonical JSON, this is the **third convergent numeric source validation** for the fixed arithmetic modular symbol.

**Boundary:** Nonzero fixed classical modular-symbol value (-1) is not the specific 2-auxiliary-prime Kurihara weighted sum; it does not establish (m_2(p)=0), any actual Selmer (operatorname{Fitt}_2) unit, (Sha[p^infty]=0), global finiteness of Sha or strong BSD.

An [exact mixed finite-difference lemma for two-prime Kurihara weights](../paper/bsd389_kurihara_two_auxiliary_mixed_difference_lemma_2026-11-01.md) explains why the weights annihilate every additively separable function, so this unit source fact alone cannot force a weighted mixed nonvanishing.
