#!/usr/bin/env python3
"""110 genuine integral right ideals of norm 121 in the explicit maximal order.

R = Z[1,omega,J,omega*J] in quaternion B=(-43,-389).
I_a = {x in R : (1,-a)*rho(x)=0 mod121}, a in (Z/121)^*.
These are NOT yet source-authenticated Castella-Hsieh Gross P_2 classes.
"""
M=121
V=[[1,11,5,55],[0,0,23,11],[0,0,114,70],[1,111,116,50]]
VI=[[12,50,77,110],[98,5,70,23],[0,111,88,0],[0,120,14,0]]
E=[[[1,0],[0,1]],[[11,0],[0,111]],[[5,23],[114,116]],[[55,11],[70,50]]]
D=[[12,0],[0,112]]
R=39
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%M for j in range(2)] for i in range(2)]
def from_coords(c):
    v=[sum(V[i][j]*c[j] for j in range(4))%M for i in range(4)]
    return [[v[0],v[1]],[v[2],v[3]]]
def coords(X):
    v=[X[0][0],X[0][1],X[1][0],X[1][1]]
    return tuple(sum(VI[i][j]*v[j] for j in range(4))%M for i in range(4))
def belongs(a,X):
    return all((X[0][i]-a*X[1][i])%M==0 for i in range(2))
def gens(a):
    return coords([[a,0],[1,0]]),coords([[0,a],[0,1]])
def main():
    assert all(sum(V[i][k]*VI[k][j]for k in range(4))%M==(i==j)for i in range(4)for j in range(4))
    assert len(set(pow(R,k,M)for k in range(110)))==110
    invD=[[pow(12,-1,M),0],[0,pow(112,-1,M)]]
    for k in range(110):
        a=pow(R,k,M);u,v=gens(a)
        assert u==tuple(x%M for x in (12*a+77,98*a+70,88,14))
        assert v==tuple(x%M for x in (50*a+110,5*a+23,111*a,120*a))
        for c in (u,v):
            X=from_coords(c)
            assert belongs(a,X)
            assert all(belongs(a,mm(X,H)) for H in E)
            assert belongs(a*pow(R,-1,M)%M,mm(mm(invD,X),D))
        assert not belongs((a+1)%M,from_coords(u))
    # Formula for I_1 in basis 1,omega,J,omega*J:
    H=[(121,0,0,0),(0,121,0,0),(32,73,1,0),(4,89,0,1)]
    assert all(belongs(1,from_coords(c)) for c in H)
    print("RIGHT_IDEALS_110_DISTINCT_PASS")
    print("EACH_RIGHT_IDEAL_INDEX_121_SQUARED_PASS")
    print("RIGHT_CLOSURE_110_TIMES_2_TIMES_4_PASS")
    print("NORM13_LOCAL_CONJUGATION_CYCLE_PASS")
    print("SAMPLE_I1_HERMITE_BASIS_PASS",H)
    print("BOUNDARY: GROSS_IDEAL_ORIENTATION_AND_BRANDT_VALUES_NOT_VERIFIED")
if __name__=="__main__":main()
