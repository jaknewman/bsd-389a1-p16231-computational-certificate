# GLOBAL all-prime visibility theorem for 389a1: EVERY Sha class is invisible at level 389, and Sha(E) embeds in Sha(J0(389))

Date: 2026-11-06. No previous p-local computation was rerun. This is an exact, **all-rational-prime** cohomological theorem derived from the fixed degree-40 modular parametrisation and **previously authenticated** 2- and 5-primary Sha vanishing certificates. It does **not** imply Sha(E) finite or zero.

## Input: fixed, integral modular map

E/Q = 389a1, J=J0(389). Let φ:X0(389)→E denote the optimal parametrization of exact degree 40, and β=φ*:E→J, α=φ*:J→E its dual (pushforward), with αβ=[40]_E. By optimality α has connected kernel and β is a closed immersion.

Let B=J/β(E) and π:J→B, so there is a short exact sequence of abelian varieties over Q
\[
0\to E\xrightarrow{\beta}J\xrightarrow{\pi}B\to0.
\]

The **visible subgroup in the standard kernel definition** is
\[
\mathrm{Vis}_J\Sha(E):=\ker(\Sha(E/\mathbf Q)\xrightarrow{\beta_*}\Sha(J/\mathbf Q)).
\]

## Theorem 1: modular degree 40 annihilates ALL visible Sha classes, without finiteness

For every ξ∈H¹(Q,E), functoriality of H¹ and αβ=[40] imply
\[
\alpha_*\beta_*(\xi)=[40]\xi.
\]
If β_*(ξ)=0 then [40]ξ=0. Hence
\[
\boxed{40\cdot\mathrm{Vis}_J\Sha(E)=0.}
\]
In particular
\[
\boxed{\mathrm{Vis}_J\Sha(E)[p^\infty]=0\quad\text{for every }p\ne2,5.}
\]
This is a **single universal proof**, not a run through primes. It is precisely Mazur's classical modular-degree obstruction to Sha visibility. It does NOT say that Sha(E)[p∞]=0 for p≠2,5: such classes could instead be nonvisible and inject into Sha(J)[p∞].

## Theorem 2: explicit finite Mordell–Weil quotient for the visible part

The long exact sequence of Galois cohomology gives
\[
B(\mathbf Q)\xrightarrow{\delta}H¹(\mathbf Q,E)\xrightarrow{\beta_*}H¹(\mathbf Q,J)
\]
with
\[
\mathrm{im}(\delta)\simeq B(\mathbf Q)/\pi J(\mathbf Q).
\]
Impose everywhere local triviality by defining
\[
B(\mathbf Q)_{\mathrm{loc}}:=\{b\in B(\mathbf Q):
  b\in\pi(J(\mathbf Q_v))\ \text{for all places }v\}.
\]
Then EXACTLY
\[
\boxed{\mathrm{Vis}_J\Sha(E)\simeq
  B(\mathbf Q)_{\mathrm{loc}}/\pi J(\mathbf Q).}
\]

Moreover
\[
\boxed{[40]B(\mathbf Q)\subseteq\pi J(\mathbf Q).}
\]
To prove this, the global endomorphism \(40_J-\beta\alpha:J\to J\) annihilates β(E), hence factors through B via \(\gamma:B\to J\). Since πβ=0, its composite satisfies
\(\pi\gamma\pi=[40]\pi\). Surjectivity of π gives πγ=[40]_B. Thus for every b∈B(Q), [40]b=πγ(b) belongs to πJ(Q).

