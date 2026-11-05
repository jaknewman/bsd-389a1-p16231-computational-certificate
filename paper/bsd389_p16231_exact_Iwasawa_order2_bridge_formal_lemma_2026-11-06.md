# From fully certified Gross theta to Iwasawa order two: exact formal lemma and gates

Date: 2026-11-06. E=389a1, K=Q(sqrt(-3)), p=16231, H=87809710.

## Authenticated computations

The entire Gross cycle of H points and its independent quaternionic mu3 closure passed in Sage/Boost. Its raw binomial moments mod p are [0,0,4083], and its normalized finite theta coefficients are [0,0,3739] modulo p.

The latest user-run Appendix-local formula gate completed with CH_APPENDIX_STATUS=0. It checked the fixed integer Brandt vector at Hecke primes 2,3,5,7 with eigenvalues -2,-2,-3,-5; exact P1 principal-unit lattice invariance at four anchors; n=1,2 upper-unipotent scaled right lattice construction; exact cubic symmetry of true P2 classes at four independent anchors; and -3*4986*4083=3739 modp. This does not independently check every possible adelic convention.

## Source formula

Castella--Hsieh, Forum Math. Sigma 10 (2022), Appendix section 6, defines the right ideal P_n^a from the upper-unipotent matrix r_n(a)_p=[[1,a/p^n],[0,1]] and its finite theta

Theta_n(T)=alpha_p^(-n-1) SUM_(i=0)^(p^n-1) SUM_(a in mu_(p-1))
 [alpha_p*phi(P_n^(a(1+p)^i))-phi(P_(n+1)^(a(1+p)^i))]*(1+T)^i.

The appendix states Theta_infinity=Theta_n modulo ((1+T)^(p^n)-1). In characteristic p and n=1, ((1+T)^p-1)=T^p. Hence the degree 0,1,2 coefficients of the true infinite series modulo p agree with those of the finite n=1 theta, assuming equality of the actual source ideals/eigenform normalization and our builder.

For n=1 the P1 term is independent of i (a*(1+p)^i=a modp), and sums of binomial(i,k), 0<=i<p, vanish modulo p for k=0,1,2. The global cubic action quotient on true P2 classes converts the full a sum to three times the H orbit. The local ordinary root has alpha_p^-2=4986 modulo p. The coordinate i=10816*n modulo p is the principal-unit exponent of the exact norm19 generator w. This yields b0=b1=0 and b2=3739!=0 modp in the chosen orientation, provided the ring-class reciprocity map agrees with the cyclic coordinate.

## Formal lemma: infer exact degree 2 from the functional equation

Let F(T)=a0+a1*T+a2*T^2+... in Z_p[[T]] with p odd. Assume:
(1) a0=0 EXACTLY, not merely modp.
(2) a1=0 modp and a2!=0 modp.
(3) The anticyclotomic functional equation has form
F(-T/(1+T))=epsilon*U(T)*F(T),
epsilon in {+1,-1}, U(T) in 1+T*Z_p[[T]].

Then necessarily epsilon=+1 and a1=0 EXACTLY, so ord_T(F)=2.

Proof: Compare degree one: -a1=epsilon*a1. If epsilon=+1, then 2a1=0, so a1=0. If epsilon=-1, compare degree two, writing U(T)=1+u1*T+...:
a1+a2=-a2-u1*a1, hence 2a2=-(u1+1)*a1. Modp the RHS is zero, contradicting a2!=0 modulo odd p. Thus epsilon=+1. QED.

This avoids relying on a guessed sign from Atkin-Lehner conventions. The exact sign will be FORCED by a nonzero quadratic coefficient if the actual functional equation applies.

## Exact constant term

The square of the infinite theta at the trivial anticyclotomic character is proportional via Castella--Hsieh Theorem 2.3 to L(E/K,1)=L(E,1)*L(E^(-3),1). Rigorous Mordell-Weil rank2 implies L(E,1)=0 by the established theorem that L(E,1) nonzero forces E(Q) to have rank0. Thus a0=Theta_infinity(0)=0 EXACTLY.

## Conditions not to collapse into a PASS

The remaining mathematical proof obligations are: global identification of every quaternionic Gross right ideal with the appendix P_n right ideal (not only finite samples), integral Jacquet-Langlands eigenform and Brandt order conventions, correct matching of class reciprocity with the coordinate i_n (up to invertible change of generator), and applicability of the actual theta functional equation in this trivial-character setting. The algebraic proofs of P1 invariance and cubic-unit action extend beyond the four sampled anchors, but their global adelic correspondence must be documented.

If all these identifications are rigorously closed, ord_T Theta_infinity=2. Under the further hypotheses of Castella--Hsieh Theorems A and B, together with existence of a suitable auxiliary ringclass character with L(E/K,chi,1)!=0, generalized Kato classes are nonzero and the rational p-adic Selmer dimension is 2. Given MW rank2, this would imply finiteness of Sha(E/Q)[p^infinity], not triviality or full BSD. Appendix section 6 cites an existence theorem of Vatsal/Chida--Hsieh that may supply some suitable chi without an explicit conductor53 evaluation.

Primary references:
https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864
https://www.math.ntu.edu.tw/~mlhsieh/research/central.pdf
