#!/bin/env gnuplot

atom = ARG1
rep = ARG2

set terminal svg enhanced font "Latin Modern Roman,12" size 1300,800
set output sprintf("gaussian_target_predicted_values_%s_%s.svg", atom, rep)
set key
set multiplot layout 2,3 title sprintf("Target and Predicted Values : %s", atom)
set xlabel "Target values"
set ylabel "Predicted values"
unset grid

do for [i in "1 3 4 5"] {
    filename = sprintf("gaussian/results_Yannick/gaussian_target_pred_%s_%s_split_%d.txt", atom, rep, i)
    set title sprintf("Split %d", i) 
    stats filename using 1:2 name "S" nooutput
    slope = S_slope
    intercept = S_intercept
    r2 = S_correlation**2
    set label 1 sprintf("R² = %.3f", r2) at graph 0.05, 0.9 front

    plot filename using 1:2 with points pt 7 lc rgb "#FF0000" notitle, \
         slope * x + intercept with lines lw 2 lc rgb "#00A79F" notitle 
    unset label 1
}

unset multiplot
set output
set terminal
