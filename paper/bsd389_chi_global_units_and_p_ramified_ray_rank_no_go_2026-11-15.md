# E389a1: the χ-unit rank is exactly (p+1)/2, forcing ≥(p+1)/2 free p-ramified ray-class directions at supersingular p

**15 November 2026.** This is a genuine, mathematically proved NEW CHARACTER-BY-CHARACTER arithmetic structure theorem for the actual Borel character field L_p/Q associated with E389a1. It is explicitly **a NO-GO for a proposed ray-class dimensional upper bound** and a better mathematical isolation of the genuinely finite ordinary p-class-group excess. **It DOES NOT prove rχ,p≤2, Sha[p]=0 for a new prime, the all-large-p Sha bound or complete rank-two BSD.**

## 1. Genuine curve/fields and signatures

Use the curve E/Q: y²+y=x³+x²−2x, with conductor and discriminant +389. Fix a good rational prime p≥5 with full residual GL2(Fp) image. Let V=E[p], F=Q(E[p]), C⊂V a line, B=Stab_GL2(C), W=V/C, and χ:B→Fp× the action on W (the **DUAL** p-isogeny kernel). Define

  K=F^B,     L=F^(ker χ),     Δ=Gal(L/K)=Fp×.

Then [K:Q]=p+1 and [L:Q]=p²−1, and Δ is **cyclic of order p−1**, prime to p. Its tautological χ takes −1∈Δ to −1∈Fp×, so χ is ODD.

Complex conjugation c∈GL2(Fp) has eigenvalues +1 and −1. It fixes exactly TWO projective lines, and exactly p−1 nonzero covectors on the dual V∨. Thus the signatures are

  **signature(K)=(2,(p−1)/2),**
  **signature(L)=(p−1,p(p−1)/2).**

The two real places of K arise from fixed lines C^+ and C^−. With W=V/C, χ(c) is −1 at C^+ and +1 at C^−. Consequently:
- above ONE real place of K, the p−1 places of L are real, and Δ acts REGULARLY;
- above the other real place, the (p−1)/2 places of L are complex pairs and Δ acts as Δ/{±1};
- above EACH of the (p−1)/2 complex places of K, Δ permutes the p−1 complex places of L REGULARLY.

This completely determines the Δ-permutation representation on L's archimedean places.

## 2. THEOREM A — exact Dirichlet χ-unit rank

Let U_L=O_L×, and eχ=(1/(p−1))Σ_{σ∈Δ} χ(σ)^(−1)σ ∈Z_p[Δ], where χ is lifted via Teichmüller. The equivariant Dirichlet logarithm theorem identifies U_L⊗R with the archimedean permutation representation minus its one-dimensional trivial diagonal. Hence, as virtual representations,

  U_L⊗C = [(p+1)/2] C[Δ] ⊕ C[Δ/{±1}] − 1.

The quotient representation C[Δ/{±1}] contains precisely those 1D characters ψ with ψ(−1)=+1. The trivial subtraction affects ONLY ψ=1. Therefore for EVERY good p≥5 with full GL2,

  **rank_Zp eχ(U_L⊗Zp)=(p+1)/2**   (χ is odd);

more generally, ψ=1 has unit rank (p+1)/2; nontrivial ψ even has (p+3)/2; nontrivial ψ odd has (p+1)/2. Their sum equals the ordinary Dirichlet unit rank

  r1(L)+r2(L)−1=(p²+p−4)/2.

This p-adic rank is exact and unconditional on Leopoldt: it is determined by the ARCHIMEDEAN Δ representation over Q, and eχ exists integrally since p∤|Δ|. L does NOT contain μp globally because det:ker χ→Fp× is surjective (upper triangular [[a,b],[0,1]] have determinant a), so the χ-global p-units have no hidden p-torsion roots of unity.

Concrete arithmetic outputs:
- p=5, degree24: rank(U_L)^χ=3, total unit rank13;
- p=7, degree48: rank(U_L)^χ=4, total unit rank26;
- p=107, degree11448: rank(U_L)^χ=54;
- **p=599, degree358800: rank(U_L)^χ=300, total unit rank179698**;
- p=16231, degree263445360: rank(U_L)^χ=8116. This last number concerns GLOBAL units only (the one-prime local analysis below is only supersingular).

**Independent source:** the companion Python verifier performs exact χ-eigenspace linear algebra on the ACTUAL ARCHIMEDEAN PERMUTATION Δ-modules for p=5,7,11,13 and proves the symbolic orbit formula for p=107,599,16231. It does not construct unit generators.

Dirichlet's logarithmic equivariant unit theorem: https://openmaths.org/courses/NT-ANT/dirichlets-unit-theorem.html (general statement), and the group-ring formulation in Stark/Artin L-function literature.

## 3. THEOREM B — a hard rank lower bound for p-ramified χ-ray classes at supersingular p

