#!/bin/env gnuplot
 
set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "Atomic_charges_and_Kernels_bSPAHM.svg"
 
set multiplot layout 2,3 title "QM7 Radical Cations - Kernels : SPAHM(b)"
set style fill transparent solid 0.25
unset key
 
set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u." 

set style line 1 lc rgb "red" lw 2 pt 5 ps 0.5
set style line 2 lc rgb "blue" lw 2 pt 5 ps 0.5
 
atoms = "C"
 
do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    unset logscale x
    unset logscale y
 
    stats sprintf("gaussian/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 100) nooutput
    x_min = STATS_min_x
    x_max = STATS_max_x
    y_min = STATS_min_y
    y_max = STATS_max_y

    stats sprintf("myLfast/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 100) nooutput
    x_min = (STATS_min_x < x_min) ? STATS_min_x : x_min
    x_max = (STATS_max_x > x_max) ? STATS_max_x : x_max
    y_min = (STATS_min_y < y_min) ? STATS_min_y : y_min
    y_max = (STATS_max_y > y_max) ? STATS_max_y : y_max

    y_min = (y_min <= 0) ? 1e-3 : y_min

    set xrange [x_min:x_max]
    set yrange [y_min:y_max]

    unset xtics
    set xtics auto
    set grid xtics
    set title sprintf("%s", atom)

    set logscale y 3 
    set logscale x 1.5
 
    plot sprintf("gaussian/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "red" notitle, \
         sprintf("gaussian/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
         sprintf("myLfast/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "blue" notitle, \
         sprintf("myLfast/mean_MAE_%s_b_spahm.txt", atom) using 1:($2 * 100) with linespoints ls 2 title "Laplacian"
}
 
unset multiplot
set output
set terminal
