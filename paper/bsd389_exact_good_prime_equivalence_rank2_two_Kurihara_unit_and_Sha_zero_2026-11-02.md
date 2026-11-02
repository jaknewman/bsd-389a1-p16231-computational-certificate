# Exact all-good-prime criterion: rank-two Kurihara unit witness ⇔ p-primary Sha triviality for E389a1

**Date:** November 2, 2026.

**What is new in this project:** a clearly isolated, logically exact equivalence specializing the **existing results** of Chan-Ho Kim (Theorem 1.8) and Castella–Sano (Theorem B). This is NOT a new proof of either theorem and does **not** show that the equivalent statements hold uniformly. It is the correct next mathematical target after the actual 710-chunk p107 archive reaggregation PASS.

## 1. Statement and explicit conditions

Let
\[
E:\; y^2+y=x^3+x^2-2x,\quad N=389,\quad \operatorname{rank}E(\mathbf Q)=2,
\]
with rational saturated MW generators \(P=(-1,1),Q=(0,-1)\), rational torsion order 1 and Tamagawa product 1. Let \(p\ge5\) be a prime **of good reduction**, i.e. \(p\ne389\), for which the mod-p representation is surjective and the optimal Manin constant is a p-unit.

For an admissible auxiliary prime \(q\nmid389p\), require
\(q\equiv1\bmod p,\ a_q(E)\equiv q+1\bmod p\); let
\(\widetilde\delta_{q_1q_2}\) be **the correctly p-integral, Néron-period-normalized two-prime Kurihara number** of Kim's §1.4, reduced modulo p.

### Theorem (precise criterion for each fixed good p)

Under the preceding arithmetic hypotheses:
\[
\boxed{
\Sha(E/\mathbf Q)[p^\infty]=0
\quad\Longleftrightarrow\quad
\exists\;q_1\ne q_2\text{ admissible}:
\widetilde\delta_{q_1q_2}\not\equiv0\pmod p.
}
\tag{1}
\]

This equivalence is **prime-by-prime**, not an existence theorem for all primes. It applies to the relevant good p for which the stated residual/Manin assumptions hold; the project has residual surjectivity for p5,7,107 and semistability/Mazur control for p≥11. The excluded bad prime p389 and small primes p2,3 require separate arguments and are not covered by (1).

A more general algebraic expression follows from the same sources: if the p-primary Selmer corank is 2, then
\[
\boxed{
\mathrm{Fitt}_{2,\mathbf Z_p}
(\mathrm{Sel}_{p^\infty}(E/\mathbf Q)^\vee)
=p^{\,\partial^{(2)}(\widetilde\delta)}\,\mathbf Z_p,
}
\tag{2}
\]
**because** Castella–Sano Theorem B gives \(\partial^{(\infty)}(\widetilde\delta)=v_p(\mathrm{Tam}_E)=0\). Importantly equation (2) requires corank EXACTLY 2, which is NOT proved merely by rankMW2 or by the existence of a Kurihara witness with arbitrarily many auxiliary factors. If the Selmer corank is >2, the 2nd Fitting ideal vanishes, and one must not apply (2).

## 2. Primary-source statements, checked

**Chan-Ho Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorem 1.8(1)–(3)**:
[author PDF](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf), printed page 7. For p≥5, residual GL2 surjectivity, p-unit Manin constant, and \(\mathrm{ord}(\widetilde\delta)<\infty\):
\[
\rho:=\mathrm{corank}_{\mathbf Z_p}\mathrm{Sel}_{p^\infty}
=\mathrm{ord}(\widetilde\delta),
\]
and for indices \(i\ge\rho\) of matching parity,
\[
\mathrm{Fitt}_{i,\mathbf Z_p}(\mathrm{Sel}_{p^\infty}^\vee)
=p^{\partial^{(i)}-\partial^{(\infty)}}\mathbf Z_p.
\]
The finite-length quotient of Selmer by its maximal divisible subgroup has length \(\partial^{(\rho)}-\partial^{(\infty)}\). Kim's **Theorem 1.10** gives an alternative mod-p semi-local proof when the two-prime unit witness is at the minimal auxiliary cardinality, subject to additional local p-torsion/Tamagawa conditions.

