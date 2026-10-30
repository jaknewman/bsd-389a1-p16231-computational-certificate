# BSD 389a1 — genuine cyclotomic Mazur–Tate p² quadratic coefficient nonzero at p=599

**2026-10-30. Observed on user's Sage-enabled Ubuntu. Status:** PASS for a finite-level mod-599 group-ring calculation, **NOT** a rank-two Kolyvagin/Kurihara delta or a Sha certificate.

## Input and exact user-executed output

Source: [Sage script](../verification/bsd389_p599_cyclotomic_p2_moment_probe.py). User's table SHA-256: `fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8`.

```bash
python -u verification/bsd389_p599_cyclotomic_p2_moment_probe.py \
  --p 599 --table ~/bsd389_p599_manin_table.txt \
  2>&1 | tee ~/bsd389_p599_cyclotomic_p2.log
```

```text
CYCLOTOMIC_MANIN_TABLE_SHA256 fc162c6f20459e2973c0641629d3c9feba3df39c0b42cd58aaf2e1bbed7435c8
CYCLOTOMIC_P2_CONFIG p 599 n 358801 a_p 0 S0_modp 0
CYCLOTOMIC_P2_ALL_HECKE_FIBRES_PASS 598
CYCLOTOMIC_P2_PARITY_GAMMA_PASS pairs 179101
CYCLOTOMIC_P2_SUPERSINGULAR_ZERO_AUGMENTATIONS_PASS 598
CYCLOTOMIC_P2_TAME_TRIVIAL_MOMENTS 599 C0 0 C1 0 C2 543 seconds 3.231
BOUNDARY: finite cyclotomic theta moments, NOT Kurihara delta, Selmer or Sha.
```

## Mathematical deduction

Put p=599 and gamma=1+p modulo p². The tame-trivial projection of the standard (unhalved) plus modular symbol group-ring element theta_(p²) has expansion theta(T)=sum_(j=0)^(p-1) C_j*T^j in Fp[T]/(T^p), where

  k(a) = - (a^(p-1)-1)/p (mod p);
  C_j = sum_(a mod p², p not dividing a) S(a/p²) binom(k(a),j) mod p.

The finite-field arithmetic and 598 Hecke fibres were checked by the user. Therefore the exact residue statement is

  theta(T) = 543*T² + O(T³) in F_599[T]/(T^599)

with coefficient 543 = -56 mod 599 != 0, and theta lies in I² but not I³ for the augmentation ideal I=(T) **of that tame-trivial cyclic p-group projection**. Its augmentation filtration order is exactly 2. This is a genuine *finite-level* arithmetic fact; the coefficient cannot be silently identified with a signed supersingular p-adic L-function leading term or the original q1*q2 Kurihara coefficient.

**Independent follow-up:** construct a separate continued-fraction C++ computation to reproduce 543 and compare a sample of coefficients to eclib itself, not just the same 390-Manin Python evaluator. **Still outstanding:** theorem-level bridge from this finite-level leading term to a certified supersingular Selmer/Fitting bound and Sha[599^infinity]. Ordinary p-adic BSD leading-term predictions are not an unconditional substitute. 
