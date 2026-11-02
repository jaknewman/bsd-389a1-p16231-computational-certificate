#!/usr/bin/env python3
"""Fast p=107 joint-provenance gate: exact MW local certificate + OLD Kurihara archive.

This does NOT re-run the 71-billion term full Kurihara computation.
It reads the user's NEW true run canonical local JSON, checking SHA256
3d9f..., and checks SHA256 of the previously frozen complete p107
Kurihara archive b341.... It asserts exact conductor/admissibility/local
determinant records (369793,383917), matrix [[1,15],[1,53]],
det=38 mod107, q traces 2,-854, and #E(F107)=108.

P107 historical global delta = 34 mod107 comes from that OLD
archive, NOT recalculated by this script. A SHA proves exact file
identity, NOT source-code correctness or a new theorem.
Under independently verified archived Kurihara correctness, saturated
MW rank2, mod107 GL2 surjectivity, p-unit Manin constant and Tamagawa,
and E(Q107)[107]=0, Kim Theorem 1.10 gives Sel(E[107]) = two local
lines. Since the independent MW local matrix has det 38,
the Kummer injection is a bijection and Sha[107]=0, hence
Sha[107^infinity]=0. All conditional external requirements printed.

Use in Ubuntu:
 python -u verification/bsd389_p107_Kim_joint_local_Kurihara_archive_gate.py \
    --output ~/bsd389_p107_joint_Kim_bridge.json
"""
import argparse
import hashlib
import json
from pathlib import Path

P = 107
N = 141969819181
Q = [369793, 383917]
NEW_LOCAL_JSON_SHA256 = "3d9f3b2b6f5594adbc5927794159f5425fb20cd8825ce944b52f3522d1f29e7e"
OLD_K107_ARCHIVE_SHA256 = "b34131819db43fb6b227fa0e769f94b23733270df87dcd6b6dc47ed40693e754"


def digest_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local-json", type=Path,
        default=Path.home() / "bsd389_MW_local_determinants_5_7_107.json"
    )
    parser.add_argument(
        "--k107-archive", type=Path,
        default=Path.home() / "bsd389_k107_certificate_COMPLETE_20261028.tar.gz"
    )
    parser.add_argument(
        "--output", type=Path,
        default=Path.home() / "bsd389_p107_joint_Kim_bridge.json"
    )
    args = parser.parse_args()

    local_path = args.local_json.expanduser()
    archive = args.k107_archive.expanduser()
    assert local_path.is_file(), ("MISSING_NEW_USER_LOCAL_JSON", str(local_path))
    raw = local_path.read_bytes()
    data = json.loads(raw)
    canonical = json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    assert raw == canonical + b"\n", "LOCAL_JSON_IS_NOT_CANONICAL"
    local_sha = hashlib.sha256(canonical).hexdigest()
    assert local_sha == NEW_LOCAL_JSON_SHA256, (
        "LOCAL_JSON_SHA_MISMATCH", local_sha
    )
    print("P107_NEW_MW_LOCAL_JSON_SHA256_EXACT_USER_PASS", local_sha, flush=True)

    assert data["curve"] == "389a1"
    assert data["weierstrass_model"] == [0, 1, 1, -2, 0]
    assert data["MW_points"] == ["(-1,1)", "(0,-1)"]
    p107 = [case for case in data["cases"] if case["p"] == P]
    assert len(p107) == 1
    case = p107[0]
    assert case["auxiliaries"] == Q
    assert Q[0] * Q[1] == N
    assert case["E_Fp_order"] == 108 and case["E_Fp_order"] % P != 0
    assert case["matrix"] == [[1, 15], [1, 53]]
    assert case["det_mod_p"] == 38
    assert case["det_inverse_mod_p"] == 31
    assert case["delta_HISTORICAL_NOT_RECOMPUTED_BY_THIS_PROGRAM"] == 34
    locals_ = case["local_groups"]
    assert len(locals_) == 2
    expected = (
        (369793, 2, 369792, 3456, [1, 15]),
        (383917, -854, 384772, 3596, [1, 53]),
    )
    for item, (q, aq, order, cofactor, row) in zip(locals_, expected):
        assert (item["q"], item["a_q"], item["E_Fq_order"],
                item["cofactor"], item["row"]) == (
                    q, aq, order, cofactor, row
                )
        assert q % P == 1
        assert (aq - q - 1) % P == 0
        assert order % P == 0 and order % (P * P) != 0
    assert (case["matrix"][0][0] * case["matrix"][1][1]
            - case["matrix"][0][1] * case["matrix"][1][0]) % P == 38
    print(
        "P107_MW_KUMMER_LOCAL_DET_EXACT_PASS", "p", P,
        "q", Q, "matrix", case["matrix"], "det", 38,
        "E_F107_order", 108, flush=True
    )

    assert archive.is_file(), (
        "MISSING_OLD_FROZEN_K107_ARCHIVE",
        str(archive),
        "Use --k107-archive if stored elsewhere."
    )
    archive_sha = digest_file(archive)
    assert archive_sha == OLD_K107_ARCHIVE_SHA256, (
        "OLD_KURIHARA_FULL_ARCHIVE_SHA_MISMATCH", archive_sha
    )
    print(
        "P107_FROZEN_KURIHARA_GLOBAL_ARCHIVE_SHA256_PASS",
        archive_sha, flush=True
    )
    print(
        "P107_GLOBAL_KURIHARA_DELTA_34_HISTORICAL_ARCHIVE_INPUT",
        "delta_mod107", 34, "NOT_RECOMPUTED", flush=True
    )
    print(
        "P107_KIM_THEOREM_1_10_EXACT_MODP_SELMER_GATE_CONDITIONAL",
        "rank_MW", 2, "local_dim", 2,
        "needs_valid_delta_algorithm_and_residual_Manin_Tamagawa_hypotheses",
        flush=True
    )
    print(
        "P107_SHA_PRIMARY_ZERO_CONDITIONAL_ON_VERIFIED_KIM_HYPOTHESES",
        "MW_map_determinant", 38,
        "no_global_uniform_SHA_claim", flush=True
    )

    obj = {
        "curve": "389a1",
        "p": P,
        "q": Q,
        "n": N,
        "local_json": str(local_path),
        "local_json_sha256_canonical": local_sha,
        "MW_local_matrix": case["matrix"],
        "MW_local_det_mod107": 38,
        "E_F107_order": 108,
        "historical_archive": str(archive),
        "historical_archive_sha256": archive_sha,
        "historical_delta_mod107_not_computed_here": 34,
        "Kim_modp_localization_and_Sha107": (
            "CONDITIONAL: Validity of the old complete Kurihara archive "
            "and p-integral normalization, proven rank-two saturated MW "
            "basis, residual GL2 surjectivity, p-unit Manin constant "
            "and Tamagawa factors, E(Q107)[107]=0. Kim Thm 1.10 "
            "then implies Sel(E[107]) is the two local lines, "
            "and MW image is a basis; hence Sha[107]=0 and "
            "Sha[107^infinity]=0. This script does not prove these "
            "external theorems or the old Kurihara algorithm."
        )
    }
    encoded = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    target = args.output.expanduser()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(encoded + b"\n")
    print("P107_KIM_JOINT_CANONICAL_JSON_SHA256",
          hashlib.sha256(encoded).hexdigest(), flush=True)
    print("P107_KIM_JOINT_REPORT", target, flush=True)
    print("BOUNDARY_P107_ONLY_AND_EXTERNAL_GLOBAL_DELTA_NOT_RECOMPUTED", flush=True)


if __name__ == "__main__":
    main()
