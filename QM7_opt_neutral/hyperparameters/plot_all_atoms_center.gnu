#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,16" size 1600,1000
set output "learning_curves.svg"
set key
set style fill transparent solid 0.25
set lmargin 0
set tmargin 4
set style line 1 lc rgb "#FF0000" lw 2 pt 11 ps 0.8
set style line 2 lc rgb "#00A79F" lw 2 pt 13 ps 0.8
set style line 3 lc rgb "#CAC7C7" lw 2 pt 7 ps 0.8
set key font "Latin Modern Roman,16"
set key at screen 0.2, 0.40 
set format y "%.2f"
w = 0.28
h = 0.38
set multiplot title "{/:Bold QM7^*-RC/2 + QM7/2: Atomic Hirshfeld Charges}"

init_plot(pos_x, pos_y, titre) = \
    sprintf("unset tmargin; unset bmargin; unset lmargin; unset rmargin; \
             set size %f,%f; set origin %f,%f; \
             unset colorbox; \
             set xlabel 'Training set size' font 'Latin Modern Roman,14' offset 0,0.5; \
             set ylabel 'MAE, a.u.' font 'Latin Modern Roman,14' offset 1,0; \
             set xtics font 'Latin Modern Roman,14' offset 0,0; \
             set ytics font 'Latin Modern Roman,14' offset 0,0; \
             set title '{/:Bold %s}' font 'Latin Modern Roman,14' offset 0,-0.5; \
             set log y 2.5; set log x 1.5; \
             set border lw 1; \
             set object 1 rect from graph 0,0 to graph 1,1 front fs empty border lc rgb 'black'", \
             w, h, pos_x, pos_y, titre)

eval(init_plot(0.25, 0.55, "{/:Bold S}"))
set xtics (3,7,14,28)
plot \
    sprintf("laplacian/mean_MAE_S_a_spahm.txt") using 1:($2) with linespoints ls 1 notitle "SPA^HM(a)", \
    sprintf("laplacian/mean_MAE_S_a_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#FF0000" notitle, \
    sprintf("laplacian/mean_MAE_S_b_spahm.txt") using 1:($2) with linespoints ls 2 notitle "SPA^HM(b)", \
    sprintf("laplacian/mean_MAE_S_b_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#00A79F" notitle, \
    sprintf("laplacian/mean_MAE_S_slatm.txt") using 1:($2) with linespoints ls 3 notitle "aSLATM", \
    sprintf("laplacian/mean_MAE_S_slatm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#CAC7C7" notitle

eval(init_plot(0.55, 0.55, "{/:Bold N}"))
set xtics (448,897,1795,3590)
plot \
    sprintf("laplacian/mean_MAE_N_a_spahm.txt") using 1:($2) with linespoints ls 1 notitle "SPA^HM(a)", \
    sprintf("laplacian/mean_MAE_N_a_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#FF0000" notitle, \
    sprintf("laplacian/mean_MAE_N_b_spahm.txt") using 1:($2) with linespoints ls 2 notitle "SPA^HM(b)", \
    sprintf("laplacian/mean_MAE_N_b_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#00A79F" notitle, \
    sprintf("laplacian/mean_MAE_N_slatm.txt") using 1:($2) with linespoints ls 3 notitle "aSLATM", \
    sprintf("laplacian/mean_MAE_N_slatm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#CAC7C7" notitle

eval(init_plot(0.25, 0.08, "{/:Bold O}"))
set xtics (512,1025,2051,4102)
plot \
    sprintf("laplacian/mean_MAE_O_a_spahm.txt") using 1:($2) with linespoints ls 1 notitle "SPA^HM(a)", \
    sprintf("laplacian/mean_MAE_O_a_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#FF0000" notitle, \
    sprintf("laplacian/mean_MAE_O_b_spahm.txt") using 1:($2) with linespoints ls 2 notitle "SPA^HM(b)", \
    sprintf("laplacian/mean_MAE_O_b_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#00A79F" notitle, \
    sprintf("laplacian/mean_MAE_O_slatm.txt") using 1:($2) with linespoints ls 3 notitle "aSLATM", \
    sprintf("laplacian/mean_MAE_O_slatm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#CAC7C7" notitle

eval(init_plot(0.55, 0.08, "{/:Bold C}"))
set xtics (3727,7454,14909,29819)
plot \
    sprintf("gaussian/mean_MAE_C_a_spahm.txt") using 1:($2) with linespoints ls 1 title "SPA^HM(a)", \
    sprintf("gaussian/mean_MAE_C_a_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#FF0000" notitle, \
    sprintf("gaussian/mean_MAE_C_b_spahm.txt") using 1:($2) with linespoints ls 2 title "SPA^HM(b)", \
    sprintf("gaussian/mean_MAE_C_b_spahm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#00A79F" notitle, \
    sprintf("laplacian/mean_MAE_C_slatm.txt") using 1:($2) with linespoints ls 3 title "aSLATM", \
    sprintf("laplacian/mean_MAE_C_slatm.txt") using 1:($2-$3):($2+$3) with filledcurves lc rgb "#CAC7C7" notitle

unset multiplot
set output
