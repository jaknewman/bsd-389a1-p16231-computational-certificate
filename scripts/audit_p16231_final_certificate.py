#!/usr/bin/env python3
"""Integrity and exact-arithmetic audit of the BSD389 p=16231 proof ledger.

READ-ONLY and QUICK. This checks locally present historical files and
the published terminal record. IT DOES NOT replay 263 million C01 pairs,
recompute the full Sage level-3 series, or execute Sha.p_primary_bound.

Expected to run in ordinary Python >=3.9 from any working directory:
  python -u scripts/audit_p16231_final_certificate.py
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HOME=Path.home()
HIST=HOME/"bsd389-c01-v14-production"
ORIG=ROOT/"historical/originals"
PROV=ROOT/"historical/provenance"
P=16231
P2=P*P
TOTAL=P*(P-1)
EXPECTED={
    "binary": "31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63",
    "v11_source": "0d8b18696587fc3a0f497c54ebbba99f4d582e69d5a98d0da0e2a4275172b187",
    "driver": "61eef8564236babf1b669c3fdd40db5d201ebc96bb4f1f8a40a04a6b9e5df418",
    "export": "9c385efb6cf1a0c8e9061e971c4bc1cd3c241c6979c490ac7a916554ee8eb8f8",
    "v19_full_log": "7389152cd65c641b7173d69dc3de8098f510e550943179cfaf0373c748443a7a",
    "v19_preflight_log": "89e6cda8fc3a712f7f724b6f9f55863eae1bef3c113e05bc02e7f9d90cf5bdc4",
    "v19_replay_log": "07db19e00beecc654e4ccffcf8f2f55b36a10fc8f93052ddf7cd86dc5121e473",
    "final_state": "5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e",
    "v11_report": "a9b853ee30d95bb48565bc99c35799dcc40c57b2bc8b9915792b81e72e3e9371",
}

def require(cond,msg):
    if not cond:
        raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for blk in iter(lambda:f.read(1<<20),b""):
            h.update(blk)
    return h.hexdigest()

def check_hash(path,expected,label):
    require(path.is_file(), "missing "+label+": "+str(path))
    d=sha(path)
    require(d==expected,label+" SHA mismatch "+d+" != "+expected)
    print("FINAL_CERT_SOURCE_SHA_PASS",label,d,flush=True)

def main():
    require(P==16231 and P2==263445361 and TOTAL==263429130,
            "domain constants changed")
    require(pow(128,P-2,P)==5199, "Frobenius mod-p inverse changed")
    require((179060520**2-128*179060520+P)%P2==0,
            "reported alpha is not a root modulo p^2")
    require(179060520%P==128,"wrong alpha residue")

    check_hash(ORIG/"bsd389_c01_v11_aggregated.cpp",
               EXPECTED["v11_source"],"original_V11_source")
    check_hash(ORIG/"v19_production.py",
               EXPECTED["driver"],"historical_V19_driver")
    check_hash(ORIG/"bsd389_tame_relation_export_p16231.json",
               EXPECTED["export"],"original_relations_JSON")
    check_hash(HOME/"bsd389-c01-v11-test/bsd389_c01_v11_aggregated",
               EXPECTED["binary"],"historical_original_ELF")
    check_hash(PROV/"v11_provenance_report_2026-10-19.json",
               EXPECTED["v11_report"],"V11_binary_provenance_report")
    for filename,kind in (("v19_chain_full.log","v19_full_log"),
                           ("v19_chain_preflight.log","v19_preflight_log"),
                           ("bsd389_v19_stratified_producer.log","v19_replay_log")):
        check_hash(PROV/filename,EXPECTED[kind],kind)

    provenance=json.loads((PROV/"v11_provenance_report_2026-10-19.json").read_text())
    require(provenance["artifact_digest"]["binary"]==EXPECTED["binary"],
            "V11 report executable hash inconsistent")
    require(provenance["artifact_digest"]["final_state"]==EXPECTED["final_state"],
            "V11 report final-state hash inconsistent")
    require(provenance["reproducible_binary"] is True,"no byte-identical rebuild")
    builds=[x for x in provenance["compilation"] if x["optimization"]=="-O2"]
    require(len(builds)==1 and builds[0]["same_bytes_as_original"] is True
            and builds[0]["sha256"]==EXPECTED["binary"],"not an O2 byte rebuild")
    require(len(provenance["bounded_windows"])==4
            and all(x["original"]["sha256"]==x["rebuilt"]["sha256"]
                    for x in provenance["bounded_windows"]),
            "V11 historical/rebuilt sample windows disagree")
    print("FINAL_CERT_BYTE_IDENTICAL_V11_BUILD_REPORT_PASS",flush=True)

    archive=json.loads((PROV/"v11_v19_archive_manifest.json").read_text())
    require(archive["sha256"]["v19_chain_full.log"]==EXPECTED["v19_full_log"],
            "manifest/log mismatch")
    chain=(PROV/"v19_chain_full.log").read_text()
    pattern=(r"V19_FULL_CHUNK_TO_CHECKPOINT_CHAIN_PASS pairs (\d+) "
             r"expected_chunks (\d+) checkpoints (\d+) all_rows (\d+) "
             r"final_sha256 ([0-9a-f]{64})")
    matches=re.findall(pattern,chain)
    require(len(matches)==1,"cannot uniquely find final chain PASS record")
    pairs,chunks,checkpoints,rows,finalsha=matches[0]
    require((int(pairs),int(chunks),int(checkpoints),int(rows))==
            (TOTAL,514511,4019,9759143225),
            "V19 final coverage changed")
    require(finalsha==EXPECTED["final_state"],"wrong terminal state hash")
    progress=json.loads((PROV/"v19_independent_chain_audit_progress.json").read_text())
    require(progress["end"]==TOTAL and progress["blocks_done"]==4018
            and progress["rows_read"]==9759143225
            and progress["digest"]==EXPECTED["final_state"],
            "auditor progress not at final checkpoint")
    print("FINAL_CERT_RECOMPOSED_ARCHIVED_CHAIN_REPORTED_PASS",
          pairs,chunks,checkpoints,rows,flush=True)

    replay=(PROV/"bsd389_v19_stratified_producer.log").read_text()
    found=re.findall(
        r"^V19_NATIVE_ARCHIVE_CHUNK_BYTES_PASS (\d+) (\d+) "
        r"(\d+) (\d+) ([0-9a-f]{64})$",replay,re.M)
    require(len(found)==57,"not 57 archived native pair windows")
    require([int(x[0]) for x in found]==list(range(1,58)),
            "missing or repeated replay ordinal")
    require(all(int(x[1])==57 for x in found),"wrong replay denominator")
    ranges=[(int(x[2]),int(x[3])) for x in found]
    require(all(0<=lo<hi<=TOTAL and hi-lo<=512 for lo,hi in ranges),
            "invalid native replay interval")
    require(len(set(ranges))==57 and sum(hi-lo for lo,hi in ranges)==28682,
            "sample intervals overlap/coverage mismatch")
    require(re.search(
        r"^V19_STRATIFIED_PRODUCER_REPLAY_PASS 57 "
        r"pairs_covered 28682 exceptional_E0 1186 exceptional_E1 14540$",
        replay,re.M),"missing exact replay summary")
    print("FINAL_CERT_NATIVE_SOURCE_DATA_SAMPLED_PASS",
          "windows=57","pairs=28682",flush=True)

    j=json.loads((ROOT/"historical/v65/v65_terminal_certificate.json").read_text())
    require((j["J0"],j["J1"],j["J"],j["generators"],
             j["checks_per_generator"])==(16014,4703,4486,67,2),
            "V65 terminal values changed")
    require(j["state_sha256"]==EXPECTED["final_state"],
            "V65 source state incompatible with V19")
    require(j["reference_eclib_table_sha256"]==
            "aca208b2c2f8ab87b3588a480929dc4d3600ec9c2889c02699225e7a9799374c",
            "V65 eclib table provenance changed")
    require((j["J0"]+j["J1"])%P==j["J"],"V65 contraction not additive")
    print("FINAL_CERT_TERMINAL_MOMENTS_REPORTED_PASS",
          j["J0"],j["J1"],j["J"],flush=True)

    a2=json.loads((ROOT/"historical/level2/v61_a2_p2_result.json").read_text())
    record={k:v for k,v in a2.items() if k!="sha256"}
    digest=hashlib.sha256(json.dumps(
        record,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    require(digest==a2["sha256"],"V61 result canonical digest mismatch")
    require(a2["a_covered"]==(P-1)//2
            and a2["alpha_mod_p2"]==179060520,
            "V61 level2 source and half-range changed")
    require(a2["a2_n2_mod_p2"]==1199*P==19460969,
            "level2 analytic coefficient changed")
    inv4=pow(4*128*128,-1,P)
    require(inv4==9362,"wrong quadratic correction factor")
    correction=j["J"]*inv4%P
    require(correction==8335,"wrong J correction")
    expected=(a2["a2_n2_mod_p2"]+P*correction)%P2
    require(expected==154746354 and expected//P==9534,
            "wrong conditionally inferred level3 coefficient")
    require(a2["a2_n3_mod_p2_CONDITIONAL"]==expected,
            "V61 conditional level3 result mismatch")
    print("FINAL_CERT_LEVEL3_SOURCE_IDENTITY_CONDITIONAL_PASS",
          "J",j["J"],"A2_n2",a2["a2_n2_mod_p2"],
          "A2_n3_mod_p2",expected,flush=True)

    ratio=(1930*(1-pow(128,-1,P))**2)%P
    require(ratio==9534,"p-adic regulator residue disagrees")
    require((9534*pow(ratio,-1,P))%P==1,
            "conditional p-adic quotient not one modulo p")
    print("FINAL_CERT_QUOTIENT_UNIT_CONDITIONAL_PASS",
          "v_p=0","first_digit=1",flush=True)

    gate=(ROOT/"results/kato389_sage10_9_terminal_pass_2026-10-19.md").read_text()
    require("KATO389_LOCAL_RANK2_SURJECTIVE_ORDINARY_PASS" in gate
            and "KATO389_NORMALIZATION_LEVEL3_PRECISION_PASS ['+Infinity', '2', '2']" in gate
            and "KATO389_ARITHMETIC_GATE_PASS" in gate
            and "Sha.p_primary_bound(16231) NOT called" in gate,
            "Sage theorem prerequisite evidence missing")
    # These are reported test outputs, not a programmatically proved theorem.
    print("FINAL_CERT_KATO_SAGE_GATES_REPORTED_PASS",flush=True)

    source=(ROOT/"results/c01_all_32658784_shapiro_transports_PASS_2026-10-24.md").read_text()
    require("13306773584111587599" in source
            and "FULL_EXIT_STATUS=0" in source,
            "full Shapiro user-run report is absent")
    local=(ROOT/"results/local_sage_level3_c01_a2_b3_nonzero_kappa_PASS_2026-10-24.md").read_text()
    require("LOCAL_INDEPENDENT_ANALYTIC_C01_BRIDGE_PASS 2 3" in local
            and "EXIT_STATUS=0" in local,"nonzero-kappa analytic oracle absent")
    print("FINAL_CERT_CROSSCHECK_REPORTS_PRESENT_PASS",flush=True)
    print("FINAL_CERT_ARCHIVED_EVIDENCE_AND_ARITHMETIC_PASS",flush=True)
    print("CONDITIONAL_THEOREM: If historical C01 exactly evaluates J_ref, "
          "then Sha(389a1/Q)[16231^infinity]=0 by Sage's proved p-primary bound.")
    print("PUBLICATION_BOUNDARY: no full independent producer replay, "
          "no direct lp.series(n=3), no direct p_primary_bound(16231); "
          "no exact u_p=1 or full BSD theorem.")

if __name__=="__main__":
    main()
