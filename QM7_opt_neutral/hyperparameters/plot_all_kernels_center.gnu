#!/bin/env gnuplot

set terminal svg enhanced font "Latin Modern Roman,16" size 1600, 1000
set output "atomic_charges_kernels_mixed_data_bspahm.svg"
set lmargin 0
set tmargin 4
set style fill transparent solid 0.25
set key
set key font "Latin Modern Roman,16"
set style line 1 lc rgb "#FF0000" lw 2 pt 11 ps 0.8
set style line 2 lc rgb "#00A79F" lw 2 pt 13 ps 0.8
set key at screen 0.2, 0.40 
w = 0.28
h = 0.38

set multiplot title "{/:Bold QM7^*-RC/2 + QM7/2: Atomic Hirshfeld Charges for the SPA^HM(b)}"

init_plot(pos_x, pos_y, titre) = \
    sprintf("unset tmargin; unset bmargin; unset lmargin; unset rmargin; \
             set size %f,%f; set origin %f,%f; \
             unset colorbox; \
             set xlabel 'Training set size' font 'Latin Modern Roman,14' offset 0,0.5; \
             set ylabel 'MAE, 10^{−2} a.u.' font 'Latin Modern Roman,14' offset 1,0; \
             set xtics font 'Latin Modern Roman,14' offset 0,0; \
             set ytics font 'Latin Modern Roman,14' offset 0,0; \
             set title '{/:Bold %s}' font 'Latin Modern Roman,14' offset 0,-0.5; \
             set log y 2.5; set log x 1.5; \
             set border lw 1; \
             set object 1 rect from graph 0,0 to graph 1,1 front fs empty border lc rgb 'black'", \
             w, h, pos_x, pos_y, titre)

############# Line 1 #############

eval(init_plot(0.05, 0.58, "{/:Bold S}"))
set xtics (29,59,118,177,236)
plot sprintf("gaussian/mean_MAE_S_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_S_b_spahm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_S_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_S_b_spahm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

eval(init_plot(0.37, 0.58, "{/:Bold N}"))
set xtics (660,1320,2641,5282)
plot sprintf("gaussian/mean_MAE_N_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_N_b_spahm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_N_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_N_b_spahm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

eval(init_plot(0.69, 0.58, "{/:Bold O}"))
set xtics (595,1190,2380,4760)
plot sprintf("gaussian/mean_MAE_O_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_O_b_spahm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_O_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_O_b_spahm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

############# Line 2 #############

eval(init_plot(0.22, 0.21, "{/:Bold C}"))
set xtics (3551,7102,14204,28409)
plot sprintf("gaussian/mean_MAE_C_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_C_b_spahm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
     sprintf("myLfast/mean_MAE_C_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
     sprintf("myLfast/mean_MAE_C_b_spahm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

eval(init_plot(0.54, 0.21, "{/:Bold H}"))
set xtics (6149,12299,24599,49199)
plot sprintf("gaussian/mean_MAE_H_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#FF0000" notitle, \
     sprintf("gaussian/mean_MAE_H_b_spahm.txt") using 1:($2 * 100) with linespoints ls 1 title "Gaussian", \
#     sprintf("myLfast/mean_MAE_H_b_spahm.txt") using 1:($2 * 100 - $3 * 100):($2 * 100 + $3 * 100) with filledcurves lc rgb "#00A79F" notitle, \
#     sprintf("myLfast/mean_MAE_H_b_spahm.txt") using 1:($2 * 100) with linespoints ls 2 title "Laplacian"

unset multiplot
set output
