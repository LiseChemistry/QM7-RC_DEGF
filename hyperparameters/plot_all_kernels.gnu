#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "Atomic_charges_and_Kernels_aSPAHM.svg"

set multiplot layout 2,3 title "QM7 Radical Cations - Kernels : SPAHM(a)"
set style fill transparent solid 0.25
set key

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."

set style line 1 lc rgb "red" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "blue" lw 2 pt 5 ps 0.5

atoms = "S N O"  

do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    set title sprintf("%s", atom)
    set logscale y 3
    set logscale x 1.5

    plot sprintf("gaussian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "red" notitle, \
         sprintf("gaussian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
         sprintf("myLfast/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "blue" notitle, \
         sprintf("myLfast/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 100) with linespoints ls 2 title "Laplacian"
}

set title "C"

plot sprintf("gaussian/results/gaussian_MAE_C_a_spahm_split_4.txt", atom) using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "red" notitle, \
     sprintf("gaussian/results/gaussian_MAE_C_a_spahm_split_4.txt", atom) using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_C_a_spahm.txt", atom) using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "blue" notitle, \
     sprintf("myLfast/mean_MAE_C_a_spahm.txt", atom) using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset multiplot
set output
set terminal
