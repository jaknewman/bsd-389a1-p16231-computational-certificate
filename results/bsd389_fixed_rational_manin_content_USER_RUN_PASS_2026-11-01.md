# Fixed rational plus modular symbols at 389 cusps — real Ubuntu Sage/eclib PASS

**Provenance:** verbatim output pasted by the user from their Sage-enabled Ubuntu host, after a successful fast-forward of `main` from `3a2d82c` to `ce03049`. Code: [`verification/bsd389_fixed_rational_manin_content.py`](../verification/bsd389_fixed_rational_manin_content.py). This records a real user execution, not a GitHub CI run. The JSON payload remains **on the user's Ubuntu host**; it has not been uploaded or independently parsed by the assistant.

## Run

```bash
python -u verification/bsd389_fixed_rational_manin_content.py \
  --output ~/bsd389_fixed_rational_manin_content.json \
  2>&1 | tee ~/bsd389_fixed_rational_manin.log
```

Exact user-provided stdout:

```text
FIXED_M389_PROGRESS 100 / 389
FIXED_M389_PROGRESS 200 / 389
FIXED_M389_PROGRESS 300 / 389
FIXED_M389_EXACT_ALL_SAGE_ECLIB_MATCH_PASS 389
FIXED_M389_NONZERO_SYMBOLS 228
FIXED_M389_RATIONAL_DENOMINATOR_LCM 1
FIXED_M389_INTEGRAL_SCALED_CONTENT 1
FIXED_M389_PRIMITIVE_VECTOR_CONTENT_PASS 1
FIXED_M389_EXACT_BEZOUT_WITNESS_PASS gcd 1 nonzero_coefficients 2
FIXED_M389_EXACT_CANONICAL_JSON_SHA256 9719d0863045ef63fe3519b23da0c4bb74303ee3d84cb9791f95e2a29d456dd4
FIXED_M389_REPORT /home/bsdadmin/bsd389_fixed_rational_manin_content.json
BOUNDARY_FIXED_MODULAR_SYMBOL_DATA_NOT_UNIFORM_SHA_FITTING_COMPARISON
```

## Exact implications and proof boundary

Let `v[a]=m_E^+(a/389)` for integers `a=0,...,388` in the same Néron period / `L_ratio` normalization. The computation successfully compared all 389 rational values from **Sage's own modular symbol implementation and eclib**, found 228 nonzero, and obtained:

[
D=operatorname{lcm}_{a}operatorname{den}(v_a)=1,qquad
g=gcd_a(Dv_a)=1.
]
The script also constructed a **verified exact integer Bézout identity**
[
sum_{a=0}^{388} c_a v_a=1,
]
with exactly **two nonzero** Bézout coefficients stored in the user-local JSON as `bezout_identity_sparse`. Their individual indices and values are **not yet present in this archive** and should not be invented. These computations show that the fixed rational vector is primitive over `Z`; for **every rational prime p** at least one of its 389 entries is nonzero modulo p. This is a *fixed modular-symbol* theorem (given the authenticity of the computed 389 values), with no finite exceptional set.

**Crucial negative inference:** A nonzero vector in `F_p^{389}` may be annihilated by every weight functional in a particular restricted family. The two-prime Kurihara numbers are **specific constrained weighted sums**, varying with auxiliary conductors, not arbitrary evaluation functionals. Thus this evidence **does not imply** `m2(p)=0`, `Sha[p∞]=0`, `Fitt_2(Sel_{p∞}^dual)=Z_p`, a p-uniform `C`, or complete BSD. Rank-two Euler-system/Kolyvagin derivative compatibility and the integral Fitting comparison remain unproved.

Next step: independently parse/check the exact canonical JSON, its SHA256, denominator/content and two-term Bézout identity, without calling Sage. [New independent audit script](../verification/bsd389_fixed_rational_manin_independent_audit.py); **not yet user executed** at time of this note.
