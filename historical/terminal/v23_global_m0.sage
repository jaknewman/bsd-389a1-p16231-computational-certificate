from sage.all import *
from pathlib import Path
from array import array
import hashlib, json, os, time, sys

p, N, ainv = 16231, 389, 5199
COS, GEN = p+1, 67
ROOT = Path.home() / "bsd389-c01-v14-production"
EXPORT = ROOT.parent / "bsd389-portable-c01-v2/data/bsd389_tame_relation_export_p16231.json"
STATE = ROOT / "v19_checkpoints/state_263429130.bin"
SAVE = ROOT / "v23_m0_progress.json"

raw = STATE.read_bytes()
assert hashlib.sha256(raw).hexdigest() == (
    "5ebeffa2fd67fe2eb54ce6a925bd21dfb850"
    "ed9616f9462dce330f98a5a9da1e"
)
assert sys.byteorder == "little"
c0 = array("H")
c0.frombytes(raw[:2*GEN*COS])

data = json.loads(EXPORT.read_text())
bygen = {int(x["generator"]): x for x in data["reps"]}
Rinf = matrix(ZZ,2,2,data["rinf"])

E = EllipticCurve("389a1")
assert E.ap(p) == 128
m = E.modular_symbol(sign=+1, implementation="eclib")

def f(n,d):
    if d == 0:
        return ZZ(0)
    q = -m(QQ(n)/QQ(d))
    num, den = ZZ(q.numerator()), ZZ(q.denominator())
    if den % p == 0:
        raise ArithmeticError("Noninvertible denominator")
    return num * inverse_mod(den,p) % p

def F(a,b,c,d):
    return (f(b,d)-f(a,c)) % p

def M0(a,b,c,d):
    return (F(a,b,c,d)-ainv*F(p*a,p*b,c,d)) % p

if SAVE.exists():
    progress = json.loads(SAVE.read_text())
    assert progress["source_sha256"] == hashlib.sha256(raw).hexdigest()
    assert 0 <= progress["next_generator"] <= GEN
else:
    progress = {
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "next_generator": 0,
        "J0": 0,
        "per_generator": []
    }

t0 = time.monotonic()

for g in range(progress["next_generator"],GEN):
    z = bygen[g]["matrix"]
    G = matrix(ZZ,2,2,z)
    subtotal = ZZ(0)
    nonzero = 0

    for j in range(COS):
        if j == p:
            D = Rinf * G
        else:
            D = matrix(ZZ,[[1,0],[N*j,1]]) * G

        a,b,c,d = map(ZZ,D.list())
        value = M0(a,b,c,d)
        if value:
            nonzero += 1

        slot = g*COS+j
        subtotal = (subtotal + ZZ(c0[slot])*value) % p

    progress["J0"] = int((ZZ(progress["J0"])+subtotal)%p)
    progress["next_generator"] = g+1
    progress["per_generator"].append({
        "g":g, "contribution":int(subtotal),
        "nonzero_m0":nonzero
    })

    temp = SAVE.with_suffix(".json.tmp")
    temp.write_text(json.dumps(progress,sort_keys=True,indent=2,default=int))
    os.replace(temp,SAVE)

    print("V23_GENERATOR_PASS",g,
          "J0_PARTIAL",progress["J0"],
          "M0_NONZERO",nonzero,
          "SECONDS",round(time.monotonic()-t0,2),
          flush=True)

print("V23_J0_MOD_P",progress["J0"])
print("V23_GLOBAL_M0_CONTRACTION_PASS")
