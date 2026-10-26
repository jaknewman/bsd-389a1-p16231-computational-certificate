#!/usr/bin/env python3
"""Read-only evidence audit of the second FULL 263,429,130-pair scalar J run.

The historical value J=4486 is NOT assumed valid to manufacture a PASS;
the completed checkpoint and logged terminal results are independently
checked for presence, parseability, coherence, and all relevant SHA pins.
This does not re-execute the entire outer summation or prove binary semantics.
"""
from pathlib import Path
import hashlib
import re
import subprocess
import sys

P=16231
TOTAL=P*(P-1)
EXPECTED_TABLE="aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c"
EXPECTED_EXPORT="9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8"
ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda:file.read(1048576),b""):
            h.update(chunk)
    return h.hexdigest()

def required(path):
    if not path.is_file():
        raise FileNotFoundError("Required file missing: "+str(path))
    digest=sha(path)
    print("SECOND_J_EVIDENCE_SHA256",str(path),digest,flush=True)
    return digest

def main():
    reference=HOME/"bsd389-c01-v14-production/v65_independent_terminal/eclib_beta_table.bin"
    export=ROOT/"historical/originals/bsd389_tame_relation_export_p16231.json"
    cpp=ROOT/"verification/independent_c01_scalar_J.cpp"
    ntt=ROOT/"historical/v65/v65_independent_terminal_ntt.cpp"
    elf=Path("/tmp/bsd389_independent_J")
    checkpoint=HOME/"bsd389_independent_J_full.chk"
    logfile=HOME/"bsd389_independent_J_full.log"

    assert required(reference)==EXPECTED_TABLE, "V65 SHA did not match"
    assert required(export)==EXPECTED_EXPORT, "Manin export SHA did not match"
    for file in (cpp,ntt,elf,checkpoint,logfile):
        required(file)
    assert elf.stat().st_size>0 and elf.stat().st_mode&0o100, "missing executable mode"
    print("SECOND_J_PINNED_INPUTS_PASS",flush=True)

    fields=checkpoint.read_text().strip().split()
    assert fields==["BSD389_INDEPENDENT_SCALAR_J_V1",
                    "0",str(TOTAL),str(TOTAL),"4486"], (
                        "unexpected final independent checkpoint",fields)
    print("SECOND_J_FINAL_CHECKPOINT_PASS",
          "pairs",TOTAL,"sum_mod_p",4486,flush=True)

    log=logfile.read_text(errors="replace")
    target1=(
        "INDEPENDENT_SCALAR_INTERVAL_PASS start=0 end="
        +str(TOTAL)+" J_mod_p=4486")
    target2=(
        "INDEPENDENT_SCALAR_GLOBAL_J_4486_PASS pairs="+str(TOTAL))
    assert target1 in log and target2 in log, "global full terminal PASS absent"
    assert (
        "INDEPENDENT_SCALAR_CHECKPOINT_PASS next="+str(TOTAL)
        +" sum_mod_p=4486 of="+str(TOTAL)) in log, "final checkpoint PASS absent"
    assert "INDEPENDENT_SCALAR_ALL_BASIS_MOMENTS_PASS 1087544" in log
    assert (
        "INDEPENDENT_SCALAR_ALL_390_REP_MOMENTS_PASS slots=6330480 "
        "expanded_relation_terms=31571240") in log
    assert "INDEPENDENT_SCALAR_TEICH_TABLE_PASS 16230" in log

    positions=[
        (int(a),int(b),int(c))
        for a,b,c in re.findall(
            r"INDEPENDENT_SCALAR_CHECKPOINT_PASS next=(\d+)"
            r" sum_mod_p=(\d+) of=(\d+)",log)
    ]
    assert positions and positions[-1]==(TOTAL,4486,TOTAL)
    assert all(c==TOTAL and 0<=b<P and 0<a<=TOTAL
               and (a%1000000==0 or a==TOTAL)
               for a,b,c in positions), "invalid checkpoint record"
    assert all(positions[i][0]<=positions[i+1][0]
               for i in range(len(positions)-1)), (
        "checkpoint sequence decreased; inspect whether multiple restarts "
        "were concatenated")
    assert "INDEPENDENT_SCALAR_J_FAIL " not in log
    assert "INDEPENDENT_SCALAR_GLOBAL_J_MISMATCH" not in log
    print("SECOND_J_COMPLETE_LOG_AND_CHECKPOINT_PASS",
          "checkpoints_logged",len(positions),"last",positions[-1][0],
          "sum_mod_p",positions[-1][1],flush=True)

    commit=subprocess.run(
        ["git","-C",str(ROOT),"rev-parse","HEAD"],
        check=True,capture_output=True,text=True).stdout.strip()
    print("SECOND_J_REPO_COMMIT",commit,flush=True)
    print("SECOND_J_INDEPENDENT_FULL_EVIDENCE_PASS",flush=True)
    print("BOUNDARY: hash/log/checkpoint auditor, NOT a fresh "
          "263429130-pair computation and NOT independent eclib source data.")
if __name__=="__main__":
    try: main()
    except Exception as exc:
        print("SECOND_J_EVIDENCE_FAIL",str(exc),file=sys.stderr,flush=True)
        raise
