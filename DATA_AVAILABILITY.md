# Data availability and archiving plan

Large V19 outputs (approximately 514,511 sparse TSV chunks; 4,019 checkpoint states), V54/V61 records, and V65 intermediate reference tables are **not** included in the starter Git repository. Neither historical checksum manifests nor the source snippets re-create the missing data.

The V19 terminal state has 2 * 1,087,544 unsigned-16-bit coordinates, 4,350,176 bytes, and expected SHA-256 `5ebeffa2fd67fe2eb54ce6a925bd21dfb850ed9616f9462dce330f98a5a9da1e`.

Recommended data release:

1. Freeze metadata: tool versions, machine architecture, signed release tag, all SHA-256 digests and complete interval coverage manifest.
2. Create content-addressed, reproducible archive shards from the already verified historical files, without recomputing C01 and without copying credentials or personal home-directory configuration.
3. Publish archive(s) separately (e.g. Zenodo with DOI), after verifying storage quota. Link exact archive checksums and persistent identifiers from this repository.
4. Keep separate independently regenerated reference outputs, clearly distinguished from production inputs.

Do not store SSH private keys, GitHub tokens, password files, unrelated research archives or unreviewed backup directories in any archive, even before making it public.