# Reported Magma 3-descent — user supplied on 2026-11-27

Curve: y^2+y=x^3+x^2-2*x, conductor 389.

```text
3-division polynomial is not integral; scaling equation of E.
Bad prime 389 --> c_389 = 1
Bad primes for 3-descent: [ 3 ]
Computing KS3 for Number Field with defining polynomial of degree 8 ...
Rank = 7
Finding the kernel of the norm:
 ... norm kernel has rank 3
A(S, 3) (the kernel of the norm) has dimension 3
Finding local image for p = 3 ...
 dim E(Q_3)[3] = 0
 p-adic precision at p = 3 is 114
 Total local image should have dimension 1
 Finished finding local points at 3.
 Dimension of local image = 1 = expected dimension.
Local conditions at 3 -> dimension = 2
Final step (involving the algebra B)
Final step: testing cubeness in B using at least 10 primes
Final step: verifying cubeness in B
Restriction to kernel of map to B^*/(B^*)^3 -> dimension = 2
BSD389_3SELMER_ORDER 9
BSD389_3SELMER_INVARIANTS [ 3, 3 ]
BSD389_SHA_3_PRIMARY_ZERO_PASS
```

The `Rank = 7` line belongs to a descent auxiliary module, **not** `rank E(Q)`. Source is the user's pasted run, not a separately repeated execution.
