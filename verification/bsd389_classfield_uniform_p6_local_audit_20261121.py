#!/usr/bin/env python3
"""Verify local arithmetic input for E389a1 class-field p^4/p^6 criterion.

No class group of Q(E[p]) is calculated; the theorem in paper/
bsd389_uniform_classfield_p6_division_field_obstruction_20261121.md
is mathematical, not a numerical claim that class numbers avoid p^6.
"""
from math import gcd
SAMPLES=(5,7,11,17,23,97,107,599,859,1213,1493,1951,16231)
EXPECTED={5:-3,7:-5,11:-4,17:-6,23:-4,107:0,599:0,
          859:1,1213:1,1493:1,1951:1,16231:128}

def ap(p):
    result=0
    for x in range(p):
        D=(1+4*(x*x*x+x*x-2*x))%p
        if D:
            s=pow(D,(p-1)//2,p)
            assert s in (1,p-1)
            result+=1 if s==1 else -1
    return -result

def run():
    a1,a2,a3,a4,a6=0,1,1,-2,0
    b2=a1*a1+4*a2
    b4=2*a4+a1*a3
    b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    delta=-(b2*b2*b8+8*b4**3+27*b6*b6-9*b2*b4*b6)
    c4=b2*b2-24*b4
    c6=-b2**3+36*b2*b4-216*b6
    assert (delta,c4,c6)==(389,112,-856)
    assert c4%389 and pow(-c6%389,194,389)==1
    assert 388==4*97 and gcd(388,389)==1
    print("BSD389_SPLIT_MULTIPLICATIVE_I1_TORUS_PASS",
          "delta",delta,"c4",c4,"c6",c6,"torus_order",388)
    for p in SAMPLES:
        assert p>=5 and p!=389
        a=ap(p)
        if p in EXPECTED: assert a==EXPECTED[p],(p,a)
        Np=p+1-a
        anomalous=Np%p==0
        if p==97:
            print("BSD389_SPECIAL_TORUS_EXCEPTION",p)
        else:
            # Necessary *consequence* of proved class-field lemma,
            # not a purported computation of h(Q(E[p])).
            v=4 if anomalous else 6
            print("BSD389_CLASSFIELD_NECESSARY_DIVISIBILITY",
                  "p",p,"a_p",a,"E_Fp",Np,
                  "anomalous",anomalous,
                  "IF_Sha_p_nonzero_THEN_vp_hK_ge",v)
    print("BSD389_CLASSFIELD_LOCAL_PRECONDITIONS_PASS")
    print("BOUNDARY: no class-number upper bound or global Sha finiteness")

if __name__=="__main__":run()
