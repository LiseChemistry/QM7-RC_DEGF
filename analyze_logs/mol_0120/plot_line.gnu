#!/home/calvino/.local/bin/gnuplot

set term svg size 1200,600 noenhanced
set output "SCF_energies.svg"

set multiplot layout 1,2 title "Monitoring mol_0120"


set title "SCF_energies"
plot 'SCF_energies.txt' u 1:2 w l lc 'blue' noti, '' u 1:2 w p lc 'red' pt 7 noti


set title "Optimization steps SCF energies"
plot 'optimiation_energies.txt' u 1:2 w l lc 'blue' noti, '' u 1:2 w p lc 'red' pt 7 noti



