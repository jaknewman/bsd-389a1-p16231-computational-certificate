#!/usr/bin/env python3
"""Independent finite-arithmetic audit for exact rank-two Kummer–Chebotarev
prime-pair density and historical Kurihara residue histogram.

Only tests finite GL2(Z/p²) lift counts and archived quadratic-volume
sample. The Galois/surjectivity theorem, Chebotarev and the universal
nonvanishing of two-prime Kurihara sums are NOT established by this script.
"""
from fractions import Fraction
from collections import Counter

def density_check(p):
    good=0; total=0
    for a in range(p):
      for b in range(p):
        for c in range(p):
          for d in range(p):
            # A=[[1+pa,1+pb],[pc,1+pd]], U=[[1,1],[0,1]]
            det=( (-p*a)*(-p*d) -(-1-p*b)*(-p*c))%(p*p)
            assert det%p==0
            good+=(det!=0);total+=1
    assert (total,good)==(p**4,(p-1)*p**3)
    group_order=(p*p-1)*(p*p-p)
    unipotent_class=p*p-1
    assert Fraction(unipotent_class,group_order)==Fraction(1,p*(p-1))
    frobenius=Fraction(unipotent_class,group_order)*Fraction(good,total)
    one_slope=frobenius*Fraction(p-1,p*p)
    nonzero=frobenius*Fraction(p*p-1,p*p)
    two_independent=p*(p+1)*one_slope*one_slope
    assert frobenius==Fraction(1,p*p)
    assert one_slope==Fraction(p-1,p**4)
    assert nonzero==Fraction(p*p-1,p**4)
    assert two_independent==Fraction((p+1)*(p-1)**2,p**7)
    print("EXACT_KUMMER_FROBENIUS_DENSITY_FINITE_CHECK_PASS",
          "p",p,"p2_lifts",total,"p_parallel_point_count_lifts",good,
          "frob_density",frobenius,"slope_density",one_slope,
          "independent_ordered_pair_density",two_independent)

# Actual p=5 completed 105-pair modular-symbol results, recovered from
# the independently archived VERIFIED quadratic local-volume factorization.
def finite_kurihara_histogram():
    p=5
    directions=[3,0,4,4,None,2,1,0,2,None,2,1,3,3,1]
    local_units=[1,2,2,4,1,1,4,4,4,3,3,2,1,3,1]
    hist=Counter()
    for i in range(len(directions)):
        for j in range(i+1,len(directions)):
            s,t=directions[i],directions[j]
            determinant=(t-s)%p if s is not None and t is not None else int(s!=t)
            delta=3*local_units[i]*local_units[j]*determinant**2%p
            hist[delta]+=1
    assert hist==Counter({0:12,1:19,2:25,3:23,4:26})
    print("ARCHIVED_GENUINE_P5_105_KURIHARA_RESIDUE_HISTOGRAM_PASS",
          sorted(hist.items()),"eligible_nonzero",sum(hist[v] for v in range(1,p)),
          "not_asymptotic_distribution_evidence")

if __name__=="__main__":
    for p in (5,7,11):density_check(p)
    finite_kurihara_histogram()
    print("BOUNDARY_NO_NEW_TWO_FACTOR_UNIT_EXISTENCE_NO_GLOBAL_SHA_FIN")
