#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1500, 1000
set output 'hyperparam_map_S_SPAHM(a)all_splits.svg'

set xlabel "eta"
set ylabel "sigma"
#set logscale x 1.5
#set logscale y 3
set palette defined (0 "blue", 1 "green", 2 "yellow", 3 "red")

set view map
set size ratio -1
set colorbox

set dgrid3d 30,30
set pm3d map

set multiplot layout 2,3 title "Hyperparameter Map of SPA^HM(a) of S : All Splits" font ",14"

set title "Split 1"
splot "gaussian/results/gaussian_hyperparam_S_a_spahm_split_1.txt" using 3:4:1 with pm3d

set title "Split 2"
splot "gaussian/results/gaussian_hyperparam_S_a_spahm_split_2.txt" using 3:4:1 with pm3d

set title "Split 3"
splot "gaussian/results/gaussian_hyperparam_S_a_spahm_split_3.txt" using 3:4:1 with pm3d

set title "Split 4"
splot "gaussian/results/gaussian_hyperparam_S_a_spahm_split_4.txt" using 3:4:1 with pm3d

set title "Split 5"
splot "gaussian/results/gaussian_hyperparam_S_a_spahm_split_5.txt" using 3:4:1 with pm3d

unset multiplot
