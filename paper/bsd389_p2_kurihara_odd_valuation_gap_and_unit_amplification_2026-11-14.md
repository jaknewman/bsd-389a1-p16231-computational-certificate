# E389a1: a p²-precision two-factor Kurihara witness forces p-primary Sha triviality

**14 November 2026.** **Status:** A newly isolated **rigorous arithmetic deduction** from C.-H. Kim, Theorem 1.8, Castella–Sano, Theorem B, the unconditional Kummer splitting for a known rank-two Mordell–Weil group, and the Cassels–Tate alternating pairing. The deduction does **not** construct a new p²-level Kurihara coefficient or settle uniform Sha support / strong BSD.

## 1. Exact sources and notational distinction

Curve E=389a1: y²+y=x³+x²−2x; conductor 389, rank E(Q)=2, torsion zero, Tamagawa product 1, no CM. The Manin constant of the optimal modular parametrization is 1. The recorded p-adic Galois image is maximal at every prime; see https://www.lmfdb.org/EllipticCurve/Q/389a1/ .

Sources:

1. C.-H. Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, American Journal of Mathematics (2025), Thm 1.8, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf .
2. F. Castella–T. Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin* (2026), §1.1.4 Theorem B, https://web.math.ucsb.edu/~castella/Kurihara.pdf .
3. The exact rank-two Kummer–Fitting identity already proved in [our project](bsd389_unconditional_rank2_kummer_fitt2_identity_2026-10-30.md).

Fix p≥5, p≠389, with surjective residual representation, and the p-unit Manin constant. Let N_k be the squarefree products n=q1...qr of p^k-admissible good primes:

$$
q\equiv1\bmod p^k,\qquad a_q(E)\equiv q+1\bmod p^k.
$$

The **correct** coefficient ideal (in Z_p) is

$$
I_q=(q-1,\ a_q-q-1)\mathbf Z_p,\qquad
\boxed{I_n=\sum_{q\mid n}I_q}.
$$

Thus if both q1 and q2 belong to N_2, then I_n⊆p²Z_p, so reducing δ_n modulo p² is meaningful. **Do not replace I_n by a product.**

Kim defines the minimum degree

$$
r_p=\mathrm{ord}(\widetilde\delta_p)
=\min\{\nu(n):\widetilde\delta_n\ne0\text{ in }\mathbf Z_p/I_n\}
$$

and the valuation invariants \(\partial_p^{(j)}\), with \(\partial_p^{(2)}=\infty\) if every two-prime coefficient vanishes in its finite-level quotient.

**Important:** "coefficient nonzero in Z_p/I_n" is not the same as "coefficient a unit modulo p". This distinction is necessary to discuss nontrivial finite p-primary Sha; arbitrary-degree mod-p Kurihara nonvanishing does not force degree two.

Castella–Sano Theorem B gives, for p good ordinary or good supersingular with conductor squarefree:

$$
\boxed{\partial_p^{(\infty)}=v_p(\mathrm{Tam}_E)=0.}\tag{CS}
$$

Both ordinary and supersingular good primes are covered for E389a1; the published theorem yields *some* mod-p unit at **unspecified auxiliary degree**. This is already a uniform published nonvanishing theorem, **not** a claim that a two-prime unit exists.

## 2. Exact all-prime parity and Fitting theorem

**Theorem A (proved from the published theorems).** Under the above conditions,

$$
\operatorname{Fitt}_{2,\mathbf Z_p}
\bigl(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee\bigr)
=
p^{\partial_p^{(2)}}\mathbf Z_p
$$

with convention p^∞Z_p=(0), and

$$
\boxed{\partial_p^{(2)}\in\{0,2,4,6,\ldots\}\cup\{\infty\}.}\tag{A}
$$

Moreover:

- If \(\partial_p^{(2)}=e<\infty\), then \(\Sha(E/\mathbf Q)[p^\infty]\) is finite, with **exact order p^e**.
- If \(\partial_p^{(2)}=\infty\), then \(\Sha(E/\mathbf Q)[p^\infty]\) has positive Z_p-corank, and hence is infinite.

**Proof.** From the known rank-two MW basis, the Kummer exact sequence gives an unconditional isomorphism of finitely generated Z_p-modules

$$
X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee
\simeq\mathbf Z_p^2\oplus\Sha(E/\mathbf Q)[p^\infty]^\vee.
$$

If \(\partial_p^{(2)}<\infty\), some two-prime δ_n is nonzero in Z_p/I_n; Kim's definition gives \(r_p\le2\). Since \(\operatorname{corank}X_p\ge2\) and Kim 1.8 identifies \(r_p=\operatorname{corank}X_p\), necessarily r_p=2. Thus Sha[p∞] has corank zero, so is **finite**. Kim 1.8 also states

$$
\operatorname{Fitt}_2(X_p)=
p^{\partial_p^{(2)}-\partial_p^{(\infty)}}\mathbf Z_p
=p^{\partial_p^{(2)}}\mathbf Z_p,
$$

