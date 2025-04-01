#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1300, 800
set output "C_SPAHM(a).svg"

set multiplot layout 2,3 title "C - SLATM(a) : SPLITS"
set style fill transparent solid 0.25

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."

set style line 1 lc rgb "red" lw 2 pt 7 ps 0.5

set log y 3
set log x 1.5

splits = "1 2 3 4 5"

do for [i=1:words(splits)] {
    split = word(splits, i)

    set grid
    set title sprintf("%s", split)

    plot sprintf("gaussian/results/gaussian_regression_C_a_spahm_split_%s.txt", split) using 1:($2 * 10**2 - $3 * 10**2):($2 * 10**2 + $3 * 10**2) with filledcurves lc rgb "red" notitle, \
         sprintf("gaussian/results/gaussian_regression_C_a_spahm_split_%s.txt", split) using 1:($2 * 10**2) with linespoints ls 1 title "SPAHM(a)"
}

unset multiplot
set output
set terminal
