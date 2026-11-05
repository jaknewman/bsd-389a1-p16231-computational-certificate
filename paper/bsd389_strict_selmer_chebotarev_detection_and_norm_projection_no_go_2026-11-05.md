# E389a1 — exact strict-Selmer splitting and a finite-level Mazur–Tate norm-projection no-go theorem

Date: 2026-11-05. All statements below are proved algebraically, subject to explicit standard hypotheses. No uniform vanishing of Sha and no strong BSD formula are claimed.

## A. Strict-Selmer splitting at a two-prime MW-local basis

Let p be an odd prime, E/Q have rational torsion prime to p, and let rank E(Q)=2 with saturated rational basis P,Q. Pick distinct good q1,q2 != p, such that each local Kummer quotient

L_qi = E(Q_qi)/pE(Q_qi) ≅ E(F_qi)/pE(F_qi)

has Fp-dimension one. (Good reduction and q != p yield this identification.) Put S_p=Sel(E[p]/Q), M_p=E(Q)/pE(Q), L=L_q1 ⊕ L_q2, and let λ:S_p -> L be localization. Suppose that the 2x2 matrix A whose columns are λ(P),λ(Q) is invertible mod p.

Then λ restricted to M_p is an isomorphism, and

**S_p = M_p ⊕ ker(λ)**

with a canonical isomorphism (given the selected pair) **ker(λ) ≅ Sha(E/Q)[p]**, induced by the Kummer quotient. Proof: define the retraction π:S_p -> M_p by π = (λ|M_p)^(-1) ∘ λ. Then π|M_p=id, and ker π=ker λ. By the Kummer exact sequence 0->M_p->S_p->Sha[p]->0, the quotient S_p/M_p is Sha[p] and also ker λ.

Consequently, **Sha[p]=0 iff λ is injective iff λ is an isomorphism** for every such MW-basis pair. This does **not** follow from det(A) != 0 alone; the kernel is the possible Sha obstruction.

### Concrete inverse matrices from genuine user's independent local calculations

User-authenticated local matrices are stored at
[results/bsd389_MW_local_determinants_USER_RUN_PASS_2026-11-02.md](../results/bsd389_MW_local_determinants_USER_RUN_PASS_2026-11-02.md).

| p | (q1,q2) | A | det(A) mod p | A^-1 mod p |
|---:|---|---|---:|---|
| 5 | (41,61) | [[1,3],[1,0]] | 2 | [[0,1],[2,3]] |
| 7 | (113,673) | [[1,3],[1,6]] | 3 | [[2,6],[2,5]] |
| 107 | (369793,383917) | [[1,15],[1,53]] | 38 | [[38,70],[76,31]] |

Each A·A^-1 = I was directly checked in Python modulo its p.

For p107, if the localization vector of an arbitrary p-Selmer class in the saved local bases is (u,v), its **unique rational-MW component** is

(38u+70v)·P + (76u+31v)·Q mod 107.

Subtracting this component gives a class in the strict kernel ker λ. The separate genuine SageMath 10.9 certified bound p_primary_bound(107)=0 implies Sha[107]=0, so **the strict kernel is 0 and λ is an isomorphism for this exact pair, without assuming correctness of the original massive native Kurihara loop**. Same implication at p5,p7 from the separate Sage bounds. This is a corollary of the executed inputs plus exact algebra, not a new user execution of a full Selmer basis.

## B. Stronger Chebotarev detection theorem: the minimum number of auxiliary primes

Let p>=5, assume the residual representation Gal(Q(E[p])/Q)=GL2(Fp), and write s=dim_Fp Sel(E[p]/Q), which is finite. Then there exist distinct good **p-admissible** primes q1,...,qs (each q≡1 modp, a_q≡q+1≡2 modp, and dim_Fp E(Fq)/p=1), such that

**Sel(E[p]/Q) -> ⊕_(i=1)^s E(F_qi)/p is an isomorphism**.

The proof is an extension of the standard Kummer–Chebotarev argument to a basis of ALL Selmer classes (not just the MW subspace):

