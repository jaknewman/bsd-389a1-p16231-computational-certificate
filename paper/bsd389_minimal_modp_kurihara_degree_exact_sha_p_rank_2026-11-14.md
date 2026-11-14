# 389a1: minimal mod-p Kurihara degree exactly measures Sha[p] dimension

**Date:** 2026-11-14. **Status:** rigorous new deduction from the exact *proof* of Kim Theorem 1.10, Castella–Sano Theorem B, the Kummer sequence, and Cassels–Tate where relevant. No claim that all p have Sha[p]=0; no global BSD leading-term identity.

## A. Precise hypotheses and the finite minimum

Let E/Q=389a1 with global minimal equation y²+y=x³+x²−2x, proven rank 2, torsion 1, conductor 389, discriminant +389, Tamagawa product 1. Fix a good prime p≥5, p≠389, such that
(i) the residual representation on E[p] is surjective;
(ii) the modular parametrization has p-integral Manin constant;
(iii) E(Q_p)[p]=0.

The local condition (iii) is important: it follows if p does not divide #E(F_p), but it is **not automatically guaranteed** by good reduction and global surjectivity at all p. In particular the argument below makes no assertion about potentially anomalous primes where condition (iii) is not known.

Let N1 be the set of squarefree products of p-admissible auxiliary primes q with q≡1 and a_q≡q+1 modulo p. For n∈N1 let tilde_delta_n be the correctly normalized Kurihara number with I_n=Σ_{q|n}(q−1,a_q−q−1)Z_p. Define

$$
\mu_p=\min\{\nu(n): n\in N_1,\ \widetilde\delta_n\not\equiv0\bmod p\}.
$$

Because E has semistable squarefree conductor and Tamagawa product 1, the good-prime case of Castella–Sano, Theorem B (good ordinary OR good supersingular with N squarefree), gives existence of at least one p-unit Kurihara number. Hence μ_p is a finite integer. Primary source: https://arxiv.org/html/2601.14504 .

## B. Exact minimal-degree theorem (proved)

**Theorem.** Under A,

$$
\boxed{\mu_p=\dim_{\mathbf F_p}\operatorname{Sel}(E[p]/\mathbf Q)
=2+\dim_{\mathbf F_p}\operatorname{Sha}(E/\mathbf Q)[p].}\tag{1}
$$

In particular,

$$
\boxed{\mu_p=2\iff\operatorname{Sha}(E/\mathbf Q)[p]=0
\iff\operatorname{Sha}(E/\mathbf Q)[p^\infty]=0.}\tag{2}
$$

**Proof.** Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, Theorem 1.10, under the conditions (i)–(iii) plus Tamagawa p-units, applies to a nonzero mod-p Kurihara coefficient at minimal auxiliary degree μ_p. In the *proof* of Theorem 1.10 (printed p. 33, lines 1579–1603 of the online PDF) he establishes explicitly:

$$
\mu_p=\dim_{\mathbf F_p}\operatorname{Sel}(E[p]/\mathbf Q).
$$

This is not a fresh claim that local Mordell–Weil independence forces δ nonvanishing: it is a theorem conditional on the already published mod-p Kato primitivity, guaranteed here at some degree by Castella–Sano.

The exact Kummer sequence
$$
0\to E(\mathbf Q)/pE(\mathbf Q)\to \operatorname{Sel}(E[p]/\mathbf Q)
\to\operatorname{Sha}(E/\mathbf Q)[p]\to0
$$
and the certified group E(Q)≅Z² give the second equality of (1). A nonzero p-primary torsion group contains an element of order p, so triviality at p is equivalent to triviality of the full p-primary Sha subgroup. QED.

Primary PDF: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf (Theorem 1.10 and proof of equation (6.1), concluding μ_p=dim Sel_p at printed page 33).

## C. Generalization: scalar-Frobenius is impossible in *any minimal* mod-p witness

Let n=q1...qμ be a unit witness with μ=μ_p, under A. Kim's semilocal theorem provides an isomorphism

$$
\operatorname{Sel}(E[p]/\mathbf Q)
\xrightarrow{\sim}
\bigoplus_{q|n} E(\mathbf F_q)/p.
$$

The source has dimension μ, and each target factor is of dimension at least 1 by q-admissibility. There are exactly μ factors; hence every local target factor has dimension exactly 1. Since the characteristic polynomial of the mod-p Frobenius at q is (X−1)², the Frobenius must be **nonidentity unipotent**, not the scalar identity.

