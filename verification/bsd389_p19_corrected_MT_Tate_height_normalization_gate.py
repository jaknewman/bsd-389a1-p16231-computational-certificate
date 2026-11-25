#!/usr/bin/env python3
"""Exact finite-field arithmetic audit for the corrected Mazur--Tate/Tate
height comparison at E389a1 p=19.  NO Kato or Mazur--Tate theta input.

The *theorem* that identifies canonical tame Poincare splitting with Tate
monodromy is proved in the companion paper from Tan (L4) and Robert
(Cor. 2.5, 3.12).  This tiny script checks the mandatory inverse factors
and the resulting rank-two matrix arithmetic; it does NOT independently
compute the global biextension height or prove any BSD leading term.
"""
from bsd389_local_reduced_Tate_weights_independent import weight, count_points

p=19
q1,q2=2243,3877
N1,N2=count_points(q1),count_points(q2)
assert N1==2261 and N2==3781
assert N1%p==N2%p==0 and N1%(p*p)!=0 and N2%(p*p)!=0
M1,M2=N1//p,N2//p
w1,w2=weight(q1,p,True),weight(q2,p,True)
assert (w1,w2)==(17,18)
v1,v2=(1,1),(0,1)

# The p-order representatives u_i are actual multiples of M_i but 1 mod p.
u1,u2=4*M1,17*M2
assert (u1,u2)==(476,3383)
assert u1%p==u2%p==1
assert (u1//M1)%p==pow(M1,-1,p)
assert (u2//M2)%p==pow(M2,-1,p)

alpha1=w1*pow(M1,-1,p)%p
alpha2=w2*pow(M2,-1,p)%p
assert (alpha1,alpha2)==(11,2)
assert alpha1 not in {w1,(-w1)%p} and alpha2 not in {w2,(-w2)%p}

H=[[ (alpha1*v1[i]*v1[j]+alpha2*v2[i]*v2[j])%p for j in range(2)] for i in range(2)]
assert H==[[11,11],[11,13]]
det=(H[0][0]*H[1][1]-H[0][1]*H[1][0])%p
assert det==3
assert (2*M1*M2*det)%p==4

print("P19_CANONICAL_TAME_HEIGHT_MINVERSE_NORMALIZATION_PASS",
      "Mmod19",(M1%p,M2%p),"Tate_weights",(w1,w2),
      "corrected_alpha",(alpha1,alpha2),"H_up_to_common_sign",H,
      "height_det",det)
print("P19_EMPIRICAL_KATO_THETA_COMPARISON_STILL_UNPROVED",
      "2M1M2_times_height_det_mod19",(2*M1*M2*det)%p,
      "known_true_Kurihara_coefficient_mod19",4)
print("BOUNDARY_NO_NEW_SHA_VANISHING_NO_UNIFORM_BSD")
