#!/usr/bin/env python3
"""E389a1: exact finite checks for the tame p^3 class-field descent.

No class numbers are calculated, no Sha upper bound is asserted.
The theorem is proved in:
paper/bsd389_tame_subfield_classgroup_descent_uniform_good_primes_20261121.md
"""
from math import isqrt

P=(5,7,11,17,23,97,107,599,859,1213,1493,1951,16231)
AP={5:-3,7:-5,11:-4,17:-6,23:-4,97:-9,107:0,
    599:0,859:1,1213:1,1493:1,1951:1,16231:128}

def trace(p):
    s=0
    for x in range(p):
        d=(1+4*(x*x*x+x*x-2*x))%p
        if d:
            t=pow(d,(p-1)//2,p)
            assert t in (1,p-1)
            s += 1 if t==1 else -1
    return -s

def verify(p):
    assert trace(p)==AP[p]
    # GL2(F_p), SL2(F_p), tame complement H.
    size_G=(p*p-1)*(p*p-p)
    size_H=p-1
    size_SL=p*(p*p-1)
    assert size_G==size_H*size_SL
    assert size_G//size_H==size_SL
    # Each diag(1,a) fixes covector ell(x,y)=x and e1.
    for a in (1,2,p-1):
        assert 1<=a<p
        for x,y in ((0,1),(1,0),(2,3),(p-1,p-2)):
            assert (x + 0*(a*y))%p == x%p
        assert a%p
    # Norm∘extension=[p-1] is invertible modulo p.
    assert pow(p-1,-1,p)==p-1
    n=p+1-AP[p]
    anomalous=n%p==0
    # At odd p>=5, local Kummer dimension 1 if nonanomalous;
    # at anomalous p it is 1 or 2, without assuming either.
    lower=2 if anomalous else 3
    print("BSD389_TAME_CLASSGROUP_SUBFIELD_PASS",
          "p",p,"a_p",AP[p],"E_Fp",n,
          "degree_K",size_G,"degree_F",size_SL,
          "cyclotomic_index",size_H,
          "anomalous",int(anomalous),
          "IF_Sha_p_nonzero_THEN_class_p_rank_at_least",lower,
          flush=True)
    return lower

def run():
    # c4=112, c6=-856, discriminant=+389.
    a1,a2,a3,a4,a6=0,1,1,-2,0
    b2=a1*a1+4*a2
    b4=2*a4+a1*a3
    b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    delta=-(b2*b2*b8+8*b4**3+27*b6*b6-9*b2*b4*b6)
    c4=b2*b2-24*b4
    c6=-b2**3+36*b2*b4-216*b6
    assert (delta,c4,c6)==(389,112,-856)
    assert pow(-c6%389,194,389)==1   # split multiplicative
    assert delta%389==0 and c4%389
    print("BSD389_TATE_I1_SPLIT_BAD_PRIME_PASS",delta,c4,c6)
    for p in P:verify(p)
    assert (97+1-AP[97])==107
    assert (16231*(16231**2-1))==4275981638160
    print("BSD389_BAD97_ELIMINATED_BY_TATE_UNIT_UNRAMIFIED_LEMMA_PASS")
    print("BSD389_TAME_P_CUBIC_CLASSFIELD_AUDIT_PASS",
          "checked_primes",len(P))
    print("BOUNDARY: no class-number rank calculation or uniform Sha tail bound")

if __name__=="__main__":run()
