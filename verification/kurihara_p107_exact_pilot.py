#!/usr/bin/env sage -python
"""Exact modular-symbol Kurihara sum, with honest bounded pilots.

Usage:
  sage -python kurihara_p107_exact_pilot.py --limit 1000
  sage -python kurihara_p107_exact_pilot.py --p 5 --auto-small --limit 1000000
  sage -python kurihara_p107_exact_pilot.py --full

The --limit result is a PARTIAL SUM and is NEVER a Kurihara certificate.
Full p=107 is prohibitively expensive without a new algorithm.
"""
import argparse, json, math, time
from sage.all import EllipticCurve, QQ, ZZ, GF, prime_range
from sage.libs.eclib.newforms import ECModularSymbol


def logs_mod_p(q, p):
    """Discrete logs modulo p for every nonzero residue modulo prime q."""
    F = GF(q)
    generator = int(F.multiplicative_generator())
    table = bytearray(q) if p < 256 else [0]*q
    x = 1
    for k in range(q-1):
        table[x] = k % p
        x = (x * generator) % q
    assert x == 1
    assert pow(generator, (q-1)//p, q) != 1
    assert table[1] == 0
    assert table[q-1] == ((q-1)//2) % p
    return table, generator


def admissible(E, p, q):
    return q != 389 and (q - 1) % p == 0 and int(E.ap(q) - q - 1) % p == 0


def find_small_pair(E,p,bound):
    qs=[int(q) for q in prime_range(3,bound) if admissible(E,p,q)]
    if len(qs)<2: raise ValueError('Need at least two admissible primes; increase --bound')
    return qs[:2]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--p', type=int, default=107)
    parser.add_argument('--q1', type=int, default=369793)
    parser.add_argument('--q2', type=int, default=383917)
    parser.add_argument('--auto-small', action='store_true')
    parser.add_argument('--bound', type=int, default=2000)
    parser.add_argument('--limit', type=int, default=1000, help='maximum representatives a to evaluate, default is pilot only')
    parser.add_argument('--full', action='store_true', help='evaluate all reps (enormous for p107)')
    parser.add_argument('--progress-every', type=int, default=10000)
    args=parser.parse_args()
    E=EllipticCurve(QQ,[0,1,1,-2,0]); p=args.p
    assert p>=5 and ZZ(p).is_prime()
    q1,q2=find_small_pair(E,p,args.bound) if args.auto_small else (args.q1,args.q2)
    for q in (q1,q2):
        assert ZZ(q).is_prime() and admissible(E,p,q), (p,q)
    assert q1!=q2
    n=q1*q2; phi=(q1-1)*(q2-1)
    # Both q_i are 1 mod 2p in the target instance, hence log_q(-1) is 0 mod p.
    assert (q1-1)//2 % p == 0 and (q2-1)//2 % p == 0, 'pairing by a->n-a not valid in this mode'
    logs1,g1=logs_mod_p(q1,p); logs2,g2=logs_mod_p(q2,p)
    symbol=ECModularSymbol(E,sign=1)
    scale=2 if E.discriminant()<0 else 1  # eclib normalisation (Ghitza-Kim)
    upper=(n-1)//2
    end=upper if args.full else min(upper,args.limit)
    total=0; nonzero_terms=0; ts=time.monotonic()
    print('CONFIG',json.dumps({'p':p,'q1':q1,'q2':q2,'n':n,'phi':phi,
          'symmetry_reps':phi//2,'primitive_roots':[g1,g2],
          'normalization_scale':scale,'requested_reps':end,'full':args.full}),flush=True)
    checks=0
    for a in range(1,end+1):
        r1=a%q1; r2=a%q2
        if not r1 or not r2:continue
        l=(logs1[r1]*logs2[r2])%p
        if not l: continue
        v=QQ(symbol(QQ(a)/n))
        # The sign-plus modular symbol must be invariant under a -> n-a.
        if checks<8:
            assert v == QQ(symbol(QQ(n-a)/n)), ('plus symmetry failure',a)
            checks+=1
        assert v.denominator()%p != 0, ('non p-integral symbol',a,v)
        contribution=(int(v.numerator())%p)*pow(int(v.denominator())%p,-1,p)%p
        total=(total+l*contribution)%p
        nonzero_terms+=1
        if args.progress_every and a%args.progress_every == 0:
            print('PARTIAL',a,total,round(time.monotonic()-ts,2),flush=True)
    if args.full:
        result=(total*2*pow(scale,-1,p))%p
        print('KURIHARA_DELTA_COMPLETE',result, 'NONZERO',bool(result),flush=True)
    else:
        print('INCOMPLETE_NO_CERTIFICATE',json.dumps({'last_a':end,'max_a':upper,
              'partial_sum_unscaled_unpaired':total,'evaluated_nonzero_weights':nonzero_terms,
              'seconds':round(time.monotonic()-ts,3)}),flush=True)

if __name__=='__main__': main()