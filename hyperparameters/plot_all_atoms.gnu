#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300,800
set output "learning_curves.svg"
set key

set multiplot layout 2,3 title "QM7 Radical Cations - Atomic Charges"
set style fill transparent solid 0.25

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."

set style line 1 lc rgb "red" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "blue" lw 2 pt 5 ps 0.5
set style line 3 lc rgb "green" lw 2 pt 5 ps 0.5
set style line 4 lc rgb "cyan" lw 2 pt 5 ps 0.5

set log y 3
set log x 1.5

atoms = "S N O"

do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    set grid
    set title sprintf("%s", atom)

    plot sprintf("gaussian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
         sprintf("gaussian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "red" notitle, \
         sprintf("myLfast/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian SPA^HM(b)", \
         sprintf("myLfast/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "blue" notitle, \
         sprintf("myLfast/mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2) with linespoints ls 3 title "Laplacian SLATM(a)", \
         sprintf("myLfast/mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "green" notitle
}

set title "C"

plot sprintf("gaussian/results/gaussian_MAE_C_a_spahm_split_4.txt", atom) using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian SPA^HM(a)", \
     sprintf("gaussian/results/gaussian_MAE_C_a_spahm_split_4.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "red" notitle, \
     sprintf("myLfast/mean_MAE_C_b_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian SPA^HM(b)", \
     sprintf("myLfast/mean_MAE_C_b_spahm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "blue" notitle, \
     sprintf("myLfast/mean_MAE_C_a_slatm.txt", atom) using 1:($2 * 10**2) with linespoints ls 3 title "Laplacian SLATM(a)", \
     sprintf("myLfast/mean_MAE_C_a_slatm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "green" notitle

unset multiplot
set output
set terminal
