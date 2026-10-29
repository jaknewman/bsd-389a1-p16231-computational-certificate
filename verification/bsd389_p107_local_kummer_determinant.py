#!/usr/bin/env python3
"""Independent arithmetic certificate for the 107-local Mordell--Weil determinant.

No Sage, eclib, modular symbols, Kurihara archive, or conjectural BSD inputs.
Checks by exhaustive exact Legendre-symbol counting at two primes, then exact
elliptic-group arithmetic on y^2 + y = x^3 + x^2 - 2*x.

OUTPUT: local MW mod 107 isomorphism. It does NOT prove Sel_107 is the same
as local MW without an additional global Selmer comparison theorem.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

P = 107
QS = [369793, 383917]
GENERATORS = ((0, 0), (1, 0))

def check(condition, message):
    if not condition:
        raise AssertionError(message)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def point_count(q):
    # Completing the square: (2*y+1)^2=1+4*(x^3+x^2-2*x).
    total = q + 1
    for x in range(q):
        disc = (1 + 4 * (x*x*x + x*x - 2*x)) % q
        leg = pow(disc, (q-1)//2, q) if disc else 0
        if leg == 1:
            total += 1
        elif leg == q-1:
            total -= 1
        else:
            check(leg == 0, "unexpected Legendre symbol")
    return total


def belongs(R, q):
    if R is None:
        return True
    x, y = R
    return (y*y + y - x*x*x - x*x + 2*x) % q == 0


def add(A, B, q):
    if A is None:
        return B
    if B is None:
        return A
    x1, y1 = A
    x2, y2 = B
    if x1 == x2 and (y1+y2+1) % q == 0:
        return None
    if A == B:
        denom = (2*y1+1) % q
        check(denom != 0, "doubling denominator zero")
        lam = ((3*x1*x1+2*x1-2) * pow(denom,-1,q)) % q
    else:
        denom = (x2-x1) % q
        check(denom != 0, "distinct-point denominator zero")
        lam = ((y2-y1)*pow(denom,-1,q)) % q
    nu = (y1-lam*x1) % q
    x3 = (lam*lam - 1 - x1 - x2) % q
    y3 = (-lam*x3 - nu - 1) % q
    R=(x3,y3)
    check(belongs(R,q),"sum is not on curve")
    return R


def multiply(n, A, q):
    check(n >= 0, "negative scalar")
    R = None
    while n:
        if n & 1:
            R = add(R,A,q)
        A = add(A,A,q)
        n >>= 1
    return R


def basis_coordinates(q,N):
    check(N % P == 0 and (N//P) % P != 0, "p must divide #E(Fq) exactly once")
    A = multiply(N//P, GENERATORS[0], q)
    B = multiply(N//P, GENERATORS[1], q)
    check(A is not None or B is not None, "both local Kummer values zero")
    T = A if A is not None else B
    check(multiply(P,T,q) is None, "T is not p-torsion")
    check(multiply(P,A,q) is None and multiply(P,B,q) is None, "invalid local point")
    table={}
    R=None
    for j in range(P):
        check(R not in table, "noninjective discrete log table")
        table[R]=j
        R=add(R,T,q)
    check(R is None and len(table)==P, "T does not have order p")
    check(A in table and B in table,"p-torsion not cyclic as expected")
    return {"q":q,"cardinality":N,"P_times_cofactor":A,
            "Q_times_cofactor":B,"basis_T":T,
            "row":[table[A],table[B]]}


def main():
    check(is_prime(P), "p is not prime")
    records=[]
    for q in QS:
        check(is_prime(q), "q is not prime")
        check(q % P == 1, "q not 1 mod p")
        check(all(belongs(A,q) for A in GENERATORS),"generator not on curve")
        N=point_count(q)
        ap=q+1-N
        check(ap % P == (q+1) % P, "not a Kurihara auxiliary prime")
        rec=basis_coordinates(q,N)
        rec["ap"]=ap
        records.append(rec)
        print("P107_LOCAL_DIRECT_POINTCOUNT_PASS", q, "cardinality",N,
              "a_q",ap,flush=True)
        print("P107_LOCAL_MULTIPLES",q,"[N/p]P",rec["P_times_cofactor"],
              "[N/p]Q",rec["Q_times_cofactor"],flush=True)
        print("P107_LOCAL_COORDINATE_ROW",q,rec["row"],flush=True)
    rows=[r["row"] for r in records]
    determinant=(rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0]) % P
    check(rows==[[1,58],[1,3]], "independent row values differ from verified target")
    check(determinant==52,"local determinant incorrect")
    print("P107_LOCAL_MORDELL_WEIL_DETERMINANT_NONZERO_PASS",determinant,
          "mod",P,flush=True)
    print("P107_MW_MOD_P_TO_TWO_LOCAL_GROUPS_ISOMORPHISM_PASS",flush=True)
    print("BOUNDARY: a local MW determinant does not bound Sha or prove the",
          "full Selmer localization map is injective; Kim+Kurihara is separate.",flush=True)
    data={"curve":"389a1","model":[0,1,1,-2,0],"p":P,
          "generators":[list(x) for x in GENERATORS],
          "records":records,"matrix":rows,"determinant_mod_p":determinant,
          "sha_conclusion_from_this_program":False}
    path=Path.home()/"bsd389_p107_local_kummer_determinant.json"
    path.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
    print("P107_LOCAL_REPORT",path,flush=True)

if __name__=='__main__':
    main()