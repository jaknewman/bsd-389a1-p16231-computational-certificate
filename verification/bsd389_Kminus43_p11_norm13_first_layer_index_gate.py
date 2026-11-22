#!/usr/bin/env python3
"""K=-43, p=11: norm-13 ring-class first layer, explicit quaternion p-chart.

No Gross weights are computed; optional CSV must provide all 110 externally
authenticated p-stabilized weights, indexed by (1+omega)^k, k=0..109.
"""
import argparse
import csv

P=11; M=121
ROOTS=(11,111)
R=39 # (1+omega) has local ratio (12/112) mod121.

def norm(a,b):
    return a*a+a*b+11*b*b

def ratio(a,b):
    x=(a+b*ROOTS[0])%M
    y=(a+b*ROOTS[1])%M
    if x%P==0 or y%P==0: raise ValueError("nonunit")
    return x*pow(y,-1,M)%M

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2))%M
             for j in range(2)] for i in range(2)]

def verify():
    # Class number 1: Minkowski bound (2/pi)*sqrt(43)<5;
    # 2 and 3 are inert; the norm-4 ideal (2) is principal.
    assert (-43)%8==5 and (-43)%3==2
    assert all((x*x-x+11)%M==0 for x in ROOTS)
    assert (ROOTS[0]-ROOTS[1])%P!=0
    assert norm(1,1)==13 and ratio(1,1)==R
    assert pow(R,110,M)==1
    assert [pow(R,k,M) for k in (10,22,55)] == [111,3,120]
    assert len({pow(R,k,M) for k in range(110)})==110
    assert ratio(10,11)==12 and norm(10,11)==1541
    assert pow(R,100,M)==12 and 100%11==1
    # At 389 symbol (-43/389)=-1; at 43 (-389/43)=+1;
    # at 2, odd units 5 & 3 give Hilbert symbol +1; infinity ramifies.
    assert pow((-43)%389,194,389)==388
    assert pow((-389)%43,21,43)==1
    assert (-43)%8==5 and (-389)%8==3
    i=[[21,0],[0,-21]]
    j=[[0,1],[-389,0]]
    I=[[1,0],[0,1]]
    assert matmul(i,i)==[[(-43)%M,0],[0,(-43)%M]]
    assert matmul(j,j)==[[(-389)%M,0],[0,(-389)%M]]
    ij=matmul(i,j);ji=matmul(j,i)
    assert all((ij[a][b]+ji[a][b])%M==0
               for a in range(2) for b in range(2))
    half=pow(2,-1,M)
    omega=[[(I[a][b]+i[a][b])*half%M for b in range(2)]
           for a in range(2)]
    pi=[[(3*I[a][b]+i[a][b])*half%M for b in range(2)]
        for a in range(2)]
    assert omega==[[11,0],[0,111]]
    assert pi==[[12,0],[0,112]]
    assert pi[0][0]*pi[1][1]%M==13
    assert pi[0][0]*pow(pi[1][1],-1,M)%M==R
    fibers=[[k+11*j for j in range(10)] for k in range(11)]
    assert set(sum(fibers,[]))==set(range(110))
    print("NORM13_FULL_RINGCLASS_C110_PASS",R)
    print("KMINUS43_QUATERNION_DISC389_SPLIT_CHART_PASS",omega,pi)
    print("ELEVEN_10_CLASS_FIBERS_PASS")
    return fibers

def moments(weights):
    if set(weights)!=set(range(110)):raise ValueError("Need all 110 weights")
    c=[sum(weights[i+11*j] for j in range(10))%11 for i in range(11)]
    return c,(sum(c)%11, sum(i*c[i] for i in range(11))%11,
              sum(i*(i-1)//2*c[i] for i in range(11))%11)

def read_csv(path):
    weights={}
    with open(path,encoding="utf-8",newline="") as stream:
        for row in csv.reader(stream):
            if not row or row[0].startswith("#"):continue
            if len(row)!=2: raise ValueError("CSV k,weight required")
            k,w=map(int,row)
            if not 0<=k<110 or k in weights:raise ValueError("duplicate/bad k")
            weights[k]=w
    return weights

def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument("--weights-csv")
    a.add_argument("--synthetic-self-test",action="store_true")
    a.add_argument("--list-fibers",action="store_true")
    z=a.parse_args()
    fibers=verify()
    if z.list_fibers:
        for i,f in enumerate(fibers):
            print("FIBER",i,[(k,pow(R,k,M)) for k in f])
    if z.synthetic_self_test:
        w={k:0 for k in range(110)}
        w[0],w[1],w[2]=1,-2,1
        _,m=moments(w)
        assert m==(0,0,1)
        print("SYNTHETIC_THETA_MOMENTS_PASS",m)
        print("NOT_REAL_GROSS_WEIGHTS")
    if z.weights_csv:
        c,m=moments(read_csv(z.weights_csv))
        print("CONDITIONAL_GROUPED_WEIGHTS",c)
        print("CONDITIONAL_MOMENTS_MOD11",m)
        print("NO_GROSS_PROVENANCE_OR_THETA_NORMALIZATION_ASSERTED")

if __name__=="__main__":main()