Therefore the visible Sha subgroup embeds into a quotient of the **single finite group**
\[
B(\mathbf Q)/40B(\mathbf Q)
\simeq(\mathbf Z/40)^{r_B}\oplus B(\mathbf Q)_{\mathrm{tors}}/
40 B(\mathbf Q)_{\mathrm{tors}},
\]
where \(r_B=\mathrm{rank} B(\mathbf Q)\) is finite by Mordell–Weil. Explicitly
\[
\boxed{\#\mathrm{Vis}_J\Sha(E)\le
40^{r_B}\#B(\mathbf Q)[40]\le40^{r_B+62},}
\]
since \(\dim B=31\) and \(B(\overline{\mathbf Q})[40]\) has order \(40^{2\cdot31}=40^{62}\). The rank r_B is NOT evaluated here, so the last displayed bound is a fixed finite expression, not an asserted fully numeric numerical certificate. This strengthens the exponent statement to an actual finite group bound for the visible part without assuming whole Sha finite.

## Theorem 3: for THIS curve, the entire visible subgroup vanishes at ALL primes

The research archive's **original Sage+PARI+mwrank 2-Selmer user output** provides
\[
\Sha(E/\mathbf Q)[2^\infty]=0
\]
with rankMW=2, torsion1, and Sel_2 F₂-dimension2. See \`results/full_BSD_sha_2_primary_TRIVIAL_PASS_2026-10-19.md\`.

Separately the authenticated Sage 10.9 p-primary bounds e_p=0 for p=5, and the published independent two-prime Kurihara computation of Kim for **this same E389a1**, prove
\[
\Sha(E/\mathbf Q)[5^\infty]=0.
\]
See \`results/full_BSD_sha_5_7_11_13_primary_TRIVIAL_PASS_2026-10-19.md\` and the citations in STATUS.md.

Every class in Vis_J Sha(E) is killed by 40=2³·5 by Theorem 1. But Sha(E)[40]=0 by these two independently certified 2- and 5-primary gates. Consequently
\[
\boxed{\mathrm{Vis}_{J_0(389)}\Sha(E)=0,\quad
\Sha(E/\mathbf Q)\xhookrightarrow{\ \beta_*\ }
\Sha(J_0(389)/\mathbf Q).}\tag{GLOBAL}
\]
The injection holds for the FULL group, including any hypothetical divisible subgroup; no finiteness of Sha(E) or Sha(J) is assumed.

**This is an exact uniform all-prime application of a known visibility theorem**, not a new theorem about finite support of Sha(E).

## Correct global interpretation: a precise obstruction, not the missing Sha bound

This global injection has a useful negative lesson: a proof seeking to bound Sha(E) merely by detecting classes **that become zero in Sha(J0(389))** can never detect any nonzero class for this E, because the visible kernel is already proven zero. A genuinely new method must bound its **image** in Sha(J), and the modular projector does not do that. In particular the claim “modular degree 40 kills Sha(E)” is FALSE: 40 only kills the visibility kernel.

Also, even if one subsequently proves Sha(J) finite by an independent global theorem, the injection implies finiteness of Sha(E), but it does not furnish the exact COMPLEX rank-two L''/period/regulator identity. Proving finite Sha(J) without circular use of the E factor remains itself a difficult higher-rank theorem.

The companion Faltings–Hriljac determinant expresses Reg(E) via two modular divisors and is separately unconditional; it gives no bridge from this visibility injection to L''(E,1)/2.

No E389a1 BSD full proof is claimed.

## Literature

- Mazur's visibility theorem, including the modular degree annihilating the visible subgroup: classical description in Agashe–Stein, *Visibility of Shafarevich–Tate Groups of Abelian Varieties*, Journal of Number Theory 97 (2002), 171–185; https://www.sciencedirect.com/science/article/pii/S0022314X02928106 .
- Mazur's discussion and exact B(Q)_loc / πJ(Q) formula, cited in standard visibility literature.
- Jetchev–Stein, *Visibility of Shafarevich–Tate Groups of Abelian Varieties at Higher Level*: https://wstein.org/papers/works/works.pdf (visibility limitations and possible higher-level embeddings).
- Archived optimal degree-40 projector proof in PR #12 and audited earlier Sha2/Sha5 primary certificates.
