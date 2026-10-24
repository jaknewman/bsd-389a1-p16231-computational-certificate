from sage.all import *
from pathlib import Path
from array import array
import hashlib, json, os, sys, time

p, N, ainv = 16231, 389, 5199
COS, GEN = p + 1, 67
L = p - 1
F = GF(p)

ROOT = Path.home() / "bsd389-c01-v14-production"
EXPORT = Path.home() / (
    "bsd389-portable-c01-v2/data/"
    "bsd389_tame_relation_export_p16231.json"
)
STATE = ROOT / "v19_checkpoints/state_263429130.bin"
SAVE = ROOT / "v26_m1_progress.json"

EXPECTED_SHA = (
    "5ebeffa2fd67fe2eb54ce6a925bd21"
    "dfb850ed9616f9462dce330f98a5a9da1e"
)

assert sys.byteorder == "little"
assert hashlib.sha256(STATE.read_bytes()).hexdigest() == EXPECTED_SHA

raw = STATE.read_bytes()
assert len(raw) == 4 * GEN * COS

c1 = array("H")
c1.frombytes(raw[2 * GEN * COS:])
assert len(c1) == GEN * COS
assert max(c1) < p

data = json.loads(EXPORT.read_text())
bygen = {int(x["generator"]): x for x in data["reps"]}
assert all(g in bygen for g in range(GEN)), (
    "Missing generator among 0..66",
    sorted(set(range(GEN)) - set(bygen))
)
print(
    "V26_GENERATOR_MAPPING_PASS",
    "TOTAL_EXPORT_REPS", len(bygen),
    "SELECTED_GENERATORS", GEN,
    flush=True
)

Rinf = matrix(ZZ, 2, 2, data["rinf"])
assert Rinf.det() == 1

E = EllipticCurve("389a1")
assert E.ap(p) == 128
symbol = E.modular_symbol(sign=+1, implementation="eclib")

def f(n, d):
    if d == 0:
        return 0
    q = -symbol(QQ(n) / QQ(d))
    num = ZZ(q.numerator())
    den = ZZ(q.denominator())
    assert den % p != 0
    return int(num * inverse_mod(den, p) % p)

def value(D):
    return (
        f(D[0,1], D[1,1]) -
        f(D[0,0], D[1,0])
    ) % p

Pmat = matrix(ZZ, [[p,0],[0,1]])

def beta(t):
    return matrix(ZZ, [[1,t],[0,p]])

def direct_m1(G, Rj):
    D = Rj * G
    z = 0
    for t in range(p):
        z += t * value(beta(t) * D)
    return (ainv * z) % p

# La table des logarithmes et le noyau de convolution
# ne dépendent pas du générateur.
primitive = F.multiplicative_generator()
powers = [int(primitive**k) for k in range(L)]
assert len(set(powers)) == L

logs = [-1] * p
for k, s in enumerate(powers):
    logs[s] = k

B = [
    0 if s == 1 else int(F(1-s)**(-1))
    for s in powers
]

PR = PolynomialRing(F, "X")
PB = PR(B)

def calculate_moments(G):
    V = [value(beta(t)*G) for t in range(p)]
    Vinf = value(Pmat*G)

    A = [(s*V[s]) % p for s in powers]
    Arev = [A[(-k) % L] for k in range(L)]

    prod = (PR(Arev)*PB).list()

    C = [
        int(
            (prod[k] if k < len(prod) else F(0)) +
            (prod[k+L] if k+L < len(prod) else F(0))
        ) % p
        for k in range(L)
    ]

    M = [0] * COS
    M[0] = (ainv * sum(s*V[s] for s in range(p))) % p

    for j in range(1,p):
        u = (N*j) % p
        ell = logs[u]
        assert ell >= 0
        M[j] = (
            ainv * (C[ell] - Vinf*pow(u,-1,p))
        ) % p

    # Coset exceptionnel Rinf.
    a,b,c,d = [int(x) % p for x in Rinf.list()]
    z = 0

    for s in range(p):
        den = (d-c*s) % p
        if den == 0:
            continue
        t = ((a*s-b)*pow(den,-1,p)) % p
        z = (z + t*V[s]) % p

    if c != 0:
        t_exceptional = (-a*pow(c,-1,p)) % p
        z = (z+t_exceptional*Vinf) % p

    M[p] = (ainv*z) % p

    return M

if SAVE.exists():
    progress = json.loads(SAVE.read_text())
    assert progress["source_sha256"] == EXPECTED_SHA
    assert 0 <= progress["next_generator"] <= GEN
    assert len(progress["per_generator"]) == progress["next_generator"]
else:
    progress = {
        "source_sha256": EXPECTED_SHA,
        "next_generator": 0,
        "J1": 0,
        "per_generator": []
    }

start = time.monotonic()

for g in range(progress["next_generator"], GEN):
    G = matrix(ZZ, 2, 2, bygen[g]["matrix"])
    moments = calculate_moments(G)

    # Vérification indépendante de la méthode rapide
    # pour trois générateurs répartis dans le corpus.
    if g in (0,1,66):
        for j in (1,p):
            Rj = (
                matrix(ZZ,[[1,0],[N*j,1]])
                if j < p else Rinf
            )
            oracle = direct_m1(G, Rj)
            actual = moments[j]

            print(
                "V26_ORACLE",g,j,
                "FAST",actual,
                "DIRECT",oracle,
                "MATCH",actual == oracle,
                flush=True
            )
            assert actual == oracle

    offset = g*COS
    subtotal = sum(
        int(c1[offset+j])*moments[j]
        for j in range(COS)
    ) % p

    progress["J1"] = int(
        (progress["J1"] + subtotal) % p
    )
    progress["next_generator"] = int(g+1)
    progress["per_generator"].append({
        "g": int(g),
        "contribution": int(subtotal),
        "exceptional_m1": int(moments[p])
    })

    tmp = SAVE.with_name(SAVE.name + ".tmp")
    with tmp.open("w") as out:
        json.dump(progress,out,sort_keys=True,indent=2)
        out.flush()
        os.fsync(out.fileno())
    os.replace(tmp,SAVE)

    print(
        "V26_GENERATOR_PASS",g,
        "J1_PARTIAL",progress["J1"],
        "EXCEPTIONAL_M1",moments[p],
        "SECONDS",round(time.monotonic()-start,2),
        flush=True
    )

if progress["next_generator"] == GEN:
    J0 = 16014
    J1 = int(progress["J1"])
    J = (J0+J1) % p

    print("V26_J0_MOD_P",J0)
    print("V26_J1_MOD_P",J1)
    print("V26_J_EFFECTIVE_CANDIDATE_MOD_P",J)
    print("V26_GLOBAL_M1_CONTRACTION_PASS")
