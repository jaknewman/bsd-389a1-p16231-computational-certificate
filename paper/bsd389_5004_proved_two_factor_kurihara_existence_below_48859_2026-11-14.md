# E389a1: exactly 5004 good primes p<48859 with certified *existence* of two-factor Kurihara units

Date: 2026-11-14. **The arithmetic input is a PUBLISHED FINITE-RANGE theorem plus one archived p107 certificate; this note deduces a new *nonconstructive* statement about 5004 two-factor Kurihara witnesses. No infinite-range uniform bound, global Sha finiteness, or strong BSD is proved.**

## 1. Published theorem that we can now reuse without new p-adic computation

William Stein and Christian Wuthrich, "Algorithms for the arithmetic of elliptic curves using Iwasawa theory", *Mathematics of Computation* **82** (2013), Theorem 12.3, printed page 1788:

> For E=389a1, Sha(E/Q)[p]=0 for p=2 and for all 5005 **good ordinary** primes p<48859 except p=16231.

Primary PDF: https://wstein.org/papers/mcom2649-iwasawa-alg.pdf, printed p.1788, page index31. (The theorem covers p=3 among its 5005 ordinary primes, but the Kurihara/CS statement below is restricted to p≥5.)

Its excluded bad or supersingular primes are

$$
107,\ \mathbf{389},\ 599,\ 1049,\ 2957,\ 6661,\ 8263,\ 9397,\ 9551,\ 14633,\ 15101,\ 28591,\ 30671,\ 30869,\ 31799,\ 34781,\ 36263,\ 45161.
$$

Additionally, p=16231 is **ordinary**, but exceptional for the Stein–Wuthrich computation because of unexpectedly high p-adic regulator valuation; its absence is not a statement that Sha there is nonzero.

This is an unconditional published p-torsion vanishing result over that finite range, **not** a blanket all-prime theorem.

## 2. Exact arithmetic inventory

Below 48859, there are 5024 rational primes, including 2 and 3. Restricting to p≥5 leaves 5022; removing bad p=389 leaves exactly 5021 good primes.

Of those 5021 good p≥5:
- 5003 ordinary primes are covered by Stein–Wuthrich Theorem 12.3;
- 17 are good supersingular primes, one of which is p=107;
- 1 ordinary exception is p=16231.

For p=107, the project has **separate proof-mode Sage p_primary_bound(107)=0**, archived in [USER PASS](../results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md), as well as a distinct archived p107 normalized Kurihara coefficient and its native frozen archive aggregate.

Thus there are exactly

$$
\boxed{5003+1=5004}
$$

good p≥5 below 48859 with Sha[p∞]=0, covered by the union of these *genuine* proved inputs. There are 17 remaining good primes below the cutoff whose Sha[p∞] is not established by these two sources:

$$
\boxed{
599,\ 1049,\ 2957,\ 6661,\ 8263,\ 9397,\ 9551,\ 14633,\ 15101,\ 16231,\ 28591,\ 30671,\ 30869,\ 31799,\ 34781,\ 36263,\ 45161.
}
$$

These 17 are **exceptions to this pair of sources**, not assertions that their Sha is nonzero or has no alternative proof. Note the prime 389 is bad and omitted from the good-prime comparison.

## 3. New derived theorem: 5004 existence statements with only TWO factors

