# 389a1 — exact local Selmer/Fitting rank shift: the Kato index-ONE ideal is enough

**24 November 2026. Status:** Proven integral algebraic theorem and a conditional application to BSS. This is a real simplification of the uniform Sha-finiteness proof cut, **not** a new certificate of the missing uniform Kato primitivity. No numerical experiments are required.

## 1. Honest local condition: a one-dimensional p-adic Lie group

Let E/Q be 389a1 with E(Q)=Z P+Z Q (rank 2 and zero torsion), p any prime and A=E[p^\infty]. Set
\[
S_f=\operatorname{Sel}_{p^\infty}(E/\mathbf Q),\qquad
H_f^1(\mathbf Q_p,A)=E(\mathbf Q_p)\otimes\mathbf Q_p/\mathbf Z_p.
\]
The local elliptic Lie group has Z_p-corank one, so
\[
H_f^1(\mathbf Q_p,A)\simeq\mathbf Q_p/\mathbf Z_p.
\]

A rational non-torsion point P is non-torsion in E(Q_p); its local p-adic Lie logarithm is therefore nonzero. The map from the rank-two Mordell–Weil divisible subgroup
\[
(\mathbf Q_p/\mathbf Z_p)^2\subset S_f
\]
onto the local Kummer group is a nonzero Z_p-linear map to Q_p/Z_p. Every nonzero such map is surjective: multiplication by any nonzero a in Z_p on Q_p/Z_p is surjective.

Thus the localization of **the full Selmer group** onto the finite local Kummer group is actually surjective. Defining
\[
S_0:=\ker(S_f\to H_f^1(\mathbf Q_p,A)),
\quad X_f=S_f^\vee,\quad X_0=S_0^\vee,
\]
Pontryagin duality gives a CANONICAL exact sequence
\[
\boxed{0\to\mathbf Z_p\xrightarrow{j_p}X_f\to X_0\to0.}
\]

## 2. Integral rank-shift theorem (does NOT assume Sha finite)

From the Kummer sequence and projectivity of Z_p²:
\[
X_f\simeq\mathbf Z_p^2\oplus Y_p,\quad
Y_p=\Sha(E/\mathbf Q)[p^\infty]^\vee.
\]
The module Y_p is finitely generated over Z_p and may have nonzero free rank (we do NOT assume Sha finiteness).

Let (a_p,b_p) be the image of \(j_p(1)\) in the canonical MW quotient \(X_f\twoheadrightarrow\mathbf Z_p^2\). This vector is nonzero. Define the integral localization index
\[
\mathfrak l_p=(a_p,b_p)=p^{t_p}\mathbf Z_p,\quad t_p\ge0.
\]
It is well-defined up to units and does not require choosing a global splitting X_f≅Z_p²⊕Y_p.

**THEOREM.** As *actual integral ideals* of Z_p,
\[
\boxed{
\operatorname{Fitt}_{1,\mathbf Z_p}(X_0)
=
\mathfrak l_p\,\operatorname{Fitt}_{2,\mathbf Z_p}(X_f).
}
\]
Therefore
\[
\boxed{\operatorname{Fitt}_1(X_0)\subseteq\operatorname{Fitt}_2(X_f).}
\]
This requires **no saturation assumption**, no Sha finiteness and no BSD.

### Proof

If Y_p has positive free rank δ>0, then X_f has rank ≥3, so Fitt₂(X_f)=0. The exact sequence reduces rank by one, leaving X_0 of rank ≥2, so Fitt₁(X_0)=0. Thus both sides vanish.

Assume Y_p is finite of length e. Choose a Z_p basis of the free MW quotient to put the nonzero vector (a_p,b_p) into Smith form (p^{t_p},0), up to a unit. Splitting X_f=Z_p²⊕Y_p, write the generator of the image j_p as
\[
(p^{t_p},0,y_0)\in\mathbf Z_p\oplus\mathbf Z_p\oplus Y_p.
\]
Then
\[
X_0\simeq\mathbf Z_p\oplus C,\quad
C=(\mathbf Z_p\oplus Y_p)/\langle(p^{t_p},y_0)\rangle.
\]
There is an exact sequence
\[
0\to Y_p\to C\to\mathbf Z_p/p^{t_p}\to0
\]
(including the case t_p=0, when the right term is zero). Therefore C is finite of length \(e+t_p\). A finite module over a DVR has zeroth Fitting ideal equal to its order ideal; hence
\[
\operatorname{Fitt}_1(X_0)=\operatorname{Fitt}_0(C)
=(p^{e+t_p}),
\qquad
\operatorname{Fitt}_2(X_f)=\operatorname{Fitt}_0(Y_p)=(p^e).
\]
This proves the claimed equality.

If t_p>0, the inclusion is strict whenever Fitt₂(X_f) is nonzero. This is why local saturation **would be required for equality without a correction**, but **is not required at all for the useful one-way inclusion**. QED.

## 3. Important consequence for existing Euler-system machinery: use I_1, not I_2