1. Let V=E[p], K=Q(E[p]). A central scalar 2I in GL2(Fp) has (2I-I) invertible; the cocycle identity gives H¹(GL2(Fp),V)=0. Inflation–restriction thus injects H¹(Q,V) into H¹(K,V).
2. Choose an Fp-basis c1,...,cs of Sel(E[p]/Q) ⊂ H¹(Q,V); their restrictions to G_K are independent continuous homomorphisms G_K -> V. Their combined image U ⊂ V^s is GL2-stable for the diagonal action.
3. The natural GL2(Fp)-module V is absolutely simple, with End_GL2(V)=Fp. Therefore a proper stable submodule U of the isotypic semisimple module V^s is annihilated by a nonzero Fp-linear combination of the s coordinate projections V^s -> V. That would contradict independence of c1,...,cs over G_K. Thus U=V^s.
4. Choose a nonidentity unipotent A∈GL2(Fp), whose invariants have dim1, trace=2 and determinant=1. In the finite Galois extension cut out by c1,...,cs and E[p], choose s Frobenius lifts of A with translation images giving the standard basis in each one-dimensional quotient V/(A-I)V. Full U=V^s allows this. By Chebotarev there are infinitely many choices of good primes with these conjugacy classes. They give an invertible s×s localization matrix on the chosen Selmer basis.

Since each chosen local target has dimension one, at least s primes are necessary for injectivity. Consequently, if d_p is the minimum number of 1D p-admissible auxiliary local factors required to make localization on the **full** p-Selmer injective, then

**d_p = dim_Fp Sel(E[p]/Q) = rank E(Q) + dim_Fp E(Q)[p] + dim_Fp Sha(E/Q)[p]**.

For E389a1 the torsion is 1 and rank=2, so **d_p = 2 + dim_Fp Sha(E/Q)[p]** whenever residual GL2 surjectivity holds. This is a mathematically exact characterization, not an effective algorithm to compute d_p without understanding full Selmer. It is also not the same as Kim's *minimal nonzero Kurihara auxiliary degree*, which measures a different invariant.

**Critical noncircularity:** Chebotarev guarantees an injective localization with s primes, not necessarily two. Knowing that a MW-local 2×2 determinant is a unit never implies s=2 or Sha[p]=0.

## C. The sharp finite-level no-go for norm projections

Let R = Fp[X1,...,Xr]/(X1^p,...,Xr^p), with r>=2 and p odd. Let π_j set X_j=0. Then

**∩_(j=1)^r ker π_j = (X1⋯Xr)R**, of Fp-dimension (p-1)^r.

Proof: ker π_j=(X_j), and in the monomial basis their intersection consists of polynomials where every variable has positive exponent, exactly the ideal generated by X1⋯Xr. It has (p-1)^r monomial basis elements.

Modulo J^(r+1), where J=(X1,...,Xr), the above kernel is one-dimensional, generated by X1⋯Xr.

The explicit group ring element H_r=∏_(j=1)^r (σ_j-1) is killed by **every** projection omitting any auxiliary prime, yet

[X1⋯Xr] H_r = 1.

Thus if the complete norm-projection data at all proper divisors of n are fixed, replacing a candidate F_n by F_n+c H_r leaves every one of those projections (and therefore its corresponding norm equation with fixed lower-level elements) unchanged, while shifting the fully mixed leading coefficient by c∈Fp. All the lower total-degree constraints are preserved.

This proves **nonvanishing cannot be deduced from those proper-conductor projection identities alone**, even when all are known exactly. It does **not** assert the perturbed element is a true elliptic modular symbol satisfying all Manin/Hecke identities or higher-conductor compatibility. Hence it is a sharply scoped no-go result, not a counterexample to genuine Kurihara nonvanishing.

For r=2, p=107, the undetermined projection-kernel dimension is (107-1)^2 = 11236; its total-degree-two part is just the 1D scalar XY. This identifies the *exact extra global datum* needed beyond norm relations.

## D. Next concrete proof obligation

Use an independent global cohomological mechanism (e.g. explicit reciprocity for Kato's Euler system or an actual Selmer computation) to prove the **strict Selmer kernel ker λ is zero** for an MW-basis pair at a new p, or to control these kernels uniformly. This extra information is precisely what neither proper conductor distributions nor local MW Chebotarev existence supplies. No such all-large-p argument has been proved here.

Literature context: C.-H. Kim, *The Structure of Selmer Groups and the Iwasawa Main Conjecture for Elliptic Curves*, Theorems 1.8 and 1.10, <https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf>. The above strict-splitting and detection arguments are elementary linear algebra / inflation–restriction / Chebotarev and do not require Kim to be true.
