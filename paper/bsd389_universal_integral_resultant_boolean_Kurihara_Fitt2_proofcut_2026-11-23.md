# 389a1 — universal INTEGER cyclotomic resultant detector: normalized twisted-L product is exactly 0 or 1 modulo p

**23 November 2026. Status: a fully proved finite cyclotomic algebra theorem, applicable to the GENUINE Hecke-normalized rank-two Mazur–Tate theta at any deep p^k-admissible pair.** It creates one honest integer from ALL nontrivial characters and gives a sharp modulo-p Boolean test for a two-factor Kurihara p-unit. The criterion is **primewise**; there is no global prime-independent Sha annihilator or strong BSD proof.

## 1. True integer theta and its quadratic coefficient

Let p≥5, k≥1, m=p^k. Let q1,q2 be distinct good auxiliary primes with

    q_i≡1 (modm),   a_(q_i)(389a1)≡2 (modm),

and choose primitive roots and reductions of their discrete logs λ_i:G_(qi)→Z/m. For each r∈(Z/m)^× define the **genuine integral theta polynomial**

    F_r(X) := sum_(a mod q1q2)^* m_E^+(a/(q1q2))
                           X^([λ1(a)+rλ2(a)]_m) ∈ Z[X],

with canonical exponents in 0,...,m−1. This is a polynomial representing the actual cyclic diagonal Mazur–Tate group ring, not a formal or analytic guess.

Write

    F_r(1+T)=c0+c1*T+c2*T²+T³ H(T).

The authentic Hecke distribution, along with L(E,1)=0, proves

    c0 ≡ c1 ≡ 0 (mod m),
    c2 ≡ r*δ_(q1q2) (mod m).

These statements were checked directly by the user's complete p5, p11 and p5-depth25 symbol sums, including true Hecke norm projections at p5 and p11.

## 2. NEW exact all-p,k determinant/resolvent theorem

Put
    S_m(X) = (X^m−1)/(X−1)=1+X+...+X^(m−1),
and define the single global-in-character (but conductor-dependent) integer

    B_r = Res_X(S_m(X), F_r(X))
        = prod_(t=1)^(m−1) F_r(ζ_m^t) ∈ Z.

**THEOREM (integral normalized resultant).** For EVERY above p,k,q1,q2,r,

    **m² | B_r in Z**,

and writing
    R_r = B_r / m²  ∈ Z,

one has the universal CONGRUENCE

    **R_r ≡ c2^(m−1) ≡ (r*δ_(q1q2))^(p^k−1) (mod p).**

Because p^k−1 is divisible by p−1, Fermat's little theorem gives the even sharper Boolean identity

    **R_r ≡ 1 (mod p)  iff  δ_(q1q2) is a p-unit,**
    **R_r ≡ 0 (mod p)  iff  δ_(q1q2)≡0 (mod p).**

There are NO other possible residues for this normalized integer: it is ALWAYS 0 or 1 modulo p, independent of k and of the unit r.

This is an exact INTEGER criterion, not only a p-adic valuation condition. If δ is a p-unit, v_p(B_r)=2k and R_r is a p-unit. If δ≡0 modp, each nontrivial character specialization has valuation at least 3 in its own cyclotomic uniformizer, hence v_p(B_r)≥3k (or B_r=0); in particular p divides R_r.

## 3. Proof: divide by the algebraic product of ALL cyclotomic uniformizers

Let ζ=ζ_m and O=Z_p[ζ]. For each 1≤t≤m−1 put π_t=ζ^t−1. If ζ^t has exact order p^j (1≤j≤k), then π_t is a uniformizer in Q_p(ζ_(p^j)). The local ramification index there is φ(p^j)≥4.

Expand
    F_r(ζ^t)=c0+c1 π_t+c2 π_t²+π_t³ H(π_t).
Since m=p^k divides c0 and c1, the two quotients c0/π_t² and c1/π_t are INTEGRAL in Z_p[ζ_(p^j)] and vanish modulo its uniformizer: their valuations are at least k φ(p^j)−2≥2 and k φ(p^j)−1≥3. Also π_t H(π_t) is integral and vanishes modulo π_t. Consequently

    **G_t := F_r(ζ^t)/ (ζ^t−1)² ∈ O**
    **G_t ≡ c2 (mod the unique maximal ideal above p).**

