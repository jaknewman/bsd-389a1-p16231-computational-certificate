#!/usr/bin/env python3
"""Independent q-only reduced Tate prediction at p=19 for E389a1.

NO modular symbols or two-prime Kurihara data are used for the prediction.
The C++ companion independently evaluates the complete genuine global sum.
Run from any cwd: python verification/bsd389_iltr_p19_reduced_tate_holdout_gate.py
"""
from bsd389_local_reduced_Tate_weights_independent import weight, add, mul, count_points

def local_row(q,p):
    n=count_points(q)
    assert n%p==0 and n%(p*p)!=0
    P=(q-1,1); Q=(0,q-1)
    A=mul(P,n//p,q)
    B=mul(Q,n//p,q)
    if A is None:
        assert B is not None
        return (0,1)
    for j in range(p):
        if mul(A,j,q)==B:
            return (1,j)
    raise AssertionError("rational points do not span a local cyclic quotient")

def main():
    p=19
    q1,q2=2243,3877
    n1,n2=count_points(q1),count_points(q2)
    assert n1==2261 and n2==3781
    v1,v2=local_row(q1,p),local_row(q2,p)
    assert v1==(1,1) and v2==(0,1), (v1,v2)
    w1=weight(q1,p,True)
    w2=weight(q2,p,True)
    assert (w1,w2)==(17,18),(w1,w2)
    det=(v1[0]*v2[1]-v1[1]*v2[0])%p
    prediction=2*w1*w2*det*det%p
    assert det==1 and prediction==4
    print("P19_INDEPENDENT_REDUCED_TATE_PREDICTION_PASS",
          "q1",q1,"q2",q2,"orders",n1,n2,
          "local_rows",v1,v2,"weights",(w1,w2),
          "det",det,"prediction_mod19",prediction)
    print("SCOPE: LOCAL arithmetic only; verify global delta independently in native C++")

if __name__=="__main__":
    main()
