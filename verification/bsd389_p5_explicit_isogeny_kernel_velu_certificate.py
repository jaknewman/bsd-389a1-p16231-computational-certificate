#!/usr/bin/env python3
"""389a1: exact K5 quadratic order-5 kernel + Velu codomain verification.

K5=Q[t]/(389(t²+10t+5)^3-1404928t), degree 6.
Everything is exact rational polynomial arithmetic in K5. No Sage required,
but SymPy is required. This constructs a genuine isogeny, NOT its Selmer group.
"""
import sympy as s
t,X=s.symbols("t X")
u=t*t+10*t+5
v=t*t+22*t+125
w=t*t+4*t-1
e=t*t+22*t+89
vp=t*t+250*t+3125
wp=t*t-500*t-15625
f=389*u**3-1404928*t
F=s.Poly(f,t,domain=s.QQ).monic()
assert F.is_irreducible
K=lambda z:s.Poly(z,t,domain=s.QQ).rem(F)
mul=lambda a,b:(a*b).rem(F)
inv=lambda a:s.invert(a,F)
zero,one=K(0),K(1)
uin,win,tin=inv(K(u)),inv(K(w)),inv(K(t))
a=mul(K(-s.Rational(321,7)*u),win)
b=mul(K(1008*e),uin)
A,B=-3024,46224
def reduce_x(poly):
    P=s.Poly(poly,X)
    r0,r1=one,zero
    z0,z1=zero,zero
    for n in range(P.degree()+1):
        c=P.nth(n)
        z0=(z0+c*r0).rem(F)
        z1=(z1+c*r1).rem(F)
        r0,r1=mul(-b,r1),(r0-mul(a,r1)).rem(F)
    return z0,z1
psi3=3*X**4+6*A*X**2+12*B*X-A*A
psi4div=(X**6+5*A*X**4+20*B*X**3-5*A*A*X**2
         -4*A*B*X-8*B*B-A**3)
psi5=32*(X**3+A*X+B)**2*psi4div-psi3**3
assert s.Poly(psi5,X).LC()==5
assert reduce_x(psi5)==(zero,zero)
print("P5_GENUINE_E389A1_ORDER5_KERNEL_PSI5_DIVISIBILITY_PASS",flush=True)
# Duplication swaps the two roots of h=X²+a X+b.
N2=X**4-2*A*X**2-8*B*X+A*A
D2=4*(X**3+A*X+B)
n0,n1=reduce_x(N2)
d0,d1=reduce_x(D2)
assert (n0-mul(b,d1)+mul(a,d0)).rem(F)==zero
assert (n1+d0).rem(F)==zero
assert d0!=zero or d1!=zero
print("P5_GENUINE_E389A1_KERNEL_CYCLIC_DUPLICATION_PASS",flush=True)
# Velu on ±P,±2P, using symmetric sums of their two distinct x's.
s1,s2=-a,b
sum2=(mul(s1,s1)-2*s2).rem(F)
sum3=(mul(mul(s1,s1),s1)-3*mul(s1,s2)).rem(F)
T=(2*(3*sum2+2*K(A))).rem(F)
W=(2*(5*sum3+3*A*s1+4*K(B))).rem(F)
Ap=(K(A)-5*T).rem(F)
Bp=(K(B)-7*W).rem(F)
assert Ap==mul(K(-3024*vp),uin)
assert Bp==mul(K(46224*wp),win)
print("P5_GENUINE_E389A1_VELU_CODOMAIN_PASS",flush=True)
# Fricke j-invariant of E'=E/C
jnum=(1728*4*mul(mul(Ap,Ap),Ap)).rem(F)
jden=(4*mul(mul(Ap,Ap),Ap)+27*mul(Bp,Bp)).rem(F)
assert jden!=zero
jprime=mul(jnum,inv(jden))
jformula=mul(K(vp**3),mul(mul(tin,tin),mul(mul(tin,tin),tin)))
assert jprime==jformula
print("P5_EXACT_TARGET_FRICKE_J_PASS",flush=True)
print("CONSTRUCTED K5_DEGREE=6 KERNEL_DEGREE=2 ISOGENY_DEGREE=5")
print("SCOPE: NO ISOGENY SELMER, SHA OR COMPLEX BSD COMPUTED")
