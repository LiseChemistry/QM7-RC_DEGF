#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "Atomic_charges_and_Kernels_SLATM(a).svg"

set multiplot layout 2,3 title "QM7 Radical Cations - Kernels : SLATM(a)"
set style fill transparent solid 0.25

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u." 

set style line 1 lc rgb "red" lw 2 pt 7 ps 0.5
set style line 2 lc rgb "blue" lw 2 pt 7 ps 0.5

set log y 3
set log x 1.5

atoms = "C O S N"

do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    set grid
    set title sprintf("%s", atom)

    plot sprintf("gaussian/mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "red" notitle, \
         sprintf("gaussian/mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian", \
         sprintf("laplacian/mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "blue" notitle, \
         sprintf("laplacian/mean_MAE_%s_a_slatm.txt", atom) using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian"
}

unset multiplot
set output
set terminal