Thus the scalar-Frobenius veto, previously derived only for *degree-two* unit witnesses, in fact holds for **all witnesses at minimal mod-p unit degree**. It does **not** assert that any coefficient for a *nonminimal* n containing a scalar-Frobenius prime vanishes.

## D. Two independent axes: mod-p degree and p-adic precision

Assume now the p-primary Sha group is finite and write its Cassels–Tate paired elementary divisor decomposition

$$
\operatorname{Sha}(E/\mathbf Q)[p^\infty]
\simeq
\bigoplus_{j=1}^{s}(\mathbf Z/p^{e_j}\mathbf Z)^2,\qquad e_j\ge1.
$$

Then (1) gives

$$
\boxed{\mu_p=2+2s.}\tag{3}
$$

This depends only on the number of paired cyclic factors, *not* their exponents. On the other hand, Kim 1.8 and Castella–Sano B (which yields ∂∞=0 because Tamagawa product is 1) give

$$
\operatorname{Fitt}_{2,\mathbf Z_p}
(\operatorname{Sel}_{p^\infty}(E/\mathbf Q)^\vee)
=p^{\partial_p^{(2)}}\mathbf Z_p,
$$

and the unconditional rank-two Kummer–Fitting identity gives

$$
\boxed{\partial_p^{(2)}=v_p(\#\Sha[p^\infty])=2\sum_{j=1}^s e_j.}\tag{4}
$$

In other words:
- **minimal mod-p auxiliary degree** μ_p detects p-rank of Sha;
- **minimal two-prime p-adic valuation** ∂p^(2) detects p-adic order of Sha if it is finite.

Example as an algebraic model, NOT a claim for 389a1: if Sha[p∞]≅(Z/p^a)^2, then μ_p=4 and ∂p^(2)=2a. A two-factor coefficient could first become visibly nonzero only with modulus p^{2a+1}, whereas a mod-p **unit** occurs first at four auxiliary factors. This explains why increasing the modulus and increasing auxiliary degree measure different invariants.

The same identities show that, when Sha[p∞] is finite, μ_p=2 does not merely say its p-corank vanishes; it says the entire p-primary group is trivial. No previous finiteness assumption is needed for (1)–(2).

## E. New consequence for actual E389a1: nonconstructive two-factor witnesses at known zero primes

The project's user-executed Sage 10.9 p_primary_bound(p)=0 certifies Sha[p∞]=0 at p∈{5,7,11,13,107}; an independent 2-Selmer proof handles p=2. For p=5,7,11,13,107 one independently computes

$$
\#E(\mathbf F_p)=9,\ 13,\ 16,\ 17,\ 108
$$

respectively, all coprime to p. Thus E(Q_p)[p]=0 for these primes.

**Consequently**, Theorem (1) proves \(\mu_p=2\) at each of these five p. The project has already explicit unit Kurihara witnesses for p=5,7,11 and a separately archived p=107 certificate; **at p=13 the existence of some two-prime mod13 Kurihara unit is now an unconditional-on-new-sums *nonconstructive theorem***, combining the Sage p-primary zero certificate with the two published theorems. This is not a newly calculated conductor or coefficient: one must still find q1,q2 and evaluate the sum if an explicit certificate is wanted.

For the studied p=16231 the project has a_p=128, giving #E(F_p)=16104 coprime to p. Thus Theorem (1) also applies, **but there is no presently established value of μ_16231=2** from the cited hypotheses alone. The substantial anticyclotomic theta order-two work is not an integral two-prime Kurihara unit certificate.

## F. Why this does not finish the uniform problem

The exact equality
$$
\mu_p-2=\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p]
$$
is a **fixed-p diagnostic, not an independent all-large-p upper bound**. The desired uniform statement μ_p=2 for all sufficiently large p is equivalent to Sha[p]=0 at those p under the stated published theorems, hence cannot be inferred solely from positive-density Kummer auxiliary pairs or the independent Hecke Smith determinant 2. Even a unit at some *unspecified* higher degree, guaranteed by Castella–Sano, does not control μ_p.

There is also a **separate** unclosed requirement for strong BSD: the exact complex identity between L''(E,1)/2, Néron period, regulator and Sha order. A rigorous positive interval for L''/2 establishes analytic rank 2 but not its exact leading-term relation.

**Verdict:** genuinely proved global-in-form, primewise exact degree-to-Sha[p]-dimension theorem and extension of scalar-Frobenius veto to every minimum-degree witness, plus the new nonconstructive p13 existence deduction. No uniform Sha finite-support proof or full BSD.