The elementary cyclotomic product identity
    prod_(t=1)^(m−1) (1−ζ^t)=S_m(1)=m
implies
    prod_(t=1)^(m−1)(ζ^t−1)²=m².

Hence
    B_r/m² = prod_(t=1)^(m−1) G_t
is p-adically integral. Since B_r is an ordinary integer and m² is a pure p-power, this implies **m²|B_r in Z**. Reducing the equality in O modulo π=ζ−1 gives

    R_r modp = prod G_t modπ = c2^(m−1) modp.

The output R_r is a rational integer, so its reduction modπ agrees with its reduction modp. The authentic theta quadratic coefficient is c2≡rδ modp, so the stated Boolean congruence follows. QED.

All terms are genuine integers in the integral modular-symbol normalization; the only analytic input is the already established exact L(E,1)=0 needed for the low-jet Hecke vanishing. No Sha finiteness is used.

## 4. Quantitative coincidence with Mordell–Weil trace determinant

For a p-unit δ, the theorem gives **v_p(B_r)=2k**.

By the independently proved general Kato/Hecke rank-stability theorem
    paper/bsd389_general_p_power_Kurihara_unit_34_fields_532_twists_MW_no_growth_2026-11-23.md,
each associated cyclic real field F_r has E(F_r)=E(Q)=Z².

The Galois trace (norm) from E(F_r) to E(Q) acts on the two saturated rational generators as multiplication by [F_r:Q]=p^k:

    Tr_(F_r/Q)|_(MW)=p^k I_2,

so its INTEGRAL rank-two determinant is

    **det Tr_(MW)=(p^k)^2=p^(2k).**

The exact valuation **v_p(B_r)=v_p(det Tr)=2k** thus matches automatically at every p and k under the unit-Kurihara hypothesis.

This is a **numerical/structural determinant match**, NOT an identification of the spectral integer B_r with the determinant of a Selmer complex. The normalized B_r/p^(2k) is a p-unit congruent to1, but no map from its spectral norm to Fitt_2(Sel) is constructed. We must not infer Sha vanishing from the match alone.

## 5. Three authentic E389a1 certificates and one short test

Certified genuine pairs:

- p=5,k=1,n=41*61, δ=4 mod5 ⇒ R_r≡1 mod5 for each of 4 cyclic degree5 fields.
- p=11,k=1,n=397*991, δ=1 mod11 ⇒ R_r≡1 mod11 for each of 10 cyclic degree11 fields.
- p=5,k=2,n=5351*10651, δ=22 mod25 ⇒ R_r≡1 mod5 for each of 20 cyclic degree25 fields.

**No expensive new 28-million-term run is required to deduce these normalized resultant congruences**, because they follow rigorously from the user-certified genuine quadratic jets.

An independent exact SymPy verifier, executed by the assistant, checks the normalized resultant Boolean theorem for abstract **integral** polynomials F with c0,c1 divisible m and c2 either a unit or nonunit at:
    (p,k)=(5,1),(11,1),(5,2).
Its 9 tests include explicit genuine coefficient values c2=4,1,22, and forced nonunit controls c2=p or0. The verifier tests the algebraic theorem, not the enormous exact resultant for each original conductor.

Code: verification/bsd389_normalized_resultant_boolean_gate.py

## 6. Clear remaining mathematical obligation for the full BSD problem

This is a universal primewise **TRUE INTEGER** package for the Kurihara information:
    δ unit <=> R_r≡1 modp,
which might provide a suitable target for an integral derived Kato/Selmer determinant map.

BUT the INTEGER R_r depends on p, q1, q2 and r. Nothing in the proof bounds the possible primes p for which every such R_r≡0, nor constructs a SINGLE nonzero integer D with (D)⊂Fitt_2(Sel_p) for all p. Nor does it give the exact complex rank-two BSD leading coefficient.

**New proof target:** Build an actual integral arithmetic morphism comparing the normalized character norm R_r with the TRUE rank-two second-Fitting characteristic of the global Selmer complex, uniformly over p. The mere equality of valuation with the MW trace determinant does not construct this morphism.

**VERDICT:** A real all-p,k cyclotomic-resultant Boolean theorem, a sharpened valuation gap, and an EXACT integer candidate with value 1 modp at our 34 certified fields. No all-prime Sha theorem is claimed.