**Francesc Castella–Takamichi Sano, *On refined nonvanishing conjectures by Kurihara and Kolyvagin*, Theorem B**:
[author PDF](https://web.math.ucsb.edu/~castella/Kurihara.pdf), printed page 4. For p>3, surjective residual representation and p-unit optimal Manin constant:
- good ordinary p, or
- good supersingular p and squarefree conductor N,

the proven refined Kurihara equality is
\[
\partial^{(\infty)}(\widetilde\delta)
=v_p(\mathrm{Tam}_E).
\]
For 389a1, N=389 squarefree, \(\mathrm{Tam}_E=1\), hence for **every good p meeting those hypotheses**,
\[
\boxed{\partial^{(\infty)}(\widetilde\delta)=0.}
\tag{3}
\]
This guarantees a nonzero p-unit Kurihara number for SOME squarefree auxiliary n, with no restriction \(\nu(n)=2\). It does NOT by itself prove the desired (1) RHS.

## 3. Proof of the equivalence

### (RHS ⇒ LHS): a unit two-prime witness eliminates p-primary Sha

Suppose there is an admissible pair q1,q2 with \(\widetilde\delta_{q_1q_2}\not\equiv0\bmod p\). Then \(\rho=\mathrm{ord}(\widetilde\delta)\le2\) by Kim, because the collection is nontrivial. On the other hand, the Kummer embedding of rank-two MW forces \(\mathrm{corank}_{\mathbf Z_p}\mathrm{Sel}_{p^\infty}\ge2\), hence \(\rho\ge2\), so **\(\rho=2\)**. The unit witness also gives \(\partial^{(2)}=0\). By (3) \(\partial^{(\infty)}=0\), and Kim Theorem 1.8(3) shows that the quotient of Selmer by its maximal divisible subgroup is **zero**. Therefore
\[
\mathrm{Sel}_{p^\infty}\simeq(\mathbf Q_p/\mathbf Z_p)^{\oplus2}.
\]
The Kummer exact injection
\[
(\mathbf Q_p/\mathbf Z_p)^2\simeq
E(\mathbf Q)\otimes\mathbf Q_p/\mathbf Z_p
\hookrightarrow \mathrm{Sel}_{p^\infty}
\]
is an injection between two p-divisible groups of the same finite corank. Such an injection is an isomorphism (dualize to a surjection \(\mathbf Z_p^2\to\mathbf Z_p^2\) and use Nakayama), and hence \(\Sha(E/\mathbf Q)[p^\infty]=0\). This reasoning **does not assume Sha finiteness** in advance. Note: even the Castella–Sano theorem is logically unnecessary in this direction, since a two-prime *unit* witness already forces \(\partial^{(\infty)}=0\).

### (LHS ⇒ RHS): if p-primary Sha is trivial, there MUST be a unit two-prime witness

Assume \(\Sha[p^\infty]=0\). Then the Kummer exact sequence gives
\[
\mathrm{Sel}_{p^\infty}
=E(\mathbf Q)\otimes(\mathbf Q_p/\mathbf Z_p)
\simeq(\mathbf Q_p/\mathbf Z_p)^2,
\quad
X_p:=\mathrm{Sel}_{p^\infty}^\vee\simeq\mathbf Z_p^2,
\]
so \(\mathrm{Fitt}_{2,\mathbf Z_p}(X_p)=\mathbf Z_p\).

By the already-proved Castella–Sano equality (3), \(\partial^{(\infty)}=0\), so the Kurihara collection is nonzero. Kim Theorem 1.8(1) applies, giving \(\rho=\mathrm{ord}(\widetilde\delta)=\mathrm{corank}\mathrm{Sel}=2\). Apply Kim's *exact Fitting formula* at \(i=2\):
\[
\mathbf Z_p=\mathrm{Fitt}_2(X_p)
=p^{\,\partial^{(2)}-\partial^{(\infty)}}\mathbf Z_p
=p^{\,\partial^{(2)}}\mathbf Z_p.
\]
Thus \(\partial^{(2)}=0\). By its definition as the minimum p-divisibility among two-prime auxiliary Kurihara elements, **there exists an admissible product n=q1q2 whose mod-p coefficient is a unit**, proving the RHS. This direction uses both nontrivial theorems and is not inferred from the MW local Chebotarev result.

QED.

## 4. Why this is the correct global obstruction, not an easy tautological proof of Sha finite support

For every covered good p, the above exact theorem identifies the **nonzero two-prime unit witness** as the obstruction to p-primary Sha triviality. It does NOT supply that unit witness. The uniform statement
\[
\exists C\ne0\in\mathbf Z\quad
\forall p\nmid C:\ 
\exists(q_1,q_2)\;\widetilde\delta_{q_1q_2}\not\equiv0\bmod p
\]
is **equivalent**, under these hypotheses, to triviality of p-primary Sha for all but finitely many good p. It is **not** proved by knowing \(\partial^{(\infty)}=0\) because the latter allows the *first* nonvanishing auxiliary cardinality \(\rho\) to be 4,6,..., or allows \(\rho=2\) but all degree-two coefficients to be divisible by p.

The [uniform Kummer/Chebotarev MW-local theorem](bsd389_uniform_Chebotarev_Kummer_MW_local_two_auxiliary_wedge_2026-11-02.md) does give infinitely many primes q1,q2 detecting the rational wedge P∧Q locally for each large p, but that is **not** nonvanishing of the global Kato-derived Kurihara functional at those primes. The earlier p5 explicit rank39 mixed-distribution counterexamples prove exactly why the implication cannot follow from local rank and marginal data alone.

The previously authenticated **Hecke congruence Smith constant 2** controls only a fixed integral modular-symbol eigenline: it does not enter this Selmer \(\mathrm{Fitt}_2\) formula. Replacing the unknown \(\mathrm{Fitt}_2(X_p)\) with a Hecke Smith determinant would be mathematically incorrect.

## 5. Numerical anchors and exact p107 provenance

- p5, n=41·61: authentic direct user-evaluated two-prime \(\delta_5=4\bmod5\), published independent example in Kim (printed §8 Example 1), and user MW-local det 2. Thus \(\Sha[5^\infty]=0\) by the known Kim example.
- p7, n=113·673: historical \(\delta_7=2\bmod7\), MW-local det 3; the global δ is **not re-run in this note**.
- p107, n=369793·383917: actual user frozen 710-payload reaggregation **PASS**. **All 710 archived block canonical hashes and M390 dot products** and full contiguous coverage of 70,984,909,590 numerators checked; half=17, \(\widetilde\delta=34\bmod107\). User report SHA256 `439bd3aa0bc8c861dfad63ac7b1ece48a3c5faabf28308d7c2e3fa62a06f8e62`; full authentic output [here](../results/bsd389_p107_frozen_tar_710_internal_reaggregate_USER_PASS_2026-11-02.md), plus independently authenticated p107 MW-local det38. These checks reconstruct **the stored 710 output blocks**, and do NOT re-execute the original massive native loop. Thus the p107 Kim/Sha conclusion remains **a computer-assisted theorem conditional on correctness of the original Manin/C++ routine and p-integral symbol normalization**.

## 6. Next genuine proof obligation

Find an **arithmetic mechanism independent of the desired Sha conclusion** controlling the **degree-two** Kurihara leading coefficient for all sufficiently large good primes p, e.g. an integral global Euler/Kolyvagin regulator identity with a single fixed nonzero rational or integer determinant whose p-unit reduction forces existence of a *two-prime* Kurihara unit. Merely invoking nonvanishing with unrestricted number of auxiliary primes (Castella–Sano), the all-p local MW wedge, or all-odd-p integral Hecke eigensymbol rigidity does NOT provide it.

The separate exact complex strong BSD leading-term equality is not deduced even by proving this uniform p-primary statement.
