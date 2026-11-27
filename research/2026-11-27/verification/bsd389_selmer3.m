// Magma 2.30+ full 3-Selmer exact gate. This has NOT been executed here.
// Run: magma bsd389_selmer3.m | tee bsd389_selmer3.log
Q := Rationals();
E := EllipticCurve([ Q | 0,1,1,-2,0 ]);
assert Conductor(E) eq 389;
assert #TorsionSubgroup(E) eq 1;
// Rank 2 and saturated Mordell-Weil basis are separately established.
SetVerbose("Selmer", 2);
S3, map3 := ThreeSelmerGroup(E);
print "BSD389_3SELMER_ORDER", #S3;
print "BSD389_3SELMER_INVARIANTS", Invariants(S3);
assert #S3 ge 9;
if #S3 eq 9 then
    print "BSD389_SHA_3_PRIMARY_ZERO_PASS", "requires certified rank2 and saturation";
else
    print "BSD389_SHA_3_PRIMARY_NOT_DECIDED", "Selmer has extra 3-torsion classes";
end if;