Let \(\mathcal P\) be the explicit subset of 5004 good p≥5 below48859 certified in §2. For E389a1, the Néron-integral plus-symbol normalization and p-unit Manin constant are fixed, and the residual Galois representation is surjective for each such p (see the existing user-run project's global mod-p representation certificate, and the [LMFDB curve](https://www.lmfdb.org/EllipticCurve/Q/389a1/)).

**Theorem.** For EVERY p∈\(\mathcal P\) there exist distinct good auxiliary primes q1(p),q2(p) such that

$$
q_i\equiv1\pmod p,\quad a_{q_i}\equiv q_i+1\pmod p,
\qquad
\boxed{\widetilde\delta_{q_1q_2}(389a1)\ne0\pmod p.}
\tag{1}
$$

**Proof.** For each p in \(\mathcal P\), Stein–Wuthrich or the separate p107 Sage theorem gives Sha(E/Q)[p]=0 and thus Sha[p∞]=0 (any nontrivial p-primary torsion group has a nontrivial element of order p). Hence the exact rank-two Kummer sequence gives Sel(E[p∞]/Q)^∨≅Z_p², with Fitt_2=Z_p. Under the proven Castella–Sano Theorem B (ordinary or, for the supersingular p107, squarefree conductor), the minimum \(\partial^{(\infty)}(\widetilde\delta)\) is zero since Tamagawa product is1. Kim Theorem 1.8 then gives \(\rho=\mathrm{corank}\,\mathrm{Sel}=2\) and

$$
\mathbb Z_p=\mathrm{Fitt}_2(X_p)
=p^{\partial^{(2)}-\partial^{(\infty)}}\mathbb Z_p
=p^{\partial^{(2)}}\mathbb Z_p.
$$

Therefore \(\partial^{(2)}=0\), so a two-prime normalized Kurihara unit exists. This proof requires neither E(Q_p)[p]=0 nor constructing the auxiliary primes. QED.

Sources:
- C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf.
- F. Castella and T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B, https://arxiv.org/abs/2601.14504.

**Boundary:** This is a finite collection of 5004 provable existence statements. q1(p),q2(p) are **not explicitly supplied** by Stein–Wuthrich or this argument. The user-executed explicit witnesses at p5,7,11,107 remain separate arithmetic certificates.

## 4. An actual *bounded-range*, NOT global, integer annihilator

Let \(\mathcal E\) be the 18 uncertified primes p≥5 below48859, i.e. the 17 good exceptions above plus bad p=389. Set

$$
D_{\rm low}=\prod_{p\in\mathcal E}p
=627863883549010692613176172370737913398606747759161305426648442740476277.
$$

For each p≥5 below48859:
- if p∤D_low, then Sha(E/Q)[p]=0 by the established sources;
- if p|D_low, multiplication by p kills Sha(E/Q)[p] **by definition**.

Thus, **unconditionally from the published finite-range theorem and the archived p107 result,**

$$
\boxed{
D_{\rm low}\cdot\bigoplus_{\substack{5\le p<48859\\p\text{ prime}}}
\Sha(E/\mathbb Q)[p]=0.}
\tag{2}
$$

The subgroup on the left is finite, since only finitely many p are involved and each Sha[p] is finite. Equation (2) controls **only order-p torsion in this finite interval**, not higher-order p^n-torsion at exceptional primes nor any p≥48859. This integer is not a global Sha annihilator and does not prove global finiteness.

The [dependency-free standard-library verifier](../verification/bsd389_kurihara_5004_primes_published_range_audit.py) was executed by the assistant on 2026-11-14 to check the sieve counts, the 17 exceptions, product D_low and the arithmetic consistency of this deduction. It does NOT rerun Stein–Wuthrich's large p-adic computations or compute 5004 Kurihara sums.

## 5. Honest boundary on the user-requested *decisive bound*

The desired asymptotic \(\exists B\ \forall p>B:\mu_p\le3\) **is not proved** by this finite-range coverage. Since \(\mu_p\in\{2,4,6,\ldots\}\), such a bound would force \(\mu_p=2\) and finite prime support of Sha, but the all-large-p step still requires new integral arithmetic input. The potential denominator of a rational determinant, a prime-independent finite Fitting comparison, or degree-two Kato leading-term primitivity is **not constructed** by any of the cited published sources or archived Hecke Smith computations.

For clarity: Stein–Wuthrich Theorem 12.3 gives a very strong **bounded-range certificate**, not an upper bound on the possible primes dividing Sha for 389a1. The original bad prime 389 and the 17 good exceptions are finite extra obligations **even if** an all-large-p tail theorem were ultimately found.

**Verdict:** exactly 5004 proven nonconstructive two-prime unit-witness existence statements, one explicit bounded-range annihilator on Sha[p], and an exact exceptional set; no uniform all-large-p theorem and no strong BSD.
