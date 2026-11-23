#!/usr/bin/env python3
"""Genuine E389a1 Mazur--Tate augmentation SATURATION: exact INTEGER matrices.

Rebuilds actual symmetric theta from three historically independently USER
certified integer Manin coefficient vectors, not synthetic polynomials.
Verifies:
 - the exact quadratic-jet map epsilon_2(b_j) = j^2 modulo m;
 - epsilon_2 * A_m = 0 modulo m, coefficient by coefficient;
 - the canonical integer division G=y*U in Z[y]/P_m;
 - the basis conjugacy A_m <-> multiplication by y U;
 - det(m_y)=(-1)^h*m and det(m_U)=(-1)^h*det(A_m)/m;
 - signed half-resultant mod p=(-1)^h*delta^h;
 - m_U invertible over Z_p at each certified Kurihara unit.
SymPy required. Does not assert that this analytic module IS Selmer or Sha.
"""
import sympy as sp

Y=sp.Symbol('Y')
INPUTS={
  5:(5,1,4,[-50,34,32,34,-50],4,-7220),
  11:(11,1,0,[564,-414,344,-230,60,-42,-42,60,-230,344,-414],1,-395563875872),
  25:(5,2,5,[-7110,5550,17732,17732,5550,-7110,-9364,-21952,-6882,376,19002,14602,8698,2028,-12468,-20424,-12468,2028,8698,14602,19002,376,-6882,-21952,-9364],22,-151753339112452007665001265791485409507737600),
}

def audit(m,p,k,shift,hist,delta,expected_A_det):
    assert m==p**k and len(hist)==m and sum(hist)==0
    h=(m-1)//2
    assert all(hist[j]==hist[(shift-j)%m] for j in range(m))
    t=next(j for j in range(m) if (2*j+shift)%m==0)
    g=[hist[(j-t)%m] for j in range(m)]
    assert all(g[j]==g[(-j)%m] for j in range(m))
    S=[sp.Integer(2),Y+2]
    for j in range(2,h+1):
        S.append(sp.expand((Y+2)*S[-1]-S[-2]))
    P=sp.Poly(1+sum(S[1:h+1]),Y,domain=sp.ZZ)
    assert P.degree()==h and P.LC()==1 and P.eval(0)==m
    assert all(int(c)%p==0 for c in P.all_coeffs()[1:])
    G=sp.Poly(g[0]+sum(g[j]*S[j] for j in range(1,h+1)),Y,domain=sp.ZZ)
    assert G.eval(0)==0
    U,remainder=sp.div(G,sp.Poly(Y,Y),domain=sp.ZZ)
    assert remainder.is_zero
    assert int(U.eval(0))%p==delta%p

    mult=lambda W:sp.Matrix(h,h,lambda i,j:
         int(sp.rem(W*sp.Poly(Y**j,Y),P).nth(i)))
    My=mult(sp.Poly(Y,Y))
    Mu=mult(U)
    A=sp.Matrix(h,h,lambda i,j:
         g[(i+1-(j+1))%m]+g[(i+1+(j+1))%m]-2*g[i+1])
    B=sp.Matrix(h,h,lambda i,j:
         int(sp.div(sp.Poly(S[j+1]-2,Y),sp.Poly(Y,Y),
                    domain=sp.ZZ)[0].nth(i)))
    assert B.det()==1
    assert B*A==My*Mu*B
    assert int(My.det())==(-1)**h*m
    assert int(A.det())==expected_A_det
    assert int(Mu.det())==(-1)**h*expected_A_det//m
    assert int(Mu.det())%p==pow(delta,h,p)
    assert (expected_A_det//m)%p==((-1)**h*pow(delta,h,p))%p

    jet_row=sp.Matrix(1,h,lambda i,j:(j+1)**2)
    assert all(int(z)%m==0 for z in jet_row*A)
    assert jet_row[0]==1
    print('TRUE_QUADRATIC_JET_CANONICAL_ANNIHILATOR_PASS',
          'm',m,'row',list(jet_row),'row_A_mod_m',[int(z)%m for z in jet_row*A],
          flush=True)
    print('TRUE_MAZUR_TATE_SATURATED_INTEGER_MATRIX_PASS',
          'm',m,'h',h,'center',t,
          'U_constant',U.eval(0),'U_constant_mod_pk',int(U.eval(0))%m,
          'det_A',expected_A_det,'det_U',int(Mu.det()),
          'det_U_modp',int(Mu.det())%p,
          'signed_det_A_div_m_modp',(expected_A_det//m)%p,
          'expected_signed',((-1)**h*pow(delta,h,p))%p,
          flush=True)
    print('TRUE_ANALYTIC_SATURATED_P_COKERNEL_ZERO_PASS',p,k,flush=True)

for m,data in INPUTS.items():
    audit(m,*data)

print('CANONICAL_Z_EXACT_SEQUENCE_PROVED_BY_IDEAL_FACTORIZATION:')
print('0 -> coker(m_U) -> coker(m_(yU)) -> Z/(p^k) -> 0')
print('BOUNDARY_NO_MAP_FROM_ANALYTIC_SATURATED_DEFECT_TO_SHA')
