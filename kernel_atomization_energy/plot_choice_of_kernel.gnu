#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,14" size 1100,700
set output "kernels_atom_en.svg"

set title "QM7^*-RC: Atomization Energy"
set xlabel "Representation"
set ylabel "MAE (kcal/mol)"

set style data histograms
set style histogram clustered gap 5
set style fill solid 1.0 border -1
set boxwidth 1.0
set grid ytics
set xtics
set key outside top right

plot 'min_MAE_kernels.dat' using 2:xtic(1) title "Gaussian" lc rgb "#FF0000", \
     '' using 3 title "Laplacian" lc rgb "#00A79F"
