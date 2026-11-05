# First genuine Gross-point right ideal P1^a from the conductor-one quaternionic base

**Date:** 2026-11-05. Source-level arithmetic construction and new independent lattice verification; code is published, **not yet user-run**.

## 1. Certified input from user Ubuntu Sage

From the 2026-11-05 genuine conductor-one CM base:
- K=Q(sqrt(-3)), O_K=Z[omega], omega²+omega+1=0.
- The unique Brandt maximal left order containing O_K has index 32 and weight 3, with certified omega basis coordinates (-1,153,-27,-64).
- The local split algebra chart at p=16231, modulo M=p²=263445361, is \`rho:R_32 tensor Z/M ≅ M2(Z/M)\`, with omega diagonal and a 4x4 basis-map determinant 389 (a p-adic unit).
- The actual user Sage JSON, not present in this GitHub checkout by default, is \`~/bsd389_p16231_conductor1_CM_base_and_local_split.json\`.
- The global base ideal I_32 is a right ideal of the common Brandt order R_0 with left order R_32.

The issue of old conductor 53 contamination is solved: this is a globally conductor-ONE optimal embedding.

## 2. Exact published Gross-point definition

Castella–Hsieh, *On the nonvanishing of generalized Kato classes for elliptic curves of rank 2*, Appendix, define

r_n(a)_p=[[1,a/p^n],[0,1]],   r_n(a)_ell=1 at ell !=p,

and P_n^a=(r_n(a) Rhat) intersect B, a fractional right ideal of the quaternionic base order. The scalar p^n does not change the adelic double class, so define the **integral** right ideal

J_n(a)=(p^n r_n(a) Rhat) intersect B.

At n=1, at the prime p,

rho(J_1(a))_p =
t(a) M2(Z_p),    t(a)=[[p,a],[0,p]].

At all other rational primes, J_1(a)_ell=R_ell since p is a unit there.

## 3. The two congruence theorem

For an integral quaternion x∈R_32 and X=rho(x)=[[X11,X12],[X21,X22]], the local lattice condition t(a)^(-1) X ∈ M2(Z_p) is equivalent to

p·X11 − a·X21 ≡ 0 mod p²,
p·X12 − a·X22 ≡ 0 mod p².

Indeed t^-1=[[1/p,-a/p²],[0,1/p]], so the top two entries have denominators p² and the bottom entries denominators p. Since a∈Z_p×, the top two congruences already force both bottom entries divisible by p; these are therefore both necessary and sufficient.

**Consequently** the global right ideal J_1(a) is the Z-lattice cut out from the integral order R_32 by exactly two congruences modulo p².

Writing x=Σ z_j b_j for an integral order basis and the known p² matrix images rho(b_j), form the explicit integer 2×4 congruence matrix D with rows
D_(0,j)=p*rho(b_j)_(1,1)−a*rho(b_j)_(2,1),
D_(1,j)=p*rho(b_j)_(1,2)−a*rho(b_j)_(2,2), modulo p².

The lattice of solution vectors z is the projection to the first four coordinates of the **integral** kernel of the 2×6 matrix [D | −p² I2]. This is a rank-4 lattice of exact index p^4 in Z^4. The index identity is also clear from determinant(t)=p², since left multiplication by t on 2×2 matrices has determinant (det t)^2 = p^4.

A second, **independent lattice reconstruction** pulls back the four explicit t(a)-multiples of matrix units E11,E12,E21,E22 through the inverse 4×4 order basis map modulo p², appends p² times each order basis vector, and takes the integral HNF of the resulting eight generators. Both constructions must yield the same rank-4 Z-lattice. This comparison is valuable for catching row/column, left/right and modular-index errors.

The code checks that the four reconstructed quaternion basis vectors are closed under right multiplication by all four integral order basis vectors, i.e. 16 exact rational quaternion membership tests. The constructed ideal has right order R_32.

## 4. Transport to the 33 Brandt classes

The local definition above is initially a right ideal of R_32, not of the common Brandt base order R_0. Multiply by the **actual** original right ideal I_32:

T_1(a) = J_1(a) * I_32.

As left-order(I_32)=R_32, the product T_1(a) is a right R_0-ideal. Its right-equivalence class among the existing Brandt representatives I_0,...,I_32 is precisely the Brandt class of P_1^a based at the fixed conductor-one CM point.

Both sides have to be kept consistent: for i=0, n=0, the identity local component gives back class I_32. Conjugating the p-adic local orientation can invert or permute labels but should not be silently ignored when inserting classes in the Castella–Hsieh theta formula.

The optional \`--classify\` flag tests equivalence against the 33 existing classes, potentially expensive for the p² norm ideal. Default first mode only constructs and certifies J_1(a), with no large class search.

## 5. Pilot command and source

Source: [verification/bsd389_p16231_conductor1_first_gross_P1_ideal_pilot.py](../verification/bsd389_p16231_conductor1_first_gross_P1_ideal_pilot.py).

\`\`\`bash
cd ~/bsd-389a1-p16231-computational-certificate
git pull --ff-only origin main
set -o pipefail
python -u verification/bsd389_p16231_conductor1_first_gross_P1_ideal_pilot.py --a 1 \
  2>&1 | tee ~/bsd389_p16231_first_P1_ideal_pilot.log
echo "P1_PILOT_STATUS=$?"
\`\`\`

Once base lattice passes, a separate **single-class** attempt can run the same script with \`--classify\` and an external timeout.

## 6. What remains

- This reconstructs an actual **P_1^a adelic right ideal** (up to the harmless global scalar p), not just a ring-class logarithm or a conductor-53 class.
- The second theta term \`P_2^a\` involves \`r_2(a)_p=[[1,a/p²],[0,1]]\`; the corresponding integer scalar is \`p²\`, and its local chart needs **mod p^4**, not p². The congruence formula generalizes to two equations \`p² X11−a X21 = p² X12−a X22=0 mod p^4\`, producing a lattice index p^8.
- The large theta computation also needs values for a running over the genuine Teichmuller group mu_(p−1) and p-power cyclotomic cosets; the pilot's a=1 is only one valid input.
- No theta order-two, generalized Kato nonvanishing, Selmer corank or Sha theorem follows from a single P1 ideal alone.

**Published source:** Castella–Hsieh appendix p. 26 https://web.math.ucsb.edu/~castella/Kato.pdf

**Sage right ideal API:** https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/quatalg/quaternion_algebra.html


## 4 bis. A genuine trivial-character theta simplification at n=0

For **every** p-adic unit a, the local matrix r_0(a)=[[1,a],[0,1]] belongs to GL2(Z_p), and it is the identity away from p. Consequently P_0^a=R_32 as a local-global right ideal, hence its Brandt right class (after multiplying by I_32) is identically **32**. The independently user-validated 33-coordinate Stage30 Hecke eigenvector satisfies v[32]=0. Therefore

phi_f(P_0^a)=v[32]=0 for EVERY a in Z_p^×.

This is a genuine direct consequence of the conductor-one base and the actual Brandt eigenvector, not an extrapolation from the conductor-53 finite toric period. It eliminates the alpha_p*phi_f(P_0^a) term in the theta formula at n=0. It does **not** determine the P_1^a term or the n=1 quadratic theta coefficient. The P1 pilot checks the frozen-v vector's baseline coordinate before any new ideal construction.
