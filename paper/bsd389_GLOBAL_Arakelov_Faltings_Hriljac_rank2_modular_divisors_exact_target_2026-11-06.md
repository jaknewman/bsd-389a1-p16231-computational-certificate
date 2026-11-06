# GLOBAL BSD 389a1 as ONE arithmetic-intersection identity on the regular modular surface X_0(389)

Date: 2026-11-06. Exact, **prime-independent** geometric height construction using the proven Faltings–Hriljac theorem and the fixed degree-40 modular parametrization. This supplies a concrete arithmetic-surface right-hand side for rank-two BSD; **the equality with the second complex L-derivative remains unproved**.

## Fixed explicit divisors (no ad hoc p-adic normalisation)

Let E=389a1, P=(-1,1) and Q=(0,-1) the full Mordell–Weil basis, X=X_0(389), and φ:X→E the optimal degree-40 parametrization taking ∞ to O. Define degree-zero Q-rational divisors
\[
D_P:=\phi^*([P]-[O]),\qquad
D_Q:=\phi^*([Q]-[O])
\]
on X. Each is a difference of two Q-rational effective **degree-40** divisors. In J=Pic^0(X), they represent φ^*(P) and φ^*(Q) as points of J(Q).

Take a regular proper arithmetic model \(\mathcal X/\mathbf Z\) of X (a regular desingularization of the integral modular curve). Choose admissible arithmetic extensions of the degree-zero divisors with vertical corrections making their intersection with vertical components degree zero and the canonical admissible Arakelov Green metrics at the archimedean place.

The following EXACT theorem is the starting point, not a conjecture:

Faltings–Hriljac (with the conventions of Holmes–Müller / Holmes, Theorem 4.1) states that if \([D]\) and \([E]\) lie in J(Q), the local Néron pairings of disjoint divisor representatives satisfy
\[
\boxed{\hat h_{2\Theta_J}([D],[E])
=-\sum_{v\in M_{\mathbf Q}}\langle D,E\rangle_v,}\tag{FH}
\]
where \(2\Theta_J\) is twice the principal symmetric theta polarisation. Define the half-normalized bilinear arithmetic intersection
\[
\boxed{\mathcal I(D,E)
:=-\tfrac12\sum_v\langle D,E\rangle_v
=\langle[D],[E]\rangle_{\mathrm{NT},\Theta_J}.}\tag{1}
\]
The factor 1/2 is IMPORTANT: using the height associated to \(2\Theta_J\) directly would introduce a factor 4 in our rank-two determinant. Our convention is the usual degree-one principal polarisation, matching the standard elliptic canonical height. Other standard height conventions can be converted systematically but must not be mixed.

## Theorem 1 (exact arithmetic intersection determinant = 1600 times the original regulator)

The optimal modular map has \(\deg\phi=40\) and the functorial homomorphisms α=φ_*:J→E and β=φ^*:E→J obey αβ=[40] on E. The duality/adjunction of the Jacobian principal polarisations gives for every R,S∈E(Q)
\[
\langle\beta R,\beta S\rangle_{\mathrm{NT},\Theta_J}
=\langle R,\alpha\beta S\rangle_{\mathrm{NT},\Theta_E}
=40\langle R,S\rangle_{\mathrm{NT},E}.
\]
Applying (1), the completely specified fixed arithmetic intersections satisfy
\[
\boxed{
\mathcal I(D_P,D_P)=40\hat h_E(P),\quad
\mathcal I(D_P,D_Q)=40\langle P,Q\rangle_E,\quad
\mathcal I(D_Q,D_Q)=40\hat h_E(Q).
}\tag{2}
\]
Their determinant is EXACTLY
\[
\boxed{
\mathcal I(D_P,D_P)\mathcal I(D_Q,D_Q)
-\mathcal I(D_P,D_Q)^2
=1600\,\operatorname{Reg}(E).
}\tag{3}
\]

This theorem is unconditional given the proven degree 40 and the standard Faltings–Hriljac and height functoriality theorems. It is **not numerical**, makes NO BSD assumption, and uses two explicit integral divisor families on a SINGLE arithmetic surface.

## The exact global complex leading coefficient, and the SINGLE unproved equality

The rigorous Mellin–Fricke theorem in the companion paper has already given
\[
\frac{L''(E,1)}2=
2\pi\sum_{n\ge1}a_n\int_{1/\sqrt{389}}^\infty
e^{-2\pi nt}\log^2(t\sqrt{389})\,dt,
\]
with an explicit exponentially decreasing truncation bound.

The full real Néron period Ω_E is independently an exact complete elliptic integral. Since torsion and Tamagawa product for E are 1, strong BSD with conjectural Sha=1 would be the following *SINGLE concrete equality of global analytic and arithmetic geometric objects*:
\[
\boxed{
2\pi\sum_{n\ge1}a_n\int_{1/\sqrt{389}}^\infty
e^{-2\pi nt}\log^2(t\sqrt{389})\,dt
\overset{?}{=}
\frac{\Omega_E}{1600}
\bigl(\mathcal I(D_P,D_P)\mathcal I(D_Q,D_Q)
-\mathcal I(D_P,D_Q)^2\bigr).
}\tag{4}
\]

**The equality marked (?) is NOT proved.** Equations (1)-(3) prove the exact right-hand-side normalization. Mellin–Fricke proves the left-hand side. Their numerical proximity does not prove equality. The missing mathematical theorem is a genuine **SECOND-complex-derivative arithmetic-height formula** for the particular pair of degree-40 modular divisors D_P,D_Q, not a first-derivative Gross–Zagier theorem or a cyclotomic p-adic height formula.

One route to attack (4) is to identify the modular arithmetic divisor pairing or its exterior determinant in the coefficient of a *double derived automorphic theta/Rankin kernel*. But constructing that kernel and proving its arithmetic intersection comparison is a new theorem obligation. The ordinary arithmetic theta lifting currently cited in the Gross–Zagier literature gives first derivatives, not (4) in rank two.

## Precise separation from Sha finiteness

A proof of (4) (with predicted Sha=1) does **NOT** by itself prove \(\Sha(E/Q)=0\) as an abstract group; an independent ALL-PRIME control theorem is still required. Conversely, an independent all-prime vanishing proof for Sha does NOT imply (4) without an analytic height identity. These are genuinely separate requirements, now both located on the fixed modular factor selected by the global 40-degree correspondence.

The previously proved p-uniform Selmer splitting via e_E=(β α)/40 works integrally at every p except 2,5, but it gives no uniform annihilator of Sha. Do NOT infer finite Sha support from the arithmetic surface having a fixed finite set of vertical intersection primes: the global Selmer obstruction is not measured by those vertical intersections without an independently proved Euler/ETNC comparison.

## Primary sources

- Faltings–Hriljac as formulated with \(2\Theta\) and local intersections: David Holmes and collaborators, *Explicit arithmetic intersection theory*, Theorem 4.1, https://pure.rug.nl/ws/portalfiles/portal/226926877/S0025_5718_2019_03441_5.pdf .
- General Faltings–Hriljac arithmetic self-intersection formula: Ulf Kühn, *On an upper bound for the arithmetic self-intersection*, Theorem 1.8, https://recercat.cat/bitstream/handle/2072/1396/Pr656.pdf?sequence=1 .
- Sage verification of degree 40: https://more-sagemath-tutorials.readthedocs.io/en/latest/demo-number-theory.html .
- Companion fixed modular correspondence and p-uniform Selmer decomposition manuscript in this PR.
