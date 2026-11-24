# BSD 389a1 — 2026 Castella–Sano + Kim close the uniform Kato divisibility-index problem; true remaining obstruction is exactly TWO-factor nonvanishing

**24 November 2026.** This is an audit and an exact new specialization/corollary of published theorems. It DOES NOT prove the all-prime \(\Sha(E/\mathbf Q)=0\) statement or complex rank-two BSD. It avoids proposing another auxiliary finite computation.

## Setup and fully stated large-p hypotheses

Let \(E:y^2+y=x^3+x^2-2x\) be the optimal rational elliptic curve 389a1, with \(N=389\) squarefree, no CM, Tamagawa product \(1\), \(E(\mathbf Q)=\mathbf Z^2\), root number \(+1\), analytic rank \(2\) (the latter independently certified by modular symbols and Arb in this repository). For every sufficiently large rational prime \(p>5\), we have:
- \(p\nmid N\), so reduction is **good**, either ordinary or supersingular; in the latter case \(N\) is squarefree;
- \(\bar\rho_{E,p}(G_\mathbf Q)=\mathrm{GL}_2(\mathbf F_p)\) by Serre's non-CM open-image theorem; no effective cutoff is claimed here;
- the optimal Manin constant is a p-unit since \(p^2\nmid N\) (Mazur's theorem, as quoted verbatim in Castella–Sano §1.1.1).

These are exactly the hypotheses of Castella–Sano [CS26] Theorem B, for every sufficiently large p.

Let \(\mathcal N_p\) denote their squarefree products of Kurihara-admissible primes. For \(n\in\mathcal N_p\), let \(\delta_n\in\mathbf Z_p/I_n\) be their authentic normalized modular-symbol sum and \(\nu(n)\) the number of prime factors. Set
\[
\rho_p=\min\{\nu(n):\delta_n\ne0\},\quad
\partial_p^{(i)}=\min_{\nu(n)=i}v_p(\delta_n),\quad
\partial_p^{(\infty)}=\min_i\partial_p^{(i)}.
\]
In these formulas \(v_p\) of a residue in \(\mathbf Z_p/I_n\) is the **truncated valuation** defined exactly in Kim §1.5 and CS §1.1, with \(v_p(0)=+\infty\). To test nonzero modp one needs p|I_n; standard admissibility ensures this.

## Theorem 1 (uniform nonvanishing proven, not conjectural)

By Castella–Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin* (January 20, 2026), **Theorem B** (good ordinary, or good supersingular with N squarefree),
\[
\boxed{\partial_p^{(\infty)}=v_p(\mathrm{Tam}_E)=0
\quad\text{for every sufficiently large }p.}
\]
Therefore there exists some squarefree \(n\in\mathcal N_p\) with \(\delta_n\bmod p\ne0\), unconditionally for the large-p tail. This says **nothing about an upper bound on \(\nu(n)\)**. For 389a1, parity and exact modular symbol rank imply the relevant n must have an even positive number of factors, at least 2. Local Chebotarev alone cannot fix that number.

## Theorem 2 (complete large-p three-way structural alternative)

Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.8 (AJM accepted/published, manuscript May 12, 2025), applies as soon as the collection \(\delta\) is not identically zero. Its equalities specialize to
\[
\boxed{\operatorname{corank}_{\mathbf Z_p}
\operatorname{Sel}_{p^\infty}(E/\mathbf Q)=\rho_p},
\quad
\boxed{\operatorname{Fitt}_{i,\mathbf Z_p}(X_p)
=(p^{\,\partial_p^{(i)}-\partial_p^{(\infty)}})
=(p^{\partial_p^{(i)}}),\quad i\ge\rho_p,\ i\equiv\rho_p\bmod2.}
\]
Here \(X_p=\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee\). The second equality uses CS Theorem B. The source also gives \(\operatorname{length}_{\mathbf Z_p}(\operatorname{Sel}_{p^\infty}/\mathrm{div})=\partial_p^{(\rho_p)}\).

Our saturated MW rank2 embeds \((\mathbf Q_p/\mathbf Z_p)^2\) into the Selmer group; hence \(\rho_p\ge2\). The root number is \(+1\) and the modular-symbol functional equation gives \(\delta_n=0\) for odd \(\nu(n)\), so \(\rho_p\in\{2,4,6,\dots\}\).

The **three mutually exclusive cases** for every sufficiently large p are:

1. \(\rho_p=2\), \(\partial_p^{(2)}=0\). Then \(X_p\) has \(\mathbf Z_p\)-rank 2 and \(\operatorname{Fitt}_2(X_p)=\mathbf Z_p\), hence \(\boxed{\Sha(E/\mathbf Q)[p^\infty]=0}\).
2. \(\rho_p=2\), \(\partial_p^{(2)}>0\). Then \(\Sha[p^\infty]\) is finite of exact order \(p^{\partial_p^{(2)}}\). Its exponent is *not* determined by the order alone. The finite Cassels–Tate alternating pairing makes \(\partial_p^{(2)}\) an **even integer at least 2**.
3. \(\rho_p\ge4\). Then \(\Sha[p^\infty]\) has **positive \(\mathbf Z_p\)-corank** \(\rho_p-2\), so it is infinite and contains a divisible \((\mathbf Q_p/\mathbf Z_p)^{\rho_p-2}\) subgroup. This is NOT ruled out by the published Iwasawa main conjecture or CS Theorem B. The finite quotient by its maximal divisible subgroup still has the Kim-prescribed length.

These follow by taking the exact Kummer sequence
\[
0\to (\mathbf Q_p/\mathbf Z_p)^2\to\operatorname{Sel}_{p^\infty}
\to\Sha(E/\mathbf Q)[p^\infty]\to0
\]
and applying Kim Theorem 1.8 and finite odd-primary Cassels–Tate duality.

### The exact iff-condition for a fixed p

Since \(\partial_p^{(\infty)}=0\),
\[
\boxed{
\Sha(E/\mathbf Q)[p^\infty]=0
\quad\Longleftrightarrow\quad
\exists\, n=q_1q_2\in\mathcal N_p:
\delta_{q_1q_2}\not\equiv0\pmod p.
}
\tag{*}
\]
Proof (right to left): such n makes \(\rho_p\le2\) and \(\partial_p^{(2)}=0\). Rank2 and central vanishing force \(\rho_p\ge2\), so Kim gives Fitt2(Xp)=Zp, hence Sha0. Proof (left to right): if Sha0, Selmer corank is exactly2, hence \(\rho_p=2\) by Kim. Also Fitt2(Xp)=Zp, hence \(\partial_p^{(2)}=0\), forcing some genuine two-prime residue to be a unit modulo p by definition of the min. QED.

**This is a necessary-and-sufficient equivalence, not just a sufficient Kurihara test.** Consequently *CS Theorem B guarantees some nonzero witness at unknown even \(\nu(n)\)* but CANNOT be promoted to two factors without precisely solving the remaining large-p Sha-vanishing problem. The once-proposed "prove existence of two factors for every large p" is now seen to be **equivalent to** the missing result. It is not a shortcut proved by Chebotarev or by CS alone.

For a genuine two-factor residue with valuation 1 modulo p², under the same assumptions, Kim gives a finite Sha5 order exponent e≤1 if \(\rho=2\), but Cassels–Tate forces e even. Therefore e=0 and, by (*), there must exist **another** two-factor pair with a p-unit residue. This reconciles the previous depth-p² criterion with the new equivalence.

## Theorem 3 (Kato's global divisibility index is already explicit, with local correction)

The same Castella–Sano paper, **Theorem 2.1.3** and equations **(2.16)–(2.17)**, proves via the exact reciprocity law
\[
\overline{\exp^*}(\operatorname{res}_p\kappa_n^{\rm Kato})
=u\cdot\#E(\mathbf Q_p)[p^\infty]\cdot\delta_n
\]
and the divisibility-index identities that
\[
\boxed{
\mathcal M_\infty(\kappa^{\rm Kato})
=
v_p(\#E(\mathbf Q_p)[p^\infty])
+\partial_p^{(\infty)}
=
v_p(\#E(\mathbf Q_p)[p^\infty]).
}
\tag{**}
\]

This is a genuine **published uniform control of the Kato-system divisibility index**. The older project note claiming this index remained wholly unknown, or that no existing explicit reciprocity bridge existed, was OVERSTATED. The bridge exists, and the divisibility index is entirely a LOCAL quantity in this large-p tail.

For p≥7 of good reduction, the formal reduction kernel \(E_1(\mathbf Q_p)\) is torsionfree at p by the formal logarithm; thus \(E(\mathbf Q_p)[p^\infty]\hookrightarrow E(\mathbf F_p)[p^\infty]\). Hasse:
\[
\#E(\mathbf F_p)\le p+1+2\sqrt p<2p\quad(p\ge7).
\]
Thus \(\boxed{v_p(\#E(\mathbf Q_p)[p^\infty])\le1}\). In supersingular reduction a_p(E)=0, so \(\#E(\mathbf F_p)=p+1\), and this valuation is 0. For ordinary **nonanomalous** p, \(p\nmid \#E(\mathbf F_p)\), and again valuation 0. The exceptional local correction at any large p is at most one factor p; NO assertion is made that anomalous primes are finite.

**BSS/Mazur–Rubin normalization warning:** The index \(\mathcal M_\infty(\kappa^{\rm Kato})\) in (**) is defined for the *classical* Kato Kolyvagin system in CS/MR notation. To replace the scalar \(v_p(a_p)\) from the project's BSS rank-one generator decomposition by this index, one MUST prove that the chosen BSS and CS systems and auxiliary normalizations agree up to a unit under the natural identification of the two Kolyvagin modules. The value (**) itself DOES NOT require that comparison.

## What the exact result proves—and does NOT

- ***Proved for all sufficiently large p:*** the main conjecture in the CS setting implies \(\partial^\infty_p=0\); some finite-factor Kurihara coefficient is a unit; Kato's full system has divisibility index at most 1 after its local factor; the true Selmer corank and Fitting ideals are exactly controlled by the **first** nonvanishing Kurihara depth \(\rho_p\) and its valuations.
- ***Not proved:*** \(\rho_p=2\) for each large p; any uniform bound on \(\rho_p\) that would force it to 2; any prime-independent finite-support integer D bounding Sha. Thus neither the global finiteness nor the vanishing of Sha(E/Q) is established.
- ***Separate from ALL of this:*** the exact *complex* rank-two BSD leading-term identity \(L''(E,1)/2=\Omega_E\mathrm{Reg}_E\) remains unproved. The entire discussion is p-adic Selmer structure, not an Archimedean comparison.

## Primary cited originals, with sections/theorems

1. Francesc Castella and Takamichi Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, 20 January 2026, **Theorem B**, **Theorem 2.1.3**, equations (2.16)–(2.17): https://web.math.ucsb.edu/~castella/Kurihara.pdf
2. Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, manuscript May 12 2025 / *American Journal of Mathematics* 2026, **Theorem 1.8**, §§1.4–1.5: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf
3. Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II*, arXiv:1805.08448, Theorem 5.25 and Corollary 6.18 in arXiv v1 (numbering differs in other editions).

## Research decision

Do NOT launch more finite Kurihara q-pair computations at currently certified primes or more auxiliary extension theta spectra. The ONLY genuinely new uniform rank-two p-tail assertion required to close Sha0 is the **two-factor** claim in (*). This is now an exactly equivalent formulation of the unresolved arithmetic target. A real new route must either bound \(\rho_p\) by 2 without assuming Sha or furnish an independent all-prime Fitt2 bound; simply proving nontriviality of the full Kato system is no longer useful because that nontriviality follows from CS Theorem B.
