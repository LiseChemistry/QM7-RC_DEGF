#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,14" size 1300, 800
set output "At_energy_Kernels_aspahm_mixed_data.svg"
set title "{/:Bold QM7^*-RC/2 + QM7/2: Atomization Energy for the SPA^HM(a)}"
set style fill transparent solid 0.25
set key
set xlabel "Training set size"
set ylabel "MAE, kcal/mol"
set style line 1 lc rgb "#FF0000" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "#00A79F" lw 2 pt 5 ps 0.5

unset grid
plot sprintf("gaussian/mean_MAE_a_spahm_G.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_a_spahm_G.txt") using 1:($2) with linespoints ls 1 title "Gaussian", \
     sprintf("laplacian/mean_MAE_a_spahm_L.txt") using 1:($2 - $3):($2 + $3) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("laplacian/mean_MAE_a_spahm_L.txt") using 1:($2) with linespoints ls 2 title "Laplacian"

set output
set terminal
