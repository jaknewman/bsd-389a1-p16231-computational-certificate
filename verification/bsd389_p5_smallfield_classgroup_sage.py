#!/usr/bin/env sage -python
"""Actual E389a1 p5 dual-isogeny character field, degree 24.

Invocation on a Sage 10.9+ system:
  sage -python verification/bsd389_p5_smallfield_classgroup_sage.py
  sage -python verification/bsd389_p5_smallfield_classgroup_sage.py --classgroup

First invocation constructs the exact degree-24 number field and
checks Galois-character degrees. --classgroup requests a proven class
group; this may be computationally heavy. NO actual class number was
computed by the assistant in its Sage-free runtime.

Theorem: if v5(h(L5))<=2, then Sha(E389a1/Q)[5^infty]=0,
which is already independently known at p5.
"""
import argparse
from sage.all import QQ, ZZ, PolynomialRing, NumberField, EllipticCurve

parser=argparse.ArgumentParser()
parser.add_argument('--classgroup',action='store_true')
args=parser.parse_args()

Rt=PolynomialRing(QQ,'T'); T=Rt.gen()
u=T*T+10*T+5
K=NumberField((389*u**3-1404928*T).monic(),'t')
t=K.gen()
assert K.degree()==6

E=EllipticCurve(K,[0,0,0,-3024,46224])
R=PolynomialRing(K,'X'); X=R.gen()
u=t*t+10*t+5
w=t*t+4*t-1
e=t*t+22*t+89
h=X**2-321*u/(7*w)*X+1008*e/u
assert h.is_irreducible()
phi=E.isogeny(h)
assert phi.degree()==5
Ep=phi.codomain()
hat=phi.dual()
assert hat.degree()==5
hd=hat.kernel_polynomial()
assert hd.degree()==2 and hd.is_irreducible()
print("E389A1_TRUE_DUAL5_KERNEL_QUADRATIC_PASS",flush=True)

# Dual kernel W is the quotient E[5]/C: character image F5^x,
# so its x-coordinate extension has degree2, y adds another degree2.
Kx=K.extension(hd,'xk')
xk=Kx.gen()
a1,a2,a3,a4,a6=[Kx(z) for z in Ep.ainvs()]
D=(a1*xk+a3)**2 + 4*(xk**3+a2*xk**2+a4*xk+a6)
Rz=PolynomialRing(Kx,'Z'); Z=Rz.gen()
hy=Z**2-D
assert hy.is_irreducible()
Lrel=Kx.extension(hy,'yk')
assert Lrel.absolute_degree()==24
L=Lrel.absolute_field('z')
assert L.degree()==24
print("E389A1_TRUE_DUAL_KERNEL_CHARACTER_FIELD_DEGREE24_PASS",flush=True)
print("DEGREE24_DEFINING_POLYNOMIAL",L.defining_polynomial(),flush=True)

if args.classgroup:
    Cl=L.class_group(proof=True)
    hL=ZZ(Cl.order())
    vp=hL.valuation(5)
    print("PROVED_L5_CLASS_NUMBER",hL,flush=True)
    print("PROVED_L5_CLASS_NUMBER_V5",vp,flush=True)
    if vp<=2:
        print("SHA5_VANISHING_SMALL_CLASS_FIELD_GATE_PASS",flush=True)
    else:
        print("SHA5_SMALL_CLASS_FIELD_GATE_INCONCLUSIVE",flush=True)
else:
    print("CLASS_GROUP_NOT_COMPUTED_RUN_WITH_--classgroup_TO_REQUEST",flush=True)
print("NO_NEW_SHA_PRIME_OR_GLOBAL_BSD_CONCLUSION")
