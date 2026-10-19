# Full BSD 389a1: the global finiteness obstruction and a derived-Heegner route

**Date:** 2026-10-19. **Research status:** mathematical roadmap and exact local gates; no global finiteness or full BSD theorem claimed.

## 1. Formal global obstruction

For `E: y²+y=x³+x²−2x`, conductor `389`, analytic/algebraic rank `2`, all archived:

- Rigorous analytic order `ord_{s=1}L(E,s)=2`: exact modular symbol `L(E,1)=0`, root number `+1`, positive Arb interval for `L''(E,1)/2`.
- `Sha[p^infinity]=0` for `p=2,3,5,7,11,13` via exact Selmer computations and Sage proved p-primary bounds.
- `Sha[16231^infinity]=0`: strong computer-assisted conditional certificate with faithful C01 historical production as explicit trusted premise.
- Numeric `L''/2 = Omega Reg`, **not** an exact complex BSD equality.

For any torsion abelian group `A`, `A=0 iff A[p]=0` for **every** prime `p`. Since the Weil–Châtelet group, and hence Sha, is torsion, to show `Sha(E/Q)=0` we must either establish a uniform finite exceptional set of primes with complete local elimination or produce a truly global theorem. **Finitely many individual Selmer computations cannot by themselves meet the global quantifier.**

The documented Sage result `E.sha().bound_kolyvagin() == (0,0)` for `389a1` signifies **no information about global finiteness**, not a bound of order zero. Source: https://doc.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/elliptic_curves.html

## 2. Structural dead end: ordinary rank-one Heegner cannot close rank-two E

For any imaginary quadratic `K=Q(sqrt(D))`, the Artin identity

`L(E/K,s) = L(E/Q,s) L(E^D/Q,s)`

shows that `ord_{s=1}L(E/K,s) >= 2` since `ord_{s=1}L(E/Q,s)=2`. Thus the classical rank-1 Gross–Zagier–Kolyvagin theorem for `E/K` cannot directly establish finite Sha globally for this curve. Its hypotheses are not satisfied for *any* quadratic base-change.

## 3. New relevant research: Chan-Ho Kim, Sep 2026

'On the arithmetic of Tate-Shafarevich groups via Kolyvagin's conjecture', https://arxiv.org/abs/2609.15328 , preprint dated 2026-09-14, Theorem 1.1, investigates derived Heegner points and gives an equivalence for **p-primary finiteness at a fixed p** in arbitrary rank, under detailed semistable/Heegner/representation hypotheses. Remark 1.9 specifies ordinary primes need `N^+=N` split, `p` split, and quadratic twist analytic rank at most 1. A preprint is not a settled unconditional general BSD theorem.

Critically, the results concern a specified prime p and **do not supply a uniform support bound across every p**; the global finiteness problem remains.

## 4. Concrete test case K=Q(sqrt(-19))

Elementary **exact** arithmetic:
```text
D_K = -19 is a negative fundamental discriminant.
389 is prime and splits: sqrt(-19) mod 389 = +/-52 (roots 52,337).
p=16231 splits: sqrt(-19) mod 16231 = +/-7139 (roots 7139,9092).
p does not divide conductor N=389; good ordinary and mod-p surjective known from local IONOS gate.
Root number E=+1; twist E^(-19) expected root number -1.
Conductor E^(-19) expected 389*19^2 = 140429.
```

**NOT established yet:** `ord_{s=1}L(E^(-19),s)=1`, which is a necessary condition in Kim's ordinary-prime Remark 1.9 (odd root number by itself guarantees only odd analytic rank).

Next IONOS test (cheap; NO inference of proof of twist analytic rank from a single decimal):

```python
from sage.all import EllipticCurve, ZZ, kronecker_symbol
E = EllipticCurve('389a1')
D = ZZ(-19); p = ZZ(16231)
print('HEEGNER_SPLITS', kronecker_symbol(D,389), kronecker_symbol(D,p))
T = E.quadratic_twist(D)
print('TWIST_CONDUCTOR', T.conductor(), 'TWIST_ROOT', T.root_number())
Lp = T.lseries().dokchitser(prec=80, algorithm='pari')
print('TWIST_LPRIME_AT_ONE_NUMERICAL', Lp.derivative(1,1))
```

If `L'(E^(-19),1)` is numerically nonzero, this is a **candidate** for a later exact Arb interval proof of analytic rank one, and a basis for an independent derived-Heegner p-adic study. Even success does not prove the global Sha finite support or complex BSD leading-term identity.

## 5. Actual full BSD proof gates

(A) Uniform support/elimination of all Sha[p] (or another unconditional proof global Sha finite and order), **OPEN**.

(B) Rigorous analytic L''/2 enclosure, **PASS**; exact Mordell-Weil rank and torsion/Tamagawa, **PASS**.

(C) Exact complex leading coefficient formula `L''/2 = Omega*Reg*#Sha`, **OPEN**. Even if (A) gave `Sha=0`, numerical agreement (B) is not an exact transcendental identity.

Avoid calling (A) or (C) proved because of agreement to 35 digits.