Burns–Sakamoto–Sano, *On the theory of higher rank Euler, Kolyvagin and Stark systems, II*, Corollary 6.21(ii), states that under its hypotheses an Euler system c of its valid Euler rank r yields a Kolyvagin system κ(c), with
\[
I_i(\kappa(c))\subseteq
\operatorname{Fitt}_i\!\left(
H^1_{\mathcal F_{\rm can}^*}(\mathbf Q,T^\vee(1))^\vee
\right)\quad(i\ge0).
\]
Their *Euler rank* for T_pE over Q is r=1, because the archimedean (+)-invariant module has Z_p rank1. Their index i can nevertheless be any nonnegative integer.

At the prime p the canonical local condition on T is full H¹ (BSS §6.2), so its dual on \(A=E[p^\infty]\) is strict (zero). For E389a1, at primes q≠p, the ordinary Kummer conditions and the BSS canonical-dual conditions must be compared exactly; the only bad prime is 389, with Tamagawa number1, which is favorable but the equality and all BSS hypotheses must still be checked, especially p=389.

**If** this local-structure comparison identifies the target BSS strict module with X_0 above, the theorem of §2 yields
\[
\boxed{I_1(\kappa_{\rm Kato,p})
\subseteq\operatorname{Fitt}_1(X_0)
\subseteq\operatorname{Fitt}_2(X_f)
=\operatorname{Fitt}_0(Y_p).}
\]

**This is the correct index:** the previously proposed \(I_2\subseteq\operatorname{Fitt}_2(X_0)\) does not generally control \(\operatorname{Fitt}_2(X_f)\). Because the localization eliminates **one free rank**, the useful strict Fitting index is **one**, not two.

### Precise consequences IF the BSS hypotheses and identification have been checked

- Any **nonzero** element of genuine \(I_1(\kappa_{\rm Kato,p})\) forces \(Y_p\) finite, hence Sha(E/Q)[p^\infty] finite (possibly nontrivial).
- If this ideal contains a p-adic **unit**, then \(\operatorname{Fitt}_2(X_f)=\mathbf Z_p\), so Sha(E/Q)[p^\infty]=0.
- If for every sufficiently large p the ideal contains a p-unit, and all excluded small primes have independently certified Sha-vanishing, then Sha(E/Q)=0 globally.
- If a **single nonzero integer D**, independent of p, can be shown to lie in the genuine I1(κ_Kato,p) (or in the corresponding strict Fitting ideal) for all p outside a finite explicitly checked set, then \(D\mathbf Z_p\subseteq\operatorname{Fitt}_2(X_f)\) for all those p. The finite exceptional cases must be dealt with separately. In particular, D whose prime support is entirely among already-certified Sha-zero primes would suffice.

None of these statements asserts that such **uniform nonvanishing of I1** has been proved. The Burns–Sakamoto–Sano inclusion is one-sided; it does NOT guarantee that the particular Kato Euler system yields a primitive Kolyvagin system, nor that I1 is nonzero.

## 4. A clean falsification test for a wrong index or wrong local identification

Take \(O=\mathbf Z_p\), \(Y=(O/p)^2\), \(X_f=O^2\oplus Y\), and j_p(1)=(1,0,0). Then
\[
X_0=O\oplus (O/p)^2,\quad
\operatorname{Fitt}_1(X_0)=(p^2)=\operatorname{Fitt}_2(X_f),
\]
but \(\operatorname{Fitt}_2(X_0)=(p)\). Thus using I2(strict) only controls a **weaker** ideal and in general is insufficient to bound the true Sha order. When j_p(1)=(p^t,0,0), t>0, the strict Fitting ideal becomes (p^{e+t}), a strict subideal of (p^e); this is exactly compatible with the useful inclusion.

## 5. Research verdict (no computation needed yet)

We have **proved** the formerly missing strict-to-usual integral Fitting **inclusion**, including its precise localization-index correction. A formerly posited 'saturation prerequisite' is NOT a prerequisite for a Sha order bound. We have also identified the right **Kato-derived higher-Fitting index I1**.

Two genuine outstanding arithmetic steps:
1. Verify every BSS Corollary 6.21 hypothesis for T_pE and identify its exact Selmer target with the strict p-local Kummer Selmer group, including bad-prime conditions, for all sufficiently large p. In particular the source may require auxiliary \(\Sigma\)-modified cohomology; don't assume this step is automatic.
2. Prove a nonzero/primitive \(I_1(\kappa_{\rm Kato,p})\) at all large p, or construct one integral D uniformly represented. The source does not promise this primitivity. Such a statement is as strong as the missing global p-support theorem and cannot be generated by formal Fitting identities alone.

The separate original **exact complex BSD leading-term equality** still demands an independent analytic/arithmetic normalization theorem. This note solely sharpens the *global Sha* route.

**References**
- BSS II, §6.2 and Corollary 6.21(ii): https://nms.kcl.ac.uk/david.burns/web_page/bss.pdf
- Kummer exact sequence and local conditions: standard arithmetic duality and Bloch–Kato Selmer theory.
