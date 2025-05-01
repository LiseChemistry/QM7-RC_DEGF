#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,12" size 1500, 500
set output "Comparison_Methods.svg"
set title "QM7 Database: Evaluation of the performance of SPA^HM (a, b) and aSLATM"
set xlabel "Atoms"
set ylabel "MAE, a.u."
set style data histograms
set style histogram clustered gap 1
set style fill solid 1.0 border -1
set grid ytics
set key outside right vertical

plot 'min_MAE.dat' using 2:xtic(1) title 'Gaussian aSLATM' linecolor rgb "#FF0000", \
     '' using 3 title 'Gaussian SPAHM(a)' linecolor rgb "#CAC7C7", \
     '' using 4 title 'Gaussian SPAHM(b)' linecolor rgb "#00A79F", \
     '' using 5 title 'Laplacian aSLATM' linecolor rgb "#EC6608", \
     '' using 6 title 'Laplacian SPAHM(a)' linecolor rgb "#5C2483", \
     '' using 7 title 'Laplacian SPAHM(b)' linecolor rgb "#C8D300"
