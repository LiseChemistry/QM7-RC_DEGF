#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,14" size 700,500
set output "histogram_repres_atom_en_mixed_data.svg"

set title "QM7^*-RC/2 + QM7/2: Atomization Energy"
set xlabel "Type of representation"
set ylabel "MAE, kcal/mol"

set style data histograms
set style histogram rowstacked
set boxwidth 0.7
set style fill solid 1.0 border -1
set grid ytics
set rmargin 20
set key outside right vertical
unset xtics
set datafile separator whitespace

plot 'min_MAE.dat' using 3:xtic(1) title "SPA^HM(a)" lc rgb "#CAC7C7", \
     '' using 4 title "SPA^HM(b)" lc rgb "#00A79F", \
     '' using 5 title "ε-SPA^HM"  lc rgb "#C8D300", \
     '' using 2 title "aSLATM"    lc rgb "#FF0000"
