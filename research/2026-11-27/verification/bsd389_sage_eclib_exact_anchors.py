# Independent exact rational modular-symbol comparison in SageMath/eclib.
# Run from this directory:
#   sage -python bsd389_sage_eclib_exact_anchors.py
# This script was NOT run in the current ChatGPT environment (Sage absent).
from pathlib import Path
from sage.all import ZZ, QQ, EllipticCurve
from bsd389_standalone_p2_audit import modular_symbol, load_table

E = EllipticCurve(QQ, [0,1,1,-2,0])
assert E.conductor() == 389
v = load_table(Path(__file__).with_name("manin_390.txt"))
M_eclib = E.modular_symbol(sign=1, implementation="eclib")
M_sage = E.modular_symbol(sign=1, implementation="sage", normalize="period")
assert M_eclib(QQ(5)/389) == -2
assert M_eclib(QQ(7)/389) == -1
for a in range(1,389):
    expected = ZZ(modular_symbol(a,389,v))
    actual = M_eclib(QQ(a)/389)
    assert actual == expected, (a,actual,expected)
print("ECLIB_NERON_NORMALIZATION_EXACT_PASS 388")
print("SAGE_PERIOD_ANCHORS",M_sage(QQ(5)/389),M_sage(QQ(7)/389))
