#!/usr/bin/env python3
"""BSD389 p=16231: two DIFFERENT Sage 10.9 p-adic height algorithms.

The old arithmetic certificate called E.padic_regulator(p), whose
implementation uses E.padic_height(p) and the default basis. This
independent audit builds the height matrix directly by polarization
and, crucially, recomputes ALL its entries using an ALTERNATE
Harvey multiplication-based p-adic height algorithm. The determinant
must match 1930*p^3 mod p^4, giving B_p/p == 9534 mod p.

No historical V56 regulator output or certificate file is read.
Uses Sage's p-adic implementation for the underlying height series,
but TWO DIFFERENT code paths, not independent from Sage itself.
"""
import time
from sage.all import EllipticCurve, Integer, Qp, ZZ

P=Integer(16231)
PREC=6

def verify(flag, ok, info=""):
    if not ok: raise AssertionError(flag+" "+str(info))
    print(flag, info, flush=True)

def valuation_and_residue_mod(x):
    verify("HEIGHT_INTEGRAL_PASS", x.valuation()>=0, str(x.valuation()))
    return int(ZZ(x.lift())%(P**5))

def height_matrix_from_points(name,E,P0,Q0,height):
    start=time.monotonic()
    hP=height(P0)
    hQ=height(Q0)
    hPlus=height(P0+Q0)
    hMinus=height(P0-Q0)
    modulus=int(P**5)
    entries=[valuation_and_residue_mod(h) for h in (hP,hQ,hPlus,hMinus)]
    a,b,c,d=entries
    verify("HEIGHT_PARALLELOGRAM_"+name+"_PASS",
           (c+d-2*a-2*b)%modulus==0)
    off=(c-a-b)*pow(2,-1,modulus)%modulus
    determinant=(a*b-off*off)%modulus
    verify("HEIGHT_DET_VALUATION_"+name+"_PASS",
           determinant%(P**3)==0 and determinant%(P**4)!=0)
    coefficient=determinant//int(P**3)%int(P)
    verify("HEIGHT_DETERMINANT_"+name+"_PASS",
           coefficient==1930,
           "Reg/p^3 mod p="+str(coefficient))
    print("HEIGHT_ALGORITHM_TIME",name,round(time.monotonic()-start,3),
          "hP",a,"hQ",b,"hPplusQ",c,"hPminusQ",d,"off",off,
          "det_mod_p5",determinant,flush=True)
    return entries,determinant

def main():
    E=EllipticCurve("389a1")
    assert E.conductor()==389 and E.is_good(P) and E.is_ordinary(P)
    assert E.ap(P)==128
    assert E.rank(proof=True)==2 and E.torsion_order()==1
    basis=E.gens()
    verify("REGULATOR_BASIS_RANK2_PASS",len(basis)==2,str(basis))
    assert callable(getattr(E,"padic_height_via_multiply",None)), (
        "Sage build lacks alternative padic_height_via_multiply")
    print("INDEPENDENT_REGULATOR_ALGORITHM_START","prec",PREC,
          "p",P,flush=True)

    h_sigma=E.padic_height(P,prec=PREC)
    vals1,d1=height_matrix_from_points("SIGMA",E,*basis,h_sigma)

    # DIFFERENT algorithmic route; E2-based multiply algorithm,
    # rather than the p-adic sigma-height used by padic_regulator.
    h_mult=E.padic_height_via_multiply(P,prec=PREC)
    vals2,d2=height_matrix_from_points("MULTIPLY",E,*basis,h_mult)
    verify("INDEPENDENT_HEIGHT_VALUES_AGREE_MODP5_PASS",vals1==vals2)
    verify("INDEPENDENT_REGULATOR_ALGORITHMS_AGREE_MODP5_PASS",d1==d2)

    K=Qp(P,prec=10)
    lp=E.padic_lseries(P,implementation="eclib")
    alpha=K(lp.alpha(prec=10))
    assert int(alpha.residue())==128
    reg=K(d2)
    assert reg.valuation()==3
    assert int((reg/K(P**3)).residue())==1930

    B=(reg*(1-alpha**(-1))**2
         *K(E.tamagawa_product())/
         (K(E.torsion_order())**2*K(1+P).log()**2))
    verify("INDEPENDENT_REGULATOR_B_FACTOR_VALUATION_PASS",
           B.valuation()==1,str(B.valuation()))
    digit=int((B/K(P)).residue())
    verify("INDEPENDENT_REGULATOR_B_OVER_P_9534_PASS",
           digit==9534,"B/p mod p="+str(digit))
    print("BSD389_REGULATOR_ALTERNATE_HEIGHT_METHODS_PASS",flush=True)
    print("BOUNDARY: two alternate Sage height algorithms share Sage's "
          "global arithmetic and p-adic math; this does not compute L_p "
          "or Sha.p_primary_bound.",flush=True)

if __name__=="__main__":
    main()
