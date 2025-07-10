#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,14" size 1300, 800
set output "Atomization_energy_best_kernel_mixed_data.svg"
set title "{/:Bold QM7^*-RC/2 + QM7/2: Atomization Energy}"
set style fill transparent solid 0.25
set key
set xlabel "Training set size"
set ylabel "MAE, kcal/mol"

set style line 1 lc rgb "#FF0000" lw 2 pt 5 ps 1
set style line 2 lc rgb "#00A79F" lw 2 pt 11 ps 1
set style line 3 lc rgb "#C8D300" lw 2 pt 13 ps 1
set style line 4 lc rgb "#CAC7C7" lw 2 pt 7 ps 1

unset grid

plot sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_a_spahm/gaussian/mean_MAE_a_spahm_G.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#FF0000" notitle , \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_a_spahm/gaussian/mean_MAE_a_spahm_G.txt") using 1:($2) with linespoints ls 1 title "SPA^HM(a)", \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_b_spahm/gaussian/mean_MAE_b_spahm_G.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_b_spahm/gaussian/mean_MAE_b_spahm_G.txt") using 1:($2) with linespoints ls 2 title "SPA^HM(b)", \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_e_spahm/laplacian/mean_MAE_e_spahm_L.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#C8D300" notitle, \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_e_spahm/laplacian/mean_MAE_e_spahm_L.txt") using 1:($2) with linespoints ls 3 title "ε-SPA^HM", \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_slatm/gaussian/mean_MAE_slatm_G.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#CAC7C7" notitle, \
     sprintf("/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/kernel_atomization_energy/mixed_slatm/gaussian/mean_MAE_slatm_G.txt") using 1:($2) with linespoints ls 4 title "aSLATM"

set output
set terminal
