# K599: Three absolute traces instead of 599 coordinates

Date: 2026-10-29. Exact algebraic identity, not a new fast algorithm.

Let p=599 and n=6912461*13963889. Use the existing Artin–Schreier normalization A2=lambda*A1, where lambda=500 mod p, A=A1, A^p-A=187. Let K be the finite field containing the n-th roots of unity, and Shat(m) the additive Fourier transform of the normalized plus modular symbol S(a) in Fp.

For each unit frequency m, define b1=log1(m*q2^(-1)), b2=log2(m*q1^(-1)) and T_r(m)=Tr_(K/Fp)(A^r*Shat(-m)) for r=0,1,2. Then the Kurihara number equals

delta_n = (2/n) * sum_[m modulo <p,-1>]
  (lambda*T_2(m) + (b2+lambda*b1)*T_1(m) + b1*b2*T_0(m)) (mod p).

There are exactly 4792 such frequency classes, so 14376 scalar traces. Since n=1 mod 599, the factor n^(-1)=1.

Proof: the weight Fourier transform is (A+b1)*(lambda*A+b2). Apply character orthogonality, the fact that Fp absolute traces are invariant under Frobenius, and pairing m with -m.

More explicitly, writing H_m=Tr_(K/Fp(A))(Shat(-m)) as sum_(k=0)^(p-1) h_k*A^k, one has T_r(m)=-h_(p-1-r). Indeed the conjugates of A are A+j*187, j in Fp, and Tr_(Fp(A)/Fp)(A^s)=0 for s in [0,p+1], except at s=p-1 where it is -1. Therefore the 599-dimensional coordinate decomposition of H_m is not necessary to read its three target coordinates.

The authentic p=5 Fourier–Artin–Schreier equality was user-verified; see results/bsd389_k5_authentic_fourier_artin_schreier_PASS_2026-10-29.md.

BOUNDARY: This replaces coordinate solves by three traces. It does not compute those traces without constructing the enormous cyclotomic extension or performing an equivalent sum. No sublinear p599 Kurihara algorithm, delta599, or Sha bound is claimed.
