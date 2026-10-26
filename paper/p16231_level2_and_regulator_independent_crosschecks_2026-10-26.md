# BSD389 p=16231 — new independent audits of level-2 coefficient and regulator

Date: 2026-10-26. **SOURCES WRITTEN, NOT YET EXECUTED ON IONOS.**

## A. Second level-2 coefficient by direct cyclotomic indexing

The old V61 program enumerates x=a+p*b and recovers the cyclotomic exponent u through the Fermat quotient Q_p(a). The new script `verification/independent_p16231_level2_u_enumeration.py` starts with u directly. For each 1<=a<=8115, construct the Teichmuller lift omega(a) mod p² as a^p mod p², and then x(a,u)=omega(a)*(1+p*u) mod p². Since (1+p)^u=1+p*u mod p² and omega(a)^(p-1)=1 mod p², this enumerates exactly once every residue with fixed a mod p and exponent u.

Let m be Sage's plus eclib modular symbol with `L_ratio` normalization. The new sums are

`R2 = sum_(a=1)^8115 sum_(u=2)^(p-1) binom(u,2)*m(x(a,u)/p²) mod p²`,

`R1 = sum_(a=1)^8115 m(a/p) mod p²`.

The pairing a with p-a uses the evenness of the plus modular symbol and cancels the 1/2 real-components divisor. If alpha is the Frobenius unit root modulo p², Sage's n=2 coefficient is

`A2^(2) = alpha^-2 * ( R2 - alpha^-1*binom(p,3)*R1 ) mod p²`.

The previously obtained value was `R2=79629286`, `R1=0`, `A2^(2)=19460969=1199p (mod p²)`, but the new script **does not read those values** as input: it directly calls Sage/eclib on x(a,u)/p² and computes independent per-a checksummed JSON records.

The first execution can cover one complete a row (16229 symbol calls), then the full first 32-a block (519328 symbols), which it compares **after the computation** with old V61's first checkpoint. Finally, the optional `all` mode independently enumerates the entire 131714565 half-domain (only u>=2 triggers eclib evaluations) and compares the output. The `all` run is potentially expensive and can resume at the previous per-a checkpoint.

Boundary: V61 and the new independent indexing both rely on Sage/eclib for the underlying normalized modular symbol; the new calculation is independent of the Fermat-quotient enumeration, old checkpoint accumulator, and V61 numerical outcomes.

## B. Second regulator from a different height algorithm

Sage 10.9's `E.padic_regulator(p)` uses the determinant of `padic_height_pairing_matrix`, whose default height routine is `E.padic_height(p)` (sigma-series algorithm). Sage 10.9 also implements `E.padic_height_via_multiply(p)`, a separate multiplication-based height algorithm. The new `verification/independent_p16231_regulator_two_height_algorithms.py` explicitly evaluates the basis heights h(P), h(Q), h(P+Q), h(P-Q) with *both* methods, checks the parallelogram law, constructs the polarization matrix and its determinant modulo p^5 separately, and requires agreement.

For rank two, the pairing is `H11=h(P)`, `H22=h(Q)`, `H12=(h(P+Q)-h(P)-h(Q))/2`, with `Reg_p=H11*H22-H12^2`.

Expected prior leading residue: `Reg_p/p³=1930 mod p`. With good ordinary alpha=128 mod p and log(1+p)/p=1 mod p, `B_p/p = 1930*(1-128^-1)^2 = 9534 mod p`. The new code must *compute* these values, and can fail if either height algorithm disagrees.

Boundary: the two algorithms have distinct Sage height computations, but still share Sage rational elliptic curve arithmetic and p-adic field routines. This is not an external independently written regulator library.

## Commands on the user's activated Sage IONOS shell

```bash
cd ~/bsd-389a1-p16231-computational-certificate
git pull --ff-only
set -o pipefail

python -u verification/independent_p16231_regulator_two_height_algorithms.py 2>&1 | tee ~/bsd389_regulator_two_height_algorithms.log
echo "REGULATOR_STATUS=${PIPESTATUS[*]}"

python -u verification/independent_p16231_level2_u_enumeration.py pilot 2>&1 | tee ~/bsd389_level2_u_pilot.log
echo "LEVEL2_PILOT_STATUS=${PIPESTATUS[*]}"

python -u verification/independent_p16231_level2_u_enumeration.py first-block 2>&1 | tee ~/bsd389_level2_u_first_block.log
echo "LEVEL2_BLOCK_STATUS=${PIPESTATUS[*]}"
```

Once all local checks pass, optional full-run command:

```bash
python -u verification/independent_p16231_level2_u_enumeration.py all 2>&1 | tee -a ~/bsd389_level2_u_full.log
echo "LEVEL2_FULL_STATUS=${PIPESTATUS[*]}"
```

The intended success markers, **not yet observed**, are `BSD389_REGULATOR_ALTERNATE_HEIGHT_METHODS_PASS`, `INDEPENDENT_U_FIRST_BLOCK_V61_AGREEMENT_PASS` and only after the complete all-run `INDEPENDENT_U_FULL_LEVEL2_1199P_PASS`. Do not record PASS from writing scripts alone.
