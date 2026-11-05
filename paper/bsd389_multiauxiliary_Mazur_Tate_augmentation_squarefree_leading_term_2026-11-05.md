# E389a1: squarefree leading-term support for any number of admissible auxiliaries

**Date:** 2026-11-05. This note proves a conditional-on-standard-norm-relations algebraic theorem, not global nonvanishing or BSD.

## Precise assumptions

Fix an odd prime p>=5 and a family of **compatibly Néron-period normalized p-integral** Mazur–Tate elements `Theta_n`, indexed by squarefree products n of p-admissible good primes q. Assume the family obeys the standard Hecke projection relation, for q not dividing m,

`pi_(mq,m)(Theta_(mq)) = U_(q,m) Theta_m`

in the relevant p-group ring, where the Euler factor `U_(q,m)` has augmentation order >=2 modulo p. There are *different* conventions:
- **raw symbols:** frequently `a_q - sigma_q - sigma_q^(-1)`;
- **regularized symbols:** an Euler factor equal up to a group unit to `q - a_q sigma_q^(-1) + sigma_q^(-2)`.

For a p-admissible q, `q≡1` and `a_q≡q+1≡2 (mod p)`. For `s=(1+T)^t`, the raw factor has quadratic term `-t²T²`; the regularized factor `1-2s^(-1)+s^(-2)=(1-s^(-1))²` has quadratic term `+t²T²`. Thus both are in augmentation squared. Do NOT substitute the raw norm factor for a regularized Theta, or vice versa. The exact source convention must be checked when applying to the C++ Manin table.

Reference for regularized construction and norm: Henri Darmon, *Euler Systems and Refined Conjectures of Birch Swinnerton-Dyer Type*, §§2.3.1–2.3.2, Lemma 2.2: https://www.math.mcgill.ca/darmon/pub/Articles/Research/06.Euler-systems/paper.pdf .

## Theorem (leading squarefree monomial)

Let `n=q1...qr`, r>=1, all q_i p-admissible. Let `Phi_n` project the p-primary quotient of each q_i factor into `Fp[Xi]/Xi^p`, and put `F_n=Phi_n(Theta_n)`, `J_n=(X1,...,Xr)`.

Then **`F_n ≡ delta_n · X1...Xr (mod J_n^(r+1))`**, where `delta_n` is the coefficient of the squarefree monomial `X1...Xr` (and, in the correct modular-symbol convention, the corresponding normalized Kurihara sum). In particular `F_n ∈ J_n^r`. Every monomial of degree <=r other than the full squarefree product has zero coefficient.

### Proof by induction

For r=1, evaluate at X1=0. The norm relation down to m=1 gives `epsilon(F_q)=epsilon(U_(q,1)) Theta_1=0 mod p`; hence `F_q ∈ (X1)` and `F_q ≡ delta_q X1 mod (X1)^2`.

Suppose the statement holds for r-1. Fix any index j and set Xj=0. This corresponds to projection from q1...qr to m=n/qj; by the norm relation,

`F_n|_(Xj=0) = U_(qj,m) F_m`.

As all corresponding Euler factors are in `J_m²`, and inductively `F_m∈ J_m^(r-1)`, the projection lies in `J_m^(r+1)`.

Take any monomial of total degree <=r in F_n. If it misses at least one variable Xj, its coefficient vanishes by the projection assertion. A monomial of degree <=r involving all r variables must have degree exactly r and be the full squarefree product. Thus the asserted congruence follows. QED.

The proof requires p-integrality and actual norm compatibility at each intermediate squarefree m; mere availability of a frozen array of residues cannot replace these hypotheses.

## Concrete consequences and testing

- r=2: `F_(q1q2) ≡ delta_(q1q2) X1 X2 mod J³`. This implies the three polarization projections satisfy `Q10=Q01=0, Q11=delta`.
- r=3: `F_(q1q2q3) ≡ delta_(q1q2q3) X1X2X3 mod J⁴`. All constant, linear and quadratic coefficients and every cubic pure/repeated-direction coefficient vanish.
- r=4 and higher: analogously the degree-r term is proportional to `∏Xi`.
- The norm-factor quadratic expansions were checked locally in exact integer arithmetic for all t modulo p=5,7,107 (119 tests). This checks algebra only, not actual Manin symbol evaluations.
- For p107 n=369793·383917, the archived reaggregate delta=34 predicts `F≡34XY mod J³` if the original Manin table normalizations implement the correct compatible modular-symbol system. The genuine 710-block audit does **not** independently compute the pure coefficient projections.
- **No uniform primitivity follows**: `delta_n=0` is consistent with all these congruences. The theorem gives the *shape* of the degree-r leading term, not whether it is a unit or which degree r first occurs.

## Boundary for Sha

The theorem cannot force the first nonzero leading coefficient to have r=2 for all large p. Kim's theorem can interpret the minimal nonvanishing auxiliary cardinality as Selmer corank and Fitting information, but the augmentation support theorem alone leaves all leading coefficients potentially zero. Consequently this is not a proof of uniform finiteness of Sha or full BSD.
