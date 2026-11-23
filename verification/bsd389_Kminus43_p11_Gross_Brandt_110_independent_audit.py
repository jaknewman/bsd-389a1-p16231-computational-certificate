#!/usr/bin/env python3
"""Independent audit of the 110 genuine Gross-Brandt checkpoint for 389a1.

No Sage dependency; this script REAGGREGATES verified Brandt weights from
the Sage-created JSON. It does not reproduce quaternion isomorphisms,
the 33-class ideal equivalences or their recorded witnesses.

Usage:
 python verification/bsd389_Kminus43_p11_Gross_Brandt_110_independent_audit.py \
   ~/bsd389_Kminus43_p11_Gross_Brandt_110.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

P, MOD = 11, 121
V = (
    0,0,0,1,-1,1,-1,-1,1,-1,-1,-1,0,0,1,-1,-1,0,0,
    2,2,1,0,0,0,1,1,-2,1,-2,-2,2,0
)


def audit(checkpoint: dict) -> dict:
    assert checkpoint["curve"] == "389a1"
    assert checkpoint["K_disc"] == -43 and checkpoint["p"] == P
    assert checkpoint["status"] in (
        "PARTIAL_110_GENUINE_BRANDT",
        "ALL_110_GENUINE_BRANDT_WEIGHTS_COMPUTED",
    )
    assert len(V) == 33
    assert 0 <= checkpoint["base_index"] < 33
    assert isinstance(checkpoint["gamma"], str) and checkpoint["gamma"]
    records = {int(k): v for k, v in checkpoint["records"].items()}
    assert len(records) <= 110
    assert all(0 <= k < 110 for k in records)
    assert len(records) == len(checkpoint["records"])
    slope_set = set()
    source_set = set()
    moments = [0, 0, 0]
    for k, rec in sorted(records.items()):
        b = pow(39, k, MOD)
        a = b * pow(45, -1, MOD) % MOD
        i = (k - 4) % P
        j = rec["index"]
        assert 0 <= j < len(V)
        assert rec["slope"] == b
        assert rec["source_parameter"] == a
        assert rec["principal_exponent"] == i
        assert rec["brandt_weight"] == V[j]
        assert isinstance(rec["right_equivalence_witness"], str)
        assert rec["right_equivalence_witness"]
        assert a % P and b % P
        assert b not in slope_set and a not in source_set
        slope_set.add(b)
        source_set.add(a)
        moments[0] = (moments[0] + V[j]) % P
        moments[1] = (moments[1] + i*V[j]) % P
        moments[2] = (moments[2] + (i*(i-1)//2)*V[j]) % P

    canonical = json.dumps(
        {str(k): records[k] for k in sorted(records)},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    ).encode("utf-8")
    report = {
        "count": len(records),
        "total": 110,
        "canonical_record_sha256": hashlib.sha256(canonical).hexdigest(),
        "partial_moments_mod11": moments,
        "partial_theta2_contribution_mod11": 2*moments[2] % P,
        "complete": len(records) == 110,
    }
    if len(records) != 110:
        assert checkpoint["status"] == "PARTIAL_110_GENUINE_BRANDT"
        report["status"] = "PARTIAL_ONLY__DO_NOT_INFER_THETA_NONVANISHING"
        return report

    assert slope_set == {a for a in range(MOD) if a % P}
    assert source_set == slope_set
    assert checkpoint["status"] == "ALL_110_GENUINE_BRANDT_WEIGHTS_COMPUTED"
    assert [int(x) for x in checkpoint["moments_mod11"]] == moments

    # An independent regrouping: use the source's 10 Teichmuller units and
    # 11 principal units, not the Gross script's k -> i(k) accumulation.
    log39 = {pow(39,k,MOD): k for k in range(110)}
    assert len(log39) == 110
    tau = pow(2,P,MOD)     # 2 mod 11 is a generator of F_11^*
    assert len({pow(tau,j,MOD) for j in range(10)}) == 10
    assert pow(12,11,MOD) == 1
    by_i = []
    covered = set()
    for i in range(P):
        gross_values = []
        for j in range(10):
            a = (pow(tau,j,MOD)*pow(12,i,MOD))%MOD
            b = (45*a)%MOD
            k = log39[b]
            assert k not in covered
            assert records[k]["principal_exponent"] == i
            covered.add(k)
            gross_values.append(records[k]["brandt_weight"])
        by_i.append(sum(gross_values))
    assert len(covered) == 110
    independent_moments = [
        sum(by_i)%P,
        sum(i*by_i[i] for i in range(P))%P,
        sum((i*(i-1)//2)*by_i[i] for i in range(P))%P,
    ]
    assert independent_moments == moments
    theta2 = -pow(-4%P, -2, P)*moments[2]%P
    assert theta2 == (2*moments[2])%P
    assert checkpoint["theta2_mod11_up_to_JL_unit"] == theta2
    assert checkpoint["theta2_unit"] is bool(theta2)
    assert sum(i*(i-1)//2 for i in range(P))%P == 0
    report.update(
        status="ALL_110_INDEPENDENT_MOMENTS_PASS",
        moments_mod11=moments,
        theta2_mod11_up_to_JL_unit=theta2,
        theta2_unit=bool(theta2),
        grouped_weight_sums_mod11=[s%P for s in by_i],
        caveat="This audits the JSON arithmetic; Sage equivalences still rely on the source's certificates.",
    )
    return report


def self_test():
    seed = {
        "curve":"389a1", "K_disc":-43,"p":11,
        "status":"PARTIAL_110_GENUINE_BRANDT",
        "base_index":18,"gamma":"TEST_ONLY",
        "records":{
          "0":{"slope":1,"source_parameter":78,"principal_exponent":7,
                "index":16,"brandt_weight":-1,
                "right_equivalence_witness":"TEST_ONLY"},
          "1":{"slope":39,"source_parameter":19,"principal_exponent":8,
                "index":23,"brandt_weight":0,
                "right_equivalence_witness":"TEST_ONLY"},
        },
    }
    # Derive actual source parameters independently rather than hardcode:
    for k in (0,1):
        seed["records"][str(k)]["source_parameter"] = (
            pow(39,k,MOD)*pow(45,-1,MOD) % MOD
        )
    result = audit(seed)
    assert result["count"] == 2
    assert result["partial_theta2_contribution_mod11"] == 2
    print("PILOT_2_RECORD_REAGGREGATION_PASS", result["partial_moments_mod11"])
    print("SELF_TEST_PASS__NO_NEW_GROSS_CERTIFICATION")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path, nargs="?")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    if args.self_test:
        self_test()
    if args.checkpoint is None:
        if not args.self_test:
            parser.error("Provide checkpoint filename or --self-test")
        return
    payload=json.loads(args.checkpoint.read_text(encoding="utf-8"))
    result=audit(payload)
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
