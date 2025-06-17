#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,14" size 1600,600
set output "atomic_charges_kernel_histogram.svg"
set title "QM7*-RC: Atomic Hirshfeld Charges"
set style data histograms
set style histogram clustered gap 2
set boxwidth 1.0
set style fill solid border -1
set grid ytics
set xlabel "Atom"
set ylabel "MAE (a.u.)"
set key outside top right
set key spacing 1.2
set key samplen 1
set xtics
set style fill solid 1.0 noborder

plot 'min_MAE_kernels.dat' using 2:xtic(1) title "aSLATM - Gaussian" fillstyle pattern 2 lc rgb "#FF0000", \
     '' using 3 title "aSLATM - Laplacian" lc rgb "#FF0000", \
     '' using 4 notitle lc rgb "#FF0000", \
     '' using 5 title "SPA^HM(a) - Gaussian" fillstyle pattern 2 lc rgb "#CAC7C7", \
     '' using 6 title "SPA^HM(a) - Laplacian" lc rgb "#CAC7C7", \
     '' using 7 notitle fillstyle empty border rgb "#CAC7C7", \
     '' using 8 title "SPA^HM(b) - Gaussian" fillstyle pattern 2 lc rgb "#00A79F", \
     '' using 9 title "SPA^HM(b) - Laplacian" lc rgb "#00A79F"
