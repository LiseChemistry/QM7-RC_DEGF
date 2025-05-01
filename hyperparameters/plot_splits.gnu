#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "splits_C_SPAHMa.svg"
set key top left 
set multiplot layout 2,3 title "Splits: Atom C - SPA^HM(a)"
set style fill transparent solid 0.25
set xlabel "Training set size"
set ylabel "MAE, 10^{−2} a.u."
set style line 1 lc rgb "#FF0000" lw 2 pt 5 ps 0.5
set log y 2.5
set log x 1.5
unset grid
set xtics (3551,7102,14204,28409)

splits = "1 2 3 4 5"

do for [i=1:words(splits)] {
    split = word(splits, i)

    set title sprintf("%s", split)

    plot sprintf("gaussian/results_Yannick/gaussian_regression_C_a_spahm_split_%s.txt", split) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "#FF0000" notitle, \
         sprintf("gaussian/results_Yannick/gaussian_regression_C_a_spahm_split_%s.txt", split) using 1:($2 * 10**2) with linespoints ls 1 title "SPA^HM(a)"
}

unset multiplot
set output
set terminal
