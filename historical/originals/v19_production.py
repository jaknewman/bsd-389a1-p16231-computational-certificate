from pathlib import Path
from array import array
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, os, subprocess, sys, time

assert sys.byteorder == "little"
P = 16231
N = 67 * (P + 1)
STEP = 512
BLOCK = 65536
TOTAL = P * (P - 1)
SEED = 131072
ROOT = Path.home() / "bsd389-c01-v14-production"
CHUNKS = ROOT / "chunks"
LOGS = ROOT / "logs"
CHECK = ROOT / "v19_checkpoints"
BIN = Path.home() / "bsd389-c01-v11-test/bsd389_c01_v11_aggregated"
EXPORT = Path.home() / "bsd389-portable-c01-v2/data/bsd389_tame_relation_export_p16231.json"
EXPECTED = "31fe2b3675d723b372160683e1e8693f30a24d1a9254010a5f388d0ac4f27c63"

for d in (CHUNKS, LOGS, CHECK):
    d.mkdir(parents=True, exist_ok=True)

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

assert digest(BIN) == EXPECTED, "V11 binary mismatch"
export_hash = digest(EXPORT)

def paths(L, R):
    name = f"{L}_{R}.tsv"
    return name, CHUNKS / name, CHUNKS / (name + ".sha256")

def verified(L, R):
    name, out, sha = paths(L, R)
    if not (out.is_file() and sha.is_file()):
        return False
    parts = sha.read_text().split()
    return (
        len(parts) == 2
        and parts[1] == name
        and len(parts[0]) == 64
        and digest(out) == parts[0]
    )

def run_chunk(L, R):
    if verified(L, R):
        return
    name, out, sha = paths(L, R)
    tmp = CHUNKS / (name + f".tmp.{os.getpid()}")
    log = LOGS / f"V19_{L}_{R}.log"
    try:
        with log.open("w") as f:
            subprocess.run(
                [str(BIN), str(EXPORT), str(L), str(R), str(tmp)],
                stdout=f, stderr=subprocess.STDOUT, check=True
            )
        assert tmp.is_file(), f"Missing output {L}:{R}"
        os.replace(tmp, out)
        shatmp = sha.with_name(sha.name + ".tmp")
        shatmp.write_text(f"{digest(out)}  {name}\n")
        os.replace(shatmp, sha)
    finally:
        tmp.unlink(missing_ok=True)

def accumulate(c0, c1, L, R):
    assert verified(L, R), f"Unverified chunk {L}:{R}"
    _, out, _ = paths(L, R)
    prev = -1
    with out.open() as f:
        for line in f:
            s, x, y = map(int, line.split())
            assert prev < s < N
            assert 0 <= x < P and 0 <= y < P
            assert x or y
            c0[s] = (c0[s] + x) % P
            c1[s] = (c1[s] + y) % P
            prev = s

def atomic_write(path, data):
    tmp = path.with_name(path.name + f".tmp.{os.getpid()}")
    try:
        with tmp.open("wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)

def save(end, c0, c1):
    raw = c0.tobytes() + c1.tobytes()
    binary = CHECK / f"state_{end}.bin"
    meta = CHECK / f"state_{end}.json"

    atomic_write(binary, raw)
    info = {
        "end": end,
        "p": P,
        "slots": N,
        "binary_sha256": hashlib.sha256(raw).hexdigest(),
        "v11_sha256": EXPECTED,
        "export_sha256": export_hash,
    }
    atomic_write(meta, json.dumps(info, sort_keys=True).encode())
    print("V19_CHECKPOINT_PASS", end, info["binary_sha256"], flush=True)

def recover():
    entries = sorted(
        CHECK.glob("state_*.json"),
        key=lambda p: int(p.stem.split("_")[1]),
        reverse=True
    )
    for meta in entries:
        try:
            m = json.loads(meta.read_text())
            end = m["end"]
            binary = CHECK / f"state_{end}.bin"
            if (m["p"], m["slots"], m["v11_sha256"],
                m["export_sha256"]) != (P, N, EXPECTED, export_hash):
                continue
            raw = binary.read_bytes()
            if len(raw) != 4 * N:
                continue
            if hashlib.sha256(raw).hexdigest() != m["binary_sha256"]:
                continue
            c0 = array("H")
            c1 = array("H")
            c0.frombytes(raw[:2*N])
            c1.frombytes(raw[2*N:])
            assert len(c0) == len(c1) == N
            print("V19_RECOVERED", end, flush=True)
            return end, c0, c1
        except (OSError, ValueError, KeyError, AssertionError):
            continue

    print("V19_BUILDING_SEED", SEED, flush=True)
    c0, c1 = array("H", [0]) * N, array("H", [0]) * N
    for L in range(0, SEED, STEP):
        accumulate(c0, c1, L, L + STEP)
    save(SEED, c0, c1)
    return SEED, c0, c1

def main():
    stop = int(sys.argv[1]) if len(sys.argv) > 1 else TOTAL
    assert SEED <= stop <= TOTAL
    end, c0, c1 = recover()
    assert end <= stop, "Existing checkpoint exceeds requested stop"

    while end < stop:
        nxt = min(end + BLOCK, stop)
        spans = [(L, min(L+STEP, nxt))
                 for L in range(end, nxt, STEP)]
        t0 = time.monotonic()

        print("V19_BLOCK_START", end, nxt, flush=True)
        with ThreadPoolExecutor(max_workers=4) as executor:
            list(executor.map(lambda lr: run_chunk(*lr), spans))

        for L, R in spans:
            accumulate(c0, c1, L, R)

        save(nxt, c0, c1)
        print("V19_BLOCK_SECONDS", round(time.monotonic()-t0, 2),
              flush=True)
        end = nxt

    print("V19_REACHED", end, flush=True)
    if end == TOTAL:
        print("V19_FULL_C01_ACCUMULATION_PASS", flush=True)
    else:
        print("V19_BOUNDED_RUN_PASS", flush=True)

if __name__ == "__main__":
    main()
