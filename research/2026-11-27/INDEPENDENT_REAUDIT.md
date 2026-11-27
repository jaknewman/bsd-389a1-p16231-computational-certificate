# Independent re-audit — 27 November 2026

**Status: code and finite calculations checked; the implications to the Selmer group and full BSD have different validation requirements.**

## Reproduced locally in this conversation

1. Ran the exact 390-entry Manin relation/Hecke certificate, which reported the same SHA-256 and the 1170 Manin, 1307 T2, and 2643 T3/T5/T7 checks.
2. Ran the original independent Python and native C++ p=389 cyclotomic programs. Both returned \`[0,0,0,321,102,102]\` for the first six coefficients and exact \`U_389\` distribution at all 388 nonzero residue classes.
3. Ran the native ordinary program for \`p=5,7,11,13,17,89\`; observed \`c2=2,5,2,2,1,8\`, respectively, with \`c0=c1=0\`.
4. Parsed the full manifest: it lists exactly 297 primes in the range 5 to 1999 excluding \`107,389,599,1049\`; counts equal \`p(p-1)\`, all \`c0=c1=0\`, and all \`c2\` are nonzero. This is a *consistency audit* of reported output, not a rerun of all 297 raw sums.
5. Wrote and independently ran the \`verification/bsd389_standalone_p2_audit.py\` program with a relative data path. It reproduces the six ordinary cases above and the p=389 leading moment 321, using Python standard library only.

## Primary-source scope check

* Christian Wuthrich, *On the Integrality of Modular Symbols and Kato's Euler System for Elliptic Curves* (Documenta Math. 19, 2014), Corollary 19: ordinary semistable \`char_\Lambda(X)\mid (L_p)\`; split multiplicative \`I \cdot char_\Lambda(X)\mid (L_p)\`. Verify the exact tame-character projection before reusing the latter.
* Ralph Greenberg, *Iwasawa Theory for Elliptic Curves* (1998), Proposition 4.15: under \`Lambda\`-cotorsion and mild local ramification/reduction assumptions, the classical Selmer has no proper finite-index \`Lambda\`-submodule (dually: no nonzero finite \`Lambda\`-submodule).
* The ordinary level-\`p^2\` distribution correction is crucial. Do not identify the **raw modular-symbol** Taylor coefficient with the fully normalized \`p\`-adic \`L\` coefficient without checking the unit-root stabilization and tame-character projection.

## Explicit reproducibility fix

The independent Python script in the earlier ZIP archive used a hard-coded \`/mnt/data/bsd389_verify/...\` import path; it would not run directly from a GitHub checkout. The new \`verification/bsd389_standalone_p2_audit.py\` uses only relative paths and is checked with the included \`manin_390.txt\` file.

## Pending proof reviews

- [ ] Independently reproduce the normalizing values of the modular symbol from Sage/eclib; the finite relations alone determine a rational eigenline but not its analytic period normalization.
- [ ] Trace ordinary stabilization through the complete character projection and verify the exact Selmer group and control map in the cited Wuthrich and Greenberg arguments.
- [ ] Check all exceptional-zero normalizations and the full tame-character projection at p=389.
- [ ] Reproduce the 297-prime sweep independently. Current Python confirms a sample; the CSV passes internal checks.
- [ ] Archive the original source scripts and raw logs from remaining ZIP packages.

**No statement here establishes the exact complex leading-term equality or global finiteness of Sha for all primes.**
