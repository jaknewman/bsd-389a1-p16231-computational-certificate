# Rank-two Sha at p=107: Sage Iwasawa upper bound and its precise uniform limit

**Date:** 2026-11-02. **Curve:** E = 389a1, y^2+y=x^3+x^2-2x, conductor 389, MW rank 2.

## 1. Genuine executed user certificate

The user's Ubuntu SageMath 10.9 run of `S = EllipticCurve('389a1').sha(); S.p_primary_bound(p)` completed with exit status 0. It returned exponent 0 for each `p in [5,7,11,13,107]`; `E.ap(107)=0` (good supersingular). The user's terminal reported 163.86 seconds for p107. Transcript: [results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md](../results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md).

This is a Sage-documented *provable upper bound*, not an application of a conjectural BSD order. On a successful run, `p_primary_bound(p)=e` gives `#Sha(E/Q)[p∞] <= p^e`, and e=0 forces trivial p-primary Sha, without presupposing the entire Sha finite.

**Caveat:** the Markdown transcript is a user-provided log transcription; it does not constitute an independent SHA256 verification of the original local log bytes.

## 2. The actual implementation

Public Sage source: <https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py>, method `Sha.p_primary_bound`. Its essential final operation is:

```python
shan = self.an_padic(p, prec=0, use_twists=True)
if shan == 0:
    raise RuntimeError("There is a bug in an_padic.")
return shan.valuation()
```

Prior checks in that method require suitable reduction and mod-p Galois image. The documented mathematical input is Kato / Iwasawa theory as presented by Stein–Wuthrich. The related `an_padic` routine handles supersingular primes with a two-component valued p-adic L-function and normalized regulator; the output ratio is a computationally *conjectural p-adic BSD order* before the separate Kato-based upper-bound interpretation. Thus one must NOT claim that `an_padic` itself proves full p-adic BSD.

Official reference: <https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/sha_tate.html>. Stein–Wuthrich research article: <https://wstein.org/papers/shark/>.

## 3. Exactly what uniformity would require

Write `B_p = S.an_padic(p, prec=0, use_twists=True)` where defined and successfully verified. The implemented upper-bound theorem gives

```text
v_p(B_p) = 0    =>    Sha(E/Q)[p∞] = 0.
```

The desired new result would assert `v_p(B_p)=0` for all sufficiently large good p (or a compatible bound), **without computing each prime separately**. The five successful p-specific computations do not furnish such a theorem. In particular, `B_p` lives in varying p-adic coefficient rings, is normalized using p-adic logarithms and the p-adic regulator, and no *fixed integer* with those unit valuations has been constructed. A numerical strong BSD prediction `#Sha=1` is not a replacement for this uniform statement.

A sound global strategy would require a theorem giving a p-independent integral comparison of the p-adic L-function leading term and regulator, with a fixed finite exceptional prime set and no hidden assumption of the conclusion. None is established by these specific Sage runs.

## 4. P107 dual-source ledger

- **Iwasawa:** independent genuine Sage 10.9 certified upper exponent 0, establishing p107 Sha-primary triviality within the documented hypotheses.
- **Kurihara:** frozen 710 blocks independently reaggregated into delta=34 mod107, but original native numerator loop and correct Néron symbol normalization are separate proof-source obligations.
- **Uniformity:** not established. Neither audit turns a finite list of verified primes into a bound for all primes.

## 5. Precise supersingular two-component source audit (2026-11-02)

The Sage source for `Sha.an_padic` has a separate supersingular branch, not simply an ordinary one-variable ratio. In the branch for good supersingular p, it constructs:

```python
K = reg[0].parent()
lg = log(K(1 + p))
bsdp = tam / tors / lg**r * reg
lps = lp.Dp_valued_series(n, quadratic_twist=D, prec=r + 1)
lstar = [lps[0][r], lps[1][r]]
shan0 = lstar[0] / bsdp[0] if bsdp[0] != 0 else 0
shan1 = lstar[1] / bsdp[1] if bsdp[1] != 0 else 0
```

It raises a `RuntimeError` if both candidate quotients are nonzero yet inconsistent at available precision, and chooses the candidate with better relative precision. Subsequently `p_primary_bound` returns `shan.valuation()` under its residual and reduction preconditions. The actual source should be inspected whenever the installed Sage version differs from the public source. Source: <https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/sha_tate.py>; 2013 Stein–Wuthrich <https://wstein.org/papers/mcom2649-iwasawa-alg.pdf>.

**What the run proves:** Sage returned a certified p107 upper exponent 0. It does *not* reveal both component values or their precise digits in the user's published log, and it does not prove a fixed-integer identity between p-adic quotients for varying primes. Do not invent component valuations or claim they were separately printed.

### Formal obstruction to extrapolating finite certificates

For any finite set of primes S, there exists an infinite torsion abelian group
`A = ⊕_{p∉S} (Z/pZ)`. It has `A[p∞]=0` for every p in S, while A is infinite. Thus finite sets of proven p-primary vanishings cannot logically imply a uniform global bound, even when each proof is independent.

The proposed uniform p-adic conclusion `v_p(B_p)=0` for all large good p is itself powerful enough, combined with appropriate residual and local hypotheses, to force Sha to have finite support and thereby be finite once the remaining p-parts are bounded. No such implication follows from p-adic BSD *predictions* or numerical real BSD leading-term estimates alone.

**Focused next proof obligation:** supply a non-circular p-independent integrality/comparison theorem that controls `B_p` or the two-prime Kurihara leading coefficient outside a finite set. No formula or fixed integer accomplishing this has yet been constructed.
