#!/bin/env gnuplot

atom = ARG1
rep = ARG2

set terminal svg enhanced font "Latin Modern Roman,12" size 1300,800
set output sprintf("target_predicted_values_%s_%s.svg", atom, rep)
unset key
set multiplot layout 2,3

set title sprintf("Target and Predicted Values : %s, %s", atom, rep)
set xlabel "Target values"
set ylabel "Predicted values"
set grid

do for [i=1:5] {
    filename = sprintf("gaussian/results/gaussian_target_pred_%s_%s_split_%d.txt", atom, rep, i)

    stats filename using 1:2 name "S" nooutput

    slope = S_slope
    intercept = S_intercept
    r2 = S_correlation**2

    set label 1 sprintf("R² = %.4f", r2) at graph 0.05, 0.9 front

    plot filename using 1:2 with points pt 7 lc rgb "red" title sprintf("Split %d", i), \
         slope * x + intercept with lines lw 2 lc rgb "black" title "Régression"

    unset label 1
}

unset multiplot
set output
set terminal
