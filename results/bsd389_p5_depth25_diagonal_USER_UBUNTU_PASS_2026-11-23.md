# BSD389: authenticated USER Ubuntu rerun — full p5 depth25 diagonal Kurihara certificate

Date: 2026-11-23. Execution platform: user's Ubuntu terminal with conda `sage` environment; optimized `g++ -O3 -std=c++17`. This is a **genuine user reproduced full computation**, not only an assistant-side execution.

## Exact command

```bash
g++ -O3 -std=c++17 \
  verification/bsd389_p5_depth25_real_two_prime_diagonal_native.cpp \
  -o /tmp/bsd389_p5_depth25
/tmp/bsd389_p5_depth25
```

## Actual terminal stdout from the user

```text
P5_MOD25_LOCAL_POINT_COUNTS 5375 10650
P5_MOD25_TRUE_LOCAL_MW_MATRIX [[1,14],[1,2]] DET 13
0 0 0
0 22 16
0 17 14
P5_MOD25_DEEP_Q1 5351 TRACE -23
P5_MOD25_DEEP_Q2 10651 TRACE 2
P5_MOD25_DEEP_COUNTS 28488750 nonzero_symbols 23811548
P5_MOD25_DEEP_MIXED_KURIHARA 22 diagonal 22 pure2 0,0 pure_linear 0,0 augmentation 0
P5_MOD25_EXACT_DIAGONAL_MATCH PASS
SECONDS 4.77932
```

## Precise mathematical outcome

At E389a1 and `p=5,k=2,q1=5351,q2=10651`, genuine finite-field point counting yields `#E(F5351)=5375`, `#E(F10651)=10650` and `a_q=(-23,2)`, giving both auxiliary congruences `q≡1` and `a_q≡2 mod25`.

The saturated rational Mordell–Weil P,Q local coordinates are `(1,14)`, `(1,2)` modulo 25; the local determinant `13` is a 5-adic unit.

All `φ(q1q2)/2=28,488,750` plus-symmetry primitive classes were enumerated using the previously authenticated frozen 390-edge integer modular-symbol vector. The complete degree≤2 moment matrix modulo 25 equals

```
0  0  0
0 22 16
0 17 14
```

Therefore `M11=22 mod25` is a 5-adic unit and exactly equals the cyclic diagonal theta's degree-two coefficient. The verification confirms this finite-level identity and the low-jet vanishing at p². It does **not independently regenerate the frozen Manin integer vector** in Sage/eclib.

The true general Hecke norm / diagonal theorem appears in `paper/bsd389_p2_deep_Hecke_diagonal_full_Kurihara_mod25_2026-11-23.md`.

**Boundary:** this certificate is for the fixed prime p5. Even with the exact depth-p² formula, it does not construct an all-large-p unit nonvanishing theorem or a global finite Sha annihilator, nor the exact archimedean BSD leading-term identity.
