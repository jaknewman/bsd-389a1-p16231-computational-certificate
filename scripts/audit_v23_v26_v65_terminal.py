#!/usr/bin/env python3
"""Read-only V23/V26/V65 terminal audit, 389a1 p=16231.

Recompute SHA identities and all 67 per-generator comparisons using historical
files. Does NOT rerun Sage/eclib or prove the 263m-pair C01 producer or BSD.
"""
from pathlib import Path
from array import array
import csv
import hashlib
import json
import sys

P = 16231
GEN = 67
COS = P + 1
STATE_SHA = "5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e"
ROOT = Path.home() / "bsd389-c01-v14-production"
V65 = ROOT / "v65_independent_terminal"
PROJECT = Path(__file__).resolve().parents[1]

def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def check(condition, label):
    if not condition:
        raise AssertionError(label)
    print("PASS", label, flush=True)

def main():
    state = ROOT / "v19_checkpoints/state_263429130.bin"
    p0 = ROOT / "v23_m0_progress.json"
    p1 = ROOT / "v26_m1_progress.json"
    tsv = V65 / "v65_per_generator.tsv"
    cert = V65 / "v65_terminal_certificate.json"
    table = V65 / "eclib_beta_table.bin"
    table_manifest = V65 / "eclib_beta_table_manifest.json"

    check(sys.byteorder == "little", "LITTLE_ENDIAN")
    check(state.stat().st_size == 4*GEN*COS, "STATE_BYTE_LENGTH")
    check(sha(state) == STATE_SHA, "STATE_FROZEN_SHA256")
    d0 = json.loads(p0.read_text())
    d1 = json.loads(p1.read_text())
    audit = json.loads(cert.read_text())

    for tag, d, field in [("V23",d0,"J0"),("V26",d1,"J1")]:
        check(d["source_sha256"] == STATE_SHA, tag+"_STATE_SHA256")
        check(d["next_generator"] == GEN, tag+"_ALL_GENERATORS")
        rr = d["per_generator"]
        check(len(rr) == GEN and [int(x["g"]) for x in rr] == list(range(GEN)),
              tag+"_ORDERED_PER_GENERATOR")
        reconstructed = sum(int(x["contribution"]) for x in rr)%P
        check(reconstructed == int(d[field]), tag+"_RECONSTRUCTION")
        print(tag+"_TOTAL",reconstructed,flush=True)

    with tsv.open(newline="") as f:
        rows = list(csv.DictReader(f,delimiter="\t"))
    check(len(rows)==GEN+1 and rows[-1]["g"]=="TOTAL","V65_TSV_DIMENSIONS")

    j0 = j1 = 0
    for g in range(GEN):
        r = rows[g]
        checkrow = (int(r["g"])==g
            and int(r["J0"])==int(d0["per_generator"][g]["contribution"])
            and int(r["J1"])==int(d1["per_generator"][g]["contribution"])
            and int(r["Hecke"])==0)
        if not checkrow:
            raise AssertionError(f"V65_PER_GENERATOR_MISMATCH g={g}: {r}")
        j0=(j0+int(r["J0"]))%P
        j1=(j1+int(r["J1"]))%P
    check((j0,j1,(j0+j1)%P)==(16014,4703,4486),
          "V65_67X2_TOTALS_EXACT")
    check((int(rows[-1]["J0"]),int(rows[-1]["J1"]))==(j0,j1),
          "V65_TSV_TOTAL_ROW")
    check((audit["J0"],audit["J1"],audit["J"])==(j0,j1,4486),
          "V65_CERTIFICATE_TOTALS")
    check(audit["state_sha256"]==STATE_SHA, "V65_CERTIFICATE_STATE")
    for name,path in [("terminal_tsv_sha256",tsv),
                      ("v23_progress_sha256",p0),
                      ("v26_progress_sha256",p1)]:
        check(sha(path)==audit[name], "V65_CERTIFICATE_"+name)

    if table.exists():
        check(sha(table)==audit["reference_eclib_table_sha256"],
              "V65_ECLIB_TABLE_SHA256")
        if table_manifest.exists():
            manifest=json.loads(table_manifest.read_text())
            check(manifest["table_sha256"]==sha(table),
                  "V65_ECLIB_MANIFEST_SHA256")
            check(manifest["generators"]==GEN, "V65_TABLE_GENERATORS")
        # Optional cross-check header+size even when manifest not present.
        with table.open("rb") as f: header=f.read(20)
        check(header[:8]==b"BSD65F01" and
              [int.from_bytes(header[k:k+4],"little") for k in (8,12,16)]
              ==[P,389,GEN], "V65_TABLE_HEADER")
        check(table.stat().st_size==20+GEN*(P+2)*2,"V65_TABLE_SIZE")
    else:
        print("NOT_CHECKED V65_ECLIB_TABLE_FILE_MISSING",flush=True)

    check((128*5199)%P==1,"ALPHA_INVERSE")
    factor=(4486*pow(4*128*128,-1,P))%P
    a2=(1199+factor)%P
    b2=(1930*pow(1-5199,2,P))%P
    check((factor,a2,b2)==(8335,9534,9534),"CONDITIONAL_SAGE_BRIDGE_ARITHMETIC")
    check((a2*pow(b2,-1,P))%P==1,"CONDITIONAL_QUOTIENT_DIGIT_ONE")
    print("V23_V26_V65_TERMINAL_CROSS_AUDIT_PASS",flush=True)
    print("BOUNDARY: C01 all-pairs production and the Sage level-2/level-3 comparison were NOT re-executed",flush=True)
    print("BOUNDARY: unconditional Sha[16231^infinity]=0 and full BSD NOT asserted",flush=True)

if __name__=="__main__":
    main()
