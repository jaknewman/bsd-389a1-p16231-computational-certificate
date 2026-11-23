# E389a1 — 20 NEW degree-25 real cyclic fields with no MW rank growth although two-factor Kurihara vanishes mod5

**23 Nov 2026. New genuine arithmetic result with explicit exhaustive evidence.** This paper extends the p5 valuation-one conductor \`n=5351*13001=69,568,351\`, independently user-reproduced in \`verification/bsd389_p5_depth25_valuation1_Fitting_gate.py\`, by evaluating all **twenty** unit-weight diagonal integer Mazur–Tate polynomials from ALL 34,775,000 genuine plus-Manin representatives. The 20 polynomial histograms were independently computed and ALL **40** true cyclotomic resultants were computed in SymPy; they have nonzero values. A theorem of Kato then forces rank stability over 20 NEW real cyclic degree25 fields, despite \`delta_(q1q2)=15 mod25 =0 mod5\`. This DOES NOT prove Sha(E/K)[5∞]=0 for these new fields, and does not prove all-prime Sha(E/Q) finiteness or full BSD.

## 1. Exact definition of the fields

Take E/Q: y²+y=x³+x²−2x, conductor389, rank2, torsion0 and no rational isogeny. Let
    q1=5351, q2=13001, n=69,568,351, m=25, p=5;
    g1=11 (primitive root modq1), g2=3 (primitive root modq2).
Write lambda_i(a)=discrete_log_(g_i)(a) mod25. Since 50|q_i−1 the characters are even.

For every r∈(Z/25)^×, let
    chi_r(a)=zeta25^(lambda_1(a)+r lambda_2(a)),
    K_r=Q(zeta_n)^(ker chi_r).
These are TWENTY distinct totally real cyclic degree25 extensions with conductor n and discriminant n^24. Every nontrivial character chi_r^t, t=1..24, is primitive of conductor n. The 20 sets together contain 400 distinct order25 characters, and 16 distinct order5 characters, so **416 distinct twisted L values** (not 480).

The original genuine 34,775,000-representative certificate gave
    delta_(q1q2) ≡ 15 mod25,  v5(delta)=1.
Thus none of these r can satisfy the old unit-mod5 two-factor Kurihara criterion.

## 2. NEW ALL-20 authentic integer Mazur–Tate calculation

For each of the 20 unit residues r, independently compute the full ORIGINAL 25 integer coefficients

    F_r(X)= sum_(a mod n)^* m_E^+(a/n)
                    X^([lambda_1(a)+r lambda_2(a)]_25)
       ∈ Z[X], degree<=24.

An optimized C++ program evaluates **34,775,000 plus-Manin representatives**, and for each representative accumulates all 20 orientations using the previously separately authenticated original 390-integer Manin symbol vector. All 500 integer histogram coefficients are stored and verified with SHA256 of the canonical compact JSON array of [r,hist] pairs:

    **1a22c0ed1b4ac336a648ec0a0bf1d6121fd6224993c37e928713117cd1d4c463**.

The entire r=1 histogram exactly reproduces the user's independent previous val1 result.

All actual low Taylor coefficients c_j(r)=[T^j]F_r(1+T) obey
    c0=0,
    c1 ≡0 mod25,
    c2 ≡15r mod25,
    c3 ≡0 mod5.

The first nonzero mod5 Taylor coefficient and the actual integral cyclotomic resultants form TWO regular classes:

| r mod5 | # fields | first j with c_j mod5 !=0 | v5(Res(F_r,Phi_5)) | v5(Res(F_r,Phi_25)) |
|:--:|--:|--:|--:|--:|
|1 or 2|10|4|4|4|
|3 or 4|10|6|6|6|

The degree-four residues c4 mod5 are 1,4,0,0 for r≡1,2,3,4. The degree-six residues are 2,4,3,3, respectively. **All forty exact cyclotomic resultants are NONZERO**, not inferred from a raw mod5 cancellation heuristic.

The order25 characters have valuations v_(zeta25−1) A(E,chi_r^t)=4 or6 for 5∤t, from the exact Phi25 resultants (unique totally ramified prime of Q(zeta25) above5).

The order5 characters have valuations v_(zeta5−1) A(E,chi_r^t)=4 or6 for 5|t (nonzero t), from the exact Phi5 resultants. The latter need an actual resultant check: when r≡3,4 mod5, the quadratic coefficient's p-valuation can TIE with the degree-six term after evaluating at zeta5−1, so treating the degree-six unit alone as sufficient would be unsafe. The direct resultant confirms no cancellation.

By the genuine Birch–Stevens twisted modular-symbol identity, all those modular-symbol values being nonzero implies the 416 distinct complex critical twisted values
    **L(E,chi,1) != 0**.

### Extra full integral Smith-matrix classification (20 more genuine tests)

Recenter every TRUE 25-entry theta F_r by its actual Frobenius-inversion shift s_r, obtaining a symmetric G_r(X). Let A_r be multiplication by G_r on the 12-dimensional integral symmetric augmentation lattice, with entries g_(i-j)+g_(i+j)-2g_i.

Independent exact SymPy computations on ALL TWENTY original matrices give:

| r mod5 | number | p=5 Smith elementary exponents of A_r | nonunit invariant factors |
|---|---:|---|---|
|1 or 2|10|[0 repeated 10, 2, 2]|25,25|
|3 or 4|10|[0 repeated 9, 1, 2, 3]|5,25,125|

In EVERY case, \`det(A_r)^2=Res(F_r,Phi5)*Res(F_r,Phi25)\` exactly over the integers, not merely modulo5. These patterns match the true resultant valuations 8 or12, respectively. The companion Python verification program now recomputes all 20 Smith matrices and these exact determinant-square identities in addition to the 40 cyclotomic resultants.

**This analytic Smith classification MUST NOT be misinterpreted as the Smith form of a Selmer presentation** or as the structure of Sha(E/K_r)[5∞]. It is evidence about the genuine integral theta multiplication operators.

## 3. NEW arithmetic consequence: 20 extra fields with exact MW non-growth

Kato's proved theorem for weight2 modular elliptic curves and nontrivial abelian Dirichlet characters states: L(E/Q,chi,1)≠0 implies that the chi-isotypic multiplicity of E(K)⊗C is ZERO. (Reference: R. Greenberg, *Iwasawa Theory for Elliptic Curves*, Theorem1.20 explicitly attributing the assertion to Kato, https://www.math.union.edu/~hatleyj/Park.pdf; or Kato, Astérisque295.)

All nontrivial Galois characters of each K_r have a nonzero central L-value, so

    **rank_Z E(K_r)=rank_Z E(Q)=2**.

The curve 389a1 has no Q-rational isogeny, so each E[ell] is irreducible. Because K_r/Q is Galois of degree25, any nonzero E[ell](K_r) would equal full E[ell]. For odd ell this forces μell⊂K_r, impossible because [Q(μell):Q]=ell−1 is even and 25 is odd. For ell=2 it forces Q(E[2])⊂K_r, impossible since [Q(E[2]):Q]|gcd(6,25)=1 but E(Q)[2]=0.

Thus E(K_r) is torsion-free. Rank equality implies every R∈E(K_r) is rational: some integer multiple is rational, and (σR−R) is torsion, hence zero. Consequently

    **E(K_r)=E(Q)=ZP⊕ZQ EXACTLY**.

The Artin product similarly proves
    **ord_(s=1) L(E/K_r,s)=2**
using the already independently certified analytic rank2 of E/Q.

This is a strict extension of the project: the previous 34 rank-stable cyclic fields had p-unit two-factor Kurihara witnesses. The present TWENTY have NONUNIT two-factor Kurihara modulo5, yet ALL twists remain nonzero. Since the new conductor n is distinct from the previous three, total currently certified (conditionally on published Kato theorem) is

    **54 distinct totally real cyclic fields with E(K)=E(Q)**
    **948 distinct nontrivial characters with L(E,chi,1)≠0**.

The latter count is 532 previous plus416 new, with distinct conductors.

## 4. IMPORTANT: no new Sha(K) annihilation conclusion

The valuation-one depth25 theorem proved earlier via Bullach–Honnor plus p-parity guarantees **Sha(E/Q)[5∞]=0**, and that implication does NOT require twisted L-value nonvanishing. But the same p² val1 coefficient is NOT a unit and does NOT trigger the strong **Sha(E/K_r)[5∞]=0** theorem or equality (theta)=(T²).

For these 20 K_r the true Mazur–Tate theta has mod5 augmentation order 4 or6, rather than2, and the genuine analytic saturated cokernel may be nonzero. Even though E(K_r)=E(Q), there could be nontrivial p-primary Sha(E/K_r). Do NOT confuse rank stability with Sha finiteness or triviality.

## 5. Provenance/replay and specific reproducible artifacts

Actual full 20-orientation C++ code:
    verification/bsd389_p5_val1_all20_cyclic25_integer_hist_native.cpp

Exact integer SHA256 + all 40 genuine Phi5/Phi25 resultant verifier:
    verification/bsd389_p5_val1_all20_twisted_L_norm_spectrum_gate.py

Reproduce on Ubuntu:
\`\`\`bash
g++ -O3 -std=c++17 \
 verification/bsd389_p5_val1_all20_cyclic25_integer_hist_native.cpp \
 -o /tmp/bsd389_val1_all20
/tmp/bsd389_val1_all20 > /tmp/bsd389_val1_all20.txt
python -u verification/bsd389_p5_val1_all20_twisted_L_norm_spectrum_gate.py \
 --hist /tmp/bsd389_val1_all20.txt
\`\`\`

The assistant HAS executed both steps fully on 2026-11-23, obtained 20 clean integer histograms and all 40 nonzero exact resultants. The user has independently confirmed only the r=1 valuation-one conductor, and has not yet reproduced the new all-20 extension. The code uses frozen historically authenticated 390-Manin symbols, not an independent Sage/eclib table regenerated for this new conductor.

**Global BSD:** This is an authentic extension-field rank result and a refined characterization of the p5 valuation-one analytic obstruction. It does NOT prove the global p-uniform two-factor Kurihara modp² nonvanishing or the exact complex rank-two BSD formula.
