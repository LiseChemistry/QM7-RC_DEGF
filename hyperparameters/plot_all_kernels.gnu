#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "Atomic_charges_and_Kernels_aslatm.svg"
set multiplot layout 2,3 title "QM7 Radical Cations - Best Kernel Functions: SLATM(a)"
set style fill transparent solid 0.25
set key
set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."
set style line 1 lc rgb "#FF0000" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "#00A79F" lw 2 pt 5 ps 0.5

unset grid
set title "S"
set xtics (29,59,118,177,236)
plot sprintf("gaussian/mean_MAE_S_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_S_a_slatm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_S_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_S_a_slatm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset grid
set title "N"
set xtics (660,1320,2641,3961,5282)
plot sprintf("gaussian/mean_MAE_N_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_N_a_slatm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_N_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_N_a_slatm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset grid
set title "O"
set xtics (595,1190,2380,3570,4760)
plot sprintf("gaussian/mean_MAE_O_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_O_a_slatm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_O_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_O_a_slatm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset grid
set title "C"
set xtics (3551,7102,14204,28409)
plot sprintf("gaussian/mean_MAE_C_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_C_a_slatm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_C_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_C_a_slatm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset grid
set title "H"
set xtics (6149,12299,24599,49199)
plot sprintf("gaussian/mean_MAE_H_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_H_a_slatm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_H_a_slatm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_H_a_slatm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset multiplot
set output
set terminal
