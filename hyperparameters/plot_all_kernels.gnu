set terminal svg enhanced font "Latin Modern Roman,12" size 1200,900
set output "Atomic_charges_and_Kernels.svg"

set multiplot layout 3,2 title "QM7 Radical Cations - Kernels"

set xlabel "Training set size"
set ylabel "MAE, 10−2 a.u."
set grid

set logscale y

set style line 1 lc rgb "red" lw 2 pt 7 ps 1.5
set style line 2 lc rgb "blue" lw 2 pt 7 ps 1.5

atoms = "O S N"

do for [i=1:words(atoms)] {
    atom = word(atoms, i)

    set title sprintf("%s", atom)

    plot sprintf("gaussian_mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 1 title "Laplacian", \
         sprintf("laplacian_mean_MAE_%s_a_spahm.txt", atom) using 1:($2 * 10**2) with linespoints ls 2 title "Gaussian"
}

unset multiplot
set output
set terminal qt
