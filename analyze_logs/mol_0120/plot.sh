#!/bin/bash


tot=$(grep -E "^\s*E=" mol_0120.log | cut -d " " -f 3 | wc -l)

grep -E "^\s*E=" mol_0120.log | cut -d " " -f 3 > tmpvalues
seq $tot > tmpindices

paste tmpindices tmpvalues > ./SCF_energies.txt
rm tmpvalues tmpindices

tot=$(grep "SCF Done" mol_0120.log | wc -l)
grep "SCF Done" mol_0120.log | cut -d " " -f 8 > tmpvalues
seq $tot > tmpindices

paste tmpindices tmpvalues > ./optimiation_energies.txt
rm tmpvalues tmpindices

gnuplot ./plot_line.gnu


