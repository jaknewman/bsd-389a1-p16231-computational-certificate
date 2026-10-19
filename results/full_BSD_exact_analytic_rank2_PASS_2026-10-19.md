# Full BSD 389a1: certified analytic rank 2 (2026-10-19)

**Input:** Researcher's executed terminal commands under SageMath 10.9, following rigorous Arb integration. **Status:** exact central modular symbol PASS; positive rigorously enclosed second Taylor coefficient PASS.

## Exact central vanishing

```python
from sage.all import EllipticCurve, QQ
E = EllipticCurve('389a1')
w = E.root_number()
m0 = E.modular_symbol(sign=1, implementation='eclib')(QQ(0))
assert w == 1
assert m0 == 0
```

Researcher's output:

```text
ROOT_NUMBER 1
MODULAR_SYMBOL_AT_ZERO 0
BSD389_EXACT_CENTRAL_VANISHING_PASS
BSD389_ANALYTIC_RANK_TWO_WITH_ARB_PASS
```

Exact sign-one modular symbol zero implies `L(E,1)=0` (the modular symbol's L-value has a nonzero period scaling). The root number +1, by the functional equation around `s=1`, forces `L'(E,1)=0`.

## Rigorous nonvanishing of quadratic term

See [certified Arb Lstar](full_BSD_phase1_Arb_Lstar_interval_PASS_2026-10-19.md), which used rigorously enclosed integration over 4 intervals plus explicit, separately validated Fourier and integral tails:

```text
L''(E,1)/2 ∈ [0.7593165002884268 +/- 7.81e-17] > 0
```

Under exact central vanishing, the functional-equation Mellin identity used by the Arb integral identifies this enclosure with `L''(E,1)/2`. Since this interval excludes zero,

```text
ord_{s=1} L(E,s) = 2.
```

The rank of `E(Q)` was independently reported proved 2 (rank/generators), giving the **rank equality predicted by BSD for this one curve**.

## Remaining full BSD barriers

Neither this rank equality nor numeric period–regulator agreement proves the leading-term equality. Nor does it prove `Sha(E/Q)` finite or trivial globally. The 16231-primary result remains tied to the explicit computer-assisted coefficient bridge.

Next targeted arithmetic task: certify `Sha(E/Q)[2^infinity]=0` using exact 2-Selmer computation and the Kummer exact sequence. This is distinct from any global finiteness claim.
