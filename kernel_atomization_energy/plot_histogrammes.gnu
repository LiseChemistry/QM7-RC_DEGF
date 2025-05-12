#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 600, 500
set output "Comparison_Methods_ENN_Kernels.svg"
set title "QM7 Database: Evaluation of the performance of SPA^HM (a, b) and ε-SPA^HM"
set xlabel "Type of architecture"
set ylabel "MAE, kcal/mol"
set style data histograms
set style histogram clustered gap 1
set boxwidth 1.0
set style fill solid 1.0 border -1
set grid ytics
unset xtics
set key outside right vertical

plot 'min_MAE.dat' using 2:xtic(2) title 'SPA^HM(a)' linecolor rgb "#FF0000", \
     '' using 3 title 'SPA^HM(b)' linecolor rgb "#CAC7C7", \
     '' using 4 title 'ε-SPA^HM' linecolor rgb "#00A79F", \
     '' using 5 title 'ENN' linecolor rgb "#EC6608", \
#     '' using 6 title 'Laplacian SPA^HM(a)' linecolor rgb "#5C2483", \
#     '' using 7 title 'Laplacian SPA^HM(b)' linecolor rgb "#C8D300"
