#!/usr/bin/env python3
"""New (not previously certified) exact formal-log saturation test for E=389a1.
Only standard Python; independent binary and Montgomery-ladder scalar methods.
"""
P=16231
NP=P+1-128
POINTS=[(-1,1),(0,-1)]

def evaluate(prec,algorithm):
    n=P**prec
    i3=pow(3,-1,n)
    A=(-112*i3)%n
    B=(1712*pow(27,-1,n))%n
    O=(1,1,0)
    def curve(t):
        x,y,z=t
        return (y*y-x**3-A*x*z**4-B*z**6)%n==0
    def dbl(t):
        x,y,z=t
        if z==0:return t
        yy=y*y%n
        s=4*x*yy%n
        m=(3*x*x+A*pow(z,4,n))%n
        xx=(m*m-2*s)%n
        return xx,(m*(s-xx)-8*yy*yy)%n,2*y*z%n
    def add(t,u):
        x,y,z=t
        xx,yy,zz=u
        if z==0:return u
        if zz==0:return t
        a=x*zz*zz%n;b=xx*z*z%n
        c=y*pow(zz,3,n)%n;d=yy*pow(z,3,n)%n
        h=(b-a)%n;r=(d-c)%n
        if h==0 and r==0:return dbl(t)
        xxx=(r*r-h**3-2*a*h*h)%n
        return xxx,(r*(a*h*h-xxx)-c*h**3)%n,h*z*zz%n
    def binary(t,k):
        r=O
        while k:
            if k&1:r=add(r,t)
            t=dbl(t)
            k//=2
        return r
    def ladder(t,k):
        r,s=O,t
        for digit in bin(k)[2:]:
            if digit=='0':r,s=dbl(r),add(r,s)
            else:r,s=add(r,s),dbl(s)
        return r
    output=[]
    for x,y in POINTS:
        t=((4*x+4*i3)%n,(8*y+4)%n,1)
        assert curve(t)
        X,Y,Z=(binary if algorithm=="binary" else ladder)(t,NP)
        assert curve((X,Y,Z)) and Y%P!=0 and Z%P==0
        formal=(-2*(X-4*i3*Z*Z)*Z*pow(Y-4*Z**3,-1,n))%n
        assert formal%P==0
        # Original formal-group parameter t=-x/y; omega=dx/(2y+1).
        # Since formal is in p Z_p, log(formal)=formal (mod p^2).
        ell=((formal//P)*pow(NP,-1,P))%P
        output.append((formal%(P*P),ell))
    return output

def main():
    assert NP==16104
    for k in (2,3,4):
        b=evaluate(k,"binary")
        l=evaluate(k,"ladder")
        assert b==l,(k,b,l)
        assert [x[1] for x in b]==[6575,12208]
        print("MW_FORMAL_LOG_DOUBLE_ALGORITHM_PASS",k,b)
    print("MW_LOG_SATURATION_P16231_EXPONENT",0)
    print("MW_LOG_SATURATION_P16231_PRIMITIVE_MODP",12208,-6575)
    print("MW_LOG_SATURATION_P16231_PASS")
    print("BOUNDARY: no global Selmer Fitting, no derived height or full BSD proof")
if __name__=="__main__":main()
