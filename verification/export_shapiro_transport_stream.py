#!/usr/bin/env python3
"""Canonical, SHA-pinned, plain-text export for the standalone C01 verifier.

No Sage, Boost or third-party dependencies. Emits 2,404 data lines on stdout,
diagnostics only on stderr. Intended for a direct pipe into the C++ verifier.
"""
import hashlib
import json
import sys
from pathlib import Path

EXPECTED_SHA = "9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
N=389
P=16231

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python verification/export_shapiro_transport_stream.py EXPORT.json")
    fp=Path(sys.argv[1])
    payload=fp.read_bytes()
    digest=hashlib.sha256(payload).hexdigest()
    assert digest==EXPECTED_SHA, ("ORIGINAL_EXPORT_SHA256_MISMATCH",digest)
    obj=json.loads(payload)
    assert obj["N"]==N and obj["p"]==P
    reps=obj["reps"]
    assert len(reps)==390 and len(obj["generators"])==67
    assert len(obj["key_to_rep"])==390
    terms=sum(len(r["relations"]) for r in reps)
    assert terms==2012
    rinf=obj["rinf"]
    assert len(rinf)==4 and all(isinstance(x,int) for x in rinf)

    print("BSD389_SHAPIRO_V1",N,P,390,67,terms)
    print("RINF",*rinf)
    for i,r in enumerate(reps):
        m=r["matrix"]
        g=r["generator"]
        ts=r["relations"]
        assert len(m)==4 and all(isinstance(x,int) for x in m)
        assert isinstance(g,int) and (-1<=g<67)
        print("REP",i,*m,g,len(ts))
        for t in ts:
            mm=t["A"]
            assert len(mm)==4 and all(isinstance(x,int) for x in mm)
            assert t["coeff"] in (-1,1)
            assert 0<=t["r"]<390
            print("TERM",i,t["coeff"],t["r"],*mm)
    print("ORIGINAL_EXPORT_SHA256_PASS",digest,file=sys.stderr,flush=True)
    print("ORIGINAL_EXPORT_RELATIONS_PASS",len(reps),terms,file=sys.stderr,flush=True)

if __name__=="__main__":
    main()
