#!/usr/bin/env python3
"""Local Kummer size and cyclotomic congruences for the curve 389a1.

Pure Python exact finite arithmetic. Does not establish an automorphic
congruence, a global Selmer inequality, Sha finiteness or BSD.
"""
PRIMES = (5, 7, 11, 107, 599, 16231)
KNOWN_AP = {5: -3, 7: -5, 11: -4, 107: 0, 599: 0, 16231: 128}

def ap_legendre(p):
    # y^2+y=f(x), discriminant 1+4f(x).
    total = 0
    for x in range(p):
        f = (x*x*x+x*x-2*x) % p
        d = (1+4*f) % p
        if d:
            s = pow(d, (p-1)//2, p)
            assert s in (1, p-1)
            total += (1 if s == 1 else -1)
    return -total

def run():
    checks = 0
    for p in PRIMES:
        a = ap_legendre(p)
        assert a == KNOWN_AP[p], (p,a)
        cardinal = p+1-a
        assert cardinal % p != 0, (p, cardinal)
        for n in (1, 2, 3, 4):
            k = (p-1)*p**(n-1)
            pn = p**n
            assert pow(1+p, k, pn) == 1
            assert pow(1+p, k, pn*p) == (1-pn)%(pn*p)
            for u in (2,3,5,7,11,13,17,19,23):
                if u%p:
                    assert pow(u, k, pn) == 1
                    checks += 1
            # For p >= 5, p != 389, kernel E_1(Q_p) = Z_p.
            # Since p does not divide #E(F_p), the reduction quotient
            # is p-divisible, whence E(Q_p)/p^n = Z/p^n.
            print("LOCAL_KUMMER_PASS", "p",p, "n",n,
                  "ap",a, "E_Fp",cardinal,
                  "KUMMER_ORDER",pn, "KUMMER_LENGTH",n)
    print("LOCAL_REGULARIZED_TOWER_PASS", "checked_units", checks,
          "primes",len(PRIMES), "levels",4)
    print("BOUNDARY: intrinsic finite-level Bloch-Kato local conditions "
          "for regularized twists were NOT identified with Kummer; "
          "no global Selmer bound or BSD proof.")

if __name__ == "__main__":
    run()
