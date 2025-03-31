set terminal svg enhanced font "Latin Modern Roman,12" size 1600, 1200
set output "Atomic_charges_and_Kernels_aSPAHM.svg"

set multiplot layout 3,2 title "QM7 Radical Cations - Kernels"

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."
set grid

set style line 1 lc rgb "red" lw 2 pt 7 ps 2
set style line 2 lc rgb "blue" lw 2 pt 7 ps 2
set style line 3 lc rgb "red" lw 1 pt 7 ps 1.5
set style line 4 lc rgb "blue" lw 1 pt 7 ps 1.5

set logscale y

atoms = "C O S N"

do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    set title sprintf("%s", atom)

    plot sprintf("gaussian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2):($3 * 10**2) with yerrorbars ls 3 notitle, \
         sprintf("gaussian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 1 title "Gaussian", \
         sprintf("laplacian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2):($3 * 10**2) with yerrorbars ls 4 notitle, \
         sprintf("laplacian/mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 2 title "Laplacian"
}

unset multiplot
set output
set terminal
