# Independent 389-symbol canonical JSON audit — authentic user PASS (2026-11-01)

**Source:** exact stdout supplied by the user from `bsdadmin@ubuntu` with `sage` active. This is the independent **standard-library Python JSON audit**; it does not recompute modular symbols and does not prove anything about the actual `Sha` beyond the fixed symbol claims stated below.

Run:

```bash
python -u verification/bsd389_fixed_rational_manin_independent_audit.py \
  --input ~/bsd389_fixed_rational_manin_content.json \
  2>&1 | tee ~/bsd389_fixed_rational_manin_independent.log
```

Verbatim stdout:

```text
FIXED_M389_INDEPENDENT_CANONICAL_JSON_SHA256_PASS 9719d0863045ef63fe3519b23da0c4bb74303ee3d84cb9791f95e2a29d456dd4
FIXED_M389_INDEPENDENT_389_FRACTIONS_PASS 389
FIXED_M389_INDEPENDENT_NONZERO_COUNT_PASS 228
FIXED_M389_INDEPENDENT_DENOMINATOR_CONTENT_PASS D 1 g 1
FIXED_M389_INDEPENDENT_PLUS_EVENNESS_PASS comparisons 389
FIXED_M389_INDEPENDENT_BEZOUT_TERM a 382 symbol -1 coefficient 1
FIXED_M389_INDEPENDENT_BEZOUT_TERM a 384 symbol -2 coefficient -1
FIXED_M389_INDEPENDENT_BEZOUT_SUM_PASS 1
FIXED_M389_ALL_PRIMES_NONZERO_FIXED_SYMBOL_VECTOR_PASS
BOUNDARY_NO_TWO_PRIME_KURIHARA_OR_SHA_FITTING_IMPLICATION
```

## Stronger *one-cusp* consequence

The exact original canonical data yields `m_E^+(382/389)=-1` and `m_E^+(384/389)=-2`; the integer Bézout witness is the exact identity `(-1)-(-2)=1`.

But **the first value alone is an integer unit**. Since the independently checked sign-plus involution obeys `m_E^+(a/389)=m_E^+((389-a)/389)`, we further have `m_E^+(7/389)=-1` and `m_E^+(5/389)=-2`. Thus **one classical normalized plus-symbol** already guarantees `m_E^+(7/389) != 0 mod p` **for every rational prime p**, with no exception and no prime-by-prime computation.

This is a fixed classical modular-symbol unit statement; it is **not** a two-prime Kurihara number or an integral Kolyvagin/Euler special element. No implication for `Fitt_2(Sel_{p∞}^dual)`, `Sha[p∞]`, Sha finiteness or full BSD has been established.

The standalone two-cusp direct Sage/eclib reproduction script `verification/bsd389_single_cusp_global_unit.py` was added as a follow-up and is **not yet user executed**.
