# Exact GLOBAL rational-point descent for E389a1 from K=Q(sqrt(-3)): E(K)=E(Q), not just equal rank

Date 2026-11-06. A fully explicit, prime-INDEPENDENT theorem for the elliptic curve relevant to full BSD. Uses only the already proved rank-zero quadratic twist, the 2-division polynomial, and tiny field cardinalities 4 and 7. **Does not calculate any new Sha[p], make an integral Euler-system comparison or prove full BSD.**

E: y²+y=x³+x²−2x; K=Q(sqrt(-3)); tau denotes complex conjugation. Let E^(-3) be the quadratic twist, already certified to satisfy L(E^(-3),1)>9/2, hence rank(E^(-3)(Q))=0 and its Sha is finite by the standard Kolyvagin rank-zero theorem.

## Theorem: exact rational points

\[
\boxed{E(K)=E(Q)=\mathbf Z P\oplus\mathbf Z Q,\quad P=(-1,1), Q=(0,-1).}
\]

**Proof part A: absence of 2-torsion.** A nontrivial point of order two must satisfy 2y+1=0, and its x coordinate is a root of
\(4x^3+4x^2-8x+1\).
The rational-root candidates ±1, ±1/2, ±1/4 all fail. Thus the cubic is irreducible over Q, so cannot acquire a root in any quadratic field. In particular E(K)[2]=0 and all torsion of E(K) is of odd order.

**Proof part B: torsion is in fact trivial.** The primes 2 and 7 are good for E. In K, 2 is inert (residue field F4) and 7 is split (residue field F7).

At 2, direct point counting on E(F2) gives 5 points (x=0 and x=1 each give y=0,1, plus infinity); therefore a2=2+1−5=−2. The finite-field Frobenius recurrence gives a4=a2²−2·2=0, hence
\(\#E(\mathbf F_4)=4+1-a_4=5\).
All torsion is odd by part A, so reduction at the unique place above 2 injects E(K)_tors into the group of order 5. In particular its order divides 5.

At 7, direct point counting over F7 yields 13 points: for x=0,1,3,4,5,6 there are two y values and for x=2 there are zero, plus infinity (6·2+1=13). Thus \(\#E(\mathbf F_7)=13\).
Any remaining 5-torsion injects under reduction at a split place over 7 into E(F7), which has no 5-torsion. Therefore
\[
\boxed{E(K)_{\mathrm{tors}}=0.}
\]

**Proof part C: no non-rational non-torsion points.** For any R∈E(K), put T=R−tau(R). Then tau(T)=−T, and T belongs to the anti-invariant rational point group, identified under quadratic twisting with E^(-3)(Q). Since the twist has rank zero, T is torsion. By part B, E(K)_tors=0, so T=0 and tau(R)=R. Thus R∈E(Q). The reverse inclusion is automatic. QED.

This is an equality of FULL groups, not only of ranks, rational vector spaces or indices of finite 2-power.

## Consequences for both GLOBAL BSD obligations

**(i) Regulator/normalization.** The full saturated MW generators P,Q are exactly the same over Q and K, with NO lattice index factor. Under absolute field-normalized canonical heights, \(\mathrm{Reg}_{E/K}=\mathrm{Reg}_{E/Q}\) exactly. Under the alternative unnormalized trace-height convention the rank-two determinant gains the known factor 4. No unknown lattice denominator survives.

**(ii) Exact analytic Artin factorization.** For every s,
\(L(E/K,s)=L(E,s)L(E^{-3},s)\).
Since L(E,1)=L'(E,1)=0 exactly and L(E^{-3},1)>0, the exact leading coefficient is
\[
\boxed{\frac{L''(E/K,1)}2=L(E^{-3},1)\,\frac{L''(E,1)}2.}
\]
So the rank-two COMPLEX leading-term problem over K and over Q are connected by a single nonzero, exactly defined rank-zero L-value. This is an identity of analytic quantities, not a new proof of BSD.

**(iii) Full Sha finiteness descends.** For all odd p, odd-primary quadratic decomposition is exact:
\[
\Sha(E/K)[p^\infty]\simeq\Sha(E/Q)[p^\infty]\oplus\Sha(E^{-3}/Q)[p^\infty].
\]
At p=2 the rational Shapiro/splitting of Bloch–Kato Selmer gives equality of coranks; the twist is known finite, so Sha(E/K)[2∞] is finite iff Sha(E/Q)[2∞] is finite. Therefore
\[
\boxed{\Sha(E/K)\text{ finite}\iff\Sha(E/Q)\text{ finite}.}
\]
This is a global logical EQUIVALENCE, not a proof of either finiteness.

**(iv) Full BSD global transfer.** The degree-4 isogeny
\(E\times E^{-3}\to\operatorname{Res}_{K/Q}E_K\)
and Cassels–Milne isogeny/Weil-restriction invariance show that full strong BSD for E/K **together with** full rank-zero BSD for the twist would imply full strong BSD for E/Q, and conversely. This is a legitimate bridge of BOTH finiteness and the exact complex leading coefficient, but does not supply the still-missing rank-two global theorem over K.

**Stop rule:** Do not present this improvement as a solution to global Sha or rationality of \((L''(E,1)/2)/(\Omega_E\operatorname{Reg}_E)\). It is a genuinely new, proved full-group descent result which removes the last Mordell–Weil index and torsion complications from that attack, so that a future higher-rank theorem over K can be imported without an unmeasured MW factor.

Sources: standard reduction-injectivity of prime-to-residue-characteristic torsion at good places (Silverman, *Arithmetic of Elliptic Curves*, VII.3); Artin formalism; Cassels–Milne isogeny and Weil restriction invariance; previously archived exact rank-zero twist L positivity and rank-two MW saturation.
