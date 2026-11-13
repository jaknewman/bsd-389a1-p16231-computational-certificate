# E389a1: auxiliary-field Sha exponent bounds from norm–theta descent

**Date: 2026-11-13.** **Status: CONDITIONAL on the two reported 2026-11-13 auxiliary norm–theta annihilation inclusions.** These inclusions have not yet been independently reproduced or frozen in this repository. The formal deductions below are proved; neither global finiteness of Sha over Q nor complex BSD is claimed.

## 1. Independent base-field input

Let

$$
E/\mathbf Q : y^2+y=x^3+x^2-2x,\qquad N=389.
$$

The genuine Sage 10.9 run recorded in [the project's results](../results/bsd389_sha_iwasawa_5_7_11_13_107_USER_PASS_2026-11-02.md) reports the provable bounds

$$
\operatorname{Sha}(E/\mathbf Q)[5^\infty]
=\operatorname{Sha}(E/\mathbf Q)[7^\infty]=0.\tag{1}
$$

Sage's documented p_primary_bound method gives a *provable* bound, also in rank > 1: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/sha_tate.html. Independently, Kim §8 example (1) obtains 5-primary triviality using the Kurihara witness at 41·61: https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf.

## 2. General norm–descent lemma (proof)

Let K/F be finite Galois with group G. Fix a prime p and put

$$
A=\operatorname{Sha}(E/K)[p^\infty],\quad
B=\operatorname{Sha}(E/F)[p^\infty].
$$

Restriction and corestriction $r:B\to A$, $c:A\to B$ satisfy

$$
N_G:=\sum_{g\in G}g=r\circ c\qquad\text{on }A.\tag{2}
$$

**Lemma.** If some $\Theta\in\mathbf Z_p[G]$ annihilates all of A and

$$
p^m\cdot1\in(\Theta,N_G)\subseteq\mathbf Z_p[G],\tag{3}
$$

then

$$
p^mA\subseteq r(B),\qquad p^m\ker(c)=0.\tag{4}
$$

**Proof.** Write $p^m=U\Theta+VN_G$, with $U,V\in\mathbf Z_p[G]$. For $a\in A$,

$$
p^m a=V N_G a=V\,r(c(a))=r(\varepsilon(V)c(a)),
$$

since $r(B)$ is G-invariant and $\varepsilon$ is the augmentation. If $c(a)=0$, this expression is zero. QED.

**Corollary.** Even without (3), the inclusion $p^m A\subseteq r(B)$ and $p^s B=0$ imply $p^{m+s}A=0$. In particular $B=0$ gives $p^m A=0$. Moreover, $A$ is finite because it equals its $p^{m+s}$-torsion subgroup, which is finite by descent (the finite-level Selmer group).

## 3. Applications to the two auxiliary fields

The most recent previous conversation reported the following arithmetic inputs:

$$
25\operatorname{Sha}(E/K'_5)[5^\infty]
\subseteq r\operatorname{Sha}(E/\mathbf Q)[5^\infty], \tag{H5}
$$

with auxiliary conductor $131\cdot251=32881$, and

$$
49\operatorname{Sha}(E/K_7)[7^\infty]
\subseteq r\operatorname{Sha}(E/\mathbf Q)[7^\infty]. \tag{H7}
$$

It also reported $49\in(\Theta_{K_7},N_G)$ and
$(\Theta_{K'_5},N_G)\cap\mathbf Z_5=25\mathbf Z_5$.
The exact extension definitions, ideal witnesses, and the required theta-annihilation hypotheses are **not independently re-proved in this note**.

**Conditional theorem.** Assuming H5 and H7 as valid inclusions for the stated Tate–Shafarevich modules, equation (1) yields

$$
\boxed{
25\operatorname{Sha}(E/K'_5)[5^\infty]=0,\qquad
49\operatorname{Sha}(E/K_7)[7^\infty]=0.
}\tag{5}
$$

Both groups are finite by the corollary. The perfect alternating Cassels–Tate pairing on each finite odd-primary Sha forces paired elementary divisors, hence

$$
\operatorname{Sha}(E/K'_5)[5^\infty]
\simeq(\mathbf Z/5)^{2a}\oplus(\mathbf Z/25)^{2b},
$$

$$
\operatorname{Sha}(E/K_7)[7^\infty]
\simeq(\mathbf Z/7)^{2c}\oplus(\mathbf Z/49)^{2d}
\quad(a,b,c,d\geq0).
$$

This proves possible structures only, not that any of $a,b,c,d$ is zero.

## 4. Strict boundary and open proof obligations

Neither the norm–theta relation nor the auxiliary exponent bound gives a new bound on Sha(E/Q). The vanishing in (1) was **independent input**. In addition, two fixed-prime arguments cannot yield the needed all-large-p finite-support theorem or the complex BSD leading-term identity.

Before this conditional theorem can be presented as a fully certified application, the project must:

1. State the exact fields $K'_5$, $K_7$, their Galois groups and norm maps.
2. Exhibit machine-checkable exact group-ring ideal identities at 25 and 49.
3. Prove that each theta annihilates the **full required Sha module**, or directly prove H5/H7 from arithmetic (an ideal-membership calculation alone does not prove this).
4. Freeze and audit those proofs independently.

For the global BSD goal, the missing step remains p-uniform degree-two Kurihara/Euler–Kolyvagin to Selmer control, as isolated in [the existing exact criterion](bsd389_exact_good_prime_equivalence_rank2_two_Kurihara_unit_and_Sha_zero_2026-11-02.md), and separately the exact complex leading term.

**Verdict:** A genuine formal strengthening of the reported auxiliary descents, with the still-uncertified arithmetic hypotheses explicitly visible. Not full BSD.