Now assume in addition p is supersingular at E, so a_p(E)=0 for p≥5. The published inertia theorem (Serre's level-two fundamental character) gives a full nonsplit Cartan F_(p²)× on E[p], order p²−1. It acts regularly on the nonzero dual covectors, so p is TOTALLY RAMIFIED in L/Q with [L_\mathfrak p:Q_p]=p²−1 and there is exactly one prime \mathfrak p of L above p. The extension K/Q has one prime above p with local degree p+1, and L_\mathfrak p/K_\mathfrak q is a cyclic tame extension of degree p−1 with Galois group Δ.

The p-adic logarithm of local units gives a Q_p[Δ] comparison

  (O_(L_\mathfrak p)×)^∧p ⊗Qp ≅ L_\mathfrak p.

By the LOCAL NORMAL BASIS theorem, L_\mathfrak p≅K_\mathfrak q[Δ] as K_\mathfrak q[Δ]-modules. Since [K_\mathfrak q:Qp]=p+1, **EVERY** 1D Δ-character, and in particular χ, occurs with multiplicity exactly p+1:

  **rank_Zp eχ (O_(L_\mathfrak p)×)^∧p = p+1.**

Let X_p(L)=Gal(L_{unram outside p}^{ab,pro-p}/L), the Galois group of the MAXIMAL abelian pro-p extension of L unramified outside its unique p-adic prime (all infinite primes are allowed as usual). Global Artin reciprocity gives an exact χ-isotypic sequence of compact finitely generated Z_p-modules

  0 → eχ(U_loc / closure(U_global)) → eχ X_p(L)
     → eχ(Cl(L)⊗Z_p) → 0.

The last term is FINITE, though its order is UNKNOWN; the local-unit term has rank (p+1)−rank(im global units).

Define the nonnegative **χ-Leopoldt defect**

  δχ,p = rank_Zp ker[eχ(U_L⊗Zp) → eχ U_loc].

Then the exact character-specific rank formula is

  **rank_Zp eχ X_p(L) = (p+1)/2 + δχ,p ≥(p+1)/2.**

This requires **NO Leopoldt conjecture**. Under Leopoldt for this χ component the rank is exactly (p+1)/2; without Leopoldt it may be even larger.

At p=107: rank eχ X_107(L)≥54.
At p=599: **rank eχ X_599(L)≥300**.
For all eligible good supersingular p, this lower bound grows linearly in p.

**Decisive mathematical scope:** A proposed universal bound "dim_Fp of the χ-part of the FULL p-RAMIFIED ray-class module ≤2" is PROVABLY FALSE for these supersingular p, even after dividing out any finite amount of known Mordell–Weil torsion, because its Zp-free quotient has rank≥(p+1)/2. One MUST isolate the ORDINARY everywhere-unramified finite class group, AND impose the genuine rational descent equations; bounding the whole ray group cannot work.

This result DOES NOT imply the ordinary classgroup p-rank is large. The exact *finite* quotient eχ Cl(L)⊗Zp may have p-rank 0,1,2, or more; its unknown p-rank rχ,p is the correct target from PR33. The fact that X_p(L) has ≥300 FREE directions at p599 does NOT contradict our earlier sufficient gate rχ,599≤2.

Sources: Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, supersingular inertia; tame local normal basis; global class field theory and p-ramified exact sequences; https://openmaths.org/courses/NOE-ABS/NOE-ABS-05.html for normal integral bases and https://math.ucla.edu/~sharifi/notes/iwasawa-ch01.html for classes/units.

## 4. THEOREM C — the Hecke/Artin L-function has a HIGH order zero at s=0

Lift the nontrivial χ to a finite-order complex Hecke character \(\widetilde\chi\) of K, via the cyclic extension L/K. At the two real K places, \(\widetilde\chi\) is even at one and odd at the other. At each of the (p−1)/2 complex K places its local gamma factor is Γ_C(s). Therefore the archimedean gamma product has exactly

  1+(p−1)/2 = (p+1)/2

simple poles at s=0: one Γ_R(s) from the even real place, and (p−1)/2 copies of Γ_C(s) from the complex places. The odd real factor Γ_R(s+1) is regular at 0. The completed Hecke L-function is entire at 0 and its functional equation relates its nonzero leading value to the nonzero Hecke L(1,χbar); hence the primitive complex Hecke L-function has EXACTLY

  **ord_(s=0) L(s,χtilde)=(p+1)/2.**

At p599 this is an exact order-300 zero. This is a theorem of the ordinary Hecke functional equation, not an assumption about generalized Stark units or an explicit calculation of the 300th derivative. It provides an independent analytic confirmation of the χ-unit rank. The leading coefficient/regulator's p-integral normalization and its relation to χ-p-class torsion is precisely what remains *uncomputed*.

Source: Hecke gamma factors/functional equation https://people.maths.ox.ac.uk/horawa/L-functions.pdf ; Stark higher-order leading-term literature (equivariant class number formulas).

## 5. Executed exact independent verification and honest boundary

Companion standard-library Python proof-sanity checker:

  verification/bsd389_chi_units_ray_class_rank_audit.py

Its **assistant-executed standalone** source in current chat is /mnt/data/bsd389_chi_units_ray_class_rank_audit.py, SHA256:

  4ac9628b3d035308b75cae1a66ec5b7df31b02a3223201cd8cc1e61155bfb4b9

It checks p5,7,11,13,107,599,16231 signature and relative unit-rank arithmetic, plus constructs the exact Δ action on ALL archimedean embeddings and directly computes the χ-eigenspace kernels of matrices size 14,27,65,90 for p5,7,11,13. It does NOT compute unit generators, their p-adic logarithms, the finite χ-classgroup rχ,p or actual Sha at any new p.

**Conclusion / research verdict.** This proves a genuinely new structural obstruction to a naive class-field uniform upper bound and singles out the finite ordinary p-classgroup χ-component as the only viable target of this particular approach. The still missing key assertion rχ,p≤2 for every sufficiently large p is **NOT** implied by any of the new ranks or analytic orders. A comparison with proven integral Kato Fitting ideals or an actual χ-classgroup calculation remains necessary. Global Sha finiteness and the exact complex rank-two BSD identity are still OPEN.
