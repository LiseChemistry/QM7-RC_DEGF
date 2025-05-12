#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "Atomic_charges_and_best_kernel.svg"
set title "QM7 Radical Cations - Best Kernel Functions"
set style fill transparent solid 0.25
set key
set xlabel "Training set size"
set ylabel "MAE, kcal/mol"

set style line 1 lc rgb "#FF0000" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "#00A79F" lw 2 pt 5 ps 0.5
set style line 3 lc rgb "#CAC7C7" lw 2 pt 5 ps 0.5
set style line 4 lc rgb "#C8D300" lw 2 pt 5 ps 0.5

unset grid

plot sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/kernel_atomization_energy/a_spahm/gaussian/mean_MAE_a_spahm_G.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#FF0000" notitle , \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/kernel_atomization_energy/a_spahm/gaussian/mean_MAE_a_spahm_G.txt") using 1:($2) with linespoints ls 1 title "Gaussian - SPAHM(a)", \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/kernel_atomization_energy/b_spahm/gaussian/mean_MAE_b_spahm_G.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/kernel_atomization_energy/b_spahm/gaussian/mean_MAE_b_spahm_G.txt") using 1:($2) with linespoints ls 2 title "Gaussian - SPAHM(b)", \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/kernel_atomization_energy/e_spahm/laplacian/mean_MAE_e_spahm_L.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#C8D300" notitle, \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/kernel_atomization_energy/e_spahm/laplacian/mean_MAE_e_spahm_L.txt") using 1:($2) with linespoints ls 4 title "Laplacian - ε-SPAHM"

set output
set terminal
