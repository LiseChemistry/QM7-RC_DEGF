#!/bin/env gnuplot

set terminal pngcairo enhanced font "Latin Modern Roman,12" size 1300,800
set output "target_predicted_values_S_aSLATM.png"

set title "Target and Predicted Values - SLATM(a) : S"
set xlabel "Target values"
set ylabel "Predicted values"
set grid

set logscale x y

plot "gaussian/results/gaussian_target_pred_S_a_slatm_split_1.txt" using 1:2 with points pt 7 lc rgb "red" title "Split 1"

set output
set terminal
