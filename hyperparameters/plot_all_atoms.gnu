#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300,800
set output "learning_curves.svg"
set key

set multiplot layout 2,3 title "QM7 Database - Atomic Charges"
set style fill transparent solid 0.25

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."

set style line 1 lc rgb "#CAC7C7" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "#00A79F" lw 2 pt 5 ps 0.5
set style line 3 lc rgb "#FF0000" lw 2 pt 5 ps 0.5

set log y 2.5
set log x 1.5

set grid
set title "S"
set xtics (29,59,118,177,236)
plot sprintf("gaussian/mean_MAE_S_a_spahm.txt") using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
     sprintf("gaussian/mean_MAE_S_a_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#CAC7C7" notitle, \
     sprintf("gaussian/mean_MAE_S_b_spahm.txt") using 1:($2 * 10**2) with linespoints ls 2 title "Gaussian SPA^HM(b)", \
     sprintf("gaussian/mean_MAE_S_b_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("gaussian/mean_MAE_S_a_slatm.txt") using 1:($2 * 10**2) with linespoints ls 3 title "Gaussian aSLATM", \
     sprintf("gaussian/mean_MAE_S_a_slatm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#FF0000" notitle

set grid
set title "N"
set xtics (660,1320,2641,3961,5282)
plot sprintf("gaussian/mean_MAE_N_a_spahm.txt") using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
     sprintf("gaussian/mean_MAE_N_a_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#CAC7C7" notitle, \
     sprintf("myLfast/mean_MAE_N_b_spahm.txt") using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian SPA^HM(b)", \
     sprintf("myLfast/mean_MAE_N_b_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_N_a_slatm.txt") using 1:($2 * 10**2) with linespoints ls 3 title "Laplacian aSLATM", \
     sprintf("myLfast/mean_MAE_N_a_slatm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#FF0000" notitle

set grid
set title "O"
set xtics (595,1190,2380,3570,4760)
plot sprintf("gaussian/mean_MAE_O_a_spahm.txt") using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
     sprintf("gaussian/mean_MAE_O_a_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#CAC7C7" notitle, \
     sprintf("myLfast/mean_MAE_O_b_spahm.txt") using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian SPA^HM(b)", \
     sprintf("myLfast/mean_MAE_O_b_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_O_a_slatm.txt") using 1:($2 * 10**2) with linespoints ls 3 title "Laplacian aSLATM", \
     sprintf("myLfast/mean_MAE_O_a_slatm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#FF0000" notitle

set grid
set title "C"
set xtics (3551,7102,14204,28409)
plot sprintf("gaussian/results/gaussian_MAE_C_a_spahm_split_4.txt") using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
     sprintf("gaussian/results/gaussian_MAE_C_a_spahm_split_4.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#CAC7C7" notitle, \
     sprintf("myLfast/mean_MAE_C_b_spahm.txt") using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian SPA^HM(b)", \
     sprintf("myLfast/mean_MAE_C_b_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_C_a_slatm.txt") using 1:($2 * 10**2) with linespoints ls 3 title "Laplacian aSLATM", \
     sprintf("myLfast/mean_MAE_C_a_slatm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#FF0000" notitle

set grid
set title "H"
set xtics (6149,12299,24599,49199)
plot sprintf("myLfast/mean_MAE_H_a_spahm.txt") using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
     sprintf("myLfast/mean_MAE_H_a_spahm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#CAC7C7" notitle, \
     sprintf("myLfast/mean_MAE_H_a_slatm.txt") using 1:($2 * 10**2) with linespoints ls 3 title "Laplacian aSLATM", \
     sprintf("myLfast/mean_MAE_H_a_slatm.txt") using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#FF0000" notitle

unset multiplot
set output
