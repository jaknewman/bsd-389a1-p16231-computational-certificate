#!/usr/bin/env python3
"""Exact maximal order certificate for B=(-43,-389), p=11. No Gross weights."""
from fractions import Fraction as F

A,B=-43,-389
# Quaternion multiplication in basis 1,i,j,k=ij.
T={(0,0):(1,0),(0,1):(1,1),(0,2):(1,2),(0,3):(1,3),
   (1,0):(1,1),(1,1):(A,0),(1,2):(1,3),(1,3):(A,2),
   (2,0):(1,2),(2,1):(-1,3),(2,2):(B,0),(2,3):(-B,1),
   (3,0):(1,3),(3,1):(-A,2),(3,2):(B,1),(3,3):(-A*B,0)}
def mul(x,y):
    z=[F(0)]*4
    for a in range(4):
        for b in range(4):
            c,k=T[a,b]
            z[k]+=c*x[a]*y[b]
    return tuple(z)
def det(M):
    a=[list(map(F,row)) for row in M]
    v=F(1);n=len(a)
    for k in range(n):
        q=next((i for i in range(k,n) if a[i][k]),None)
        if q is None:return F(0)
        if q!=k:a[k],a[q]=a[q],a[k];v=-v
        d=a[k][k];v*=d
        for i in range(k+1,n):
            t=a[i][k]/d
            for j in range(k+1,n):a[i][j]-=t*a[k][j]
            a[i][k]=0
    return v
def in_basis(E,z):
    A=[[E[j][i] for j in range(4)] for i in range(4)]
    d=det(A)
    return tuple(det([[z[i] if j==k else A[i][j]
                       for j in range(4)] for i in range(4)])/d for k in range(4))
def mm(X,Y,m=121):
    return [[sum(X[i][k]*Y[k][j] for k in range(2))%m for j in range(2)]for i in range(2)]
def main():
    e0=(F(1),F(0),F(0),F(0))
    w=(F(1,2),F(1,2),F(0),F(0))
    J=(F(0),F(16,43),F(0),F(1,43))
    E=[e0,w,J,mul(w,J)]
    for x in E:
        for y in E:
            assert all(q.denominator==1 for q in in_basis(E,mul(x,y)))
    G=[[2*mul(x,y)[0] for y in E]for x in E]
    assert G==[[2,1,0,-16],[1,-21,-16,-16],[0,-16,-30,-15],[-16,-16,-15,-74]]
    assert det(G)==-389**2
    assert mul(J,J)==tuple(-15*t for t in e0)
    assert pow((-43)%389,194,389)==388
    assert pow((-389)%43,21,43)==1
    I=[[21,0],[0,-21]];K=[[0,1],[-389,0]]
    assert mm(I,I)==[[(-43)%121,0],[0,(-43)%121]]
    assert mm(K,K)==[[(-389)%121,0],[0,(-389)%121]]
    omega=[[11,0],[0,111]]
    Xi=[[5,23],[114,116]]
    assert mm(omega,Xi)==[[55,11],[70,50]]
    charts=[[[1,0],[0,1]],omega,Xi,mm(omega,Xi)]
    V=[[h[i][j] for h in charts] for i,j in [(0,0),(0,1),(1,0),(1,1)]]
    assert det(V)==35600
    Vinv=[[12,50,77,110],[98,5,70,23],[0,111,88,0],[0,120,14,0]]
    assert all(sum(V[i][k]*Vinv[k][j]for k in range(4))%121==(i==j) for i in range(4)for j in range(4))
    assert 12*112%121==13 and 12*pow(112,-1,121)%121==39
    assert pow(39,110,121)==1 and all(pow(39,110//q,121)!=1 for q in (2,5,11))
    print("GLOBAL_MAXIMAL_ORDER_TRACE_DISCRIMINANT_389_PASS",int(det(G)))
    print("ALL_16_INTEGRAL_PRODUCTS_AND_LOCAL_SPLIT_PASS")
    print("NORM13_PI_RATIO39_ORDER110_PASS")
    print("BOUNDARY: NOT YET ACTUAL GROSS WEIGHTS")
if __name__=="__main__":main()
