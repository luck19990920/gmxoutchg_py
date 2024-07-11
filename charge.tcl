set sel [atomselect top all]
set natom [$sel num]
set rdchg [open "charge.txt" r]
set chglist {}
for {set iatm 0} {$iatm<=[expr $natom-1]} {incr iatm} {
gets $rdchg line
scan $line "%f" chg
lappend chglist $chg
}
$sel set charge $chglist
close $rdchg