using (CS). The Kummer splitting identifies the same ideal with \((\#\Sha[p^\infty])\mathbf Z_p\). As finite odd-primary Sha carries a perfect alternating Cassels–Tate pairing, its order is a square. Therefore e is even.

If instead \(\partial_p^{(2)}=\infty\), then r_p>2 (because degree two is absent, degree zero vanishes from L(E,1)=0, and degree one vanishes from the functional equation sign +1). By Kim, \(\operatorname{corank}X_p=r_p>2\). Kummer then gives positive p-Sha corank, and the second Fitting ideal is zero. By (CS), arbitrary-degree δ remains nontrivial, so r_p is finite, but can exceed two. QED.

## 3. A weak mod-p² two-factor witness forces a strong mod-p one

**Theorem B (p²-to-p unit amplification).** Suppose a squarefree n=q1q2 lies in N_2 and its genuine normalized Kurihara coefficient satisfies

$$
\boxed{\widetilde\delta_n\not\equiv0\bmod p^2.}\tag{Binput}
$$

Then

$$
\boxed{\Sha(E/\mathbf Q)[p^\infty]=0,\qquad
\exists n'=q'_1q'_2\in N_1:\widetilde\delta_{n'}\not\equiv0\bmod p.}\tag{B}
$$

The pair n' **need not equal** the pair n; in particular a witness with δ_n≡p·u mod p² need not be a mod-p unit at the same conductor.

**Proof.** Because I_n⊆p²Z_p, condition (Binput) means \(\partial_p^{(2)}\le1\). From Theorem A its only possible finite value is 0. Hence the p-primary Sha is zero; the minimum valuation 0 is attained by some two-prime δ_{n'}, which is a unit modulo p. QED.

**A proof requiring only Kim 1.8, without the separate Castella–Sano result:** Already (Binput) implies \(r_p=2\), Sha[p∞] finite, and \(\partial^{(2)}\le1\); the Kim length formula reads \(\mathrm{length}_{\mathbf Z_p}\Sha[p^\infty]=\partial^{(2)}-\partial^{(\infty)}\in\{0,1\}\). Cassels–Tate forces the length to be even, hence zero. The **existence of another unit pair** specifically uses the known (CS) normalization \(\partial^{(\infty)}=0\).

**Quantitative extension.** If n=q1q2∈N_k and δ_n is nonzero modulo p^k, then

$$
\partial_p^{(2)}\le k-1,\quad
\boxed{\#\Sha(E/\mathbf Q)[p^\infty]\mid
p^{\,2\lfloor(k-1)/2\rfloor}.}\tag{Q}
$$

At k=2 this gives order 1. At k=3 or 4 it bounds the order by p² (in particular it excludes all higher exponents and nonzero divisible corank). This is a **one-witness theorem**, not an actual high-precision certificate for a new p.

## 4. Chebotarev: the deep auxiliary primes do exist

Under surjectivity of \(\rho_{E,p^2}:G_\mathbf Q\twoheadrightarrow\mathrm{GL}_2(\mathbf Z/p^2)\), which is consistent with the known maximal ell-adic image for E389a1, the p²-admissibility congruences are equivalent to

$$
\mathrm{tr}(\mathrm{Frob}_q)\equiv2,\qquad
\det(\mathrm{Frob}_q)\equiv1\pmod{p^2}.
$$

Among reduction modp matrices with characteristic polynomial (T−1)², exactly 1 is identity and p²−1 are **nonidentity unipotent**. For the identity the trace/det constraints on a p²-lift are dependent, giving p³ lifts. For each nonidentity unipotent they are independent, giving p² lifts.

Since \(|\mathrm{GL}_2(\mathbf Z/p^2)|=p^4\,p(p-1)^2(p+1)\), Chebotarev gives

$$
\boxed{\delta_{\mathrm{p^2\ adm,\ nontriv\ unip}}=\frac1{p^3(p-1)}},\tag{D1}
$$

$$
\boxed{\delta_{\mathrm{p^2\ adm,\ scalar\ modp}}=\frac1{p\,|\mathrm{GL}_2(\mathbf F_p)|}},\tag{D2}
$$

$$
\boxed{\Pr(\mathrm{nontriv\ unip}\mid\mathrm{p^2\ adm})
=\frac{p^2-1}{p^2+p-1}.}\tag{D3}
$$

All the sets have **positive** prime density. This proves the existence of infinitely many p²-admissible *local candidates*, but says nothing about the nonvanishing of their **global** Kurihara coefficient. The case of q whose Frobenius is scalar modp is not excluded by the mere p²-congruences.

The [independent exact standard-library verifier](../verification/bsd389_p2_auxiliary_density_exact.py) exhaustively counts p²-lifts at p=5,7 and checks the rational formulas at p=5,7,11,107,16231. It was executed by the assistant on 2026-11-14; output includes:
- p=5: regular=600, scalar=125 admissible lifts; regular density 1/500;
- p=7: regular=2352, scalar=343 admissible lifts; regular density 1/2058.

The verifier is **only** finite matrix combinatorics, not a proof of any new δ≠0.

## 5. Current unsolved input and separation from strong BSD

The new sufficient condition (Binput) is **strictly weaker as a numerical congruence** than the demand that the same p²-admissible δ_n be a unit mod p. It demands **deeper prime congruences** on both auxiliaries, so it is not automatically easier computationally.

To deduce all-large-p Sha vanishing one would now need, for all large p, the existence of at least one degree-two p²-level nonzero Kurihara coefficient, or a different independent global Selmer/Fitting bound. Neither is established here. The p11 pair 397·991 is only **p-admissible**, not p²-admissible; its genuine mod11 unit run remains untouched.

Even if every prime-primary Sha group were shown trivial, the exact **complex** identity involving \(L''(E,1)/2\), the Néron period and the regulator is a separate theorem requirement.

**Verdict:** rigorous p²-to-p amplification and parity gap, with exact deep-auxiliary positive-density proof; no global BSD conclusion.
