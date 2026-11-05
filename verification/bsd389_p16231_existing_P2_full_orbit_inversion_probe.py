#!/usr/bin/env python3
"""Cheap test of inversion symmetry from the ALREADY computed 16231 Gross points.

Reads the frozen 32 authenticated chunk JSONs and verifies all records,
without running quaternionic classification again. Tests whether
v(P2^(u^i)) equals v(P2^(u^(-i))) and compares Brandt class labels.
A numerical equality is only a clue: global inverse symmetry requires
a separate proof before exploiting it to reduce a theta computation.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path
from math import comb
P=16231
M=P*P
DIR=Path.home()/"bsd389_p16231_P2_u_orbit_chunk_certificates"
V=(0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,
   0,2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0)
sha="2a12796dd1fd56351e82c2337c02d74d578ab87fa01f40c564dc37c79ad66db5"
start=DIR/"r1_i00000_00512.json"
assert start.is_file()
assert hashlib.sha256(start.read_bytes()).hexdigest()==sha
entries=[None]*P
files=sorted(DIR.glob("r1_i*.json"))
assert len(files)==32,("EXPECTED_32_EXISTING_CERTIFIED_CHUNKS",len(files))
for path in files:
    o=json.loads(path.read_text())
    assert o["status"]=="P2_GROSS_EXACT_CHUNK_PASS"
    assert o["p"]==P and o["residue"]==1
    lo,hi=o["start"],o["end_exclusive"]
    assert 0<=lo<hi<=P and len(o["points"])==hi-lo
    local=[0,0,0]
    for t,row in enumerate(o["points"],lo):
        assert entries[t] is None and row["i"]==t
        assert row["a"]==(1+P*t)%M
        j=row["brandt_class"];v=row["brandt_value"]
        assert type(j) is int and 0<=j<33
        assert v==V[j]
        entries[t]=(j,v)
        local[0]=(local[0]+v)%P
        local[1]=(local[1]+t*v)%P
        local[2]=(local[2]+comb(t,2)*v)%P
    assert local==o["moment0_1_2_modp"],("CHUNK_MOMENT_ERROR",path.name)
assert all(z is not None for z in entries)
full=[sum(comb(i,k)*v for i,(_j,v) in enumerate(entries))%P
      for k in range(3)]
assert full==[0,10775,5515]
print("P2_INVERSION_SOURCE_FULL_ORBIT_REAGGREGATE_PASS",full,flush=True)

value_equal=sum(entries[i][1]==entries[(-i)%P][1] for i in range(P))
class_equal=sum(entries[i][0]==entries[(-i)%P][0] for i in range(P))
value_negative=sum(entries[i][1]==-entries[(-i)%P][1] for i in range(P))
first_mismatches=[
   [i,entries[i],(-i)%P,entries[(-i)%P]]
   for i in range(P) if entries[i][1]!=entries[(-i)%P][1]
][:8]
print("P2_INVERSION_VALUE_EQUAL_COUNT",value_equal,"OF",P,flush=True)
print("P2_INVERSION_CLASS_EQUAL_COUNT",class_equal,"OF",P,flush=True)
print("P2_INVERSION_VALUE_NEGATIVE_COUNT",value_negative,"OF",P,flush=True)
print("P2_INVERSION_FIRST_VALUE_MISMATCHES",first_mismatches,flush=True)
if value_equal==P:
    print("P2_INVERSION_VALUE_SYMMETRY_OBSERVED_ON_FULL_TEICH1_ORBIT_PASS",flush=True)
    print("BOUNDARY_A_GLOBAL_ALL_TEICH_INVOLUTION_PROOF_NOT_PROVIDED",flush=True)
else:
    print("P2_SIMPLE_INVERSION_VALUE_SYMMETRY_REFUTED_ON_TEICH1_ORBIT",flush=True)

# Complex conjugation can include a change of base point / translation.
# Check modest possible shifts without asserting any of them mathematically.
for shift in (0,1,2,3,P-1):
    equal=sum(entries[i][1]==entries[(shift-i)%P][1] for i in range(P))
    print("P2_INVERSION_WITH_SHIFT_EQUAL_COUNT",shift,equal,"OF",P,flush=True)
print("P2_EXISTING_ORBIT_INVERSION_PROBE_PASS",flush=True)
print("BOUNDARY_PROBE_DOES_NOT_CHANGE_GLOBAL_THETA_STATUS",flush=True)
