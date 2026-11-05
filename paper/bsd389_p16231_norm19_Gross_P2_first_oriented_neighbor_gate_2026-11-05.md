# Exact one-step norm-19 oriented Gross-point transport at conductor p² (pilot)

Date: 2026-11-05. E389a1, p=16231, K=Q(sqrt(-3)), O_m with m=p²=263445361. The user's run confirmed that [g], g=5+3omega, has order 87809710 in Pic(O_m), and that the genuine conductor-one P2^1 class is a right ideal with Brandt class 9. The 16231-point principal-unit orbit for a=1 is completely computed, with moments [0,10775,5515] mod p.

## Differentiate ring-class vs quaternionic action

The finite group theorem [g] generates Pic(O_m) is not the same as knowing the definite quaternionic **oriented** right-ideal class after a prime-19 step. A class-only transition on the 33 Brandt indices is in general not deterministic: it also requires the **current CM embedding** and the chosen prime above 19. The Stage22 conductor53 transport is valid but not a replacement for conductor p².

This note develops a ONE-STEP exact reconstruction and independent validation, with no assertion that 87.8 million steps have been run.

## Correct prime-19 orientation at conductor p²

Let omega²+omega+1=0 embedded globally in the unique Brandt maximal order R_32 with six units, as user certified. The genuine Gross right ideal for a=1, n=2, is T(1)=J_2(1) I_32; its left maximal order is L=T(1).left_order(). The element

q = m*omega

belongs to L, since locally at p the conjugate r_2(1)^(−1) q r_2(1) has integral matrix entries, and away from p omega already lies in R_32. Its characteristic polynomial is t²+m t +m²=0.

Modulo 19, p=16231 ≡5, m ≡6. In the norm19 ideal (g)=(5+3omega) we have omega≡-5/3≡11 (mod19), and for conjugate (gbar)=(2−3omega) we have omega≡2/3≡7 (mod19). Therefore

root_g = m*11 mod19 = **9**,
root_gbar = m*7 mod19 = **4**.

Both satisfy root²+m root+m²≡0 (mod19), and correspond to opposite oriented prime ideals over 19.

For root r, form the exact integral left ideal

J_r = L.left_ideal([q-r,19]).

It must have Z-lattice index 19²=361 in L, and q must belong to J_r.right_order(). The right-ideal class action is represented by

T_next = conjugate(J_r) * T(1),

as in the user's older exact conductor53 Stage22. This is a REAL conductor-p² right ideal, not a symbolic transition.

## Completely independent comparison

The previously certified p4 Hensel/Peirce algorithm builds direct true Gross right ideals T(a) from two mod-p4 congruences, p8 lattice index and exact quaternionic right-ideal closure. The CRT split ratio of the norm19 element is

w(g) = (5+3*r0)/(5+3*r1) = **138112843** (mod m),
w(g)^(-1) = **56004792** (mod m).

The planned verification compares:
- root 9 transport of T(1) to independently reconstructed T(138112843);
- root 4 transport of T(1) to independently reconstructed T(56004792).

At each comparison the script requests an exact quaternion multiplier from Sage's right-ideal equivalence certificate and checks alpha*T_next=T(a). It also tries a **stronger proposed global ideal identity**

(g/19) * conjugate(J_root9) * T(1) == T(w(g)),
(gbar/19) * conjugate(J_root4) * T(1) == T(w(g)^(-1)),

which may need correction for exact fractional-lattice normalization, even if the class equivalence holds. The script prints the yes/no status; only successful witnessed equivalence earns a transport PASS.

This is the first necessary orientation gate for using the full cyclic generator. Even after it passes, an efficient iteration of many thousands/millions of 19-steps requires controlled ideal reduction **and transport of the embedded q**. Knowledge of a 33-class index alone is insufficient to predict the next class. No global theta coefficient is determined by one- or two-step consistency.

## Scripts and verified prerequisites

- USER PASS 2026-11-05: [norm19 full ringclass group generator](../results/bsd389_p16231_norm19_full_class_group_generator_USER_PASS_2026-11-05.md).
- USER PASS 2026-11-05: [first full P2 i-orbit moments](../results/bsd389_p16231_P2_FULL_residue1_16231_gross_moments_USER_PASS_2026-11-05.md).
- NEW, not yet user-run: [one-step oriented norm19 P2 transport and independent direct-anchor test](../verification/bsd389_p16231_P2_norm19_one_step_adelic_transport.py).

Boundary: no theorem-level nonvanishing of theta coefficient, no established theta order exactly 2, no new Sha p-primary finiteness or full BSD proof.
